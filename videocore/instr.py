#=============================================================================
# Instruction definitions for sanity check
#=============================================================================

def is_add(instr):
  return isinstance(instr, AddInstr)
def is_mul(instr):
  return isinstance(instr, MulInstr)
def is_loadimm(instr):
  return isinstance(instr, LoadImmInstr)
def is_branch(instr):
  return isinstance(instr, BranchInstr)
def is_sema(instr):
  return isinstance(instr, SemaInstr)
def is_composed(instr):
  return isinstance(instr, ComposedInstr)
def is_label(instr):
  return isinstance(instr, assembler.Label)

class InstrBase(object):
  def __init__():
    return

  def get_dst(self):
    return None

  def get_arg1(self):
    return None

  def get_arg2(self):
    return None

class AddInstr:
  def __init__ (self, op_add, dst, opd1, opd2, sig, set_flag, cond):
    self.op_add = op_add
    self.dst = dst
    self.opd1 = opd1
    self.opd2 = opd2
    self.sig = sig
    self.set_flag = set_flag
    self.cond = cond

  def __str__(self):
    s = '{}, {}, {}, {}'.format(self.op_add, self.dst, self.opd1, self.opd2)
    if self.set_flag:
      s += ' set_flag=True'
    if not (self.cond == 'always'):
      s += 'cond={}'.format(self.cond)
    return s

class MulInstr(InstrBase):
  def __init__ (self, op_mul, dst, opd1, opd2, sig, set_flag, cond):
    self.op_mul = op_mul
    self.dst = dst
    self.opd1 = opd1
    self.opd2 = opd2
    self.sig = sig
    self.set_flag = set_flag
    self.cond = cond

  def __str__(self):
    s = '{}, {}, {}, {}'.format(self.op_mul, self.dst, self.opd1, self.opd2)
    if self.set_flag:
      s += ' set_flag=True'
    if not (self.cond == 'always'):
      s += 'cond={}'.format(self.cond)
    return s

  def get_dst(self):
    return self.op_mul

  def get_arg1(self):
    return self.opd1

  def get_arg2(self):
    return self.opd2

class LoadImmInstr(InstrBase):
  def __init__(self, reg1, reg2, imm):
    self.reg1 = reg1
    self.reg2 = reg2
    self.imm = imm

  def __str__(self):
    s = 'ldi {}, {}'.format(self.reg1, self.imm)
    if (self.reg2 != REGISTERS['null']):
      s += '; ldi {}, {}'.format(self.reg2, self.imm)
    return s

  def get_dst(self):
    return self.reg1

  def get_arg1(self):
    return self.imm

  def get_arg2(self):
    return None


class BranchInstr(InstrBase):
  def __init__(self, cond_br, target, reg, absolute, link):
    self.cond_br = cond_br
    self.target = target
    self.reg = reg
    self.absolute = absolute
    self.link = link

class SemaInstr(InstrBase):
  def __init__(self, sa, sema_id):
    self.sa = sa
    self.sema_id = sema_id

class ComposedInstr(InstrBase):
  def __init__(self, add, mul):
    self.add_instr = add
    self.mul_instr = mul

  def __str__(self):
    return str(self.add_instr) + '; ' + str(self.mul_instr)

  def get_output(self):
    assert (false)

  def get_arg1(self):
    assert (false)

  def get_arg2(self):
    assert (false)

class Label(InstrBase):
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return ':' + self.name
