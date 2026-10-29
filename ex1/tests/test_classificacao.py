import pytest
from classificacao import classificar_aluno


def test_aprovado():
    assert classificar_aluno(8.0, 80) == "Aprovado"


def test_reprovado():
    assert classificar_aluno(3.0, 90) == "Reprovado"


@pytest.mark.parametrize("media", [-0.1, 10.1])
def test_media_invalida(media):
    with pytest.raises(ValueError, match="^Media invalida$"):
        classificar_aluno(media, 80)


@pytest.mark.parametrize("presenca", [-1, 101])
def test_presenca_invalida(presenca):
    with pytest.raises(ValueError, match="^Presenca invalida$"):
        classificar_aluno(8.0, presenca)


@pytest.mark.parametrize("media,presenca", [(0, 0), (0, 100), (10, 100), (10, 75)])
def test_limites_validos(media, presenca):
    classificar_aluno(media, presenca)


def test_media_e_presenca_invalidas_prioriza_media():
    with pytest.raises(ValueError, match="^Media invalida$"):
        classificar_aluno(11, 101)


@pytest.mark.parametrize("media,presenca,esperado", [
    (8.0, 74, "Reprovado por falta"),
    (8.0, 75, "Aprovado"),
    (0, 0, "Reprovado por falta"),
    (7.0, 75, "Aprovado"),
    (6.9, 75, "Recuperacao"),
    (5.0, 75, "Recuperacao"),
    (4.9, 75, "Reprovado"),
    (0, 100, "Reprovado"),
    (10, 100, "Aprovado"),
])
def test_fronteiras(media, presenca, esperado):
    assert classificar_aluno(media, presenca) == esperado
