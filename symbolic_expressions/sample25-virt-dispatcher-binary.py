#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_16983 = ref_278 # MOV operation
ref_17326 = ref_16983 # MOV operation
ref_17340 = ((ref_17326 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_23865 = ref_278 # MOV operation
ref_24354 = ref_23865 # MOV operation
ref_24368 = (ref_24354 >> (0x33 & 0x3F)) # SHR operation
ref_25068 = ref_17340 # MOV operation
ref_25072 = ref_24368 # MOV operation
ref_25074 = (ref_25072 | ref_25068) # OR operation
ref_25888 = ref_25074 # MOV operation
ref_37461 = ref_278 # MOV operation
ref_38204 = ref_37461 # MOV operation
ref_38220 = ((((0x0) << 64 | ref_38204) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_39559 = ref_38220 # MOV operation
ref_39565 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_39559)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_40376 = ref_39565 # MOV operation
ref_51099 = ref_25888 # MOV operation
ref_56749 = ref_40376 # MOV operation
ref_57424 = ref_51099 # MOV operation
ref_57428 = ref_56749 # MOV operation
ref_57430 = (ref_57428 | ref_57424) # OR operation
ref_63172 = ref_278 # MOV operation
ref_63877 = ref_63172 # MOV operation
ref_63889 = ref_57430 # MOV operation
ref_63891 = ((ref_63889 + ref_63877) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_64706 = ref_63891 # MOV operation
ref_76995 = ref_25888 # MOV operation
ref_78167 = ref_76995 # MOV operation
ref_78173 = ((ref_78167 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_78181 = ref_78173 # MOV operation
ref_78594 = ref_78181 # MOV operation
ref_78596 = ((0x28E5FC28 - ref_78594) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_78604 = ref_78596 # MOV operation
ref_79113 = ref_78604 # MOV operation
ref_79127 = (ref_79113 >> (0x2 & 0x3F)) # SHR operation
ref_80578 = ref_79127 # MOV operation
ref_80584 = (0x7 & ref_80578) # AND operation
ref_82067 = ref_80584 # MOV operation
ref_82073 = (0x1 | ref_82067) # OR operation
ref_87748 = ref_40376 # MOV operation
ref_93465 = ref_278 # MOV operation
ref_94170 = ref_93465 # MOV operation
ref_94182 = ref_87748 # MOV operation
ref_94184 = ((ref_94182 + ref_94170) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_94699 = ref_94184 # MOV operation
ref_94711 = ref_82073 # MOV operation
ref_94713 = (ref_94699 >> ((ref_94711 & 0xFF) & 0x3F)) # SHR operation
ref_95527 = ref_94713 # MOV operation
ref_107033 = ref_95527 # MOV operation
ref_107522 = ref_107033 # MOV operation
ref_107536 = (ref_107522 >> (0x1 & 0x3F)) # SHR operation
ref_108987 = ref_107536 # MOV operation
ref_108993 = (0x7 & ref_108987) # AND operation
ref_110476 = ref_108993 # MOV operation
ref_110482 = (0x1 | ref_110476) # OR operation
ref_116157 = ref_95527 # MOV operation
ref_116646 = ref_116157 # MOV operation
ref_116658 = ref_110482 # MOV operation
ref_116660 = (ref_116646 >> ((ref_116658 & 0xFF) & 0x3F)) # SHR operation
ref_117474 = ref_116660 # MOV operation
ref_117476 = ((ref_117474 >> 56) & 0xFF) # Byte reference - MOV operation
ref_117477 = ((ref_117474 >> 48) & 0xFF) # Byte reference - MOV operation
ref_117478 = ((ref_117474 >> 40) & 0xFF) # Byte reference - MOV operation
ref_117479 = ((ref_117474 >> 32) & 0xFF) # Byte reference - MOV operation
ref_117480 = ((ref_117474 >> 24) & 0xFF) # Byte reference - MOV operation
ref_117481 = ((ref_117474 >> 16) & 0xFF) # Byte reference - MOV operation
ref_117482 = ((ref_117474 >> 8) & 0xFF) # Byte reference - MOV operation
ref_117483 = (ref_117474 & 0xFF) # Byte reference - MOV operation
ref_134817 = ref_64706 # MOV operation
ref_141821 = ref_25888 # MOV operation
ref_143247 = ref_141821 # MOV operation
ref_143253 = (0x7 & ref_143247) # AND operation
ref_143621 = ref_143253 # MOV operation
ref_143635 = ((ref_143621 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_144335 = ref_134817 # MOV operation
ref_144339 = ref_143635 # MOV operation
ref_144341 = (ref_144339 | ref_144335) # OR operation
ref_145155 = ref_144341 # MOV operation
ref_155104 = ((((ref_117476) << 8 | ref_117477) << 8 | ref_117478) << 8 | ref_117479) # MOV operation
ref_155781 = (ref_155104 & 0xFFFFFFFF) # MOV operation
ref_173506 = ((((ref_117480) << 8 | ref_117481) << 8 | ref_117482) << 8 | ref_117483) # MOV operation
ref_174183 = (ref_173506 & 0xFFFFFFFF) # MOV operation
ref_184128 = (ref_155781 & 0xFFFFFFFF) # MOV operation
ref_184805 = (ref_184128 & 0xFFFFFFFF) # MOV operation
ref_204243 = ref_145155 # MOV operation
ref_211247 = ref_145155 # MOV operation
ref_212673 = ref_211247 # MOV operation
ref_212679 = (0x7 & ref_212673) # AND operation
ref_213047 = ref_212679 # MOV operation
ref_213061 = ((ref_213047 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_213761 = ref_204243 # MOV operation
ref_213765 = ref_213061 # MOV operation
ref_213767 = (ref_213765 | ref_213761) # OR operation
ref_214581 = ref_213767 # MOV operation
ref_224530 = (ref_174183 & 0xFFFFFFFF) # MOV operation
ref_225207 = (ref_224530 & 0xFFFFFFFF) # MOV operation
ref_242932 = (ref_184805 & 0xFFFFFFFF) # MOV operation
ref_243609 = (ref_242932 & 0xFFFFFFFF) # MOV operation
ref_243611 = (((ref_243609 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_243612 = (((ref_243609 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_243613 = (((ref_243609 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_243614 = ((ref_243609 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_253554 = (ref_225207 & 0xFFFFFFFF) # MOV operation
ref_254231 = (ref_253554 & 0xFFFFFFFF) # MOV operation
ref_254233 = (((ref_254231 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_254234 = (((ref_254231 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_254235 = (((ref_254231 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_254236 = ((ref_254231 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_274948 = ref_214581 # MOV operation
ref_280598 = ((((((((ref_243611) << 8 | ref_243612) << 8 | ref_243613) << 8 | ref_243614) << 8 | ref_254233) << 8 | ref_254234) << 8 | ref_254235) << 8 | ref_254236) # MOV operation
ref_281916 = ref_280598 # MOV operation
ref_281922 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_281916)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_282695 = ref_274948 # MOV operation
ref_282699 = ref_281922 # MOV operation
ref_282701 = (ref_282699 ^ ref_282695) # XOR operation
ref_284152 = ref_282701 # MOV operation
ref_284158 = (0xF & ref_284152) # AND operation
ref_285641 = ref_284158 # MOV operation
ref_285647 = (0x1 | ref_285641) # OR operation
ref_291322 = ref_25888 # MOV operation
ref_296972 = ref_40376 # MOV operation
ref_297507 = ref_291322 # MOV operation
ref_297511 = ref_296972 # MOV operation
ref_297513 = (((sx(0x40, ref_297511) * sx(0x40, ref_297507)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_297878 = ref_297513 # MOV operation
ref_297890 = ref_285647 # MOV operation
ref_297892 = ((ref_297878 << ((ref_297890 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_304350 = ref_214581 # MOV operation
ref_310000 = ((((((((ref_243611) << 8 | ref_243612) << 8 | ref_243613) << 8 | ref_243614) << 8 | ref_254233) << 8 | ref_254234) << 8 | ref_254235) << 8 | ref_254236) # MOV operation
ref_311318 = ref_310000 # MOV operation
ref_311324 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_311318)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_312097 = ref_304350 # MOV operation
ref_312101 = ref_311324 # MOV operation
ref_312103 = (ref_312101 ^ ref_312097) # XOR operation
ref_313554 = ref_312103 # MOV operation
ref_313560 = (0xF & ref_313554) # AND operation
ref_315043 = ref_313560 # MOV operation
ref_315049 = (0x1 | ref_315043) # OR operation
ref_315467 = ref_315049 # MOV operation
ref_315469 = ((0x40 - ref_315467) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_315477 = ref_315469 # MOV operation
ref_321147 = ref_25888 # MOV operation
ref_326797 = ref_40376 # MOV operation
ref_327332 = ref_321147 # MOV operation
ref_327336 = ref_326797 # MOV operation
ref_327338 = (((sx(0x40, ref_327336) * sx(0x40, ref_327332)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_327849 = ref_327338 # MOV operation
ref_327861 = ref_315477 # MOV operation
ref_327863 = (ref_327849 >> ((ref_327861 & 0xFF) & 0x3F)) # SHR operation
ref_328563 = ref_297892 # MOV operation
ref_328567 = ref_327863 # MOV operation
ref_328569 = (ref_328567 | ref_328563) # OR operation
ref_329383 = ref_328569 # MOV operation
ref_330490 = ref_329383 # MOV operation
ref_330492 = ref_330490 # MOV operation

print ref_330492 & 0xffffffffffffffff
