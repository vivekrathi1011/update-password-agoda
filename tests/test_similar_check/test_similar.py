import os
import yaml
from password_update.similar_check.check_similarity_oldpassword import similar

with open( "tests/test_data/test_data_similar_check.yaml", 'r' ) as stream:
    test_data_dict = yaml.load( stream )


def test_similar():
    assert (similar( os.path.join( test_data_dict['test']['test_similar_old_password']['value'] ),\
                     os.path.join( test_data_dict['test']['test_similar_new_password']['value'] ) ))


def test_negative_case_similar():
    assert (not similar( os.path.join( test_data_dict['test']['test_negative_case_similar_old_password']['value'] ),\
                         os.path.join( test_data_dict['test']['test_negative_case_similar_new_password']['value'] ) ))
