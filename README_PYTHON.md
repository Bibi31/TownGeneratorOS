# Medieval Fantasy City Generator - Python Port

This is a Python port of the Medieval Fantasy City Generator, originally written in Haxe/OpenFL.

## Original Project

The original project can be found at:
- Live version: https://watabou.itch.io/medieval-fantasy-city-generator/
- Alternative: http://fantasycities.watabou.ru/

## Python Port Status

This Python port is currently **IN PROGRESS**. The following modules have been converted:

### ✅ Completed Modules

#### Utilities (`src/watabou/utils/`)
- `random.py` - Random number generator with seed support
- `math_utils.py` - Math utility functions (clamp, sign, etc.)
- `string_utils.py` - String manipulation utilities
- `null_utils.py` - Null/None handling utilities
- `perlin_noise.py` - Perlin noise implementation
- `markov_chain.py` - Markov chain for sequence generation
- `array_utils.py` - Array/list utility functions
- `point.py` - 2D point class with geometric operations
- `observable.py` - Observable pattern implementation
- `stopwatch.py` - Timing utilities

#### Geometry (`src/watabou/geom/`)
- `geom_utils.py` - Geometry utility functions
- `segment.py` - Line segment class
- `circle.py` - Circle class
- `polygon.py` - Polygon class with extensive geometric operations
- `spline.py` - Spline curve utilities

#### Town Generator (`src/watabou/towngenerator/`)
- `state_manager.py` - Application state management
- `mapping/palette.py` - Color palettes for rendering

### 🚧 To Be Converted

- Graph and Voronoi diagram implementations
- UI framework (coogee) - needs adaptation to Python GUI (pygame/pyglet/tkinter)
- Building generation modules
- Ward (district) modules
- Mapping visualization modules
- UI components (buttons, tooltips, etc.)
- Main application entry point

## Installation

### Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

### Setup

```bash
# Clone the repository
git clone https://github.com/Bibi31/TownGeneratorOS.git
cd TownGeneratorOS

# Install dependencies
pip install -r requirements.txt
```

## Usage

**Note:** The Python port is not yet complete. Once finished, it will support:

```bash
# Generate a city with default parameters
python -m watabou.towngenerator.main

# Generate with specific size and seed
python -m watabou.towngenerator.main --size 15 --seed 12345
```

## Architecture

The codebase is organized into several modules:

- **utils/** - General utility functions and classes
- **geom/** - Geometric primitives and algorithms
- **coogee/** - UI framework (to be adapted for Python)
- **towngenerator/** - Core city generation logic
  - **building/** - Building placement and generation
  - **wards/** - City district types (slums, markets, castles, etc.)
  - **mapping/** - Map rendering and visualization
  - **ui/** - User interface components

## Converting from Haxe

The original Haxe code used OpenFL (similar to Flash/ActionScript) for graphics. The Python port will use one of the following:

- **pygame** - For 2D graphics and UI (default choice)
- **pyglet** - Alternative graphics library
- **tkinter** - Built-in Python GUI (simpler but less powerful)

## Development Status

This is an active conversion project. The conversion progress is:
- **17/59 files converted** (~29%)
- Core utilities: ✅ Complete
- Geometry system: ✅ Complete
- Game framework: ⏳ In Progress
- City generation: ⏳ In Progress
- Rendering/UI: ⏳ In Progress

## License

The original project's license applies to this port. See LICENSE file for details.

## Credits

- Original Haxe version by Oleg Dolya (watabou)
- Python port in progress

## Contributing

Contributions are welcome! If you'd like to help complete the Python port:

1. Pick a module from the "To Be Converted" list
2. Convert it maintaining the original logic
3. Test the converted code
4. Submit a pull request

## Original README

For information about the original Haxe version, see the project description above.
