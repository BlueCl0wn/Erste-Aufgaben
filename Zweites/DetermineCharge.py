def getCharge(my_arr, i, j, n):
    """Berechnet die Energie eines einzelnen Spins."""
    charge = my_arr[i][j]
    charge += my_arr[i - 1][j] if i >= 0 else 0
    charge += my_arr[i + 1][j] if i <= (n-1) else 0
    charge += my_arr[i][j - 1] if j >= 0 else 0
    charge += my_arr[i][j + 1] if j <= (n-1) else 0

    return charge

def getAllCharge(my_arr, n):
    """Berechnet die Gesamtladung des Feldes."""
    totalCharge = 0
 
    for i in range(n-1):
        for j in range(n-1):
            totalCharge += getCharge(my_arr, i, j, n)

    return totalCharge
