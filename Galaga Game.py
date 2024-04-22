import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
ENEMY_WIDTH, ENEMY_HEIGHT = 40, 40
BULLET_WIDTH, BULLET_HEIGHT = 5, 20
PLAYER_SPEED = 5
ENEMY_SPEED = 2
BULLET_SPEED = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga")

# Clock
clock = pygame.time.Clock()

# Player
player_img = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_img.fill((255, 0, 0))
player_rect = player_img.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))

# Enemies
enemies = []
for i in range(5):
    enemy_img = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
    enemy_img.fill((0, 255, 0))
    enemy_rect = enemy_img.get_rect(midbottom=(random.randint(0, WIDTH), random.randint(-100, -ENEMY_HEIGHT)))
    enemies.append({"rect": enemy_rect, "speed": ENEMY_SPEED})

# Bullets
bullets = []

# Function to shoot bullets
def shoot_bullet():
    bullet_rect = pygame.Rect(player_rect.centerx - BULLET_WIDTH // 2, player_rect.top, BULLET_WIDTH, BULLET_HEIGHT)
    bullets.append(bullet_rect)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot_bullet()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += PLAYER_SPEED

    # Move and draw enemies
    for enemy in enemies:
        enemy["rect"].y += enemy["speed"]
        pygame.draw.rect(screen, (0, 255, 0), enemy["rect"])

    # Move and draw bullets
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        pygame.draw.rect(screen, WHITE, bullet)

    # Check for collisions between bullets and enemies
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy["rect"]):
                enemies.remove(enemy)
                bullets.remove(bullet)

    # Check for collisions between player and enemies
    for enemy in enemies:
        if player_rect.colliderect(enemy["rect"]):
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), player_rect)

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
