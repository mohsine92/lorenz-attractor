# Lorenz Attractor

A Python implementation for numerical simulation and 3D visualization of the Lorenz attractor, a classic chaotic dynamical system.

## Inspiration

This project was inspired by the work of mathematicians **Cédric Villani** and **Étienne Ghys**, whose contributions to chaos theory and nonlinear dynamical systems have been fundamental in understanding complex mathematical phenomena.

- **Cédric Villani**: Fields Medal winner (2010) for his work on the Landau damping and the Boltzmann equation, and his contributions to mathematical physics and dynamical systems.
- **Étienne Ghys**: Renowned for his work in dynamical systems, geometry, and topology, particularly in the study of chaotic systems and their visualizations.

Their research and pedagogical approach to nonlinear dynamics and chaos theory have been a significant source of inspiration for exploring these fascinating mathematical structures.

## Description

The Lorenz attractor is a system of three coupled ordinary differential equations that exhibits chaotic behavior. This project simulates multiple trajectories with different initial conditions to demonstrate the sensitivity to initial conditions, a fundamental characteristic of chaotic systems.

## System Equations

The Lorenz system is defined by the following differential equations:

```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

Where:
- **σ (sigma)** = 10 : Prandtl number
- **β (beta)** = 8/3 : Geometric parameter
- **ρ (rho)** = 28 : Rayleigh number

These standard parameter values produce the characteristic butterfly-shaped attractor.

## Installation

### Prerequisites

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install numpy matplotlib scipy pillow
```

### Running the Simulation

Execute the main script:

```bash
python lorenz_attracor.py
```

## Configuration

All simulation parameters can be easily modified at the top of `lorenz_attracor.py`:

- **System parameters**: `SIGMA`, `BETA`, `RHO`
- **Simulation parameters**: `TIME_START`, `TIME_END`, `NUM_POINTS`
- **Animation parameters**: `ANIMATION_INTERVAL`, `TRAIL_LENGTH`
- **Initial conditions**: `INITIAL_POSITIONS` (list of [x, y, z] coordinates)
- **Visualization**: `COLORS` (trajectory colors)

## Saving Animations

To save the animation as a GIF file, modify the `save_path` parameter in the `main()` function:

```python
save_path='lorenz_animation.gif'
```

**Note**: Requires `pillow` package for GIF export (included in requirements.txt).

## Features

- Numerical integration using `scipy.integrate.odeint` for accurate solutions
- Interactive 3D visualization with matplotlib
- Animated trajectories with configurable trail effect
- Support for multiple simultaneous trajectories
- Modular, well-documented codebase
- Easily configurable parameters
- Automatic axis scaling during animation

## Project Structure

```
Lorenz_Attractor/
├── lorenz_attracor.py    # Main simulation script
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore rules
```

## Code Architecture

The code is organized into modular functions:

- `lorenz_system()`: Defines the system of differential equations
- `solve_lorenz_system()`: Numerical integration for a given initial condition
- `setup_plot()`: Configures the 3D plot with proper labels and styling
- `create_animation()`: Generates and manages the animation
- `main()`: Orchestrates the simulation and visualization

## Technical Details

- **Integration method**: Adaptive Runge-Kutta method (via `odeint`)
- **Time discretization**: Uniform grid with configurable resolution
- **Visualization**: Matplotlib 3D plotting with real-time updates
- **Animation**: Frame-by-frame updates with configurable trail length

## References

- [Lorenz System - Wikipedia](https://en.wikipedia.org/wiki/Lorenz_system)
- [Edward N. Lorenz - Wikipedia](https://en.wikipedia.org/wiki/Edward_Norton_Lorenz)
- Lorenz, E. N. (1963). "Deterministic Nonperiodic Flow". Journal of the Atmospheric Sciences.
- [Cédric Villani - Wikipedia](https://en.wikipedia.org/wiki/C%C3%A9dric_Villani)
- [Étienne Ghys - Wikipedia](https://en.wikipedia.org/wiki/%C3%89tienne_Ghys)

## License

This project is provided for educational and research purposes. Feel free to use and modify as needed.

## Contributing

Contributions, issues, and feature requests are welcome. Please feel free to submit a pull request.
