# harmonies-score

## Project Description

The "Harmonies" Board Game Computer Vision Tool is designed to detect colored pieces on a hexagonal grid, determine their stacking height, and calculate scores based on piece distribution and height. This tool aims to enhance the gameplay experience by providing accurate and dynamic scoring based on the detected pieces.

### Objectives

- Detect colored pieces on a hexagonal grid.
- Determine the stacking height of the pieces.
- Calculate scores based on piece distribution and height.
- Provide a user-friendly interface for displaying detected colors, positions, stack heights, and calculated scores.
- Allow users to verify and adjust detected heights if necessary.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/dgruano/harmonies-score.git
   cd harmonies-score
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. Capture images of the game board following the provided guidelines.
2. Run the tool to process the images and detect the pieces.
3. View the detected colors, positions, stack heights, and calculated scores on the user interface.
4. Verify and adjust detected heights if necessary.

## Examples

### Expected Input Images

![Example Input Image](docs/images/example_input.jpg)

### Corresponding Outputs

![Example Output Image](docs/images/example_output.jpg)
