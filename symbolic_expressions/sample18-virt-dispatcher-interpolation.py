#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_14987 = ref_278 # MOV operation
ref_16233 = ref_14987 # MOV operation
ref_16241 = ((ref_16233 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_16248 = ref_16241 # MOV operation
ref_21010 = ref_278 # MOV operation
ref_22001 = ref_21010 # MOV operation
ref_22009 = (ref_22001 >> (0xD & 0x3F)) # SHR operation
ref_22016 = ref_22009 # MOV operation
ref_22635 = ref_22016 # MOV operation
ref_22647 = ref_16248 # MOV operation
ref_22649 = (ref_22647 | ref_22635) # OR operation
ref_23528 = ref_22649 # MOV operation
ref_23542 = ((0x2EA4A1C39AF5800 + ref_23528) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_24137 = ref_23542 # MOV operation
ref_33212 = ref_24137 # MOV operation
ref_37954 = ref_278 # MOV operation
ref_38553 = ref_37954 # MOV operation
ref_38565 = ref_33212 # MOV operation
ref_38567 = ((ref_38553 - ref_38565) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_38575 = ref_38567 # MOV operation
ref_39164 = ref_38575 # MOV operation
ref_48154 = ref_278 # MOV operation
ref_49145 = ref_48154 # MOV operation
ref_49153 = (ref_49145 >> (0x37 & 0x3F)) # SHR operation
ref_49160 = ref_49153 # MOV operation
ref_53922 = ref_278 # MOV operation
ref_55168 = ref_53922 # MOV operation
ref_55176 = ((ref_55168 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_55183 = ref_55176 # MOV operation
ref_55802 = ref_55183 # MOV operation
ref_55814 = ref_49160 # MOV operation
ref_55816 = (ref_55814 | ref_55802) # OR operation
ref_56410 = ref_55816 # MOV operation
ref_66039 = ref_278 # MOV operation
ref_66638 = ref_66039 # MOV operation
ref_66652 = (0x3E908497 | ref_66638) # OR operation
ref_67246 = ref_66652 # MOV operation
ref_72700 = ref_67246 # MOV operation
ref_77527 = ref_56410 # MOV operation
ref_78126 = ref_77527 # MOV operation
ref_78138 = ref_72700 # MOV operation
ref_78140 = ((ref_78126 - ref_78138) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_78148 = ref_78140 # MOV operation
ref_82995 = ref_24137 # MOV operation
ref_88461 = ref_39164 # MOV operation
ref_89452 = ref_88461 # MOV operation
ref_89460 = (ref_89452 >> (0x2 & 0x3F)) # SHR operation
ref_89467 = ref_89460 # MOV operation
ref_90733 = ref_89467 # MOV operation
ref_90739 = (0xF & ref_90733) # AND operation
ref_91363 = ref_90739 # MOV operation
ref_91377 = (0x1 | ref_91363) # OR operation
ref_92652 = ref_91377 # MOV operation
ref_92654 = ((0x40 - ref_92652) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_92662 = ref_92654 # MOV operation
ref_93289 = ref_82995 # MOV operation
ref_93293 = ref_92662 # MOV operation
ref_93295 = (ref_93293 & 0xFFFFFFFF) # MOV operation
ref_93297 = ((ref_93289 << ((ref_93295 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_93304 = ref_93297 # MOV operation
ref_98151 = ref_24137 # MOV operation
ref_103617 = ref_39164 # MOV operation
ref_104608 = ref_103617 # MOV operation
ref_104616 = (ref_104608 >> (0x2 & 0x3F)) # SHR operation
ref_104623 = ref_104616 # MOV operation
ref_105889 = ref_104623 # MOV operation
ref_105895 = (0xF & ref_105889) # AND operation
ref_106519 = ref_105895 # MOV operation
ref_106533 = (0x1 | ref_106519) # OR operation
ref_106910 = ref_98151 # MOV operation
ref_106914 = ref_106533 # MOV operation
ref_106916 = (ref_106914 & 0xFFFFFFFF) # MOV operation
ref_106918 = (ref_106910 >> ((ref_106916 & 0xFF) & 0x3F)) # SHR operation
ref_106925 = ref_106918 # MOV operation
ref_107544 = ref_106925 # MOV operation
ref_107556 = ref_93304 # MOV operation
ref_107558 = (ref_107556 | ref_107544) # OR operation
ref_108182 = ref_107558 # MOV operation
ref_108194 = ref_78148 # MOV operation
ref_108196 = ((ref_108182 - ref_108194) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_108198 = ((((ref_108182 ^ (ref_108194 ^ ref_108196)) ^ ((ref_108182 ^ ref_108196) & (ref_108182 ^ ref_108194))) >> 63) & 0x1) # Carry flag
ref_108204 = ((((ref_108194 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (ref_108198 == 0x1) else 0x0)) # SETB operation
ref_108206 = (ref_108204 & 0xFF) # MOVZX operation
ref_108817 = (ref_108206 & 0xFFFFFFFF) # MOV operation
ref_108819 = ((ref_108817 & 0xFFFFFFFF) & (ref_108817 & 0xFFFFFFFF)) # TEST operation
ref_108824 = (0x1 if (ref_108819 == 0x0) else 0x0) # Zero flag
ref_108826 = (0x1934 if (ref_108824 == 0x1) else 0x1916) # Program Counter


if (ref_108824 == 0x1):
    ref_253072 = SymVar_0
    ref_253087 = ref_253072 # MOV operation
    ref_267801 = ref_253087 # MOV operation
    ref_269047 = ref_267801 # MOV operation
    ref_269055 = ((ref_269047 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_269062 = ref_269055 # MOV operation
    ref_273824 = ref_253087 # MOV operation
    ref_274815 = ref_273824 # MOV operation
    ref_274823 = (ref_274815 >> (0xD & 0x3F)) # SHR operation
    ref_274830 = ref_274823 # MOV operation
    ref_275449 = ref_274830 # MOV operation
    ref_275461 = ref_269062 # MOV operation
    ref_275463 = (ref_275461 | ref_275449) # OR operation
    ref_276342 = ref_275463 # MOV operation
    ref_276356 = ((0x2EA4A1C39AF5800 + ref_276342) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_276951 = ref_276356 # MOV operation
    ref_286026 = ref_276951 # MOV operation
    ref_290768 = ref_253087 # MOV operation
    ref_291367 = ref_290768 # MOV operation
    ref_291379 = ref_286026 # MOV operation
    ref_291381 = ((ref_291367 - ref_291379) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_291389 = ref_291381 # MOV operation
    ref_291978 = ref_291389 # MOV operation
    ref_300968 = ref_253087 # MOV operation
    ref_301959 = ref_300968 # MOV operation
    ref_301967 = (ref_301959 >> (0x37 & 0x3F)) # SHR operation
    ref_301974 = ref_301967 # MOV operation
    ref_306736 = ref_253087 # MOV operation
    ref_307982 = ref_306736 # MOV operation
    ref_307990 = ((ref_307982 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_307997 = ref_307990 # MOV operation
    ref_308616 = ref_307997 # MOV operation
    ref_308628 = ref_301974 # MOV operation
    ref_308630 = (ref_308628 | ref_308616) # OR operation
    ref_309224 = ref_308630 # MOV operation
    ref_318853 = ref_253087 # MOV operation
    ref_319452 = ref_318853 # MOV operation
    ref_319466 = (0x3E908497 | ref_319452) # OR operation
    ref_320060 = ref_319466 # MOV operation
    ref_371255 = ref_276951 # MOV operation
    ref_376721 = ref_291978 # MOV operation
    ref_377712 = ref_376721 # MOV operation
    ref_377720 = (ref_377712 >> (0x4 & 0x3F)) # SHR operation
    ref_377727 = ref_377720 # MOV operation
    ref_378993 = ref_377727 # MOV operation
    ref_378999 = (0xF & ref_378993) # AND operation
    ref_379623 = ref_378999 # MOV operation
    ref_379637 = (0x1 | ref_379623) # OR operation
    ref_380912 = ref_379637 # MOV operation
    ref_380914 = ((0x40 - ref_380912) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_380922 = ref_380914 # MOV operation
    ref_381294 = ref_371255 # MOV operation
    ref_381298 = ref_380922 # MOV operation
    ref_381300 = (ref_381298 & 0xFFFFFFFF) # MOV operation
    ref_381302 = (ref_381294 >> ((ref_381300 & 0xFF) & 0x3F)) # SHR operation
    ref_381309 = ref_381302 # MOV operation
    ref_386156 = ref_276951 # MOV operation
    ref_391622 = ref_291978 # MOV operation
    ref_392613 = ref_391622 # MOV operation
    ref_392621 = (ref_392613 >> (0x4 & 0x3F)) # SHR operation
    ref_392628 = ref_392621 # MOV operation
    ref_393894 = ref_392628 # MOV operation
    ref_393900 = (0xF & ref_393894) # AND operation
    ref_394524 = ref_393900 # MOV operation
    ref_394538 = (0x1 | ref_394524) # OR operation
    ref_395170 = ref_386156 # MOV operation
    ref_395174 = ref_394538 # MOV operation
    ref_395176 = (ref_395174 & 0xFFFFFFFF) # MOV operation
    ref_395178 = ((ref_395170 << ((ref_395176 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_395185 = ref_395178 # MOV operation
    ref_395804 = ref_395185 # MOV operation
    ref_395816 = ref_381309 # MOV operation
    ref_395818 = (ref_395816 | ref_395804) # OR operation
    ref_401309 = ref_320060 # MOV operation
    ref_406136 = ref_309224 # MOV operation
    ref_406735 = ref_406136 # MOV operation
    ref_406747 = ref_401309 # MOV operation
    ref_406749 = (ref_406747 | ref_406735) # OR operation
    ref_407765 = ref_406749 # MOV operation
    ref_407773 = (ref_407765 >> (0x4 & 0x3F)) # SHR operation
    ref_407780 = ref_407773 # MOV operation
    ref_409046 = ref_407780 # MOV operation
    ref_409052 = (0x7 & ref_409046) # AND operation
    ref_409676 = ref_409052 # MOV operation
    ref_409690 = (0x1 | ref_409676) # OR operation
    ref_410067 = ref_395818 # MOV operation
    ref_410071 = ref_409690 # MOV operation
    ref_410073 = (ref_410071 & 0xFFFFFFFF) # MOV operation
    ref_410075 = (ref_410067 >> ((ref_410073 & 0xFF) & 0x3F)) # SHR operation
    ref_410082 = ref_410075 # MOV operation
    ref_410671 = ref_410082 # MOV operation
    ref_411673 = ref_410671 # MOV operation
    ref_411675 = ref_411673 # MOV operation
    endb = ref_411675


else:
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_14987 = ref_278 # MOV operation
    ref_16233 = ref_14987 # MOV operation
    ref_16241 = ((ref_16233 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_16248 = ref_16241 # MOV operation
    ref_21010 = ref_278 # MOV operation
    ref_22001 = ref_21010 # MOV operation
    ref_22009 = (ref_22001 >> (0xD & 0x3F)) # SHR operation
    ref_22016 = ref_22009 # MOV operation
    ref_22635 = ref_22016 # MOV operation
    ref_22647 = ref_16248 # MOV operation
    ref_22649 = (ref_22647 | ref_22635) # OR operation
    ref_23528 = ref_22649 # MOV operation
    ref_23542 = ((0x2EA4A1C39AF5800 + ref_23528) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_24137 = ref_23542 # MOV operation
    ref_33212 = ref_24137 # MOV operation
    ref_37954 = ref_278 # MOV operation
    ref_38553 = ref_37954 # MOV operation
    ref_38565 = ref_33212 # MOV operation
    ref_38567 = ((ref_38553 - ref_38565) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_38575 = ref_38567 # MOV operation
    ref_39164 = ref_38575 # MOV operation
    ref_39166 = ((ref_39164 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_39167 = ((ref_39164 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_39168 = ((ref_39164 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_39169 = ((ref_39164 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_39170 = ((ref_39164 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_39171 = ((ref_39164 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_39172 = ((ref_39164 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_39173 = (ref_39164 & 0xFF) # Byte reference - MOV operation
    ref_48154 = ref_278 # MOV operation
    ref_49145 = ref_48154 # MOV operation
    ref_49153 = (ref_49145 >> (0x37 & 0x3F)) # SHR operation
    ref_49160 = ref_49153 # MOV operation
    ref_53922 = ref_278 # MOV operation
    ref_55168 = ref_53922 # MOV operation
    ref_55176 = ((ref_55168 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_55183 = ref_55176 # MOV operation
    ref_55802 = ref_55183 # MOV operation
    ref_55814 = ref_49160 # MOV operation
    ref_55816 = (ref_55814 | ref_55802) # OR operation
    ref_56410 = ref_55816 # MOV operation
    ref_66039 = ref_278 # MOV operation
    ref_66638 = ref_66039 # MOV operation
    ref_66652 = (0x3E908497 | ref_66638) # OR operation
    ref_67246 = ref_66652 # MOV operation
    ref_117140 = ((((ref_39166) << 8 | ref_39167) << 8 | ref_39168) << 8 | ref_39169) # MOV operation
    ref_118139 = (ref_117140 & 0xFFFFFFFF) # MOV operation
    ref_126433 = ((((ref_39170) << 8 | ref_39171) << 8 | ref_39172) << 8 | ref_39173) # MOV operation
    ref_134715 = (ref_126433 & 0xFFFFFFFF) # MOV operation
    ref_134717 = (((ref_134715 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_134718 = (((ref_134715 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_134719 = (((ref_134715 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_134720 = ((ref_134715 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_135726 = (ref_118139 & 0xFFFFFFFF) # MOV operation
    ref_144008 = (ref_135726 & 0xFFFFFFFF) # MOV operation
    ref_144010 = (((ref_144008 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_144011 = (((ref_144008 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_144012 = (((ref_144008 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_144013 = ((ref_144008 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_153079 = ref_24137 # MOV operation
    ref_154325 = ref_153079 # MOV operation
    ref_154331 = (0x3F & ref_154325) # AND operation
    ref_155602 = ref_154331 # MOV operation
    ref_155610 = ((ref_155602 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_155617 = ref_155610 # MOV operation
    ref_160464 = ref_24137 # MOV operation
    ref_161063 = ref_160464 # MOV operation
    ref_161075 = ref_155617 # MOV operation
    ref_161077 = (ref_161075 | ref_161063) # OR operation
    ref_161671 = ref_161077 # MOV operation
    ref_170746 = ref_161671 # MOV operation
    ref_171992 = ref_170746 # MOV operation
    ref_171998 = (0x1F & ref_171992) # AND operation
    ref_173269 = ref_171998 # MOV operation
    ref_173277 = ((ref_173269 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_173284 = ref_173277 # MOV operation
    ref_178131 = ref_67246 # MOV operation
    ref_178730 = ref_178131 # MOV operation
    ref_178742 = ref_173284 # MOV operation
    ref_178744 = (ref_178742 | ref_178730) # OR operation
    ref_179338 = ref_178744 # MOV operation
    ref_188413 = ref_56410 # MOV operation
    ref_193240 = ref_161671 # MOV operation
    ref_194094 = ref_193240 # MOV operation
    ref_194106 = ref_188413 # MOV operation
    ref_194108 = ((ref_194106 + ref_194094) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_195380 = ref_194108 # MOV operation
    ref_195386 = (0x1F & ref_195380) # AND operation
    ref_196657 = ref_195386 # MOV operation
    ref_196665 = ((ref_196657 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_196672 = ref_196665 # MOV operation
    ref_201519 = ref_161671 # MOV operation
    ref_202118 = ref_201519 # MOV operation
    ref_202130 = ref_196672 # MOV operation
    ref_202132 = (ref_202130 | ref_202118) # OR operation
    ref_202726 = ref_202132 # MOV operation
    ref_212332 = ref_202726 # MOV operation
    ref_217798 = ((((((((ref_134717) << 8 | ref_134718) << 8 | ref_134719) << 8 | ref_134720) << 8 | ref_144010) << 8 | ref_144011) << 8 | ref_144012) << 8 | ref_144013) # MOV operation
    ref_218789 = ref_217798 # MOV operation
    ref_218797 = (ref_218789 >> (0x4 & 0x3F)) # SHR operation
    ref_218804 = ref_218797 # MOV operation
    ref_220070 = ref_218804 # MOV operation
    ref_220076 = (0xF & ref_220070) # AND operation
    ref_220700 = ref_220076 # MOV operation
    ref_220714 = (0x1 | ref_220700) # OR operation
    ref_221989 = ref_220714 # MOV operation
    ref_221991 = ((0x40 - ref_221989) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_221999 = ref_221991 # MOV operation
    ref_222371 = ref_212332 # MOV operation
    ref_222375 = ref_221999 # MOV operation
    ref_222377 = (ref_222375 & 0xFFFFFFFF) # MOV operation
    ref_222379 = (ref_222371 >> ((ref_222377 & 0xFF) & 0x3F)) # SHR operation
    ref_222386 = ref_222379 # MOV operation
    ref_227233 = ref_202726 # MOV operation
    ref_232699 = ((((((((ref_134717) << 8 | ref_134718) << 8 | ref_134719) << 8 | ref_134720) << 8 | ref_144010) << 8 | ref_144011) << 8 | ref_144012) << 8 | ref_144013) # MOV operation
    ref_233690 = ref_232699 # MOV operation
    ref_233698 = (ref_233690 >> (0x4 & 0x3F)) # SHR operation
    ref_233705 = ref_233698 # MOV operation
    ref_234971 = ref_233705 # MOV operation
    ref_234977 = (0xF & ref_234971) # AND operation
    ref_235601 = ref_234977 # MOV operation
    ref_235615 = (0x1 | ref_235601) # OR operation
    ref_236247 = ref_227233 # MOV operation
    ref_236251 = ref_235615 # MOV operation
    ref_236253 = (ref_236251 & 0xFFFFFFFF) # MOV operation
    ref_236255 = ((ref_236247 << ((ref_236253 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_236262 = ref_236255 # MOV operation
    ref_236881 = ref_236262 # MOV operation
    ref_236893 = ref_222386 # MOV operation
    ref_236895 = (ref_236893 | ref_236881) # OR operation
    ref_242386 = ref_179338 # MOV operation
    ref_247213 = ref_56410 # MOV operation
    ref_247812 = ref_247213 # MOV operation
    ref_247824 = ref_242386 # MOV operation
    ref_247826 = (ref_247824 | ref_247812) # OR operation
    ref_248842 = ref_247826 # MOV operation
    ref_248850 = (ref_248842 >> (0x4 & 0x3F)) # SHR operation
    ref_248857 = ref_248850 # MOV operation
    ref_250123 = ref_248857 # MOV operation
    ref_250129 = (0x7 & ref_250123) # AND operation
    ref_250753 = ref_250129 # MOV operation
    ref_250767 = (0x1 | ref_250753) # OR operation
    ref_251144 = ref_236895 # MOV operation
    ref_251148 = ref_250767 # MOV operation
    ref_251150 = (ref_251148 & 0xFFFFFFFF) # MOV operation
    ref_251152 = (ref_251144 >> ((ref_251150 & 0xFF) & 0x3F)) # SHR operation
    ref_251159 = ref_251152 # MOV operation
    ref_251748 = ref_251159 # MOV operation
    ref_252750 = ref_251748 # MOV operation
    ref_252752 = ref_252750 # MOV operation
    endb = ref_252752


print endb & 0xffffffffffffffff
