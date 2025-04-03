	.text
	.globl main
main: 	                                                           
	addi	sp,sp,-16
	sd	ra,8(sp)
## TODO Your assembly code there
	la t0, mydata
	ld a0, 0(t0)
	ld a1, 8(t0)

	bge a0, a1, a1_is_min

	la t0, min
	sd a0, 0(t0) 
	j print_result

a1_is_min:
	la t0, min
	sd a1, 0(t0)

print_result:
	la t0, min
	ld a0, 0(t0)
	call print_int 
	call newline
## END TODO End of user assembly code
	ld	ra,8(sp)
	addi	sp,sp,16
	ret

# Data comes here
	.section	.data
mydata:
	.dword 7
	.dword 42
min:
	.dword 0
