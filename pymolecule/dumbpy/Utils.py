from Array import DictArray
from Array import array
from DType import dtype as dtypeClass
from collections import OrderedDict
from Support import to_list
from Support import var_type

def genfromtxt(fname, dtype = "", names = [], delimiter = []):
    # fname here is a file object.

    # Load the data
    data = OrderedDict({})
    for n in names:
        data[n] = []

    for line in fname:
        parts = []
        for num in delimiter:
            parts.append(line[:num])
            line = line[num:]
        
        for i, name in enumerate(names):
            data[name].append(parts[i])

    # Fix any types
    dtype = [l.strip() for l in dtype.split(",")]
    for i, name in enumerate(names):
        if "int" in dtype[i] or dtype[i][:1] == "i":
            data[name] = [int(l) for l in data[name]]
        if "float" in dtype[i] or dtype[i][:1] == "f":
            data[name] = [float(l) for l in data[name]]
    
    return DictArray(data, dtype)

def nonzero(arr):
    if len(arr.shape) == 1:
        indx_to_keep = []
        for i, val in enumerate(arr):
            if val != 0:
                indx_to_keep.append(i)
        indx_to_keep = (array(indx_to_keep),)
    elif len(arr.shape) == 2:
        indx1_to_keep = []
        indx2_to_keep = []

        for i, row in enumerate(arr):
            for j, val in enumerate(row):
                if val != 0:
                    indx1_to_keep.append(i)
                    indx2_to_keep.append(j)
        indx_to_keep = (array(indx1_to_keep), array(indx2_to_keep))

    #print arr
    #print arr.shape
    #sdf
    return indx_to_keep

def logical_or(arr1, arr2):
    if len(arr1.shape) == 1:
        or_result = [x or y for x,y in zip(arr1, arr2)]
        return array(or_result)

def logical_not(arr):
    # Only for 1D arrays
    return array([not i for i in arr])

def defchararray_strip(arr):
    if len(arr.shape) == 1:
        strip_result = [s.strip() for s in arr]
        return array(strip_result)

def vstack(arrays):
    # This implementation only accepts three input parameters
    return array([arrays[0].lst, arrays[1].lst, arrays[2].lst])

def append_fields(arr, field_name, data):
    arr[field_name] = data
    return arr

def max(arr):
    # This has only been implemented fo 1d arrays for now
    max = arr[0]
    for a in arr[1:]:
        if a > max:
            max = a
    return max

def unique(arr):
    # This has only been implemented fo 1d arrays
    return array(list(set(arr.lst)))

def defchararray_add(arr, addit):
    # If addit is a string
    if var_type(addit) == "string":
        lst = [l + addit for l in arr.lst]
        return array(lst)
    else: # addit is another array of some sort
        added = [l[0] + l[1] for l in zip(arr, addit)]
        return array(added)

def insert(arr, indx, val):
    # A very limited implementation of insert.
    lst = arr.lst[:]
    lst.insert(indx, val)
    return array(lst)  

def append(arr1, to_append):
    lst = arr1.lst[:]

    # First, assume to_append is a list.
    if var_type(to_append) == "list":
        lst.extend(to_append)
    else:
        # It's not a list.
        lst.append(to_append)

    return array(lst)

def arange(start, stop, step, dtype = "f8"):  # float by default
    return [
        dtypeClass.convert(dtype, t * step) 
        for t in range(int(start / step), int(stop / step), 1)
    ]

def defchararray_rjust(arr, width):
    arr = to_list(arr)
    return array([a.rjust(width) for a in arr])

def defchararray_upper(arr):
    arr = to_list(arr)
    return array([a.upper() for a in arr])

def defchararray_lstrip(arr, chars = [" ", "\t"]):
    arr = to_list(arr)
    return array([a.lstrip(chars) for a in arr])

def defchararray_split(arr, num = -1):
    arr = to_list(arr)
    return array([a.split(num) for a in arr])

def get_col(lst, num):
    return array([a[num] for a in lst])

def all_same_num(dims, num, dtype="float"):
    arr = []
    val = dtypeClass.convert(dtype, 1.0)

    # Start by assuming dims is a tuple or list
    try:
        for xi in range(dims[0]):
            arr.append([val] * dims[1])
        return array(arr)
    except:
        # So it's an int.
        return array([val] * dims)

def ones(dims, dtype="float"):
    return all_same_num(dims, 1.0, dtype=dtype)

def zeros(dims, dtype="float"):
    return all_same_num(dims, 0.0, dtype=dtype)

def empty(dims, dtype="float"):
    return zeros(dims, dtype=dtype)
