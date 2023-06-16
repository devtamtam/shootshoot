import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

# Box attributes
box_width, box_height = 50, 50
box1_x = 400
box1_y = 400
box1_speed = 5

box2_x = 800
box2_y = 200
box2_speed = 5

# Bullet attributes
bullet1_width,bullet1_height = 10, 5
bullet1_speed = 10
bullet1_state = "ready"

bullet2_width,bullet2_height = 10, 5
bullet2_speed = 10
bullet2_state = "ready"


# Game loop
running = True
clock = pygame.time.Clock()

def box(x, y, color):
    pygame.draw.rect(screen, color, (x, y, box_width, box_height))

def fire_bullet1(x, y, direction):
    global bullet1_state
    bullet1_state = "fire"
    pygame.draw.rect(screen, (255, 255, 255), (x, y + box_height // 2 - bullet1_height // 2, bullet1_width, bullet1_height))
    if direction == "left":
        return -bullet1_speed
    elif direction == "right":
        return bullet1_speed
    return 0




def fire_bullet2(x, y, direction):
    global bullet2_state
    bullet2_state = "fire"
    pygame.draw.rect(screen, (255, 255, 255), (x, y + box_height // 2 - bullet2_height // 2, bullet2_width, bullet2_height))
    if direction == "left":
        return -bullet2_speed
    elif direction == "right":
        return bullet2_speed
    return 0

box1_hit_count = 0
box2_hit_count = 0

def display_hit_counts():
    font = pygame.font.Font(None, 30)
    box1_hit_text = font.render("Box1 Hits: " + str(box1_hit_count), True, (255, 255, 255))
    box2_hit_text = font.render("Box2 Hits: " + str(box2_hit_count), True, (255, 255, 255))
    screen.blit(box1_hit_text, (10, 10))
    screen.blit(box2_hit_text, (screen_width - box2_hit_text.get_width() - 10, 10))






while running:
    clock.tick(60)  # Set the frame rate
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet1_state == "ready":
                bullet1_x = box1_x + box_width
                bullet1_y = box1_y
                bullet1_state = "fire"
                bullet1_direction = "right"
            if event.key == pygame.K_p and bullet2_state == "ready":
                bullet2_x = box2_x
                bullet2_y = box2_y
                bullet2_state = "fire"
                bullet2_direction = "left"
    
    #handle evnt2   
    
    
    
    
    
    # Handle box 2 movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box2_x -= box2_speed
    if keys[pygame.K_RIGHT]:
        box2_x += box2_speed
    if keys[pygame.K_UP]:
        box2_y -= box2_speed
    if keys[pygame.K_DOWN]:
        box2_y += box2_speed
    
    # Handle box 1 movement
    if keys[pygame.K_a]:
        box1_x -= box1_speed
    if keys[pygame.K_d]:
        box1_x += box1_speed
    if keys[pygame.K_w]:
        box1_y -= box1_speed
    if keys[pygame.K_s]:
        box1_y += box1_speed
    
    # Update bullet1 position
    if bullet1_state == "fire":
        if bullet1_x > screen_width or bullet1_x < 0:
            bullet1_state = "ready"
        else:
            if bullet1_direction == "left" and bullet1_y >= box1_y and bullet1_y <= box1_y + box_height and bullet1_x >= box1_x and bullet1_x <= box1_x + box_width:
                bullet1_state = "ready"
            elif bullet1_direction == "right" and bullet1_y >= box2_y -25 and bullet1_y <= box2_y + 25 and bullet1_x >= box2_x and bullet1_x <= box2_x + box_width:
                bullet1_state = "ready"
                box2_hit_count += 1
            
            if bullet1_state == "fire":
                bullet1_x += fire_bullet1(bullet1_x, bullet1_y, bullet1_direction)
    
    #update bullet2 position
    if bullet2_state == "fire":
        if bullet2_x > screen_width or bullet2_x < 0:
            bullet2_state = "ready"
        else:
            if bullet2_direction == "left" and bullet2_y >= box1_y - 25 and bullet2_y <= box1_y + 25 and bullet2_x >= box1_x and bullet2_x <= box1_x + box_width:
                bullet2_state = "ready"
                box1_hit_count += 1
            elif bullet2_direction == "right" and bullet2_y >= box2_y and bullet2_y <= box2_y  and bullet2_x >= box2_x and bullet2_x <= box2_x + box_width:
                bullet2_state = "ready"
            
            if bullet2_state == "fire":
                bullet2_x += fire_bullet2(bullet2_x, bullet2_y, bullet2_direction)
    

    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw the boxes
    box(box1_x, box1_y, (255, 0, 0))
    box(box2_x, box2_y, (0, 255, 0))
    
    # Draw the bullet
    if bullet1_state == "fire":
       pygame.draw.rect(screen, (255, 255, 255), (bullet1_x, bullet1_y + box_height // 2 - bullet1_height // 2, bullet1_width, bullet1_height))

    if bullet2_state == "fire":
       pygame.draw.rect(screen, (255, 255, 255), (bullet2_x, bullet2_y + box_height // 2 - bullet2_height // 2, bullet2_width, bullet2_height))
    
    
    # Display hit counts
    display_hit_counts()
 
    
    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()

