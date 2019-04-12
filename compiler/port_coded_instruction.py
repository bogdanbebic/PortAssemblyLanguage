class CodedInstruction(object):
    """Represents an instruction coded to
    memory of a port processor"""

    mem_depth = 1024
    mem_width = 64  # 8 bits in byte * 8 bytes instruction length
    address_radix = "DEC"
    data_radix = "HEX"

    def __init__(self, opcode=0, addr1=0, addr2=0, addr3=0, arg1=0, arg2=0, arg3=0):
        super().__init__()
        self.opcode = opcode # 4 bits
        self.addr1 = addr1  # 4 bits
        self.addr2 = addr2  # 4 bits
        self.addr3 = addr3  # 4 bits
        self.arg1 = arg1   # 2 bytes
        self.arg2 = arg2   # 2 bytes
        self.arg3 = arg3   # 2 bytes
        pass

    def convert_to_hex_str(self):
        # TODO: [opcode, addr1, addr2, addr3, arg1, arg2, arg3] to HEX
        return "0000000000000000"

def compile_to_mif(out_file_path : str, coded_instructions : list):
    """Takes out_file_name and coded_instructions list of coded_instructions
    and creates an output mif file containing the program"""
    with open(out_file_path, "w") as output:
        output.write("DEPTH = " + str(CodedInstruction.mem_depth) + ";\n\n")
        output.write("WIDTH = " + str(CodedInstruction.mem_width) + ";\n\n")
        output.write("ADDRESS_RADIX = " + str(CodedInstruction.address_radix) + ";\n")
        output.write("DATA_RADIX = " + str(CodedInstruction.data_radix) + ";\n\n")
        output.write("CONTENT\n")
        output.write("BEGIN\n")
        for i, coded_instruction in enumerate(coded_instructions):
            output.write(str(i) + " : " + coded_instruction.convert_to_hex_str() + ";\n")
        output.write("\nEND;\n")
    pass
