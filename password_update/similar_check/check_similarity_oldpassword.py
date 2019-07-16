from difflib import SequenceMatcher
import logging

logger = logging.getLogger()

'''Password is not similar to old password &lt; 80% match.'''


def similar(old_password, new_password):
    if SequenceMatcher( None, old_password, new_password ).ratio() < 0.8:
        return True
    logger.info( " Fail : password is not similar to old password : < 80% match." )
    return False
