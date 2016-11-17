import copy
from DType import dtype as dtypeClass
from collections import OrderedDict
from Support import to_list
from Support import var_type

def array(lst, dtype=""):
    """Determines whether or not a 1D or 2D array should be used.

        Args:
            lst -- A list to convert to an array.

        Returns:
            An Array2D or Array1D object, as required.
    """

    if len(lst) == 0:
        return Array1D(lst, dtype)
    elif type(lst[0]) is list:
        return Array2D(lst, dtype)
    else:
        return Array1D(lst, dtype)


class ArrayParent:
    """The parent of all Array classes."""
    
    lst = []
    shape = ()

    def __iter__(self):
        # So you could use for... in...
        for x in self.lst:
            yield x

    def __str__(self):
        return str(self.lst)

    def __repr__(self):
        return "array(" + self.__str__() + ")"

    def __getitem__(self, selection):
        # []
        new_lst = []

        # If selection is itself an array, convert it to a list.
        selection = to_list(selection)

        try:
            # Assume the selection is iterable.
            for i in selection:
                new_lst.append(self.lst[i])
        except:
            # selection must not be iterable. Just a number.
            new_lst.append(self.lst[selection])
    
        # If it's just one item, then just return the value, not the value in
        # an array
        if len(new_lst) == 1:
            return new_lst[0]

        return array(new_lst)
    
    def __setitem__(self, key, item):       
        if var_type(key) in ["string", "number"]:
            # The key is not iterable. Probably just a number.
            self.lst[key] = item
            return
        else:
            # The key is iterable
            if var_type(item) in ["string", "number"]:
                # But the item is not iterable
                for k in key:
                    self.lst[k] = item
                    return
            else:
                # So the item is also iterable.
                for k, i in zip(key, item):
                    self.lst[k] = i
                return

    def __len__(self):
        return len(self.lst)


class Array1D(ArrayParent):
    """A 1D Array."""

    type = "1D"

    def __init__(self, lst, dtype=""):
        self.shape = (len(lst),)
        
        if dtype != "":
            for i, val in enumerate(lst):
                lst[i] = dtypeClass.convert(dtype, val)

        self.lst = lst

    def __eq__(self, other):
        bools = copy.deepcopy(self.lst)
        for x in range(self.shape[0]):
            bools[x] = (bools[x] == other)
        return array(bools)

    def astype(self, dtype):
        for i, val in enumerate(self.lst):
            self.lst[i] = dtypeClass.convert(dtype, val)
        return self
    

class Array2D(ArrayParent):
    """A 2D Array."""

    type = "2D"

    def __init__(self, lst, dtype="float"):
        self.shape = (len(lst), len(lst[0]))

        self.lst = []
        for row in lst:
            self.lst.append(array(row))

    def __eq__(self, other):
        bools = copy.deepcopy(self.lst)
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                bools[x][y] = (bools[x][y] == other)
        return array(bools)
    
    def __getattr__(self, attr):
        if attr == "T":
            return zip(*self.lst)  

class DictArray:
    """A Dictionary array."""

    type = "Dict"

    # Collection of arrays accessible through dictionary keys.
    dict = OrderedDict({})
    dtype = None
    ndim = 1  # I think for a DictArray this is always 1?

    def __init__(self, dict, dtypes = []):
        # dict maps keys to arrays.
        for key in dict:
            self.dict[key] = array(dict[key])
        
        self.dtype = dtypeClass(dtypes)

        #self.dtype.names = dict.keys()
        #for i, key in enumerate(dict.keys()):
        #    try:
        #        self.dtype.descr.append((key, "|" + dtypes[i]))
        #    except:
        #        pass
    
    def copy(self):
        new_one = DictArray({})
        new_one.type = self.type
        new_one.dict = self.dict.copy()
        new_one.dtype = self.dtype
        new_one.ndim = self.ndim
        return new_one
    
    def __len__(self):
        key = self.dict.keys()[0]
        return len(self.dict[key])

    def __repr__(self):
        return "dictarray(" + self.__str__() + ")"
    
    def __str__(self):
        return str(self.dict)

    def __getitem__(self, lookup_key):
        if isinstance(lookup_key, basestring):
            return self.dict[lookup_key]
        elif isinstance(lookup_key[0], basestring):
            # So it's a list of strings

            # So key must be something that should act on the individual
            # Arrays, like ["key1", "key2", "key3", "key4""]
            new_dict = OrderedDict({})
            for str_key in lookup_key:
                new_dict[str_key] = self.dict[str_key]
            
            #print "DDD", new_dict.keys()

            updated_dict = DictArray(new_dict)
            updated_dict.dict = new_dict

            return updated_dict

        else: # So it's a list of integers
            # So key must be something that should act on the individual
            # Arrays, like [1, 2, 3, 4]
            new_dict = OrderedDict({})
            for str_key in self.dict.keys():
                new_dict[str_key] = self.dict[str_key][lookup_key].lst
            
            return DictArray(new_dict)
    
    def __setitem__(self, key, vals):
        # In this implementation, key must be a string.
        self.dict[key] = vals

    def astype(self, dtype):
        self.dtype = dtype
        for key in dtype.signature.keys():
            tp = dtype.signature[key]
            for i, val in enumerate(self.dict[key]):
                self.dict[key][i] = dtypeClass.convert(tp, val)
        return self

