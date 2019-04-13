import port_exceptions

num_of_mem_locations = 1024

max_number = 1 << 16 - 1
min_number = 0

keyword_to_obj = {
    "halt" : 0,
    "add" : 1,
    "sub" : 2,
    "load" : 3,
    "store" : 4,
    "push" : 5,
    "pop" : 6,
    "call" : 7,
    "ret" : 8,
    "bgt" : 9,
    "beq" : 10
}

keyword_args_cnt = {
    "halt" : 0,
    "add" : 3,
    "sub" : 3,
    "load" : 1,
    "store" : 1,
    "push" : 0,
    "pop" : 0,
    "call" : 1,
    "ret" : 0,
    "bgt" : 3,
    "beq" : 3
}

addr_to_obj = {
    "regdir" : 0,
    "regind" : 1,
    "memdir" : 2,
    "immediate" : 3
}

num_of_regs = 32

regs_to_obj = {
    "pc" : num_of_regs - 1,
    "sp" : num_of_regs - 2,
    "ax" : num_of_regs - 3,
    "bx" : num_of_regs - 4
}

def mem_location_out_of_bounds(mem_location_index : int, index_of_src_code : int, line_of_src_code : str):
    if not (0 <= mem_location_index and mem_location_index <= num_of_mem_locations):
        port_exceptions.raise_build_error("illegal mem location", index_of_src_code, line_of_src_code)
    return mem_location_index

def reg_index_out_of_bounds(reg_index : int, index_of_src_code : int, line_of_src_code : str):
    if not (0 <= reg_index and reg_index <= num_of_regs):
        port_exceptions.raise_build_error("illegal mem location", index_of_src_code, line_of_src_code)
    return reg_index

def number_out_of_bounds(constant : int, index_of_src_code : int, line_of_src_code : str):
    if not (min_number <= constant and constant <= max_number):
        port_exceptions.raise_build_error("illegal mem location", index_of_src_code, line_of_src_code)
    return constant
