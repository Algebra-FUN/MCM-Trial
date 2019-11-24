import json
import numpy as np


def to_Matrix_arr():
    with open('./Analysis/storage/baked_data.json', 'r') as f:
        data = json.loads(f.read())
    native_M = []
    for vector in data.values():
        row = []
        for item in vector.values():
            row.append(item)
        native_M.append(row)
    return native_M

def to_Matrix():
    return np.array(to_Matrix_arr())

def to_matlib_matrix():
    arr = [','.join([str(item) for item in row]) for row in to_Matrix_arr()]
    with open('./Analysis/storage/m.txt', 'w') as f:
        f.write('[{}]'.format(';'.join(arr)))
    return arr
    
to_matlib_matrix()