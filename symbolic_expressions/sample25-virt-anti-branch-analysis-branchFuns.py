#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_269 = SymVar_0
ref_284 = ref_269 # MOV operation
ref_13254 = ref_284 # MOV operation
ref_13715 = ref_13254 # MOV operation
ref_13729 = (ref_13715 >> (0x33 & 0x3F)) # SHR operation
ref_17720 = ref_284 # MOV operation
ref_18725 = ref_17720 # MOV operation
ref_18733 = ((ref_18725 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18740 = ref_18733 # MOV operation
ref_19208 = ref_18740 # MOV operation
ref_19220 = ref_13729 # MOV operation
ref_19222 = (ref_19220 | ref_19208) # OR operation
ref_23100 = ref_19222 # MOV operation
ref_27533 = ref_284 # MOV operation
ref_28025 = ref_27533 # MOV operation
ref_28041 = ((((0x0) << 64 | ref_28025) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_28955 = ref_28041 # MOV operation
ref_28961 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_28955)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_32836 = ref_28961 # MOV operation
ref_36671 = ref_32836 # MOV operation
ref_40534 = ref_23100 # MOV operation
ref_40990 = ref_40534 # MOV operation
ref_41002 = ref_36671 # MOV operation
ref_41004 = (ref_41002 | ref_40990) # OR operation
ref_44995 = ref_284 # MOV operation
ref_45456 = ref_44995 # MOV operation
ref_45468 = ref_41004 # MOV operation
ref_45470 = ((ref_45468 + ref_45456) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_49336 = ref_45470 # MOV operation
ref_54551 = ref_23100 # MOV operation
ref_55012 = ref_54551 # MOV operation
ref_55026 = ((ref_55012 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_55034 = ref_55026 # MOV operation
ref_55951 = ref_55034 # MOV operation
ref_55953 = ((0x28E5FC28 - ref_55951) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_55961 = ref_55953 # MOV operation
ref_56406 = ref_55961 # MOV operation
ref_56420 = (ref_56406 >> (0x2 & 0x3F)) # SHR operation
ref_57340 = ref_56420 # MOV operation
ref_57346 = (0x7 & ref_57340) # AND operation
ref_57820 = ref_57346 # MOV operation
ref_57834 = (0x1 | ref_57820) # OR operation
ref_61687 = ref_32836 # MOV operation
ref_65688 = ref_284 # MOV operation
ref_66149 = ref_65688 # MOV operation
ref_66161 = ref_61687 # MOV operation
ref_66163 = ((ref_66161 + ref_66149) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_66602 = ref_66163 # MOV operation
ref_66614 = ref_57834 # MOV operation
ref_66616 = (ref_66602 >> ((ref_66614 & 0xFF) & 0x3F)) # SHR operation
ref_70494 = ref_66616 # MOV operation
ref_75249 = ref_70494 # MOV operation
ref_75710 = ref_75249 # MOV operation
ref_75724 = (ref_75710 >> (0x1 & 0x3F)) # SHR operation
ref_76644 = ref_75724 # MOV operation
ref_76650 = (0x7 & ref_76644) # AND operation
ref_77124 = ref_76650 # MOV operation
ref_77138 = (0x1 | ref_77124) # OR operation
ref_80991 = ref_70494 # MOV operation
ref_81452 = ref_80991 # MOV operation
ref_81464 = ref_77138 # MOV operation
ref_81466 = (ref_81452 >> ((ref_81464 & 0xFF) & 0x3F)) # SHR operation
ref_85344 = ref_81466 # MOV operation
ref_85346 = ((ref_85344 >> 56) & 0xFF) # Byte reference - MOV operation
ref_85347 = ((ref_85344 >> 48) & 0xFF) # Byte reference - MOV operation
ref_85348 = ((ref_85344 >> 40) & 0xFF) # Byte reference - MOV operation
ref_85349 = ((ref_85344 >> 32) & 0xFF) # Byte reference - MOV operation
ref_85350 = ((ref_85344 >> 24) & 0xFF) # Byte reference - MOV operation
ref_85351 = ((ref_85344 >> 16) & 0xFF) # Byte reference - MOV operation
ref_85352 = ((ref_85344 >> 8) & 0xFF) # Byte reference - MOV operation
ref_85353 = (ref_85344 & 0xFF) # Byte reference - MOV operation
ref_94165 = ref_23100 # MOV operation
ref_95095 = ref_94165 # MOV operation
ref_95101 = (0x7 & ref_95095) # AND operation
ref_96124 = ref_95101 # MOV operation
ref_96132 = ((ref_96124 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_96139 = ref_96132 # MOV operation
ref_100014 = ref_49336 # MOV operation
ref_100470 = ref_100014 # MOV operation
ref_100482 = ref_96139 # MOV operation
ref_100484 = (ref_100482 | ref_100470) # OR operation
ref_104362 = ref_100484 # MOV operation
ref_110934 = ((((ref_85346) << 8 | ref_85347) << 8 | ref_85348) << 8 | ref_85349) # MOV operation
ref_111874 = (ref_110934 & 0xFFFFFFFF) # MOV operation
ref_118454 = ((((ref_85350) << 8 | ref_85351) << 8 | ref_85352) << 8 | ref_85353) # MOV operation
ref_125040 = (ref_118454 & 0xFFFFFFFF) # MOV operation
ref_125974 = (ref_111874 & 0xFFFFFFFF) # MOV operation
ref_132560 = (ref_125974 & 0xFFFFFFFF) # MOV operation
ref_142810 = ref_104362 # MOV operation
ref_143740 = ref_142810 # MOV operation
ref_143746 = (0x7 & ref_143740) # AND operation
ref_144769 = ref_143746 # MOV operation
ref_144777 = ((ref_144769 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_144784 = ref_144777 # MOV operation
ref_148659 = ref_104362 # MOV operation
ref_149115 = ref_148659 # MOV operation
ref_149127 = ref_144784 # MOV operation
ref_149129 = (ref_149127 | ref_149115) # OR operation
ref_153007 = ref_149129 # MOV operation
ref_159579 = (ref_125040 & 0xFFFFFFFF) # MOV operation
ref_160519 = (ref_159579 & 0xFFFFFFFF) # MOV operation
ref_167099 = (ref_132560 & 0xFFFFFFFF) # MOV operation
ref_173685 = (ref_167099 & 0xFFFFFFFF) # MOV operation
ref_173687 = (((ref_173685 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_173688 = (((ref_173685 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_173689 = (((ref_173685 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_173690 = ((ref_173685 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_174619 = (ref_160519 & 0xFFFFFFFF) # MOV operation
ref_181205 = (ref_174619 & 0xFFFFFFFF) # MOV operation
ref_181207 = (((ref_181205 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_181208 = (((ref_181205 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_181209 = (((ref_181205 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_181210 = ((ref_181205 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_192253 = ref_153007 # MOV operation
ref_196116 = ((((((((ref_173687) << 8 | ref_173688) << 8 | ref_173689) << 8 | ref_173690) << 8 | ref_181207) << 8 | ref_181208) << 8 | ref_181209) << 8 | ref_181210) # MOV operation
ref_197040 = ref_196116 # MOV operation
ref_197046 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_197040)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_197498 = ref_192253 # MOV operation
ref_197502 = ref_197046 # MOV operation
ref_197504 = (ref_197502 ^ ref_197498) # XOR operation
ref_198424 = ref_197504 # MOV operation
ref_198430 = (0xF & ref_198424) # AND operation
ref_198904 = ref_198430 # MOV operation
ref_198918 = (0x1 | ref_198904) # OR operation
ref_199841 = ref_198918 # MOV operation
ref_199843 = ((0x40 - ref_199841) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_199851 = ref_199843 # MOV operation
ref_203698 = ref_23100 # MOV operation
ref_207561 = ref_32836 # MOV operation
ref_208025 = ref_203698 # MOV operation
ref_208029 = ref_207561 # MOV operation
ref_208031 = (((sx(0x40, ref_208029) * sx(0x40, ref_208025)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_208479 = ref_208031 # MOV operation
ref_208491 = ref_199851 # MOV operation
ref_208493 = (ref_208479 >> ((ref_208491 & 0xFF) & 0x3F)) # SHR operation
ref_212346 = ref_23100 # MOV operation
ref_216209 = ref_32836 # MOV operation
ref_216673 = ref_212346 # MOV operation
ref_216677 = ref_216209 # MOV operation
ref_216679 = (((sx(0x40, ref_216677) * sx(0x40, ref_216673)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_220989 = ref_153007 # MOV operation
ref_224852 = ((((((((ref_173687) << 8 | ref_173688) << 8 | ref_173689) << 8 | ref_173690) << 8 | ref_181207) << 8 | ref_181208) << 8 | ref_181209) << 8 | ref_181210) # MOV operation
ref_225776 = ref_224852 # MOV operation
ref_225782 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_225776)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_226234 = ref_220989 # MOV operation
ref_226238 = ref_225782 # MOV operation
ref_226240 = (ref_226238 ^ ref_226234) # XOR operation
ref_227160 = ref_226240 # MOV operation
ref_227166 = (0xF & ref_227160) # AND operation
ref_227640 = ref_227166 # MOV operation
ref_227654 = (0x1 | ref_227640) # OR operation
ref_228189 = ref_216679 # MOV operation
ref_228193 = ref_227654 # MOV operation
ref_228195 = (ref_228193 & 0xFFFFFFFF) # MOV operation
ref_228197 = ((ref_228189 << ((ref_228195 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_228204 = ref_228197 # MOV operation
ref_228672 = ref_228204 # MOV operation
ref_228684 = ref_208493 # MOV operation
ref_228686 = (ref_228684 | ref_228672) # OR operation
ref_232718 = ref_228686 # MOV operation
ref_233611 = ref_232718 # MOV operation
ref_233613 = ref_233611 # MOV operation

print ref_233613 & 0xffffffffffffffff
