import pytest


@pytest.fixture(scope='session')
def data_folder():
    # PATRIC genome ID for Bacteroides thetaiotaomicron VPI-5482
    return 'mminte/test/data'


@pytest.fixture(scope='session')
def model_files():
    return ['BT.sbml', 'FP.sbml']
