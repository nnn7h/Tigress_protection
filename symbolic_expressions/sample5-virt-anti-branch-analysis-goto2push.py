#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_215 = SymVar_0
ref_226 = ref_215 # MOV operation
ref_238 = ref_226 # MOV operation
ref_240 = ref_238 # MOV operation
ref_274 = ((ref_240 >> 56) & 0xFF) # Byte reference - MOV operation
ref_275 = ((ref_240 >> 48) & 0xFF) # Byte reference - MOV operation
ref_276 = ((ref_240 >> 40) & 0xFF) # Byte reference - MOV operation
ref_277 = ((ref_240 >> 32) & 0xFF) # Byte reference - MOV operation
ref_278 = ((ref_240 >> 24) & 0xFF) # Byte reference - MOV operation
ref_279 = ((ref_240 >> 16) & 0xFF) # Byte reference - MOV operation
ref_280 = ((ref_240 >> 8) & 0xFF) # Byte reference - MOV operation
ref_281 = (ref_240 & 0xFF) # Byte reference - MOV operation
ref_22629 = ref_281 # MOVZX operation
ref_22734 = (ref_22629 & 0xFF) # MOVZX operation
ref_22736 = (ref_22734 & 0xFF) # MOVZX operation
ref_23137 = (ref_22736 & 0xFFFFFFFF) # MOV operation
ref_23139 = (((ref_23137 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_23284 = (ref_23139 & 0xFFFFFFFF) # MOV operation
ref_23749 = (ref_23284 & 0xFFFFFFFF) # MOV operation
ref_24019 = (ref_23749 & 0xFFFFFFFF) # MOV operation
ref_24027 = (((ref_24019 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_24034 = (ref_24027 & 0xFFFFFFFF) # MOV operation
ref_24332 = (ref_23284 & 0xFFFFFFFF) # MOV operation
ref_24443 = (ref_24332 & 0xFFFFFFFF) # MOV operation
ref_24455 = (ref_24034 & 0xFFFFFFFF) # MOV operation
ref_24457 = (((ref_24455 & 0xFFFFFFFF) + (ref_24443 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_24602 = (ref_24457 & 0xFFFFFFFF) # MOV operation
ref_25067 = (ref_24602 & 0xFFFFFFFF) # MOV operation
ref_25496 = (ref_24602 & 0xFFFFFFFF) # MOV operation
ref_25607 = (ref_25496 & 0xFFFFFFFF) # MOV operation
ref_25623 = ((ref_25607 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_25630 = (ref_25623 & 0xFFFFFFFF) # MOV operation
ref_25769 = (ref_25067 & 0xFFFFFFFF) # MOV operation
ref_25773 = (ref_25630 & 0xFFFFFFFF) # MOV operation
ref_25775 = ((ref_25773 & 0xFFFFFFFF) ^ (ref_25769 & 0xFFFFFFFF)) # XOR operation
ref_25919 = (ref_25775 & 0xFFFFFFFF) # MOV operation
ref_29884 = ref_280 # MOVZX operation
ref_29989 = (ref_29884 & 0xFF) # MOVZX operation
ref_29991 = (ref_29989 & 0xFF) # MOVZX operation
ref_30269 = (ref_25919 & 0xFFFFFFFF) # MOV operation
ref_30380 = (ref_30269 & 0xFFFFFFFF) # MOV operation
ref_30392 = (ref_29991 & 0xFFFFFFFF) # MOV operation
ref_30394 = (((ref_30392 & 0xFFFFFFFF) + (ref_30380 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_30539 = (ref_30394 & 0xFFFFFFFF) # MOV operation
ref_31004 = (ref_30539 & 0xFFFFFFFF) # MOV operation
ref_31274 = (ref_31004 & 0xFFFFFFFF) # MOV operation
ref_31282 = (((ref_31274 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_31289 = (ref_31282 & 0xFFFFFFFF) # MOV operation
ref_31587 = (ref_30539 & 0xFFFFFFFF) # MOV operation
ref_31698 = (ref_31587 & 0xFFFFFFFF) # MOV operation
ref_31710 = (ref_31289 & 0xFFFFFFFF) # MOV operation
ref_31712 = (((ref_31710 & 0xFFFFFFFF) + (ref_31698 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_31857 = (ref_31712 & 0xFFFFFFFF) # MOV operation
ref_32322 = (ref_31857 & 0xFFFFFFFF) # MOV operation
ref_32751 = (ref_31857 & 0xFFFFFFFF) # MOV operation
ref_32862 = (ref_32751 & 0xFFFFFFFF) # MOV operation
ref_32878 = ((ref_32862 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_32885 = (ref_32878 & 0xFFFFFFFF) # MOV operation
ref_33024 = (ref_32322 & 0xFFFFFFFF) # MOV operation
ref_33028 = (ref_32885 & 0xFFFFFFFF) # MOV operation
ref_33030 = ((ref_33028 & 0xFFFFFFFF) ^ (ref_33024 & 0xFFFFFFFF)) # XOR operation
ref_33174 = (ref_33030 & 0xFFFFFFFF) # MOV operation
ref_37139 = ref_279 # MOVZX operation
ref_37244 = (ref_37139 & 0xFF) # MOVZX operation
ref_37246 = (ref_37244 & 0xFF) # MOVZX operation
ref_37524 = (ref_33174 & 0xFFFFFFFF) # MOV operation
ref_37635 = (ref_37524 & 0xFFFFFFFF) # MOV operation
ref_37647 = (ref_37246 & 0xFFFFFFFF) # MOV operation
ref_37649 = (((ref_37647 & 0xFFFFFFFF) + (ref_37635 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_37794 = (ref_37649 & 0xFFFFFFFF) # MOV operation
ref_38259 = (ref_37794 & 0xFFFFFFFF) # MOV operation
ref_38529 = (ref_38259 & 0xFFFFFFFF) # MOV operation
ref_38537 = (((ref_38529 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_38544 = (ref_38537 & 0xFFFFFFFF) # MOV operation
ref_38842 = (ref_37794 & 0xFFFFFFFF) # MOV operation
ref_38953 = (ref_38842 & 0xFFFFFFFF) # MOV operation
ref_38965 = (ref_38544 & 0xFFFFFFFF) # MOV operation
ref_38967 = (((ref_38965 & 0xFFFFFFFF) + (ref_38953 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_39112 = (ref_38967 & 0xFFFFFFFF) # MOV operation
ref_39577 = (ref_39112 & 0xFFFFFFFF) # MOV operation
ref_40006 = (ref_39112 & 0xFFFFFFFF) # MOV operation
ref_40117 = (ref_40006 & 0xFFFFFFFF) # MOV operation
ref_40133 = ((ref_40117 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_40140 = (ref_40133 & 0xFFFFFFFF) # MOV operation
ref_40279 = (ref_39577 & 0xFFFFFFFF) # MOV operation
ref_40283 = (ref_40140 & 0xFFFFFFFF) # MOV operation
ref_40285 = ((ref_40283 & 0xFFFFFFFF) ^ (ref_40279 & 0xFFFFFFFF)) # XOR operation
ref_40429 = (ref_40285 & 0xFFFFFFFF) # MOV operation
ref_44394 = ref_278 # MOVZX operation
ref_44499 = (ref_44394 & 0xFF) # MOVZX operation
ref_44501 = (ref_44499 & 0xFF) # MOVZX operation
ref_44779 = (ref_40429 & 0xFFFFFFFF) # MOV operation
ref_44890 = (ref_44779 & 0xFFFFFFFF) # MOV operation
ref_44902 = (ref_44501 & 0xFFFFFFFF) # MOV operation
ref_44904 = (((ref_44902 & 0xFFFFFFFF) + (ref_44890 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_45049 = (ref_44904 & 0xFFFFFFFF) # MOV operation
ref_45514 = (ref_45049 & 0xFFFFFFFF) # MOV operation
ref_45784 = (ref_45514 & 0xFFFFFFFF) # MOV operation
ref_45792 = (((ref_45784 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_45799 = (ref_45792 & 0xFFFFFFFF) # MOV operation
ref_46097 = (ref_45049 & 0xFFFFFFFF) # MOV operation
ref_46208 = (ref_46097 & 0xFFFFFFFF) # MOV operation
ref_46220 = (ref_45799 & 0xFFFFFFFF) # MOV operation
ref_46222 = (((ref_46220 & 0xFFFFFFFF) + (ref_46208 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_46367 = (ref_46222 & 0xFFFFFFFF) # MOV operation
ref_46832 = (ref_46367 & 0xFFFFFFFF) # MOV operation
ref_47261 = (ref_46367 & 0xFFFFFFFF) # MOV operation
ref_47372 = (ref_47261 & 0xFFFFFFFF) # MOV operation
ref_47388 = ((ref_47372 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_47395 = (ref_47388 & 0xFFFFFFFF) # MOV operation
ref_47534 = (ref_46832 & 0xFFFFFFFF) # MOV operation
ref_47538 = (ref_47395 & 0xFFFFFFFF) # MOV operation
ref_47540 = ((ref_47538 & 0xFFFFFFFF) ^ (ref_47534 & 0xFFFFFFFF)) # XOR operation
ref_47684 = (ref_47540 & 0xFFFFFFFF) # MOV operation
ref_51649 = ref_277 # MOVZX operation
ref_51754 = (ref_51649 & 0xFF) # MOVZX operation
ref_51756 = (ref_51754 & 0xFF) # MOVZX operation
ref_52034 = (ref_47684 & 0xFFFFFFFF) # MOV operation
ref_52145 = (ref_52034 & 0xFFFFFFFF) # MOV operation
ref_52157 = (ref_51756 & 0xFFFFFFFF) # MOV operation
ref_52159 = (((ref_52157 & 0xFFFFFFFF) + (ref_52145 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_52304 = (ref_52159 & 0xFFFFFFFF) # MOV operation
ref_52769 = (ref_52304 & 0xFFFFFFFF) # MOV operation
ref_53039 = (ref_52769 & 0xFFFFFFFF) # MOV operation
ref_53047 = (((ref_53039 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_53054 = (ref_53047 & 0xFFFFFFFF) # MOV operation
ref_53352 = (ref_52304 & 0xFFFFFFFF) # MOV operation
ref_53463 = (ref_53352 & 0xFFFFFFFF) # MOV operation
ref_53475 = (ref_53054 & 0xFFFFFFFF) # MOV operation
ref_53477 = (((ref_53475 & 0xFFFFFFFF) + (ref_53463 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_53622 = (ref_53477 & 0xFFFFFFFF) # MOV operation
ref_54087 = (ref_53622 & 0xFFFFFFFF) # MOV operation
ref_54516 = (ref_53622 & 0xFFFFFFFF) # MOV operation
ref_54627 = (ref_54516 & 0xFFFFFFFF) # MOV operation
ref_54643 = ((ref_54627 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_54650 = (ref_54643 & 0xFFFFFFFF) # MOV operation
ref_54789 = (ref_54087 & 0xFFFFFFFF) # MOV operation
ref_54793 = (ref_54650 & 0xFFFFFFFF) # MOV operation
ref_54795 = ((ref_54793 & 0xFFFFFFFF) ^ (ref_54789 & 0xFFFFFFFF)) # XOR operation
ref_54939 = (ref_54795 & 0xFFFFFFFF) # MOV operation
ref_58904 = ref_276 # MOVZX operation
ref_59009 = (ref_58904 & 0xFF) # MOVZX operation
ref_59011 = (ref_59009 & 0xFF) # MOVZX operation
ref_59289 = (ref_54939 & 0xFFFFFFFF) # MOV operation
ref_59400 = (ref_59289 & 0xFFFFFFFF) # MOV operation
ref_59412 = (ref_59011 & 0xFFFFFFFF) # MOV operation
ref_59414 = (((ref_59412 & 0xFFFFFFFF) + (ref_59400 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_59559 = (ref_59414 & 0xFFFFFFFF) # MOV operation
ref_60024 = (ref_59559 & 0xFFFFFFFF) # MOV operation
ref_60294 = (ref_60024 & 0xFFFFFFFF) # MOV operation
ref_60302 = (((ref_60294 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_60309 = (ref_60302 & 0xFFFFFFFF) # MOV operation
ref_60607 = (ref_59559 & 0xFFFFFFFF) # MOV operation
ref_60718 = (ref_60607 & 0xFFFFFFFF) # MOV operation
ref_60730 = (ref_60309 & 0xFFFFFFFF) # MOV operation
ref_60732 = (((ref_60730 & 0xFFFFFFFF) + (ref_60718 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_60877 = (ref_60732 & 0xFFFFFFFF) # MOV operation
ref_61342 = (ref_60877 & 0xFFFFFFFF) # MOV operation
ref_61771 = (ref_60877 & 0xFFFFFFFF) # MOV operation
ref_61882 = (ref_61771 & 0xFFFFFFFF) # MOV operation
ref_61898 = ((ref_61882 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_61905 = (ref_61898 & 0xFFFFFFFF) # MOV operation
ref_62044 = (ref_61342 & 0xFFFFFFFF) # MOV operation
ref_62048 = (ref_61905 & 0xFFFFFFFF) # MOV operation
ref_62050 = ((ref_62048 & 0xFFFFFFFF) ^ (ref_62044 & 0xFFFFFFFF)) # XOR operation
ref_62194 = (ref_62050 & 0xFFFFFFFF) # MOV operation
ref_66159 = ref_275 # MOVZX operation
ref_66264 = (ref_66159 & 0xFF) # MOVZX operation
ref_66266 = (ref_66264 & 0xFF) # MOVZX operation
ref_66544 = (ref_62194 & 0xFFFFFFFF) # MOV operation
ref_66655 = (ref_66544 & 0xFFFFFFFF) # MOV operation
ref_66667 = (ref_66266 & 0xFFFFFFFF) # MOV operation
ref_66669 = (((ref_66667 & 0xFFFFFFFF) + (ref_66655 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_66814 = (ref_66669 & 0xFFFFFFFF) # MOV operation
ref_67279 = (ref_66814 & 0xFFFFFFFF) # MOV operation
ref_67549 = (ref_67279 & 0xFFFFFFFF) # MOV operation
ref_67557 = (((ref_67549 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_67564 = (ref_67557 & 0xFFFFFFFF) # MOV operation
ref_67862 = (ref_66814 & 0xFFFFFFFF) # MOV operation
ref_67973 = (ref_67862 & 0xFFFFFFFF) # MOV operation
ref_67985 = (ref_67564 & 0xFFFFFFFF) # MOV operation
ref_67987 = (((ref_67985 & 0xFFFFFFFF) + (ref_67973 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_68132 = (ref_67987 & 0xFFFFFFFF) # MOV operation
ref_68597 = (ref_68132 & 0xFFFFFFFF) # MOV operation
ref_69026 = (ref_68132 & 0xFFFFFFFF) # MOV operation
ref_69137 = (ref_69026 & 0xFFFFFFFF) # MOV operation
ref_69153 = ((ref_69137 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_69160 = (ref_69153 & 0xFFFFFFFF) # MOV operation
ref_69299 = (ref_68597 & 0xFFFFFFFF) # MOV operation
ref_69303 = (ref_69160 & 0xFFFFFFFF) # MOV operation
ref_69305 = ((ref_69303 & 0xFFFFFFFF) ^ (ref_69299 & 0xFFFFFFFF)) # XOR operation
ref_69449 = (ref_69305 & 0xFFFFFFFF) # MOV operation
ref_73414 = ref_274 # MOVZX operation
ref_73519 = (ref_73414 & 0xFF) # MOVZX operation
ref_73521 = (ref_73519 & 0xFF) # MOVZX operation
ref_73799 = (ref_69449 & 0xFFFFFFFF) # MOV operation
ref_73910 = (ref_73799 & 0xFFFFFFFF) # MOV operation
ref_73922 = (ref_73521 & 0xFFFFFFFF) # MOV operation
ref_73924 = (((ref_73922 & 0xFFFFFFFF) + (ref_73910 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_74069 = (ref_73924 & 0xFFFFFFFF) # MOV operation
ref_74534 = (ref_74069 & 0xFFFFFFFF) # MOV operation
ref_74804 = (ref_74534 & 0xFFFFFFFF) # MOV operation
ref_74812 = (((ref_74804 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_74819 = (ref_74812 & 0xFFFFFFFF) # MOV operation
ref_75117 = (ref_74069 & 0xFFFFFFFF) # MOV operation
ref_75228 = (ref_75117 & 0xFFFFFFFF) # MOV operation
ref_75240 = (ref_74819 & 0xFFFFFFFF) # MOV operation
ref_75242 = (((ref_75240 & 0xFFFFFFFF) + (ref_75228 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_75387 = (ref_75242 & 0xFFFFFFFF) # MOV operation
ref_75852 = (ref_75387 & 0xFFFFFFFF) # MOV operation
ref_76281 = (ref_75387 & 0xFFFFFFFF) # MOV operation
ref_76392 = (ref_76281 & 0xFFFFFFFF) # MOV operation
ref_76408 = ((ref_76392 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_76415 = (ref_76408 & 0xFFFFFFFF) # MOV operation
ref_76554 = (ref_75852 & 0xFFFFFFFF) # MOV operation
ref_76558 = (ref_76415 & 0xFFFFFFFF) # MOV operation
ref_76560 = ((ref_76558 & 0xFFFFFFFF) ^ (ref_76554 & 0xFFFFFFFF)) # XOR operation
ref_76704 = (ref_76560 & 0xFFFFFFFF) # MOV operation
ref_78444 = (ref_76704 & 0xFFFFFFFF) # MOV operation
ref_78714 = (ref_78444 & 0xFFFFFFFF) # MOV operation
ref_78722 = (((ref_78714 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_78729 = (ref_78722 & 0xFFFFFFFF) # MOV operation
ref_79027 = (ref_76704 & 0xFFFFFFFF) # MOV operation
ref_79138 = (ref_79027 & 0xFFFFFFFF) # MOV operation
ref_79150 = (ref_78729 & 0xFFFFFFFF) # MOV operation
ref_79152 = (((ref_79150 & 0xFFFFFFFF) + (ref_79138 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_79297 = (ref_79152 & 0xFFFFFFFF) # MOV operation
ref_79762 = (ref_79297 & 0xFFFFFFFF) # MOV operation
ref_80191 = (ref_79297 & 0xFFFFFFFF) # MOV operation
ref_80302 = (ref_80191 & 0xFFFFFFFF) # MOV operation
ref_80318 = ((ref_80302 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_80325 = (ref_80318 & 0xFFFFFFFF) # MOV operation
ref_80464 = (ref_79762 & 0xFFFFFFFF) # MOV operation
ref_80468 = (ref_80325 & 0xFFFFFFFF) # MOV operation
ref_80470 = ((ref_80468 & 0xFFFFFFFF) ^ (ref_80464 & 0xFFFFFFFF)) # XOR operation
ref_80614 = (ref_80470 & 0xFFFFFFFF) # MOV operation
ref_81079 = (ref_80614 & 0xFFFFFFFF) # MOV operation
ref_81349 = (ref_81079 & 0xFFFFFFFF) # MOV operation
ref_81357 = (((ref_81349 & 0xFFFFFFFF) << (0xF & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_81364 = (ref_81357 & 0xFFFFFFFF) # MOV operation
ref_81662 = (ref_80614 & 0xFFFFFFFF) # MOV operation
ref_81773 = (ref_81662 & 0xFFFFFFFF) # MOV operation
ref_81785 = (ref_81364 & 0xFFFFFFFF) # MOV operation
ref_81787 = (((ref_81785 & 0xFFFFFFFF) + (ref_81773 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_81932 = (ref_81787 & 0xFFFFFFFF) # MOV operation
ref_82353 = (ref_81932 & 0xFFFFFFFF) # MOV operation
ref_82460 = (ref_82353 & 0xFFFFFFFF) # MOV operation
ref_82484 = (ref_82460 & 0xFFFFFFFF) # MOV operation
ref_82492 = (ref_82484 & 0xFFFFFFFF) # MOV operation
ref_82494 = (ref_82492 & 0xFFFFFFFF) # MOV operation

print ref_82494 & 0xffffffffffffffff
