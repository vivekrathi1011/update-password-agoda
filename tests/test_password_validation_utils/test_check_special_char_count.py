import os
import yaml
from password_update.password_validation_utils.validation import check_special_char_count

with open( "tests/test_data/test_data_password_validation_utils.yaml", 'r' ) as stream:
    test_data_dict = yaml.load( stream )


def test_check_special_char_count():
    assert(check_special_char_count( os.path.join( test_data_dict['test']['test_check_special_char_count']['value'] ) ))


def test_negative_case_check_special_char_count():
    assert(not check_special_char_count( os.path.join( test_data_dict['test']['test_negative_case_check_special_char_count']['value'] )))