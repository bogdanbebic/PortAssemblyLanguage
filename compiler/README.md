# CPU description

The compiler translates port assembly language for the port processor described in this file.

[comment]: <TODO: describe the port processor>

An instruction consists of 8 Bytes,
the first two are used for opcode and operand addressing modes,
second and third are used for the first operand,
fourth and fifth are used for the second operand,
sixth and seventh are used for the third operand
(indexing statrs from 0).

Opcode (keyword mapping) of the instruction takes up the first 4 bits,
and each of the addressing modes take up 4 bits. Opcode is in the upper four bits
of the zeroth byte, after which are addressing modes - 4 bits each.

If the instruction requires less than three operands, the "*free*" space of the instruction
is padded with zeros.

There are 32 registers in the processor - `r0` to `r31`.  
* `r31` is used as the `pc` (program counter).  
* `r30` is used as the `sp` (stack pointer).  
* `r29` is used as the `ax` (accumulator).  
* `r28` is used as the `bx` (backup register).  

Following is a list of instruction to hex value mapping (keywords):  
* <code><b>add</b></code> to 1  
* <code><b>sub</b></code> to 2  
* <code><b>load</b></code> to 3  
* <code><b>store</b></code> to 4  
* <code><b>push</b></code> to 5  
* <code><b>pop</b></code> to 6  
* <code><b>call</b></code> to 7  
* <code><b>ret</b></code> to 8  
* <code><b>bgt</b></code> to 9  
* <code><b>beq</b></code> to A  
* <code><b>halt</b></code> to 0  

Following is a list of operand to hex value mapping:  
* <code><b>r</b>x</code> to 0
* <code><b>ir</b>x</code> to 1  
* <code><b>m</b>address</code> to 2  
* <code>constant</code> to 3  
  
