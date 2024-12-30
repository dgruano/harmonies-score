"""
Scoring Logic for "Harmonies" Board Game
"""

def define_scoring_rules(piece_distribution, heights):
    """
    Defines scoring rules based on piece distribution and heights.
    
    Parameters:
    piece_distribution (dict): Dictionary with piece colors as keys and their counts as values.
    heights (list): List of heights of the pieces.
    
    Returns:
    int: Calculated score based on the rules.
    """
    score = 0
    
    # Example scoring rules
    for color, count in piece_distribution.items():
        score += count * 10  # Each piece of a color is worth 10 points
    
    for height in heights:
        score += height * 5  # Each height level is worth 5 points
    
    return score

def calculate_scores(detected_pieces):
    """
    Calculates scores dynamically based on detected pieces.
    
    Parameters:
    detected_pieces (list): List of detected pieces with their colors and heights.
    
    Returns:
    int: Total calculated score.
    """
    piece_distribution = {}
    heights = []
    
    for piece in detected_pieces:
        color = piece['color']
        height = piece['height']
        
        if color in piece_distribution:
            piece_distribution[color] += 1
        else:
            piece_distribution[color] = 1
        
        heights.append(height)
    
    score = define_scoring_rules(piece_distribution, heights)
    
    return score
