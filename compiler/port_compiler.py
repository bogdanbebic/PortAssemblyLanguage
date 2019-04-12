import re
import port_regex as port_re
import port_instructions as port_inst
import port_exceptions

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
                    raise(port_exceptions.BuildError("BuildError-line{}: {}".format(i + 1, line)))
            except port_exceptions.BuildError as build_error:
                print(build_error)
                self.build_error = True
        pass

    def compile(self):
        for i, line in enumerate(self.preprocessed):
            try:
                instruction =  re.fullmatch(port_re.instruction, line)
                if instruction.group(2) in port_inst.keyword_to_obj:
                    pass
                else:
                    raise(port_exceptions.BuildError("BuildError-illegal keyword-line{}: {}".format(self.instruction_src_code_line[i], \
                    self.src_code[self.instruction_src_code_line[i] - 1])))
                # TODO: decode instruction and operands
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
