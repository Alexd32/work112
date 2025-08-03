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
        @pytest.mark.parametrize(
            "x, y, expected",
            [
                (2, 3, 5),
                (-1, 1, 0),
                (0, 0, 0),
                (100, 200, 300),
            ]
        )
        def test_sum_additional(x, y, expected):
            assert calc.sum(x, y) == expected

        @pytest.mark.parametrize(
            "x, y, expected",
            [
                (6, 3, 2),
                (10, 2, 5),
                (-4, 2, -2),
                (0, 1, 0),
            ]
        )
        def test_delen_additional(x, y, expected):
            assert calc.delen(x, y) == expected

        @pytest.mark.parametrize(
            "x, y",
            [
                (1, 0),
                (0, 0),
                (-5, 0),
            ]
        )
        def test_delen_zero_division(x, y):
            with pytest.raises(ZeroDivisionError):
                calc.delen(x, y)