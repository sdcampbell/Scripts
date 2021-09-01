#!/usr/bin/env python3

from pwn import *
import sys

def find_ip(payload):
    corefile = Coredump('./core')
    if corefile.bits == 32:
        ip_offset = cyclic_find(corefile.pc)
    else:
        ip_offset = cyclic_find(corefile.read(corefile.sp, 4))
    ip_offset = cyclic_find(corefile.read(corefile.sp, 4))  # x64
    info('located offset at {a}'.format(a=ip_offset))
    return ip_offset
    
def main():
    if len(sys.argv) < 2:
        print("""
              Finds the offset from the stack pointer to the return address from a core dump.
              Expects to find a core file in the current working directory

              Usage: findoffset [size]""")
        sys.exit()
    offset = find_ip(cyclic(int(sys.argv[1])))
    
if __name__ == "__main__":
    main()

