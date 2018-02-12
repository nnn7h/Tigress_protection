#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_5743 = ref_239 # MOV operation
ref_5747 = ((0xDEADBEEFDEADBEEF + ref_5743) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5854 = ref_5747 # MOV operation
ref_5856 = (0xE6ADBEEFDEADBEEF ^ ref_5854) # XOR operation
ref_5877 = ref_5747 # MOV operation
ref_5881 = ref_5877 # MOV operation
ref_5925 = ref_5881 # MOV operation
ref_5929 = rol(0xF, ref_5925) # ROL operation
ref_5933 = ref_5929 # MOV operation
ref_5940 = ref_5933 # MOV operation
ref_5956 = ref_5856 # MOV operation
ref_5960 = ref_5940 # MOV operation
ref_5962 = ((ref_5956 + ref_5960) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5988 = ref_5962 # MOV operation
ref_5990 = (0x1234 ^ ref_5988) # XOR operation
ref_6011 = ref_5962 # MOV operation
ref_6015 = ref_6011 # MOV operation
ref_6059 = ref_6015 # MOV operation
ref_6063 = rol(0x34, ref_6059) # ROL operation
ref_6067 = ref_6063 # MOV operation
ref_6074 = ref_6067 # MOV operation
ref_6090 = ref_5990 # MOV operation
ref_6094 = ref_6074 # MOV operation
ref_6096 = ((ref_6090 + ref_6094) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6122 = ref_6096 # MOV operation
ref_6124 = (0x1234 ^ ref_6122) # XOR operation
ref_6145 = ref_6096 # MOV operation
ref_6149 = ref_6145 # MOV operation
ref_6193 = ref_6149 # MOV operation
ref_6197 = rol(0x1A, ref_6193) # ROL operation
ref_6201 = ref_6197 # MOV operation
ref_6208 = ref_6201 # MOV operation
ref_6224 = ref_6124 # MOV operation
ref_6228 = ref_6208 # MOV operation
ref_6230 = ((ref_6224 + ref_6228) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6252 = ref_5940 # MOV operation
ref_6256 = ref_6230 # MOV operation
ref_6258 = (ref_6252 ^ ref_6256) # XOR operation
ref_6279 = ref_6230 # MOV operation
ref_6283 = ref_6279 # MOV operation
ref_6327 = ref_6283 # MOV operation
ref_6331 = rol(0x33, ref_6327) # ROL operation
ref_6335 = ref_6331 # MOV operation
ref_6342 = ref_6335 # MOV operation
ref_6358 = ref_6258 # MOV operation
ref_6362 = ref_6342 # MOV operation
ref_6364 = ((ref_6358 + ref_6362) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6386 = ref_6074 # MOV operation
ref_6390 = ref_6364 # MOV operation
ref_6392 = (ref_6386 ^ ref_6390) # XOR operation
ref_6413 = ref_6364 # MOV operation
ref_6417 = ref_6413 # MOV operation
ref_6461 = ref_6417 # MOV operation
ref_6465 = rol(0x1C, ref_6461) # ROL operation
ref_6469 = ref_6465 # MOV operation
ref_6476 = ref_6469 # MOV operation
ref_6492 = ref_6392 # MOV operation
ref_6496 = ref_6476 # MOV operation
ref_6498 = ((ref_6492 + ref_6496) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6520 = ref_6208 # MOV operation
ref_6524 = ref_6498 # MOV operation
ref_6526 = (ref_6520 ^ ref_6524) # XOR operation
ref_6547 = ref_6498 # MOV operation
ref_6551 = ref_6547 # MOV operation
ref_6595 = ref_6551 # MOV operation
ref_6599 = rol(0x9, ref_6595) # ROL operation
ref_6603 = ref_6599 # MOV operation
ref_6610 = ref_6603 # MOV operation
ref_6626 = ref_6526 # MOV operation
ref_6630 = ref_6610 # MOV operation
ref_6632 = ((ref_6626 + ref_6630) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6654 = ref_6342 # MOV operation
ref_6658 = ref_6632 # MOV operation
ref_6660 = (ref_6654 ^ ref_6658) # XOR operation
ref_6681 = ref_6632 # MOV operation
ref_6685 = ref_6681 # MOV operation
ref_6729 = ref_6685 # MOV operation
ref_6733 = rol(0x2F, ref_6729) # ROL operation
ref_6737 = ref_6733 # MOV operation
ref_6744 = ref_6737 # MOV operation
ref_6760 = ref_6660 # MOV operation
ref_6764 = ref_6744 # MOV operation
ref_6766 = ((ref_6760 + ref_6764) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6788 = ref_6476 # MOV operation
ref_6792 = ref_6766 # MOV operation
ref_6794 = (ref_6788 ^ ref_6792) # XOR operation
ref_6815 = ref_6766 # MOV operation
ref_6819 = ref_6815 # MOV operation
ref_6863 = ref_6819 # MOV operation
ref_6867 = rol(0x36, ref_6863) # ROL operation
ref_6871 = ref_6867 # MOV operation
ref_6878 = ref_6871 # MOV operation
ref_6894 = ref_6794 # MOV operation
ref_6898 = ref_6878 # MOV operation
ref_6900 = ((ref_6894 + ref_6898) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6922 = ref_6610 # MOV operation
ref_6926 = ref_6900 # MOV operation
ref_6928 = (ref_6922 ^ ref_6926) # XOR operation
ref_6949 = ref_6900 # MOV operation
ref_6953 = ref_6949 # MOV operation
ref_6997 = ref_6953 # MOV operation
ref_7001 = rol(0x20, ref_6997) # ROL operation
ref_7005 = ref_7001 # MOV operation
ref_7012 = ref_7005 # MOV operation
ref_7028 = ref_6928 # MOV operation
ref_7032 = ref_7012 # MOV operation
ref_7034 = ((ref_7028 + ref_7032) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7056 = ref_6744 # MOV operation
ref_7060 = ref_7034 # MOV operation
ref_7062 = (ref_7056 ^ ref_7060) # XOR operation
ref_7083 = ref_7034 # MOV operation
ref_7087 = ref_7083 # MOV operation
ref_7131 = ref_7087 # MOV operation
ref_7135 = rol(0x19, ref_7131) # ROL operation
ref_7139 = ref_7135 # MOV operation
ref_7146 = ref_7139 # MOV operation
ref_7162 = ref_7062 # MOV operation
ref_7166 = ref_7146 # MOV operation
ref_7168 = ((ref_7162 + ref_7166) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7217 = ref_7168 # MOV operation
ref_7221 = ref_7217 # MOV operation
ref_7265 = ref_7221 # MOV operation
ref_7269 = rol(0x3F, ref_7265) # ROL operation
ref_7273 = ref_7269 # MOV operation
ref_7280 = ref_7273 # MOV operation
ref_7329 = ref_7280 # MOV operation
ref_7391 = ref_7329 # MOV operation
ref_7639 = ref_7391 # MOV operation
ref_7865 = ref_7639 # MOV operation
ref_8195 = ref_7865 # MOV operation
ref_8317 = ref_8195 # MOV operation
ref_8355 = ref_8317 # MOV operation
ref_8367 = ref_8355 # MOV operation
ref_8369 = ref_8367 # MOV operation

print ref_8369 & 0xffffffffffffffff
