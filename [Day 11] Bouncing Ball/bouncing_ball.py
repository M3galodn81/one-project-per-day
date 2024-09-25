import pygame,sys
import random

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
running = True

class Ball:
    def __init__(self, x, y, radius, gravity=3):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
        self.gravity = gravity

        self.x_velocity = random.randint(-4,4)
        if self.x_velocity == 0:
            self.x_velocity = random.uniform(-1, 1)

        self.y_velocity = random.randint(-4,4)
        if self.y_velocity == 0:
            self.y_velocity = random.uniform(-1, 1)

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        self.y_velocity += self.gravity * 0.01

        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.x_velocity = -self.x_velocity

        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.y_velocity = -self.y_velocity
            

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


balls = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                new_ball = Ball(screen_width // 2, screen_height // 2, 20)
                balls.append(new_ball)

    # Update all the balls
    for ball in balls:
        ball.update()

        if ball.y + ball.radius >= screen_height and not last_ball_hit_ground:
            last_ball_hit_ground = True
            new_ball = Ball(screen_width // 2, screen_height // 2, 20)
            balls.append(new_ball)
            print(f"{len(balls)} balls")
        elif ball.y + ball.radius < screen_height:
            last_ball_hit_ground = False

    screen.fill("black")

    for ball in balls:
        ball.draw(screen)

    pygame.display.flip()


    clock.tick(60)
    
pygame.quit()
sys.exit()