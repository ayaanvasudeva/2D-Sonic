import pygame, sys
import word
from pygame.locals import QUIT, K_LEFT, K_RIGHT, KEYDOWN
import random
t = 0
c = 0
v = 0
s = 1
choic8 = 0
skin = 'sonic'
pygame.init()
pygame_icon = pygame.image.load('python.png')
pygame.display.set_icon(pygame_icon)
test_font_equipped = pygame.font.Font(None, 25)
equipped = test_font_equipped.render('(equipped)', True, 'white')
test_font_rule = pygame.font.Font(None, 25)
test_font_l = pygame.font.Font(None, 25)
test_font_leaderboard_sign = pygame.font.Font(None, 40)
test_font_leaderboard = pygame.font.Font(None, 25)
test_font_leaderboard1 = pygame.font.Font(None, 25)
test_font_leaderboard2 = pygame.font.Font(None, 25)
test_font_leaderboard3 = pygame.font.Font(None, 25)
test_font_leaderboard4 = pygame.font.Font(None, 25)
test_font_leaderboard5 = pygame.font.Font(None, 25)
test_font_leaderboard6 = pygame.font.Font(None, 25)
test_font_leaderboard7 = pygame.font.Font(None, 25)
test_font_leaderboard8 = pygame.font.Font(None, 25)
leaderboard8 = pygame.font.Font(None, 25)
test_font_leaderboard9 = pygame.font.Font(None, 25)
rule = test_font_rule.render('Avoid colliding with enemys by using the left and right arrow keys, ', True, 'white')
leader = test_font_leaderboard.render('1: @SuperSayianCoding Score 9214 ', True, 'white')
leaderh = test_font_l.render('To get on the leaderboard take a screenshot of your highscore and put', True, 'white')
leaderv = leaderboard8.render('it in the chat.', True, 'white')
leader_b = test_font_leaderboard_sign.render('Game Leaderboard', True, 'white')
leader1 = test_font_leaderboard1.render('2: @lion0622 Score 3173 ', True, 'white')
leader2 = test_font_leaderboard2.render('3: (blank) Score (blank) ', True, 'white')
leader3 = test_font_leaderboard2.render('4: (blank) Score (blank) ', True, 'white')
leader4 = test_font_leaderboard2.render('5: (blank) Score (blank) ', True, 'white')
leader5 = test_font_leaderboard2.render('6: (blank) Score (blank) ', True, 'white')
leader6 = test_font_leaderboard2.render('7: (blank) Score (blank) ', True, 'white')
leader7 = test_font_leaderboard2.render('8: (blank) Score (blank) ', True, 'white')
leader8 = test_font_leaderboard2.render('9: (blank) Score (blank) ', True, 'white')
leader9 = test_font_leaderboard2.render('10: (blank) Score (blank) ', True, 'white')
test_font_rule1 = pygame.font.Font(None, 25)
rule1 = test_font_rule1.render('collect coins and try to beat your high score.', True, 'white')
test_font_details = pygame.font.Font(None, 25)
details = test_font_details.render('coin                      enemy', True, 'white')


test_font_sonic = pygame.font.Font(None, 30)
test_font_score = pygame.font.Font(None, 20)
test_font_coin = pygame.font.Font(None, 20)
test_font_score1 = pygame.font.Font(None, 40)
test_font_gameover = pygame.font.Font(None, 100)
gameover = test_font_gameover.render('GameOver', True, 'white')
sky_surface = pygame.Surface((600,400))
sky_surface.fill('green')
b_ground = pygame.Surface((600,400))
b_ground.fill('blue')
avatar = pygame.Surface((85,150))
avatar.fill('white')
under_surface = pygame.Surface((150,25))
under_surface.fill('black')
over_surface = pygame.Surface((360,70))
over_surface.fill('black')
mid_rec = sky_surface.get_rect(midtop = (100,0))
left_track = pygame.Surface((200,400))
left_track.fill('dark green')
left_rec = left_track.get_rect(midtop = (100,0))
right_track = pygame.Surface((200,400))
right_track.fill('dark green')
right_rec = right_track.get_rect(midtop = (500,0))
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Sonic')
background = pygame.image.load('graphics/background.jpg').convert_alpha()
leaderboard = pygame.image.load('graphics/leaderboard.png').convert_alpha()
player = pygame.image.load('graphics/player.png').convert_alpha()
player1 = pygame.image.load('graphics/player1.png').convert_alpha()
player_rec = player.get_rect(midbottom = (300,400))
player_rec1 = player.get_rect(midbottom = (300,400))
player_avatar = pygame.image.load('graphics/player.png').convert_alpha()
player_avatar1 = pygame.image.load('graphics/player1.png').convert_alpha()
right = pygame.image.load('graphics/right.png').convert_alpha()
crab = pygame.image.load('graphics/crab.png').convert_alpha()
crab_rec = crab.get_rect(midbottom = (300,0))
crab_right = pygame.image.load('graphics/crab.png').convert_alpha()
crab_rec_right = crab_right.get_rect(midbottom = (500,0))
crab_left = pygame.image.load('graphics/crab.png').convert_alpha()
crab_rec_left = crab_left.get_rect(midbottom = (100,0))
coin = pygame.image.load('graphics/coin.png').convert_alpha()
coin_rec = coin.get_rect(midbottom = (100,0)) 
play = pygame.image.load('graphics/play.png').convert_alpha()
rules = pygame.image.load('graphics/rules.png').convert_alpha()
back = pygame.image.load('graphics/back.png').convert_alpha()
game_is_still_going = "no"
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mx, my = pygame.mouse.get_pos()
          print(mx, my)
          if mx >= 26 and mx <= 331:
            if my >= 115 and my <= 230:
              if game_is_still_going == "no":
                game_is_still_going = "yes"
                t = 0
                s = 1
                crab_rec.y = -20
                crab_rec_right.y = -20
                crab_rec_left.y = -20
                print("play")
          if mx >= 86 and mx <= 275:
            if my >= 251 and my <= 291:
               if game_is_still_going == 'no':
                 game_is_still_going = 'rule'
                 print('rule')
          if mx >= 4 and mx <= 158:
            if my >= 9 and my <= 63:
              if game_is_still_going == 'rule' or game_is_still_going == 'leaderboard':
                game_is_still_going = 'no'
          if mx >= 448 and mx <= 599:
            if my >= 347 and my <= 399: 
              if game_is_still_going == 'gameover':
                game_is_still_going = 'no'
          if mx >= 92 and mx <= 267:
            if my >= 306 and my <= 331:
              game_is_still_going = 'leaderboard'
          if mx >= 494 and mx <= 526:
            if my >= 156 and my <= 191:
              if skin == 'sonic':
                skin = 'knuckles'
                print(skin)
              else:
                skin = 'sonic'
                print(skin)
            
            
        if event.type == pygame.KEYDOWN:
          if game_is_still_going == "yes":
            if skin == 'sonic':
              if event.key == pygame.K_LEFT:
                if player_rec.colliderect(left_rec):
                  print('')
                else:
                  player_rec.x -= 200
                
                  
              if event.key == pygame.K_RIGHT:
                if player_rec.colliderect(right_rec):
                  print('')
                else:
                  player_rec.x += 200
            else:
              if event.key == pygame.K_LEFT:
                if player_rec1.colliderect(left_rec):
                  print('')
                else:
                  player_rec1.x -= 200
                
                  
              if event.key == pygame.K_RIGHT:
                if player_rec1.colliderect(right_rec):
                  print('')
                else:
                  player_rec1.x += 200
              
    if game_is_still_going == 'leaderboard':
      screen.blit(b_ground,(0,0))
      screen.blit(back,(0,0))
      screen.blit(leader,(10,100))
      screen.blit(leader1,(10,120))
      screen.blit(leader2,(10,140))
      screen.blit(leader3,(10,160))
      screen.blit(leader4,(10,180))
      screen.blit(leader5,(10,200))
      screen.blit(leader6,(10,220))
      screen.blit(leader7,(10,240))
      screen.blit(leader8,(10,260))
      screen.blit(leader9,(10,280))
      screen.blit(leader_b,(5,70))
      screen.blit(leaderh,(10,320))
      screen.blit(leaderv,(10,340))
    if game_is_still_going == 'rule':
      screen.blit(b_ground,(0,0))
      screen.blit(back,(0,0))
      screen.blit(rule,(5,70))
      screen.blit(rule1,(5,90))
      screen.blit(coin,(5,200))
      screen.blit(crab,(150,200))
      screen.blit(details,(40,300))
      
    if game_is_still_going == "no":
        if skin == 'sonic':
          sonic = test_font_sonic.render('Sonic', True, 'white')
        else:
          sonic = test_font_sonic.render('Knuckles', True, 'white')
        screen.blit(b_ground,(0,0))
        screen.blit(play,(0,0))
        screen.blit(rules,(80,220))
        screen.blit(leaderboard,(92,300))
        screen.blit(avatar,(400,100))
        if skin == 'sonic':
          screen.blit(player_avatar,(400,100))
        else:
          screen.blit(player_avatar1,(395,100))
        screen.blit(right,(410,100))
        if skin == 'sonic':
          screen.blit(sonic,(410,80))
        else:
          screen.blit(sonic,(400,80))
        screen.blit(equipped,(400,250))
    if game_is_still_going == "gameover":
      text_surfacel1 = test_font_score1.render(f'Score: {t}', True, 'white')
      screen.blit(background,(0,0))
      screen.blit(under_surface,(0,0))
      screen.blit(text_surfacel1,(0,0))
      screen.blit(over_surface,(200,200))
      screen.blit(gameover,(200,200))
      screen.blit(back,(445,340))
             
    if game_is_still_going == "yes":
      t += 1
      text_surfacel = test_font_score.render(f'Score: {t}', True, 'white')
      coin_score = test_font_coin.render(f'Coins: {c}', True, 'white')
      if choic8 == 0:
        answer = random.randint(1,2)
        print(answer)
        choic8 = 1
      crab_rec.y += s
      if crab_rec.y >= 620:
        if s <= 4:
           s += 0.5
      

        crab_rec.y = -20
      
      if t >= 635:
        if answer == 1:
            crab_rec_right.y += s
            if crab_rec_right.y >= 620:
              crab_rec_right.y = -20
              choic8 = 0
      if t >= 635:
        if answer == 2:
          crab_rec_left.y += s
          if crab_rec_left.y >= 620:
            crab_rec_left.y = -20
            choic8 = 0
      if t >= 300:
        if c == 0:
          coin_rec.y += s
          if coin_rec.y >= 620:
            coin_rec.y = -20
      if skin == 'sonic':
        if player_rec.colliderect(coin_rec):
          c = 1
      else:
        if player_rec1.colliderect(coin_rec):
          c = 1
      if skin == 'sonic':
        if player_rec.colliderect(crab_rec) or player_rec.colliderect(crab_rec_right):
          game_is_still_going = "gameover"
      if skin == 'knuckles':
        if player_rec1.colliderect(crab_rec) or player_rec1.colliderect(crab_rec_right):
          game_is_still_going = "gameover"
      if skin == 'sonic':
        if player_rec.colliderect(crab_rec_left):
          game_is_still_going = "gameover"
      if skin == 'knuckles':
        if player_rec1.colliderect(crab_rec_left):
          game_is_still_going = "gameover"
        
      screen.blit(sky_surface,(mid_rec))  
      screen.blit(left_track,(left_rec))
      screen.blit(right_track,(right_rec))
      if skin == 'sonic':
        screen.blit(player,(player_rec))
      else:
        screen.blit(player1,(player_rec1))
      screen.blit(crab,(crab_rec))
      if t >= 635:
        if answer == 1:
          screen.blit(crab_right,(crab_rec_right))
      if t >= 635:
        if answer == 2:
          screen.blit(crab_right,(crab_rec_left))
      screen.blit(text_surfacel,(0,0))
      screen.blit(coin_score,(0,15))
      
      
      if t >= 300:
        if c == 0:
          screen.blit(coin,(coin_rec))
 
          
            
   
   
    pygame.display.update()
    clock.tick(60)