from videocore.instr import *

# helper functions

def instruction_number(instrs, target):
  return instrs.index(target)

def print_with_indent(instr):
  print ('    {}'.format(instr))

def print_with_attension(instr):
  print ('>>> {}'.format(instr))

def print_instructions(instrs, indexes):
  for index in indexes:
    print_with_indent(instrs[index])

def print_around(instrs, target):
  index = instruction_number(instrs, target)
  print_instructions(instrs, range (max (0, index-2), max (0, index)))
  print_with_attension(target)
  print_instructions(instrs, range (min (len(instrs), index), min (len(instrs), index + 2)))

#================ check functions ======================================

def check_composed(instrs):
  for instr in instrs:
    if (is_composed(instr)):
      if instr.add_instr.dst == instr.mul_instr.dst and instr.add_instr.sig != 'thread end':
        print ('warning: dst is the same register in the following composed-instruction')
        print_around(instrs, instr)

def check_regfile(instrs):
  if len(instrs) == 1:
    return

  for index in range (0, len(instrs) - 1):
    prev = instrs[index]
    current = instrs[index+1]

all_checks = [check_composed, check_regfile]

def check(instrs):
  for check in all_checks:
    check(instrs)
  return
