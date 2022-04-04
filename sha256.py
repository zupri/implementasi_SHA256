# Implementasi dokumen SHA-256 kedalam bahasa pemrograman python

import sys
import os.path
import operation as opr

def text_aligment(text: str, length: int = 128):
    t = ''
    for i in range(0, len(text),length):
        t += str(text[i:i+length])+'\n'
    return t

if len(sys.argv) is 3 or len(sys.argv) is 2:
    file = sys.argv[1]
    view = ''
    if len(sys.argv) is 3 :
        view = sys.argv[2]
    
    if os.path.isfile(file):
        with open(file, "rb") as f :
            message = f.read()
        if isinstance(message, str) :
            message = bytearray(message)
            print(f'message dari file : {file}')
        elif isinstance(message, bytes):
            message = bytearray(message)
        elif not isinstance(message, bytearray):
            print('BUKAN DATA BYTE')
            raise TypeError
    else:
        message = bytearray(file,'utf-8')
        print('='*128)
        print('file tidak ditemukan :\nMessage = {}'.format(file))
else:
    print('Ketik sbb :\n{} message [v]\n'.format(sys.argv[0]))
    print('option :')
    print('    message    message burapa string langsung atau file')
    print('    v          Menampilkan hasil operasi jika tidak ada maka')
    print('               panjang message dibawah atau sama dengan 1976')
    print('               akan ditampilkan')
    exit()

lenMessage = len(message)*8

if view == "v" or lenMessage <= 1976 :
    show = True
else :
    show = False

info_message = str(f'! Panjang Message {lenMessage} lebih dari 1976, hasil tidak ditampilkan')
print('='*128)
print('Message dalam (hex) :')
print('-'*128)
if show :
    print(text_aligment(message.hex()))
else:
    print(info_message)
print('='*128)


# A. PREPROCESSING

print('\n')
print('='*128)
print('A. PREPROCESSING')
print('-'*128)

l = len(message)*8 # Jumlah bit = byte*8
print('Panjang message asli (bit) = ',l)

# A.1.a Menambahkan bit 1
message.append(0x80)
lpad = len(message) * 8 # Jumlah bit = byte*8
print('Panjang message setelah penambahan bit \'10000000\' (bit) = ',lpad)

# A.1.b menambahkan bit 0 sebanyak k
k = (448-lpad) % 512
message += b'\x00' * (k//8) # berikan bit '0' sebanyak k
print('Panjang message setelah penambahan bit \'0\' sebanyak {} (bit) = {}'.format(k,len(message)*8))

# A.1.c menambahkan informasi panjang message
message += l.to_bytes(8,'big') # pad 64 bit
print('Panjang message setelah penambahan 64 bit info length = {}'.format(len(message)*8))

# A.1.d Cek Padding message
if (len(message) * 8) % 512 == 0 : 
    print('Padding sudah benar message {} mod 512 = 0'.format(len(message)*8))
else:
    print('Padding tidak benar message {} mod 512 != 0'.format(len(message)*8))


print('message padding (hex) :')
if show :
    print(text_aligment(message.hex()))
else:
    print(info_message)
print('-'*128)


# A.2 Parsing message kedalam block
blocks = [] # berisi 512-bit potongan message
for i in range(0, len(message), 64): # 64 bytes adalah 512 bits
    blocks.append(message[i:i+64])

Nblock = (len(message)*8)//512
print('Jumlah N blok = ', Nblock)

  
for index, val in enumerate(blocks) :
    print('M({}) :\n{}'.format(index+1,val.hex()))
print(128*'=','\n')

# A.3 Setting nilai inisial Hash.
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h5 = 0x9b05688c
h4 = 0x510e527f
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

# B. HASH COMPUTATION


print('='*128)
print('B. HASH COMPUTATION\n')
print('-'*128)

# B. Iterasi N block
for index, message_block in enumerate(blocks):
    blok_header = f' Blok ke-{index+1} dari total {Nblock} blok '
    odd = 0 if (len(blok_header)%2 == 0) else 1
    print('='*(63-len(blok_header)//2) + blok_header + '='*(63-len(blok_header)//2) + '='*odd)

    # B.1 Menyiapkan message schedule
    
    print('B.1 Menyiapkan message schedule')
    if not show :
        print(f'    {info_message}')
    
    message_schedule = []
    for t in range(0, 64):

            # B.1.a Untuk t dari 0 s/d 15.
        if t <= 15:
            message_schedule.append(bytes(message_block[t*4:(t*4)+4]))
        else:

            # B.1.b Untuk t dari 16 s/d 63.
            wt2 = opr.sigma1(int.from_bytes(message_schedule[t-2], 'big'))
            wt7 = int.from_bytes(message_schedule[t-7], 'big')
            wt15 = opr.sigma0(int.from_bytes(message_schedule[t-15], 'big'))
            wt16 = int.from_bytes(message_schedule[t-16], 'big')
    
            schedule = ((wt2 + wt7 + wt15 + wt16) % 2**32).to_bytes(4, 'big')
            message_schedule.append(schedule)
    
    if show :
        print('    Message schedule M({}):'.format(index+1))
        print('    untuk t0 s/d t15 :')
        for idx, val in enumerate(message_schedule) :
            if idx <= 15:
                print('    W[{}] = M({})[{}] =  {}'.format(idx,index+1,idx,val.hex()))

        print('\n    untuk t16 s/d t63 :')
        for idx, val in enumerate(message_schedule) :
            if idx >= 16:
                print('    W[{}] = M({})[{}] =  {}'.format(idx,index+1,idx,val.hex()))

   # B.2 Inisialisasi delapan working variable
    print('\nB.2 Inisialisasi delapan working variable')

    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7
        
    print('    Hash value ke-(i-1) block ke-{} dari total {} block :'.format(index+1,Nblock))    
    print('    H({})0 = {} '.format(index,hex(h0)))
    print('    H({})1 = {} '.format(index,hex(h1)))
    print('    H({})2 = {} '.format(index,hex(h2)))
    print('    H({})3 = {} '.format(index,hex(h3)))
    print('    H({})4 = {} '.format(index,hex(h4)))
    print('    H({})5 = {} '.format(index,hex(h5)))
    print('    H({})6 = {} '.format(index,hex(h6)))
    print('    H({})7 = {} '.format(index,hex(h7)))    
    
    print('\nB.3 Menghitung working variable yang baru.')
    print('    t(t) |     a     |     b    |    c     |     d    |     e    |     f    |     g    |     h     |')
    
    # B.3 Menghitung working variable yang baru.
    for t in range(64):
        t1 = ((h + opr.sum1(e) + opr.ch(e, f, g) + opr.K[t] +
               int.from_bytes(message_schedule[t], 'big')) % 2**32)
        
        t2 = (opr.sum0(a) + opr.maj(a, b, c)) % 2**32
        
        h = g
        g = f
        f = e
        e = (d + t1) % 2**32
        d = c
        c = b
        b = a
        a = (t1 + t2) % 2**32

        if show :
            print(f'    t({t}) : {hex(a)} {hex(b)} {hex(c)} {hex(d)} {hex(e)} {hex(f)} {hex(g)} {hex(h)} ')

    if not show :
        print(f'    {info_message}')

    print('\n    Hasil operasi working variable block(i) {} dari tota(N) {} block.'.format(index+1,Nblock))
    print('    a = ',hex(a))
    print('    b = ',hex(b))
    print('    c = ',hex(c))
    print('    d = ',hex(d))
    print('    e = ',hex(e))
    print('    f = ',hex(f))
    print('    g = ',hex(g))
    print('    h = ',hex(h))

    # B.4 Menjumlahkan hash value.
    
    print('\nB.4 Menjumlahkan hash value.')
    h0 = (h0 + a) % 2**32
    h1 = (h1 + b) % 2**32
    h2 = (h2 + c) % 2**32
    h3 = (h3 + d) % 2**32
    h4 = (h4 + e) % 2**32
    h5 = (h5 + f) % 2**32
    h6 = (h6 + g) % 2**32
    h7 = (h7 + h) % 2**32

    print('    H({})0 = {}'.format(index+1,hex(h0)))
    print('    H({})1 = {}'.format(index+1,hex(h1)))
    print('    H({})2 = {}'.format(index+1,hex(h2)))
    print('    H({})3 = {}'.format(index+1,hex(h3)))
    print('    H({})4 = {}'.format(index+1,hex(h4)))
    print('    H({})5 = {}'.format(index+1,hex(h5)))
    print('    H({})6 = {}'.format(index+1,hex(h6)))
    print('    H({})7 = {}'.format(index+1,hex(h7)))

message_digest  = (h0).to_bytes(4, 'big')
message_digest += (h1).to_bytes(4, 'big')
message_digest += (h2).to_bytes(4, 'big')
message_digest += (h3).to_bytes(4, 'big')
message_digest += (h4).to_bytes(4, 'big')
message_digest += (h5).to_bytes(4, 'big')
message_digest += (h6).to_bytes(4, 'big')
message_digest += (h7).to_bytes(4, 'big')
        
print(('\nMessage digest Akhir dari H(M):\n{}'.format(message_digest.hex()).upper()))

# H('abc') = ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad

# text.txt = 12519f7a5eee9c9473df9142a882a44b5133a2f2850881453d82254563e00a0a
