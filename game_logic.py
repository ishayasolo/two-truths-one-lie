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
    stm.truths[randomListOfLies[0]]
  ]

  listOfShuffledStatements = random.sample(range(0, len(statements)), 3)
  print(listOfShuffledStatements)