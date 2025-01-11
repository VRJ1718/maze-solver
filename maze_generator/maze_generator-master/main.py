import pygame
from pygame.locals import *
from maze import Maze
from maze_solver import Maze_Solver
import time

# Initialization
pygame.init()

size = width, height = 800, 800
margin = 100

# Colors for Light and Dark Modes
light_mode_colors = {
    "bg": (255, 255, 255),  # White background
    "wall": (0, 0, 0),      # Black walls
    "solution": (255, 255, 0),  # Yellow solution path
    "start": (0, 0, 255),       # Blue start point
    "end": (255, 0, 0)          # Red end point
}

dark_mode_colors = {
    "bg": (0, 0, 0),        # Black background
    "wall": (255, 255, 255),# White walls
    "solution": (0, 255, 0),     # Green solution path
    "start": (0, 0, 255),       # Blue start point
    "end": (255, 0, 0)          # Red end point
}

# Default Mode
is_dark_mode = True
colors = dark_mode_colors

# Pygame Window Setup
screen = pygame.display.set_mode(size, RESIZABLE)
clock = pygame.time.Clock()
is_fullscreen = False

# Maze Parameters
MAZE_SIZE = (30, 40)
CELL_SIZE = min((width - 2 * margin) // MAZE_SIZE[0], (height - 2 * margin) // MAZE_SIZE[1])

# Generate Maze
start_time = time.time()
m = Maze(MAZE_SIZE)
end_time = time.time()
print(f"{MAZE_SIZE[0]}x{MAZE_SIZE[1]} Maze generated in {end_time - start_time:.2f} seconds")

# Define Start and End Points
start_point = (0, 0)  # Fixed start point (top-left)
end_point = (MAZE_SIZE[0] - 1, MAZE_SIZE[1] - 1)  # Fixed end point (bottom-right)

# Solve Maze
solver = Maze_Solver(m)
solver.solve(start=start_point, end=end_point)
solution = solver.get_solution()
solution.reverse()  # Reverse solution for correct animation

# Drawing Variables
def calculate_cell_size():
    global width, height, CELL_SIZE, bx, by
    CELL_SIZE = min((width - 2 * margin) // MAZE_SIZE[0], (height - 2 * margin) // MAZE_SIZE[1])
    bx = (width - CELL_SIZE * MAZE_SIZE[0]) // 2
    by = (height - CELL_SIZE * MAZE_SIZE[1]) // 2

calculate_cell_size()

# Animation Variables
step_index = 0  # Tracks animated solution progress
animation_speed = 2  # Animation speed

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_f:  # Toggle fullscreen mode
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode((0, 0), FULLSCREEN)
                    info = pygame.display.Info()
                    width, height = info.current_w, info.current_h
                else:
                    screen = pygame.display.set_mode(size, RESIZABLE)
                    width, height = size
                calculate_cell_size()
            elif event.key == K_m:  # Toggle light/dark mode
                is_dark_mode = not is_dark_mode
                colors = dark_mode_colors if is_dark_mode else light_mode_colors

    screen.fill(colors["bg"])

    # Draw Maze Walls
    for x in range(MAZE_SIZE[0]):
        for y in range(MAZE_SIZE[1]):
            # Draw Vertical Walls
            if not (x - 1, y, x, y) in m.doors:
                pygame.draw.line(screen, colors["wall"], (bx + x * CELL_SIZE, by + y * CELL_SIZE),
                                 (bx + x * CELL_SIZE, by + (y + 1) * CELL_SIZE))
            # Draw Horizontal Walls
            if not (x, y - 1, x, y) in m.doors:
                pygame.draw.line(screen, colors["wall"], (bx + x * CELL_SIZE, by + y * CELL_SIZE),
                                 (bx + (x + 1) * CELL_SIZE, by + y * CELL_SIZE))

    # Draw Start Point
    sx, sy = start_point
    pygame.draw.rect(screen, colors["start"],
                     (bx + sx * CELL_SIZE, by + sy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw End Point
    ex, ey = end_point
    pygame.draw.rect(screen, colors["end"],
                     (bx + ex * CELL_SIZE, by + ey * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw Animated Solution Path
    for i in range(min(step_index, len(solution) - 1)):
        x1, y1 = solution[i]
        x2, y2 = solution[i + 1]

        # Only draw connections for adjacent cells
        if abs(x1 - x2) + abs(y1 - y2) == 1:
            pygame.draw.line(screen, colors["solution"],
                             (bx + x1 * CELL_SIZE + CELL_SIZE // 2, by + y1 * CELL_SIZE + CELL_SIZE // 2),
                             (bx + x2 * CELL_SIZE + CELL_SIZE // 2, by + y2 * CELL_SIZE + CELL_SIZE // 2), 5)

    # Update Animation Step
    if step_index < len(solution) - 1:
        step_index += animation_speed

    pygame.display.update()
    clock.tick(20)
