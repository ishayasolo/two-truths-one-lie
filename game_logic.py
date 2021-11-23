# modules importation
import random # built-in module
import statements as stm, coin_merchant as c # user-defined module

# launcher
def init():
  # create a random list containing two generated truths and one generated lie
  statements = [
    stm.truths[random.randint(0, len(stm.truths) - 1)],
    stm.truths[random.randint(0, len(stm.truths) - 1)],
    stm.lies[random.randint(0, len(stm.lies) - 1)]
  ]

  lie = statements[2] # the false statement

  # create an empty list that'll hold shuffled statements
  shuffled_statements = []

  # generate a list of shuffled numbers between 0 and 2
  random_list_of_indices = random.sample(range(0, 3), 3)

  # a subroutine for printing the statements
  def print_statements():
    print('\n**************')
    print('* STATEMENTS *')
    print('**************')

    x = 0
    while x < 3:
      shuffled_statements.append(statements[random_list_of_indices[x]])
      x += 1
    
    print('(1.)', shuffled_statements[0])
    print('(2.)', shuffled_statements[1])
    print('(3.)', shuffled_statements[2])

  # a subroutine for validating the player's selection
  def validate_selection():
    if selection == lie:
      print('\nyou are correct!!!')
      c.add_coins()
      print('you\'ve been awarded 10 coins')
    else:
      print('\nyour answer is wrong!')
      print('the false statement is --', lie)
      print('you earned 0 coins')

    print('you currently have', c.get_coins(), 'coins')
    
  # a subroutine to mark the player's answer
  # this subroutine also calls the 'validate_selection()' function
  def mark_answer():
    global selection
    if answer == '1':
      selection = shuffled_statements[0]
    elif answer == '2':
      selection = shuffled_statements[1]
    elif answer == '3':
      selection = shuffled_statements[2]
    
    validate_selection()
  
  # a subroutine that'll as if the player wishes to continue or not
  # and make decisions based on the player's response
  def continue_or_not():
    playOn = input('\ndo you wish to play on? (\'yes\' or \'no\')\n>>> ')
    
    if playOn == 'yes':
      init()
    elif playOn == 'no':
      print('ok!...bye!')
    else:
      print('i\'ll take that as a \'no\'...bye!')

  # function calls
  print_statements()
  answer = input('\nwhich of the above statements is a lie? (\'1\', \'2\' or \'3\')\n>>> ')
  mark_answer()
  continue_or_not()