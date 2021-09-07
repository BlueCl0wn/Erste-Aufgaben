# Bibliotheken
import numpy as np
import itertools

# Funktionen
from SwitchSpinOptimized import switchSpin as swSp
from  MakeGitter import getGitterV2 as getGitter

def repeat(reps, n, T, r, distanz=0, akzeptanzrate=False, GraphE=True, GraphMag=False, Abbruchbedingung=(False, None)) -> list:
    return [swSp(getGitter(n), n, T, r, distanz=0, akzeptanzrate=False, GraphE=True, GraphMag=False, Abbruchbedingung=(False, None))[1][1] for x in itertools.repeat(None, reps)]


def averageArray(my_arrays) -> np.ndarray:
    return np.mean((my_arrays), axis=0)
