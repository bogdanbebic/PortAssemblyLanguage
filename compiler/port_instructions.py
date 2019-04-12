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

addr_to_obj = {
    "reg" : 0,
    "regind" : 1,
    "mem" : 2,
    "immediate" : 3
}

num_of_regs = 32

regs_to_obj = {
    "pc" : num_of_regs - 1,
    "sp" : num_of_regs - 2,
    "ax" : num_of_regs - 3,
    "bx" : num_of_regs - 4
}



for i in range(num_of_regs):
    regs_to_obj["r" + str(i)] = i
