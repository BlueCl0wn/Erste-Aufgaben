# Calculates Charge of s single position.
def getCharge(my_arr, i, j, n):
    charge = my_arr[i][j]
    charge += my_arr[i - 1][j] if i >= 0 else 0
    charge += my_arr[i + 1][j] if i <= (n-1) else 0
    charge += my_arr[i][j - 1] if j >= 0 else 0
    charge += my_arr[i][j + 1] if j <= (n-1) else 0

    return charge

# Calculates the overall magnetic charge of the whole field.
def getAllCharge(my_arr, n):
    totalCharge = 0

    for i in range(n-1):
        for j in range(n-1):
            totalCharge += getCharge(my_arr, i, j, n)

    return totalCharge
