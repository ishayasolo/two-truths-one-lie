# modules importation
from curses.ascii import isdigit
import random # built-in module
import statements as stm, coin_merchant as cm, round_merchant as rm # user-defined module

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
  def validate_selection(selection, lie):
    if selection == lie:
      print('\n- you are correct!!!')
      cm.add_coins()
      print('- you\'ve been awarded 10 coins')
    else:
      print('\n- your answer is wrong!')
      print('- the false statement is ->', lie)
      print('- you earned 0 coins')
    
  # a subroutine to mark the player's answer
  # this subroutine also calls the 'validate_selection()' function
  def mark_answer():
    if not answer or not isdigit(answer):
      print('\n- you were supposed to type in \'1\', \'2\' or \'3\'')
      print('- congrats!...you have ruined this round')
    elif answer == '1':
      selection = shuffled_statements[0]
      validate_selection(selection, lie)
    elif answer == '2':
      selection = shuffled_statements[1]
      validate_selection(selection, lie)
    elif answer == '3':
      selection = shuffled_statements[2]
      validate_selection(selection, lie)
    else:
      print('\n- you were supposed to type in \'1\', \'2\' or \'3\'')
      print('- congrats!...you have ruined this round')
    
    print('- you currently have', cm.get_coins(), 'coins')
    print('- and you have played', rm.get_rounds(), 'round(s)')
  
  # a subroutine that'll as if the player wishes to continue or not
  # and make decisions based on the player's response
  def continue_or_not():
    play_on = input('\ndo you wish to play on? (\'yes\' or \'no\')\n>>> ')
    
    if play_on == 'yes' or play_on == 'yea' or play_on == 'yeah' or play_on == 'y' or play_on == 'ya' or play_on == 'yah' or play_on == 'true' or play_on == 'True' or play_on == True or play_on == '1':
      init()
    elif play_on == 'no' or play_on == 'n' or play_on == 'false' or play_on == 'False' or play_on == False or  play_on == '0':
      print('ok!...bye!')
    else:
      print('i\'ll take that as a \'no\'...bye!')

  # function calls
  print('\n**************')
  print('** ROUND ', rm.get_rounds(), '**')
  print('**************')
  print_statements()
  answer = input('\nwhich of the above statements is a lie? (\'1\', \'2\' or \'3\')\n>>> ')
  mark_answer()
  rm.add_round()
  continue_or_not()

  