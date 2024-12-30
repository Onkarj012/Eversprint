import pygame
from entities.player import PlayerAnimation
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SKY_BLUE

class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

        # Create animations and position them on the screen
        self.idle_animation = PlayerAnimation(100, 300, "idle")
        self.run_animation = PlayerAnimation(300, 300, "run")
        self.hurt_animation = PlayerAnimation(500, 300, "hurt")
        self.death_animation = PlayerAnimation(700, 300, "death")

        self.all_sprites.add(
            self.idle_animation,
            self.run_animation,
            self.hurt_animation,
            self.death_animation,
        )

    def update(self, dt):
        # Update all animations
        self.all_sprites.update(dt)

    def render(self, screen):
        # Fill the background
        screen.fill(SKY_BLUE)
        # Draw all animations
        self.all_sprites.draw(screen)
