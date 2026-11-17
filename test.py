import pytest
from core import calculate_blanket_yarn
#(90" x 108") Blanket with 4" x 4" granny squares and 50 gram milk cotton yarn balls
result = calculate_blanket_yarn(90.0,108.0)
assert result["blanket_area_sq_in"] == 9720.0
assert result["square_area_sq_in"]== 16.0
assert result["total_squares"] == 608
assert result["total_yarn_grams"] == 2432
assert result["balls_needed"] == 49
# Test 1
def test_blanket_yarn_calculation_upperbound():
    result = calculate_blanket_yarn(4.0,4.0)
    assert result["total_squares"] == 1
    assert result["balls_needed"] == 1
# test 2
def test_blanket_rejects_npositive():
# For Negative or zero input
    with pytest.raises(ValueError):
        calculate_blanket_yarn(-36.0,48.0)
    with pytest.raises(ValueError):
        calculate_blanket_yarn(0,108.0)
    with pytest.raises(ValueError):
        calculate_blanket_yarn(36.0, 48.0, square_weight_grams=-4.0)
# Test 3
from core import calculate_blanket_yarn, calculate_cardigan_neck

def test_cardigan_neck():
# The stnadard measurement taken from youtube
    result = calculate_cardigan_neck(117)
    assert result["back"] == 40
    assert result["left_front"] == 20
    assert result["right_front"] ==21
    assert result["left_shoulder"] == 18
    assert result["right_shoulder"] == 18
    assert result["total_chains"] == 117

# test 4
def test_cardigan_neck_for_any_total():
    result = calculate_cardigan_neck(100)
    assert result["back"]== 35
    assert result["left_front"] == 17
    assert result["right_front"] == 18
    assert result["left_shoulder"] == 15
    assert result["right_shoulder"] == 15
    assert result["total_chains"] == 100
# test 5
def test_cardigan_neck_nonpositive_value():
    with pytest.raises(ValueError):
        calculate_cardigan_neck(-30)
    with pytest.raises(ValueError):
        calculate_cardigan_neck(0)


from core import(
    calculate_gauge,
    adjust_stich,
    calculate_muffler_chain,
    estimate_crafting_time
)
# Test 6 : gauge calculation

result = calculate_gauge(4.0,16,20)
assert result["stiches_per_unit"] == 4.0
assert result["rows_per_unit"] == 5.0

def test_gauge_nonpositive_numbers():
    with pytest.raises(ValueError):
        calculate_gauge(4,-12,20)
    with pytest.raises(ValueError):
        calculate_gauge(0,20,32)
    with pytest.raises(ValueError):
        calculate_gauge(2, 16, -32)
    with pytest.raises(ValueError):
        calculate_gauge(5, 0, 35)

assert adjust_stich(100,multiple =3, plus= 1) == 100
assert adjust_stich(107, multiple = 4, plus= 2) == 106

#Test 7 : Muffler cahin calculation
def test_muffler_chain(): 
    assert calculate_muffler_chain(60.0, 4.0, 16, turning_chains = 2) == 242

#Test 8 : Test muffler stich doesn't take negative or zero value
def test_muffler_nonpositive_number():
    with pytest.raises(ValueError):
        calculate_muffler_chain(16, 3, -2)
    with pytest.raises(ValueError):
        calculate_muffler_chain(60,0, 20)

result = estimate_crafting_time(1926, 20)
assert result["hours"] == 1
assert result["minutes"] == 36
assert result["formatted"] == "1 hr 36 min"

#Test 9: Time estimation under one hour
def test_time_under_hour():
    result = estimate_crafting_time(100, 20)
    assert result["hours"] == 0      # Added the 's'
    assert result["minutes"] == 5    # Changed 'min' to 'minutes'
    assert result["formatted"] == "0 hr 5 min"
#Test 10: Non positive number for time estimation

def test_nonpositive_number():
    with pytest.raises(ValueError):
        estimate_crafting_time(-1937, 20)
    with pytest.raises(ValueError):
        estimate_crafting_time(2067, -20)
    with pytest.raises(ValueError):
        estimate_crafting_time(0, 20)



