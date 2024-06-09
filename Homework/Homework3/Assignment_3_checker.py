"""Place this file in the same folder as your assignment 3 solution script. If you changed the name from
Assignment_3_Template.py, change the import statement below to reflect that. At any point while writing your
code, you should be able to confirm that your work so far is correct. Note that this script does not
check parse_args or write_data -- those you will have to check on your own 
This checker was written by Tucker J Lancaster"""

import sys
import numpy as np

try:
    from Assignment_3_Solution import read_data, calculate_ratio, master_merge, pivot, strain_avg
except ImportError:
    print('Error importing one or more user-defined functions. Make sure you have not renamed a function or commented'
          'it out')
    sys.exit(1)


def test_read_data():
    print('testing read_data')
    dt_well, dt_dictionary = read_data('SampleData.xlsx')
    assert dt_well.shape == (112, 3), "unexpected shape for dt_well"
    assert dt_dictionary.shape == (54, 5), "unexpected shape for dt_dictionary"
    assert sorted(list(dt_well.columns)) == [
        'Concentration',  'TargetType', 'Well'], "unexpected column names in dt_well"
    assert sorted(list(dt_dictionary.columns)) == [
        'Replicate', 'Strain1', 'Strain2', 'Time Point', 'Well'], "unexpected column names in dt_dictionary"
    assert np.isclose(dt_well.Concentration.mean(), 798.88), "unexpected values in the Concentration column of dt_well"
    assert np.isclose(dt_dictionary.Replicate.mean(), 9.5), "unexpected values in the Replicate column of dt_dictionary"
    print('   passed')


def test_calculate_ratio():
    print('testing calculate_ratio')
    dt_well, dt_dictionary = read_data('SampleData.xlsx')
    dt_well_sl = calculate_ratio(dt_well)
    assert dt_well_sl.shape == (56, 6), "unexpected shape for dt_well_sl"
    assert sorted(list(dt_well_sl.columns)) == ['Concentration_x', 'Concentration_y', 'Ratio', 'TargetType_x',
                                                'TargetType_y', 'Well'], "unexpected column names in dt_well"
    assert np.isclose(dt_well_sl.Concentration_x.mean(), 1488.0), \
        "unexpected values in the Concentration_x column of dt_well_sl"
    assert np.isclose(dt_well_sl.Concentration_y.mean(), 109.760), \
        "unexpected values in the Concentration_y column of dt_well_sl"
    print('   passed')


def test_master_merge():
    print('testing master_merge')
    dt_well, dt_dictionary = read_data('SampleData.xlsx')
    dt_well_sl = calculate_ratio(dt_well)
    dt_master = master_merge(dt_dictionary, dt_well_sl)
    assert sorted(list(dt_master.columns)) == \
           ['Concentration_x', 'Concentration_y', 'Ratio', 'Replicate', 'Strain1', 'Strain2', 'TargetType_x',
            'TargetType_y', 'Time Point', 'Well'], 'unexpected column headers'
    assert dt_master.shape == (54, 10), "unexpected shape for dt_master"
    assert np.isclose(dt_master.Replicate.mean(), 9.5), 'unexpected value in Replicate column'
    assert np.isclose(dt_master['Time Point'].mean(), 4.0), 'unexpected value in Time Point column'
    assert np.isclose(dt_master.Concentration_x.mean(), 1531.037), 'unexpected value in Concentration_x column'
    assert np.isclose(dt_master.Concentration_y.mean(), 105.594), 'unexpected value in Concentration_y column'
    assert np.isclose(dt_master.Ratio.mean(), 0.0809685), 'unexpected value in Ratio column'
    print('   passed')

def test_pivot():
    print('testing pivot')
    dt_well, dt_dictionary = read_data('SampleData.xlsx')
    dt_well_sl = calculate_ratio(dt_well)
    dt_master = master_merge(dt_dictionary, dt_well_sl)
    dt_output1 = pivot(dt_master)
    assert np.isclose(dt_output1.sum().sum(), 4.372303897721276), 'unexpected DataFrame contents'
    print('   passed')


def test_strain_avg():
    print('testing strain_avg')
    dt_well, dt_dictionary = read_data('SampleData.xlsx')
    dt_well_sl = calculate_ratio(dt_well)
    dt_master = master_merge(dt_dictionary, dt_well_sl)
    dt_output1 = pivot(dt_master)
    dt_output2 = strain_avg(dt_output1)
    assert np.isclose(dt_output2.squeeze().sum(), 0.24290577209562642)
    print('   passed')


def test_all():
    test_read_data()
    test_calculate_ratio()
    test_master_merge()
    test_pivot()
    test_strain_avg()


if __name__ == '__main__':
    test_all()
