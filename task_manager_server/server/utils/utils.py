### Utils functions

import hashlib


def hash_password(password: str) -> str:
    """ Function hashes a plain text password using the sha256 algorithm.

    Args:
        password (str): A plain text password.

    Returns:
        str: The hashed password.
    """
    m = hashlib.sha256()
    m.update(password.encode())
    return m.hexdigest()
