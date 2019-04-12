import re
import port_regex as port_re
import port_instructions as port_inst
import port_exceptions
import port_coded_instruction as port_obj

src_path = "test.port"  # TODO: take the file as an argument

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

    def compile(self):
        for i, line in enumerate(self.preprocessed):
            try:
                instruction =  re.fullmatch(port_re.instruction, line)
                keyword = instruction.group(2)
                args_string = instruction.group(3)
                temp_coded_instruction = port_obj.CodedInstruction(keyword)
                successfully_coded = False
                if keyword in port_inst.keyword_to_obj:
                    args_match = re.fullmatch(port_re.args, args_string)
                    if args_match:
                        # TODO: code operands
                        pass
                        #for it in range(1, 6):
                        #    print(args_match.group(it), end="---")
                        #print("\n")
                    else:
                        port_exceptions.raise_build_error("generic error", \
                            self.instruction_src_code_line[i], \
                            self.src_code[self.instruction_src_code_line[i] - 1])
                        
                    if successfully_coded:
                        self.coded_instructions.append(temp_coded_instruction)
                    else:
                        pass
                        #raise(port_exceptions.BuildError("BuildError-generic error-line{}: {}".format(self.instruction_src_code_line[i], \
                    #self.src_code[self.instruction_src_code_line[i] - 1])))
                else:
                    port_exceptions.raise_build_error("illegal keyword", \
                            self.instruction_src_code_line[i], \
                            self.src_code[self.instruction_src_code_line[i] - 1])
                
                # print("line {}: {} {}{}".format(i, instruction.group(1), instruction.group(2), instruction.group(3)))
                pass
            except port_exceptions.BuildError as build_error:
                print(build_error)
                self.build_error = True
        if self.build_error:
            exit()
        pass


def main():
    port_compiler = PortCompiler(src_path)
    port_compiler.read_src_code()
    # print(port_compiler.src_code)
    port_compiler.preprocess()
    #print(port_compiler.preprocessed)
    #print(port_compiler.instruction_src_code_line)
    #print(port_compiler.label_code_line_pair)
    port_compiler.compile()
    pass

if __name__ == '__main__':
    main()
