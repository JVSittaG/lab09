import pytest
from carrinho import total_com_desconto


def test_total_cinco_itens():
    assert total_com_desconto([10, 20, 30, 40, 50]) == 141.0


def test_tres_itens_sem_desconto():
    assert total_com_desconto([10, 20, 30]) == 60


def test_quarto_item_com_desconto():
    assert total_com_desconto([10, 20, 30, 40]) == 96.0


def test_lista_vazia():
    assert total_com_desconto([]) == 0


def test_um_item():
    assert total_com_desconto([10]) == 10


def test_precos_decimais_arredondamento():
    assert total_com_desconto([1, 1, 1, 1.11]) == 4.0


def test_precos_decimais_arredondamento_duas_casas():
    assert total_com_desconto([0.1, 0.2, 0.3, 0.55]) == 1.1


def test_preco_zero_no_desconto():
    assert total_com_desconto([5, 5, 5, 0]) == 15
