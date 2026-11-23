"""
GenAI Acknowledgment (Assessment 1 - Gen-AI-Assisted Reviewer):
In compliance with Keele University academic integrity policies and module guidelines,
generative AI (Google Gemini) was utilized strictly as an automated code reviewer. 
The tool assisted in identifying syntax typos, unhandled cases, and logical errors (such as rounding drift in garment splits and dictionary key mismatches). 
All code structures,  logic, algorithmic decisions, and test cases were written
(Help of Ai was taken on how to write these test cases and how to check that on terminal but the calculations and logic was given by Shatabdi),
 understood, and verified by Shatabdi Majumder. 
"""

# 1. All Blanket measurement Calculations size, area, yran weight and number of yarn balls needed for the project.
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

# 1.1 Pattern stich Multiples
def adjust_stich(raw_stiches: int, multiple: int=1, plus: int = 0) -> int:
    if raw_stiches <=0:
        raise ValueError("Raw stiches must be a positive number.")
    if multiple <=0:
        raise ValueError("Pattern Multiple must be a positive number")
    if plus <0:
        raise ValueError("Plus stiches must be a positive number")
    
    base = raw_stiches - plus
    remainder = base % multiple
    if remainder == 0:
        adjusted_base = base
    elif remainder >= (multiple / 2.0):
        adjusted_base = base + (multiple - remainder)
    else:
        adjusted_base =base - remainder 

    if adjusted_base <=0:
        adjusted_base = multiple
    return adjusted_base + plus

# 2. Granny Square Blanket 

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
# 3. Universal gauge calculator of the crochet project.
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
    if row_count <=0:
            raise ValueError("Row count can not be zero or negative")
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
    if stiches_in_swatch <= 0:
        raise ValueError("Stiches in swatch can not be zero or negative")
    if desired_length <=0:
        raise ValueError("Desitred length can not be zero or negative")
    if swatch_width <=0:
        raise ValueError("Swatch width can not be zero or negative")
    if turning_chains <= 0:
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
        left_front = math.ceil(half_back)
        right_front= math.ceil(half_back)
        right_front = back - left_front
        left_shoulder =round(total_chains * 0.15)
        right_shoulder= left_shoulder
        left_chain = total_chains -(left_shoulder + right_shoulder)
        back= left_chain // 2
        front= left_chain- back
        left_front = (front // 2)
        right_front = front - left_front
        return {
            "back" : back,
            "front" : front,
            "left_front" : left_front,
            "right_front": right_front,
            "left_shoulder": left_shoulder,
            "right_shoulder": right_shoulder,
            "total_chains": back + left_front + right_front + left_shoulder + right_shoulder 
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