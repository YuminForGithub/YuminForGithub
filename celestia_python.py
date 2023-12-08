# some changes will active to comments
# and some comments will in korean


from os import system as sys, abort
from numpy.random import randint as rand
from time import sleep as wait
from random import random
from colorama import Fore, Back, Style
from getpass import getpass as getpq
cv = '{0:012d}'.format(rand(0, 99999999999))
print('warning: you need to play this game in only terminal.\ncolor error can occures that unicode appears when color actives.')
maxscore = int(input('max celestia end score? ')) # 점수가 입력한 점수보다 많으면 이김.
if maxscore <= 0:
  print(f'You cannot input 0 or negative score in celestia game in python, caused to game ends with game starts.\ncopy this code:\n{cv}')
  if getpq() == str(cv):
    print('mader mode on')
  else:
    abort()

try:
  print(Fore.GREEN + 'game start, CPU player 2, you\'re an player 1.' + Style.RESET_ALL)
  is_not_falling = True # 시작 전엔 난파가 아님
  cpt = 1 # 1은 플레이어, 2는 컴퓨터
  rd_amount = 2 # 돌리는 주사위의 개수
  cardValid = True # 사용할 수 있는 카드가 있는지 없는지를 결정하는 변수
  cards = rand(1, 4, size=8) # 가지고 있는 도구 카드
  CPcards = rand(1, 4, size=8) # CPU가 가지고 있는 도구 카드
  treasures = 0 # 점수
  CPtreasures = 0 # CPU 점수
  stage = 1 # 현재 섬의 위치
  CPstatus = 0 # 내릴지 아닐지를 결정할 때 사용하는 변수
  CPU_in_boat = True # CPU가 올라탈지 아닐지를 결정하는 변수
  in_boat_1 = True # 플레이어가 타고 있는가
  in_boat_2 = True # CPU가 타고 있는가
  in_boat_all = in_boat_1 and in_boat_2 # 둘 다 타고 있는가
  while treasures <= maxscore and CPtreasures <= maxscore:
    if stage % 4 == 0:
      rd_amount += 1
    print(f'captin player {cpt} rolled a dice.')
    danger_list = [Fore.LIGHTBLUE_EX + 'foggy forest' + Fore.RESET, Fore.YELLOW + 'stormy location' + Fore.RESET, Fore.RED + 'violent bird' + Fore.RESET, Back.LIGHTBLACK_EX + 'pirates\' attack' + Back.RESET]
    dangers = rand(0, 3, size=rd_amount) # 위험 요소
    strds = danger_list[dangers[0]]
    
    # strds = [] # 원래는 상수 리스트로 만들어진 위험 주사위를 굴린 결과를 문자열 리스트로 변환한 결과가 들어갈 빈 리스트
    # for i in range(len(dangers)):
    #   if dangers[i] == 1:
    #     strds.append(Fore.BLUE + 'foggy forest' + Style.RESET_ALL)
    #   elif dangers[i] == 2:
    #     strds.append(Fore.YELLOW + 'stormy location' + Style.RESET_ALL)
    #   elif dangers[i] == 3:
    #     strds.append(Fore.MAGENTA + 'violent bird' + Style.RESET_ALL)
    #   else:
    #     strds.append(Back.LIGHTBLACK_EX + 'pirates\' attack' + Style.RESET_ALL)
    
    #strds = " and ".join(strds)
    
    if dangers[0] == dangers[1]:
      strds = "2 " + strds + "s"
    else:
      strds = strds+' and '+danger_list[dangers[1]]
    
    wait(0.7)
    print(Fore.GREEN + 'dice rolled.' + Style.RESET_ALL)
    print(f'dice showed: {strds}')
    CPstatus = random()
    wait(random() * 1.5)
    if cpt == 1:
      if CPstatus > 1 - (1/rand(30, 200)):
        print('CPU is now' + Fore.RED + 'out' + Fore.RESET + 'of a boat.')
        in_boat_2 = False
        in_boat_all = False
      else:
        print('CPU will stay in a boat.')
    else:
      if input('do you want to stay in a boat?\nif you want to stay in a boat, input y and press enter key.\nif you want don\'t stay in a boat, input anything or press only enter key.\n') == 'y':
        print('you\'re staying in a boat.')
      else:
        print('you are' + Fore.RED + ' exitted ' + Fore.RESET + 'from this boat.')
        in_boat_1 = False
        in_boat_all = False
    try:
      if cpt == 1:
        for j in range(len(dangers)):
          if dangers[j] > 3:
            for i in range(len(cards)):
              if cards[i] == 4:
                cardValid = True
                del cards[i]
                cards.append(rand(1, 4))
            
              
          if dangers[j] > 2:
            for i in range(len(cards)):
              if cards[i] == 3:
                cardValid = True
                del cards[i]
                cards.append(rand(1, 4))
            
              
            if dangers[j] > 0:
              for i in range(len(cards)):
                if cards[i] == 1:
                  cardValid = True
                  del cards[i]
                  cards.append(rand(1, 4))
              
                
            if dangers[j] > 1:
              for i in range(len(cards)):
                if cards[i] == 2:
                  cardValid = True
                  del cards[i]
                  cards.append(rand(1, 4))
      elif cpt == 2:
        if random() > 0.991:
          raise
        else:
          cardValid = True      
    except:
      print(f'your sail falled in! new start! (in information, CPU point is {CPtreasures}, Your point is {treasures})')
    print('you used a card and go to next stage!' if cpt == 1 else 'CPU used a card and go to next stage!') 
    # if cpt == 1:
    #   cpt += 1
    # elif cpt == 2:
    #   cpt -= 1
    
    if cpt == 1:
      cpt = 2
    elif cpt == 2:
      cpt = 1
    
    stage += 1
    
    if cpt == 2:
      treasures += rand(stage, (stage + 7 if stage % 2 != 0 else stage + 8))
    elif cpt == 1:
      CPtreasures += rand(stage, (stage + 7 if stage % 2 != 0 else stage + 8))
    print(f'point: {treasures if cpt == 2 else ('CPU ' + str(CPtreasures))}')
    continue
finally:
  print(f'good game. {'you win.' if treasures > maxscore else 'you lose...'} great job!')

if input('do you want to clean this terminal before return to terminal?\npress y to clean. ') == 'y':
  print('cleaning terminal...')
  sys('clear')
  
