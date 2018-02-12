#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_10839 = ref_278 # MOV operation
ref_11599 = ref_10839 # MOV operation
ref_11609 = (ref_11599 >> (0x35 & 0x3F)) # SHR operation
ref_11616 = ref_11609 # MOV operation
ref_14751 = ref_278 # MOV operation
ref_15551 = ref_14751 # MOV operation
ref_15561 = ((ref_15551 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_15568 = ref_15561 # MOV operation
ref_15978 = ref_15568 # MOV operation
ref_15992 = ref_11616 # MOV operation
ref_15994 = (ref_15992 | ref_15978) # OR operation
ref_16795 = ref_15994 # MOV operation
ref_16805 = (ref_16795 >> (0x1 & 0x3F)) # SHR operation
ref_16812 = ref_16805 # MOV operation
ref_17234 = ref_16812 # MOV operation
ref_23789 = ref_278 # MOV operation
ref_24153 = ref_23789 # MOV operation
ref_24171 = ((((0x0) << 64 | ref_24153) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_27916 = ref_17234 # MOV operation
ref_28226 = ref_27916 # MOV operation
ref_28242 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_28226)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_28638 = ref_24171 # MOV operation
ref_28644 = ref_28242 # MOV operation
ref_28646 = ((ref_28638 - ref_28644) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_28654 = ref_28646 # MOV operation
ref_29079 = ref_28654 # MOV operation
ref_35644 = ref_278 # MOV operation
ref_35989 = ref_35644 # MOV operation
ref_36005 = ((0x9919884 + ref_35989) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_39749 = ref_29079 # MOV operation
ref_40531 = ref_39749 # MOV operation
ref_40541 = (ref_40531 >> (0x7 & 0x3F)) # SHR operation
ref_40548 = ref_40541 # MOV operation
ref_41410 = ref_40548 # MOV operation
ref_41420 = (ref_41410 >> (0x2 & 0x3F)) # SHR operation
ref_41427 = ref_41420 # MOV operation
ref_42222 = ref_41427 # MOV operation
ref_42230 = (0x7 & ref_42222) # AND operation
ref_42656 = ref_42230 # MOV operation
ref_42672 = (0x1 | ref_42656) # OR operation
ref_43055 = ref_36005 # MOV operation
ref_43061 = ref_42672 # MOV operation
ref_43063 = (ref_43061 & 0xFFFFFFFF) # MOV operation
ref_43065 = (ref_43055 >> ((ref_43063 & 0xFF) & 0x3F)) # SHR operation
ref_43072 = ref_43065 # MOV operation
ref_43497 = ref_43072 # MOV operation
ref_49993 = ref_278 # MOV operation
ref_50407 = ref_49993 # MOV operation
ref_50423 = ((0x1E5EA08F8 + ref_50407) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_50813 = ref_50423 # MOV operation
ref_63163 = ref_43497 # MOV operation
ref_63986 = ref_63163 # MOV operation
ref_63994 = (0x3F & ref_63986) # AND operation
ref_64823 = ref_63994 # MOV operation
ref_64833 = ((ref_64823 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_64840 = ref_64833 # MOV operation
ref_69314 = ref_43497 # MOV operation
ref_69676 = ref_69314 # MOV operation
ref_69690 = ref_64840 # MOV operation
ref_69692 = (ref_69690 | ref_69676) # OR operation
ref_70137 = ref_69692 # MOV operation
ref_81958 = ref_17234 # MOV operation
ref_86143 = ref_29079 # MOV operation
ref_86883 = ref_86143 # MOV operation
ref_86893 = (ref_86883 >> (0x2 & 0x3F)) # SHR operation
ref_86900 = ref_86893 # MOV operation
ref_87733 = ref_86900 # MOV operation
ref_87741 = (0xF & ref_87733) # AND operation
ref_88138 = ref_87741 # MOV operation
ref_88154 = (0x1 | ref_88138) # OR operation
ref_88553 = ref_88154 # MOV operation
ref_88555 = ((0x40 - ref_88553) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_88563 = ref_88555 # MOV operation
ref_88986 = ref_81958 # MOV operation
ref_88992 = ref_88563 # MOV operation
ref_88994 = (ref_88992 & 0xFFFFFFFF) # MOV operation
ref_88996 = (ref_88986 >> ((ref_88994 & 0xFF) & 0x3F)) # SHR operation
ref_89003 = ref_88996 # MOV operation
ref_92278 = ref_17234 # MOV operation
ref_96058 = ref_29079 # MOV operation
ref_96853 = ref_96058 # MOV operation
ref_96863 = (ref_96853 >> (0x2 & 0x3F)) # SHR operation
ref_96870 = ref_96863 # MOV operation
ref_97684 = ref_96870 # MOV operation
ref_97692 = (0xF & ref_97684) # AND operation
ref_98083 = ref_97692 # MOV operation
ref_98099 = (0x1 | ref_98083) # OR operation
ref_98486 = ref_92278 # MOV operation
ref_98492 = ref_98099 # MOV operation
ref_98494 = (ref_98492 & 0xFFFFFFFF) # MOV operation
ref_98496 = ((ref_98486 << ((ref_98494 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_98503 = ref_98496 # MOV operation
ref_98889 = ref_98503 # MOV operation
ref_98903 = ref_89003 # MOV operation
ref_98905 = (ref_98903 | ref_98889) # OR operation
ref_99698 = ref_98905 # MOV operation
ref_99706 = (0x7 & ref_99698) # AND operation
ref_100499 = ref_99706 # MOV operation
ref_100509 = ((ref_100499 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_100516 = ref_100509 # MOV operation
ref_103719 = ref_70137 # MOV operation
ref_104117 = ref_103719 # MOV operation
ref_104131 = ref_100516 # MOV operation
ref_104133 = (ref_104131 | ref_104117) # OR operation
ref_104528 = ref_104133 # MOV operation
ref_108197 = ref_17234 # MOV operation
ref_112237 = ref_29079 # MOV operation
ref_113075 = ref_112237 # MOV operation
ref_113085 = (ref_113075 >> (0x3 & 0x3F)) # SHR operation
ref_113092 = ref_113085 # MOV operation
ref_113888 = ref_113092 # MOV operation
ref_113896 = (0xF & ref_113888) # AND operation
ref_114277 = ref_113896 # MOV operation
ref_114293 = (0x1 | ref_114277) # OR operation
ref_114732 = ref_114293 # MOV operation
ref_114734 = ((0x40 - ref_114732) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_114742 = ref_114734 # MOV operation
ref_115146 = ref_108197 # MOV operation
ref_115152 = ref_114742 # MOV operation
ref_115154 = (ref_115152 & 0xFFFFFFFF) # MOV operation
ref_115156 = ((ref_115146 << ((ref_115154 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_115163 = ref_115156 # MOV operation
ref_118514 = ref_17234 # MOV operation
ref_122154 = ref_29079 # MOV operation
ref_122927 = ref_122154 # MOV operation
ref_122937 = (ref_122927 >> (0x3 & 0x3F)) # SHR operation
ref_122944 = ref_122937 # MOV operation
ref_123794 = ref_122944 # MOV operation
ref_123802 = (0xF & ref_123794) # AND operation
ref_124177 = ref_123802 # MOV operation
ref_124193 = (0x1 | ref_124177) # OR operation
ref_124596 = ref_118514 # MOV operation
ref_124602 = ref_124193 # MOV operation
ref_124604 = (ref_124602 & 0xFFFFFFFF) # MOV operation
ref_124606 = (ref_124596 >> ((ref_124604 & 0xFF) & 0x3F)) # SHR operation
ref_124613 = ref_124606 # MOV operation
ref_125032 = ref_124613 # MOV operation
ref_125046 = ref_115163 # MOV operation
ref_125048 = (ref_125046 | ref_125032) # OR operation
ref_128419 = ref_104528 # MOV operation
ref_132442 = ref_50813 # MOV operation
ref_133245 = ref_132442 # MOV operation
ref_133255 = (ref_133245 >> (0x4 & 0x3F)) # SHR operation
ref_133262 = ref_133255 # MOV operation
ref_134088 = ref_133262 # MOV operation
ref_134096 = (0xF & ref_134088) # AND operation
ref_134518 = ref_134096 # MOV operation
ref_134534 = (0x1 | ref_134518) # OR operation
ref_134920 = ref_134534 # MOV operation
ref_134922 = ((0x40 - ref_134920) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_134930 = ref_134922 # MOV operation
ref_135348 = ref_128419 # MOV operation
ref_135354 = ref_134930 # MOV operation
ref_135356 = (ref_135354 & 0xFFFFFFFF) # MOV operation
ref_135358 = ((ref_135348 << ((ref_135356 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_135365 = ref_135358 # MOV operation
ref_138710 = ref_104528 # MOV operation
ref_142397 = ref_50813 # MOV operation
ref_143162 = ref_142397 # MOV operation
ref_143172 = (ref_143162 >> (0x4 & 0x3F)) # SHR operation
ref_143179 = ref_143172 # MOV operation
ref_144000 = ref_143179 # MOV operation
ref_144008 = (0xF & ref_144000) # AND operation
ref_144383 = ref_144008 # MOV operation
ref_144399 = (0x1 | ref_144383) # OR operation
ref_144829 = ref_138710 # MOV operation
ref_144835 = ref_144399 # MOV operation
ref_144837 = (ref_144835 & 0xFFFFFFFF) # MOV operation
ref_144839 = (ref_144829 >> ((ref_144837 & 0xFF) & 0x3F)) # SHR operation
ref_144846 = ref_144839 # MOV operation
ref_145263 = ref_144846 # MOV operation
ref_145277 = ref_135365 # MOV operation
ref_145279 = (ref_145277 | ref_145263) # OR operation
ref_145660 = ref_125048 # MOV operation
ref_145666 = ref_145279 # MOV operation
ref_145668 = ((ref_145660 - ref_145666) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_145670 = ((((ref_145660 ^ (ref_145666 ^ ref_145668)) ^ ((ref_145660 ^ ref_145668) & (ref_145660 ^ ref_145666))) >> 63) & 0x1) # Carry flag
ref_145674 = (0x1 if (ref_145668 == 0x0) else 0x0) # Zero flag
ref_145676 = ((((ref_145666 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (((~(ref_145670) & 0x1) & (~(ref_145674) & 0x1)) == 0x1) else 0x0)) # SETA operation
ref_145678 = (ref_145676 & 0xFF) # MOVZX operation
ref_146062 = (ref_145678 & 0xFFFFFFFF) # MOV operation
ref_146064 = ((ref_146062 & 0xFFFFFFFF) & (ref_146062 & 0xFFFFFFFF)) # TEST operation
ref_146069 = (0x1 if (ref_146064 == 0x0) else 0x0) # Zero flag
ref_146071 = (0x2C30 if (ref_146069 == 0x1) else 0x2C06) # Program Counter


if (ref_146069 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_10839 = ref_278 # MOV operation
    ref_11599 = ref_10839 # MOV operation
    ref_11609 = (ref_11599 >> (0x35 & 0x3F)) # SHR operation
    ref_11616 = ref_11609 # MOV operation
    ref_14751 = ref_278 # MOV operation
    ref_15551 = ref_14751 # MOV operation
    ref_15561 = ((ref_15551 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_15568 = ref_15561 # MOV operation
    ref_15978 = ref_15568 # MOV operation
    ref_15992 = ref_11616 # MOV operation
    ref_15994 = (ref_15992 | ref_15978) # OR operation
    ref_16795 = ref_15994 # MOV operation
    ref_16805 = (ref_16795 >> (0x1 & 0x3F)) # SHR operation
    ref_16812 = ref_16805 # MOV operation
    ref_17234 = ref_16812 # MOV operation
    ref_23789 = ref_278 # MOV operation
    ref_24153 = ref_23789 # MOV operation
    ref_24171 = ((((0x0) << 64 | ref_24153) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_27916 = ref_17234 # MOV operation
    ref_28226 = ref_27916 # MOV operation
    ref_28242 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_28226)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_28638 = ref_24171 # MOV operation
    ref_28644 = ref_28242 # MOV operation
    ref_28646 = ((ref_28638 - ref_28644) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_28654 = ref_28646 # MOV operation
    ref_29079 = ref_28654 # MOV operation
    ref_35644 = ref_278 # MOV operation
    ref_35989 = ref_35644 # MOV operation
    ref_36005 = ((0x9919884 + ref_35989) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_39749 = ref_29079 # MOV operation
    ref_40531 = ref_39749 # MOV operation
    ref_40541 = (ref_40531 >> (0x7 & 0x3F)) # SHR operation
    ref_40548 = ref_40541 # MOV operation
    ref_41410 = ref_40548 # MOV operation
    ref_41420 = (ref_41410 >> (0x2 & 0x3F)) # SHR operation
    ref_41427 = ref_41420 # MOV operation
    ref_42222 = ref_41427 # MOV operation
    ref_42230 = (0x7 & ref_42222) # AND operation
    ref_42656 = ref_42230 # MOV operation
    ref_42672 = (0x1 | ref_42656) # OR operation
    ref_43055 = ref_36005 # MOV operation
    ref_43061 = ref_42672 # MOV operation
    ref_43063 = (ref_43061 & 0xFFFFFFFF) # MOV operation
    ref_43065 = (ref_43055 >> ((ref_43063 & 0xFF) & 0x3F)) # SHR operation
    ref_43072 = ref_43065 # MOV operation
    ref_43497 = ref_43072 # MOV operation
    ref_49993 = ref_278 # MOV operation
    ref_50407 = ref_49993 # MOV operation
    ref_50423 = ((0x1E5EA08F8 + ref_50407) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_50813 = ref_50423 # MOV operation
    ref_63163 = ref_43497 # MOV operation
    ref_63986 = ref_63163 # MOV operation
    ref_63994 = (0x3F & ref_63986) # AND operation
    ref_64823 = ref_63994 # MOV operation
    ref_64833 = ((ref_64823 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_64840 = ref_64833 # MOV operation
    ref_69314 = ref_43497 # MOV operation
    ref_69676 = ref_69314 # MOV operation
    ref_69690 = ref_64840 # MOV operation
    ref_69692 = (ref_69690 | ref_69676) # OR operation
    ref_70137 = ref_69692 # MOV operation
    ref_81958 = ref_17234 # MOV operation
    ref_86143 = ref_29079 # MOV operation
    ref_86883 = ref_86143 # MOV operation
    ref_86893 = (ref_86883 >> (0x2 & 0x3F)) # SHR operation
    ref_86900 = ref_86893 # MOV operation
    ref_87733 = ref_86900 # MOV operation
    ref_87741 = (0xF & ref_87733) # AND operation
    ref_88138 = ref_87741 # MOV operation
    ref_88154 = (0x1 | ref_88138) # OR operation
    ref_88553 = ref_88154 # MOV operation
    ref_88555 = ((0x40 - ref_88553) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_88563 = ref_88555 # MOV operation
    ref_88986 = ref_81958 # MOV operation
    ref_88992 = ref_88563 # MOV operation
    ref_88994 = (ref_88992 & 0xFFFFFFFF) # MOV operation
    ref_88996 = (ref_88986 >> ((ref_88994 & 0xFF) & 0x3F)) # SHR operation
    ref_89003 = ref_88996 # MOV operation
    ref_92278 = ref_17234 # MOV operation
    ref_96058 = ref_29079 # MOV operation
    ref_96853 = ref_96058 # MOV operation
    ref_96863 = (ref_96853 >> (0x2 & 0x3F)) # SHR operation
    ref_96870 = ref_96863 # MOV operation
    ref_97684 = ref_96870 # MOV operation
    ref_97692 = (0xF & ref_97684) # AND operation
    ref_98083 = ref_97692 # MOV operation
    ref_98099 = (0x1 | ref_98083) # OR operation
    ref_98486 = ref_92278 # MOV operation
    ref_98492 = ref_98099 # MOV operation
    ref_98494 = (ref_98492 & 0xFFFFFFFF) # MOV operation
    ref_98496 = ((ref_98486 << ((ref_98494 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_98503 = ref_98496 # MOV operation
    ref_98889 = ref_98503 # MOV operation
    ref_98903 = ref_89003 # MOV operation
    ref_98905 = (ref_98903 | ref_98889) # OR operation
    ref_99698 = ref_98905 # MOV operation
    ref_99706 = (0x7 & ref_99698) # AND operation
    ref_100499 = ref_99706 # MOV operation
    ref_100509 = ((ref_100499 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_100516 = ref_100509 # MOV operation
    ref_103719 = ref_70137 # MOV operation
    ref_104117 = ref_103719 # MOV operation
    ref_104131 = ref_100516 # MOV operation
    ref_104133 = (ref_104131 | ref_104117) # OR operation
    ref_104528 = ref_104133 # MOV operation
    ref_152706 = ref_29079 # MOV operation
    ref_153478 = ref_152706 # MOV operation
    ref_153486 = (0xF & ref_153478) # AND operation
    ref_154340 = ref_153486 # MOV operation
    ref_154350 = ((ref_154340 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_154357 = ref_154350 # MOV operation
    ref_157652 = ref_29079 # MOV operation
    ref_158030 = ref_157652 # MOV operation
    ref_158044 = ref_154357 # MOV operation
    ref_158046 = (ref_158044 | ref_158030) # OR operation
    ref_158474 = ref_158046 # MOV operation
    ref_164640 = ref_104528 # MOV operation
    ref_167942 = ref_158474 # MOV operation
    ref_168344 = ref_164640 # MOV operation
    ref_168350 = ref_167942 # MOV operation
    ref_168352 = (ref_168350 & ref_168344) # AND operation
    ref_169185 = ref_168352 # MOV operation
    ref_169193 = (0x1F & ref_169185) # AND operation
    ref_169988 = ref_169193 # MOV operation
    ref_169998 = ((ref_169988 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_170005 = ref_169998 # MOV operation
    ref_173355 = ref_17234 # MOV operation
    ref_173687 = ref_173355 # MOV operation
    ref_173701 = ref_170005 # MOV operation
    ref_173703 = (ref_173701 | ref_173687) # OR operation
    ref_174093 = ref_173703 # MOV operation
    ref_180614 = ref_50813 # MOV operation
    ref_183976 = ref_104528 # MOV operation
    ref_184364 = ref_183976 # MOV operation
    ref_184378 = ref_180614 # MOV operation
    ref_184380 = (((sx(0x40, ref_184378) * sx(0x40, ref_184364)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_187625 = ref_158474 # MOV operation
    ref_190985 = ref_174093 # MOV operation
    ref_191317 = ref_190985 # MOV operation
    ref_191331 = ref_187625 # MOV operation
    ref_191333 = (ref_191331 | ref_191317) # OR operation
    ref_191698 = ref_191333 # MOV operation
    ref_191712 = ref_184380 # MOV operation
    ref_191714 = (((sx(0x40, ref_191712) * sx(0x40, ref_191698)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_192181 = ref_191714 # MOV operation
    ref_192975 = ref_192181 # MOV operation
    ref_192977 = ref_192975 # MOV operation
    endb = ref_192977


else:
    ref_193297 = SymVar_0
    ref_193312 = ref_193297 # MOV operation
    ref_203498 = ref_193312 # MOV operation
    ref_204298 = ref_203498 # MOV operation
    ref_204308 = (ref_204298 >> (0x35 & 0x3F)) # SHR operation
    ref_204315 = ref_204308 # MOV operation
    ref_207569 = ref_193312 # MOV operation
    ref_208346 = ref_207569 # MOV operation
    ref_208356 = ((ref_208346 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_208363 = ref_208356 # MOV operation
    ref_208779 = ref_208363 # MOV operation
    ref_208793 = ref_204315 # MOV operation
    ref_208795 = (ref_208793 | ref_208779) # OR operation
    ref_209588 = ref_208795 # MOV operation
    ref_209598 = (ref_209588 >> (0x1 & 0x3F)) # SHR operation
    ref_209605 = ref_209598 # MOV operation
    ref_210034 = ref_209605 # MOV operation
    ref_216588 = ref_193312 # MOV operation
    ref_216898 = ref_216588 # MOV operation
    ref_216916 = ((((0x0) << 64 | ref_216898) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_220713 = ref_210034 # MOV operation
    ref_221069 = ref_220713 # MOV operation
    ref_221085 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_221069)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_221507 = ref_216916 # MOV operation
    ref_221513 = ref_221085 # MOV operation
    ref_221515 = ((ref_221507 - ref_221513) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_221523 = ref_221515 # MOV operation
    ref_221943 = ref_221523 # MOV operation
    ref_228418 = ref_193312 # MOV operation
    ref_228776 = ref_228418 # MOV operation
    ref_228792 = ((0x9919884 + ref_228776) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_232607 = ref_221943 # MOV operation
    ref_233331 = ref_232607 # MOV operation
    ref_233341 = (ref_233331 >> (0x7 & 0x3F)) # SHR operation
    ref_233348 = ref_233341 # MOV operation
    ref_234171 = ref_233348 # MOV operation
    ref_234181 = (ref_234171 >> (0x2 & 0x3F)) # SHR operation
    ref_234188 = ref_234181 # MOV operation
    ref_235012 = ref_234188 # MOV operation
    ref_235020 = (0x7 & ref_235012) # AND operation
    ref_235388 = ref_235020 # MOV operation
    ref_235404 = (0x1 | ref_235388) # OR operation
    ref_235816 = ref_228792 # MOV operation
    ref_235822 = ref_235404 # MOV operation
    ref_235824 = (ref_235822 & 0xFFFFFFFF) # MOV operation
    ref_235826 = (ref_235816 >> ((ref_235824 & 0xFF) & 0x3F)) # SHR operation
    ref_235833 = ref_235826 # MOV operation
    ref_236249 = ref_235833 # MOV operation
    ref_242856 = ref_193312 # MOV operation
    ref_243255 = ref_242856 # MOV operation
    ref_243271 = ((0x1E5EA08F8 + ref_243255) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_243645 = ref_243271 # MOV operation
    ref_255951 = ref_236249 # MOV operation
    ref_256691 = ref_255951 # MOV operation
    ref_256699 = (0x3F & ref_256691) # AND operation
    ref_257541 = ref_256699 # MOV operation
    ref_257551 = ((ref_257541 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_257558 = ref_257551 # MOV operation
    ref_262124 = ref_236249 # MOV operation
    ref_262466 = ref_262124 # MOV operation
    ref_262480 = ref_257558 # MOV operation
    ref_262482 = (ref_262480 | ref_262466) # OR operation
    ref_262888 = ref_262482 # MOV operation
    ref_274816 = ref_210034 # MOV operation
    ref_278879 = ref_221943 # MOV operation
    ref_279691 = ref_278879 # MOV operation
    ref_279701 = (ref_279691 >> (0x2 & 0x3F)) # SHR operation
    ref_279708 = ref_279701 # MOV operation
    ref_280517 = ref_279708 # MOV operation
    ref_280525 = (0xF & ref_280517) # AND operation
    ref_280899 = ref_280525 # MOV operation
    ref_280915 = (0x1 | ref_280899) # OR operation
    ref_281344 = ref_280915 # MOV operation
    ref_281346 = ((0x40 - ref_281344) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_281354 = ref_281346 # MOV operation
    ref_281738 = ref_274816 # MOV operation
    ref_281744 = ref_281354 # MOV operation
    ref_281746 = (ref_281744 & 0xFFFFFFFF) # MOV operation
    ref_281748 = (ref_281738 >> ((ref_281746 & 0xFF) & 0x3F)) # SHR operation
    ref_281755 = ref_281748 # MOV operation
    ref_285119 = ref_210034 # MOV operation
    ref_288736 = ref_221943 # MOV operation
    ref_289558 = ref_288736 # MOV operation
    ref_289568 = (ref_289558 >> (0x2 & 0x3F)) # SHR operation
    ref_289575 = ref_289568 # MOV operation
    ref_290363 = ref_289575 # MOV operation
    ref_290371 = (0xF & ref_290363) # AND operation
    ref_290800 = ref_290371 # MOV operation
    ref_290816 = (0x1 | ref_290800) # OR operation
    ref_291251 = ref_285119 # MOV operation
    ref_291257 = ref_290816 # MOV operation
    ref_291259 = (ref_291257 & 0xFFFFFFFF) # MOV operation
    ref_291261 = ((ref_291251 << ((ref_291259 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_291268 = ref_291261 # MOV operation
    ref_291596 = ref_291268 # MOV operation
    ref_291610 = ref_281755 # MOV operation
    ref_291612 = (ref_291610 | ref_291596) # OR operation
    ref_292447 = ref_291612 # MOV operation
    ref_292455 = (0x7 & ref_292447) # AND operation
    ref_293290 = ref_292455 # MOV operation
    ref_293300 = ((ref_293290 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_293307 = ref_293300 # MOV operation
    ref_296670 = ref_262888 # MOV operation
    ref_296976 = ref_296670 # MOV operation
    ref_296990 = ref_293307 # MOV operation
    ref_296992 = (ref_296990 | ref_296976) # OR operation
    ref_297397 = ref_296992 # MOV operation
    ref_297399 = ((ref_297397 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_297400 = ((ref_297397 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_297401 = ((ref_297397 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_297402 = ((ref_297397 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_297403 = ((ref_297397 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_297404 = ((ref_297397 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_297405 = ((ref_297397 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_297406 = (ref_297397 & 0xFF) # Byte reference - MOV operation
    ref_344870 = ref_243645 # MOV operation
    ref_349001 = ref_243645 # MOV operation
    ref_349844 = ref_349001 # MOV operation
    ref_349854 = (ref_349844 >> (0x3 & 0x3F)) # SHR operation
    ref_349861 = ref_349854 # MOV operation
    ref_350629 = ref_349861 # MOV operation
    ref_350637 = (0xF & ref_350629) # AND operation
    ref_351053 = ref_350637 # MOV operation
    ref_351069 = (0x1 | ref_351053) # OR operation
    ref_351438 = ref_351069 # MOV operation
    ref_351440 = ((0x40 - ref_351438) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_351448 = ref_351440 # MOV operation
    ref_351820 = ref_344870 # MOV operation
    ref_351826 = ref_351448 # MOV operation
    ref_351828 = (ref_351826 & 0xFFFFFFFF) # MOV operation
    ref_351830 = (ref_351820 >> ((ref_351828 & 0xFF) & 0x3F)) # SHR operation
    ref_351837 = ref_351830 # MOV operation
    ref_355183 = ref_243645 # MOV operation
    ref_358789 = ref_243645 # MOV operation
    ref_359636 = ref_358789 # MOV operation
    ref_359646 = (ref_359636 >> (0x3 & 0x3F)) # SHR operation
    ref_359653 = ref_359646 # MOV operation
    ref_360471 = ref_359653 # MOV operation
    ref_360479 = (0xF & ref_360471) # AND operation
    ref_360856 = ref_360479 # MOV operation
    ref_360872 = (0x1 | ref_360856) # OR operation
    ref_361271 = ref_355183 # MOV operation
    ref_361277 = ref_360872 # MOV operation
    ref_361279 = (ref_361277 & 0xFFFFFFFF) # MOV operation
    ref_361281 = ((ref_361271 << ((ref_361279 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_361288 = ref_361281 # MOV operation
    ref_361662 = ref_361288 # MOV operation
    ref_361676 = ref_351837 # MOV operation
    ref_361678 = (ref_361676 | ref_361662) # OR operation
    ref_362077 = ref_361678 # MOV operation
    ref_368189 = ref_297405 # MOVZX operation
    ref_368547 = (ref_368189 & 0xFF) # MOVZX operation
    ref_379419 = ref_297403 # MOVZX operation
    ref_379799 = (ref_379419 & 0xFF) # MOVZX operation
    ref_379801 = (ref_379799 & 0xFF) # Byte reference - MOV operation
    ref_385860 = (ref_368547 & 0xFF) # MOVZX operation
    ref_386250 = (ref_385860 & 0xFF) # MOVZX operation
    ref_386252 = (ref_386250 & 0xFF) # Byte reference - MOV operation
    ref_392730 = ref_243645 # MOV operation
    ref_395973 = ((((((((ref_297399) << 8 | ref_297400) << 8 | ref_297401) << 8 | ref_297402) << 8 | ref_386252) << 8 | ref_297404) << 8 | ref_379801) << 8 | ref_297406) # MOV operation
    ref_396341 = ref_395973 # MOV operation
    ref_396355 = ref_392730 # MOV operation
    ref_396357 = (((sx(0x40, ref_396355) * sx(0x40, ref_396341)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_399678 = ref_221943 # MOV operation
    ref_402927 = ref_362077 # MOV operation
    ref_403317 = ref_402927 # MOV operation
    ref_403331 = ref_399678 # MOV operation
    ref_403333 = (ref_403331 | ref_403317) # OR operation
    ref_403702 = ref_403333 # MOV operation
    ref_403716 = ref_396357 # MOV operation
    ref_403718 = (((sx(0x40, ref_403716) * sx(0x40, ref_403702)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_404118 = ref_403718 # MOV operation
    ref_404938 = ref_404118 # MOV operation
    ref_404940 = ref_404938 # MOV operation
    endb = ref_404940


print endb & 0xffffffffffffffff
