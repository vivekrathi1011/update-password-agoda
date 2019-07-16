import os
import yaml

from password_update.password_validation_utils.validation import *

with open( "tests/test_data/test_data_password_validation_utils.yaml", 'r' ) as stream:
    test_data_dict = yaml.load( stream )


def test_check_allowed_special_chars():
    assert(check_allowed_special_chars( os.path.join( test_data_dict['test']['test_check_allowed_special_chars']['value'] ) ))


def test_negative_case_check_allowed_special_chars():
    assert(not check_allowed_special_chars( os.path.join( test_data_dict['test']['test_negative_case_check_allowed_special_chars']['value'] )))

