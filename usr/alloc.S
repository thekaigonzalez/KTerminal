	.file	"_cmalloc.c"
	.text
	.section	.rodata
	.align 8
.LC0:
	.string	"KTerminal Interaction Software 1.0 | [q] Exit | [b] Begin | [^D] Exit\n\n"
.LC1:
	.string	"Confirm exit?\n"
.LC2:
	.string	"load\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	call	initscr@PLT
	call	noecho@PLT
	call	cbreak@PLT
	movq	stdscr(%rip), %rax
	testq	%rax, %rax
	je	.L2
	movq	stdscr(%rip), %rax
	movzwl	4(%rax), %eax
	cwtl
	addl	$1, %eax
	jmp	.L3
.L2:
	movl	$-1, %eax
.L3:
	movl	%eax, -8(%rbp)
	movq	stdscr(%rip), %rax
	testq	%rax, %rax
	je	.L4
	movq	stdscr(%rip), %rax
	movzwl	6(%rax), %eax
	cwtl
	addl	$1, %eax
	jmp	.L5
.L4:
	movl	$-1, %eax
.L5:
	movl	%eax, -4(%rbp)
	movq	stdscr(%rip), %rax
	movl	$1, %esi
	movq	%rax, %rdi
	call	scrollok@PLT
	call	start_color@PLT
	movl	$7, %edx
	movl	$0, %esi
	movl	$1, %edi
	call	init_pair@PLT
	movq	stdscr(%rip), %rax
	movl	$0, %edx
	movl	$256, %esi
	movq	%rax, %rdi
	call	wattr_on@PLT
	movq	stdscr(%rip), %rax
	movl	$0, %edx
	movl	$1, %esi
	movq	%rax, %rdi
	call	wmove@PLT
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printw@PLT
	movq	stdscr(%rip), %rax
	movl	$0, %edx
	movl	$256, %esi
	movq	%rax, %rdi
	call	wattr_off@PLT
	movq	stdscr(%rip), %rax
	movq	%rax, %rdi
	call	wgetch@PLT
	movb	%al, -14(%rbp)
	cmpb	$113, -14(%rbp)
	jne	.L6
	leaq	.LC1(%rip), %rdi
	movl	$0, %eax
	call	printw@PLT
	movq	stdscr(%rip), %rax
	movq	%rax, %rdi
	call	wgetch@PLT
	movb	%al, -13(%rbp)
	cmpb	$121, -13(%rbp)
	jne	.L7
	call	echo@PLT
	movl	$0, %eax
	call	endwindow@PLT
	jmp	.L7
.L6:
	cmpb	$98, -14(%rbp)
	jne	.L7
	movl	$0, -12(%rbp)
	jmp	.L8
.L9:
	leaq	.LC2(%rip), %rdi
	movl	$0, %eax
	call	printw@PLT
	addl	$1, -12(%rbp)
.L8:
	cmpl	$9999, -12(%rbp)
	jle	.L9
.L7:
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
