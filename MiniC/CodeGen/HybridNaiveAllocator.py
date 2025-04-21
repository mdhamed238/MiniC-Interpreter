from Lib import RiscV
from Lib.Operands import GP_REGS, DataLocation, Offset, Temporary, Operand, S,  all_ops as branche_ops
from Lib.Statement import Instruction
from Lib.Allocator import Allocator
from typing import List, Dict


class HybridNaiveAllocator(Allocator):

    def replace(self, old_instr: Instruction) -> List[Instruction]:
        """
        Replace Temporary operands with the corresponding allocated
        physical register (Register) OR memory location (Offset).
        """
        before: List[Instruction] = []
        after: List[Instruction] = []
        new_args: List[Operand] = []
        # TODO: Compute before, after, new_args. This is similar to what
        # TODO: replace from the Naive and AllInMem Allocators do.
        numreg = 1
        old_args = old_instr.args()
        
        for idx, arg in enumerate(old_args):
            if isinstance(arg, Temporary):
                if isinstance(arg.get_alloced_loc(), Offset):
                    if idx == 0:
                        if Instruction.is_read_only(old_instr):
                            before.append(RiscV.ld(S[numreg], arg.get_alloced_loc()))
                        else:
                            after.append(RiscV.sd(S[numreg], arg.get_alloced_loc()))
                        new_args.append(S[numreg])
                    elif idx > 0:
                        new_args.append(S[numreg])
                        before.append(RiscV.ld(S[numreg], arg.get_alloced_loc()))
                    
                    numreg += 1
                else:
                    new_args.append(arg.get_alloced_loc())
            else:
                new_args.append(arg)
        
        # And now return the new list!
        instr = old_instr.with_args(new_args)
        return before + [instr] + after

    def prepare(self) -> None:
        """Allocate all temporaries to registers first (like Naive), and then
        memory (like AllInMem).
        Invariants: - Expanded instructions can use s1, s2 and s3
          (to store the values of temporaries before the actual instruction).
        """
        regs = list(GP_REGS)  # Get a writable copy
        temp_allocation: Dict[Temporary, DataLocation] = dict()
        for tmp in self._fdata._pool.get_all_temps():
            if regs:
                location = regs.pop()
            else:
                location = self._fdata.fresh_offset()
            temp_allocation[tmp] = location
        self._fdata._pool.set_temp_allocation(temp_allocation)
