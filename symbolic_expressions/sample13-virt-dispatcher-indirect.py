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
ref_8849 = ref_239 # MOV operation
ref_8853 = ((0xDEADBEEFDEADBEEF + ref_8849) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8960 = ref_8853 # MOV operation
ref_8962 = (0xE6ADBEEFDEADBEEF ^ ref_8960) # XOR operation
ref_8983 = ref_8853 # MOV operation
ref_8987 = ref_8983 # MOV operation
ref_9031 = ref_8987 # MOV operation
ref_9035 = rol(0xF, ref_9031) # ROL operation
ref_9039 = ref_9035 # MOV operation
ref_9046 = ref_9039 # MOV operation
ref_9062 = ref_8962 # MOV operation
ref_9066 = ref_9046 # MOV operation
ref_9068 = ((ref_9062 + ref_9066) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9094 = ref_9068 # MOV operation
ref_9096 = (0x1234 ^ ref_9094) # XOR operation
ref_9117 = ref_9068 # MOV operation
ref_9121 = ref_9117 # MOV operation
ref_9165 = ref_9121 # MOV operation
ref_9169 = rol(0x34, ref_9165) # ROL operation
ref_9173 = ref_9169 # MOV operation
ref_9180 = ref_9173 # MOV operation
ref_9196 = ref_9096 # MOV operation
ref_9200 = ref_9180 # MOV operation
ref_9202 = ((ref_9196 + ref_9200) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9228 = ref_9202 # MOV operation
ref_9230 = (0x1234 ^ ref_9228) # XOR operation
ref_9251 = ref_9202 # MOV operation
ref_9255 = ref_9251 # MOV operation
ref_9299 = ref_9255 # MOV operation
ref_9303 = rol(0x1A, ref_9299) # ROL operation
ref_9307 = ref_9303 # MOV operation
ref_9314 = ref_9307 # MOV operation
ref_9330 = ref_9230 # MOV operation
ref_9334 = ref_9314 # MOV operation
ref_9336 = ((ref_9330 + ref_9334) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9358 = ref_9046 # MOV operation
ref_9362 = ref_9336 # MOV operation
ref_9364 = (ref_9358 ^ ref_9362) # XOR operation
ref_9385 = ref_9336 # MOV operation
ref_9389 = ref_9385 # MOV operation
ref_9433 = ref_9389 # MOV operation
ref_9437 = rol(0x33, ref_9433) # ROL operation
ref_9441 = ref_9437 # MOV operation
ref_9448 = ref_9441 # MOV operation
ref_9464 = ref_9364 # MOV operation
ref_9468 = ref_9448 # MOV operation
ref_9470 = ((ref_9464 + ref_9468) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9492 = ref_9180 # MOV operation
ref_9496 = ref_9470 # MOV operation
ref_9498 = (ref_9492 ^ ref_9496) # XOR operation
ref_9519 = ref_9470 # MOV operation
ref_9523 = ref_9519 # MOV operation
ref_9567 = ref_9523 # MOV operation
ref_9571 = rol(0x1C, ref_9567) # ROL operation
ref_9575 = ref_9571 # MOV operation
ref_9582 = ref_9575 # MOV operation
ref_9598 = ref_9498 # MOV operation
ref_9602 = ref_9582 # MOV operation
ref_9604 = ((ref_9598 + ref_9602) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9626 = ref_9314 # MOV operation
ref_9630 = ref_9604 # MOV operation
ref_9632 = (ref_9626 ^ ref_9630) # XOR operation
ref_9653 = ref_9604 # MOV operation
ref_9657 = ref_9653 # MOV operation
ref_9701 = ref_9657 # MOV operation
ref_9705 = rol(0x9, ref_9701) # ROL operation
ref_9709 = ref_9705 # MOV operation
ref_9716 = ref_9709 # MOV operation
ref_9732 = ref_9632 # MOV operation
ref_9736 = ref_9716 # MOV operation
ref_9738 = ((ref_9732 + ref_9736) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9760 = ref_9448 # MOV operation
ref_9764 = ref_9738 # MOV operation
ref_9766 = (ref_9760 ^ ref_9764) # XOR operation
ref_9787 = ref_9738 # MOV operation
ref_9791 = ref_9787 # MOV operation
ref_9835 = ref_9791 # MOV operation
ref_9839 = rol(0x2F, ref_9835) # ROL operation
ref_9843 = ref_9839 # MOV operation
ref_9850 = ref_9843 # MOV operation
ref_9866 = ref_9766 # MOV operation
ref_9870 = ref_9850 # MOV operation
ref_9872 = ((ref_9866 + ref_9870) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9894 = ref_9582 # MOV operation
ref_9898 = ref_9872 # MOV operation
ref_9900 = (ref_9894 ^ ref_9898) # XOR operation
ref_9921 = ref_9872 # MOV operation
ref_9925 = ref_9921 # MOV operation
ref_9969 = ref_9925 # MOV operation
ref_9973 = rol(0x36, ref_9969) # ROL operation
ref_9977 = ref_9973 # MOV operation
ref_9984 = ref_9977 # MOV operation
ref_10000 = ref_9900 # MOV operation
ref_10004 = ref_9984 # MOV operation
ref_10006 = ((ref_10000 + ref_10004) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10028 = ref_9716 # MOV operation
ref_10032 = ref_10006 # MOV operation
ref_10034 = (ref_10028 ^ ref_10032) # XOR operation
ref_10055 = ref_10006 # MOV operation
ref_10059 = ref_10055 # MOV operation
ref_10103 = ref_10059 # MOV operation
ref_10107 = rol(0x20, ref_10103) # ROL operation
ref_10111 = ref_10107 # MOV operation
ref_10118 = ref_10111 # MOV operation
ref_10134 = ref_10034 # MOV operation
ref_10138 = ref_10118 # MOV operation
ref_10140 = ((ref_10134 + ref_10138) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10162 = ref_9850 # MOV operation
ref_10166 = ref_10140 # MOV operation
ref_10168 = (ref_10162 ^ ref_10166) # XOR operation
ref_10189 = ref_10140 # MOV operation
ref_10193 = ref_10189 # MOV operation
ref_10237 = ref_10193 # MOV operation
ref_10241 = rol(0x19, ref_10237) # ROL operation
ref_10245 = ref_10241 # MOV operation
ref_10252 = ref_10245 # MOV operation
ref_10268 = ref_10168 # MOV operation
ref_10272 = ref_10252 # MOV operation
ref_10274 = ((ref_10268 + ref_10272) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10323 = ref_10274 # MOV operation
ref_10327 = ref_10323 # MOV operation
ref_10371 = ref_10327 # MOV operation
ref_10375 = rol(0x3F, ref_10371) # ROL operation
ref_10379 = ref_10375 # MOV operation
ref_10386 = ref_10379 # MOV operation
ref_10435 = ref_10386 # MOV operation
ref_10497 = ref_10435 # MOV operation
ref_10788 = ref_10497 # MOV operation
ref_10846 = ref_10788 # MOV operation
ref_11076 = ref_10846 # MOV operation
ref_11122 = ref_11076 # MOV operation
ref_11160 = ref_11122 # MOV operation
ref_11172 = ref_11160 # MOV operation
ref_11174 = ref_11172 # MOV operation

print ref_11174 & 0xffffffffffffffff
