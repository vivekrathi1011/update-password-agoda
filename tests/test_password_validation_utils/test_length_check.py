import os
import yaml

from password_update.password_validation_utils.validation import length_check

with open( "tests/test_data/test_data_password_validation_utils.yaml", 'r' ) as stream:
    test_data_dict = yaml.load( stream )


def test_length_check():
    assert (length_check( os.path.join( test_data_dict['test']['test_length_check']['value'] ) ))


def test_negative_case_length__check():
    assert (not length_check( os.path.join( test_data_dict['test']['test_negative_case_length__check']['value'] ) ))
