# Maze Solver

This project is a Python-based maze solver using **Pygame** for visualization. The program generates random mazes, solves them using algorithms, and provides a visual representation of the solution path. It also includes features like light/dark mode, fullscreen toggle, and adjustable maze sizes.

---

## Features

- **Maze Generation:**
  - Generates a random maze using the Depth-First Search (DFS) algorithm with backtracking.

- **Maze Solving:**
  - Uses the Breadth-First Search (BFS) algorithm to find the shortest path between the start and end points.

- **Interactive Visualization:**
  - Displays the maze, walls, start point, end point, and solution path.
  - Animates the solution path step-by-step.

- **Customization Options:**
  - Toggle between light and dark modes.
  - Switch between fullscreen and windowed modes.
  - Automatically adjusts maze dimensions and scaling for different screen sizes.

---

## Requirements

- Python 3.7 or above
- Pygame

Install dependencies using pip:
```bash
pip install pygame
```

---

## Usage

1. Clone the repository:
```bash
git clone https://github.com/VRJ1718/maze-solver.git
cd maze-solver
```

2. Run the main program:
```bash
python main.py
```

---

## Controls

- **`F` Key:** Toggle fullscreen mode.
- **`M` Key:** Toggle light/dark mode.
- **`ESC` Key or Close Button:** Exit the program.

---

## File Structure

- **`main.py`**
  - The main driver script for the program.

- **`maze.py`**
  - Contains the `Maze` class for generating the maze.

- **`maze_solver.py`**
  - Contains the `Maze_Solver` class for solving the maze.

- **`visuals.py`**
  - Handles all graphical rendering and visualization logic.

---

## Features in Detail

1. **Maze Generation:**
   - Uses DFS with backtracking to generate a random solvable maze.

2. **Maze Solving:**
   - Finds the shortest path using BFS.
   - Ensures optimal solution rendering.

3. **Light/Dark Mode:**
   - **Light Mode:**
     - Background: White
     - Walls: Black
     - Solution Path: Yellow
   - **Dark Mode:**
     - Background: Black
     - Walls: White
     - Solution Path: Green

4. **Fullscreen Toggle:**
   - Dynamically adjusts maze scaling for different resolutions.

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- Maze generation and solving algorithms were inspired by classic computer science concepts.
- Pygame was used for creating the interactive visualization.

---

Happy Coding!

