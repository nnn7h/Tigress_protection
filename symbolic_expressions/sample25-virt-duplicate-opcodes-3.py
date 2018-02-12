#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5594 = ref_278 # MOV operation
ref_5670 = ref_5594 # MOV operation
ref_5684 = (ref_5670 >> (0x33 & 0x3F)) # SHR operation
ref_6638 = ref_278 # MOV operation
ref_6714 = ref_6638 # MOV operation
ref_6728 = ((ref_6714 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_6829 = ref_6728 # MOV operation
ref_6841 = ref_5684 # MOV operation
ref_6843 = (ref_6841 | ref_6829) # OR operation
ref_7774 = ref_6843 # MOV operation
ref_8607 = ref_278 # MOV operation
ref_8807 = ref_8607 # MOV operation
ref_8815 = ((((0x0) << 64 | ref_8807) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_9036 = ref_8815 # MOV operation
ref_9042 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_9036)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9970 = ref_9042 # MOV operation
ref_11625 = ref_278 # MOV operation
ref_12523 = ref_9970 # MOV operation
ref_13421 = ref_7774 # MOV operation
ref_13497 = ref_13421 # MOV operation
ref_13509 = ref_12523 # MOV operation
ref_13511 = (ref_13509 | ref_13497) # OR operation
ref_13620 = ref_11625 # MOV operation
ref_13624 = ref_13511 # MOV operation
ref_13626 = ((ref_13624 + ref_13620) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_13736 = ref_13626 # MOV operation
ref_15391 = ref_278 # MOV operation
ref_16289 = ref_9970 # MOV operation
ref_16373 = ref_15391 # MOV operation
ref_16377 = ref_16289 # MOV operation
ref_16379 = ((ref_16377 + ref_16373) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_17767 = ref_7774 # MOV operation
ref_17843 = ref_17767 # MOV operation
ref_17857 = ((ref_17843 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_17865 = ref_17857 # MOV operation
ref_18089 = ref_17865 # MOV operation
ref_18091 = ((0x28E5FC28 - ref_18089) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_18099 = ref_18091 # MOV operation
ref_18195 = ref_18099 # MOV operation
ref_18209 = (ref_18195 >> (0x2 & 0x3F)) # SHR operation
ref_18310 = ref_18209 # MOV operation
ref_18324 = (0x7 & ref_18310) # AND operation
ref_18425 = ref_18324 # MOV operation
ref_18439 = (0x1 | ref_18425) # OR operation
ref_18548 = ref_16379 # MOV operation
ref_18552 = ref_18439 # MOV operation
ref_18554 = (ref_18552 & 0xFFFFFFFF) # MOV operation
ref_18556 = (ref_18548 >> ((ref_18554 & 0xFF) & 0x3F)) # SHR operation
ref_18563 = ref_18556 # MOV operation
ref_18667 = ref_18563 # MOV operation
ref_19585 = ref_18667 # MOV operation
ref_20715 = ref_18667 # MOV operation
ref_20791 = ref_20715 # MOV operation
ref_20805 = (ref_20791 >> (0x1 & 0x3F)) # SHR operation
ref_20906 = ref_20805 # MOV operation
ref_20920 = (0x7 & ref_20906) # AND operation
ref_21145 = ref_20920 # MOV operation
ref_21151 = (0x1 | ref_21145) # OR operation
ref_21260 = ref_19585 # MOV operation
ref_21264 = ref_21151 # MOV operation
ref_21266 = (ref_21264 & 0xFFFFFFFF) # MOV operation
ref_21268 = (ref_21260 >> ((ref_21266 & 0xFF) & 0x3F)) # SHR operation
ref_21275 = ref_21268 # MOV operation
ref_22201 = ref_21275 # MOV operation
ref_22203 = ((ref_22201 >> 56) & 0xFF) # Byte reference - MOV operation
ref_22204 = ((ref_22201 >> 48) & 0xFF) # Byte reference - MOV operation
ref_22205 = ((ref_22201 >> 40) & 0xFF) # Byte reference - MOV operation
ref_22206 = ((ref_22201 >> 32) & 0xFF) # Byte reference - MOV operation
ref_22207 = ((ref_22201 >> 24) & 0xFF) # Byte reference - MOV operation
ref_22208 = ((ref_22201 >> 16) & 0xFF) # Byte reference - MOV operation
ref_22209 = ((ref_22201 >> 8) & 0xFF) # Byte reference - MOV operation
ref_22210 = (ref_22201 & 0xFF) # Byte reference - MOV operation
ref_24104 = ref_13736 # MOV operation
ref_25206 = ref_7774 # MOV operation
ref_25282 = ref_25206 # MOV operation
ref_25296 = (0x7 & ref_25282) # AND operation
ref_25521 = ref_25296 # MOV operation
ref_25529 = ((ref_25521 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_25536 = ref_25529 # MOV operation
ref_25640 = ref_24104 # MOV operation
ref_25644 = ref_25536 # MOV operation
ref_25646 = (ref_25644 | ref_25640) # OR operation
ref_26577 = ref_25646 # MOV operation
ref_28101 = ((((ref_22203) << 8 | ref_22204) << 8 | ref_22205) << 8 | ref_22206) # MOV operation
ref_28309 = (ref_28101 & 0xFFFFFFFF) # MOV operation
ref_29829 = ((((ref_22207) << 8 | ref_22208) << 8 | ref_22209) << 8 | ref_22210) # MOV operation
ref_31337 = (ref_29829 & 0xFFFFFFFF) # MOV operation
ref_31557 = (ref_28309 & 0xFFFFFFFF) # MOV operation
ref_33065 = (ref_31557 & 0xFFFFFFFF) # MOV operation
ref_35284 = ref_26577 # MOV operation
ref_36386 = ref_26577 # MOV operation
ref_36462 = ref_36386 # MOV operation
ref_36476 = (0x7 & ref_36462) # AND operation
ref_36701 = ref_36476 # MOV operation
ref_36709 = ((ref_36701 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_36716 = ref_36709 # MOV operation
ref_36820 = ref_35284 # MOV operation
ref_36824 = ref_36716 # MOV operation
ref_36826 = (ref_36824 | ref_36820) # OR operation
ref_37757 = ref_36826 # MOV operation
ref_39281 = (ref_31337 & 0xFFFFFFFF) # MOV operation
ref_39489 = (ref_39281 & 0xFFFFFFFF) # MOV operation
ref_41009 = (ref_33065 & 0xFFFFFFFF) # MOV operation
ref_42517 = (ref_41009 & 0xFFFFFFFF) # MOV operation
ref_42519 = (((ref_42517 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_42520 = (((ref_42517 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_42521 = (((ref_42517 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_42522 = ((ref_42517 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_42737 = (ref_39489 & 0xFFFFFFFF) # MOV operation
ref_44245 = (ref_42737 & 0xFFFFFFFF) # MOV operation
ref_44247 = (((ref_44245 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_44248 = (((ref_44245 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_44249 = (((ref_44245 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_44250 = ((ref_44245 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_47371 = ref_37757 # MOV operation
ref_48269 = ((((((((ref_42519) << 8 | ref_42520) << 8 | ref_42521) << 8 | ref_42522) << 8 | ref_44247) << 8 | ref_44248) << 8 | ref_44249) << 8 | ref_44250) # MOV operation
ref_48469 = ref_48269 # MOV operation
ref_48475 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_48469)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_48581 = ref_47371 # MOV operation
ref_48585 = ref_48475 # MOV operation
ref_48587 = (ref_48585 ^ ref_48581) # XOR operation
ref_48812 = ref_48587 # MOV operation
ref_48818 = (0xF & ref_48812) # AND operation
ref_49043 = ref_48818 # MOV operation
ref_49049 = (0x1 | ref_49043) # OR operation
ref_49278 = ref_49049 # MOV operation
ref_49280 = ((0x40 - ref_49278) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_49288 = ref_49280 # MOV operation
ref_50206 = ref_7774 # MOV operation
ref_51104 = ref_9970 # MOV operation
ref_51188 = ref_50206 # MOV operation
ref_51192 = ref_51104 # MOV operation
ref_51194 = (((sx(0x40, ref_51192) * sx(0x40, ref_51188)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_51292 = ref_51194 # MOV operation
ref_51304 = ref_49288 # MOV operation
ref_51306 = (ref_51292 >> ((ref_51304 & 0xFF) & 0x3F)) # SHR operation
ref_52229 = ref_7774 # MOV operation
ref_53127 = ref_9970 # MOV operation
ref_53211 = ref_52229 # MOV operation
ref_53215 = ref_53127 # MOV operation
ref_53217 = (((sx(0x40, ref_53215) * sx(0x40, ref_53211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_54253 = ref_37757 # MOV operation
ref_55151 = ((((((((ref_42519) << 8 | ref_42520) << 8 | ref_42521) << 8 | ref_42522) << 8 | ref_44247) << 8 | ref_44248) << 8 | ref_44249) << 8 | ref_44250) # MOV operation
ref_55351 = ref_55151 # MOV operation
ref_55357 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_55351)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_55463 = ref_54253 # MOV operation
ref_55467 = ref_55357 # MOV operation
ref_55469 = (ref_55467 ^ ref_55463) # XOR operation
ref_55694 = ref_55469 # MOV operation
ref_55700 = (0xF & ref_55694) # AND operation
ref_55801 = ref_55700 # MOV operation
ref_55815 = (0x1 | ref_55801) # OR operation
ref_55924 = ref_53217 # MOV operation
ref_55928 = ref_55815 # MOV operation
ref_55930 = (ref_55928 & 0xFFFFFFFF) # MOV operation
ref_55932 = ((ref_55924 << ((ref_55930 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_55939 = ref_55932 # MOV operation
ref_56035 = ref_55939 # MOV operation
ref_56047 = ref_51306 # MOV operation
ref_56049 = (ref_56047 | ref_56035) # OR operation
ref_56158 = ref_56049 # MOV operation
ref_56369 = ref_56158 # MOV operation
ref_56371 = ref_56369 # MOV operation

print ref_56371 & 0xffffffffffffffff
