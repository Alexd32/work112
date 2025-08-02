import pytest
from calc import calc

class TestCalc:
    @pytest.mark.parametrize(
        "x, y, rez",
        [
            (1,2,0.5),
            (4,2,2),
            (1,1,1),
            (5,5,1)
        ]
    )
    def test_delen(self, x, y, rez):
        assert calc.delen(x, y) == rez


    @pytest.mark.parametrize(
        "x, y, rez",
        [
            (1,2,3),
            (4,2,6),
            (1,1,2),
            (5,5,10)
        ]
    )
    def test_sum(self, x, y, rez):
        assert calc.sum(x, y) == rez