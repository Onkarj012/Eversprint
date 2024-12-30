import pygame
import os

class PlayerAnimation(pygame.sprite.Sprite):
    def __init__(self, x, y, animation_type):
        super().__init__()
        self.animation_frames = self.load_animation(animation_type)
        self.current_frame = 0
        self.animation_speed = 8  # Adjust for animation speed
        self.animation_timer = 0

        # Set the initial image and position
        self.image = self.animation_frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=(x, y))

    def load_animation(self, animation_type):
        """Load frames for a specific animation type."""
        animation_path = f"assets/images/player/{animation_type}/"
        frame_files = sorted(os.listdir(animation_path))  # Sort to ensure frames are in order
        frames = [
            pygame.transform.scale(
                pygame.image.load(os.path.join(animation_path, frame)).convert_alpha(),
                (pygame.image.load(os.path.join(animation_path, frame)).get_width() * 4,
                 pygame.image.load(os.path.join(animation_path, frame)).get_height() * 4)  # Scale by 4x
            )
            for frame in frame_files
        ]
        return frames

    def update(self, dt):
        # Update the animation timer
        self.animation_timer += self.animation_speed * dt
        if self.animation_timer >= 1:
            self.animation_timer = 0
            # Advance to the next frame (looping)
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.image = self.animation_frames[self.current_frame]
