#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_97286 = ref_278 # MOV operation
ref_97362 = ref_97286 # MOV operation
ref_97376 = (0x1F02C962 | ref_97362) # OR operation
ref_97601 = ref_97376 # MOV operation
ref_97607 = (0x1F8797B2 & ref_97601) # AND operation
ref_98538 = ref_97607 # MOV operation
ref_99371 = ref_278 # MOV operation
ref_100269 = ref_98538 # MOV operation
ref_100353 = ref_99371 # MOV operation
ref_100357 = ref_100269 # MOV operation
ref_100359 = (ref_100357 & ref_100353) # AND operation
ref_101290 = ref_100359 # MOV operation
ref_102208 = ref_101290 # MOV operation
ref_102408 = ref_102208 # MOV operation
ref_102416 = ((ref_102408 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_102423 = ref_102416 # MOV operation
ref_103341 = ref_101290 # MOV operation
ref_103541 = ref_103341 # MOV operation
ref_103549 = (ref_103541 >> (0x7 & 0x3F)) # SHR operation
ref_103556 = ref_103549 # MOV operation
ref_103652 = ref_103556 # MOV operation
ref_103664 = ref_102423 # MOV operation
ref_103666 = (ref_103664 | ref_103652) # OR operation
ref_104504 = ref_278 # MOV operation
ref_104704 = ref_104504 # MOV operation
ref_104710 = (((sx(0x40, 0x66AF1DF) * sx(0x40, ref_104704)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_104808 = ref_104710 # MOV operation
ref_104820 = ref_103666 # MOV operation
ref_104822 = ((ref_104820 + ref_104808) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_105754 = ref_104822 # MOV operation
ref_114306 = ref_105754 # MOV operation
ref_115524 = ref_105754 # MOV operation
ref_115600 = ref_115524 # MOV operation
ref_115612 = ref_114306 # MOV operation
ref_115614 = ((ref_115612 + ref_115600) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_116546 = ref_115614 # MOV operation
ref_117552 = ref_101290 # MOV operation
ref_117752 = ref_117552 # MOV operation
ref_117758 = (0x7 & ref_117752) # AND operation
ref_117983 = ref_117758 # MOV operation
ref_117991 = ((ref_117983 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_117998 = ref_117991 # MOV operation
ref_119236 = ref_105754 # MOV operation
ref_119312 = ref_119236 # MOV operation
ref_119324 = ref_117998 # MOV operation
ref_119326 = (ref_119324 | ref_119312) # OR operation
ref_120577 = ref_119326 # MOV operation
ref_120579 = ((ref_120577 >> 56) & 0xFF) # Byte reference - MOV operation
ref_120580 = ((ref_120577 >> 48) & 0xFF) # Byte reference - MOV operation
ref_120581 = ((ref_120577 >> 40) & 0xFF) # Byte reference - MOV operation
ref_120582 = ((ref_120577 >> 32) & 0xFF) # Byte reference - MOV operation
ref_120583 = ((ref_120577 >> 24) & 0xFF) # Byte reference - MOV operation
ref_120584 = ((ref_120577 >> 16) & 0xFF) # Byte reference - MOV operation
ref_120585 = ((ref_120577 >> 8) & 0xFF) # Byte reference - MOV operation
ref_120586 = (ref_120577 & 0xFF) # Byte reference - MOV operation
ref_122421 = ref_120579 # MOVZX operation
ref_122625 = (ref_122421 & 0xFF) # MOVZX operation
ref_124461 = ref_120586 # MOVZX operation
ref_126285 = (ref_124461 & 0xFF) # MOVZX operation
ref_126287 = (ref_126285 & 0xFF) # Byte reference - MOV operation
ref_126501 = (ref_122625 & 0xFF) # MOVZX operation
ref_128325 = (ref_126501 & 0xFF) # MOVZX operation
ref_128327 = (ref_128325 & 0xFF) # Byte reference - MOV operation
ref_129555 = ((((((((ref_126287) << 8 | ref_120580) << 8 | ref_120581) << 8 | ref_120582) << 8 | ref_120583) << 8 | ref_120584) << 8 | ref_120585) << 8 | ref_128327) # MOV operation
ref_130541 = ref_101290 # MOV operation
ref_130625 = ref_129555 # MOV operation
ref_130629 = ref_130541 # MOV operation
ref_130631 = (ref_130629 & ref_130625) # AND operation
ref_130856 = ref_130631 # MOV operation
ref_130862 = (0x1F & ref_130856) # AND operation
ref_131087 = ref_130862 # MOV operation
ref_131095 = ((ref_131087 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_131102 = ref_131095 # MOV operation
ref_132020 = ref_98538 # MOV operation
ref_132096 = ref_132020 # MOV operation
ref_132108 = ref_131102 # MOV operation
ref_132110 = (ref_132108 | ref_132096) # OR operation
ref_133041 = ref_132110 # MOV operation
ref_135584 = ref_116546 # MOV operation
ref_136802 = ref_116546 # MOV operation
ref_136878 = ref_136802 # MOV operation
ref_136890 = ref_135584 # MOV operation
ref_136892 = ((ref_136890 + ref_136878) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_137824 = ref_136892 # MOV operation
ref_138830 = ((((((((ref_126287) << 8 | ref_120580) << 8 | ref_120581) << 8 | ref_120582) << 8 | ref_120583) << 8 | ref_120584) << 8 | ref_120585) << 8 | ref_128327) # MOV operation
ref_139030 = ref_138830 # MOV operation
ref_139036 = (0x7 & ref_139030) # AND operation
ref_139261 = ref_139036 # MOV operation
ref_139269 = ((ref_139261 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_139276 = ref_139269 # MOV operation
ref_140514 = ref_137824 # MOV operation
ref_140590 = ref_140514 # MOV operation
ref_140602 = ref_139276 # MOV operation
ref_140604 = (ref_140602 | ref_140590) # OR operation
ref_141855 = ref_140604 # MOV operation
ref_141857 = ((ref_141855 >> 56) & 0xFF) # Byte reference - MOV operation
ref_141858 = ((ref_141855 >> 48) & 0xFF) # Byte reference - MOV operation
ref_141859 = ((ref_141855 >> 40) & 0xFF) # Byte reference - MOV operation
ref_141860 = ((ref_141855 >> 32) & 0xFF) # Byte reference - MOV operation
ref_141861 = ((ref_141855 >> 24) & 0xFF) # Byte reference - MOV operation
ref_141862 = ((ref_141855 >> 16) & 0xFF) # Byte reference - MOV operation
ref_141863 = ((ref_141855 >> 8) & 0xFF) # Byte reference - MOV operation
ref_141864 = (ref_141855 & 0xFF) # Byte reference - MOV operation
ref_143699 = ref_141857 # MOVZX operation
ref_143903 = (ref_143699 & 0xFF) # MOVZX operation
ref_145739 = ref_141864 # MOVZX operation
ref_147563 = (ref_145739 & 0xFF) # MOVZX operation
ref_147565 = (ref_147563 & 0xFF) # Byte reference - MOV operation
ref_147779 = (ref_143903 & 0xFF) # MOVZX operation
ref_149603 = (ref_147779 & 0xFF) # MOVZX operation
ref_149605 = (ref_149603 & 0xFF) # Byte reference - MOV operation
ref_150833 = ((((((((ref_147565) << 8 | ref_141858) << 8 | ref_141859) << 8 | ref_141860) << 8 | ref_141861) << 8 | ref_141862) << 8 | ref_141863) << 8 | ref_149605) # MOV operation
ref_151819 = ((((((((ref_126287) << 8 | ref_120580) << 8 | ref_120581) << 8 | ref_120582) << 8 | ref_120583) << 8 | ref_120584) << 8 | ref_120585) << 8 | ref_128327) # MOV operation
ref_151903 = ref_150833 # MOV operation
ref_151907 = ref_151819 # MOV operation
ref_151909 = (ref_151907 & ref_151903) # AND operation
ref_152134 = ref_151909 # MOV operation
ref_152140 = (0x1F & ref_152134) # AND operation
ref_152365 = ref_152140 # MOV operation
ref_152373 = ((ref_152365 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_152380 = ref_152373 # MOV operation
ref_153298 = ref_133041 # MOV operation
ref_153374 = ref_153298 # MOV operation
ref_153386 = ref_152380 # MOV operation
ref_153388 = (ref_153386 | ref_153374) # OR operation
ref_154319 = ref_153388 # MOV operation
ref_156703 = ref_154319 # MOV operation
ref_157717 = ref_101290 # MOV operation
ref_157917 = ref_157717 # MOV operation
ref_157925 = (ref_157917 >> (0x1 & 0x3F)) # SHR operation
ref_157932 = ref_157925 # MOV operation
ref_158152 = ref_157932 # MOV operation
ref_158158 = (0xF & ref_158152) # AND operation
ref_158259 = ref_158158 # MOV operation
ref_158273 = (0x1 | ref_158259) # OR operation
ref_158502 = ref_158273 # MOV operation
ref_158504 = ((0x40 - ref_158502) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_158512 = ref_158504 # MOV operation
ref_158616 = ref_156703 # MOV operation
ref_158620 = ref_158512 # MOV operation
ref_158622 = (ref_158620 & 0xFFFFFFFF) # MOV operation
ref_158624 = ((ref_158616 << ((ref_158622 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_158631 = ref_158624 # MOV operation
ref_159549 = ref_154319 # MOV operation
ref_160563 = ref_101290 # MOV operation
ref_160763 = ref_160563 # MOV operation
ref_160771 = (ref_160763 >> (0x1 & 0x3F)) # SHR operation
ref_160778 = ref_160771 # MOV operation
ref_160998 = ref_160778 # MOV operation
ref_161004 = (0xF & ref_160998) # AND operation
ref_161105 = ref_161004 # MOV operation
ref_161119 = (0x1 | ref_161105) # OR operation
ref_161228 = ref_159549 # MOV operation
ref_161232 = ref_161119 # MOV operation
ref_161234 = (ref_161232 & 0xFFFFFFFF) # MOV operation
ref_161236 = (ref_161228 >> ((ref_161234 & 0xFF) & 0x3F)) # SHR operation
ref_161243 = ref_161236 # MOV operation
ref_161339 = ref_161243 # MOV operation
ref_161351 = ref_158631 # MOV operation
ref_161353 = (ref_161351 | ref_161339) # OR operation
ref_162392 = ((((((((ref_147565) << 8 | ref_141858) << 8 | ref_141859) << 8 | ref_141860) << 8 | ref_141861) << 8 | ref_141862) << 8 | ref_141863) << 8 | ref_149605) # MOV operation
ref_163290 = ((((((((ref_126287) << 8 | ref_120580) << 8 | ref_120581) << 8 | ref_120582) << 8 | ref_120583) << 8 | ref_120584) << 8 | ref_120585) << 8 | ref_128327) # MOV operation
ref_163366 = ref_163290 # MOV operation
ref_163378 = ref_162392 # MOV operation
ref_163380 = (ref_163378 | ref_163366) # OR operation
ref_163605 = ref_163380 # MOV operation
ref_163611 = (0xF & ref_163605) # AND operation
ref_163712 = ref_163611 # MOV operation
ref_163726 = (0x1 | ref_163712) # OR operation
ref_163955 = ref_163726 # MOV operation
ref_163957 = ((0x40 - ref_163955) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_163965 = ref_163957 # MOV operation
ref_164069 = ref_161353 # MOV operation
ref_164073 = ref_163965 # MOV operation
ref_164075 = (ref_164073 & 0xFFFFFFFF) # MOV operation
ref_164077 = (ref_164069 >> ((ref_164075 & 0xFF) & 0x3F)) # SHR operation
ref_164084 = ref_164077 # MOV operation
ref_165002 = ref_154319 # MOV operation
ref_166016 = ref_101290 # MOV operation
ref_166216 = ref_166016 # MOV operation
ref_166224 = (ref_166216 >> (0x1 & 0x3F)) # SHR operation
ref_166231 = ref_166224 # MOV operation
ref_166451 = ref_166231 # MOV operation
ref_166457 = (0xF & ref_166451) # AND operation
ref_166558 = ref_166457 # MOV operation
ref_166572 = (0x1 | ref_166558) # OR operation
ref_166801 = ref_166572 # MOV operation
ref_166803 = ((0x40 - ref_166801) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_166811 = ref_166803 # MOV operation
ref_166915 = ref_165002 # MOV operation
ref_166919 = ref_166811 # MOV operation
ref_166921 = (ref_166919 & 0xFFFFFFFF) # MOV operation
ref_166923 = ((ref_166915 << ((ref_166921 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_166930 = ref_166923 # MOV operation
ref_167848 = ref_154319 # MOV operation
ref_168862 = ref_101290 # MOV operation
ref_169062 = ref_168862 # MOV operation
ref_169070 = (ref_169062 >> (0x1 & 0x3F)) # SHR operation
ref_169077 = ref_169070 # MOV operation
ref_169297 = ref_169077 # MOV operation
ref_169303 = (0xF & ref_169297) # AND operation
ref_169404 = ref_169303 # MOV operation
ref_169418 = (0x1 | ref_169404) # OR operation
ref_169527 = ref_167848 # MOV operation
ref_169531 = ref_169418 # MOV operation
ref_169533 = (ref_169531 & 0xFFFFFFFF) # MOV operation
ref_169535 = (ref_169527 >> ((ref_169533 & 0xFF) & 0x3F)) # SHR operation
ref_169542 = ref_169535 # MOV operation
ref_169638 = ref_169542 # MOV operation
ref_169650 = ref_166930 # MOV operation
ref_169652 = (ref_169650 | ref_169638) # OR operation
ref_170691 = ((((((((ref_147565) << 8 | ref_141858) << 8 | ref_141859) << 8 | ref_141860) << 8 | ref_141861) << 8 | ref_141862) << 8 | ref_141863) << 8 | ref_149605) # MOV operation
ref_171589 = ((((((((ref_126287) << 8 | ref_120580) << 8 | ref_120581) << 8 | ref_120582) << 8 | ref_120583) << 8 | ref_120584) << 8 | ref_120585) << 8 | ref_128327) # MOV operation
ref_171665 = ref_171589 # MOV operation
ref_171677 = ref_170691 # MOV operation
ref_171679 = (ref_171677 | ref_171665) # OR operation
ref_171904 = ref_171679 # MOV operation
ref_171910 = (0xF & ref_171904) # AND operation
ref_172011 = ref_171910 # MOV operation
ref_172025 = (0x1 | ref_172011) # OR operation
ref_172134 = ref_169652 # MOV operation
ref_172138 = ref_172025 # MOV operation
ref_172140 = (ref_172138 & 0xFFFFFFFF) # MOV operation
ref_172142 = ((ref_172134 << ((ref_172140 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_172149 = ref_172142 # MOV operation
ref_172245 = ref_172149 # MOV operation
ref_172257 = ref_164084 # MOV operation
ref_172259 = (ref_172257 | ref_172245) # OR operation
ref_173114 = ref_172259 # MOV operation
ref_173325 = ref_173114 # MOV operation
ref_173327 = ref_173325 # MOV operation

print ref_173327 & 0xffffffffffffffff
