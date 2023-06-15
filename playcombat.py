import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

# Box attributes
box_width, box_height = 50, 50
box1_x = screen_width // 4 - box_width // 2
box1_y = screen_height // 2 - box_height // 2
box1_speed = 5

box2_x = screen_width * 3 // 4 - box_width // 2
box2_y = screen_height // 2 - box_height // 2
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
    
    # Update bullet11 position
    if bullet1_state == "fire":
        if bullet1_x > screen_width or bullet1_x < 0:
            bullet1_state = "ready"
        else:
            if bullet1_direction == "left" and bullet1_y >= box1_y and bullet1_y <= box1_y + box_height and bullet1_x >= box1_x and bullet1_x <= box1_x + box_width:
                bullet1_state = "ready"
            elif bullet1_direction == "right" and bullet1_y >= box2_y and bullet1_y <= box2_y + box_height and bullet1_x >= box2_x and bullet1_x <= box2_x + box_width:
                bullet1_state = "ready"
            
            if bullet1_state == "fire":
                bullet1_x += fire_bullet1(bullet1_x, bullet1_y, bullet1_direction)
    
    #update bullet2 position
    if bullet2_state == "fire":
        if bullet2_x > screen_width or bullet2_x < 0:
            bullet2_state = "ready"
        else:
            if bullet2_direction == "left" and bullet2_y >= box1_y and bullet2_y <= box1_y + box_height and bullet2_x >= box1_x and bullet2_x <= box1_x + box_width:
                bullet2_state = "ready"
            elif bullet2_direction == "right" and bullet2_y >= box2_y and bullet2_y <= box2_y + box_height and bullet2_x >= box2_x and bullet2_x <= box2_x + box_width:
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
    

    
    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

# Box attributes
box_width, box_height = 50, 50
box1_x = screen_width // 4 - box_width // 2
box1_y = screen_height // 2 - box_height // 2
box1_speed = 5

box2_x = screen_width * 3 // 4 - box_width // 2
box2_y = screen_height // 2 - box_height // 2
box2_speed = 5

# Bullet attributes
bullet_width, bullet_height = 10, 5
bullet_speed = 10
bullet_state = "ready"

# Game loop
running = True
clock = pygame.time.Clock()

def box(x, y, color):
    pygame.draw.rect(screen, color, (x, y, box_width, box_height))

def fire_bullet(x, y, direction):
    global bullet_state
    bullet_state = "fire"
    pygame.draw.rect(screen, (255, 255, 255), (x, y + box_height // 2 - bullet_height // 2, bullet_width, bullet_height))
    if direction == "left":
        return -bullet_speed
    elif direction == "right":
        return bullet_speed
    return 0

while running:
    clock.tick(60)  # Set the frame rate
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = box1_x + box_width
                bullet_y = box1_y
                bullet_state = "fire"
                bullet_direction = "right"
            if event.key == pygame.K_p and bullet_state == "ready":
                bullet_x = box2_x
                bullet_y = box2_y
                bullet_state = "fire"
                bullet_direction = "left"
    
    # Handle box 1 movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box1_x -= box1_speed
    if keys[pygame.K_RIGHT]:
        box1_x += box1_speed
    if keys[pygame.K_UP]:
        box1_y -= box1_speed
    if keys[pygame.K_DOWN]:
        box1_y += box1_speed
    
    # Handle box 2 movement
    if keys[pygame.K_a]:
        box2_x -= box2_speed
    if keys[pygame.K_d]:
        box2_x += box2_speed
    if keys[pygame.K_w]:
        box2_y -= box2_speed
    if keys[pygame.K_s]:
        box2_y += box2_speed
    
    # Update bullet position
    if bullet_state == "fire":
        if bullet_x > screen_width or bullet_x < 0:
            bullet_state = "ready"
        else:
            if bullet_direction == "left" and bullet_y >= box1_y and bullet_y <= box1_y + box_height and bullet_x >= box1_x and bullet_x <= box1_x + box_width:
                bullet_state = "ready"
            elif bullet_direction == "right" and bullet_y >= box2_y and bullet_y <= box2_y + box_height and bullet_x >= box2_x and bullet_x <= box2_x + box_width:
                bullet_state = "ready"
            
            if bullet_state == "fire":
                bullet_x += fire_bullet(bullet_x, bullet_y, bullet_direction)
    

    
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw the boxes
    box(box1_x, box1_y, (255, 0, 0))
    box(box2_x, box2_y, (0, 255, 0))
    
    # Draw the bullet
    if bullet_state == "fire":
        pygame.draw.rect(screen, (255, 255, 255), (bullet_x, bullet_y + box_height // 2 - bullet_height // 2, bullet_width, bullet_height))
    
    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
