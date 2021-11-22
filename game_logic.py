import random
import statements as stm

# launcher
def init():
  # randomly print 2 true statements and one false statement
  statements = [
    stm.truths[random.sample(range(0, len(stm.lies)), 1)[0]],
    stm.truths[random.sample(range(0, len(stm.lies)), 1)[1]],
    stm.lies[random.sample(range(0, len(stm.lies)), 1)[0]]
  ]

  lie = statements[2]

  shuffledIndices = random.sample(range(0, len(statements)), 3)
  # print(statements[shuffledIndices[0]])
  # print(statements[shuffledIndices[1]])
  # print(statements[shuffledIndices[2]])

  print(statements)
  print(shuffledIndices)

  guess = input('what\'s the lie?\n>>> ')
