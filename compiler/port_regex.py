import re

"""
Contains regex definitions used in
defining the syntax and translation
of the port assembly language
"""

only_whitespace = r'^\s*$'

# \1 is non comment, \2 is comment
non_comments = r'^([^;]*)(;.*)?$'

# \1 is comment
non_instruction = r'^\s*(;.*)?$'

# \1 is optional label, \2 is keyword, \3 is the rest of line
instruction = r'^\s*([_a-zA-Z]\w*:)?\s*([_a-zA-Z]+)([^:]*)$'

# \1 is arg1, \2 is first separator
# \3 is arg2, \4 is second separator
# \5 is arg3
args = r'\s*([^\s,]*)\s*(,)?\s*([^\s,]*)\s*(,)?\s*([^\s,]*)\s*'

reg_dir = r'r(\d+)'

reg_ind = r'i([^m].*)'

mem_dir = r'm(\d+)'

immediate = r'(\d+)'
