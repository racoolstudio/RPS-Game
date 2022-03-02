import random
print('Type r for Rock')
print('Type s for Scissors')
print('Type p for Paper')
action_codes = ['r','s','p']
p1= random.choice(action_codes)
p2 = random.choice(action_codes) 
def rps(p1,p2):
    action_codes = ['r','s','p'] 
    p1_score = 0
    p2_score = 0
    response = 'y'
    auto_response = ['y','n']
    while response != 'n':
        p1= random.choice(action_codes)
        p2 = random.choice(action_codes)
        if p1 == p2:
            print('It is a tie !!!')
        elif p1 =='r' and p2=='s' :
          p1_score+=1
         
          print('Player 1 wins !')
          
        elif p1 =='r' and p2=='p' :
          p2_score+=1
          print('Player 2 wins !')
     
        elif p1 =='p' and p2=='r' :
          p1_score+=1
          print('Player 1 wins !')
          
        elif p1 =='p' and p2=='s' :
          p2_score+=1
          print('Player 2 wins !')
          
        elif p1 =='s' and p2=='p' :
          p1_score+=1
          print('Player 1 wins !')
          
        elif p1 =='s' and p2=='r' :
          p2_score+=1
          print('Player 2 wins !')
        print('Details:')
        print('Player 1 chose:',p1)
        print('Player 2 chose:',p2)
        print('Do you wish to continue ? if Yes type y else type n :')
        # if you wish to control the number of rounds
        response = str(input('Enter Your Responds :')).lower()
       # if you wish to use the computer response
       # response = random.chioce(auto_response)
    print('Total Scores :')
    print('PLayer 1 Score :',p1_score)
    print('PLayer 2 Score :',p2_score)
    if p1_score>p2_score:
        print('Player 1 wins !!!')
    elif p1_score<p2_score:
        print('PLayer 2 Wins !!!')   
rps(p1, p2)        