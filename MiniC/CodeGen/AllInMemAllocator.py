from Lib import RiscV
from Lib.Operands import Temporary, Operand, S, all_ops as branche_ops
from Lib.Statement import Instruction, Label
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
        # TODO: compute before,after,args.
        # TODO: iterate over old_args, check which argument
        # TODO: is a temporary (e.g. isinstance(..., Temporary)),
        # TODO: and if so, generate ld/sd accordingly. Replace the
        # TODO: temporary with S[1], S[2] or S[3] physical registers.
        
        old_args = old_instr.args()
        is_branch = old_instr.ins in branche_ops
        
        for idx, arg in enumerate(old_args):
            if isinstance(arg, Temporary):
                if is_branch:
                    before.append(RiscV.ld(S[numreg], arg.get_alloced_loc()))
                    new_args.append(S[numreg])
                elif idx == 0 and not Instruction.is_read_only(old_instr):
                    new_args.append(S[numreg])
                    after.append(RiscV.sd(S[numreg], arg.get_alloced_loc()))
                elif idx > 0:
                    new_args.append(S[numreg])
                    before.append(RiscV.ld(S[numreg], arg.get_alloced_loc()))
                
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
