import coin_merchant as cm

def print_rules(cm):
  print('\n*********************')
  print('* RULES OF THE GAME *')
  print('*********************')
  print('- the rules of the game are very simple')
  print('- i\'ll make three (3) statements')
  print('- two (2) out of my three (3) statements are true')
  print('- one is a BIG FAT lie')
  print('- your job is to spot the lie')
  print('- you begin with', cm.get_coins(), 'coins')
  print('- you guess correctly, you earn 10 coins')
  print('- you guess wrongly, you lose 10 coins')
  print('- type \'ctrl + shift + c\' at any point to force-close the program')
  print('- GOODLUCK!!!')
