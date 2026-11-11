# 1. All Blanket measurement Calculations size, area, yran weight and number of yarn balls needed for the project.
import math
from turtle import back
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
# Universal gauge calculator of the crochet project.
def calculate_gauge(swatch_dimension: float, 
                    stich_count:int,
                    row_count: int
                    )-> dict:
    """ Calculates the row density per inch or cm from a test swach.
    Using Raise ValueError if any input is zero or negative"""
    if swatch_dimension <=0:
        raise ValueError("Swatch dimension must be a positive number")
    if stich_count <=0:
        raise ValueError("Stich count can not be zero or negative")
    stiches_per_unit = stich_count / swatch_dimension
    rows_per_unit = row_count / swatch_dimension
    return {
        "stiches_per_unit": round(stiches_per_unit,2),
        "rows_per_unit": round(rows_per_unit,2)

    }

#3. Muffler foundation chain calculator
def calculate_muffler_chain(
        desired_length: float,
        swatch_width: float,
        stiches_in_swatch: int,
        turning_chains: int = 2, 
)-> int:
    """ Formula for muffler = ( Desired Muffler Length / Swatch Width) x Stiches in Swatch + Turning Chains.
    Note: Turninng chains in most project is 2 unless using double crochet stiches."""
    if desired_length <=0:
        raise ValueError("Desitred length can not be zero or negative")
    if swatch_width <=0:
        raise ValueError("Swatch width can not be zero or negative")
    if turning_chains < 0:
        raise ValueError("Turning chains can not be negative")
    raw_chains = (desired_length / swatch_width) * stiches_in_swatch
    return round(raw_chains) + turning_chains

#4. Crochet Cardigan neck line stich calculator which is the base and depending on the body measurements depnds."

def calculate_cardigan_neck(
        total_chains: int
        ) -> dict:
    #35% of the original chain will beon the front and that equal number will be on the back and 15% of the chain will be on shoulders
        if total_chains <=0:
            raise ValueError("Total chains can not be zero or negative")
        back= round(total_chains * 0.35)
        half_back = back/2
        left_front = round(half_back)
        right_front= round(half_back)
        right_front = back - left_front
        left_shoulder =round(total_chains * 0.15)
        right_shoulder= round(total_chains * 0.15)
        current_sum = back + left_front+ right_front+ left_shoulder + right_shoulder
        difference = total_chains - current_sum
        if difference != 0:
            adjustment = round(difference/2)
            left_shoulder -=adjustment
            right_shoulder-=(difference-adjustment)
        return{
            "back": back,
            "left_front": left_front,
            "right_front": right_front,
            "left_shoulder": left_shoulder,
            "right_shoulder": right_shoulder,
            "total": back + left_front + right_front + left_shoulder + right_shoulder
        }

# 5. Time estimation 
def estimate_crafting_time(
        total_stiches: int,
        stiches_per_minute: int =20,
)->dict:
    if total_stiches <=0:
        raise ValueError("Total stiches can not be negative or zero")
    if stiches_per_minute <=0:
        raise ValueError("Stiches per minute cannot be negative or zero")
    total_minutes = total_stiches / stiches_per_minute
    hours= int(total_minutes // 60)  
    minutes = round(total_minutes % 60)
    return{
        "total_minutes": total_minutes,
        "hours": hours,
        "minutes": minutes,
        "formatted":f"{hours} hr {minutes} min",   
          }    