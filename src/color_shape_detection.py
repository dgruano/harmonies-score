"""
Color and Shape Detection for "Harmonies" Board Game
"""

import cv2
import numpy as np

def color_segmentation(image, lower_hsv, upper_hsv):
    """
    Applies color segmentation to identify pieces by color using HSV thresholding.
    
    Parameters:
    image (numpy.ndarray): Input image in BGR format.
    lower_hsv (tuple): Lower bound of HSV values for color segmentation.
    upper_hsv (tuple): Upper bound of HSV values for color segmentation.
    
    Returns:
    numpy.ndarray: Mask of the segmented color.
    """
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Create a mask using the specified HSV range
    mask = cv2.inRange(hsv_image, lower_hsv, upper_hsv)
    
    return mask

def contour_detection(mask):
    """
    Detects contours in the given mask and outlines hexagonal shapes of the pieces.
    
    Parameters:
    mask (numpy.ndarray): Mask of the segmented color.
    
    Returns:
    list: List of detected contours.
    """
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    hexagonal_contours = []
    
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Check if the polygon has 6 sides (hexagon)
        if len(approx) == 6:
            hexagonal_contours.append(approx)
    
    return hexagonal_contours

def draw_contours(image, contours):
    """
    Draws the detected contours on the input image.
    
    Parameters:
    image (numpy.ndarray): Input image in BGR format.
    contours (list): List of detected contours.
    
    Returns:
    numpy.ndarray: Image with drawn contours.
    """
    # Draw the contours on the image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    
    return image
