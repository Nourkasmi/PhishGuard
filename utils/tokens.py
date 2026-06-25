import secrets


def generate_tracking_token():
    """
    Generates a cryptographically secure, unguessable 64-character token.
    Used to uniquely identify each target in a campaign without exposing
    sequential IDs that could be guessed or tampered with.
    """
    return secrets.token_hex(32)