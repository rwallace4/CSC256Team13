import pytest
import retirement as r

#testing retirement birth years, birth months, age years and age months for correct retrieved values as well as out of bound values
@pytest.mark.parametrize("birth_year, birth_month, age_years, age_months", [(1989, 11, 30, 14), (1930, 13, 50, 11), (1990, 12, 45, 2), (1937, 0, 1, 1), (2999, 90, 12, 1), (1900, 3, 60, 1), (1700, 0,0,0), (1934, 56, 778, 100)])

def test_calculate_retirement_date(birth_year, birth_month, age_years, age_months):
    with pytest.raises(ValueError):
            r.calculate_retirement_date(birth_year, birth_month, age_years, age_months)


