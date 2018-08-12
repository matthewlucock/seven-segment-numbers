from seven_segment_numbers import render


_NUMBER_PROMPT = 'Number: '
_SIZE_PROMPT = 'Size: '
_ROW_LENGTH_PROMPT = 'Row length: '
_INVALID_INTEGER_MESSAGE = 'You must enter a valid integer.'
_INTEGER_NOT_POSITIVE_MESSAGE = 'You must enter a positive integer.'


def _get_integer_input(prompt):
    value = None

    while value is None:
        try:
            value = int(input(prompt))
        except ValueError:
            print(_INVALID_INTEGER_MESSAGE)

    return value


def _get_positive_integer_input(prompt):
    value = None

    while value is None or value <= 0:
        value = _get_integer_input(prompt)

        if value <= 0:
            print(_INTEGER_NOT_POSITIVE_MESSAGE)

    return value


def prompt():
    number = _get_integer_input(_NUMBER_PROMPT)
    size = _get_positive_integer_input(_SIZE_PROMPT)
    row_length = _get_positive_integer_input(_ROW_LENGTH_PROMPT)

    print(
        '\n{}\n'.format(render(number, size, row_length))
    )


if __name__ == '__main__':
    while True:
        prompt()
