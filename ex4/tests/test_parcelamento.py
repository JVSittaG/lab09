import pytest
from parcelamento import parcela


@pytest.mark.parametrize("n", [0, 13, -1])
def test_parcelas_invalidas(n):
    with pytest.raises(ValueError, match="^parcelas invalidas$"):
        parcela(100, n)


@pytest.mark.parametrize("n,esperado", [
    (1, 100.0),
    (2, 50.0),
    (3, 33.33),
    (4, 25.5),
    (5, 20.8),
    (12, 9.83),
])
def test_valores(n, esperado):
    assert parcela(100, n) == esperado


def test_valor_zero():
    assert parcela(0, 6) == 0


def test_arredondamento_duas_casas():
    assert parcela(10, 3) == 3.33
