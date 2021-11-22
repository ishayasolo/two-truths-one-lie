import random
import statements as stm

# launcher
def init():
  # create a random list containing two generated truths and one generated lie
  statements = [
    stm.truths[random.randint(0, len(stm.truths) - 1)],
    stm.truths[random.randint(0, len(stm.truths) - 1)],
    stm.lies[random.randint(0, len(stm.lies) - 1)]
  ]

  shuffled_statements = []

  # generate a list of shuffled numbers between 0 and 2
  random_list_of_indices = random.sample(range(0, 3), 3)

  print('\n*** statements ***')
  
  
  x = 0
  while x < 3:
    shuffled_statements.append(statements[random_list_of_indices[x]])
    print(statements[random_list_of_indices[x]])
    
    # if false statement is found store it in a variable called 'lie'
    if statements[random_list_of_indices[x]] == statements[2]:
      lie = statements[random_list_of_indices[x]]
    
    x += 1

  print('\nlie:', lie)

  def validate():
    if selection == lie:
      print('correct!')
    else:
      print('wrong!')
    
  def marker():
    global selection
    if answer == '1':
      selection = shuffled_statements[0]
      validate()
    elif answer == '2':
      selection = shuffled_statements[1]
      validate()
    elif answer == '3':
      selection = shuffled_statements[2]
      validate()
  
  answer = input('\nwhich is the lie?\n>>> ')
  marker()