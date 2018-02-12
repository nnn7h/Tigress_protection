#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_16946 = ref_278 # MOV operation
ref_16990 = ref_16946 # MOV operation
ref_17004 = ((ref_16990 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_17670 = ref_278 # MOV operation
ref_17714 = ref_17670 # MOV operation
ref_17728 = (ref_17714 >> (0x35 & 0x3F)) # SHR operation
ref_17805 = ref_17004 # MOV operation
ref_17809 = ref_17728 # MOV operation
ref_17811 = (ref_17809 | ref_17805) # OR operation
ref_17880 = ref_17811 # MOV operation
ref_17894 = (ref_17880 >> (0x1 & 0x3F)) # SHR operation
ref_17971 = ref_17894 # MOV operation
ref_19231 = ref_17971 # MOV operation
ref_19367 = ref_19231 # MOV operation
ref_19373 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_19367)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_19952 = ref_278 # MOV operation
ref_20088 = ref_19952 # MOV operation
ref_20096 = ((((0x0) << 64 | ref_20088) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_20161 = ref_20096 # MOV operation
ref_20173 = ref_19373 # MOV operation
ref_20175 = ((ref_20161 - ref_20173) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_20183 = ref_20175 # MOV operation
ref_20255 = ref_20183 # MOV operation
ref_21767 = ref_20255 # MOV operation
ref_21811 = ref_21767 # MOV operation
ref_21825 = (ref_21811 >> (0x7 & 0x3F)) # SHR operation
ref_21894 = ref_21825 # MOV operation
ref_21908 = (ref_21894 >> (0x2 & 0x3F)) # SHR operation
ref_21977 = ref_21908 # MOV operation
ref_21991 = (0x7 & ref_21977) # AND operation
ref_22152 = ref_21991 # MOV operation
ref_22158 = (0x1 | ref_22152) # OR operation
ref_22824 = ref_278 # MOV operation
ref_22868 = ref_22824 # MOV operation
ref_22882 = ((0x9919884 + ref_22868) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_22952 = ref_22882 # MOV operation
ref_22964 = ref_22158 # MOV operation
ref_22966 = (ref_22952 >> ((ref_22964 & 0xFF) & 0x3F)) # SHR operation
ref_23043 = ref_22966 # MOV operation
ref_24302 = ref_278 # MOV operation
ref_24346 = ref_24302 # MOV operation
ref_24360 = ((0x1E5EA08F8 + ref_24346) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_24438 = ref_24360 # MOV operation
ref_26857 = ref_23043 # MOV operation
ref_27891 = ref_23043 # MOV operation
ref_27935 = ref_27891 # MOV operation
ref_27949 = (0x3F & ref_27935) # AND operation
ref_28018 = ref_27949 # MOV operation
ref_28032 = ((ref_28018 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_28109 = ref_26857 # MOV operation
ref_28113 = ref_28032 # MOV operation
ref_28115 = (ref_28113 | ref_28109) # OR operation
ref_28192 = ref_28115 # MOV operation
ref_30491 = ref_28192 # MOV operation
ref_31469 = ref_20255 # MOV operation
ref_31513 = ref_31469 # MOV operation
ref_31527 = (ref_31513 >> (0x2 & 0x3F)) # SHR operation
ref_31596 = ref_31527 # MOV operation
ref_31610 = (0xF & ref_31596) # AND operation
ref_31771 = ref_31610 # MOV operation
ref_31777 = (0x1 | ref_31771) # OR operation
ref_32444 = ref_17971 # MOV operation
ref_32488 = ref_32444 # MOV operation
ref_32500 = ref_31777 # MOV operation
ref_32502 = ((ref_32488 << ((ref_32500 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_33337 = ref_20255 # MOV operation
ref_33381 = ref_33337 # MOV operation
ref_33395 = (ref_33381 >> (0x2 & 0x3F)) # SHR operation
ref_33464 = ref_33395 # MOV operation
ref_33478 = (0xF & ref_33464) # AND operation
ref_33639 = ref_33478 # MOV operation
ref_33645 = (0x1 | ref_33639) # OR operation
ref_33810 = ref_33645 # MOV operation
ref_33812 = ((0x40 - ref_33810) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_33820 = ref_33812 # MOV operation
ref_34482 = ref_17971 # MOV operation
ref_34526 = ref_34482 # MOV operation
ref_34538 = ref_33820 # MOV operation
ref_34540 = (ref_34526 >> ((ref_34538 & 0xFF) & 0x3F)) # SHR operation
ref_34617 = ref_32502 # MOV operation
ref_34621 = ref_34540 # MOV operation
ref_34623 = (ref_34621 | ref_34617) # OR operation
ref_34692 = ref_34623 # MOV operation
ref_34706 = (0x7 & ref_34692) # AND operation
ref_34775 = ref_34706 # MOV operation
ref_34789 = ((ref_34775 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_34866 = ref_30491 # MOV operation
ref_34870 = ref_34789 # MOV operation
ref_34872 = (ref_34870 | ref_34866) # OR operation
ref_34949 = ref_34872 # MOV operation
ref_35838 = ref_24438 # MOV operation
ref_35882 = ref_35838 # MOV operation
ref_35896 = (ref_35882 >> (0x4 & 0x3F)) # SHR operation
ref_35965 = ref_35896 # MOV operation
ref_35979 = (0xF & ref_35965) # AND operation
ref_36140 = ref_35979 # MOV operation
ref_36146 = (0x1 | ref_36140) # OR operation
ref_36813 = ref_34949 # MOV operation
ref_36857 = ref_36813 # MOV operation
ref_36869 = ref_36146 # MOV operation
ref_36871 = (ref_36857 >> ((ref_36869 & 0xFF) & 0x3F)) # SHR operation
ref_37706 = ref_24438 # MOV operation
ref_37750 = ref_37706 # MOV operation
ref_37764 = (ref_37750 >> (0x4 & 0x3F)) # SHR operation
ref_37833 = ref_37764 # MOV operation
ref_37847 = (0xF & ref_37833) # AND operation
ref_38008 = ref_37847 # MOV operation
ref_38014 = (0x1 | ref_38008) # OR operation
ref_38179 = ref_38014 # MOV operation
ref_38181 = ((0x40 - ref_38179) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_38189 = ref_38181 # MOV operation
ref_38851 = ref_34949 # MOV operation
ref_38895 = ref_38851 # MOV operation
ref_38907 = ref_38189 # MOV operation
ref_38909 = ((ref_38895 << ((ref_38907 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_38986 = ref_36871 # MOV operation
ref_38990 = ref_38909 # MOV operation
ref_38992 = (ref_38990 | ref_38986) # OR operation
ref_39827 = ref_20255 # MOV operation
ref_39871 = ref_39827 # MOV operation
ref_39885 = (ref_39871 >> (0x3 & 0x3F)) # SHR operation
ref_39954 = ref_39885 # MOV operation
ref_39968 = (0xF & ref_39954) # AND operation
ref_40129 = ref_39968 # MOV operation
ref_40135 = (0x1 | ref_40129) # OR operation
ref_40802 = ref_17971 # MOV operation
ref_40846 = ref_40802 # MOV operation
ref_40858 = ref_40135 # MOV operation
ref_40860 = (ref_40846 >> ((ref_40858 & 0xFF) & 0x3F)) # SHR operation
ref_41695 = ref_20255 # MOV operation
ref_41739 = ref_41695 # MOV operation
ref_41753 = (ref_41739 >> (0x3 & 0x3F)) # SHR operation
ref_41822 = ref_41753 # MOV operation
ref_41836 = (0xF & ref_41822) # AND operation
ref_41997 = ref_41836 # MOV operation
ref_42003 = (0x1 | ref_41997) # OR operation
ref_42168 = ref_42003 # MOV operation
ref_42170 = ((0x40 - ref_42168) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_42178 = ref_42170 # MOV operation
ref_42840 = ref_17971 # MOV operation
ref_42884 = ref_42840 # MOV operation
ref_42896 = ref_42178 # MOV operation
ref_42898 = ((ref_42884 << ((ref_42896 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_42975 = ref_40860 # MOV operation
ref_42979 = ref_42898 # MOV operation
ref_42981 = (ref_42979 | ref_42975) # OR operation
ref_43050 = ref_42981 # MOV operation
ref_43062 = ref_38992 # MOV operation
ref_43064 = ((ref_43050 - ref_43062) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_43066 = ((((ref_43050 ^ (ref_43062 ^ ref_43064)) ^ ((ref_43050 ^ ref_43064) & (ref_43050 ^ ref_43062))) >> 63) & 0x1) # Carry flag
ref_43070 = (0x1 if (ref_43064 == 0x0) else 0x0) # Zero flag
ref_43072 = ((((ref_43062 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (((~(ref_43066) & 0x1) & (~(ref_43070) & 0x1)) == 0x1) else 0x0)) # SETA operation
ref_43074 = (ref_43072 & 0xFF) # MOVZX operation
ref_43130 = (ref_43074 & 0xFFFFFFFF) # MOV operation
ref_43132 = ((ref_43130 & 0xFFFFFFFF) & (ref_43130 & 0xFFFFFFFF)) # TEST operation
ref_43137 = (0x1 if (ref_43132 == 0x0) else 0x0) # Zero flag
ref_43139 = (0x539B if (ref_43137 == 0x1) else 0x5379) # Program Counter


if (ref_43137 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_16946 = ref_278 # MOV operation
    ref_16990 = ref_16946 # MOV operation
    ref_17004 = ((ref_16990 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_17670 = ref_278 # MOV operation
    ref_17714 = ref_17670 # MOV operation
    ref_17728 = (ref_17714 >> (0x35 & 0x3F)) # SHR operation
    ref_17805 = ref_17004 # MOV operation
    ref_17809 = ref_17728 # MOV operation
    ref_17811 = (ref_17809 | ref_17805) # OR operation
    ref_17880 = ref_17811 # MOV operation
    ref_17894 = (ref_17880 >> (0x1 & 0x3F)) # SHR operation
    ref_17971 = ref_17894 # MOV operation
    ref_19231 = ref_17971 # MOV operation
    ref_19367 = ref_19231 # MOV operation
    ref_19373 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_19367)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_19952 = ref_278 # MOV operation
    ref_20088 = ref_19952 # MOV operation
    ref_20096 = ((((0x0) << 64 | ref_20088) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_20161 = ref_20096 # MOV operation
    ref_20173 = ref_19373 # MOV operation
    ref_20175 = ((ref_20161 - ref_20173) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_20183 = ref_20175 # MOV operation
    ref_20255 = ref_20183 # MOV operation
    ref_21767 = ref_20255 # MOV operation
    ref_21811 = ref_21767 # MOV operation
    ref_21825 = (ref_21811 >> (0x7 & 0x3F)) # SHR operation
    ref_21894 = ref_21825 # MOV operation
    ref_21908 = (ref_21894 >> (0x2 & 0x3F)) # SHR operation
    ref_21977 = ref_21908 # MOV operation
    ref_21991 = (0x7 & ref_21977) # AND operation
    ref_22152 = ref_21991 # MOV operation
    ref_22158 = (0x1 | ref_22152) # OR operation
    ref_22824 = ref_278 # MOV operation
    ref_22868 = ref_22824 # MOV operation
    ref_22882 = ((0x9919884 + ref_22868) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_22952 = ref_22882 # MOV operation
    ref_22964 = ref_22158 # MOV operation
    ref_22966 = (ref_22952 >> ((ref_22964 & 0xFF) & 0x3F)) # SHR operation
    ref_23043 = ref_22966 # MOV operation
    ref_24302 = ref_278 # MOV operation
    ref_24346 = ref_24302 # MOV operation
    ref_24360 = ((0x1E5EA08F8 + ref_24346) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_24438 = ref_24360 # MOV operation
    ref_26857 = ref_23043 # MOV operation
    ref_27891 = ref_23043 # MOV operation
    ref_27935 = ref_27891 # MOV operation
    ref_27949 = (0x3F & ref_27935) # AND operation
    ref_28018 = ref_27949 # MOV operation
    ref_28032 = ((ref_28018 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_28109 = ref_26857 # MOV operation
    ref_28113 = ref_28032 # MOV operation
    ref_28115 = (ref_28113 | ref_28109) # OR operation
    ref_28192 = ref_28115 # MOV operation
    ref_30491 = ref_28192 # MOV operation
    ref_31469 = ref_20255 # MOV operation
    ref_31513 = ref_31469 # MOV operation
    ref_31527 = (ref_31513 >> (0x2 & 0x3F)) # SHR operation
    ref_31596 = ref_31527 # MOV operation
    ref_31610 = (0xF & ref_31596) # AND operation
    ref_31771 = ref_31610 # MOV operation
    ref_31777 = (0x1 | ref_31771) # OR operation
    ref_32444 = ref_17971 # MOV operation
    ref_32488 = ref_32444 # MOV operation
    ref_32500 = ref_31777 # MOV operation
    ref_32502 = ((ref_32488 << ((ref_32500 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_33337 = ref_20255 # MOV operation
    ref_33381 = ref_33337 # MOV operation
    ref_33395 = (ref_33381 >> (0x2 & 0x3F)) # SHR operation
    ref_33464 = ref_33395 # MOV operation
    ref_33478 = (0xF & ref_33464) # AND operation
    ref_33639 = ref_33478 # MOV operation
    ref_33645 = (0x1 | ref_33639) # OR operation
    ref_33810 = ref_33645 # MOV operation
    ref_33812 = ((0x40 - ref_33810) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_33820 = ref_33812 # MOV operation
    ref_34482 = ref_17971 # MOV operation
    ref_34526 = ref_34482 # MOV operation
    ref_34538 = ref_33820 # MOV operation
    ref_34540 = (ref_34526 >> ((ref_34538 & 0xFF) & 0x3F)) # SHR operation
    ref_34617 = ref_32502 # MOV operation
    ref_34621 = ref_34540 # MOV operation
    ref_34623 = (ref_34621 | ref_34617) # OR operation
    ref_34692 = ref_34623 # MOV operation
    ref_34706 = (0x7 & ref_34692) # AND operation
    ref_34775 = ref_34706 # MOV operation
    ref_34789 = ((ref_34775 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_34866 = ref_30491 # MOV operation
    ref_34870 = ref_34789 # MOV operation
    ref_34872 = (ref_34870 | ref_34866) # OR operation
    ref_34949 = ref_34872 # MOV operation
    ref_44467 = ref_20255 # MOV operation
    ref_45277 = ref_20255 # MOV operation
    ref_45321 = ref_45277 # MOV operation
    ref_45335 = (0xF & ref_45321) # AND operation
    ref_45404 = ref_45335 # MOV operation
    ref_45418 = ((ref_45404 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_45495 = ref_44467 # MOV operation
    ref_45499 = ref_45418 # MOV operation
    ref_45501 = (ref_45499 | ref_45495) # OR operation
    ref_45578 = ref_45501 # MOV operation
    ref_46838 = ref_17971 # MOV operation
    ref_47648 = ref_45578 # MOV operation
    ref_48290 = ref_34949 # MOV operation
    ref_48334 = ref_48290 # MOV operation
    ref_48346 = ref_47648 # MOV operation
    ref_48348 = (ref_48346 & ref_48334) # AND operation
    ref_48417 = ref_48348 # MOV operation
    ref_48431 = (0x1F & ref_48417) # AND operation
    ref_48500 = ref_48431 # MOV operation
    ref_48514 = ((ref_48500 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_48591 = ref_46838 # MOV operation
    ref_48595 = ref_48514 # MOV operation
    ref_48597 = (ref_48595 | ref_48591) # OR operation
    ref_48674 = ref_48597 # MOV operation
    ref_49917 = ref_48674 # MOV operation
    ref_50559 = ref_45578 # MOV operation
    ref_50611 = ref_49917 # MOV operation
    ref_50615 = ref_50559 # MOV operation
    ref_50617 = (ref_50615 | ref_50611) # OR operation
    ref_51284 = ref_34949 # MOV operation
    ref_51926 = ref_24438 # MOV operation
    ref_51978 = ref_51284 # MOV operation
    ref_51982 = ref_51926 # MOV operation
    ref_51984 = (((sx(0x40, ref_51982) * sx(0x40, ref_51978)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_52058 = ref_50617 # MOV operation
    ref_52062 = ref_51984 # MOV operation
    ref_52064 = (((sx(0x40, ref_52062) * sx(0x40, ref_52058)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_52138 = ref_52064 # MOV operation
    ref_52292 = ref_52138 # MOV operation
    ref_52294 = ref_52292 # MOV operation
    endb = ref_52294


else:
    ref_52614 = SymVar_0
    ref_52629 = ref_52614 # MOV operation
    ref_69302 = ref_52629 # MOV operation
    ref_69346 = ref_69302 # MOV operation
    ref_69360 = ((ref_69346 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_70026 = ref_52629 # MOV operation
    ref_70070 = ref_70026 # MOV operation
    ref_70084 = (ref_70070 >> (0x35 & 0x3F)) # SHR operation
    ref_70161 = ref_69360 # MOV operation
    ref_70165 = ref_70084 # MOV operation
    ref_70167 = (ref_70165 | ref_70161) # OR operation
    ref_70236 = ref_70167 # MOV operation
    ref_70250 = (ref_70236 >> (0x1 & 0x3F)) # SHR operation
    ref_70327 = ref_70250 # MOV operation
    ref_71587 = ref_70327 # MOV operation
    ref_71723 = ref_71587 # MOV operation
    ref_71729 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_71723)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_72308 = ref_52629 # MOV operation
    ref_72444 = ref_72308 # MOV operation
    ref_72452 = ((((0x0) << 64 | ref_72444) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_72517 = ref_72452 # MOV operation
    ref_72529 = ref_71729 # MOV operation
    ref_72531 = ((ref_72517 - ref_72529) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_72539 = ref_72531 # MOV operation
    ref_72611 = ref_72539 # MOV operation
    ref_74123 = ref_72611 # MOV operation
    ref_74167 = ref_74123 # MOV operation
    ref_74181 = (ref_74167 >> (0x7 & 0x3F)) # SHR operation
    ref_74250 = ref_74181 # MOV operation
    ref_74264 = (ref_74250 >> (0x2 & 0x3F)) # SHR operation
    ref_74333 = ref_74264 # MOV operation
    ref_74347 = (0x7 & ref_74333) # AND operation
    ref_74508 = ref_74347 # MOV operation
    ref_74514 = (0x1 | ref_74508) # OR operation
    ref_75180 = ref_52629 # MOV operation
    ref_75224 = ref_75180 # MOV operation
    ref_75238 = ((0x9919884 + ref_75224) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_75308 = ref_75238 # MOV operation
    ref_75320 = ref_74514 # MOV operation
    ref_75322 = (ref_75308 >> ((ref_75320 & 0xFF) & 0x3F)) # SHR operation
    ref_75399 = ref_75322 # MOV operation
    ref_76658 = ref_52629 # MOV operation
    ref_76702 = ref_76658 # MOV operation
    ref_76716 = ((0x1E5EA08F8 + ref_76702) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_76794 = ref_76716 # MOV operation
    ref_79213 = ref_75399 # MOV operation
    ref_80247 = ref_75399 # MOV operation
    ref_80291 = ref_80247 # MOV operation
    ref_80305 = (0x3F & ref_80291) # AND operation
    ref_80374 = ref_80305 # MOV operation
    ref_80388 = ((ref_80374 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_80465 = ref_79213 # MOV operation
    ref_80469 = ref_80388 # MOV operation
    ref_80471 = (ref_80469 | ref_80465) # OR operation
    ref_80548 = ref_80471 # MOV operation
    ref_82847 = ref_80548 # MOV operation
    ref_83825 = ref_72611 # MOV operation
    ref_83869 = ref_83825 # MOV operation
    ref_83883 = (ref_83869 >> (0x2 & 0x3F)) # SHR operation
    ref_83952 = ref_83883 # MOV operation
    ref_83966 = (0xF & ref_83952) # AND operation
    ref_84127 = ref_83966 # MOV operation
    ref_84133 = (0x1 | ref_84127) # OR operation
    ref_84800 = ref_70327 # MOV operation
    ref_84844 = ref_84800 # MOV operation
    ref_84856 = ref_84133 # MOV operation
    ref_84858 = ((ref_84844 << ((ref_84856 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_85693 = ref_72611 # MOV operation
    ref_85737 = ref_85693 # MOV operation
    ref_85751 = (ref_85737 >> (0x2 & 0x3F)) # SHR operation
    ref_85820 = ref_85751 # MOV operation
    ref_85834 = (0xF & ref_85820) # AND operation
    ref_85995 = ref_85834 # MOV operation
    ref_86001 = (0x1 | ref_85995) # OR operation
    ref_86166 = ref_86001 # MOV operation
    ref_86168 = ((0x40 - ref_86166) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_86176 = ref_86168 # MOV operation
    ref_86838 = ref_70327 # MOV operation
    ref_86882 = ref_86838 # MOV operation
    ref_86894 = ref_86176 # MOV operation
    ref_86896 = (ref_86882 >> ((ref_86894 & 0xFF) & 0x3F)) # SHR operation
    ref_86973 = ref_84858 # MOV operation
    ref_86977 = ref_86896 # MOV operation
    ref_86979 = (ref_86977 | ref_86973) # OR operation
    ref_87048 = ref_86979 # MOV operation
    ref_87062 = (0x7 & ref_87048) # AND operation
    ref_87131 = ref_87062 # MOV operation
    ref_87145 = ((ref_87131 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_87222 = ref_82847 # MOV operation
    ref_87226 = ref_87145 # MOV operation
    ref_87228 = (ref_87226 | ref_87222) # OR operation
    ref_87305 = ref_87228 # MOV operation
    ref_87307 = ((ref_87305 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_87308 = ((ref_87305 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_87309 = ((ref_87305 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_87310 = ((ref_87305 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_87311 = ((ref_87305 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_87312 = ((ref_87305 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_87313 = ((ref_87305 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_87314 = (ref_87305 & 0xFF) # Byte reference - MOV operation
    ref_96946 = ref_76794 # MOV operation
    ref_96990 = ref_96946 # MOV operation
    ref_97004 = (ref_96990 >> (0x3 & 0x3F)) # SHR operation
    ref_97073 = ref_97004 # MOV operation
    ref_97087 = (0xF & ref_97073) # AND operation
    ref_97248 = ref_97087 # MOV operation
    ref_97254 = (0x1 | ref_97248) # OR operation
    ref_97921 = ref_76794 # MOV operation
    ref_97965 = ref_97921 # MOV operation
    ref_97977 = ref_97254 # MOV operation
    ref_97979 = ((ref_97965 << ((ref_97977 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_98814 = ref_76794 # MOV operation
    ref_98858 = ref_98814 # MOV operation
    ref_98872 = (ref_98858 >> (0x3 & 0x3F)) # SHR operation
    ref_98941 = ref_98872 # MOV operation
    ref_98955 = (0xF & ref_98941) # AND operation
    ref_99116 = ref_98955 # MOV operation
    ref_99122 = (0x1 | ref_99116) # OR operation
    ref_99287 = ref_99122 # MOV operation
    ref_99289 = ((0x40 - ref_99287) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_99297 = ref_99289 # MOV operation
    ref_99959 = ref_76794 # MOV operation
    ref_100003 = ref_99959 # MOV operation
    ref_100015 = ref_99297 # MOV operation
    ref_100017 = (ref_100003 >> ((ref_100015 & 0xFF) & 0x3F)) # SHR operation
    ref_100094 = ref_97979 # MOV operation
    ref_100098 = ref_100017 # MOV operation
    ref_100100 = (ref_100098 | ref_100094) # OR operation
    ref_100177 = ref_100100 # MOV operation
    ref_101253 = ref_87313 # MOVZX operation
    ref_101393 = (ref_101253 & 0xFF) # MOVZX operation
    ref_102461 = ref_87311 # MOVZX operation
    ref_103517 = (ref_102461 & 0xFF) # MOVZX operation
    ref_103519 = (ref_103517 & 0xFF) # Byte reference - MOV operation
    ref_103669 = (ref_101393 & 0xFF) # MOVZX operation
    ref_104725 = (ref_103669 & 0xFF) # MOVZX operation
    ref_104727 = (ref_104725 & 0xFF) # Byte reference - MOV operation
    ref_105960 = ref_100177 # MOV operation
    ref_106602 = ref_72611 # MOV operation
    ref_106654 = ref_105960 # MOV operation
    ref_106658 = ref_106602 # MOV operation
    ref_106660 = (ref_106658 | ref_106654) # OR operation
    ref_107327 = ((((((((ref_87307) << 8 | ref_87308) << 8 | ref_87309) << 8 | ref_87310) << 8 | ref_104727) << 8 | ref_87312) << 8 | ref_103519) << 8 | ref_87314) # MOV operation
    ref_107969 = ref_76794 # MOV operation
    ref_108021 = ref_107327 # MOV operation
    ref_108025 = ref_107969 # MOV operation
    ref_108027 = (((sx(0x40, ref_108025) * sx(0x40, ref_108021)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_108101 = ref_106660 # MOV operation
    ref_108105 = ref_108027 # MOV operation
    ref_108107 = (((sx(0x40, ref_108105) * sx(0x40, ref_108101)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_108181 = ref_108107 # MOV operation
    ref_108335 = ref_108181 # MOV operation
    ref_108337 = ref_108335 # MOV operation
    endb = ref_108337


print endb & 0xffffffffffffffff
