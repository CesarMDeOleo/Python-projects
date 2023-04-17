import numpy as np


def median(arr):
    arr_sorted = sorted(arr.flatten())
    mid = len(arr_sorted) // 2
    if len(arr_sorted) % 2 == 0:
        return (arr_sorted[mid - 1] + arr_sorted[mid]) / 2
    else:
        return arr_sorted[mid]

def mode(arr):
    arr_flat = arr.flatten()
    mode_counts = {}
    for num in arr_flat:
        if num in mode_counts:
            mode_counts[num] += 1
        else:
            mode_counts[num] = 1
    if len(mode_counts) == 0:
        return None
    max_count = max(mode_counts.values())
    modes = []
    for num, count in mode_counts.items():
        if count == max_count:
            modes.append(num)
    return modes



arr1 = np.random.randint(0, 20, (3, 4))
arr2 = np.random.randint(0, 15, (5,2))
arr3 = np.random.randint(0, 10, (2, 3))


print("arr1:\n", arr1)
print("median(arr1):", median(arr1))
print("mode(arr1):", mode(arr1))
print("\narr2:\n", arr2)
print("median(arr2):", median(arr2))
print("mode(arr2):", mode(arr2))
print("\narr3:\n", arr3)
print("median(arr3):", median(arr3))
print("mode(arr3):", mode(arr3))


def median_axis(arr, axis=0):
    if axis == 0:
        arr_sorted = sorted(arr.flatten())
        mid = len(arr_sorted) // 2
        if len(arr_sorted) % 2 == 0:
            return (arr_sorted[mid - 1] + arr_sorted[mid]) / 2
        else:
            return arr_sorted[mid]
    elif axis == 1:
        result = []
        for col in arr.T:
            col_sorted = sorted(col)
            mid = len(col_sorted) // 2
            if len(col_sorted) % 2 == 0:
                result.append((col_sorted[mid - 1] + col_sorted[mid]) / 2)
            else:
                result.append(col_sorted[mid])
        return result


def mode_axis(arr, axis=0):
    if axis == 0:
        arr_flat = arr.flatten()
        mode_counts = {}
        for num in arr_flat:
            if num in mode_counts:
                mode_counts[num] += 1
            else:
                mode_counts[num] = 1
        if len(mode_counts) == 0:
            return None
        max_count = max(mode_counts.values())
        modes = []
        for num, count in mode_counts.items():
            if count == max_count:
                 modes.append(num)
        return modes
    elif axis == 1:
        result = []
        for col in arr.T:
            col_flat = col.flatten()
            mode_counts = {}
            for num in col_flat:
                if num in mode_counts:
                    mode_counts[num] += 1
                else:
                    mode_counts[num] = 1
            if len(mode_counts) == 0:
                result.append(None)
            else:
                max_count = max(mode_counts.values())
                modes = []
                for num, count in mode_counts.items():
                    if count == max_count:
                        modes.append(num)
                result.append(modes)
        return result


print("\nmedian(arr1) column-by-column:", median_axis(arr1, 1))   
print("mode(arr1) column-by-column:", mode_axis(arr1, 1))

print("median(arr2) column-by-column:", median_axis(arr2, 1))  
print("mode(arr2) column-by-column:", mode_axis(arr2, 1))

print("median(arr3) column-by-column:", median_axis(arr3, 1))
print("mode(arr3) column-by-column:", mode_axis(arr3, 1))