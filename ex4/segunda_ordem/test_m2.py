import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from parcelamento_m2 import parcela


def test_suite_mata_mutante_de_segunda_ordem():
    sobreviveu = all(parcela(100, n) == esperado for n, esperado in [
        (1, 100.0), (2, 50.0), (3, 33.33), (4, 25.5), (5, 20.8), (12, 9.83),
    ])
    assert not sobreviveu
