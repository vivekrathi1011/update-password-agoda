import os
import yaml
from password_update.password_validation_utils.validation import check_case_alphabet

with open( "tests/test_data/test_data_password_validation_utils.yaml", 'r' ) as stream:
    test_data_dict = yaml.load( stream )


def test_check_case_alphabet():
    assert(check_case_alphabet( os.path.join( test_data_dict['test']['test_check_case_alphabet']['value'] ) ))


def test_negative_check_case_alphabet():
    assert(not check_case_alphabet( os.path.join( test_data_dict['test']['test_negative_check_case_alphabet']['value'] )))