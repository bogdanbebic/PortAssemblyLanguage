import argparse
import port_compiler
import port_coded_instruction

import re

file_name = r'(.*)\.'

parser = argparse.ArgumentParser(description='Translates port assembly to port processor mif format')
parser.add_argument("assembly_file", help="The input port assembly file to translate")
parser.add_argument("-o", metavar="out_path", type=str,
                    help="Path and name of the output file (should be mif)")
args = parser.parse_args()


def main():
    src_path = args.assembly_file
    if args.o:
        out_file_path = args.o
    else:
        m = re.fullmatch(file_name, src_path)
        out_file_path = m.group(1) + ".mif"
    port_c = port_compiler.PortCompiler(src_path)
    port_c.read_src_code()
    port_c.preprocess()
    port_c.compile()
    port_coded_instruction.port_obj.compile_to_mif(out_file_path, port_c.coded_instructions)
    pass

if __name__ == '__main__':
    main()
