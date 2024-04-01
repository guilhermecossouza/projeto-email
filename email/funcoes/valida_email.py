import re

REGEX = re.compile(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}")


def email_valido(str_email=None):
    validado = False
    if str_email is not None:
        if REGEX.search(str_email) is not None:
            validado = True
    return validado
