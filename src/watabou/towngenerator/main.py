"""Main entry point for the Medieval Fantasy City Generator."""
import sys
import argparse
from .state_manager import StateManager
from ..utils.random import Random


def main():
    """Main function to run the city generator."""
    parser = argparse.ArgumentParser(
        description='Medieval Fantasy City Generator - Python Port'
    )
    parser.add_argument(
        '--size',
        type=int,
        default=15,
        help='City size (6-40, default: 15)'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=-1,
        help='Random seed (default: random)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='city.png',
        help='Output filename (default: city.png)'
    )
    
    args = parser.parse_args()
    
    # Validate size
    if args.size < 6:
        args.size = 6
    elif args.size > 40:
        args.size = 40
    
    # Set state
    StateManager.size = args.size
    StateManager.seed = args.seed
    StateManager.push_params()
    
    print(f"Generating {StateManager.get_state_name()}...")
    print(f"Size: {StateManager.size}")
    print(f"Seed: {StateManager.seed}")
    
    # TODO: Implement city generation and rendering
    # This will require completing the conversion of:
    # - Building/Model classes
    # - Ward classes
    # - CityMap and rendering classes
    # - UI framework adaptation
    
    print("\nNote: Full city generation is not yet implemented.")
    print("The Python port is still in progress.")
    print(f"Progress: ~30% complete")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
