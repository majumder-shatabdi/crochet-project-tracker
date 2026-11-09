import math
Blanket_sizes_inches = {
    "lovey": {"width":12.0, "length": 12.0},
    "security":{"width": 16.0, "length": 16.0},
    "cradle": {"width": 20.0, "length":32.0},
    "stroller": {"width": 30.0, "length": 36.0},
    "crib":{"width":40.0, "length":60.0},
    "lapghan":{"width":40.0,"length":48.0},
    "small_throw":{"width":52.0,"length":60.0},
    "large_throw":{"width":60.0,"length":72.0},
    "twin":{"width":66.0,"length":90.0},
    "queen":{"width":90.0,"length":90.0},
    "king":{"width":90.0,"length":108.0}
}


def calculate_blanket_yarn(
        blanket_width: float,
        blanket_length: float,
        square_width: float = 4.0,
        square_length: float = 4.0,
        square_weight_grams: float = 4.0,
        ball_weight_grams: float = 50.0,
)->dict:
    """ This function calculates total granny squares needed and the number balls required for each blanket size. It will always rounds yarn ball up to the next large number for example 4.1 will be 5 otherwise user will ran out of the yarn."""
# All inputs should be positive
    if blanket_width <=0 or blanket_length <=0:
        raise ValueError("Blanket Width and Length must be positive numbers.")
    if square_width <=0 or square_length <=0:
        raise ValueError("Square dimensions must be positive numbers.")
    if square_weight_grams <=0 or ball_weight_grams <=0:
        raise ValueError("Weight for each granny must be positive numbers.")
# Calculation of area of the blanket
    blanket_area = blanket_length * blanket_width
    square_area = square_width * square_length

# Square and weight calculations
    total_squares = math.ceil(blanket_area / square_area)
    total_yarn_grams = total_squares * square_weight_grams

# ball calculation ( always rounded up to next whole number)
    balls_needed = math.ceil(total_yarn_grams/ ball_weight_grams)

    return {
    "blanket_area_sq_in": blanket_area,
    "square_area_sq_in": square_area,
    "total_squares": total_squares,
    "total_yarn_grams": total_yarn_grams,
    "balls_needed": balls_needed,
    }

