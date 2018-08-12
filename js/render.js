'use strict'

const digits = require('./digits')

const DASH = '—'
const PIPE = '|'

const concatenateStringsHorizontally = (stringArray, separator) => {
  if (!separator) separator = ''

  const concatenatedRows = stringArray[0].split('\n')

  for (const string of stringArray.slice(1)) {
    for (const [rowIndex, row] of string.split('\n').entries()) {
      concatenatedRows[rowIndex] += separator + row
    }
  }

  return concatenatedRows.join('\n')
}

const generateDashedRow = (rowIsFilled, size) => {
  const rowCharacter = rowIsFilled ? DASH : ' '
  return ` ${rowCharacter.repeat(size)} `
}

const generatePipedSection = (left, right, size) => {
  const row = (left ? PIPE : ' ') + ' '.repeat(size) + (right ? PIPE : ' ')
  return Array(size).fill(row).join('\n')
}

const generateDigitString = (digit, size) => {
  digit = digits[digit]

  return [
    generateDashedRow(digit.top, size),
    generatePipedSection(digit.topLeft, digit.topRight, size),
    generateDashedRow(digit.middle, size),
    generatePipedSection(digit.bottomLeft, digit.bottomRight, size),
    generateDashedRow(digit.bottom, size)
  ].join('\n')
}

module.exports = (number, size, rowLength) => {
  const rows = []
  let currentRow = []
  const digitSeparator = ' '.repeat(size)
  const rowSeparator = '\n'.repeat(size + 1)

  for (const digit of number.toString()) {
    const digitString = generateDigitString(digit, size)
    currentRow.push(digitString)

    if (currentRow.length === rowLength) {
      rows.push(currentRow)
      currentRow = []
    }
  }

  if (currentRow.length) rows.push(currentRow)

  return rows
    .map(row => concatenateStringsHorizontally(row, digitSeparator))
    .join(rowSeparator)
}
