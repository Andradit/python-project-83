import validators
from urllib.parse import urlparse


def validate_url(url_name):
    if len(url_name) > 255:
        return False
    if not validators.url(url_name):
        return False
    return True


def normalize_url(url_name):
    return urlparse(url_name).scheme + '://' + urlparse(url_name).netloc
