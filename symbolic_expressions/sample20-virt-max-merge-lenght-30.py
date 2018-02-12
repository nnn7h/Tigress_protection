#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5406 = ref_278 # MOV operation
ref_5448 = ref_5406 # MOV operation
ref_5454 = (0x1F02C962 | ref_5448) # OR operation
ref_5501 = ref_5454 # MOV operation
ref_5507 = (0x1F8797B2 & ref_5501) # AND operation
ref_5546 = ref_5507 # MOV operation
ref_6201 = ref_278 # MOV operation
ref_6431 = ref_5546 # MOV operation
ref_6457 = ref_6201 # MOV operation
ref_6461 = ref_6431 # MOV operation
ref_6463 = (ref_6461 & ref_6457) # AND operation
ref_6502 = ref_6463 # MOV operation
ref_7157 = ref_278 # MOV operation
ref_7199 = ref_7157 # MOV operation
ref_7205 = (((sx(0x40, 0x66AF1DF) * sx(0x40, ref_7199)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7497 = ref_6502 # MOV operation
ref_7521 = ref_7497 # MOV operation
ref_7529 = (ref_7521 >> (0x7 & 0x3F)) # SHR operation
ref_7536 = ref_7529 # MOV operation
ref_7828 = ref_6502 # MOV operation
ref_7860 = ref_7828 # MOV operation
ref_7874 = ((ref_7860 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7895 = ref_7536 # MOV operation
ref_7907 = ref_7874 # MOV operation
ref_7909 = (ref_7907 | ref_7895) # OR operation
ref_7940 = ref_7205 # MOV operation
ref_7944 = ref_7909 # MOV operation
ref_7946 = ((ref_7944 + ref_7940) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7986 = ref_7946 # MOV operation
ref_11449 = ref_7986 # MOV operation
ref_11847 = ref_7986 # MOV operation
ref_11879 = ref_11449 # MOV operation
ref_11891 = ref_11847 # MOV operation
ref_11893 = ((ref_11891 + ref_11879) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_12031 = ref_11893 # MOV operation
ref_12675 = ref_7986 # MOV operation
ref_13113 = ref_6502 # MOV operation
ref_13155 = ref_13113 # MOV operation
ref_13161 = (0x7 & ref_13155) # AND operation
ref_13198 = ref_13161 # MOV operation
ref_13212 = ((ref_13198 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13249 = ref_12675 # MOV operation
ref_13261 = ref_13212 # MOV operation
ref_13263 = (ref_13261 | ref_13249) # OR operation
ref_13302 = ref_13263 # MOV operation
ref_13304 = ((ref_13302 >> 56) & 0xFF) # Byte reference - MOV operation
ref_13305 = ((ref_13302 >> 48) & 0xFF) # Byte reference - MOV operation
ref_13306 = ((ref_13302 >> 40) & 0xFF) # Byte reference - MOV operation
ref_13307 = ((ref_13302 >> 32) & 0xFF) # Byte reference - MOV operation
ref_13308 = ((ref_13302 >> 24) & 0xFF) # Byte reference - MOV operation
ref_13309 = ((ref_13302 >> 16) & 0xFF) # Byte reference - MOV operation
ref_13310 = ((ref_13302 >> 8) & 0xFF) # Byte reference - MOV operation
ref_13311 = (ref_13302 & 0xFF) # Byte reference - MOV operation
ref_13898 = ref_13304 # MOVZX operation
ref_13924 = (ref_13898 & 0xFF) # MOVZX operation
ref_15134 = ref_13311 # MOVZX operation
ref_15152 = (ref_15134 & 0xFF) # MOVZX operation
ref_15154 = (ref_15152 & 0xFF) # Byte reference - MOV operation
ref_15872 = (ref_13924 & 0xFF) # MOVZX operation
ref_15898 = (ref_15872 & 0xFF) # MOVZX operation
ref_15900 = (ref_15898 & 0xFF) # Byte reference - MOV operation
ref_16516 = ref_5546 # MOV operation
ref_16932 = ((((((((ref_15154) << 8 | ref_13305) << 8 | ref_13306) << 8 | ref_13307) << 8 | ref_13308) << 8 | ref_13309) << 8 | ref_13310) << 8 | ref_15900) # MOV operation
ref_17260 = ref_6502 # MOV operation
ref_17292 = ref_16932 # MOV operation
ref_17304 = ref_17260 # MOV operation
ref_17306 = (ref_17304 & ref_17292) # AND operation
ref_17451 = ref_17306 # MOV operation
ref_17465 = (0x1F & ref_17451) # AND operation
ref_17488 = ref_17465 # MOV operation
ref_17502 = ((ref_17488 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_17539 = ref_16516 # MOV operation
ref_17551 = ref_17502 # MOV operation
ref_17553 = (ref_17551 | ref_17539) # OR operation
ref_17592 = ref_17553 # MOV operation
ref_18910 = ref_12031 # MOV operation
ref_19308 = ref_12031 # MOV operation
ref_19340 = ref_18910 # MOV operation
ref_19352 = ref_19308 # MOV operation
ref_19354 = ((ref_19352 + ref_19340) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_19492 = ref_19354 # MOV operation
ref_20136 = ref_19492 # MOV operation
ref_20574 = ((((((((ref_15154) << 8 | ref_13305) << 8 | ref_13306) << 8 | ref_13307) << 8 | ref_13308) << 8 | ref_13309) << 8 | ref_13310) << 8 | ref_15900) # MOV operation
ref_20616 = ref_20574 # MOV operation
ref_20622 = (0x7 & ref_20616) # AND operation
ref_20659 = ref_20622 # MOV operation
ref_20673 = ((ref_20659 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_20710 = ref_20136 # MOV operation
ref_20722 = ref_20673 # MOV operation
ref_20724 = (ref_20722 | ref_20710) # OR operation
ref_20763 = ref_20724 # MOV operation
ref_20765 = ((ref_20763 >> 56) & 0xFF) # Byte reference - MOV operation
ref_20766 = ((ref_20763 >> 48) & 0xFF) # Byte reference - MOV operation
ref_20767 = ((ref_20763 >> 40) & 0xFF) # Byte reference - MOV operation
ref_20768 = ((ref_20763 >> 32) & 0xFF) # Byte reference - MOV operation
ref_20769 = ((ref_20763 >> 24) & 0xFF) # Byte reference - MOV operation
ref_20770 = ((ref_20763 >> 16) & 0xFF) # Byte reference - MOV operation
ref_20771 = ((ref_20763 >> 8) & 0xFF) # Byte reference - MOV operation
ref_20772 = (ref_20763 & 0xFF) # Byte reference - MOV operation
ref_21359 = ref_20765 # MOVZX operation
ref_21385 = (ref_21359 & 0xFF) # MOVZX operation
ref_22595 = ref_20772 # MOVZX operation
ref_22613 = (ref_22595 & 0xFF) # MOVZX operation
ref_22615 = (ref_22613 & 0xFF) # Byte reference - MOV operation
ref_23333 = (ref_21385 & 0xFF) # MOVZX operation
ref_23359 = (ref_23333 & 0xFF) # MOVZX operation
ref_23361 = (ref_23359 & 0xFF) # Byte reference - MOV operation
ref_23977 = ref_17592 # MOV operation
ref_24393 = ((((((((ref_22615) << 8 | ref_20766) << 8 | ref_20767) << 8 | ref_20768) << 8 | ref_20769) << 8 | ref_20770) << 8 | ref_20771) << 8 | ref_23361) # MOV operation
ref_24721 = ((((((((ref_15154) << 8 | ref_13305) << 8 | ref_13306) << 8 | ref_13307) << 8 | ref_13308) << 8 | ref_13309) << 8 | ref_13310) << 8 | ref_15900) # MOV operation
ref_24753 = ref_24393 # MOV operation
ref_24765 = ref_24721 # MOV operation
ref_24767 = (ref_24765 & ref_24753) # AND operation
ref_24912 = ref_24767 # MOV operation
ref_24926 = (0x1F & ref_24912) # AND operation
ref_24949 = ref_24926 # MOV operation
ref_24963 = ((ref_24949 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_25000 = ref_23977 # MOV operation
ref_25012 = ref_24963 # MOV operation
ref_25014 = (ref_25012 | ref_25000) # OR operation
ref_25053 = ref_25014 # MOV operation
ref_26537 = ((((((((ref_15154) << 8 | ref_13305) << 8 | ref_13306) << 8 | ref_13307) << 8 | ref_13308) << 8 | ref_13309) << 8 | ref_13310) << 8 | ref_15900) # MOV operation
ref_26811 = ((((((((ref_22615) << 8 | ref_20766) << 8 | ref_20767) << 8 | ref_20768) << 8 | ref_20769) << 8 | ref_20770) << 8 | ref_20771) << 8 | ref_23361) # MOV operation
ref_26827 = ref_26537 # MOV operation
ref_26839 = ref_26811 # MOV operation
ref_26841 = (ref_26839 | ref_26827) # OR operation
ref_26880 = ref_26841 # MOV operation
ref_26894 = (0xF & ref_26880) # AND operation
ref_26933 = ref_26894 # MOV operation
ref_26947 = (0x1 | ref_26933) # OR operation
ref_27350 = ref_6502 # MOV operation
ref_27374 = ref_27350 # MOV operation
ref_27382 = (ref_27374 >> (0x1 & 0x3F)) # SHR operation
ref_27389 = ref_27382 # MOV operation
ref_27423 = ref_27389 # MOV operation
ref_27437 = (0xF & ref_27423) # AND operation
ref_27476 = ref_27437 # MOV operation
ref_27490 = (0x1 | ref_27476) # OR operation
ref_27769 = ref_25053 # MOV operation
ref_27793 = ref_27769 # MOV operation
ref_27797 = ref_27490 # MOV operation
ref_27799 = (ref_27797 & 0xFFFFFFFF) # MOV operation
ref_27801 = (ref_27793 >> ((ref_27799 & 0xFF) & 0x3F)) # SHR operation
ref_27808 = ref_27801 # MOV operation
ref_28206 = ref_6502 # MOV operation
ref_28230 = ref_28206 # MOV operation
ref_28238 = (ref_28230 >> (0x1 & 0x3F)) # SHR operation
ref_28245 = ref_28238 # MOV operation
ref_28279 = ref_28245 # MOV operation
ref_28293 = (0xF & ref_28279) # AND operation
ref_28332 = ref_28293 # MOV operation
ref_28346 = (0x1 | ref_28332) # OR operation
ref_28397 = ref_28346 # MOV operation
ref_28399 = ((0x40 - ref_28397) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_28407 = ref_28399 # MOV operation
ref_28681 = ref_25053 # MOV operation
ref_28705 = ref_28681 # MOV operation
ref_28709 = ref_28407 # MOV operation
ref_28711 = (ref_28709 & 0xFFFFFFFF) # MOV operation
ref_28713 = ((ref_28705 << ((ref_28711 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_28720 = ref_28713 # MOV operation
ref_28746 = ref_27808 # MOV operation
ref_28750 = ref_28720 # MOV operation
ref_28752 = (ref_28750 | ref_28746) # OR operation
ref_28789 = ref_28752 # MOV operation
ref_28801 = ref_26947 # MOV operation
ref_28803 = ((ref_28789 << ((ref_28801 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_29188 = ((((((((ref_15154) << 8 | ref_13305) << 8 | ref_13306) << 8 | ref_13307) << 8 | ref_13308) << 8 | ref_13309) << 8 | ref_13310) << 8 | ref_15900) # MOV operation
ref_29462 = ((((((((ref_22615) << 8 | ref_20766) << 8 | ref_20767) << 8 | ref_20768) << 8 | ref_20769) << 8 | ref_20770) << 8 | ref_20771) << 8 | ref_23361) # MOV operation
ref_29494 = ref_29188 # MOV operation
ref_29506 = ref_29462 # MOV operation
ref_29508 = (ref_29506 | ref_29494) # OR operation
ref_29563 = ref_29508 # MOV operation
ref_29577 = (0xF & ref_29563) # AND operation
ref_29632 = ref_29577 # MOV operation
ref_29646 = (0x1 | ref_29632) # OR operation
ref_29713 = ref_29646 # MOV operation
ref_29715 = ((0x40 - ref_29713) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_29723 = ref_29715 # MOV operation
ref_30227 = ref_6502 # MOV operation
ref_30251 = ref_30227 # MOV operation
ref_30259 = (ref_30251 >> (0x1 & 0x3F)) # SHR operation
ref_30266 = ref_30259 # MOV operation
ref_30300 = ref_30266 # MOV operation
ref_30314 = (0xF & ref_30300) # AND operation
ref_30353 = ref_30314 # MOV operation
ref_30367 = (0x1 | ref_30353) # OR operation
ref_30646 = ref_25053 # MOV operation
ref_30670 = ref_30646 # MOV operation
ref_30674 = ref_30367 # MOV operation
ref_30676 = (ref_30674 & 0xFFFFFFFF) # MOV operation
ref_30678 = (ref_30670 >> ((ref_30676 & 0xFF) & 0x3F)) # SHR operation
ref_30685 = ref_30678 # MOV operation
ref_31083 = ref_6502 # MOV operation
ref_31107 = ref_31083 # MOV operation
ref_31115 = (ref_31107 >> (0x1 & 0x3F)) # SHR operation
ref_31122 = ref_31115 # MOV operation
ref_31156 = ref_31122 # MOV operation
ref_31170 = (0xF & ref_31156) # AND operation
ref_31209 = ref_31170 # MOV operation
ref_31223 = (0x1 | ref_31209) # OR operation
ref_31274 = ref_31223 # MOV operation
ref_31276 = ((0x40 - ref_31274) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_31284 = ref_31276 # MOV operation
ref_31558 = ref_25053 # MOV operation
ref_31582 = ref_31558 # MOV operation
ref_31586 = ref_31284 # MOV operation
ref_31588 = (ref_31586 & 0xFFFFFFFF) # MOV operation
ref_31590 = ((ref_31582 << ((ref_31588 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_31597 = ref_31590 # MOV operation
ref_31623 = ref_30685 # MOV operation
ref_31627 = ref_31597 # MOV operation
ref_31629 = (ref_31627 | ref_31623) # OR operation
ref_31758 = ref_31629 # MOV operation
ref_31770 = ref_29723 # MOV operation
ref_31772 = (ref_31758 >> ((ref_31770 & 0xFF) & 0x3F)) # SHR operation
ref_31889 = ref_28803 # MOV operation
ref_31893 = ref_31772 # MOV operation
ref_31895 = (ref_31893 | ref_31889) # OR operation
ref_32012 = ref_31895 # MOV operation
ref_32239 = ref_32012 # MOV operation
ref_32241 = ref_32239 # MOV operation

print ref_32241 & 0xffffffffffffffff
