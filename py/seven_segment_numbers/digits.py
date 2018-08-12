class _Digit:
    TOP = 'top'
    TOP_LEFT = 'top_left'
    TOP_RIGHT = 'top_right'
    MIDDLE = 'middle'
    BOTTOM_LEFT = 'bottom_left'
    BOTTOM_RIGHT = 'bottom_right'
    BOTTOM = 'bottom'

    SIDES = [
        TOP, TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM
    ]

    def __init__(self, sides):
        for side in _Digit.SIDES:
            setattr(self, side, side in sides)

_DIGIT_INACTIVES_SIDES = {
    '0': [_Digit.MIDDLE],
    '1': [
        _Digit.TOP,
        _Digit.TOP_LEFT,
        _Digit.MIDDLE,
        _Digit.BOTTOM_LEFT,
        _Digit.BOTTOM
    ],
    '2': [_Digit.TOP_LEFT, _Digit.BOTTOM_RIGHT],
    '3': [_Digit.TOP_LEFT, _Digit.BOTTOM_LEFT],
    '4': [_Digit.TOP, _Digit.BOTTOM_LEFT, _Digit.BOTTOM],
    '5': [_Digit.TOP_RIGHT, _Digit.BOTTOM_LEFT],
    '6': [_Digit.TOP_RIGHT],
    '7': [_Digit.MIDDLE, _Digit.BOTTOM_LEFT, _Digit.BOTTOM],
    '8': [],
    '9': [_Digit.BOTTOM_LEFT]
}

DIGITS = {
    '-': _Digit([_Digit.MIDDLE])
}

for digit, inactive_sides in _DIGIT_INACTIVES_SIDES.items():
    sides = [side for side in _Digit.SIDES if side not in inactive_sides]
    DIGITS[digit] = _Digit(sides)
