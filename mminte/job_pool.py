from multiprocessing import Queue, Process, cpu_count

from .interaction_worker import create_pair_model, compute_growth_rates


class InteractionPool(object):
    """ Base class for interaction analysis multiprocessing job pool. """

    def __init__(self, n_processes=None):
        # Figure out the size of job pool.
        self.n_processes = n_processes
        if n_processes is None:
            self.n_processes = min(cpu_count(), 4)

        # Start input and output queues.
        self.job_queue = Queue()
        self.n_submitted = 0
        self.n_complete = 0
        self.output_queue = Queue()

        # Processes are created by derived class.
        self.processes = []

    def start(self):
        """ Start processes in job pool. """
        for p in self.processes:
            p.start()

    def terminate(self):
        """ Terminate processes in job pool. """
        for p in self.processes:
            p.terminate()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.terminate()
        except:
            pass

    @property
    def pids(self):
        return [p.pid for p in self.processes]

    def __del__(self):
        for process in self.processes:
            process.terminate()
            process.join()


class CreateModelPool(InteractionPool):
    """ A pool of workers for creating two species community models. """

    def __init__(self, output_folder, n_processes=None):
        """ Initialize object.

        Parameters
        ----------
        output_folder : str
            Path to folder where pair community model files are saved
        n_processes: int, optional
            Number of processes in job pool
        """

        InteractionPool.__init__(self, n_processes=n_processes)
        for i in range(self.n_processes):
            p = Process(target=create_pair_model,
                        args=[output_folder, self.job_queue, self.output_queue])
            self.processes.append(p)

    def submit(self, pair):
        """ Submit a job to the job pool.

        Parameters
        ----------
        pair : list of str
            Each element is a path to a model file
        """

        self.job_queue.put(pair)
        self.n_submitted += 1

    def receive_one(self):
        """ Receive one job (blocks until a job completes).

        Returns
        -------
        str
            Path to two species community model file

        Raises
        ------
        Exception
            Any exception caught by worker
        """

        self.n_complete += 1
        result = self.output_queue.get()
        if isinstance(result, Exception):
            raise result
        return result

    def receive_all(self):
        """ Receive all of the jobs submitted to the job pool.

        Yields
        ------
        str
            Path to two species community model file

        Raises
        ------
        Exception
            Any exception caught by worker
        """

        while self.n_complete < self.n_submitted:
            self.n_complete += 1
            result = self.output_queue.get()
            if isinstance(result, Exception):
                raise result
            yield result


class GrowthRatePool(InteractionPool):
    """ A pool of workers for calculating growth rates of two species community models. """

    def __init__(self, media_filename, n_processes=None):
        """ Initialize object.

        Parameters
        ----------
        media_filename : str
            Path to file with exchange reaction bounds for media
        n_processes: int, optional
            Number of processes in job pool
        """

        InteractionPool.__init__(self, n_processes=n_processes)
        for i in range(self.n_processes):
            p = Process(target=compute_growth_rates,
                        args=[media_filename, self.job_queue, self.output_queue])
            self.processes.append(p)

    def submit(self, pair_model_filename):
        """ Submit a job to the job pool.

        Parameters
        ----------
        pair_model_filename : str
            Path to a two species community model file
        """

        self.job_queue.put(pair_model_filename)
        self.n_submitted += 1

    def receive_one(self):
        """ Receive one job (blocks until a job completes).

        Returns
        -------
        pandas.Series
            Growth rate details for two species community model

        Raises
        ------
        Exception
            Any exception caught by worker

        """

        self.n_complete += 1
        result = self.output_queue.get()
        if isinstance(result, Exception):
            raise result
        return result

    def receive_all(self):
        """ Receive all of the jobs submitted to the job pool.

        Yields
        ------
        pandas.Series
            Growth rate details for two species community model

        Raises
        ------
        Exception
            Any exception caught by worker
        """

        while self.n_complete < self.n_submitted:
            self.n_complete += 1
            result = self.output_queue.get()
            if isinstance(result, Exception):
                raise result
            yield result
