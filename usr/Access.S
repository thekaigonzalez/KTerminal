	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 11, 0	sdk_version 11, 3
	.globl	_proc_init                      ## -- Begin function proc_init
	.p2align	4, 0x90
_proc_init:                             ## @proc_init
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movl	$45, %eax
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_main                           ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$112, %rsp
	movl	$0, -4(%rbp)
	movl	%edi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	leaq	L_.str(%rip), %rdi
	movb	$0, %al
	callq	_printf
	leaq	L_.str.1(%rip), %rdi
	leaq	L_.str.2(%rip), %rsi
	movl	%eax, -60(%rbp)                 ## 4-byte Spill
	callq	_fopen
	movq	%rax, -24(%rbp)
	leaq	L_.str.3(%rip), %rdi
	leaq	L_.str.2(%rip), %rsi
	callq	_fopen
	movq	%rax, -32(%rbp)
	leaq	L_.str.1(%rip), %rdi
	leaq	L_.str.2(%rip), %rsi
	callq	_fopen
	movq	%rax, -40(%rbp)
	leaq	L_.str.4(%rip), %rdi
	leaq	L_.str.2(%rip), %rsi
	callq	_fopen
	movq	%rax, -48(%rbp)
	leaq	L_.str.5(%rip), %rdi
	leaq	L_.str.2(%rip), %rsi
	callq	_fopen
	movq	%rax, -56(%rbp)
	movq	-32(%rbp), %rsi
	leaq	L_.str.6(%rip), %rdi
	callq	_fputs
	movq	-40(%rbp), %rsi
	leaq	L_.str.7(%rip), %rdi
	movl	%eax, -64(%rbp)                 ## 4-byte Spill
	callq	_fputs
	movq	-48(%rbp), %rsi
	leaq	L_.str.8(%rip), %rdi
	movl	%eax, -68(%rbp)                 ## 4-byte Spill
	callq	_fputs
	movq	-56(%rbp), %rsi
	leaq	L_.str.9(%rip), %rdi
	movl	%eax, -72(%rbp)                 ## 4-byte Spill
	callq	_fputs
	movq	-24(%rbp), %rsi
	leaq	L_.str.10(%rip), %rdi
	movl	%eax, -76(%rbp)                 ## 4-byte Spill
	callq	_fputs
	movq	-24(%rbp), %rdi
	movl	%eax, -80(%rbp)                 ## 4-byte Spill
	callq	_fclose
	movq	-40(%rbp), %rdi
	movl	%eax, -84(%rbp)                 ## 4-byte Spill
	callq	_fclose
	movq	-32(%rbp), %rdi
	movl	%eax, -88(%rbp)                 ## 4-byte Spill
	callq	_fclose
	movq	-56(%rbp), %rdi
	movl	%eax, -92(%rbp)                 ## 4-byte Spill
	callq	_fclose
	movq	-48(%rbp), %rdi
	movl	%eax, -96(%rbp)                 ## 4-byte Spill
	callq	_fclose
	leaq	L_.str.11(%rip), %rdi
	movl	%eax, -100(%rbp)                ## 4-byte Spill
	movb	$0, %al
	callq	_printf
	movl	$1, %ecx
	movl	%eax, -104(%rbp)                ## 4-byte Spill
	movl	%ecx, %eax
	addq	$112, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"Creating a few configuration files...\n"

L_.str.1:                               ## @.str.1
	.asciz	"./iso.cfg"

L_.str.2:                               ## @.str.2
	.asciz	"w"

L_.str.3:                               ## @.str.3
	.asciz	"./fs.cfg"

L_.str.4:                               ## @.str.4
	.asciz	"./inno.cfg"

L_.str.5:                               ## @.str.5
	.asciz	"./setup.cfg"

L_.str.6:                               ## @.str.6
	.asciz	"valid=true"

L_.str.7:                               ## @.str.7
	.asciz	"checker=true\nusr=true\ndir=usr/clib"

L_.str.8:                               ## @.str.8
	.asciz	"../"

L_.str.9:                               ## @.str.9
	.asciz	"INLINE=FALSE"

L_.str.10:                              ## @.str.10
	.asciz	"STD=10"

L_.str.11:                              ## @.str.11
	.asciz	"done"

.subsections_via_symbols
