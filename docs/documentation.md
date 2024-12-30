# Harmonies Board Game Computer Vision Tool Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage Instructions](#usage-instructions)
4. [Troubleshooting](#troubleshooting)
5. [Examples](#examples)

## Introduction
The "Harmonies" Board Game Computer Vision Tool is designed to detect colored pieces on a hexagonal grid, determine their stacking height, and calculate scores based on piece distribution and height. This tool aims to enhance the gameplay experience by providing accurate and dynamic scoring based on the detected pieces.

## Installation
To install the tool, follow these steps:

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

## Usage Instructions
1. Capture images of the game board following the provided guidelines.
2. Run the tool to process the images and detect the pieces.
3. View the detected colors, positions, stack heights, and calculated scores on the user interface.
4. Verify and adjust detected heights if necessary.

### Image Capture Guidelines
- Ensure the game board is placed on a flat, non-reflective surface.
- Use a high-resolution camera for better image quality.
- Maintain a consistent distance between the camera and the game board.
- Avoid using digital zoom; instead, physically move the camera closer if needed.
- Capture images in a well-lit environment to avoid shadows and reflections.
- Use natural light or diffuse artificial light to minimize glare.
- Ensure the entire game board is within the frame of the image.
- Capture images from a top-down perspective, perpendicular to the game board.
- Avoid tilting the camera to prevent perspective distortion.
- Take multiple images from different angles if necessary.

### Lighting Recommendations
- Use natural light whenever possible.
- If using artificial light, use soft, diffuse lighting to avoid harsh shadows.
- Position the light source to minimize reflections on the game board.
- Avoid direct overhead lighting that can cause glare.
- Use multiple light sources from different angles to ensure even lighting.
- Test the lighting setup by capturing a few test images and adjusting as needed.

### Background Recommendations
- Use a plain, non-reflective background to avoid distractions.
- Choose a background color that contrasts with the game pieces for better visibility.
- Ensure the background is free from clutter and other objects.
- Avoid using patterned or textured backgrounds that can interfere with image processing.

### Camera Angle Recommendations
- Capture images from a top-down perspective, perpendicular to the game board.
- Avoid tilting the camera to prevent perspective distortion.
- If capturing images from different angles, ensure the game board remains in the same position.
- Use a tripod or stable surface to keep the camera steady.
- Take multiple images from different angles if necessary to capture all details.

## Troubleshooting
If you encounter any issues while using the tool, consider the following troubleshooting tips:

- Ensure that the captured images meet the provided guidelines for lighting, background, and camera angles.
- Verify that the required dependencies are installed correctly.
- Check for any error messages in the console and refer to the documentation for possible solutions.
- If the detected heights are incorrect, use the user interface to manually adjust the heights.

## Examples

### Expected Input Images

![Example Input Image](images/example_input.jpg)

### Corresponding Outputs

![Example Output Image](images/example_output.jpg)
