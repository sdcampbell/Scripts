from pwn import *
import sys

def find_ip(payload):
    corefile = Coredump('./core')
    if corefile.bits == 32:
        ip_offset = cyclic_find(corefile.pc)
    else:
        ip_offset = cyclic_find(corefile.read(corefile.sp, 4))
    ip_offset = cyclic_find(corefile.read(corefile.sp, 4))  # x64
    info('located EIP/RIP offset at {a}'.format(a=ip_offset))
    return ip_offset
    
def main():
    offset = find_ip(cyclic(int(sys.argv[1])))
    
if __name__ == "__main__":
    main()
