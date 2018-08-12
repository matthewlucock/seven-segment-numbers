'use strict'

const readline = require('readline')
const render = require('./render')

const NUMBER_PROMPT = 'Number: '
const SIZE_PROMPT = 'Size: '
const ROW_LENGTH_PROMPT = 'Row length: '

const shellInterface = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const prompt = promptText => {
  return new Promise(resolve => {
    shellInterface.question(promptText, resolve)
  })
}

const numberRendererPrompt = async () => {
  const number = Number(await prompt(NUMBER_PROMPT))
  const size = Number(await prompt(SIZE_PROMPT))
  const rowLength = Number(await prompt(ROW_LENGTH_PROMPT))

  const numberString = render(number, size, rowLength)
  console.log(`\n${numberString}\n`)
}

(async () => {
  while (true) await numberRendererPrompt()
})()
