#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_6562 = ref_278 # MOV operation
ref_6672 = ref_6562 # MOV operation
ref_6692 = (ref_6672 >> (0xD & 0x3F)) # SHR operation
ref_7706 = ref_278 # MOV operation
ref_7816 = ref_7706 # MOV operation
ref_7836 = ((ref_7816 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7951 = ref_6692 # MOV operation
ref_7967 = ref_7836 # MOV operation
ref_7969 = (ref_7951 | ref_7967) # OR operation
ref_8084 = ref_7969 # MOV operation
ref_8102 = ((ref_8084 + 0x2EA4A1C39AF5800) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8222 = ref_8102 # MOV operation
ref_9943 = ref_278 # MOV operation
ref_10867 = ref_8222 # MOV operation
ref_10985 = ref_9943 # MOV operation
ref_10993 = ref_10867 # MOV operation
ref_10995 = ((ref_10985 - ref_10993) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_11115 = ref_10995 # MOV operation
ref_12934 = ref_278 # MOV operation
ref_13044 = ref_12934 # MOV operation
ref_13064 = ((ref_13044 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14078 = ref_278 # MOV operation
ref_14188 = ref_14078 # MOV operation
ref_14208 = (ref_14188 >> (0x37 & 0x3F)) # SHR operation
ref_14323 = ref_13064 # MOV operation
ref_14339 = ref_14208 # MOV operation
ref_14341 = (ref_14323 | ref_14339) # OR operation
ref_14460 = ref_14341 # MOV operation
ref_16181 = ref_278 # MOV operation
ref_16389 = ref_16181 # MOV operation
ref_16407 = (ref_16389 | 0x3E908497) # OR operation
ref_16526 = ref_16407 # MOV operation
ref_17630 = ref_11115 # MOV operation
ref_17740 = ref_17630 # MOV operation
ref_17760 = (ref_17740 >> (0x2 & 0x3F)) # SHR operation
ref_17973 = ref_17760 # MOV operation
ref_17991 = (ref_17973 & 0xF) # AND operation
ref_18204 = ref_17991 # MOV operation
ref_18222 = (ref_18204 | 0x1) # OR operation
ref_19151 = ref_8222 # MOV operation
ref_19261 = ref_19151 # MOV operation
ref_19277 = ref_18222 # MOV operation
ref_19279 = (ref_19277 & 0xFFFFFFFF) # MOV operation
ref_19281 = (ref_19261 >> ((ref_19279 & 0xFF) & 0x3F)) # SHR operation
ref_20406 = ref_11115 # MOV operation
ref_20516 = ref_20406 # MOV operation
ref_20536 = (ref_20516 >> (0x2 & 0x3F)) # SHR operation
ref_20749 = ref_20536 # MOV operation
ref_20767 = (ref_20749 & 0xF) # AND operation
ref_20980 = ref_20767 # MOV operation
ref_20998 = (ref_20980 | 0x1) # OR operation
ref_21129 = ref_20998 # MOV operation
ref_21131 = ((0x40 - ref_21129) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_22061 = ref_8222 # MOV operation
ref_22171 = ref_22061 # MOV operation
ref_22187 = ref_21131 # MOV operation
ref_22189 = (ref_22187 & 0xFFFFFFFF) # MOV operation
ref_22191 = ((ref_22171 << ((ref_22189 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_22306 = ref_19281 # MOV operation
ref_22322 = ref_22191 # MOV operation
ref_22324 = (ref_22306 | ref_22322) # OR operation
ref_23253 = ref_14460 # MOV operation
ref_24177 = ref_16526 # MOV operation
ref_24295 = ref_23253 # MOV operation
ref_24303 = ref_24177 # MOV operation
ref_24305 = ((ref_24295 - ref_24303) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_24421 = ref_22324 # MOV operation
ref_24437 = ref_24305 # MOV operation
ref_24439 = ((ref_24421 - ref_24437) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_24441 = ((((ref_24421 ^ (ref_24437 ^ ref_24439)) ^ ((ref_24421 ^ ref_24439) & (ref_24421 ^ ref_24437))) >> 63) & 0x1) # Carry flag
ref_24447 = ((((ref_24437 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (ref_24441 == 0x1) else 0x0)) # SETB operation
ref_24449 = (ref_24447 & 0xFF) # MOVZX operation
ref_24551 = (ref_24449 & 0xFFFFFFFF) # MOV operation
ref_24553 = ((ref_24551 & 0xFFFFFFFF) & (ref_24551 & 0xFFFFFFFF)) # TEST operation
ref_24558 = (0x1 if (ref_24553 == 0x0) else 0x0) # Zero flag
ref_24560 = (0x169C if (ref_24558 == 0x1) else 0x167B) # Program Counter


if (ref_24558 == 0x1):
    ref_52665 = SymVar_0
    ref_52680 = ref_52665 # MOV operation
    ref_58969 = ref_52680 # MOV operation
    ref_59079 = ref_58969 # MOV operation
    ref_59099 = (ref_59079 >> (0xD & 0x3F)) # SHR operation
    ref_60113 = ref_52680 # MOV operation
    ref_60223 = ref_60113 # MOV operation
    ref_60243 = ((ref_60223 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_60358 = ref_59099 # MOV operation
    ref_60374 = ref_60243 # MOV operation
    ref_60376 = (ref_60358 | ref_60374) # OR operation
    ref_60491 = ref_60376 # MOV operation
    ref_60509 = ((ref_60491 + 0x2EA4A1C39AF5800) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_60629 = ref_60509 # MOV operation
    ref_62350 = ref_52680 # MOV operation
    ref_63274 = ref_60629 # MOV operation
    ref_63392 = ref_62350 # MOV operation
    ref_63400 = ref_63274 # MOV operation
    ref_63402 = ((ref_63392 - ref_63400) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_63522 = ref_63402 # MOV operation
    ref_65341 = ref_52680 # MOV operation
    ref_65451 = ref_65341 # MOV operation
    ref_65471 = ((ref_65451 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_66485 = ref_52680 # MOV operation
    ref_66595 = ref_66485 # MOV operation
    ref_66615 = (ref_66595 >> (0x37 & 0x3F)) # SHR operation
    ref_66730 = ref_65471 # MOV operation
    ref_66746 = ref_66615 # MOV operation
    ref_66748 = (ref_66730 | ref_66746) # OR operation
    ref_66867 = ref_66748 # MOV operation
    ref_68588 = ref_52680 # MOV operation
    ref_68796 = ref_68588 # MOV operation
    ref_68814 = (ref_68796 | 0x3E908497) # OR operation
    ref_68933 = ref_68814 # MOV operation
    ref_78868 = ref_66867 # MOV operation
    ref_79792 = ref_68933 # MOV operation
    ref_79902 = ref_78868 # MOV operation
    ref_79918 = ref_79792 # MOV operation
    ref_79920 = (ref_79902 | ref_79918) # OR operation
    ref_80035 = ref_79920 # MOV operation
    ref_80055 = (ref_80035 >> (0x4 & 0x3F)) # SHR operation
    ref_80268 = ref_80055 # MOV operation
    ref_80286 = (ref_80268 & 0x7) # AND operation
    ref_80499 = ref_80286 # MOV operation
    ref_80517 = (ref_80499 | 0x1) # OR operation
    ref_81544 = ref_63522 # MOV operation
    ref_81654 = ref_81544 # MOV operation
    ref_81674 = (ref_81654 >> (0x4 & 0x3F)) # SHR operation
    ref_81887 = ref_81674 # MOV operation
    ref_81905 = (ref_81887 & 0xF) # AND operation
    ref_82118 = ref_81905 # MOV operation
    ref_82136 = (ref_82118 | 0x1) # OR operation
    ref_83065 = ref_60629 # MOV operation
    ref_83175 = ref_83065 # MOV operation
    ref_83191 = ref_82136 # MOV operation
    ref_83193 = (ref_83191 & 0xFFFFFFFF) # MOV operation
    ref_83195 = ((ref_83175 << ((ref_83193 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_84320 = ref_63522 # MOV operation
    ref_84430 = ref_84320 # MOV operation
    ref_84450 = (ref_84430 >> (0x4 & 0x3F)) # SHR operation
    ref_84663 = ref_84450 # MOV operation
    ref_84681 = (ref_84663 & 0xF) # AND operation
    ref_84894 = ref_84681 # MOV operation
    ref_84912 = (ref_84894 | 0x1) # OR operation
    ref_85043 = ref_84912 # MOV operation
    ref_85045 = ((0x40 - ref_85043) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_85975 = ref_60629 # MOV operation
    ref_86085 = ref_85975 # MOV operation
    ref_86101 = ref_85045 # MOV operation
    ref_86103 = (ref_86101 & 0xFFFFFFFF) # MOV operation
    ref_86105 = (ref_86085 >> ((ref_86103 & 0xFF) & 0x3F)) # SHR operation
    ref_86220 = ref_83195 # MOV operation
    ref_86236 = ref_86105 # MOV operation
    ref_86238 = (ref_86220 | ref_86236) # OR operation
    ref_86353 = ref_86238 # MOV operation
    ref_86369 = ref_80517 # MOV operation
    ref_86371 = (ref_86369 & 0xFFFFFFFF) # MOV operation
    ref_86373 = (ref_86353 >> ((ref_86371 & 0xFF) & 0x3F)) # SHR operation
    ref_86492 = ref_86373 # MOV operation
    ref_86703 = ref_86492 # MOV operation
    ref_86705 = ref_86703 # MOV operation
    endb = ref_86705


else:
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_6562 = ref_278 # MOV operation
    ref_6672 = ref_6562 # MOV operation
    ref_6692 = (ref_6672 >> (0xD & 0x3F)) # SHR operation
    ref_7706 = ref_278 # MOV operation
    ref_7816 = ref_7706 # MOV operation
    ref_7836 = ((ref_7816 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_7951 = ref_6692 # MOV operation
    ref_7967 = ref_7836 # MOV operation
    ref_7969 = (ref_7951 | ref_7967) # OR operation
    ref_8084 = ref_7969 # MOV operation
    ref_8102 = ((ref_8084 + 0x2EA4A1C39AF5800) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_8222 = ref_8102 # MOV operation
    ref_9943 = ref_278 # MOV operation
    ref_10867 = ref_8222 # MOV operation
    ref_10985 = ref_9943 # MOV operation
    ref_10993 = ref_10867 # MOV operation
    ref_10995 = ((ref_10985 - ref_10993) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_11115 = ref_10995 # MOV operation
    ref_11117 = ((ref_11115 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_11118 = ((ref_11115 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_11119 = ((ref_11115 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_11120 = ((ref_11115 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_11121 = ((ref_11115 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_11122 = ((ref_11115 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_11123 = ((ref_11115 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_11124 = (ref_11115 & 0xFF) # Byte reference - MOV operation
    ref_12934 = ref_278 # MOV operation
    ref_13044 = ref_12934 # MOV operation
    ref_13064 = ((ref_13044 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_14078 = ref_278 # MOV operation
    ref_14188 = ref_14078 # MOV operation
    ref_14208 = (ref_14188 >> (0x37 & 0x3F)) # SHR operation
    ref_14323 = ref_13064 # MOV operation
    ref_14339 = ref_14208 # MOV operation
    ref_14341 = (ref_14323 | ref_14339) # OR operation
    ref_14460 = ref_14341 # MOV operation
    ref_16181 = ref_278 # MOV operation
    ref_16389 = ref_16181 # MOV operation
    ref_16407 = (ref_16389 | 0x3E908497) # OR operation
    ref_16526 = ref_16407 # MOV operation
    ref_26281 = ((((ref_11117) << 8 | ref_11118) << 8 | ref_11119) << 8 | ref_11120) # MOV operation
    ref_26391 = (ref_26281 & 0xFFFFFFFF) # MOV operation
    ref_29493 = ((((ref_11121) << 8 | ref_11122) << 8 | ref_11123) << 8 | ref_11124) # MOV operation
    ref_29603 = (ref_29493 & 0xFFFFFFFF) # MOV operation
    ref_29605 = (((ref_29603 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_29606 = (((ref_29603 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_29607 = (((ref_29603 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_29608 = ((ref_29603 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_31325 = (ref_26391 & 0xFFFFFFFF) # MOV operation
    ref_31435 = (ref_31325 & 0xFFFFFFFF) # MOV operation
    ref_31437 = (((ref_31435 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_31438 = (((ref_31435 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_31439 = (((ref_31435 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_31440 = ((ref_31435 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_33165 = ref_8222 # MOV operation
    ref_34187 = ref_8222 # MOV operation
    ref_34395 = ref_34187 # MOV operation
    ref_34413 = (ref_34395 & 0x3F) # AND operation
    ref_34528 = ref_34413 # MOV operation
    ref_34548 = ((ref_34528 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_34663 = ref_33165 # MOV operation
    ref_34679 = ref_34548 # MOV operation
    ref_34681 = (ref_34663 | ref_34679) # OR operation
    ref_34800 = ref_34681 # MOV operation
    ref_36534 = ref_16526 # MOV operation
    ref_37556 = ref_34800 # MOV operation
    ref_37764 = ref_37556 # MOV operation
    ref_37782 = (ref_37764 & 0x1F) # AND operation
    ref_37897 = ref_37782 # MOV operation
    ref_37917 = ((ref_37897 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_38032 = ref_36534 # MOV operation
    ref_38048 = ref_37917 # MOV operation
    ref_38050 = (ref_38032 | ref_38048) # OR operation
    ref_38169 = ref_38050 # MOV operation
    ref_39903 = ref_34800 # MOV operation
    ref_40925 = ref_14460 # MOV operation
    ref_41849 = ref_34800 # MOV operation
    ref_41959 = ref_41849 # MOV operation
    ref_41975 = ref_40925 # MOV operation
    ref_41977 = ((ref_41959 + ref_41975) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_42191 = ref_41977 # MOV operation
    ref_42209 = (ref_42191 & 0x1F) # AND operation
    ref_42324 = ref_42209 # MOV operation
    ref_42344 = ((ref_42324 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_42459 = ref_39903 # MOV operation
    ref_42475 = ref_42344 # MOV operation
    ref_42477 = (ref_42459 | ref_42475) # OR operation
    ref_42596 = ref_42477 # MOV operation
    ref_44508 = ref_14460 # MOV operation
    ref_45432 = ref_38169 # MOV operation
    ref_45542 = ref_44508 # MOV operation
    ref_45558 = ref_45432 # MOV operation
    ref_45560 = (ref_45542 | ref_45558) # OR operation
    ref_45675 = ref_45560 # MOV operation
    ref_45695 = (ref_45675 >> (0x4 & 0x3F)) # SHR operation
    ref_45908 = ref_45695 # MOV operation
    ref_45926 = (ref_45908 & 0x7) # AND operation
    ref_46139 = ref_45926 # MOV operation
    ref_46157 = (ref_46139 | 0x1) # OR operation
    ref_47184 = ((((((((ref_29605) << 8 | ref_29606) << 8 | ref_29607) << 8 | ref_29608) << 8 | ref_31437) << 8 | ref_31438) << 8 | ref_31439) << 8 | ref_31440) # MOV operation
    ref_47294 = ref_47184 # MOV operation
    ref_47314 = (ref_47294 >> (0x4 & 0x3F)) # SHR operation
    ref_47527 = ref_47314 # MOV operation
    ref_47545 = (ref_47527 & 0xF) # AND operation
    ref_47758 = ref_47545 # MOV operation
    ref_47776 = (ref_47758 | 0x1) # OR operation
    ref_48705 = ref_42596 # MOV operation
    ref_48815 = ref_48705 # MOV operation
    ref_48831 = ref_47776 # MOV operation
    ref_48833 = (ref_48831 & 0xFFFFFFFF) # MOV operation
    ref_48835 = ((ref_48815 << ((ref_48833 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_49960 = ((((((((ref_29605) << 8 | ref_29606) << 8 | ref_29607) << 8 | ref_29608) << 8 | ref_31437) << 8 | ref_31438) << 8 | ref_31439) << 8 | ref_31440) # MOV operation
    ref_50070 = ref_49960 # MOV operation
    ref_50090 = (ref_50070 >> (0x4 & 0x3F)) # SHR operation
    ref_50303 = ref_50090 # MOV operation
    ref_50321 = (ref_50303 & 0xF) # AND operation
    ref_50534 = ref_50321 # MOV operation
    ref_50552 = (ref_50534 | 0x1) # OR operation
    ref_50683 = ref_50552 # MOV operation
    ref_50685 = ((0x40 - ref_50683) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_51615 = ref_42596 # MOV operation
    ref_51725 = ref_51615 # MOV operation
    ref_51741 = ref_50685 # MOV operation
    ref_51743 = (ref_51741 & 0xFFFFFFFF) # MOV operation
    ref_51745 = (ref_51725 >> ((ref_51743 & 0xFF) & 0x3F)) # SHR operation
    ref_51860 = ref_48835 # MOV operation
    ref_51876 = ref_51745 # MOV operation
    ref_51878 = (ref_51860 | ref_51876) # OR operation
    ref_51993 = ref_51878 # MOV operation
    ref_52009 = ref_46157 # MOV operation
    ref_52011 = (ref_52009 & 0xFFFFFFFF) # MOV operation
    ref_52013 = (ref_51993 >> ((ref_52011 & 0xFF) & 0x3F)) # SHR operation
    ref_52132 = ref_52013 # MOV operation
    ref_52343 = ref_52132 # MOV operation
    ref_52345 = ref_52343 # MOV operation
    endb = ref_52345


print endb & 0xffffffffffffffff
