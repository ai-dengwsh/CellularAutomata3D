# CellularAutomata3D

A collection of fascinating cellular automata implementations, including Rule 110, Langton's Ant, and a 3D version of Conway's Game of Life. This project demonstrates various emergent behaviors and patterns that arise from simple rules in cellular automata.

## Features

- **Rule 110**: Implementation of the famous Rule 110 cellular automaton, known for its Turing completeness
- **Langton's Ant**: Multi-ant simulation with colorful visualization
- **3D Game of Life**: A three-dimensional extension of Conway's Game of Life with interactive visualization

## Requirements

```
numpy
matplotlib
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/CellularAutomata3D.git
cd CellularAutomata3D
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Rule 110
```bash
python rule110.py
```
This will generate a 400x400 pattern following Rule 110's evolution rules.

### Langton's Ant
```bash
python langtons_ant.py
```
Runs a simulation with 3 ants on a 200x200 grid, each ant having its own color.

### 3D Game of Life
```bash
python game_of_life_3d.py
```
Simulates a 20x20x20 3D version of Conway's Game of Life with animated visualization.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or find any bugs.

## License

This project is open source and available under the MIT License.
