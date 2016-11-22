import sys

def get_class_or_func_name(line):
    return line.replace("(", " ").replace(":", " ").split()[1]

def starts(haystack, needle):
    return haystack.strip().startswith(needle)

def starts_struc(line):
    return starts(line, "class ") or starts(line, "def ")

pyfile = sys.argv[1]

# Get the non-empty lines with tabs replaced by four spaces
lines = [l.replace("\t", "    ") for l in open(pyfile).readlines() if len(l.strip()) != 0]
# for l in lines:
#     print l.strip()
# sf

# Get the length of the whitespace to the right of each line
fluff_sizes = []
for line in lines:
    # Calculate the size of the whitespace on the left.
    line = line.rstrip()
    len_line = len(line)
    len_line_no_left_fluff = len(line.strip())
    size_of_fluff = len_line - len_line_no_left_fluff
    fluff = line[:size_of_fluff].replace("\t", "    ")
    fluff_sizes.append(len(fluff))

# Get the code location of each line (filename.class.def)
locs = [pyfile] * len(fluff_sizes)
lines_with_struc_elements = [i for i, l in enumerate(lines) if starts_struc(l)]
for line_index in lines_with_struc_elements:
    line = lines[line_index]
    if starts_struc(line):
        fluff_size = fluff_sizes[line_index]
        cur_i = line_index
        class_name = get_class_or_func_name(line)
        while cur_i < len(lines) - 1:
            cur_i = cur_i + 1
            cur_fluff = fluff_sizes[cur_i]
            if cur_fluff == 0:
                # if something is no longer indented, the class has ended.
                break
            if cur_fluff <= fluff_size and starts_struc(lines[cur_i]):
                # If the indentation is less than or equal to that of the original class, the class has ended.
                break;
            locs[cur_i - 1] = locs[cur_i - 1] + "//" + class_name

# Demove duplicate locs
already_seen = set([])
for i in range(len(locs)):
    if locs[i] in already_seen or locs[i] == pyfile:
        locs[i] = ""
    else:
        already_seen.add(locs[i])

i = 0
while i < len(locs):
    loc = locs[i]
    line = lines[i]

    print line.rstrip()

    if starts(line, "def ") and not ":" in line:
        i2 = i
        while not ":" in lines[i2]: i2 = i2 + 1
        locs[i2] = locs[i]
        i = i + 1
        continue

    if loc != "":
        #spaces = " " * (fluff_sizes[i] + 4)
        spaces = " " * (fluff_sizes[i + 1])
        if fluff_sizes[i] == 0 and not starts_struc(line):
            spaces = ""  
        print spaces + 'print "{MARKER}: ' + loc.rstrip() + '"'
    
    i = i + 1

#for l1, l2 in zip(lines, locs): print l1.strip() + "\t" + l2.strip() 

# class_hier = [(0, "main")]
# for line_index, line in enumerate(lines):
#     fluff_size = fluff_sizes[line_index] + 4
#     while fluff_size < class_hier[-1][0]:
#         class_hier = class_hier[:-1]

#     line = line.strip()
#     if line[:6] == "class ":
#         class_name = get_class_or_func_name(line)
#         class_hier.append((fluff_size, class_name))
#     elif line[:4] == "def ":
#         def_name = get_class_or_func_name(line)
#         print "{" + pyfile + "}." + class_hier[-1][1] + "." + def_name, class_hier

# print class_hier
