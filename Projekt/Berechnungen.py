# Bibliotheken
import numpy as np

def smooth(y, box_pts) -> np.ndarray:
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

def averageArraySameLength(my_arrays) -> np.ndarray:
    return np.mean((my_arrays), axis=0)

def tolerant_meanArray(arrs):
    lens = [len(i) for i in arrs]
    arr = np.ma.empty((np.max(lens),len(arrs)))
    # print("____")
    # print("len: ")
    # print(lens)
    # print("")
    # print("arr: ")
    # print(arr)
    # print("")
    arr.mask = True
    for idx, l in enumerate(arrs):
        # print("idx: ")
        # print(idx)
        # print("")
        # print("l: ")
        # print(l)
        # print("")

        arr[:len(l),idx] = l
    #     print("arr_zeile: ")
    #     print(arr)
    #     print("")
    # print("arr_neu: ")
    # print(arr)
    # print("")
    return arr.mean(axis = 1)  # , arr.std(axis=0)

# x = [[1, 2], [10, 20], [100, 200, 300]]
# y = tolerant_meanArray(x)
# print(y)
