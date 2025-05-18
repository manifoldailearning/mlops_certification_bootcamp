# special configuration file for pytest used to define fixtures & hooks

# acts as global test configuration and fixture provider

import pytest

@pytest.fixture
def sample_data():
    return [1,2,3,4,5]

@pytest.fixture
def sample_data2():
    return [1,2,3,4,5]

