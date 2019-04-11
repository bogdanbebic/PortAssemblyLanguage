import re
import regex_port as port_re
import port_exceptions

src_path = "test.port"  # TODO: take the file as an argument

class PortCompiler:
    def __init__(self, src_path):
        self.src_path = src_path
        self.src_code = []
        self.preprocessed = []
        self.label_code_line_pair = []
        self.code = []
        pass

    def read_src_code(self):
        """Reads source code from file self.src_path to self.src_code"""
        with open(self.src_path, "r") as in_file:
            self.src_code = in_file.read().split('\n')
        pass

    def preprocess(self):
        """Eliminates comments from self.src_code,
        puts new code in self.preprocessed"""
        for line in self.src_code:
            code_line = re.fullmatch(port_re.non_comments, line)
            self.preprocessed.append(code_line.group(1))
        pass

    def compile(self):
        for i, line in enumerate(self.preprocessed):
            try:
                whitespace = re.fullmatch(port_re.only_whitespace, line)
                instruction = re.fullmatch(port_re.instruction, line)
                if whitespace:
                    # print("line {}:".format(i), line)
                    pass
                elif instruction:
                    # TODO: decode instruction and operands
                    # print("line {}: {} {}{}".format(i, instruction.group(1), instruction.group(2), instruction.group(3)))
                    pass
                else:
                    raise(port_exceptions.BuildError("BuildError-line{}: {}".format(i, line)))
            except port_exceptions.BuildError as build_error:
                print(build_error)
                exit()
        pass

    def split_labels_and_code(self):
        for i in range(len(self.preprocessed)):
            m = re.fullmatch(port_re.label_re, self.preprocessed[i])
            if m:
                self.label_code_line_pair.append((m.group(1), i))
                self.code.append(m.group(2))
            else:
                self.code.append(self.preprocessed[i])
        pass

def main():
    port_compiler = PortCompiler(src_path)
    port_compiler.read_src_code()
    # print(port_compiler.src_code)
    port_compiler.preprocess()
    # print(port_compiler.preprocessed)
    port_compiler.compile()
    pass

if __name__ == '__main__':
    main()
