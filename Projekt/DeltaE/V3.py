import Projekt.DetermineCharge as DC


# Definition der Boltzmann-Konstanten
kBoltzmann = 1.380649e-23

def beta(T):
    """Berechnet beta."""
    return 1/(kBoltzmann * T)

def deltaE(conf_alt, altE, pos, charge, n):
    """Berechnet den Energieunterschied des Systems nach dem Umdrehen eines Spins."""
    n -= 1

    neuE = altE

    neuE -= DC.getCharge(conf_alt, pos[0], pos[1],  n)

    neuE += charge
    neuE += conf_alt[pos[0] - 1][pos[1]] if pos[0] >= 0 else 0
    neuE += conf_alt[pos[0] + 1][pos[1]] if pos[0] <= (n-1) else 0
    neuE += conf_alt[pos[0]][pos[1] - 1] if pos[1] >= 0 else 0
    neuE += conf_alt[pos[0]][pos[1] + 1] if pos[1] <= (n-1) else 0


    return neuE - altE
