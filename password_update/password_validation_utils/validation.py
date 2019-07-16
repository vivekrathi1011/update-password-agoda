import logging
import re
logger = logging.getLogger()

# Password must have at least 18 alphanumeric characters


def length_check(new_password):
    if len( new_password ) < 18:
        logger.info( " Fail : Password must have length: > 18" )
        return False
    return True

#  Password must have at least 1 Upper case and 1 lower case


def check_case_alphabet(new_password):
    if new_password.upper() == new_password or new_password.lower() == new_password:
        logger.info(
            " Fail : Password must have at-least one upper and one lower alphabet): (A - Z & a "
            "- z)" )
        return False
    return True


#  Password must have at least 1 numeric


def check_case_integer(new_password):
    if any( char.isdigit() for char in new_password ):
        return True
    logger.info( " Fail : Password must have at-least integers: (0 - 9)" )
    return False


#  Password must have at one special character

def check_special_char(new_password):
    if re.sub( '[^a-zA-Z0-9]', '', new_password ) == new_password:
        logger.info( " Fail : Password must have at-least one special character" )
        return False
    return True


#  Password must have only list of special chars ! @ # $ & *  are allowed

def check_allowed_special_chars(new_password):
    if re.match( "^[a-zA-Z0-9*;&$#@!]+$", new_password ):
        return True
    logger.info( " Fail : Password must have only list of special chars ! @ # $ & *  are allowed" )
    return False


# No duplicate repeat characters more than 4


def check_repeats(new_password):
    chars = set( new_password )
    for c in chars:
        if new_password.count( c ) > 4:
            logger.info( " Fail : No duplicate repeat characters more than 4" )
            return False
    return True


# No more than 4 special characters


def check_special_char_count(new_password):
    if len( re.sub( '[^a-zA-Z0-9]', '', new_password ) ) < len( new_password ) - 4:
        logger.info( " Fail : No more than 4 special characters" )
        return False
    return True


# 50 % of password should not be a number

def check_percentage_on_number(new_password):
    if len( re.sub( '[0-9]+', '', new_password ) ) < len( new_password ) / 2 - 1:
        logger.info( " Fail : 50 % of password should not be a number" )
        return False
    return True
