#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_241942 = ref_278 # MOV operation
ref_256738 = ref_241942 # MOV operation
ref_256752 = ((ref_256738 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_390186 = ref_278 # MOV operation
ref_404982 = ref_390186 # MOV operation
ref_404996 = (ref_404982 >> (0x33 & 0x3F)) # SHR operation
ref_419825 = ref_256752 # MOV operation
ref_419829 = ref_404996 # MOV operation
ref_419831 = (ref_419829 | ref_419825) # OR operation
ref_434660 = ref_419831 # MOV operation
ref_671951 = ref_278 # MOV operation
ref_686747 = ref_671951 # MOV operation
ref_686763 = ((((0x0) << 64 | ref_686747) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_716424 = ref_686763 # MOV operation
ref_716430 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_716424)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_731256 = ref_716430 # MOV operation
ref_953796 = ref_434660 # MOV operation
ref_1072454 = ref_731256 # MOV operation
ref_1087258 = ref_953796 # MOV operation
ref_1087262 = ref_1072454 # MOV operation
ref_1087264 = (ref_1087262 | ref_1087258) # OR operation
ref_1205862 = ref_278 # MOV operation
ref_1220658 = ref_1205862 # MOV operation
ref_1220670 = ref_1087264 # MOV operation
ref_1220672 = ((ref_1220670 + ref_1220658) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_1235502 = ref_1220672 # MOV operation
ref_1487714 = ref_434660 # MOV operation
ref_1517354 = ref_1487714 # MOV operation
ref_1517360 = ((ref_1517354 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1517368 = ref_1517360 # MOV operation
ref_1532196 = ref_1517368 # MOV operation
ref_1532198 = ((0x28E5FC28 - ref_1532196) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1532206 = ref_1532198 # MOV operation
ref_1547022 = ref_1532206 # MOV operation
ref_1547036 = (ref_1547022 >> (0x2 & 0x3F)) # SHR operation
ref_1576701 = ref_1547036 # MOV operation
ref_1576707 = (0x7 & ref_1576701) # AND operation
ref_1606372 = ref_1576707 # MOV operation
ref_1606378 = (0x1 | ref_1606372) # OR operation
ref_1725061 = ref_731256 # MOV operation
ref_1843634 = ref_278 # MOV operation
ref_1858430 = ref_1843634 # MOV operation
ref_1858442 = ref_1725061 # MOV operation
ref_1858444 = ((ref_1858442 + ref_1858430) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_1873266 = ref_1858444 # MOV operation
ref_1873278 = ref_1606378 # MOV operation
ref_1873280 = (ref_1873266 >> ((ref_1873278 & 0xFF) & 0x3F)) # SHR operation
ref_1888109 = ref_1873280 # MOV operation
ref_2125485 = ref_1888109 # MOV operation
ref_2140281 = ref_2125485 # MOV operation
ref_2140295 = (ref_2140281 >> (0x1 & 0x3F)) # SHR operation
ref_2169960 = ref_2140295 # MOV operation
ref_2169966 = (0x7 & ref_2169960) # AND operation
ref_2199631 = ref_2169966 # MOV operation
ref_2199637 = (0x1 | ref_2199631) # OR operation
ref_2318320 = ref_1888109 # MOV operation
ref_2333116 = ref_2318320 # MOV operation
ref_2333128 = ref_2199637 # MOV operation
ref_2333130 = (ref_2333116 >> ((ref_2333128 & 0xFF) & 0x3F)) # SHR operation
ref_2347959 = ref_2333130 # MOV operation
ref_2347961 = ((ref_2347959 >> 56) & 0xFF) # Byte reference - MOV operation
ref_2347962 = ((ref_2347959 >> 48) & 0xFF) # Byte reference - MOV operation
ref_2347963 = ((ref_2347959 >> 40) & 0xFF) # Byte reference - MOV operation
ref_2347964 = ((ref_2347959 >> 32) & 0xFF) # Byte reference - MOV operation
ref_2347965 = ((ref_2347959 >> 24) & 0xFF) # Byte reference - MOV operation
ref_2347966 = ((ref_2347959 >> 16) & 0xFF) # Byte reference - MOV operation
ref_2347967 = ((ref_2347959 >> 8) & 0xFF) # Byte reference - MOV operation
ref_2347968 = (ref_2347959 & 0xFF) # Byte reference - MOV operation
ref_2703964 = ref_1235502 # MOV operation
ref_2852266 = ref_434660 # MOV operation
ref_2881906 = ref_2852266 # MOV operation
ref_2881912 = (0x7 & ref_2881906) # AND operation
ref_2896733 = ref_2881912 # MOV operation
ref_2896747 = ((ref_2896733 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_2911576 = ref_2703964 # MOV operation
ref_2911580 = ref_2896747 # MOV operation
ref_2911582 = (ref_2911580 | ref_2911576) # OR operation
ref_2926411 = ref_2911582 # MOV operation
ref_3148863 = ((((ref_2347961) << 8 | ref_2347962) << 8 | ref_2347963) << 8 | ref_2347964) # MOV operation
ref_3163663 = (ref_3148863 & 0xFFFFFFFF) # MOV operation
ref_3564051 = ((((ref_2347965) << 8 | ref_2347966) << 8 | ref_2347967) << 8 | ref_2347968) # MOV operation
ref_3578851 = (ref_3564051 & 0xFFFFFFFF) # MOV operation
ref_3801299 = (ref_3163663 & 0xFFFFFFFF) # MOV operation
ref_3816099 = (ref_3801299 & 0xFFFFFFFF) # MOV operation
ref_4216580 = ref_2926411 # MOV operation
ref_4364882 = ref_2926411 # MOV operation
ref_4394522 = ref_4364882 # MOV operation
ref_4394528 = (0x7 & ref_4394522) # AND operation
ref_4409349 = ref_4394528 # MOV operation
ref_4409363 = ((ref_4409349 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_4424192 = ref_4216580 # MOV operation
ref_4424196 = ref_4409363 # MOV operation
ref_4424198 = (ref_4424196 | ref_4424192) # OR operation
ref_4439027 = ref_4424198 # MOV operation
ref_4661479 = (ref_3578851 & 0xFFFFFFFF) # MOV operation
ref_4676279 = (ref_4661479 & 0xFFFFFFFF) # MOV operation
ref_5076667 = (ref_3816099 & 0xFFFFFFFF) # MOV operation
ref_5091467 = (ref_5076667 & 0xFFFFFFFF) # MOV operation
ref_5091469 = (((ref_5091467 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_5091470 = (((ref_5091467 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_5091471 = (((ref_5091467 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_5091472 = ((ref_5091467 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_5313915 = (ref_4676279 & 0xFFFFFFFF) # MOV operation
ref_5328715 = (ref_5313915 & 0xFFFFFFFF) # MOV operation
ref_5328717 = (((ref_5328715 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_5328718 = (((ref_5328715 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_5328719 = (((ref_5328715 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_5328720 = ((ref_5328715 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_5758721 = ref_4439027 # MOV operation
ref_5877379 = ((((((((ref_5091469) << 8 | ref_5091470) << 8 | ref_5091471) << 8 | ref_5091472) << 8 | ref_5328717) << 8 | ref_5328718) << 8 | ref_5328719) << 8 | ref_5328720) # MOV operation
ref_5907019 = ref_5877379 # MOV operation
ref_5907025 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_5907019)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_5921851 = ref_5758721 # MOV operation
ref_5921855 = ref_5907025 # MOV operation
ref_5921857 = (ref_5921855 ^ ref_5921851) # XOR operation
ref_5951522 = ref_5921857 # MOV operation
ref_5951528 = (0xF & ref_5951522) # AND operation
ref_5981193 = ref_5951528 # MOV operation
ref_5981199 = (0x1 | ref_5981193) # OR operation
ref_6099882 = ref_434660 # MOV operation
ref_6218540 = ref_731256 # MOV operation
ref_6233344 = ref_6099882 # MOV operation
ref_6233348 = ref_6218540 # MOV operation
ref_6233350 = (((sx(0x40, ref_6233348) * sx(0x40, ref_6233344)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6248168 = ref_6233350 # MOV operation
ref_6248180 = ref_5981199 # MOV operation
ref_6248182 = ((ref_6248168 << ((ref_6248180 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_6381701 = ref_4439027 # MOV operation
ref_6500359 = ((((((((ref_5091469) << 8 | ref_5091470) << 8 | ref_5091471) << 8 | ref_5091472) << 8 | ref_5328717) << 8 | ref_5328718) << 8 | ref_5328719) << 8 | ref_5328720) # MOV operation
ref_6529999 = ref_6500359 # MOV operation
ref_6530005 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_6529999)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6544831 = ref_6381701 # MOV operation
ref_6544835 = ref_6530005 # MOV operation
ref_6544837 = (ref_6544835 ^ ref_6544831) # XOR operation
ref_6574502 = ref_6544837 # MOV operation
ref_6574508 = (0xF & ref_6574502) # AND operation
ref_6604173 = ref_6574508 # MOV operation
ref_6604179 = (0x1 | ref_6604173) # OR operation
ref_6619012 = ref_6604179 # MOV operation
ref_6619014 = ((0x40 - ref_6619012) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_6619022 = ref_6619014 # MOV operation
ref_6737700 = ref_434660 # MOV operation
ref_6856358 = ref_731256 # MOV operation
ref_6871162 = ref_6737700 # MOV operation
ref_6871166 = ref_6856358 # MOV operation
ref_6871168 = (((sx(0x40, ref_6871166) * sx(0x40, ref_6871162)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6885986 = ref_6871168 # MOV operation
ref_6885998 = ref_6619022 # MOV operation
ref_6886000 = (ref_6885986 >> ((ref_6885998 & 0xFF) & 0x3F)) # SHR operation
ref_6900829 = ref_6248182 # MOV operation
ref_6900833 = ref_6886000 # MOV operation
ref_6900835 = (ref_6900833 | ref_6900829) # OR operation
ref_6915664 = ref_6900835 # MOV operation
ref_6945315 = ref_6915664 # MOV operation
ref_6945317 = ref_6945315 # MOV operation

print ref_6945317 & 0xffffffffffffffff
