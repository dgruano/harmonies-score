"""
User Interface for "Harmonies" Board Game
"""

import cv2
import numpy as np
from color_shape_detection import color_segmentation, contour_detection, draw_contours
from height_estimation import detect_overlaps, vertical_alignment_check
from scoring_logic import calculate_scores

def display_results(image, detected_pieces):
    """
    Displays the detected colors, positions, stack heights, and calculated scores on the user interface.
    
    Parameters:
    image (numpy.ndarray): Input image in BGR format.
    detected_pieces (list): List of detected pieces with their colors, positions, and heights.
    """
    for piece in detected_pieces:
        color = piece['color']
        position = piece['position']
        height = piece['height']
        
        # Draw a circle at the position of the piece
        cv2.circle(image, position, 10, (0, 255, 0), -1)
        
        # Display the color and height of the piece
        text = f"Color: {color}, Height: {height}"
        cv2.putText(image, text, (position[0] + 15, position[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    # Calculate the total score
    score = calculate_scores(detected_pieces)
    
    # Display the total score on the image
    cv2.putText(image, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Show the image with the results
    cv2.imshow("Detected Pieces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def feedback_mechanism(detected_pieces):
    """
    Provides feedback mechanisms for users to verify and adjust detected heights if necessary.
    
    Parameters:
    detected_pieces (list): List of detected pieces with their colors, positions, and heights.
    
    Returns:
    list: List of adjusted detected pieces with verified heights.
    """
    adjusted_pieces = []
    
    for piece in detected_pieces:
        color = piece['color']
        position = piece['position']
        height = piece['height']
        
        # Display the detected piece information
        print(f"Detected Piece - Color: {color}, Position: {position}, Height: {height}")
        
        # Ask the user to verify or adjust the height
        new_height = input(f"Enter the correct height for the piece at position {position} (current height: {height}): ")
        
        # Update the height if the user provided a new value
        if new_height:
            piece['height'] = int(new_height)
        
        adjusted_pieces.append(piece)
    
    return adjusted_pieces
