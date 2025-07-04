import secrets
import string


def generate_short_code(length: int = 6) -> str:
    """Случайный код из букв и цифр (например: 'aBc12E')."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


