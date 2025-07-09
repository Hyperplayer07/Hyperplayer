import pygame
import sys
SPEED_MULTIPLIER = 10
class Ball:
    def __init__(self, x, y, radius, mass, color, velocity):
        self.init_x = x
        self.init_velocity = velocity
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color
        self.velocity = velocity
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
    def update_position(self):
        self.x += self.velocity * SPEED_MULTIPLIER
    def reset(self):
        self.x = self.init_x
        self.velocity = self.init_velocity
def elastic_collision(ball1, ball2):
    m1, m2 = ball1.mass, ball2.mass
    v1, v2 = ball1.velocity, ball2.velocity
    ball1.velocity = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    ball2.velocity = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
pygame.mixer.init()
hit_sound = pygame.mixer.Sound("hit.wav")
def main():
    pygame.init()
    width, height = 1400, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Galperin π 충돌 실험")
    clock = pygame.time.Clock()
    font = pygame.font.Font("NanumGothic.ttf",30)
    small_ball = Ball(200, height - 50, 20, 1, (255, 0, 0), 0)
    n = 0
    big_ball = Ball(600, height - 50, 40, 100 ** n, (0, 0, 255), -0.1)
    collision_count = 0
    running = True
    simulating = False

    while running:
        clock.tick(1200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    simulating = True
                elif event.key == pygame.K_RSHIFT:
                    small_ball.reset()
                    big_ball.reset()
                    collision_count = 0
                    simulating = False
                elif event.key == pygame.K_UP:
                    if n < 5:
                        n += 1
                        big_ball.mass = 100 ** n
                elif event.key == pygame.K_DOWN:
                    if n > 0:
                        n -= 1
                        big_ball.mass = 100 ** n
        if simulating:
            if big_ball.x - big_ball.radius <= small_ball.x + small_ball.radius:
                elastic_collision(big_ball, small_ball)
                collision_count += 1
                hit_sound.play()
            if small_ball.x <= 20:
                small_ball.velocity = -small_ball.velocity
                collision_count += 1
                hit_sound.play()
            small_ball.update_position()
            big_ball.update_position()
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (100, 100, 100), (0, height - 30, width, 30))
        small_ball.draw(screen)
        big_ball.draw(screen)
        screen.blit(font.render(f"충돌 횟슈: {collision_count}", True, (0, 0, 0)), (10, 10))
        screen.blit(font.render(f"작은 공 -  질량 = 1 / 속도 = {small_ball.velocity:.4f}", True, (255, 0, 0)), (10, 50))
        screen.blit(font.render(f"큰 공 : 질량 = 100^{n} = {big_ball.mass:.0f} / 속도 = {big_ball.velocity:.4f}", True, (0, 0, 255)), (10, 90))
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()