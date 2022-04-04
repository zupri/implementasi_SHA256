## Implementasi dokumen SHA-256 kedalam bahasa pemrograman python

Script ini dibuat untuk tujuan latihan tanpa mempertimbangkan efisiensi cpu dan memory.

Cara menggunakan program ini cukup jalankan file `sha256.py` sebagai berikut

```
$ python -m shs256 message [v]

message    message burapa string langsung atau file
v          Menampilkan hasil operasi yang panjang message
           lebih dari atau sama dengan 1976'
```

### Contoh
```shell
$ python -m sha256 abc
```
hasil :
```shell
================================================================================================================================
file tidak ditemukan :
Message = abc
================================================================================================================================
Message dalam (hex) :
--------------------------------------------------------------------------------------------------------------------------------
616263

================================================================================================================================


================================================================================================================================
A. PREPROCESSING
--------------------------------------------------------------------------------------------------------------------------------
Panjang message asli (bit) =  24
Panjang message setelah penambahan bit '10000000' (bit) =  32
Panjang message setelah penambahan bit '0' sebanyak 416 (bit) = 448
Panjang message setelah penambahan 64 bit info length = 512
Padding sudah benar message 512 mod 512 = 0
message padding (hex) :
61626380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000018

--------------------------------------------------------------------------------------------------------------------------------
Jumlah N blok =  1
M(1) :
61626380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000018
================================================================================================================================ 

================================================================================================================================
B. HASH COMPUTATION

--------------------------------------------------------------------------------------------------------------------------------
================================================= Blok ke-1 dari total 1 blok ==================================================
B.1 Menyiapkan message schedule
    Message schedule M(1):
    untuk t0 s/d t15 :
    W[0] = M(1)[0] =  61626380
    W[1] = M(1)[1] =  00000000
    W[2] = M(1)[2] =  00000000
    W[3] = M(1)[3] =  00000000
    W[4] = M(1)[4] =  00000000
    W[5] = M(1)[5] =  00000000
    W[6] = M(1)[6] =  00000000
    W[7] = M(1)[7] =  00000000
    W[8] = M(1)[8] =  00000000
    W[9] = M(1)[9] =  00000000
    W[10] = M(1)[10] =  00000000
    W[11] = M(1)[11] =  00000000
    W[12] = M(1)[12] =  00000000
    W[13] = M(1)[13] =  00000000
    W[14] = M(1)[14] =  00000000
    W[15] = M(1)[15] =  00000018

    untuk t16 s/d t63 :
    W[16] = M(1)[16] =  61626380
    W[17] = M(1)[17] =  000f0000
    W[18] = M(1)[18] =  7da86405
    W[19] = M(1)[19] =  600003c6
    W[20] = M(1)[20] =  3e9d7b78
    W[21] = M(1)[21] =  0183fc00
    W[22] = M(1)[22] =  12dcbfdb
    W[23] = M(1)[23] =  e2e2c38e
    W[24] = M(1)[24] =  c8215c1a
    W[25] = M(1)[25] =  b73679a2
    W[26] = M(1)[26] =  e5bc3909
    W[27] = M(1)[27] =  32663c5b
    W[28] = M(1)[28] =  9d209d67
    W[29] = M(1)[29] =  ec8726cb
    W[30] = M(1)[30] =  702138a4
    W[31] = M(1)[31] =  d3b7973b
    W[32] = M(1)[32] =  93f5997f
    W[33] = M(1)[33] =  3b68ba73
    W[34] = M(1)[34] =  aff4ffc1
    W[35] = M(1)[35] =  f10a5c62
    W[36] = M(1)[36] =  0a8b3996
    W[37] = M(1)[37] =  72af830a
    W[38] = M(1)[38] =  9409e33e
    W[39] = M(1)[39] =  24641522
    W[40] = M(1)[40] =  9f47bf94
    W[41] = M(1)[41] =  f0a64f5a
    W[42] = M(1)[42] =  3e246a79
    W[43] = M(1)[43] =  27333ba3
    W[44] = M(1)[44] =  0c4763f2
    W[45] = M(1)[45] =  840abf27
    W[46] = M(1)[46] =  7a290d5d
    W[47] = M(1)[47] =  065c43da
    W[48] = M(1)[48] =  fb3e89cb
    W[49] = M(1)[49] =  cc7617db
    W[50] = M(1)[50] =  b9e66c34
    W[51] = M(1)[51] =  a9993667
    W[52] = M(1)[52] =  84badedd
    W[53] = M(1)[53] =  c21462bc
    W[54] = M(1)[54] =  1487472c
    W[55] = M(1)[55] =  b20f7a99
    W[56] = M(1)[56] =  ef57b9cd
    W[57] = M(1)[57] =  ebe6b238
    W[58] = M(1)[58] =  9fe3095e
    W[59] = M(1)[59] =  78bc8d4b
    W[60] = M(1)[60] =  a43fcf15
    W[61] = M(1)[61] =  668b2ff8
    W[62] = M(1)[62] =  eeaba2cc
    W[63] = M(1)[63] =  12b1edeb

B.2 Inisialisasi delapan working variable
    Hash value ke-(i-1) block ke-1 dari total 1 block :
    H(0)0 = 0x6a09e667 
    H(0)1 = 0xbb67ae85 
    H(0)2 = 0x3c6ef372 
    H(0)3 = 0xa54ff53a 
    H(0)4 = 0x510e527f 
    H(0)5 = 0x9b05688c 
    H(0)6 = 0x1f83d9ab 
    H(0)7 = 0x5be0cd19 

B.3 Menghitung working variable yang baru.
    t(t) |     a     |     b    |    c     |     d    |     e    |     f    |     g    |     h     |
    t(0) : 0x5d6aebcd 0x6a09e667 0xbb67ae85 0x3c6ef372 0xfa2a4622 0x510e527f 0x9b05688c 0x1f83d9ab 
    t(1) : 0x5a6ad9ad 0x5d6aebcd 0x6a09e667 0xbb67ae85 0x78ce7989 0xfa2a4622 0x510e527f 0x9b05688c 
    t(2) : 0xc8c347a7 0x5a6ad9ad 0x5d6aebcd 0x6a09e667 0xf92939eb 0x78ce7989 0xfa2a4622 0x510e527f 
    t(3) : 0xd550f666 0xc8c347a7 0x5a6ad9ad 0x5d6aebcd 0x24e00850 0xf92939eb 0x78ce7989 0xfa2a4622 
    t(4) : 0x4409a6a 0xd550f666 0xc8c347a7 0x5a6ad9ad 0x43ada245 0x24e00850 0xf92939eb 0x78ce7989 
    t(5) : 0x2b4209f5 0x4409a6a 0xd550f666 0xc8c347a7 0x714260ad 0x43ada245 0x24e00850 0xf92939eb 
    t(6) : 0xe5030380 0x2b4209f5 0x4409a6a 0xd550f666 0x9b27a401 0x714260ad 0x43ada245 0x24e00850 
    t(7) : 0x85a07b5f 0xe5030380 0x2b4209f5 0x4409a6a 0xc657a79 0x9b27a401 0x714260ad 0x43ada245 
    t(8) : 0x8e04ecb9 0x85a07b5f 0xe5030380 0x2b4209f5 0x32ca2d8c 0xc657a79 0x9b27a401 0x714260ad 
    t(9) : 0x8c87346b 0x8e04ecb9 0x85a07b5f 0xe5030380 0x1cc92596 0x32ca2d8c 0xc657a79 0x9b27a401 
    t(10) : 0x4798a3f4 0x8c87346b 0x8e04ecb9 0x85a07b5f 0x436b23e8 0x1cc92596 0x32ca2d8c 0xc657a79 
    t(11) : 0xf71fc5a9 0x4798a3f4 0x8c87346b 0x8e04ecb9 0x816fd6e9 0x436b23e8 0x1cc92596 0x32ca2d8c 
    t(12) : 0x87912990 0xf71fc5a9 0x4798a3f4 0x8c87346b 0x1e578218 0x816fd6e9 0x436b23e8 0x1cc92596 
    t(13) : 0xd932eb16 0x87912990 0xf71fc5a9 0x4798a3f4 0x745a48de 0x1e578218 0x816fd6e9 0x436b23e8 
    t(14) : 0xc0645fde 0xd932eb16 0x87912990 0xf71fc5a9 0xb92f20c 0x745a48de 0x1e578218 0x816fd6e9 
    t(15) : 0xb0fa238e 0xc0645fde 0xd932eb16 0x87912990 0x7590dcd 0xb92f20c 0x745a48de 0x1e578218 
    t(16) : 0x21da9a9b 0xb0fa238e 0xc0645fde 0xd932eb16 0x8034229c 0x7590dcd 0xb92f20c 0x745a48de 
    t(17) : 0xc2fbd9d1 0x21da9a9b 0xb0fa238e 0xc0645fde 0x846ee454 0x8034229c 0x7590dcd 0xb92f20c 
    t(18) : 0xfe777bbf 0xc2fbd9d1 0x21da9a9b 0xb0fa238e 0xcc899961 0x846ee454 0x8034229c 0x7590dcd 
    t(19) : 0xe1f20c33 0xfe777bbf 0xc2fbd9d1 0x21da9a9b 0xb0638179 0xcc899961 0x846ee454 0x8034229c 
    t(20) : 0x9dc68b63 0xe1f20c33 0xfe777bbf 0xc2fbd9d1 0x8ada8930 0xb0638179 0xcc899961 0x846ee454 
    t(21) : 0xc2606d6d 0x9dc68b63 0xe1f20c33 0xfe777bbf 0xe1257970 0x8ada8930 0xb0638179 0xcc899961 
    t(22) : 0xa7a3623f 0xc2606d6d 0x9dc68b63 0xe1f20c33 0x49f5114a 0xe1257970 0x8ada8930 0xb0638179 
    t(23) : 0xc5d53d8d 0xa7a3623f 0xc2606d6d 0x9dc68b63 0xaa47c347 0x49f5114a 0xe1257970 0x8ada8930 
    t(24) : 0x1c2c2838 0xc5d53d8d 0xa7a3623f 0xc2606d6d 0x2823ef91 0xaa47c347 0x49f5114a 0xe1257970 
    t(25) : 0xcde8037d 0x1c2c2838 0xc5d53d8d 0xa7a3623f 0x14383d8e 0x2823ef91 0xaa47c347 0x49f5114a 
    t(26) : 0xb62ec4bc 0xcde8037d 0x1c2c2838 0xc5d53d8d 0xc74c6516 0x14383d8e 0x2823ef91 0xaa47c347 
    t(27) : 0x77d37528 0xb62ec4bc 0xcde8037d 0x1c2c2838 0xedffbff8 0xc74c6516 0x14383d8e 0x2823ef91 
    t(28) : 0x363482c9 0x77d37528 0xb62ec4bc 0xcde8037d 0x6112a3b7 0xedffbff8 0xc74c6516 0x14383d8e 
    t(29) : 0xa0060b30 0x363482c9 0x77d37528 0xb62ec4bc 0xade79437 0x6112a3b7 0xedffbff8 0xc74c6516 
    t(30) : 0xea992a22 0xa0060b30 0x363482c9 0x77d37528 0x109ab3a 0xade79437 0x6112a3b7 0xedffbff8 
    t(31) : 0x73b33bf5 0xea992a22 0xa0060b30 0x363482c9 0xba591112 0x109ab3a 0xade79437 0x6112a3b7 
    t(32) : 0x98e12507 0x73b33bf5 0xea992a22 0xa0060b30 0x9cd9f5f6 0xba591112 0x109ab3a 0xade79437 
    t(33) : 0xfe604df5 0x98e12507 0x73b33bf5 0xea992a22 0x59249dd3 0x9cd9f5f6 0xba591112 0x109ab3a 
    t(34) : 0xa9a7738c 0xfe604df5 0x98e12507 0x73b33bf5 0x85f3833 0x59249dd3 0x9cd9f5f6 0xba591112 
    t(35) : 0x65a0cfe4 0xa9a7738c 0xfe604df5 0x98e12507 0xf4b002d6 0x85f3833 0x59249dd3 0x9cd9f5f6 
    t(36) : 0x41a65cb1 0x65a0cfe4 0xa9a7738c 0xfe604df5 0x772a26b 0xf4b002d6 0x85f3833 0x59249dd3 
    t(37) : 0x34df1604 0x41a65cb1 0x65a0cfe4 0xa9a7738c 0xa507a53d 0x772a26b 0xf4b002d6 0x85f3833 
    t(38) : 0x6dc57a8a 0x34df1604 0x41a65cb1 0x65a0cfe4 0xf0781bc8 0xa507a53d 0x772a26b 0xf4b002d6 
    t(39) : 0x79ea687a 0x6dc57a8a 0x34df1604 0x41a65cb1 0x1efbc0a0 0xf0781bc8 0xa507a53d 0x772a26b 
    t(40) : 0xd6670766 0x79ea687a 0x6dc57a8a 0x34df1604 0x26352d63 0x1efbc0a0 0xf0781bc8 0xa507a53d 
    t(41) : 0xdf46652f 0xd6670766 0x79ea687a 0x6dc57a8a 0x838b2711 0x26352d63 0x1efbc0a0 0xf0781bc8 
    t(42) : 0x17aa0dfe 0xdf46652f 0xd6670766 0x79ea687a 0xdecd4715 0x838b2711 0x26352d63 0x1efbc0a0 
    t(43) : 0x9d4baf93 0x17aa0dfe 0xdf46652f 0xd6670766 0xfda24c2e 0xdecd4715 0x838b2711 0x26352d63 
    t(44) : 0x26628815 0x9d4baf93 0x17aa0dfe 0xdf46652f 0xa80f11f0 0xfda24c2e 0xdecd4715 0x838b2711 
    t(45) : 0x72ab4b91 0x26628815 0x9d4baf93 0x17aa0dfe 0xb7755da1 0xa80f11f0 0xfda24c2e 0xdecd4715 
    t(46) : 0xa14c14b0 0x72ab4b91 0x26628815 0x9d4baf93 0xd57b94a9 0xb7755da1 0xa80f11f0 0xfda24c2e 
    t(47) : 0x4172328d 0xa14c14b0 0x72ab4b91 0x26628815 0xfecf0bc6 0xd57b94a9 0xb7755da1 0xa80f11f0 
    t(48) : 0x5757ceb 0x4172328d 0xa14c14b0 0x72ab4b91 0xbd714038 0xfecf0bc6 0xd57b94a9 0xb7755da1 
    t(49) : 0xf11bfaa8 0x5757ceb 0x4172328d 0xa14c14b0 0x6e5c390c 0xbd714038 0xfecf0bc6 0xd57b94a9 
    t(50) : 0x7a0508a1 0xf11bfaa8 0x5757ceb 0x4172328d 0x52f1ccf7 0x6e5c390c 0xbd714038 0xfecf0bc6 
    t(51) : 0x886e7a22 0x7a0508a1 0xf11bfaa8 0x5757ceb 0x49231c1e 0x52f1ccf7 0x6e5c390c 0xbd714038 
    t(52) : 0x101fd28f 0x886e7a22 0x7a0508a1 0xf11bfaa8 0x529e7d00 0x49231c1e 0x52f1ccf7 0x6e5c390c 
    t(53) : 0xf5702fdb 0x101fd28f 0x886e7a22 0x7a0508a1 0x9f4787c3 0x529e7d00 0x49231c1e 0x52f1ccf7 
    t(54) : 0x3ec45cdb 0xf5702fdb 0x101fd28f 0x886e7a22 0xe50e1b4f 0x9f4787c3 0x529e7d00 0x49231c1e 
    t(55) : 0x38cc9913 0x3ec45cdb 0xf5702fdb 0x101fd28f 0x54cb266b 0xe50e1b4f 0x9f4787c3 0x529e7d00 
    t(56) : 0xfcd1887b 0x38cc9913 0x3ec45cdb 0xf5702fdb 0x9b5e906c 0x54cb266b 0xe50e1b4f 0x9f4787c3 
    t(57) : 0xc062d46f 0xfcd1887b 0x38cc9913 0x3ec45cdb 0x7e44008e 0x9b5e906c 0x54cb266b 0xe50e1b4f 
    t(58) : 0xffb70472 0xc062d46f 0xfcd1887b 0x38cc9913 0x6d83bfc6 0x7e44008e 0x9b5e906c 0x54cb266b 
    t(59) : 0xb6ae8fff 0xffb70472 0xc062d46f 0xfcd1887b 0xb21bad3d 0x6d83bfc6 0x7e44008e 0x9b5e906c 
    t(60) : 0xb85e2ce9 0xb6ae8fff 0xffb70472 0xc062d46f 0x961f4894 0xb21bad3d 0x6d83bfc6 0x7e44008e 
    t(61) : 0x4d24d6c 0xb85e2ce9 0xb6ae8fff 0xffb70472 0x948d25b6 0x961f4894 0xb21bad3d 0x6d83bfc6 
    t(62) : 0xd39a2165 0x4d24d6c 0xb85e2ce9 0xb6ae8fff 0xfb121210 0x948d25b6 0x961f4894 0xb21bad3d 
    t(63) : 0x506e3058 0xd39a2165 0x4d24d6c 0xb85e2ce9 0x5ef50f24 0xfb121210 0x948d25b6 0x961f4894 

    Hasil operasi working variable block(i) 1 dari tota(N) 1 block.
    a =  0x506e3058
    b =  0xd39a2165
    c =  0x4d24d6c
    d =  0xb85e2ce9
    e =  0x5ef50f24
    f =  0xfb121210
    g =  0x948d25b6
    h =  0x961f4894

B.4 Menjumlahkan hash value.
    H(1)0 = 0xba7816bf
    H(1)1 = 0x8f01cfea
    H(1)2 = 0x414140de
    H(1)3 = 0x5dae2223
    H(1)4 = 0xb00361a3
    H(1)5 = 0x96177a9c
    H(1)6 = 0xb410ff61
    H(1)7 = 0xf20015ad

MESSAGE DIGEST AKHIR DARI H(M):
BA7816BF8F01CFEA414140DE5DAE2223B00361A396177A9CB410FF61F20015AD
```