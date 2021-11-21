import random
import statements as stm

# launcher
def init():
  randomListOfTruths = random.sample(range(0, len(stm.truths)), 2)
  randomListOfLies = random.sample(range(0, len(stm.lies)), 1)

  # print 2 true statements
  statements = [
    stm.truths[randomListOfTruths[0]],
    stm.truths[randomListOfTruths[1]],
    stm.lies[randomListOfLies[0]]
  ]

  lie = statements[2]

  shuffledIndices = random.sample(range(0, len(statements)), 3)
  # print(statements[shuffledIndices[0]])
  # print(statements[shuffledIndices[1]])
  # print(statements[shuffledIndices[2]])

  print(statements)
  print(shuffledIndices)

  guess = input('what\'s the lie?\n>>> ')
