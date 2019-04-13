import re
import port_regex as port_re
import port_instructions as port_inst
import port_exceptions
import port_coded_instruction as port_obj

class PortCompiler:
    def __init__(self, src_path):
        self.src_path = src_path
        self.src_code = []
        self.preprocessed = []
        self.label_code_line_pair = dict()
        self.code = []
        self.instruction_src_code_line = []
        self.build_error = False
        self.coded_instructions = []
        pass

    def read_src_code(self):
        """Reads source code from file self.src_path to self.src_code"""
        with open(self.src_path, "r") as in_file:
            self.src_code = in_file.read().split('\n')
        pass

    def preprocess(self):
        """Eliminates comments from self.src_code,
        puts new code in self.preprocessed"""
        for i, line in enumerate(self.src_code):
            try:
                code_line = re.fullmatch(port_re.non_comments, line)
                instruction = re.fullmatch(port_re.instruction, code_line.group(1))
                if instruction:
                    self.preprocessed.append(instruction.group(2) + " " + instruction.group(3))
                    self.instruction_src_code_line.append(i + 1)
                    if instruction.group(1):
                        self.label_code_line_pair[instruction.group(1).strip(':')] = len(self.preprocessed) - 1
                elif not re.fullmatch(port_re.only_whitespace, code_line.group(1)):
                    port_exceptions.raise_build_error("illegal label", i + 1, line)
            except port_exceptions.BuildError as build_error:
                print(build_error)
                self.build_error = True
        pass

    def get_addr_and_arg(self, arg_string : str, index_of_src_code : int, line_of_src_code : str):
        reg_dir = re.fullmatch(port_re.reg_dir, arg_string)
        reg_ind = re.fullmatch(port_re.reg_ind, arg_string)
        mem_dir = re.fullmatch(port_re.mem_dir, arg_string)
        immediate = re.fullmatch(port_re.immediate, arg_string)
        if reg_dir:
            arg = port_inst.reg_index_out_of_bounds(int(reg_dir.group(1)), index_of_src_code, line_of_src_code)
            addr = port_inst.addr_to_obj["regdir"]
        elif arg_string in port_inst.regs_to_obj: # aliased regdir
            arg = port_inst.regs_to_obj[arg_string]
            addr = port_inst.addr_to_obj["regdir"]
        elif reg_ind:
            reg_dir = re.fullmatch(port_re.reg_dir, reg_ind.group(1))
            if reg_dir:
                arg = port_inst.reg_index_out_of_bounds(int(reg_dir.group(1)), index_of_src_code, line_of_src_code)
                addr = port_inst.addr_to_obj["regind"]
            elif reg_ind.group(1) in port_inst.regs_to_obj: # aliased regdir
                arg = port_inst.regs_to_obj[reg_ind.group(1)]
                addr = port_inst.addr_to_obj["regind"]
        elif mem_dir:
            arg = port_inst.mem_location_out_of_bounds(int(mem_dir.group(1)), index_of_src_code, line_of_src_code)
            addr = port_inst.addr_to_obj["memdir"]
        elif immediate:
            arg = port_inst.number_out_of_bounds(int(immediate.group(1)), index_of_src_code, line_of_src_code)
            addr = port_inst.addr_to_obj["immediate"]
        else:
            port_exceptions.raise_build_error("illegal operand", index_of_src_code, line_of_src_code)
        return int(addr), int(arg)

    def compile(self):
        for i, line in enumerate(self.preprocessed):
            try:
                instruction =  re.fullmatch(port_re.instruction, line)
                keyword = instruction.group(2)
                args_string = instruction.group(3)
                temp_coded_instruction = port_obj.CodedInstruction(port_inst.keyword_to_obj[keyword])
                successfully_coded = False
                if keyword in port_inst.keyword_to_obj:
                    args_match = re.fullmatch(port_re.args, args_string)
                    if args_match:
                        no_args = not args_match.group(2) and not args_match.group(4) \
                            and len(args_match.group(1) + args_match.group(3) + args_match.group(5)) == 0
                        one_arg = not args_match.group(2) and not args_match.group(4) \
                            and len(args_match.group(3) + args_match.group(5)) == 0 \
                            and len(args_match.group(1)) > 0
                        three_args = args_match.group(2) and args_match.group(4) \
                            and len(args_match.group(1)) > 0 \
                            and len(args_match.group(3)) > 0 \
                            and len(args_match.group(5)) > 0
                        
                        addr_arg_1 = 0, 0
                        addr_arg_2 = 0, 0
                        addr_arg_3 = 0, 0

                        if no_args and port_inst.keyword_args_cnt[keyword] == 0:
                            successfully_coded = True
                        elif one_arg and port_inst.keyword_args_cnt[keyword] == 1:
                            if keyword == "call":
                                if args_match.group(1) not in self.label_code_line_pair:
                                    port_exceptions.raise_build_error("label not recognized", \
                                        self.instruction_src_code_line[i], \
                                        self.src_code[self.instruction_src_code_line[i] - 1])
                                addr_arg_1 = port_inst.addr_to_obj["immediate"], self.label_code_line_pair[args_match.group(1)]
                                successfully_coded = True
                            else:
                                addr_arg_1 = self.get_addr_and_arg(args_match.group(1), \
                                    self.instruction_src_code_line[i], \
                                    self.src_code[self.instruction_src_code_line[i] - 1])
                                if not (keyword == "store" and addr_arg_1[0] == port_inst.addr_to_obj["immediate"]):
                                    successfully_coded = True
                                else:
                                    port_exceptions.raise_build_error("invalid addressing for store", \
                                        self.instruction_src_code_line[i], \
                                        self.src_code[self.instruction_src_code_line[i] - 1])
                        elif three_args and port_inst.keyword_args_cnt[keyword] == 3:
                            addr_arg_1 = self.get_addr_and_arg(args_match.group(1), \
                                self.instruction_src_code_line[i], \
                                self.src_code[self.instruction_src_code_line[i] - 1])
                            addr_arg_2 = self.get_addr_and_arg(args_match.group(3), \
                                self.instruction_src_code_line[i], \
                                self.src_code[self.instruction_src_code_line[i] - 1])
                            if keyword not in ["beq", "bgt"]:
                                addr_arg_3 = self.get_addr_and_arg(args_match.group(5), \
                                    self.instruction_src_code_line[i], \
                                    self.src_code[self.instruction_src_code_line[i] - 1])
                                successfully_coded = True
                            elif args_match.group(5) in self.label_code_line_pair:
                                addr_arg_3 = port_inst.addr_to_obj["immediate"], self.label_code_line_pair[args_match.group(5)]
                                successfully_coded = True
                            else:
                                port_exceptions.raise_build_error("label not recognized", \
                                    self.instruction_src_code_line[i], \
                                    self.src_code[self.instruction_src_code_line[i] - 1])
                            if not (keyword in ["add", "sub"] and addr_arg_1[0] == port_inst.addr_to_obj["immediate"]):
                                successfully_coded = True
                            else:
                                port_exceptions.raise_build_error("invalid addressing for first operand", \
                                    self.instruction_src_code_line[i], \
                                    self.src_code[self.instruction_src_code_line[i] - 1])
                        else:
                            port_exceptions.raise_build_error("illegal args", \
                                self.instruction_src_code_line[i], \
                                self.src_code[self.instruction_src_code_line[i] - 1])
                        temp_coded_instruction.addr1, temp_coded_instruction.arg1 = addr_arg_1
                        temp_coded_instruction.addr2, temp_coded_instruction.arg2 = addr_arg_2
                        temp_coded_instruction.addr3, temp_coded_instruction.arg3 = addr_arg_3
                    else:
                        port_exceptions.raise_build_error("arguments mismatch", \
                            self.instruction_src_code_line[i], \
                            self.src_code[self.instruction_src_code_line[i] - 1])

                    if successfully_coded:
                        self.coded_instructions.append(temp_coded_instruction)
                    else:
                        port_exceptions.raise_build_error("unsuccesful coding of instruction", \
                            self.instruction_src_code_line[i], \
                            self.src_code[self.instruction_src_code_line[i] - 1])
                else:
                    port_exceptions.raise_build_error("illegal keyword", \
                            self.instruction_src_code_line[i], \
                            self.src_code[self.instruction_src_code_line[i] - 1])
                pass
            except port_exceptions.BuildError as build_error:
                print(build_error)
                self.build_error = True
        if self.build_error:
            exit()
        pass


def main():
    src_path = "test.port"  # TODO: take the file as an argument
    out_file_path = "test.mif"
    port_compiler = PortCompiler(src_path)
    port_compiler.read_src_code()
    port_compiler.preprocess()
    port_compiler.compile()
    #print(port_compiler.preprocessed)
    #print(port_compiler.label_code_line_pair)
    port_obj.compile_to_mif(out_file_path, port_compiler.coded_instructions)
    pass

if __name__ == '__main__':
    main()
