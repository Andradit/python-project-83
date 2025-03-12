import validators


def validate_url(url_name):
    if len(url_name) > 255:
        return False
    if not validators.url(url_name):
        return False
    return True
