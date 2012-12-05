import hashlib

from settings import SECRET_WORD


__version__ = '0.0.0'

def get_secret_word_as_md5():
    """returns md5 hash of SECRET_WORD in upper case"""
    m = hashlib.md5()
    m.update(SECRET_WORD)
    return m.hexdigest().upper()

