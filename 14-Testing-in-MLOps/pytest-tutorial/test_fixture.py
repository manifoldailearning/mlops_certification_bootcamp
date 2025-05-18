import pytest

@pytest.fixture
def sample_data():
    return [1,2,3,4,5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_length(sample_data):
    assert len(sample_data) == 5

def test_contains(sample_data):
    assert 3 in sample_data

def test_type(sample_data):
    assert isinstance(sample_data, list)
    
    
    