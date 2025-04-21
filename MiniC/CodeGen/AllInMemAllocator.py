from Lib import RiscV
from Lib.Operands import Temporary, Operand, S
from Lib.Statement import Instruction
from Lib.Allocator import Allocator
from typing import List


class AllInMemAllocator(Allocator):

    def replace(self, old_instr: Instruction) -> List[Instruction]:
        """Replace Temporary operands with the corresponding allocated
        memory location."""
        numreg = 1
        before: List[Instruction] = []
        after: List[Instruction] = []
        new_args: List[Operand] = []
        
        old_args = old_instr.args()
        
        for idx, arg in enumerate(old_args):
            if isinstance(arg, Temporary):
                if idx == 0:
                    if Instruction.is_read_only(old_instr):
                        before.append(RiscV.ld(S[numreg], arg.get_alloced_loc()))
                    else:
                        after.append(RiscV.sd(S[numreg], arg.get_alloced_loc()))
                    new_args.append(S[numreg])
                elif idx > 0:
                    before.append(RiscV.ld(S[numreg], arg.get_alloced_loc()))
                    new_args.append(S[numreg])
                
                numreg += 1
            else:
                new_args.append(arg)
            
                
        new_instr = old_instr.with_args(new_args)
        return before + [new_instr] + after

    def prepare(self) -> None:
        """Allocate all temporaries to memory.
        Invariants:
        - Expanded instructions can use s2 and s3
          (to store the values of temporaries before the actual instruction).
        """
        self._fdata._pool.set_temp_allocation(
            {temp: self._fdata.fresh_offset()
             for temp in self._fdata._pool.get_all_temps()})
