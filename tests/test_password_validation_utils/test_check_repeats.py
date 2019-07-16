import os
import yaml
from password_update.password_validation_utils.validation import check_repeats

with open( "tests/test_data/test_data_password_validation_utils.yaml", 'r' ) as stream:
    test_data_dict = yaml.load( stream )


def test_check_repeats():
    assert(check_repeats( os.path.join( test_data_dict['test']['test_check_repeats']['value'] ) ))


def test_negative_case_check_check_repeats():
    assert(not check_repeats( os.path.join( test_data_dict['test']['test_negative_case_check_check_repeats']['value'] )))

