def var_type(var):
    if isinstance(var, basestring):
        return "string"
    
    # See if it's one of your dumbpy array objects
    try: return var.type
    except: pass

    # see if it's a list
    try:
        var[0] # must be a list or something like it
        return "list"
    except:
        # a number perhaps?
        return "number"

def to_list(arr):
    # return a list regardless of whether arr is a list or array.
    typ = var_type(arr) 
    if typ in ["1D", "2D"]:
        return arr.lst[:]
    elif typ == "list":
        # already a python list
        return arr[:]
    else:
        # a number or string
        return arr
