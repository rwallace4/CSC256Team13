import pytest
import retirement as r


##TESTING FOR CALCULATE RETIREMENT AGE-------------------------------------------------------------------------------------------
#How do I test two outputs using parametrize?
@pytest.mark.parametrize("test_input, expected", [(1937, (65, 0)), (1938, (65,2)), (1939, (65,4)), (1940, (65, 6)), (1941, (65, 8)), (1942, (65, 10)), (1943, (66,0)), (1954, (66,0)), (1955, (66,2)), (1956, (66,4)), (1957, (66,6)), (1958, (66,8)), (1959, (66,10)), (1960, (67,0)), (2000, (67,0))])
def test_calculate_retirement_age(test_input, expected):
    assert r.calculate_retirement_age(test_input) == expected

#
# #testing validation for birth year in calculate retirement age
# #testing birth year is greater than or equal to 1900
@pytest.mark.parametrize("test_input, expected", [(1900, True), (1850, False), (1910, True)])
def test_birth_year_greater_than_1900(test_input, expected):
    assert eval(test_input) == expected
 #testing birth year is less than or equal to 3000
@pytest.mark.parametrize("test_input, expected", [(2999, True), (3000, False), (1910, True)])
def test_birth_year_less_than_3000(test_input, expected):
    assert eval(test_input) == expected

#----------------------------------------------------------------------------------------------------------------------------------


