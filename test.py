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
    assert result["total_chains"] == 100
# test 5
def test_cardigan_neck_nonpositive_value():
    with pytest.raises(ValueError):
        calculate_cardigan_neck(-30)
    with pytest.raises(ValueError):
        calculate_cardigan_neck(0)


