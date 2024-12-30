"""
Preprocessing Module for "Harmonies" Board Game
"""

import cv2
import numpy as np

def color_correction(image):
    """
    Applies color correction techniques to normalize the input image.
    
    Parameters:
    image (numpy.ndarray): Input image in BGR format.
    
    Returns:
    numpy.ndarray: Color corrected image.
    """
    # Convert the image to LAB color space
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    # Split the LAB image into its channels
    l_channel, a_channel, b_channel = cv2.split(lab_image)
    
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to the L-channel
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l_channel = clahe.apply(l_channel)
    
    # Merge the channels back
    lab_image = cv2.merge((l_channel, a_channel, b_channel))
    
    # Convert the LAB image back to BGR format
    corrected_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)
    
    return corrected_image

def perspective_correction(image, src_points, dst_points):
    """
    Applies perspective correction to handle varying angles of image acquisition.
    
    Parameters:
    image (numpy.ndarray): Input image in BGR format.
    src_points (numpy.ndarray): Source points for perspective transformation.
    dst_points (numpy.ndarray): Destination points for perspective transformation.
    
    Returns:
    numpy.ndarray: Perspective corrected image.
    """
    # Calculate the perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    
    # Apply the perspective transformation
    corrected_image = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))
    
    return corrected_image
