#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5594 = ref_278 # MOV operation
ref_5670 = ref_5594 # MOV operation
ref_5684 = (ref_5670 >> (0x5 & 0x3F)) # SHR operation
ref_5909 = ref_5684 # MOV operation
ref_5915 = (0x1376783EF7559EA & ref_5909) # AND operation
ref_6846 = ref_5915 # MOV operation
ref_6848 = ((ref_6846 >> 56) & 0xFF) # Byte reference - MOV operation
ref_6849 = ((ref_6846 >> 48) & 0xFF) # Byte reference - MOV operation
ref_6850 = ((ref_6846 >> 40) & 0xFF) # Byte reference - MOV operation
ref_6851 = ((ref_6846 >> 32) & 0xFF) # Byte reference - MOV operation
ref_6852 = ((ref_6846 >> 24) & 0xFF) # Byte reference - MOV operation
ref_6853 = ((ref_6846 >> 16) & 0xFF) # Byte reference - MOV operation
ref_6854 = ((ref_6846 >> 8) & 0xFF) # Byte reference - MOV operation
ref_6855 = (ref_6846 & 0xFF) # Byte reference - MOV operation
ref_7764 = ref_6846 # MOV operation
ref_7964 = ref_7764 # MOV operation
ref_7970 = (0x7063FB7 & ref_7964) # AND operation
ref_8924 = ref_278 # MOV operation
ref_9000 = ref_8924 # MOV operation
ref_9014 = (0x1A5612E2 | ref_9000) # OR operation
ref_9115 = ref_9014 # MOV operation
ref_9127 = ref_7970 # MOV operation
ref_9129 = ((ref_9127 + ref_9115) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10061 = ref_9129 # MOV operation
ref_10063 = ((ref_10061 >> 56) & 0xFF) # Byte reference - MOV operation
ref_10064 = ((ref_10061 >> 48) & 0xFF) # Byte reference - MOV operation
ref_10065 = ((ref_10061 >> 40) & 0xFF) # Byte reference - MOV operation
ref_10066 = ((ref_10061 >> 32) & 0xFF) # Byte reference - MOV operation
ref_10067 = ((ref_10061 >> 24) & 0xFF) # Byte reference - MOV operation
ref_10068 = ((ref_10061 >> 16) & 0xFF) # Byte reference - MOV operation
ref_10069 = ((ref_10061 >> 8) & 0xFF) # Byte reference - MOV operation
ref_10070 = (ref_10061 & 0xFF) # Byte reference - MOV operation
ref_11443 = ref_10061 # MOV operation
ref_11519 = ref_11443 # MOV operation
ref_11533 = (ref_11519 >> (0x3 & 0x3F)) # SHR operation
ref_11758 = ref_11533 # MOV operation
ref_11764 = (0xF & ref_11758) # AND operation
ref_11865 = ref_11764 # MOV operation
ref_11879 = (0x1 | ref_11865) # OR operation
ref_12108 = ref_11879 # MOV operation
ref_12110 = ((0x40 - ref_12108) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_12118 = ref_12110 # MOV operation
ref_12342 = ref_12118 # MOV operation
ref_12344 = (0x3162E74F >> ((ref_12342 & 0xFF) & 0x3F)) # SHR operation
ref_13499 = ref_10061 # MOV operation
ref_13575 = ref_13499 # MOV operation
ref_13589 = (ref_13575 >> (0x3 & 0x3F)) # SHR operation
ref_13814 = ref_13589 # MOV operation
ref_13820 = (0xF & ref_13814) # AND operation
ref_13921 = ref_13820 # MOV operation
ref_13935 = (0x1 | ref_13921) # OR operation
ref_14164 = ref_13935 # MOV operation
ref_14166 = ((0x3162E74F << ((ref_14164 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14267 = ref_14166 # MOV operation
ref_14279 = ref_12344 # MOV operation
ref_14281 = (ref_14279 | ref_14267) # OR operation
ref_14382 = ref_14281 # MOV operation
ref_14396 = (ref_14382 >> (0x4 & 0x3F)) # SHR operation
ref_14621 = ref_14396 # MOV operation
ref_14627 = (0x7 & ref_14621) # AND operation
ref_14728 = ref_14627 # MOV operation
ref_14742 = (0x1 | ref_14728) # OR operation
ref_15696 = ref_278 # MOV operation
ref_15772 = ref_15696 # MOV operation
ref_15786 = ((ref_15772 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15794 = ref_15786 # MOV operation
ref_15890 = ref_15794 # MOV operation
ref_15902 = ref_14742 # MOV operation
ref_15904 = ((ref_15890 << ((ref_15902 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_16835 = ref_15904 # MOV operation
ref_17784 = ref_278 # MOV operation
ref_17860 = ref_17784 # MOV operation
ref_17874 = ((ref_17860 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_17882 = ref_17874 # MOV operation
ref_18808 = ref_17882 # MOV operation
ref_21147 = ref_10061 # MOV operation
ref_21347 = ref_21147 # MOV operation
ref_21353 = (0xF & ref_21347) # AND operation
ref_21454 = ref_21353 # MOV operation
ref_21468 = ((ref_21454 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_22391 = ref_18808 # MOV operation
ref_22467 = ref_22391 # MOV operation
ref_22479 = ref_21468 # MOV operation
ref_22481 = (ref_22479 | ref_22467) # OR operation
ref_23412 = ref_22481 # MOV operation
ref_24446 = ref_23412 # MOV operation
ref_24646 = ref_24446 # MOV operation
ref_24652 = (0x1F & ref_24646) # AND operation
ref_24753 = ref_24652 # MOV operation
ref_24767 = ((ref_24753 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_25690 = ref_16835 # MOV operation
ref_25766 = ref_25690 # MOV operation
ref_25778 = ref_24767 # MOV operation
ref_25780 = (ref_25778 | ref_25766) # OR operation
ref_26711 = ref_25780 # MOV operation
ref_28065 = ref_10061 # MOV operation
ref_28265 = ref_28065 # MOV operation
ref_28271 = (0xF & ref_28265) # AND operation
ref_28372 = ref_28271 # MOV operation
ref_28386 = ((ref_28372 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_29309 = ref_23412 # MOV operation
ref_29385 = ref_29309 # MOV operation
ref_29397 = ref_28386 # MOV operation
ref_29399 = (ref_29397 | ref_29385) # OR operation
ref_30330 = ref_29399 # MOV operation
ref_32989 = ref_30330 # MOV operation
ref_33189 = ref_32989 # MOV operation
ref_33195 = (0xF & ref_33189) # AND operation
ref_33296 = ref_33195 # MOV operation
ref_33310 = ((ref_33296 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_34233 = ref_30330 # MOV operation
ref_34309 = ref_34233 # MOV operation
ref_34321 = ref_33310 # MOV operation
ref_34323 = (ref_34321 | ref_34309) # OR operation
ref_35254 = ref_34323 # MOV operation
ref_36288 = ref_35254 # MOV operation
ref_36488 = ref_36288 # MOV operation
ref_36494 = (0x1F & ref_36488) # AND operation
ref_36595 = ref_36494 # MOV operation
ref_36609 = ((ref_36595 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_37532 = ref_26711 # MOV operation
ref_37608 = ref_37532 # MOV operation
ref_37620 = ref_36609 # MOV operation
ref_37622 = (ref_37620 | ref_37608) # OR operation
ref_38553 = ref_37622 # MOV operation
ref_38555 = ((ref_38553 >> 56) & 0xFF) # Byte reference - MOV operation
ref_38556 = ((ref_38553 >> 48) & 0xFF) # Byte reference - MOV operation
ref_38557 = ((ref_38553 >> 40) & 0xFF) # Byte reference - MOV operation
ref_38558 = ((ref_38553 >> 32) & 0xFF) # Byte reference - MOV operation
ref_38559 = ((ref_38553 >> 24) & 0xFF) # Byte reference - MOV operation
ref_38560 = ((ref_38553 >> 16) & 0xFF) # Byte reference - MOV operation
ref_38561 = ((ref_38553 >> 8) & 0xFF) # Byte reference - MOV operation
ref_38562 = (ref_38553 & 0xFF) # Byte reference - MOV operation
ref_39907 = ref_35254 # MOV operation
ref_40107 = ref_39907 # MOV operation
ref_40113 = (0xF & ref_40107) # AND operation
ref_40214 = ref_40113 # MOV operation
ref_40228 = ((ref_40214 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_41151 = ref_35254 # MOV operation
ref_41227 = ref_41151 # MOV operation
ref_41239 = ref_40228 # MOV operation
ref_41241 = (ref_41239 | ref_41227) # OR operation
ref_42172 = ref_41241 # MOV operation
ref_49420 = ref_38553 # MOV operation
ref_50318 = ref_38553 # MOV operation
ref_50394 = ref_50318 # MOV operation
ref_50406 = ref_49420 # MOV operation
ref_50408 = ((ref_50406 + ref_50394) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_50634 = ref_50408 # MOV operation
ref_50640 = (0x7 & ref_50634) # AND operation
ref_50741 = ref_50640 # MOV operation
ref_50755 = ((ref_50741 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_51678 = ref_42172 # MOV operation
ref_51754 = ref_51678 # MOV operation
ref_51766 = ref_50755 # MOV operation
ref_51768 = (ref_51766 | ref_51754) # OR operation
ref_52699 = ref_51768 # MOV operation
ref_54223 = ((((ref_38555) << 8 | ref_38556) << 8 | ref_38557) << 8 | ref_38558) # MOV operation
ref_54431 = (ref_54223 & 0xFFFFFFFF) # MOV operation
ref_55951 = ((((ref_38559) << 8 | ref_38560) << 8 | ref_38561) << 8 | ref_38562) # MOV operation
ref_57459 = (ref_55951 & 0xFFFFFFFF) # MOV operation
ref_57461 = (((ref_57459 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_57462 = (((ref_57459 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_57463 = (((ref_57459 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_57464 = ((ref_57459 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_57679 = (ref_54431 & 0xFFFFFFFF) # MOV operation
ref_59187 = (ref_57679 & 0xFFFFFFFF) # MOV operation
ref_59189 = (((ref_59187 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_59190 = (((ref_59187 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_59191 = (((ref_59187 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_59192 = ((ref_59187 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_60707 = ref_6850 # MOVZX operation
ref_60911 = (ref_60707 & 0xFF) # MOVZX operation
ref_62427 = ref_6851 # MOVZX operation
ref_63931 = (ref_62427 & 0xFF) # MOVZX operation
ref_63933 = (ref_63931 & 0xFF) # Byte reference - MOV operation
ref_64147 = (ref_60911 & 0xFF) # MOVZX operation
ref_65651 = (ref_64147 & 0xFF) # MOVZX operation
ref_65653 = (ref_65651 & 0xFF) # Byte reference - MOV operation
ref_67167 = ref_6849 # MOVZX operation
ref_67371 = (ref_67167 & 0xFF) # MOVZX operation
ref_68887 = ref_6855 # MOVZX operation
ref_70391 = (ref_68887 & 0xFF) # MOVZX operation
ref_70393 = (ref_70391 & 0xFF) # Byte reference - MOV operation
ref_70607 = (ref_67371 & 0xFF) # MOVZX operation
ref_72111 = (ref_70607 & 0xFF) # MOVZX operation
ref_72113 = (ref_72111 & 0xFF) # Byte reference - MOV operation
ref_73627 = ((((ref_10067) << 8 | ref_10068) << 8 | ref_10069) << 8 | ref_10070) # MOV operation
ref_73835 = (ref_73627 & 0xFFFFFFFF) # MOV operation
ref_75355 = ((((ref_10063) << 8 | ref_10064) << 8 | ref_10065) << 8 | ref_10066) # MOV operation
ref_76863 = (ref_75355 & 0xFFFFFFFF) # MOV operation
ref_76865 = (((ref_76863 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_76866 = (((ref_76863 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_76867 = (((ref_76863 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_76868 = ((ref_76863 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_77083 = (ref_73835 & 0xFFFFFFFF) # MOV operation
ref_78591 = (ref_77083 & 0xFFFFFFFF) # MOV operation
ref_78593 = (((ref_78591 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_78594 = (((ref_78591 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_78595 = (((ref_78591 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_78596 = ((ref_78591 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_81010 = ((((((((ref_6848) << 8 | ref_70393) << 8 | ref_63933) << 8 | ref_65653) << 8 | ref_6852) << 8 | ref_6853) << 8 | ref_6854) << 8 | ref_72113) # MOV operation
ref_81210 = ref_81010 # MOV operation
ref_81216 = (0x3F & ref_81210) # AND operation
ref_81317 = ref_81216 # MOV operation
ref_81331 = ((ref_81317 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_82342 = ((((((((ref_78593) << 8 | ref_78594) << 8 | ref_78595) << 8 | ref_78596) << 8 | ref_76865) << 8 | ref_76866) << 8 | ref_76867) << 8 | ref_76868) # MOV operation
ref_82418 = ref_82342 # MOV operation
ref_82430 = ref_81331 # MOV operation
ref_82432 = (ref_82430 | ref_82418) # OR operation
ref_83451 = ref_82432 # MOV operation
ref_86183 = ref_83451 # MOV operation
ref_86259 = ref_86183 # MOV operation
ref_86273 = (ref_86259 >> (0x3 & 0x3F)) # SHR operation
ref_86498 = ref_86273 # MOV operation
ref_86504 = (0xF & ref_86498) # AND operation
ref_86605 = ref_86504 # MOV operation
ref_86619 = (0x1 | ref_86605) # OR operation
ref_86848 = ref_86619 # MOV operation
ref_86850 = ((0x40 - ref_86848) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_86858 = ref_86850 # MOV operation
ref_87776 = ref_52699 # MOV operation
ref_87852 = ref_87776 # MOV operation
ref_87864 = ref_86858 # MOV operation
ref_87866 = ((ref_87852 << ((ref_87864 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_89021 = ref_83451 # MOV operation
ref_89097 = ref_89021 # MOV operation
ref_89111 = (ref_89097 >> (0x3 & 0x3F)) # SHR operation
ref_89336 = ref_89111 # MOV operation
ref_89342 = (0xF & ref_89336) # AND operation
ref_89443 = ref_89342 # MOV operation
ref_89457 = (0x1 | ref_89443) # OR operation
ref_90380 = ref_52699 # MOV operation
ref_90456 = ref_90380 # MOV operation
ref_90468 = ref_89457 # MOV operation
ref_90470 = (ref_90456 >> ((ref_90468 & 0xFF) & 0x3F)) # SHR operation
ref_90571 = ref_90470 # MOV operation
ref_90583 = ref_87866 # MOV operation
ref_90585 = (ref_90583 | ref_90571) # OR operation
ref_90810 = ref_90585 # MOV operation
ref_90816 = (0xF & ref_90810) # AND operation
ref_90917 = ref_90816 # MOV operation
ref_90931 = ((ref_90917 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_91854 = ((((((((ref_57461) << 8 | ref_57462) << 8 | ref_57463) << 8 | ref_57464) << 8 | ref_59189) << 8 | ref_59190) << 8 | ref_59191) << 8 | ref_59192) # MOV operation
ref_91930 = ref_91854 # MOV operation
ref_91942 = ref_90931 # MOV operation
ref_91944 = (ref_91942 | ref_91930) # OR operation
ref_92875 = ref_91944 # MOV operation
ref_93793 = ref_52699 # MOV operation
ref_94691 = ref_92875 # MOV operation
ref_94767 = ref_94691 # MOV operation
ref_94779 = ref_93793 # MOV operation
ref_94781 = (ref_94779 | ref_94767) # OR operation
ref_95936 = ref_83451 # MOV operation
ref_96012 = ref_95936 # MOV operation
ref_96026 = (ref_96012 >> (0x3 & 0x3F)) # SHR operation
ref_96251 = ref_96026 # MOV operation
ref_96257 = (0x7 & ref_96251) # AND operation
ref_96358 = ref_96257 # MOV operation
ref_96372 = (0x1 | ref_96358) # OR operation
ref_97295 = ((((((((ref_6848) << 8 | ref_70393) << 8 | ref_63933) << 8 | ref_65653) << 8 | ref_6852) << 8 | ref_6853) << 8 | ref_6854) << 8 | ref_72113) # MOV operation
ref_97371 = ref_97295 # MOV operation
ref_97383 = ref_96372 # MOV operation
ref_97385 = ((ref_97371 << ((ref_97383 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_97486 = ref_97385 # MOV operation
ref_97498 = ref_94781 # MOV operation
ref_97500 = (ref_97498 | ref_97486) # OR operation
ref_98355 = ref_97500 # MOV operation
ref_98566 = ref_98355 # MOV operation
ref_98568 = ref_98566 # MOV operation

print ref_98568 & 0xffffffffffffffff
