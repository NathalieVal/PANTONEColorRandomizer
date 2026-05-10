import pygame


# Button Class
class Button():
    def __init__(self, x , y, image, image_hover, scale):
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), 
                                                    int(height * scale)))
        self.image_hover = pygame.transform.scale(image_hover, (int(width * scale), 
                                                int(height * scale)))   
        self.current_image = self.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
    
        # Get mouse position
        position = pygame.mouse.get_pos()

        # Check mouseover and clicked positions
        if self.rect.collidepoint(position):
            self.current_image = self.image_hover

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        else: 
            self.current_image = self.image

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            

        # Draw button on screen
        surface.blit(self.current_image, (self.rect.x, self.rect.y))
        
        return action
