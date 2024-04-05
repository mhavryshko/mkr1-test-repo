import pytest
import os
from  main import read_population_data, sort_by_area, sort_by_population

@pytest.fixture
def sample_data_file(tmpdir):
    # Creating a temporary file with sample data
    data = """Ukraine, 603500, 42000000
United States of America, 9834000, 331000000
Canada, 9985000, 37590000
Australia, 7692000, 25600000
India, 3287000, 1380000000
China, 9597000, 1441000000
Brazil, 8516000, 212000000"""
    file_path = os.path.join(tmpdir, "test_data.txt")
    with open(file_path, 'w') as f:
        f.write(data)
    return file_path

def test_read_population_data(sample_data_file):
    # Test reading population data from the file
    expected_data = [
        ('Ukraine', 603500.0, 42000000),
        ('United States of America', 9834000.0, 331000000),
        ('Canada', 9985000.0, 37590000),
        ('Australia', 7692000.0, 25600000),
        ('India', 3287000.0, 1380000000),
        ('China', 9597000.0, 1441000000),
        ('Brazil', 8516000.0, 212000000)
    ]
    assert read_population_data(sample_data_file) == expected_data

def test_sort_by_area(sample_data_file):
    # Test sorting population data by area
    sorted_data = sort_by_area(read_population_data(sample_data_file))
    expected_sorted_data = [
        ('Ukraine', 603500.0, 42000000),
        ('India', 3287000.0, 1380000000),
        ('Australia', 7692000.0, 25600000),
        ('Brazil', 8516000.0, 212000000),
        ('China', 9597000.0, 1441000000),
        ('United States of America', 9834000.0, 331000000),
        ('Canada', 9985000.0, 37590000)
    ]
    assert sorted_data == expected_sorted_data
