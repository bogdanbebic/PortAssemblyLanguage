class CodedInstruction(object):
    """Represents an instruction coded to 
    memory of a port processor"""

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
    