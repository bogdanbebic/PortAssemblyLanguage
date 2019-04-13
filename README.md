# PortAssemblyLanguage
Definition of an assembly like language and an implementation of a translation program from port to mifi format

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
* <code><b>sub</b> dest, src1, src2</code>
* <code><b>load</b> src</code>
* <code><b>store</b> dest</code>
* <code><b>push</b></code>
* <code><b>pop</b></code>
* <code><b>call</b> label</code>
* <code><b>ret</b></code>
* <code><b>bgt</b> src1, src2, label</code>
* <code><b>beq</b> src1, src2, label</code>
* <code><b>halt</b></code>

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
