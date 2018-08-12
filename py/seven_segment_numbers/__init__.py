from .digits import DIGITS


_DASH = '—'
_PIPE = '|'


def _concatenate_strings_horizontally(string_list, separator=''):
    concatenated_rows = string_list[0].split('\n')

    for string in string_list[1:]:
        for row_index, row in enumerate(string.split('\n')):
            concatenated_rows[row_index] += separator + row

    return '\n'.join(concatenated_rows)


def _generate_dashed_row(row_is_filled, size):
    row_character = _DASH if row_is_filled else ' '
    return ' {} '.format(row_character * size)


def _generate_piped_section(left, right, size):
    row = (
        (_PIPE if left else ' ')
        + ' ' * size
        + (_PIPE if right else ' ')
    )

    return '\n'.join([row] * size)


def _generate_digit_string(digit, size):
    digit = DIGITS[digit]

    return '\n'.join([
        _generate_dashed_row(digit.top, size),
        _generate_piped_section(digit.top_left, digit.top_right, size),
        _generate_dashed_row(digit.middle, size),
        _generate_piped_section(digit.bottom_left, digit.bottom_right, size),
        _generate_dashed_row(digit.bottom, size)
    ])


def render(number, size, row_length=None):
    rows = []
    current_row = []
    digit_separator = ' ' * size
    row_separator = '\n' * (size + 1)

    for digit in str(number):
        digit_string = _generate_digit_string(digit, size)
        current_row.append(digit_string)

        if len(current_row) == row_length:
            rows.append(current_row)
            current_row = []

    if len(current_row):
        rows.append(current_row)

    concatenated_rows = [
        _concatenate_strings_horizontally(row, digit_separator) for row in rows
    ]

    return row_separator.join(concatenated_rows)
