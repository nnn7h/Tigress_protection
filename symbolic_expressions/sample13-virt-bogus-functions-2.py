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
ref_8217 = ref_239 # MOV operation
ref_8221 = ((0xDEADBEEFDEADBEEF + ref_8217) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8328 = ref_8221 # MOV operation
ref_8330 = (0xE6ADBEEFDEADBEEF ^ ref_8328) # XOR operation
ref_8351 = ref_8221 # MOV operation
ref_8355 = ref_8351 # MOV operation
ref_8399 = ref_8355 # MOV operation
ref_8403 = rol(0xF, ref_8399) # ROL operation
ref_8407 = ref_8403 # MOV operation
ref_8414 = ref_8407 # MOV operation
ref_8430 = ref_8330 # MOV operation
ref_8434 = ref_8414 # MOV operation
ref_8436 = ((ref_8430 + ref_8434) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8462 = ref_8436 # MOV operation
ref_8464 = (0x1234 ^ ref_8462) # XOR operation
ref_8485 = ref_8436 # MOV operation
ref_8489 = ref_8485 # MOV operation
ref_8533 = ref_8489 # MOV operation
ref_8537 = rol(0x34, ref_8533) # ROL operation
ref_8541 = ref_8537 # MOV operation
ref_8548 = ref_8541 # MOV operation
ref_8564 = ref_8464 # MOV operation
ref_8568 = ref_8548 # MOV operation
ref_8570 = ((ref_8564 + ref_8568) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8596 = ref_8570 # MOV operation
ref_8598 = (0x1234 ^ ref_8596) # XOR operation
ref_8619 = ref_8570 # MOV operation
ref_8623 = ref_8619 # MOV operation
ref_8667 = ref_8623 # MOV operation
ref_8671 = rol(0x1A, ref_8667) # ROL operation
ref_8675 = ref_8671 # MOV operation
ref_8682 = ref_8675 # MOV operation
ref_8698 = ref_8598 # MOV operation
ref_8702 = ref_8682 # MOV operation
ref_8704 = ((ref_8698 + ref_8702) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8726 = ref_8414 # MOV operation
ref_8730 = ref_8704 # MOV operation
ref_8732 = (ref_8726 ^ ref_8730) # XOR operation
ref_8753 = ref_8704 # MOV operation
ref_8757 = ref_8753 # MOV operation
ref_8801 = ref_8757 # MOV operation
ref_8805 = rol(0x33, ref_8801) # ROL operation
ref_8809 = ref_8805 # MOV operation
ref_8816 = ref_8809 # MOV operation
ref_8832 = ref_8732 # MOV operation
ref_8836 = ref_8816 # MOV operation
ref_8838 = ((ref_8832 + ref_8836) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8860 = ref_8548 # MOV operation
ref_8864 = ref_8838 # MOV operation
ref_8866 = (ref_8860 ^ ref_8864) # XOR operation
ref_8887 = ref_8838 # MOV operation
ref_8891 = ref_8887 # MOV operation
ref_8935 = ref_8891 # MOV operation
ref_8939 = rol(0x1C, ref_8935) # ROL operation
ref_8943 = ref_8939 # MOV operation
ref_8950 = ref_8943 # MOV operation
ref_8966 = ref_8866 # MOV operation
ref_8970 = ref_8950 # MOV operation
ref_8972 = ((ref_8966 + ref_8970) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8994 = ref_8682 # MOV operation
ref_8998 = ref_8972 # MOV operation
ref_9000 = (ref_8994 ^ ref_8998) # XOR operation
ref_9021 = ref_8972 # MOV operation
ref_9025 = ref_9021 # MOV operation
ref_9069 = ref_9025 # MOV operation
ref_9073 = rol(0x9, ref_9069) # ROL operation
ref_9077 = ref_9073 # MOV operation
ref_9084 = ref_9077 # MOV operation
ref_9100 = ref_9000 # MOV operation
ref_9104 = ref_9084 # MOV operation
ref_9106 = ((ref_9100 + ref_9104) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9128 = ref_8816 # MOV operation
ref_9132 = ref_9106 # MOV operation
ref_9134 = (ref_9128 ^ ref_9132) # XOR operation
ref_9155 = ref_9106 # MOV operation
ref_9159 = ref_9155 # MOV operation
ref_9203 = ref_9159 # MOV operation
ref_9207 = rol(0x2F, ref_9203) # ROL operation
ref_9211 = ref_9207 # MOV operation
ref_9218 = ref_9211 # MOV operation
ref_9234 = ref_9134 # MOV operation
ref_9238 = ref_9218 # MOV operation
ref_9240 = ((ref_9234 + ref_9238) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9262 = ref_8950 # MOV operation
ref_9266 = ref_9240 # MOV operation
ref_9268 = (ref_9262 ^ ref_9266) # XOR operation
ref_9289 = ref_9240 # MOV operation
ref_9293 = ref_9289 # MOV operation
ref_9337 = ref_9293 # MOV operation
ref_9341 = rol(0x36, ref_9337) # ROL operation
ref_9345 = ref_9341 # MOV operation
ref_9352 = ref_9345 # MOV operation
ref_9368 = ref_9268 # MOV operation
ref_9372 = ref_9352 # MOV operation
ref_9374 = ((ref_9368 + ref_9372) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9396 = ref_9084 # MOV operation
ref_9400 = ref_9374 # MOV operation
ref_9402 = (ref_9396 ^ ref_9400) # XOR operation
ref_9423 = ref_9374 # MOV operation
ref_9427 = ref_9423 # MOV operation
ref_9471 = ref_9427 # MOV operation
ref_9475 = rol(0x20, ref_9471) # ROL operation
ref_9479 = ref_9475 # MOV operation
ref_9486 = ref_9479 # MOV operation
ref_9502 = ref_9402 # MOV operation
ref_9506 = ref_9486 # MOV operation
ref_9508 = ((ref_9502 + ref_9506) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9530 = ref_9218 # MOV operation
ref_9534 = ref_9508 # MOV operation
ref_9536 = (ref_9530 ^ ref_9534) # XOR operation
ref_9557 = ref_9508 # MOV operation
ref_9561 = ref_9557 # MOV operation
ref_9605 = ref_9561 # MOV operation
ref_9609 = rol(0x19, ref_9605) # ROL operation
ref_9613 = ref_9609 # MOV operation
ref_9620 = ref_9613 # MOV operation
ref_9636 = ref_9536 # MOV operation
ref_9640 = ref_9620 # MOV operation
ref_9642 = ((ref_9636 + ref_9640) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9691 = ref_9642 # MOV operation
ref_9695 = ref_9691 # MOV operation
ref_9739 = ref_9695 # MOV operation
ref_9743 = rol(0x3F, ref_9739) # ROL operation
ref_9747 = ref_9743 # MOV operation
ref_9754 = ref_9747 # MOV operation
ref_9803 = ref_9754 # MOV operation
ref_9865 = ref_9803 # MOV operation
ref_11777 = ref_9865 # MOV operation
ref_12224 = ref_11777 # MOV operation
ref_13921 = ref_12224 # MOV operation
ref_14578 = ref_13921 # MOV operation
ref_14619 = ref_14578 # MOV operation
ref_14631 = ref_14619 # MOV operation
ref_14633 = ref_14631 # MOV operation

print ref_14633 & 0xffffffffffffffff
