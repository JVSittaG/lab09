import pytest
from temperaturas import maior, dia_do_maior


def test_maior_lista_semana():
    assert maior([21, 25, 19, 30, 22]) == 30


def test_maior_um_elemento():
    assert maior([18]) == 18


def test_maior_primeiro_e_maior():
    assert maior([30, 21]) == 30


def test_maior_segundo_e_maior():
    assert maior([21, 30]) == 30


def test_maior_lista_vazia():
    with pytest.raises(ValueError):
        maior([])


def test_dia_do_maior_lista_semana():
    assert dia_do_maior([21, 25, 19, 30, 22]) == 3


def test_dia_do_maior_um_elemento():
    assert dia_do_maior([18]) == 0


def test_dia_do_maior_primeiro_e_maior():
    assert dia_do_maior([30, 21]) == 0


def test_dia_do_maior_segundo_e_maior():
    assert dia_do_maior([21, 30]) == 1


def test_dia_do_maior_empate_devolve_primeiro():
    assert dia_do_maior([30, 21, 30]) == 0


def test_dia_do_maior_lista_vazia():
    with pytest.raises(ValueError):
        dia_do_maior([])
