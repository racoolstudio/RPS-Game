import random

win = '''
$$$$$$$$$$You-Win$$$$$$$$
$$$$$'`$$$$$$$$$$$$$'`$$$
$$$$$$  $$$$$$$$$$$  $$$$
$$$$$$$  '$/ `/ `$' .$$$$
$$$$$$$$. i  i  /! .$$$$$
$$$$$$$$$.--'--'   $$$$$$
$$^^$$$$$'        J$$$$$$
$$$   ~""   `.   .$$$$$$$
$$$$$e,      ;  .$$$$$$$$
$$$$$$$$$$$.'   $$$$$$$$$
$$$$$$$$$$$$.    $$$$$$$$
$$$$$$$$$$$$$     $$$$$$$
-------------------------
'''
lose ='''
      /))   _   _________________       ((\.
     / / _ / ` |  You  Lose !    |  ,- _ \ \.
    / / / / /`_|     Lol!        |,-\ \ \ \. 
    | |/ / / / |   Try Again.    | \ \ \ \| |
    | / / / / /| Sorryyyyyyyyyyy |\ \ \ \ \ |
    | | | `'  (|/(|___________|)\|    ' | | |
    |          `\  \         /  /,          |
    \           |  |         |  |          /
     \             |         |            /
      \           /          \           /
       \         /            \         /
        \       /              )       /
        )      /              /       /
       /                     /       /

'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
tie = '''

           ________________________________
          |                                |
          |         IT IS A TIE !!         |
          |          Try Again !!!         |
 \)\/))   |                                |   ((\/(/
 \)\.\< /))|________________________________ ((\ >//(/
  \.\.\_/_____,----.              ,----._____\_/// /
   \ `(_]_______    `.          ,'    _______[_)  /
    `-------------,   \        /  ,--------------'
                   |   \      /   |

'''
pImg='9'
cImg=''
play = 'y'
while play == 'y':
    print(''''
              ARE YOU READY ?
                CHOOSEEE
             _..-''--'----_.
           ,''.-''| .---/ _`-._
         ,' \ \  ;| | ,/ / `-._`-.
       ,' ,',\ \( | |// /,-._  / /
       ;.`. `,\ \`| |/ / |   )/ /
      / /`_`.\_\ \| /_.-.'-''/ /
     / /_|_:.`. \ |;'`..')  / /
     `-._`-._`.`.;`.\  ,'  / /
         `-._`.`/    ,'-._/ /
           : `-/     \`-.._/
           |  :      ;._ (
           :  |      \  ` '
            \         \   |
             :        :   ;
             |           /
             ;         ,'
            /         /
           /         /
                    / 
''')
    
    player = int(input('Choose 0 for Rock, 1 for Paper and 2 for Scissors\n:'))
    computer = random.randint(0,2)
    if player == 0 :
        pImg = rock
    elif player == 1:
        pImg = paper
    elif player == 2:
        pImg = scissors
    if computer == 0:
        cImg=rock
    elif computer == 1:
        cImg = paper
    elif computer==2:
        cImg = scissors 
    print(f'You Chose\n{pImg}')
    
    print(f'The Computer Chose\n{cImg}')           
    if computer == player:
        print(tie)
    elif computer == 0 and player ==1:
        print(win)
    elif computer == 2 and player==1:
        print(lose)        
    elif computer ==1 and player ==2 :
        print(win)
    elif computer ==1 and player == 0:
        print(lose)         
    elif computer==2 and player == 0:
        print(win)
    elif computer == 0 and player ==2 :
        print(lose)        
    play = input('Would You Like To Play Again\n Y for Yes or N for NO\n:').lower()    
