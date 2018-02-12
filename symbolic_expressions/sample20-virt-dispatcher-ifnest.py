#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_7330 = ref_278 # MOV operation
ref_7621 = ref_7330 # MOV operation
ref_7627 = (0x1F02C962 | ref_7621) # OR operation
ref_7916 = ref_7627 # MOV operation
ref_7922 = (0x1F8797B2 & ref_7916) # AND operation
ref_8018 = ref_7922 # MOV operation
ref_10702 = ref_278 # MOV operation
ref_12351 = ref_8018 # MOV operation
ref_12503 = ref_10702 # MOV operation
ref_12507 = ref_12351 # MOV operation
ref_12509 = (ref_12507 & ref_12503) # AND operation
ref_12605 = ref_12509 # MOV operation
ref_15289 = ref_278 # MOV operation
ref_15571 = ref_15289 # MOV operation
ref_15577 = (((sx(0x40, 0x66AF1DF) * sx(0x40, ref_15571)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_17360 = ref_12605 # MOV operation
ref_17495 = ref_17360 # MOV operation
ref_17509 = (ref_17495 >> (0x7 & 0x3F)) # SHR operation
ref_19295 = ref_12605 # MOV operation
ref_19448 = ref_19295 # MOV operation
ref_19462 = ((ref_19448 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_19666 = ref_17509 # MOV operation
ref_19670 = ref_19462 # MOV operation
ref_19672 = (ref_19670 | ref_19666) # OR operation
ref_19957 = ref_15577 # MOV operation
ref_19961 = ref_19672 # MOV operation
ref_19963 = ((ref_19961 + ref_19957) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_20060 = ref_19963 # MOV operation
ref_35499 = ref_20060 # MOV operation
ref_37807 = ref_20060 # MOV operation
ref_38067 = ref_35499 # MOV operation
ref_38071 = ref_37807 # MOV operation
ref_38073 = ((ref_38071 + ref_38067) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_38170 = ref_38073 # MOV operation
ref_42698 = ref_20060 # MOV operation
ref_44714 = ref_12605 # MOV operation
ref_44978 = ref_44714 # MOV operation
ref_44984 = (0x7 & ref_44978) # AND operation
ref_45162 = ref_44984 # MOV operation
ref_45176 = ((ref_45162 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_45380 = ref_42698 # MOV operation
ref_45384 = ref_45176 # MOV operation
ref_45386 = (ref_45384 | ref_45380) # OR operation
ref_45482 = ref_45386 # MOV operation
ref_45484 = ((ref_45482 >> 56) & 0xFF) # Byte reference - MOV operation
ref_45485 = ((ref_45482 >> 48) & 0xFF) # Byte reference - MOV operation
ref_45486 = ((ref_45482 >> 40) & 0xFF) # Byte reference - MOV operation
ref_45487 = ((ref_45482 >> 32) & 0xFF) # Byte reference - MOV operation
ref_45488 = ((ref_45482 >> 24) & 0xFF) # Byte reference - MOV operation
ref_45489 = ((ref_45482 >> 16) & 0xFF) # Byte reference - MOV operation
ref_45490 = ((ref_45482 >> 8) & 0xFF) # Byte reference - MOV operation
ref_45491 = (ref_45482 & 0xFF) # Byte reference - MOV operation
ref_49335 = ref_45484 # MOVZX operation
ref_49569 = (ref_49335 & 0xFF) # MOVZX operation
ref_56612 = ref_45491 # MOVZX operation
ref_56846 = (ref_56612 & 0xFF) # MOVZX operation
ref_56848 = (ref_56846 & 0xFF) # Byte reference - MOV operation
ref_60691 = (ref_49569 & 0xFF) # MOVZX operation
ref_60925 = (ref_60691 & 0xFF) # MOVZX operation
ref_60927 = (ref_60925 & 0xFF) # Byte reference - MOV operation
ref_64127 = ref_8018 # MOV operation
ref_66547 = ((((((((ref_56848) << 8 | ref_45485) << 8 | ref_45486) << 8 | ref_45487) << 8 | ref_45488) << 8 | ref_45489) << 8 | ref_45490) << 8 | ref_60927) # MOV operation
ref_68451 = ref_12605 # MOV operation
ref_68603 = ref_66547 # MOV operation
ref_68607 = ref_68451 # MOV operation
ref_68609 = (ref_68607 & ref_68603) # AND operation
ref_68898 = ref_68609 # MOV operation
ref_68904 = (0x1F & ref_68898) # AND operation
ref_69082 = ref_68904 # MOV operation
ref_69096 = ((ref_69082 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_69300 = ref_64127 # MOV operation
ref_69304 = ref_69096 # MOV operation
ref_69306 = (ref_69304 | ref_69300) # OR operation
ref_69402 = ref_69306 # MOV operation
ref_75608 = ref_38170 # MOV operation
ref_77916 = ref_38170 # MOV operation
ref_78176 = ref_75608 # MOV operation
ref_78180 = ref_77916 # MOV operation
ref_78182 = ((ref_78180 + ref_78176) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_78279 = ref_78182 # MOV operation
ref_82807 = ref_78279 # MOV operation
ref_84823 = ((((((((ref_56848) << 8 | ref_45485) << 8 | ref_45486) << 8 | ref_45487) << 8 | ref_45488) << 8 | ref_45489) << 8 | ref_45490) << 8 | ref_60927) # MOV operation
ref_85087 = ref_84823 # MOV operation
ref_85093 = (0x7 & ref_85087) # AND operation
ref_85271 = ref_85093 # MOV operation
ref_85285 = ((ref_85271 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_85489 = ref_82807 # MOV operation
ref_85493 = ref_85285 # MOV operation
ref_85495 = (ref_85493 | ref_85489) # OR operation
ref_85591 = ref_85495 # MOV operation
ref_85593 = ((ref_85591 >> 56) & 0xFF) # Byte reference - MOV operation
ref_85594 = ((ref_85591 >> 48) & 0xFF) # Byte reference - MOV operation
ref_85595 = ((ref_85591 >> 40) & 0xFF) # Byte reference - MOV operation
ref_85596 = ((ref_85591 >> 32) & 0xFF) # Byte reference - MOV operation
ref_85597 = ((ref_85591 >> 24) & 0xFF) # Byte reference - MOV operation
ref_85598 = ((ref_85591 >> 16) & 0xFF) # Byte reference - MOV operation
ref_85599 = ((ref_85591 >> 8) & 0xFF) # Byte reference - MOV operation
ref_85600 = (ref_85591 & 0xFF) # Byte reference - MOV operation
ref_89444 = ref_85593 # MOVZX operation
ref_89678 = (ref_89444 & 0xFF) # MOVZX operation
ref_96721 = ref_85600 # MOVZX operation
ref_96955 = (ref_96721 & 0xFF) # MOVZX operation
ref_96957 = (ref_96955 & 0xFF) # Byte reference - MOV operation
ref_100800 = (ref_89678 & 0xFF) # MOVZX operation
ref_101034 = (ref_100800 & 0xFF) # MOVZX operation
ref_101036 = (ref_101034 & 0xFF) # Byte reference - MOV operation
ref_104236 = ref_69402 # MOV operation
ref_106656 = ((((((((ref_96957) << 8 | ref_85594) << 8 | ref_85595) << 8 | ref_85596) << 8 | ref_85597) << 8 | ref_85598) << 8 | ref_85599) << 8 | ref_101036) # MOV operation
ref_108560 = ((((((((ref_56848) << 8 | ref_45485) << 8 | ref_45486) << 8 | ref_45487) << 8 | ref_45488) << 8 | ref_45489) << 8 | ref_45490) << 8 | ref_60927) # MOV operation
ref_108712 = ref_106656 # MOV operation
ref_108716 = ref_108560 # MOV operation
ref_108718 = (ref_108716 & ref_108712) # AND operation
ref_109007 = ref_108718 # MOV operation
ref_109013 = (0x1F & ref_109007) # AND operation
ref_109191 = ref_109013 # MOV operation
ref_109205 = ((ref_109191 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_109409 = ref_104236 # MOV operation
ref_109413 = ref_109205 # MOV operation
ref_109415 = (ref_109413 | ref_109409) # OR operation
ref_109511 = ref_109415 # MOV operation
ref_114928 = ((((((((ref_56848) << 8 | ref_45485) << 8 | ref_45486) << 8 | ref_45487) << 8 | ref_45488) << 8 | ref_45489) << 8 | ref_45490) << 8 | ref_60927) # MOV operation
ref_116577 = ((((((((ref_96957) << 8 | ref_85594) << 8 | ref_85595) << 8 | ref_85596) << 8 | ref_85597) << 8 | ref_85598) << 8 | ref_85599) << 8 | ref_101036) # MOV operation
ref_116756 = ref_114928 # MOV operation
ref_116760 = ref_116577 # MOV operation
ref_116762 = (ref_116760 | ref_116756) # OR operation
ref_117051 = ref_116762 # MOV operation
ref_117057 = (0xF & ref_117051) # AND operation
ref_117373 = ref_117057 # MOV operation
ref_117379 = (0x1 | ref_117373) # OR operation
ref_119165 = ref_12605 # MOV operation
ref_119300 = ref_119165 # MOV operation
ref_119314 = (ref_119300 >> (0x1 & 0x3F)) # SHR operation
ref_119603 = ref_119314 # MOV operation
ref_119609 = (0xF & ref_119603) # AND operation
ref_119925 = ref_119609 # MOV operation
ref_119931 = (0x1 | ref_119925) # OR operation
ref_121605 = ref_109511 # MOV operation
ref_121740 = ref_121605 # MOV operation
ref_121752 = ref_119931 # MOV operation
ref_121754 = (ref_121740 >> ((ref_121752 & 0xFF) & 0x3F)) # SHR operation
ref_123540 = ref_12605 # MOV operation
ref_123675 = ref_123540 # MOV operation
ref_123689 = (ref_123675 >> (0x1 & 0x3F)) # SHR operation
ref_123978 = ref_123689 # MOV operation
ref_123984 = (0xF & ref_123978) # AND operation
ref_124300 = ref_123984 # MOV operation
ref_124306 = (0x1 | ref_124300) # OR operation
ref_124635 = ref_124306 # MOV operation
ref_124637 = ((0x40 - ref_124635) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_124645 = ref_124637 # MOV operation
ref_126314 = ref_109511 # MOV operation
ref_126467 = ref_126314 # MOV operation
ref_126479 = ref_124645 # MOV operation
ref_126481 = ((ref_126467 << ((ref_126479 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_126685 = ref_121754 # MOV operation
ref_126689 = ref_126481 # MOV operation
ref_126691 = (ref_126689 | ref_126685) # OR operation
ref_126869 = ref_126691 # MOV operation
ref_126881 = ref_117379 # MOV operation
ref_126883 = ((ref_126869 << ((ref_126881 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_128557 = ((((((((ref_56848) << 8 | ref_45485) << 8 | ref_45486) << 8 | ref_45487) << 8 | ref_45488) << 8 | ref_45489) << 8 | ref_45490) << 8 | ref_60927) # MOV operation
ref_130206 = ((((((((ref_96957) << 8 | ref_85594) << 8 | ref_85595) << 8 | ref_85596) << 8 | ref_85597) << 8 | ref_85598) << 8 | ref_85599) << 8 | ref_101036) # MOV operation
ref_130385 = ref_128557 # MOV operation
ref_130389 = ref_130206 # MOV operation
ref_130391 = (ref_130389 | ref_130385) # OR operation
ref_130680 = ref_130391 # MOV operation
ref_130686 = (0xF & ref_130680) # AND operation
ref_131002 = ref_130686 # MOV operation
ref_131008 = (0x1 | ref_131002) # OR operation
ref_131337 = ref_131008 # MOV operation
ref_131339 = ((0x40 - ref_131337) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_131347 = ref_131339 # MOV operation
ref_133128 = ref_12605 # MOV operation
ref_133263 = ref_133128 # MOV operation
ref_133277 = (ref_133263 >> (0x1 & 0x3F)) # SHR operation
ref_133566 = ref_133277 # MOV operation
ref_133572 = (0xF & ref_133566) # AND operation
ref_133888 = ref_133572 # MOV operation
ref_133894 = (0x1 | ref_133888) # OR operation
ref_135568 = ref_109511 # MOV operation
ref_135703 = ref_135568 # MOV operation
ref_135715 = ref_133894 # MOV operation
ref_135717 = (ref_135703 >> ((ref_135715 & 0xFF) & 0x3F)) # SHR operation
ref_137503 = ref_12605 # MOV operation
ref_137638 = ref_137503 # MOV operation
ref_137652 = (ref_137638 >> (0x1 & 0x3F)) # SHR operation
ref_137941 = ref_137652 # MOV operation
ref_137947 = (0xF & ref_137941) # AND operation
ref_138263 = ref_137947 # MOV operation
ref_138269 = (0x1 | ref_138263) # OR operation
ref_138598 = ref_138269 # MOV operation
ref_138600 = ((0x40 - ref_138598) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_138608 = ref_138600 # MOV operation
ref_140277 = ref_109511 # MOV operation
ref_140430 = ref_140277 # MOV operation
ref_140442 = ref_138608 # MOV operation
ref_140444 = ((ref_140430 << ((ref_140442 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_140648 = ref_135717 # MOV operation
ref_140652 = ref_140444 # MOV operation
ref_140654 = (ref_140652 | ref_140648) # OR operation
ref_140814 = ref_140654 # MOV operation
ref_140826 = ref_131347 # MOV operation
ref_140828 = (ref_140814 >> ((ref_140826 & 0xFF) & 0x3F)) # SHR operation
ref_141032 = ref_126883 # MOV operation
ref_141036 = ref_140828 # MOV operation
ref_141038 = (ref_141036 | ref_141032) # OR operation
ref_141134 = ref_141038 # MOV operation
ref_141481 = ref_141134 # MOV operation
ref_141483 = ref_141481 # MOV operation

print ref_141483 & 0xffffffffffffffff
