# Bouncy Ball Simulation

This Python project uses **Pygame** and **Pymunk** to simulate balls bouncing inside a container. The balls are assigned random velocities and colors, and continuously bounce off walls. When a ball exits through a gap in the wall, 3 more are added. The simulation stops when a certain number of balls are reached.

## Features

- Realistic 2D physics using `pymunk`
- Multicolored balls with randomized movement
- Automatic ball multiplication when a ball exits
- Simulation halts after 610 balls are created

## Requirements

- Python 3.x
- `pygame`
- `pymunk`

You can install dependencies via pip:

```bash
pip install pygame pymunk
