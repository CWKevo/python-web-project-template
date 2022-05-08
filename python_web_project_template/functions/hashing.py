from bcrypt import hashpw, gensalt


def hash_password(password: str) -> str:
    """
        Hashes a password by using [bcrypt](https://pypi.org/project/bcrypt/).
    """

    return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
