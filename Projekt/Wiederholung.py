# Bibliotheken
import numpy as np
import itertools

# Funktionen
from SwitchSpinOptimized import switchSpin as swSp
from  MakeGitter import getGitterV2 as getGitter


def repeatAll(reps, n, beta, r, distanz=0, abbruch=100) -> np.ndarray:
    """Returned einen Liste mit mit allen Rückgabe-Arrays von reps Durchläufen"""
    return [swSp(getGitter(n), n, beta, r, distanz, akzeptanzrate=True, GraphE=True, Abbruchbedingung=(True, abbruch)) for x in itertools.repeat(None, reps)]

def repeatChoose(reps, n, beta, r, pos, distanz=0, akzeptanzrate=False, GraphE=True, Abbruchbedingung=(True, 100)) -> np.ndarray:
    """Returned einen Liste mit den Arrays an der Position pos von den Rückgabewerten vonswitchSpin von reps
    Durchläufen """
    return [swSp(getGitter(n), n, beta, r, distanz, akzeptanzrate, GraphE, Abbruchbedingung)[pos] for x in itertools.repeat(None, reps)]


def repeatE_Graph(reps, n, beta, r, distanz=0, akzeptanzrate=False, GraphE=True, Abbruchbedingung=(True, 100)) -> np.ndarray:
    """Returned einen Liste mit den Arrays für die Energie-Graphen von reps Durchläufen"""
    return [swSp(getGitter(n), n, beta, r, distanz, akzeptanzrate, GraphE, Abbruchbedingung)[1] for x in itertools.repeat(None, reps)]
