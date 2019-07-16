import getpass
import logging
from logging.config import fileConfig
import yaml
import importlib

from password_update.similar_check.check_similarity_oldpassword import similar

fileConfig( 'logging_config.ini' )
logger = logging.getLogger()

YAML_FILE_PATH = "config/rules.yaml"
OlD_PASSWORD_FILE_PATH = "config/old_passwd.txt"


def load_rules():
    with open( YAML_FILE_PATH, 'r' ) as stream:
        rules_dict = yaml.load( stream )
        return rules_dict['rules']


def validate_rules(new_passwd):
    rules_object = load_rules()
    for r_obj in rules_object:
        r_item = rules_object[r_obj]
        m = importlib.import_module( r_item['package_name'] )
        func = getattr( m, r_item['func_name'] )
        if not func( new_passwd ):
            return False

    return True


def change_password(old_passwd, new_passwd):
    is_old_exist = True
    if is_old_exist:
        is_valid_passwd = validate_rules( new_passwd )
        if is_valid_passwd:
            is_similar_to_old = similarity_check( old_passwd, new_passwd )
            if is_similar_to_old:
                logger.info( " Password updated successfully!" )
                return True
    return False


def similarity_check(old_password, new_password):
    return similar( old_password, new_password )


if __name__ == '__main__':
    file = open( OlD_PASSWORD_FILE_PATH, "r+" )
    old_passwd = file.read()
    print("Old Password is     :",old_passwd)
    file.close()
    new_passwd = input( "Enter New Passsword : " )
    change_password( old_passwd, new_passwd )

