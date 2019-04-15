# PortAssemblyLanguage
Definition of an assembly like language and an implementation of a translation program from port to mifi format,
designed to work on the [port processor](https://github.com/bogdanbebic/PortAssemblyLanguage/blob/master/compiler/README.md).

## Port assembly language definition

The port assembly langage (port) is considered to be in one input file.  
Every instruction is on it's own line of code (instructions are seperated with newlines).

A line of code consists of:
`[;comment]`
or
`[<label>:]<instruction>[;<comment>]`
where comments are ignored.

Optional comments start with `;` and continue to the end of the line.  
Optional labels must start with an underscore (`_`) or lower or uppercase English ASCII letters,
and consist of underscores and lower or uppercase English ASCII letters and digits.
Labels identifiers are followed immediately by a colon (`:`).

Instructions consist of a keyword, at least one whitespace mark, and arguments separated by commas (`,`):  
`<keyword><whitespace><argumets>`  
Instructions do not contain colon (`:`) characters.

Every other whitespace is ignored.

### Instruction set

Following is a list of instructions (keywords along with their operands):
* <code><b>add</b> dest, src1, src2</code>  
Adds numbers from `src1` and `src2` and stores them in `dest`.  

* <code><b>sub</b> dest, src1, src2</code>  
Subtracts numbers `src1` and `src2` and stores them in `dest`.  

* <code><b>load</b> src</code>  
Loads number from `src` and stores it in `ax`.  

* <code><b>store</b> dest</code>  
Stores number from `ax` to location `dest`.  

* <code><b>push</b></code>  
Pushes the contents of `ax` to the stack.  

* <code><b>pop</b></code>  
Pops a number from the stack and stores it in `ax`.  

* <code><b>call</b> label</code>  
Gets the number given by `label` and stores it in the `pc`, old `pc` is pushed to the stack.  

* <code><b>ret</b></code>  
Resstores the old `pc` from the stack.  

* <code><b>bgt</b> src1, src2, label</code>  
Branches control of the program to `label` if `src1` is greater than `src2`.  

* <code><b>beq</b> src1, src2, label</code>  
Branches control of the program to `label` if `src1` is equal to `src2`.  

* <code><b>halt</b></code>  
Halts the execution of the program.  

### Addressing modes

Following is a list of available addressing modes:
* <b>regdir:</b><code> <b>r</b>x </code> where x is from 0 to 31 or specific names:
  * <code><b>pc</b></code> alias for r31, 
  * <code><b>sp</b></code> alias for r30,
  * <code><b>ax</b></code> alias for r29,
  * <code><b>bx</b></code> alias for r28.
* <b>regind:</b><code> <b>ir</b>x </code> where x is from 0 to 31 or specific names:
  * <code><b>ipc</b></code> alias for r31, 
  * <code><b>isp</b></code> alias for r30,
  * <code><b>iax</b></code> alias for r29,
  * <code><b>ibx</b></code> alias for r28.
* <b>memdir:</b><code> <b>m</b>address </code> where address is from 0 to 1023.
* <b>immediate:</b><code> constant </code> where constant is from 0 to 65536 (2^16)


Keywords are given in **bold**.

[comment]: <> (TODO: maybe add instructions in and out)
[comment]: <> (TODO: add explanation for operands and instructions)
[comment]: <> (TODO: finish this list of keywords)
