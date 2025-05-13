import pygame
import pymunk
import random

def add_wall(space, pos1, pos2):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, pos1, pos2, 5)
    space.add(body, shape)
    return shape

def random_color():
    """Generate a random color"""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def add_ball(space, pos, balls):
    mass = 1  # Mass of the ball
    radius = 10  # Radius of the ball
    moment = pymunk.moment_for_circle(mass, 0, radius)  # Moment of inertia
    body = pymunk.Body(mass, moment)
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.9  # High elasticity for bouncing
    shape.friction = 0.0  # No friction so balls don't slow down
    body.damping = 0.0  # No damping (no energy loss)
    
    # Set random initial velocity to move in all directions (including vertical, diagonal, etc.)
    body.velocity = (random.uniform(-380, 380), random.uniform(-380, 380))  # Increased velocity range
    space.add(body, shape)
    
    # Assign a random color to the ball
    color = random_color()
    balls.append((shape, color))  # Store the ball and its color

def main():
    # Setup
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bouncy Balls with Walls")
    clock = pygame.time.Clock()

    # Physics space setup
    space = pymunk.Space()
    space.gravity = (0, 0)  # No gravity for this simulation

    # Create walls (container) and store shapes to draw
    walls = []
    walls.append(add_wall(space, (100, 100), (700, 100)))  # Top
    walls.append(add_wall(space, (100, 500), (700, 500)))  # Bottom
    walls.append(add_wall(space, (100, 100), (100, 500)))  # Left (full wall)
    walls.append(add_wall(space, (700, 100), (700, 400)))  # Right (full wall)

    # Half a wall on the left side (only the top half of the wall)
    walls.append(add_wall(space, (100, 100), (100, 300)))  # Half of the left wall (top to middle)

    # Ball list
    balls = []

    # Add 10 balls with random colors
    for i in range(10):
        add_ball(space, (400 + i * 10, 200), balls)  # Spread balls out

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the physics world
        space.step(1/60)  # Update physics

        # Ensure balls keep moving and don't freeze
        for ball, _ in balls:
            if abs(ball.body.velocity.x) < 90 and abs(ball.body.velocity.y) < 90:
                ball.body.velocity = (random.uniform(-230, 230), random.uniform(-230, 230))

        # Check if any balls have left the box (x > 700) and add 3 new balls
        for ball, _ in balls[:]:
            if ball.body.position.x > 700:  # Ball leaves the box (goes past the right wall)
                balls.remove((ball, _))  # Remove the ball that left
                # Add 3 new balls in random positions, if there are fewer than 610 balls
                if len(balls) < 610:  # Stop when there are 610 balls in the box
                    for _ in range(3):
                        add_ball(space, (random.randint(100, 700), random.randint(100, 400)), balls)
                else:
                    running = False  # Stop the simulation when there are 610 balls

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw walls (including the half-wall)
        for wall in walls:
            pygame.draw.lines(screen, (255, 255, 255), False, [(wall.a.x, wall.a.y), (wall.b.x, wall.b.y)], 5)

        # Draw balls with their respective random colors
        for ball, color in balls:
            pygame.draw.circle(screen, color, (int(ball.body.position.x), int(ball.body.position.y)), 10)

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
