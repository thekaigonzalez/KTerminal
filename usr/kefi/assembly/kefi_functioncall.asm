define _start


call kefi_load


call kefi_init

call kefi_main

_main:
    call kefi_return
    hlt