#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_13675 = ref_278 # MOV operation
ref_14165 = ref_13675 # MOV operation
ref_14181 = (0x1D2C27F0 | ref_14165) # OR operation
ref_14662 = ref_14181 # MOV operation
ref_14680 = (ref_14662 >> (0x37 & 0x3F)) # SHR operation
ref_14687 = ref_14680 # MOV operation
ref_19428 = ref_278 # MOV operation
ref_19917 = ref_19428 # MOV operation
ref_19933 = (0x1D2C27F0 | ref_19917) # OR operation
ref_21045 = ref_19933 # MOV operation
ref_21055 = ((ref_21045 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_21062 = ref_21055 # MOV operation
ref_21574 = ref_21062 # MOV operation
ref_21588 = ref_14687 # MOV operation
ref_21590 = (ref_21588 | ref_21574) # OR operation
ref_22085 = ref_21590 # MOV operation
ref_30768 = ref_22085 # MOV operation
ref_31310 = ref_30768 # MOV operation
ref_31328 = (ref_31310 >> (0x33 & 0x3F)) # SHR operation
ref_31335 = ref_31328 # MOV operation
ref_35607 = ref_22085 # MOV operation
ref_36679 = ref_35607 # MOV operation
ref_36689 = ((ref_36679 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_36696 = ref_36689 # MOV operation
ref_37239 = ref_36696 # MOV operation
ref_37253 = ref_31335 # MOV operation
ref_37255 = (ref_37253 | ref_37239) # OR operation
ref_41549 = ref_278 # MOV operation
ref_42024 = ref_41549 # MOV operation
ref_42038 = ref_37255 # MOV operation
ref_42040 = (ref_42038 | ref_42024) # OR operation
ref_42597 = ref_42040 # MOV operation
ref_50597 = ref_278 # MOV operation
ref_51665 = ref_50597 # MOV operation
ref_51673 = ((0x6402BE2 + ref_51665) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_52247 = ref_51673 # MOV operation
ref_60300 = ref_42597 # MOV operation
ref_64655 = ref_52247 # MOV operation
ref_65181 = ref_64655 # MOV operation
ref_65195 = ref_60300 # MOV operation
ref_65197 = (((sx(0x40, ref_65195) * sx(0x40, ref_65181)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_66293 = ref_65197 # MOV operation
ref_66295 = (((sx(0x40, ref_66293) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_71105 = ref_278 # MOV operation
ref_71647 = ref_71105 # MOV operation
ref_71663 = (0x3544223F | ref_71647) # OR operation
ref_72146 = ref_71663 # MOV operation
ref_72160 = ref_66295 # MOV operation
ref_72162 = (((sx(0x40, ref_72160) * sx(0x40, ref_72146)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_72679 = ref_72162 # MOV operation
ref_81352 = ref_72679 # MOV operation
ref_81812 = ref_81352 # MOV operation
ref_81828 = (0x1F & ref_81812) # AND operation
ref_82974 = ref_81828 # MOV operation
ref_82984 = ((ref_82974 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_82991 = ref_82984 # MOV operation
ref_87257 = ref_52247 # MOV operation
ref_87723 = ref_87257 # MOV operation
ref_87737 = ref_82991 # MOV operation
ref_87739 = (ref_87737 | ref_87723) # OR operation
ref_88279 = ref_87739 # MOV operation
ref_95348 = ref_42597 # MOV operation
ref_95864 = ref_95348 # MOV operation
ref_95882 = (ref_95864 >> (0x1 & 0x3F)) # SHR operation
ref_95889 = ref_95882 # MOV operation
ref_96438 = ref_95889 # MOV operation
ref_96454 = (0xF & ref_96438) # AND operation
ref_96966 = ref_96454 # MOV operation
ref_96982 = (0x1 | ref_96966) # OR operation
ref_97561 = ref_96982 # MOV operation
ref_97563 = ((0x40 - ref_97561) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_97571 = ref_97563 # MOV operation
ref_101820 = ref_22085 # MOV operation
ref_102346 = ref_101820 # MOV operation
ref_102360 = ref_97571 # MOV operation
ref_102362 = (ref_102360 & 0xFFFFFFFF) # MOV operation
ref_102364 = (ref_102346 >> ((ref_102362 & 0xFF) & 0x3F)) # SHR operation
ref_102371 = ref_102364 # MOV operation
ref_106673 = ref_22085 # MOV operation
ref_112594 = ref_42597 # MOV operation
ref_113100 = ref_112594 # MOV operation
ref_113118 = (ref_113100 >> (0x1 & 0x3F)) # SHR operation
ref_113125 = ref_113118 # MOV operation
ref_113661 = ref_113125 # MOV operation
ref_113677 = (0xF & ref_113661) # AND operation
ref_114199 = ref_113677 # MOV operation
ref_114215 = (0x1 | ref_114199) # OR operation
ref_114733 = ref_106673 # MOV operation
ref_114739 = ref_114215 # MOV operation
ref_114741 = (ref_114739 & 0xFFFFFFFF) # MOV operation
ref_114743 = ((ref_114733 << ((ref_114741 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_114750 = ref_114743 # MOV operation
ref_115294 = ref_114750 # MOV operation
ref_115308 = ref_102371 # MOV operation
ref_115310 = (ref_115308 | ref_115294) # OR operation
ref_121302 = ref_72679 # MOV operation
ref_121802 = ref_121302 # MOV operation
ref_121820 = (ref_121802 >> (0x3 & 0x3F)) # SHR operation
ref_121827 = ref_121820 # MOV operation
ref_122370 = ref_121827 # MOV operation
ref_122386 = (0x7 & ref_122370) # AND operation
ref_122883 = ref_122386 # MOV operation
ref_122899 = (0x1 | ref_122883) # OR operation
ref_127290 = ref_88279 # MOV operation
ref_127786 = ref_127290 # MOV operation
ref_127800 = ref_122899 # MOV operation
ref_127802 = (ref_127800 & 0xFFFFFFFF) # MOV operation
ref_127804 = (ref_127786 >> ((ref_127802 & 0xFF) & 0x3F)) # SHR operation
ref_127811 = ref_127804 # MOV operation
ref_128333 = ref_115310 # MOV operation
ref_128339 = ref_127811 # MOV operation
ref_128341 = ((ref_128333 - ref_128339) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_128343 = ((((ref_128333 ^ (ref_128339 ^ ref_128341)) ^ ((ref_128333 ^ ref_128341) & (ref_128333 ^ ref_128339))) >> 63) & 0x1) # Carry flag
ref_128347 = (0x1 if (ref_128341 == 0x0) else 0x0) # Zero flag
ref_128349 = ((((ref_128339 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if ((ref_128343 | ref_128347) == 0x1) else 0x0)) # SETBE operation
ref_128351 = (ref_128349 & 0xFF) # MOVZX operation
ref_128839 = (ref_128351 & 0xFFFFFFFF) # MOV operation
ref_128841 = ((ref_128839 & 0xFFFFFFFF) & (ref_128839 & 0xFFFFFFFF)) # TEST operation
ref_128846 = (0x1 if (ref_128841 == 0x0) else 0x0) # Zero flag
ref_128848 = (0x2816 if (ref_128846 == 0x1) else 0x27EC) # Program Counter


if (ref_128846 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_13675 = ref_278 # MOV operation
    ref_14165 = ref_13675 # MOV operation
    ref_14181 = (0x1D2C27F0 | ref_14165) # OR operation
    ref_14662 = ref_14181 # MOV operation
    ref_14680 = (ref_14662 >> (0x37 & 0x3F)) # SHR operation
    ref_14687 = ref_14680 # MOV operation
    ref_19428 = ref_278 # MOV operation
    ref_19917 = ref_19428 # MOV operation
    ref_19933 = (0x1D2C27F0 | ref_19917) # OR operation
    ref_21045 = ref_19933 # MOV operation
    ref_21055 = ((ref_21045 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_21062 = ref_21055 # MOV operation
    ref_21574 = ref_21062 # MOV operation
    ref_21588 = ref_14687 # MOV operation
    ref_21590 = (ref_21588 | ref_21574) # OR operation
    ref_22085 = ref_21590 # MOV operation
    ref_30768 = ref_22085 # MOV operation
    ref_31310 = ref_30768 # MOV operation
    ref_31328 = (ref_31310 >> (0x33 & 0x3F)) # SHR operation
    ref_31335 = ref_31328 # MOV operation
    ref_35607 = ref_22085 # MOV operation
    ref_36679 = ref_35607 # MOV operation
    ref_36689 = ((ref_36679 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_36696 = ref_36689 # MOV operation
    ref_37239 = ref_36696 # MOV operation
    ref_37253 = ref_31335 # MOV operation
    ref_37255 = (ref_37253 | ref_37239) # OR operation
    ref_41549 = ref_278 # MOV operation
    ref_42024 = ref_41549 # MOV operation
    ref_42038 = ref_37255 # MOV operation
    ref_42040 = (ref_42038 | ref_42024) # OR operation
    ref_42597 = ref_42040 # MOV operation
    ref_50597 = ref_278 # MOV operation
    ref_51665 = ref_50597 # MOV operation
    ref_51673 = ((0x6402BE2 + ref_51665) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_52247 = ref_51673 # MOV operation
    ref_60300 = ref_42597 # MOV operation
    ref_64655 = ref_52247 # MOV operation
    ref_65181 = ref_64655 # MOV operation
    ref_65195 = ref_60300 # MOV operation
    ref_65197 = (((sx(0x40, ref_65195) * sx(0x40, ref_65181)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_66293 = ref_65197 # MOV operation
    ref_66295 = (((sx(0x40, ref_66293) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_71105 = ref_278 # MOV operation
    ref_71647 = ref_71105 # MOV operation
    ref_71663 = (0x3544223F | ref_71647) # OR operation
    ref_72146 = ref_71663 # MOV operation
    ref_72160 = ref_66295 # MOV operation
    ref_72162 = (((sx(0x40, ref_72160) * sx(0x40, ref_72146)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_72679 = ref_72162 # MOV operation
    ref_81352 = ref_72679 # MOV operation
    ref_81812 = ref_81352 # MOV operation
    ref_81828 = (0x1F & ref_81812) # AND operation
    ref_82974 = ref_81828 # MOV operation
    ref_82984 = ((ref_82974 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_82991 = ref_82984 # MOV operation
    ref_87257 = ref_52247 # MOV operation
    ref_87723 = ref_87257 # MOV operation
    ref_87737 = ref_82991 # MOV operation
    ref_87739 = (ref_87737 | ref_87723) # OR operation
    ref_88279 = ref_87739 # MOV operation
    ref_137991 = ref_42597 # MOV operation
    ref_138588 = ref_137991 # MOV operation
    ref_138604 = (0xF & ref_138588) # AND operation
    ref_139647 = ref_138604 # MOV operation
    ref_139657 = ((ref_139647 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_139664 = ref_139657 # MOV operation
    ref_143898 = ref_42597 # MOV operation
    ref_144368 = ref_143898 # MOV operation
    ref_144382 = ref_139664 # MOV operation
    ref_144384 = (ref_144382 | ref_144368) # OR operation
    ref_144925 = ref_144384 # MOV operation
    ref_153498 = ref_72679 # MOV operation
    ref_154542 = ref_153498 # MOV operation
    ref_154550 = ((0x369A4780 + ref_154542) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_158840 = ref_88279 # MOV operation
    ref_159353 = ref_158840 # MOV operation
    ref_159367 = ref_154550 # MOV operation
    ref_159369 = (((sx(0x40, ref_159367) * sx(0x40, ref_159353)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_165845 = ref_144925 # MOV operation
    ref_166402 = ref_165845 # MOV operation
    ref_166420 = (ref_166402 >> (0x3 & 0x3F)) # SHR operation
    ref_166427 = ref_166420 # MOV operation
    ref_166903 = ref_166427 # MOV operation
    ref_166919 = (0xF & ref_166903) # AND operation
    ref_167464 = ref_166919 # MOV operation
    ref_167480 = (0x1 | ref_167464) # OR operation
    ref_167983 = ref_167480 # MOV operation
    ref_167985 = ((0x40 - ref_167983) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_167993 = ref_167985 # MOV operation
    ref_172295 = ref_22085 # MOV operation
    ref_172773 = ref_172295 # MOV operation
    ref_172787 = ref_167993 # MOV operation
    ref_172789 = (ref_172787 & 0xFFFFFFFF) # MOV operation
    ref_172791 = (ref_172773 >> ((ref_172789 & 0xFF) & 0x3F)) # SHR operation
    ref_172798 = ref_172791 # MOV operation
    ref_177134 = ref_22085 # MOV operation
    ref_183047 = ref_144925 # MOV operation
    ref_183533 = ref_183047 # MOV operation
    ref_183551 = (ref_183533 >> (0x3 & 0x3F)) # SHR operation
    ref_183558 = ref_183551 # MOV operation
    ref_184068 = ref_183558 # MOV operation
    ref_184084 = (0xF & ref_184068) # AND operation
    ref_184595 = ref_184084 # MOV operation
    ref_184611 = (0x1 | ref_184595) # OR operation
    ref_185176 = ref_177134 # MOV operation
    ref_185182 = ref_184611 # MOV operation
    ref_185184 = (ref_185182 & 0xFFFFFFFF) # MOV operation
    ref_185186 = ((ref_185176 << ((ref_185184 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_185193 = ref_185186 # MOV operation
    ref_185671 = ref_185193 # MOV operation
    ref_185685 = ref_172798 # MOV operation
    ref_185687 = (ref_185685 | ref_185671) # OR operation
    ref_186190 = ref_185687 # MOV operation
    ref_186204 = ref_159369 # MOV operation
    ref_186206 = (((sx(0x40, ref_186204) * sx(0x40, ref_186190)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_186748 = ref_186206 # MOV operation
    ref_187825 = ref_186748 # MOV operation
    ref_187827 = ref_187825 # MOV operation
    endb = ref_187827


else:
    ref_188147 = SymVar_0
    ref_188162 = ref_188147 # MOV operation
    ref_201193 = ref_188162 # MOV operation
    ref_201706 = ref_201193 # MOV operation
    ref_201722 = (0x1D2C27F0 | ref_201706) # OR operation
    ref_202234 = ref_201722 # MOV operation
    ref_202252 = (ref_202234 >> (0x37 & 0x3F)) # SHR operation
    ref_202259 = ref_202252 # MOV operation
    ref_207035 = ref_188162 # MOV operation
    ref_207563 = ref_207035 # MOV operation
    ref_207579 = (0x1D2C27F0 | ref_207563) # OR operation
    ref_208725 = ref_207579 # MOV operation
    ref_208735 = ((ref_208725 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_208742 = ref_208735 # MOV operation
    ref_209208 = ref_208742 # MOV operation
    ref_209222 = ref_202259 # MOV operation
    ref_209224 = (ref_209222 | ref_209208) # OR operation
    ref_209785 = ref_209224 # MOV operation
    ref_218385 = ref_209785 # MOV operation
    ref_218907 = ref_218385 # MOV operation
    ref_218925 = (ref_218907 >> (0x33 & 0x3F)) # SHR operation
    ref_218932 = ref_218925 # MOV operation
    ref_223341 = ref_209785 # MOV operation
    ref_224346 = ref_223341 # MOV operation
    ref_224356 = ((ref_224346 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_224363 = ref_224356 # MOV operation
    ref_224907 = ref_224363 # MOV operation
    ref_224921 = ref_218932 # MOV operation
    ref_224923 = (ref_224921 | ref_224907) # OR operation
    ref_229140 = ref_188162 # MOV operation
    ref_229677 = ref_229140 # MOV operation
    ref_229691 = ref_224923 # MOV operation
    ref_229693 = (ref_229691 | ref_229677) # OR operation
    ref_230172 = ref_229693 # MOV operation
    ref_230174 = ((ref_230172 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_230175 = ((ref_230172 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_230176 = ((ref_230172 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_230177 = ((ref_230172 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_230178 = ((ref_230172 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_230179 = ((ref_230172 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_230180 = ((ref_230172 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_230181 = (ref_230172 & 0xFF) # Byte reference - MOV operation
    ref_238234 = ref_188162 # MOV operation
    ref_239317 = ref_238234 # MOV operation
    ref_239325 = ((0x6402BE2 + ref_239317) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_239843 = ref_239325 # MOV operation
    ref_247996 = ref_230172 # MOV operation
    ref_252349 = ref_239843 # MOV operation
    ref_252851 = ref_252349 # MOV operation
    ref_252865 = ref_247996 # MOV operation
    ref_252867 = (((sx(0x40, ref_252865) * sx(0x40, ref_252851)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_253985 = ref_252867 # MOV operation
    ref_253987 = (((sx(0x40, ref_253985) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_258727 = ref_188162 # MOV operation
    ref_259212 = ref_258727 # MOV operation
    ref_259228 = (0x3544223F | ref_259212) # OR operation
    ref_259730 = ref_259228 # MOV operation
    ref_259744 = ref_253987 # MOV operation
    ref_259746 = (((sx(0x40, ref_259744) * sx(0x40, ref_259730)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_260294 = ref_259746 # MOV operation
    ref_268936 = ref_260294 # MOV operation
    ref_269454 = ref_268936 # MOV operation
    ref_269470 = (0x1F & ref_269454) # AND operation
    ref_270512 = ref_269470 # MOV operation
    ref_270522 = ((ref_270512 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_270529 = ref_270522 # MOV operation
    ref_274903 = ref_239843 # MOV operation
    ref_275425 = ref_274903 # MOV operation
    ref_275439 = ref_270529 # MOV operation
    ref_275441 = (ref_275439 | ref_275425) # OR operation
    ref_275978 = ref_275441 # MOV operation
    ref_324610 = ref_260294 # MOV operation
    ref_325626 = ref_324610 # MOV operation
    ref_325636 = ((((0x0) << 64 | ref_325626) / 0x8) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_326145 = ref_325636 # MOV operation
    ref_326147 = ((ref_326145 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_326148 = ((ref_326145 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_326149 = ((ref_326145 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_326150 = ((ref_326145 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_326151 = ((ref_326145 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_326152 = ((ref_326145 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_326153 = ((ref_326145 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_326154 = (ref_326145 & 0xFF) # Byte reference - MOV operation
    ref_333582 = ref_230179 # MOVZX operation
    ref_334716 = (ref_333582 & 0xFF) # MOVZX operation
    ref_342103 = ref_230176 # MOVZX operation
    ref_349598 = (ref_342103 & 0xFF) # MOVZX operation
    ref_349600 = (ref_349598 & 0xFF) # Byte reference - MOV operation
    ref_350640 = (ref_334716 & 0xFF) # MOVZX operation
    ref_358024 = (ref_350640 & 0xFF) # MOVZX operation
    ref_358026 = (ref_358024 & 0xFF) # Byte reference - MOV operation
    ref_365513 = ref_230174 # MOVZX operation
    ref_366541 = (ref_365513 & 0xFF) # MOVZX operation
    ref_373993 = ref_230181 # MOVZX operation
    ref_381404 = (ref_373993 & 0xFF) # MOVZX operation
    ref_381406 = (ref_381404 & 0xFF) # Byte reference - MOV operation
    ref_382494 = (ref_366541 & 0xFF) # MOVZX operation
    ref_389949 = (ref_382494 & 0xFF) # MOVZX operation
    ref_389951 = (ref_389949 & 0xFF) # Byte reference - MOV operation
    ref_397336 = ref_326150 # MOVZX operation
    ref_398431 = (ref_397336 & 0xFF) # MOVZX operation
    ref_405909 = ref_326154 # MOVZX operation
    ref_413275 = (ref_405909 & 0xFF) # MOVZX operation
    ref_413277 = (ref_413275 & 0xFF) # Byte reference - MOV operation
    ref_414401 = (ref_398431 & 0xFF) # MOVZX operation
    ref_421832 = (ref_414401 & 0xFF) # MOVZX operation
    ref_421834 = (ref_421832 & 0xFF) # Byte reference - MOV operation
    ref_430309 = ref_260294 # MOV operation
    ref_431439 = ref_430309 # MOV operation
    ref_431447 = ((0x369A4780 + ref_431439) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_435695 = ref_275978 # MOV operation
    ref_436207 = ref_435695 # MOV operation
    ref_436221 = ref_431447 # MOV operation
    ref_436223 = (((sx(0x40, ref_436221) * sx(0x40, ref_436207)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_442639 = ((((((((ref_381406) << 8 | ref_230175) << 8 | ref_358026) << 8 | ref_230177) << 8 | ref_230178) << 8 | ref_349600) << 8 | ref_230180) << 8 | ref_389951) # MOV operation
    ref_443157 = ref_442639 # MOV operation
    ref_443175 = (ref_443157 >> (0x3 & 0x3F)) # SHR operation
    ref_443182 = ref_443175 # MOV operation
    ref_443674 = ref_443182 # MOV operation
    ref_443690 = (0xF & ref_443674) # AND operation
    ref_444247 = ref_443690 # MOV operation
    ref_444263 = (0x1 | ref_444247) # OR operation
    ref_444786 = ref_444263 # MOV operation
    ref_444788 = ((0x40 - ref_444786) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_444796 = ref_444788 # MOV operation
    ref_449132 = ((((((((ref_326147) << 8 | ref_326148) << 8 | ref_326149) << 8 | ref_413277) << 8 | ref_326151) << 8 | ref_326152) << 8 | ref_326153) << 8 | ref_421834) # MOV operation
    ref_449590 = ref_449132 # MOV operation
    ref_449604 = ref_444796 # MOV operation
    ref_449606 = (ref_449604 & 0xFFFFFFFF) # MOV operation
    ref_449608 = (ref_449590 >> ((ref_449606 & 0xFF) & 0x3F)) # SHR operation
    ref_449615 = ref_449608 # MOV operation
    ref_453966 = ((((((((ref_326147) << 8 | ref_326148) << 8 | ref_326149) << 8 | ref_413277) << 8 | ref_326151) << 8 | ref_326152) << 8 | ref_326153) << 8 | ref_421834) # MOV operation
    ref_459877 = ((((((((ref_381406) << 8 | ref_230175) << 8 | ref_358026) << 8 | ref_230177) << 8 | ref_230178) << 8 | ref_349600) << 8 | ref_230180) << 8 | ref_389951) # MOV operation
    ref_460391 = ref_459877 # MOV operation
    ref_460409 = (ref_460391 >> (0x3 & 0x3F)) # SHR operation
    ref_460416 = ref_460409 # MOV operation
    ref_460878 = ref_460416 # MOV operation
    ref_460894 = (0xF & ref_460878) # AND operation
    ref_461435 = ref_460894 # MOV operation
    ref_461451 = (0x1 | ref_461435) # OR operation
    ref_461956 = ref_453966 # MOV operation
    ref_461962 = ref_461451 # MOV operation
    ref_461964 = (ref_461962 & 0xFFFFFFFF) # MOV operation
    ref_461966 = ((ref_461956 << ((ref_461964 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_461973 = ref_461966 # MOV operation
    ref_462509 = ref_461973 # MOV operation
    ref_462523 = ref_449615 # MOV operation
    ref_462525 = (ref_462523 | ref_462509) # OR operation
    ref_463048 = ref_462525 # MOV operation
    ref_463062 = ref_436223 # MOV operation
    ref_463064 = (((sx(0x40, ref_463062) * sx(0x40, ref_463048)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_463588 = ref_463064 # MOV operation
    ref_464612 = ref_463588 # MOV operation
    ref_464614 = ref_464612 # MOV operation
    endb = ref_464614


print endb & 0xffffffffffffffff
