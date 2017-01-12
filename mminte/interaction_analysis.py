import itertools
from warnings import warn
import pandas as pd
import sys
import traceback

from .job_pool import CreateModelPool, GrowthRatePool
from .interaction_worker import growth_rate_columns


def create_interaction_models(source_models, output_folder='data', n_processes=None):
    """ Create two species community models for all pairs in a community.

    Parameters
    ----------
    source_models : list of str
        List of path names to model files
    output_folder : str
        Path to folder where output community model files are saved
    n_processes: int, optional
        Number of processes in job pool

    Returns
    -------
    list of str
        List of path names to two species community model files
    """

    if len(source_models) < 2:
        warn('There must be at least two models in the list of source models')
        return []

    output_models = list()
    with CreateModelPool(output_folder, n_processes=n_processes) as pool:
        for pair in itertools.combinations(source_models, 2):
            pool.submit([pair[0], pair[1]])
        for community_filename in pool.receive_all():
            output_models.append(community_filename)

    return output_models


def calculate_growth_rates(pair_model_filenames, media_filename, n_processes=None):
    """ Calculate growth rates for all pairs in community.

    Parameters
    ----------
    pair_model_filenames : list of str
        List of path names to two species community model files
    media_filename : str
        Path to file with exchange reaction bounds for media
    n_processes: int, optional
        Number of processes in job pool

    Returns
    -------
    pandas.DataFrame
        Results of growth rate calculations
    """

    growth_rates = pd.DataFrame(columns=growth_rate_columns)
    with GrowthRatePool(media_filename, n_processes=n_processes) as pool:
        for pair_model in pair_model_filenames:
            pool.submit(pair_model)
        for result in pool.receive_all():
            growth_rates = growth_rates.append(result, ignore_index=True)

    return growth_rates
