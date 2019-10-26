from exception.exceptions import TooManyCharsException


def validate_chars_limit(text, limit):
    if len(text) > limit:
        raise TooManyCharsException("Diminue esse textão aí, pfv.")
