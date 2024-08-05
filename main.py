import pygame
import random
import sys
pygame.init()

clock = pygame.time.Clock()
FPS = 60
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Runner")

icon = pygame.image.load("assets/ground.png")
#icon = pygame.transform.scale(icon,(100,10))
pygame.display.set_icon(icon)

# game var

pygame.font.init()
font = pygame.font.SysFont("Minecraft",30)

class World:
     def __init__(self,x,y,x2,y2):
          

          self.sky_img = pygame.image.load("assets/Sky.png")
          self.sky_img = pygame.transform.scale(self.sky_img,(800,400))
          self.sky_img_rect = self.sky_img.get_rect()
          self.sky_img_rect.x = x
          self.sky_img_rect.y = y

          self.ground_img = pygame.image.load("assets/ground.png")
          self.ground_img_rect = self.ground_img.get_rect()
          
          
          self.ground_img_rect.x = x2
          self.ground_img_rect.y = y2

     def update(self):
          screen.blit(self.sky_img,self.sky_img_rect) 
          screen.blit(self.ground_img,self.ground_img_rect)
          #pygame.draw.rect(screen,(255,255,255),self.ground_img_rect,2)
          

     

class Player(pygame.sprite.Sprite):
     def __init__(self,x,y):
         super().__init__()
         self.sprites = []
         for i in range(0,3):
          self.sprites.append(pygame.image.load(f"assets/player_walk_{i}.png"))
         self.index = 0
         
         self.jump_sprite = (pygame.image.load("assets/player_jump_0.png"))
        
         
         self.image_player = self.sprites[self.index]
         self.image_rect_player = self.image_player.get_rect(topleft=(x,y))
         
         self.image_rect_player.x = x
         self.image_rect_player.y = y
         self.is_animating = False
         self.gravity = 2
         self.jumping = False
         self.jump_cooldown = 500
         self.last_jump_time = pygame.time.get_ticks()
         self.vel_y = 0
         

     def animate(self):
          self.is_animating = True
#score
     def update(self):
          if self.is_animating == True:
               self.index += 0.1
          
               if self.index >= len(self.sprites):
                    self.index = 0
                    self.is_animating = False
               self.image_player = self.sprites[int(self.index)]


          screen.blit(self.image_player,self.image_rect_player)
          global player_coll
          #player_coll = pygame.draw.rect(screen,"green",[self.image_rect_player.x,self.image_rect_player.y,65,50],2)

          key = pygame.key.get_pressed()
          if key[pygame.K_d]:
               player.animate()
               self.image_rect_player.x += 2
          if key[pygame.K_a]:
               player.animate()
               #self.image = pygame.transform.flip(self.image,True,False)
               #self.image = self.sprites[int(self.index)]
               self.image_rect_player.x -= 2
          if key[pygame.K_SPACE] and not self.jumping:
               current_time = pygame.time.get_ticks()
               if current_time - self.last_jump_time > self.jump_cooldown:
                    self.jumping = True
                    self.vel_y = -10
                    self.last_jump_time = current_time
                    self.image_player = self.jump_sprite
                    

          if self.jumping:
               self.vel_y += 0.3
               if self.vel_y > 3:
                    self.vel_y = 3
               self.image_rect_player.y += self.vel_y


          #self.image_rect.y += self.gravity

          if self.image_rect_player.y > 220:
               self.image_rect_player.y = 220
               self.jumping = False
               self.image_player = self.sprites[int(self.index)]
          #if self.image_rect.y == 220:
               #self.jumping = False
          
          if self.image_rect_player.x < 0:
               self.image_rect_player.x = 0
          if self.image_rect_player.x > 732:
               self.image_rect_player.x = 732

          
          #print(self.image_rect.x)
class Enemy(pygame.sprite.Sprite):
     def __init__(self,x,y,x2,y2 ):
          super().__init__()
          self.sprites = []
          self.enemie_list = []

          self.snail_sprites = []

          for i in range(1,3):
               self.sprites.append(pygame.image.load(f"assets/Fly{i}.png"))
          self.index = 0
          self.image = self.sprites[self.index]
          
          for i in range(1,3):
               self.snail_sprites.append(pygame.image.load(f"assets/snail{i}.png"))
          self.snail_index = 0
          self.snail_image = self.snail_sprites[self.snail_index]


          self.image_rect = self.image.get_rect()
          self.image_rect.x = x
          self.image_rect.y = y
          self.is_animating = False

          self.snail_image_rect = self.snail_image.get_rect(topleft=(x2,y2))
          self.snail_image_rect.x = x2
          self.snail_image_rect.y = y2
          self.score = 0
          self.start_time = pygame.time.get_ticks()
          


     def animate(self):
          self.is_animating = True
     def update(self):
          self.index += 0.1
          if self.index >=  len(self.sprites):
               self.index = 0
          self.image = self.sprites[int(self.index)]  
          
          #random_speed = random.randint(1,2)
          self.image_rect.x -= 1
          self.snail_image_rect.x -= 1.5

          if self.snail_image_rect.x < -200:
               print("Aus dem Fenster!")
               self.snail_image_rect.x = random.randint(1100,1200)
               self.snail_image_rect.y = 265

               #self.score += 100
          
          elapsed_time = pygame.time.get_ticks() - self.start_time
          self.score = elapsed_time // 1000
          
          if self.image_rect.x < -200:
               print("Aus dem Fenster!")
               
               self.image_rect.x = random.randint(630,1200)
               self.image_rect.y = random.randint(0,100)
          
               #self.score += 100
          
          self.snail_index += 0.1
          if self.snail_index >= len(self.snail_sprites):
               self.snail_index = 0
          self.snail_image = self.snail_sprites[int(self.index)]
          
              
          screen.blit(self.image,self.image_rect)
          screen.blit(self.snail_image,self.snail_image_rect)

          
          
          if player.image_rect_player.colliderect(self.snail_image_rect) or player.image_rect_player.colliderect(self.image_rect):
               print("Kollision!")
               death_screen_func()
          
          
          
          score_text = font.render(f"Score: {self.score} ",True,"black",None)
          screen.blit(score_text,dest=(10,0))
enemies = pygame.sprite.Group()
player = Player(0,220)
def spawn_enemy():
    
     #enemies
     min_distance = 100
     
     def far_enough(new_enemy):
          
          for enemy in enemies:
               if (abs(new_enemy.image_rect.x - enemy.image_rect.x) < min_distance and
                    abs(new_enemy.image_rect.y - enemy.image_rect.y) < min_distance) or (
                    abs(new_enemy.snail_image_rect.x - enemy.snail_image_rect.x) < min_distance and
                    abs(new_enemy.snail_image_rect.y - enemy.snail_image_rect.y) < min_distance):
                    return False
          return True

     while True:
           x = random.randint(632,1200)
           y = random.randint(0,100)
           #print(x)
           x2 = random.randint(1100,1200)
           y2 = 265


           new_enemy = Enemy(x,y,x2,y2)
           
           if far_enough(new_enemy):
                enemies.add(new_enemy)
                break
           
                
        
     
     
          


#moving_sprites = pygame.sprite.Group()
#world = World(0,0,0,300)

#enemies = Enemy(732,random.randint(0,250))

#enemies = pygame.sprite.Group()
#player = Player(0,220)
#moving_sprites.add(player)
#moving_sprites.add(enemies)



def death_screen_func():
     death_screen = True
     while death_screen:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    death_screen = False
                    sys.exit(0)
               if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_SPACE:
                              death_screen = False
                              main()
                              return
                         
                         
                         
                         
          
          sky_img = pygame.image.load("assets/Sky.png")
          sky_img = pygame.transform.scale(sky_img,(800,400))
          screen.blit(sky_img,dest=(0,0))

          font = pygame.font.SysFont("Minecraft",36)
          font_2 = pygame.font.SysFont("Minecraft",20)

          game_over_text = font.render("Game Over!",False,"blue",None)
          text = font_2.render("Press SPACE to Play!",False,"light blue",None)

          screen.blit(game_over_text,dest=(280,280))
          screen.blit(text,dest=(280,330))

          player_img = pygame.image.load("assets/player_walk_0.png")
          player_img = pygame.transform.scale(player_img,(190,200))
          screen.blit(player_img,dest=(290,50))
          

          pygame.display.update()
          clock.tick(FPS)
     pygame.quit()

#spawn_enemy()

def main():
     global enemies,player
     moving_sprites = pygame.sprite.Group()
     world = World(0,0,0,300)

#enemies = Enemy(732,random.randint(0,250))

     enemies = pygame.sprite.Group()
     player = Player(0,220)
     moving_sprites.add(player)
     moving_sprites.add(enemies)
     run = True
     spawn_enemy()
     while run:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    run = False
      
     
     
          world.update()
          enemies.update()
          player.update()
          
          moving_sprites.update()

    
     

     
          pygame.display.update()
          clock.tick(FPS)
     pygame.quit()

main()