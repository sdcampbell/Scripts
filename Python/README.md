# Python Script Descriptions

## b64_encode_image.py

Base 64 encodes a jpg or png image file and outputs to the clipboard the image tag to embed in HTML. I use this to make it easy to create blog posts without having to worry about where I save my image and the path, and by embedding the image in the page I don't have to worry about deleting the image when I delete the post.

## find_offset.py

Finds the offset from the stack pointer to the return address from a core dump.

Expects to find a core file in the current working directory

Usage: python3 find_offset.py [length]

```
$ findoffset 1000
[+] Parsing corefile...: Done
[*] '/home/kali/Downloads/htb/pwn/htb-reg/core'
    Arch:      amd64-64-little
    RIP:       0x4012ac
    RSP:       0x7ffc9b18a0b8
    Exe:       '/home/kali/Downloads/htb/pwn/htb-reg/reg' (0x400000)
[*] located offset at 56
```

## iplist.py

iplist prints out a list of IP addresses when given a subnet as the only argument.

Usage: `python3 iplist.py 192.168.1.0/24`
