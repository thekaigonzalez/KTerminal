	.file	"luac.c"
	.text
	.globl	iscr
	.type	iscr, @function
iscr:
.LFB0:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	call	initscr@PLT
	movl	$1, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	iscr, .-iscr
	.globl	addstr_lua
	.type	addstr_lua, @function
addstr_lua:
.LFB1:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	movq	-8(%rbp), %rax
	movl	$0, %edx
	movl	$1, %esi
	movq	%rax, %rdi
	call	luaL_checklstring@PLT
	movq	%rax, %rdi
	movl	$0, %eax
	call	printw@PLT
	movl	$1, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	addstr_lua, .-addstr_lua
	.globl	getch_w_c
	.type	getch_w_c, @function
getch_w_c:
.LFB2:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	movq	stdscr(%rip), %rax
	movq	%rax, %rdi
	call	wgetch@PLT
	movl	$1, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	getch_w_c, .-getch_w_c
	.globl	iendwin
	.type	iendwin, @function
iendwin:
.LFB3:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	call	endwin@PLT
	movl	$1, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3:
	.size	iendwin, .-iendwin
	.section	.rodata
.LC0:
	.string	"curses_initscr"
.LC1:
	.string	"curses_printw"
.LC2:
	.string	"curses_wgetch"
.LC3:
	.string	"curses_endwin"
	.text
	.globl	luaopen_curses
	.type	luaopen_curses, @function
luaopen_curses:
.LFB4:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	movq	-8(%rbp), %rax
	movl	$0, %edx
	leaq	iscr(%rip), %rsi
	movq	%rax, %rdi
	call	lua_pushcclosure@PLT
	movq	-8(%rbp), %rax
	leaq	.LC0(%rip), %rdx
	movl	$-10002, %esi
	movq	%rax, %rdi
	call	lua_setfield@PLT
	movq	-8(%rbp), %rax
	movl	$0, %edx
	leaq	addstr_lua(%rip), %rsi
	movq	%rax, %rdi
	call	lua_pushcclosure@PLT
	movq	-8(%rbp), %rax
	leaq	.LC1(%rip), %rdx
	movl	$-10002, %esi
	movq	%rax, %rdi
	call	lua_setfield@PLT
	movq	-8(%rbp), %rax
	movl	$0, %edx
	leaq	getch_w_c(%rip), %rsi
	movq	%rax, %rdi
	call	lua_pushcclosure@PLT
	movq	-8(%rbp), %rax
	leaq	.LC2(%rip), %rdx
	movl	$-10002, %esi
	movq	%rax, %rdi
	call	lua_setfield@PLT
	movq	-8(%rbp), %rax
	movl	$0, %edx
	leaq	iendwin(%rip), %rsi
	movq	%rax, %rdi
	call	lua_pushcclosure@PLT
	movq	-8(%rbp), %rax
	leaq	.LC3(%rip), %rdx
	movl	$-10002, %esi
	movq	%rax, %rdi
	call	lua_setfield@PLT
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE4:
	.size	luaopen_curses, .-luaopen_curses
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
