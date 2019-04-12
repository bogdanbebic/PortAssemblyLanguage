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
