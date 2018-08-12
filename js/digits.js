'use strict'

const TOP = 'top'
const TOP_LEFT = 'topLeft'
const TOP_RIGHT = 'topRight'
const MIDDLE = 'middle'
const BOTTOM_LEFT = 'bottomLeft'
const BOTTOM_RIGHT = 'bottomRight'
const BOTTOM = 'bottom'

const SIDES = [
  TOP, TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM
]

const DIGIT_INACTIVE_SIDES = {
  '0': [MIDDLE],
  '1': [TOP, TOP_LEFT, MIDDLE, BOTTOM_LEFT, BOTTOM],
  '2': [TOP_LEFT, BOTTOM_RIGHT],
  '3': [TOP_LEFT, BOTTOM_LEFT],
  '4': [TOP, BOTTOM_LEFT, BOTTOM],
  '5': [TOP_RIGHT, BOTTOM_LEFT],
  '6': [TOP_RIGHT],
  '7': [MIDDLE, BOTTOM_LEFT, BOTTOM],
  '8': [],
  '9': [BOTTOM_LEFT]
}

const makeDigitObject = sidesForDigit => {
  const digit = {}
  for (const side of SIDES) digit[side] = sidesForDigit.includes(side)
  return digit
}

const digits = {
  '-': makeDigitObject([MIDDLE])
}

for (const [digit, inactiveSides] of Object.entries(DIGIT_INACTIVE_SIDES)) {
  const activeSides = SIDES.filter(side => !inactiveSides.includes(side))
  digits[digit] = makeDigitObject(activeSides)
}

module.exports = digits
