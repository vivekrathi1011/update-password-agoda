import os
import yaml
from password_update.password_validation_utils.validation import check_percentage_on_number

with open( "tests/test_data/test_data_password_validation_utils.yaml", 'r' ) as stream:
    test_data_dict = yaml.load( stream )


def test_check_percentage_of_number():
    assert(check_percentage_on_number( os.path.join( test_data_dict['test']['test_check_percentage_of_number']['value'] ) ))


def test_negative_case_check_percentage_of_number():
    assert(not check_percentage_on_number( os.path.join( test_data_dict['test']['test_negative_case_check_percentage_of_number']['value'] )))

