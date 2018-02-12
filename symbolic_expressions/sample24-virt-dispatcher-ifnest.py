#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_9030 = ref_278 # MOV operation
ref_9129 = ref_9030 # MOV operation
ref_9143 = ((ref_9129 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_11528 = ref_278 # MOV operation
ref_11753 = ref_11528 # MOV operation
ref_11767 = (ref_11753 >> (0x35 & 0x3F)) # SHR operation
ref_11926 = ref_9143 # MOV operation
ref_11930 = ref_11767 # MOV operation
ref_11932 = (ref_11930 | ref_11926) # OR operation
ref_12182 = ref_11932 # MOV operation
ref_12196 = (ref_12182 >> (0x1 & 0x3F)) # SHR operation
ref_12346 = ref_12196 # MOV operation
ref_15853 = ref_12346 # MOV operation
ref_16396 = ref_15853 # MOV operation
ref_16402 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_16396)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_18438 = ref_278 # MOV operation
ref_18972 = ref_18438 # MOV operation
ref_18980 = ((((0x0) << 64 | ref_18972) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_19244 = ref_18980 # MOV operation
ref_19256 = ref_16402 # MOV operation
ref_19258 = ((ref_19244 - ref_19256) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_19266 = ref_19258 # MOV operation
ref_19411 = ref_19266 # MOV operation
ref_23956 = ref_19411 # MOV operation
ref_24181 = ref_23956 # MOV operation
ref_24195 = (ref_24181 >> (0x7 & 0x3F)) # SHR operation
ref_24445 = ref_24195 # MOV operation
ref_24459 = (ref_24445 >> (0x2 & 0x3F)) # SHR operation
ref_24754 = ref_24459 # MOV operation
ref_24768 = (0x7 & ref_24754) # AND operation
ref_25273 = ref_24768 # MOV operation
ref_25279 = (0x1 | ref_25273) # OR operation
ref_27664 = ref_278 # MOV operation
ref_27916 = ref_27664 # MOV operation
ref_27930 = ((0x9919884 + ref_27916) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_28181 = ref_27930 # MOV operation
ref_28193 = ref_25279 # MOV operation
ref_28195 = (ref_28181 >> ((ref_28193 & 0xFF) & 0x3F)) # SHR operation
ref_28345 = ref_28195 # MOV operation
ref_32383 = ref_278 # MOV operation
ref_32635 = ref_32383 # MOV operation
ref_32649 = ((0x1E5EA08F8 + ref_32635) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_32800 = ref_32649 # MOV operation
ref_39645 = ref_28345 # MOV operation
ref_42879 = ref_28345 # MOV operation
ref_43149 = ref_42879 # MOV operation
ref_43163 = (0x3F & ref_43149) # AND operation
ref_43287 = ref_43163 # MOV operation
ref_43301 = ((ref_43287 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_43460 = ref_39645 # MOV operation
ref_43464 = ref_43301 # MOV operation
ref_43466 = (ref_43464 | ref_43460) # OR operation
ref_43616 = ref_43466 # MOV operation
ref_49973 = ref_43616 # MOV operation
ref_53186 = ref_19411 # MOV operation
ref_53411 = ref_53186 # MOV operation
ref_53425 = (ref_53411 >> (0x2 & 0x3F)) # SHR operation
ref_53720 = ref_53425 # MOV operation
ref_53734 = (0xF & ref_53720) # AND operation
ref_54239 = ref_53734 # MOV operation
ref_54245 = (0x1 | ref_54239) # OR operation
ref_56099 = ref_12346 # MOV operation
ref_56198 = ref_56099 # MOV operation
ref_56210 = ref_54245 # MOV operation
ref_56212 = ((ref_56198 << ((ref_56210 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_58758 = ref_19411 # MOV operation
ref_58983 = ref_58758 # MOV operation
ref_58997 = (ref_58983 >> (0x2 & 0x3F)) # SHR operation
ref_59292 = ref_58997 # MOV operation
ref_59306 = (0xF & ref_59292) # AND operation
ref_59811 = ref_59306 # MOV operation
ref_59817 = (0x1 | ref_59811) # OR operation
ref_60443 = ref_59817 # MOV operation
ref_60445 = ((0x40 - ref_60443) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_60453 = ref_60445 # MOV operation
ref_62302 = ref_12346 # MOV operation
ref_62527 = ref_62302 # MOV operation
ref_62539 = ref_60453 # MOV operation
ref_62541 = (ref_62527 >> ((ref_62539 & 0xFF) & 0x3F)) # SHR operation
ref_62700 = ref_56212 # MOV operation
ref_62704 = ref_62541 # MOV operation
ref_62706 = (ref_62704 | ref_62700) # OR operation
ref_63001 = ref_62706 # MOV operation
ref_63015 = (0x7 & ref_63001) # AND operation
ref_63139 = ref_63015 # MOV operation
ref_63153 = ((ref_63139 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_63312 = ref_49973 # MOV operation
ref_63316 = ref_63153 # MOV operation
ref_63318 = (ref_63316 | ref_63312) # OR operation
ref_63468 = ref_63318 # MOV operation
ref_66125 = ref_32800 # MOV operation
ref_66350 = ref_66125 # MOV operation
ref_66364 = (ref_66350 >> (0x4 & 0x3F)) # SHR operation
ref_66659 = ref_66364 # MOV operation
ref_66673 = (0xF & ref_66659) # AND operation
ref_67178 = ref_66673 # MOV operation
ref_67184 = (0x1 | ref_67178) # OR operation
ref_69038 = ref_63468 # MOV operation
ref_69263 = ref_69038 # MOV operation
ref_69275 = ref_67184 # MOV operation
ref_69277 = (ref_69263 >> ((ref_69275 & 0xFF) & 0x3F)) # SHR operation
ref_71823 = ref_32800 # MOV operation
ref_72048 = ref_71823 # MOV operation
ref_72062 = (ref_72048 >> (0x4 & 0x3F)) # SHR operation
ref_72357 = ref_72062 # MOV operation
ref_72371 = (0xF & ref_72357) # AND operation
ref_72876 = ref_72371 # MOV operation
ref_72882 = (0x1 | ref_72876) # OR operation
ref_73508 = ref_72882 # MOV operation
ref_73510 = ((0x40 - ref_73508) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_73518 = ref_73510 # MOV operation
ref_75367 = ref_63468 # MOV operation
ref_75466 = ref_75367 # MOV operation
ref_75478 = ref_73518 # MOV operation
ref_75480 = ((ref_75466 << ((ref_75478 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_75639 = ref_69277 # MOV operation
ref_75643 = ref_75480 # MOV operation
ref_75645 = (ref_75643 | ref_75639) # OR operation
ref_78191 = ref_19411 # MOV operation
ref_78416 = ref_78191 # MOV operation
ref_78430 = (ref_78416 >> (0x3 & 0x3F)) # SHR operation
ref_78725 = ref_78430 # MOV operation
ref_78739 = (0xF & ref_78725) # AND operation
ref_79244 = ref_78739 # MOV operation
ref_79250 = (0x1 | ref_79244) # OR operation
ref_81104 = ref_12346 # MOV operation
ref_81329 = ref_81104 # MOV operation
ref_81341 = ref_79250 # MOV operation
ref_81343 = (ref_81329 >> ((ref_81341 & 0xFF) & 0x3F)) # SHR operation
ref_83889 = ref_19411 # MOV operation
ref_84114 = ref_83889 # MOV operation
ref_84128 = (ref_84114 >> (0x3 & 0x3F)) # SHR operation
ref_84423 = ref_84128 # MOV operation
ref_84437 = (0xF & ref_84423) # AND operation
ref_84942 = ref_84437 # MOV operation
ref_84948 = (0x1 | ref_84942) # OR operation
ref_85574 = ref_84948 # MOV operation
ref_85576 = ((0x40 - ref_85574) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_85584 = ref_85576 # MOV operation
ref_87433 = ref_12346 # MOV operation
ref_87532 = ref_87433 # MOV operation
ref_87544 = ref_85584 # MOV operation
ref_87546 = ((ref_87532 << ((ref_87544 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_87705 = ref_81343 # MOV operation
ref_87709 = ref_87546 # MOV operation
ref_87711 = (ref_87709 | ref_87705) # OR operation
ref_87880 = ref_87711 # MOV operation
ref_87892 = ref_75645 # MOV operation
ref_87894 = ((ref_87880 - ref_87892) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_87896 = ((((ref_87880 ^ (ref_87892 ^ ref_87894)) ^ ((ref_87880 ^ ref_87894) & (ref_87880 ^ ref_87892))) >> 63) & 0x1) # Carry flag
ref_87900 = (0x1 if (ref_87894 == 0x0) else 0x0) # Zero flag
ref_87902 = ((((ref_87892 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (((~(ref_87896) & 0x1) & (~(ref_87900) & 0x1)) == 0x1) else 0x0)) # SETA operation
ref_87904 = (ref_87902 & 0xFF) # MOVZX operation
ref_88051 = (ref_87904 & 0xFFFFFFFF) # MOV operation
ref_88053 = ((ref_88051 & 0xFFFFFFFF) & (ref_88051 & 0xFFFFFFFF)) # TEST operation
ref_88058 = (0x1 if (ref_88053 == 0x0) else 0x0) # Zero flag
ref_88060 = (0x1925 if (ref_88058 == 0x1) else 0x1907) # Program Counter


if (ref_88058 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_9030 = ref_278 # MOV operation
    ref_9129 = ref_9030 # MOV operation
    ref_9143 = ((ref_9129 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_11528 = ref_278 # MOV operation
    ref_11753 = ref_11528 # MOV operation
    ref_11767 = (ref_11753 >> (0x35 & 0x3F)) # SHR operation
    ref_11926 = ref_9143 # MOV operation
    ref_11930 = ref_11767 # MOV operation
    ref_11932 = (ref_11930 | ref_11926) # OR operation
    ref_12182 = ref_11932 # MOV operation
    ref_12196 = (ref_12182 >> (0x1 & 0x3F)) # SHR operation
    ref_12346 = ref_12196 # MOV operation
    ref_15853 = ref_12346 # MOV operation
    ref_16396 = ref_15853 # MOV operation
    ref_16402 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_16396)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_18438 = ref_278 # MOV operation
    ref_18972 = ref_18438 # MOV operation
    ref_18980 = ((((0x0) << 64 | ref_18972) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_19244 = ref_18980 # MOV operation
    ref_19256 = ref_16402 # MOV operation
    ref_19258 = ((ref_19244 - ref_19256) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_19266 = ref_19258 # MOV operation
    ref_19411 = ref_19266 # MOV operation
    ref_23956 = ref_19411 # MOV operation
    ref_24181 = ref_23956 # MOV operation
    ref_24195 = (ref_24181 >> (0x7 & 0x3F)) # SHR operation
    ref_24445 = ref_24195 # MOV operation
    ref_24459 = (ref_24445 >> (0x2 & 0x3F)) # SHR operation
    ref_24754 = ref_24459 # MOV operation
    ref_24768 = (0x7 & ref_24754) # AND operation
    ref_25273 = ref_24768 # MOV operation
    ref_25279 = (0x1 | ref_25273) # OR operation
    ref_27664 = ref_278 # MOV operation
    ref_27916 = ref_27664 # MOV operation
    ref_27930 = ((0x9919884 + ref_27916) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_28181 = ref_27930 # MOV operation
    ref_28193 = ref_25279 # MOV operation
    ref_28195 = (ref_28181 >> ((ref_28193 & 0xFF) & 0x3F)) # SHR operation
    ref_28345 = ref_28195 # MOV operation
    ref_32383 = ref_278 # MOV operation
    ref_32635 = ref_32383 # MOV operation
    ref_32649 = ((0x1E5EA08F8 + ref_32635) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_32800 = ref_32649 # MOV operation
    ref_39645 = ref_28345 # MOV operation
    ref_42879 = ref_28345 # MOV operation
    ref_43149 = ref_42879 # MOV operation
    ref_43163 = (0x3F & ref_43149) # AND operation
    ref_43287 = ref_43163 # MOV operation
    ref_43301 = ((ref_43287 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_43460 = ref_39645 # MOV operation
    ref_43464 = ref_43301 # MOV operation
    ref_43466 = (ref_43464 | ref_43460) # OR operation
    ref_43616 = ref_43466 # MOV operation
    ref_49973 = ref_43616 # MOV operation
    ref_53186 = ref_19411 # MOV operation
    ref_53411 = ref_53186 # MOV operation
    ref_53425 = (ref_53411 >> (0x2 & 0x3F)) # SHR operation
    ref_53720 = ref_53425 # MOV operation
    ref_53734 = (0xF & ref_53720) # AND operation
    ref_54239 = ref_53734 # MOV operation
    ref_54245 = (0x1 | ref_54239) # OR operation
    ref_56099 = ref_12346 # MOV operation
    ref_56198 = ref_56099 # MOV operation
    ref_56210 = ref_54245 # MOV operation
    ref_56212 = ((ref_56198 << ((ref_56210 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_58758 = ref_19411 # MOV operation
    ref_58983 = ref_58758 # MOV operation
    ref_58997 = (ref_58983 >> (0x2 & 0x3F)) # SHR operation
    ref_59292 = ref_58997 # MOV operation
    ref_59306 = (0xF & ref_59292) # AND operation
    ref_59811 = ref_59306 # MOV operation
    ref_59817 = (0x1 | ref_59811) # OR operation
    ref_60443 = ref_59817 # MOV operation
    ref_60445 = ((0x40 - ref_60443) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_60453 = ref_60445 # MOV operation
    ref_62302 = ref_12346 # MOV operation
    ref_62527 = ref_62302 # MOV operation
    ref_62539 = ref_60453 # MOV operation
    ref_62541 = (ref_62527 >> ((ref_62539 & 0xFF) & 0x3F)) # SHR operation
    ref_62700 = ref_56212 # MOV operation
    ref_62704 = ref_62541 # MOV operation
    ref_62706 = (ref_62704 | ref_62700) # OR operation
    ref_63001 = ref_62706 # MOV operation
    ref_63015 = (0x7 & ref_63001) # AND operation
    ref_63139 = ref_63015 # MOV operation
    ref_63153 = ((ref_63139 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_63312 = ref_49973 # MOV operation
    ref_63316 = ref_63153 # MOV operation
    ref_63318 = (ref_63316 | ref_63312) # OR operation
    ref_63468 = ref_63318 # MOV operation
    ref_91692 = ref_19411 # MOV operation
    ref_94213 = ref_19411 # MOV operation
    ref_94483 = ref_94213 # MOV operation
    ref_94497 = (0xF & ref_94483) # AND operation
    ref_94621 = ref_94497 # MOV operation
    ref_94635 = ((ref_94621 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_94794 = ref_91692 # MOV operation
    ref_94798 = ref_94635 # MOV operation
    ref_94800 = (ref_94798 | ref_94794) # OR operation
    ref_94950 = ref_94800 # MOV operation
    ref_98457 = ref_12346 # MOV operation
    ref_100978 = ref_94950 # MOV operation
    ref_102807 = ref_63468 # MOV operation
    ref_103077 = ref_102807 # MOV operation
    ref_103089 = ref_100978 # MOV operation
    ref_103091 = (ref_103089 & ref_103077) # AND operation
    ref_103386 = ref_103091 # MOV operation
    ref_103400 = (0x1F & ref_103386) # AND operation
    ref_103524 = ref_103400 # MOV operation
    ref_103538 = ((ref_103524 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_103697 = ref_98457 # MOV operation
    ref_103701 = ref_103538 # MOV operation
    ref_103703 = (ref_103701 | ref_103697) # OR operation
    ref_103853 = ref_103703 # MOV operation
    ref_107670 = ref_103853 # MOV operation
    ref_109499 = ref_94950 # MOV operation
    ref_109633 = ref_107670 # MOV operation
    ref_109637 = ref_109499 # MOV operation
    ref_109639 = (ref_109637 | ref_109633) # OR operation
    ref_111493 = ref_63468 # MOV operation
    ref_113322 = ref_32800 # MOV operation
    ref_113519 = ref_111493 # MOV operation
    ref_113523 = ref_113322 # MOV operation
    ref_113525 = (((sx(0x40, ref_113523) * sx(0x40, ref_113519)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_113744 = ref_109639 # MOV operation
    ref_113748 = ref_113525 # MOV operation
    ref_113750 = (((sx(0x40, ref_113748) * sx(0x40, ref_113744)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_113897 = ref_113750 # MOV operation
    ref_114154 = ref_113897 # MOV operation
    ref_114156 = ref_114154 # MOV operation
    endb = ref_114156


else:
    ref_114476 = SymVar_0
    ref_114491 = ref_114476 # MOV operation
    ref_123248 = ref_114491 # MOV operation
    ref_123347 = ref_123248 # MOV operation
    ref_123361 = ((ref_123347 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_125746 = ref_114491 # MOV operation
    ref_125971 = ref_125746 # MOV operation
    ref_125985 = (ref_125971 >> (0x35 & 0x3F)) # SHR operation
    ref_126144 = ref_123361 # MOV operation
    ref_126148 = ref_125985 # MOV operation
    ref_126150 = (ref_126148 | ref_126144) # OR operation
    ref_126400 = ref_126150 # MOV operation
    ref_126414 = (ref_126400 >> (0x1 & 0x3F)) # SHR operation
    ref_126564 = ref_126414 # MOV operation
    ref_130071 = ref_126564 # MOV operation
    ref_130614 = ref_130071 # MOV operation
    ref_130620 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_130614)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_132656 = ref_114491 # MOV operation
    ref_133190 = ref_132656 # MOV operation
    ref_133198 = ((((0x0) << 64 | ref_133190) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_133462 = ref_133198 # MOV operation
    ref_133474 = ref_130620 # MOV operation
    ref_133476 = ((ref_133462 - ref_133474) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_133484 = ref_133476 # MOV operation
    ref_133629 = ref_133484 # MOV operation
    ref_138174 = ref_133629 # MOV operation
    ref_138399 = ref_138174 # MOV operation
    ref_138413 = (ref_138399 >> (0x7 & 0x3F)) # SHR operation
    ref_138663 = ref_138413 # MOV operation
    ref_138677 = (ref_138663 >> (0x2 & 0x3F)) # SHR operation
    ref_138972 = ref_138677 # MOV operation
    ref_138986 = (0x7 & ref_138972) # AND operation
    ref_139491 = ref_138986 # MOV operation
    ref_139497 = (0x1 | ref_139491) # OR operation
    ref_141882 = ref_114491 # MOV operation
    ref_142134 = ref_141882 # MOV operation
    ref_142148 = ((0x9919884 + ref_142134) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_142399 = ref_142148 # MOV operation
    ref_142411 = ref_139497 # MOV operation
    ref_142413 = (ref_142399 >> ((ref_142411 & 0xFF) & 0x3F)) # SHR operation
    ref_142563 = ref_142413 # MOV operation
    ref_146601 = ref_114491 # MOV operation
    ref_146853 = ref_146601 # MOV operation
    ref_146867 = ((0x1E5EA08F8 + ref_146853) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_147018 = ref_146867 # MOV operation
    ref_153863 = ref_142563 # MOV operation
    ref_157097 = ref_142563 # MOV operation
    ref_157367 = ref_157097 # MOV operation
    ref_157381 = (0x3F & ref_157367) # AND operation
    ref_157505 = ref_157381 # MOV operation
    ref_157519 = ((ref_157505 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_157678 = ref_153863 # MOV operation
    ref_157682 = ref_157519 # MOV operation
    ref_157684 = (ref_157682 | ref_157678) # OR operation
    ref_157834 = ref_157684 # MOV operation
    ref_164191 = ref_157834 # MOV operation
    ref_167404 = ref_133629 # MOV operation
    ref_167629 = ref_167404 # MOV operation
    ref_167643 = (ref_167629 >> (0x2 & 0x3F)) # SHR operation
    ref_167938 = ref_167643 # MOV operation
    ref_167952 = (0xF & ref_167938) # AND operation
    ref_168457 = ref_167952 # MOV operation
    ref_168463 = (0x1 | ref_168457) # OR operation
    ref_170317 = ref_126564 # MOV operation
    ref_170416 = ref_170317 # MOV operation
    ref_170428 = ref_168463 # MOV operation
    ref_170430 = ((ref_170416 << ((ref_170428 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_172976 = ref_133629 # MOV operation
    ref_173201 = ref_172976 # MOV operation
    ref_173215 = (ref_173201 >> (0x2 & 0x3F)) # SHR operation
    ref_173510 = ref_173215 # MOV operation
    ref_173524 = (0xF & ref_173510) # AND operation
    ref_174029 = ref_173524 # MOV operation
    ref_174035 = (0x1 | ref_174029) # OR operation
    ref_174661 = ref_174035 # MOV operation
    ref_174663 = ((0x40 - ref_174661) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_174671 = ref_174663 # MOV operation
    ref_176520 = ref_126564 # MOV operation
    ref_176745 = ref_176520 # MOV operation
    ref_176757 = ref_174671 # MOV operation
    ref_176759 = (ref_176745 >> ((ref_176757 & 0xFF) & 0x3F)) # SHR operation
    ref_176918 = ref_170430 # MOV operation
    ref_176922 = ref_176759 # MOV operation
    ref_176924 = (ref_176922 | ref_176918) # OR operation
    ref_177219 = ref_176924 # MOV operation
    ref_177233 = (0x7 & ref_177219) # AND operation
    ref_177357 = ref_177233 # MOV operation
    ref_177371 = ((ref_177357 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_177530 = ref_164191 # MOV operation
    ref_177534 = ref_177371 # MOV operation
    ref_177536 = (ref_177534 | ref_177530) # OR operation
    ref_177686 = ref_177536 # MOV operation
    ref_177688 = ((ref_177686 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_177689 = ((ref_177686 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_177690 = ((ref_177686 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_177691 = ((ref_177686 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_177692 = ((ref_177686 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_177693 = ((ref_177686 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_177694 = ((ref_177686 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_177695 = (ref_177686 & 0xFF) # Byte reference - MOV operation
    ref_206493 = ref_147018 # MOV operation
    ref_206718 = ref_206493 # MOV operation
    ref_206732 = (ref_206718 >> (0x3 & 0x3F)) # SHR operation
    ref_207027 = ref_206732 # MOV operation
    ref_207041 = (0xF & ref_207027) # AND operation
    ref_207546 = ref_207041 # MOV operation
    ref_207552 = (0x1 | ref_207546) # OR operation
    ref_209406 = ref_147018 # MOV operation
    ref_209505 = ref_209406 # MOV operation
    ref_209517 = ref_207552 # MOV operation
    ref_209519 = ((ref_209505 << ((ref_209517 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_212065 = ref_147018 # MOV operation
    ref_212290 = ref_212065 # MOV operation
    ref_212304 = (ref_212290 >> (0x3 & 0x3F)) # SHR operation
    ref_212599 = ref_212304 # MOV operation
    ref_212613 = (0xF & ref_212599) # AND operation
    ref_213118 = ref_212613 # MOV operation
    ref_213124 = (0x1 | ref_213118) # OR operation
    ref_213750 = ref_213124 # MOV operation
    ref_213752 = ((0x40 - ref_213750) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_213760 = ref_213752 # MOV operation
    ref_215609 = ref_147018 # MOV operation
    ref_215834 = ref_215609 # MOV operation
    ref_215846 = ref_213760 # MOV operation
    ref_215848 = (ref_215834 >> ((ref_215846 & 0xFF) & 0x3F)) # SHR operation
    ref_216007 = ref_209519 # MOV operation
    ref_216011 = ref_215848 # MOV operation
    ref_216013 = (ref_216011 | ref_216007) # OR operation
    ref_216163 = ref_216013 # MOV operation
    ref_219368 = ref_177694 # MOVZX operation
    ref_219906 = (ref_219368 & 0xFF) # MOVZX operation
    ref_223103 = ref_177692 # MOVZX operation
    ref_226423 = (ref_223103 & 0xFF) # MOVZX operation
    ref_226425 = (ref_226423 & 0xFF) # Byte reference - MOV operation
    ref_226838 = (ref_219906 & 0xFF) # MOVZX operation
    ref_230158 = (ref_226838 & 0xFF) # MOVZX operation
    ref_230160 = (ref_230158 & 0xFF) # Byte reference - MOV operation
    ref_233967 = ref_216163 # MOV operation
    ref_235796 = ref_133629 # MOV operation
    ref_235930 = ref_233967 # MOV operation
    ref_235934 = ref_235796 # MOV operation
    ref_235936 = (ref_235934 | ref_235930) # OR operation
    ref_237790 = ((((((((ref_177688) << 8 | ref_177689) << 8 | ref_177690) << 8 | ref_177691) << 8 | ref_230160) << 8 | ref_177693) << 8 | ref_226425) << 8 | ref_177695) # MOV operation
    ref_239619 = ref_147018 # MOV operation
    ref_239816 = ref_237790 # MOV operation
    ref_239820 = ref_239619 # MOV operation
    ref_239822 = (((sx(0x40, ref_239820) * sx(0x40, ref_239816)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_240041 = ref_235936 # MOV operation
    ref_240045 = ref_239822 # MOV operation
    ref_240047 = (((sx(0x40, ref_240045) * sx(0x40, ref_240041)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_240194 = ref_240047 # MOV operation
    ref_240451 = ref_240194 # MOV operation
    ref_240453 = ref_240451 # MOV operation
    endb = ref_240453


print endb & 0xffffffffffffffff
