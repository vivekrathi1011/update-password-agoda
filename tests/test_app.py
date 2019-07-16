import os
import yaml

from app import validate_rules, change_password, similarity_check

with open( "tests/test_data/test_data_app.yaml", 'r' ) as stream:
    test_data_dict = yaml.load( stream )


def test_app_validate_rules_correct_password():
    assert (
        validate_rules( os.path.join( test_data_dict['test']['test_app_validate_rules_correct_password']['value'] ) ))


def test_app_validate_rules_length_check():
    assert (
        not validate_rules( os.path.join( test_data_dict['test']['test_app_validate_rules_length_check']['value'] ) ))


def test_app_validate_rules_check_case_alphabet():
    assert (not validate_rules(
        os.path.join( test_data_dict['test']['test_app_validate_rules_check_case_alphabet']['value'] ) ))


def test_app_validate_rules_check_case_integer():
    assert (not
            validate_rules(
                os.path.join( test_data_dict['test']['test_app_validate_rules_check_case_integer']['value'] ) ))


def test_app_validate_rules_check_special_char():
    assert (not
            validate_rules(
                os.path.join( test_data_dict['test']['test_app_validate_rules_check_special_char']['value'] ) ))


def test_app_validate_rules_check_allowed_special_chars():
    assert (not validate_rules(
        os.path.join( test_data_dict['test']['test_app_validate_rules_check_allowed_special_chars']['value'] ) ))


def test_app_validate_rules_check_repeats():
    assert (not
            validate_rules( os.path.join( test_data_dict['test']['test_app_validate_rules_check_repeats']['value'] ) ))


def test_app_validate_rules_check_special_char_count():
    assert (not
            validate_rules(
                os.path.join( test_data_dict['test']['test_app_validate_rules_check_special_char_count']['value'] ) ))


def test_app_validate_rules_check_percentage_on_number():
    assert (not
            validate_rules(
                os.path.join( test_data_dict['test']['test_app_validate_rules_check_percentage_on_number']['value'] ) ))


def test_app_change_password():
    assert (change_password(
        os.path.join( test_data_dict['test']['test_app_change_password']['test_app_change_password_old_passwd'] ),
        os.path.join( test_data_dict['test']['test_app_change_password']['test_app_change_password_new_passwd'] ) ))


def test_app_change_password_with_match():
    assert (not change_password( os.path.join( test_data_dict['test']['test_app_change_password_with_match'][
                                                   'test_app_change_password_with_match_old_passwd'] ),
                                 os.path.join( test_data_dict['test']['test_app_change_password_with_match'][
                                                   'test_app_change_password_with_match_new_passwd'] ) ))


def test_app_similarity_check():
    assert (similarity_check(
        os.path.join( test_data_dict['test']['test_app_change_password']['test_app_change_password_old_passwd'] ),
        os.path.join( test_data_dict['test']['test_app_change_password']['test_app_change_password_new_passwd'] ) ))


def test_app_similarity_check_negative():
    assert (not similarity_check( os.path.join( test_data_dict['test']['test_app_change_password_with_match'][
                                                   'test_app_change_password_with_match_old_passwd'] ),
                                 os.path.join( test_data_dict['test']['test_app_change_password_with_match'][
                                                   'test_app_change_password_with_match_new_passwd'] ) ))
