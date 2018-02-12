#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_250 = SymVar_0
ref_261 = ref_250 # MOV operation
ref_273 = ref_261 # MOV operation
ref_275 = ref_273 # MOV operation
ref_309 = ((ref_275 >> 56) & 0xFF) # Byte reference - MOV operation
ref_310 = ((ref_275 >> 48) & 0xFF) # Byte reference - MOV operation
ref_311 = ((ref_275 >> 40) & 0xFF) # Byte reference - MOV operation
ref_312 = ((ref_275 >> 32) & 0xFF) # Byte reference - MOV operation
ref_313 = ((ref_275 >> 24) & 0xFF) # Byte reference - MOV operation
ref_314 = ((ref_275 >> 16) & 0xFF) # Byte reference - MOV operation
ref_315 = ((ref_275 >> 8) & 0xFF) # Byte reference - MOV operation
ref_316 = (ref_275 & 0xFF) # Byte reference - MOV operation
ref_12368 = ref_316 # MOVZX operation
ref_12466 = (ref_12368 & 0xFF) # MOVZX operation
ref_12468 = (ref_12466 & 0xFF) # MOVZX operation
ref_13235 = (ref_12468 & 0xFFFFFFFF) # MOV operation
ref_13237 = (((ref_13235 & 0xFFFFFFFF) + 0x1) & 0xFFFFFFFF) # ADD operation
ref_14064 = (ref_13237 & 0xFFFFFFFF) # MOV operation
ref_14073 = ((((0x0) << 32 | (ref_14064 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_14075 = (ref_14073 & 0xFFFFFFFF) # MOV operation
ref_14369 = (ref_14075 & 0xFFFFFFFF) # MOV operation
ref_15209 = (ref_14369 & 0xFFFFFFFF) # MOV operation
ref_15976 = (ref_15209 & 0xFFFFFFFF) # MOV operation
ref_15978 = (((ref_15976 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_16805 = (ref_15978 & 0xFFFFFFFF) # MOV operation
ref_16814 = ((((0x0) << 32 | (ref_16805 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_16816 = (ref_16814 & 0xFFFFFFFF) # MOV operation
ref_17110 = (ref_16816 & 0xFFFFFFFF) # MOV operation
ref_21896 = ref_315 # MOVZX operation
ref_21994 = (ref_21896 & 0xFF) # MOVZX operation
ref_21996 = (ref_21994 & 0xFF) # MOVZX operation
ref_22512 = (ref_14369 & 0xFFFFFFFF) # MOV operation
ref_22751 = (ref_22512 & 0xFFFFFFFF) # MOV operation
ref_22763 = (ref_21996 & 0xFFFFFFFF) # MOV operation
ref_22765 = (((ref_22763 & 0xFFFFFFFF) + (ref_22751 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_23592 = (ref_22765 & 0xFFFFFFFF) # MOV operation
ref_23601 = ((((0x0) << 32 | (ref_23592 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_23603 = (ref_23601 & 0xFFFFFFFF) # MOV operation
ref_23897 = (ref_23603 & 0xFFFFFFFF) # MOV operation
ref_24737 = (ref_23897 & 0xFFFFFFFF) # MOV operation
ref_25253 = (ref_17110 & 0xFFFFFFFF) # MOV operation
ref_25492 = (ref_25253 & 0xFFFFFFFF) # MOV operation
ref_25504 = (ref_24737 & 0xFFFFFFFF) # MOV operation
ref_25506 = (((ref_25504 & 0xFFFFFFFF) + (ref_25492 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_26333 = (ref_25506 & 0xFFFFFFFF) # MOV operation
ref_26342 = ((((0x0) << 32 | (ref_26333 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_26344 = (ref_26342 & 0xFFFFFFFF) # MOV operation
ref_26638 = (ref_26344 & 0xFFFFFFFF) # MOV operation
ref_31424 = ref_314 # MOVZX operation
ref_31522 = (ref_31424 & 0xFF) # MOVZX operation
ref_31524 = (ref_31522 & 0xFF) # MOVZX operation
ref_32040 = (ref_23897 & 0xFFFFFFFF) # MOV operation
ref_32279 = (ref_32040 & 0xFFFFFFFF) # MOV operation
ref_32291 = (ref_31524 & 0xFFFFFFFF) # MOV operation
ref_32293 = (((ref_32291 & 0xFFFFFFFF) + (ref_32279 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_33120 = (ref_32293 & 0xFFFFFFFF) # MOV operation
ref_33129 = ((((0x0) << 32 | (ref_33120 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_33131 = (ref_33129 & 0xFFFFFFFF) # MOV operation
ref_33425 = (ref_33131 & 0xFFFFFFFF) # MOV operation
ref_34265 = (ref_33425 & 0xFFFFFFFF) # MOV operation
ref_34781 = (ref_26638 & 0xFFFFFFFF) # MOV operation
ref_35020 = (ref_34781 & 0xFFFFFFFF) # MOV operation
ref_35032 = (ref_34265 & 0xFFFFFFFF) # MOV operation
ref_35034 = (((ref_35032 & 0xFFFFFFFF) + (ref_35020 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_35861 = (ref_35034 & 0xFFFFFFFF) # MOV operation
ref_35870 = ((((0x0) << 32 | (ref_35861 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_35872 = (ref_35870 & 0xFFFFFFFF) # MOV operation
ref_36166 = (ref_35872 & 0xFFFFFFFF) # MOV operation
ref_40952 = ref_313 # MOVZX operation
ref_41050 = (ref_40952 & 0xFF) # MOVZX operation
ref_41052 = (ref_41050 & 0xFF) # MOVZX operation
ref_41568 = (ref_33425 & 0xFFFFFFFF) # MOV operation
ref_41807 = (ref_41568 & 0xFFFFFFFF) # MOV operation
ref_41819 = (ref_41052 & 0xFFFFFFFF) # MOV operation
ref_41821 = (((ref_41819 & 0xFFFFFFFF) + (ref_41807 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_42648 = (ref_41821 & 0xFFFFFFFF) # MOV operation
ref_42657 = ((((0x0) << 32 | (ref_42648 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_42659 = (ref_42657 & 0xFFFFFFFF) # MOV operation
ref_42953 = (ref_42659 & 0xFFFFFFFF) # MOV operation
ref_43793 = (ref_42953 & 0xFFFFFFFF) # MOV operation
ref_44309 = (ref_36166 & 0xFFFFFFFF) # MOV operation
ref_44548 = (ref_44309 & 0xFFFFFFFF) # MOV operation
ref_44560 = (ref_43793 & 0xFFFFFFFF) # MOV operation
ref_44562 = (((ref_44560 & 0xFFFFFFFF) + (ref_44548 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_45389 = (ref_44562 & 0xFFFFFFFF) # MOV operation
ref_45398 = ((((0x0) << 32 | (ref_45389 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_45400 = (ref_45398 & 0xFFFFFFFF) # MOV operation
ref_45694 = (ref_45400 & 0xFFFFFFFF) # MOV operation
ref_50480 = ref_312 # MOVZX operation
ref_50578 = (ref_50480 & 0xFF) # MOVZX operation
ref_50580 = (ref_50578 & 0xFF) # MOVZX operation
ref_51096 = (ref_42953 & 0xFFFFFFFF) # MOV operation
ref_51335 = (ref_51096 & 0xFFFFFFFF) # MOV operation
ref_51347 = (ref_50580 & 0xFFFFFFFF) # MOV operation
ref_51349 = (((ref_51347 & 0xFFFFFFFF) + (ref_51335 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_52176 = (ref_51349 & 0xFFFFFFFF) # MOV operation
ref_52185 = ((((0x0) << 32 | (ref_52176 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_52187 = (ref_52185 & 0xFFFFFFFF) # MOV operation
ref_52481 = (ref_52187 & 0xFFFFFFFF) # MOV operation
ref_53321 = (ref_52481 & 0xFFFFFFFF) # MOV operation
ref_53837 = (ref_45694 & 0xFFFFFFFF) # MOV operation
ref_54076 = (ref_53837 & 0xFFFFFFFF) # MOV operation
ref_54088 = (ref_53321 & 0xFFFFFFFF) # MOV operation
ref_54090 = (((ref_54088 & 0xFFFFFFFF) + (ref_54076 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_54917 = (ref_54090 & 0xFFFFFFFF) # MOV operation
ref_54926 = ((((0x0) << 32 | (ref_54917 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_54928 = (ref_54926 & 0xFFFFFFFF) # MOV operation
ref_55222 = (ref_54928 & 0xFFFFFFFF) # MOV operation
ref_60008 = ref_311 # MOVZX operation
ref_60106 = (ref_60008 & 0xFF) # MOVZX operation
ref_60108 = (ref_60106 & 0xFF) # MOVZX operation
ref_60624 = (ref_52481 & 0xFFFFFFFF) # MOV operation
ref_60863 = (ref_60624 & 0xFFFFFFFF) # MOV operation
ref_60875 = (ref_60108 & 0xFFFFFFFF) # MOV operation
ref_60877 = (((ref_60875 & 0xFFFFFFFF) + (ref_60863 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_61704 = (ref_60877 & 0xFFFFFFFF) # MOV operation
ref_61713 = ((((0x0) << 32 | (ref_61704 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_61715 = (ref_61713 & 0xFFFFFFFF) # MOV operation
ref_62009 = (ref_61715 & 0xFFFFFFFF) # MOV operation
ref_62849 = (ref_62009 & 0xFFFFFFFF) # MOV operation
ref_63365 = (ref_55222 & 0xFFFFFFFF) # MOV operation
ref_63604 = (ref_63365 & 0xFFFFFFFF) # MOV operation
ref_63616 = (ref_62849 & 0xFFFFFFFF) # MOV operation
ref_63618 = (((ref_63616 & 0xFFFFFFFF) + (ref_63604 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_64445 = (ref_63618 & 0xFFFFFFFF) # MOV operation
ref_64454 = ((((0x0) << 32 | (ref_64445 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_64456 = (ref_64454 & 0xFFFFFFFF) # MOV operation
ref_64750 = (ref_64456 & 0xFFFFFFFF) # MOV operation
ref_69536 = ref_310 # MOVZX operation
ref_69634 = (ref_69536 & 0xFF) # MOVZX operation
ref_69636 = (ref_69634 & 0xFF) # MOVZX operation
ref_70152 = (ref_62009 & 0xFFFFFFFF) # MOV operation
ref_70391 = (ref_70152 & 0xFFFFFFFF) # MOV operation
ref_70403 = (ref_69636 & 0xFFFFFFFF) # MOV operation
ref_70405 = (((ref_70403 & 0xFFFFFFFF) + (ref_70391 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_71232 = (ref_70405 & 0xFFFFFFFF) # MOV operation
ref_71241 = ((((0x0) << 32 | (ref_71232 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_71243 = (ref_71241 & 0xFFFFFFFF) # MOV operation
ref_71537 = (ref_71243 & 0xFFFFFFFF) # MOV operation
ref_72377 = (ref_71537 & 0xFFFFFFFF) # MOV operation
ref_72893 = (ref_64750 & 0xFFFFFFFF) # MOV operation
ref_73132 = (ref_72893 & 0xFFFFFFFF) # MOV operation
ref_73144 = (ref_72377 & 0xFFFFFFFF) # MOV operation
ref_73146 = (((ref_73144 & 0xFFFFFFFF) + (ref_73132 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_73973 = (ref_73146 & 0xFFFFFFFF) # MOV operation
ref_73982 = ((((0x0) << 32 | (ref_73973 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_73984 = (ref_73982 & 0xFFFFFFFF) # MOV operation
ref_74278 = (ref_73984 & 0xFFFFFFFF) # MOV operation
ref_79064 = ref_309 # MOVZX operation
ref_79162 = (ref_79064 & 0xFF) # MOVZX operation
ref_79164 = (ref_79162 & 0xFF) # MOVZX operation
ref_79680 = (ref_71537 & 0xFFFFFFFF) # MOV operation
ref_79919 = (ref_79680 & 0xFFFFFFFF) # MOV operation
ref_79931 = (ref_79164 & 0xFFFFFFFF) # MOV operation
ref_79933 = (((ref_79931 & 0xFFFFFFFF) + (ref_79919 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_80760 = (ref_79933 & 0xFFFFFFFF) # MOV operation
ref_80769 = ((((0x0) << 32 | (ref_80760 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_80771 = (ref_80769 & 0xFFFFFFFF) # MOV operation
ref_81065 = (ref_80771 & 0xFFFFFFFF) # MOV operation
ref_81905 = (ref_81065 & 0xFFFFFFFF) # MOV operation
ref_82421 = (ref_74278 & 0xFFFFFFFF) # MOV operation
ref_82660 = (ref_82421 & 0xFFFFFFFF) # MOV operation
ref_82672 = (ref_81905 & 0xFFFFFFFF) # MOV operation
ref_82674 = (((ref_82672 & 0xFFFFFFFF) + (ref_82660 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_83501 = (ref_82674 & 0xFFFFFFFF) # MOV operation
ref_83510 = ((((0x0) << 32 | (ref_83501 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_83512 = (ref_83510 & 0xFFFFFFFF) # MOV operation
ref_83806 = (ref_83512 & 0xFFFFFFFF) # MOV operation
ref_87787 = (ref_83806 & 0xFFFFFFFF) # MOV operation
ref_88079 = (ref_87787 & 0xFFFFFFFF) # MOV operation
ref_88087 = (((ref_88079 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_88094 = (ref_88087 & 0xFFFFFFFF) # MOV operation
ref_88630 = (ref_81065 & 0xFFFFFFFF) # MOV operation
ref_88895 = (ref_88094 & 0xFFFFFFFF) # MOV operation
ref_88899 = (ref_88630 & 0xFFFFFFFF) # MOV operation
ref_88901 = ((ref_88899 & 0xFFFFFFFF) | (ref_88895 & 0xFFFFFFFF)) # OR operation
ref_89200 = (ref_88901 & 0xFFFFFFFF) # MOV operation
ref_89906 = (ref_89200 & 0xFFFFFFFF) # MOV operation
ref_89961 = (ref_89906 & 0xFFFFFFFF) # MOV operation
ref_89985 = (ref_89961 & 0xFFFFFFFF) # MOV operation
ref_89993 = (ref_89985 & 0xFFFFFFFF) # MOV operation
ref_89995 = (ref_89993 & 0xFFFFFFFF) # MOV operation

print ref_89995 & 0xffffffffffffffff
