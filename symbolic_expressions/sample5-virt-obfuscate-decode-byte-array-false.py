#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_273 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_274 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_275 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_276 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_277 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_278 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_279 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_280 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_24839 = ref_280 # MOVZX operation
ref_24905 = (ref_24839 & 0xFF) # MOVZX operation
ref_24907 = (ref_24905 & 0xFF) # MOVZX operation
ref_25191 = (ref_24907 & 0xFFFFFFFF) # MOV operation
ref_25193 = (((ref_25191 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_25299 = (ref_25193 & 0xFFFFFFFF) # MOV operation
ref_25647 = (ref_25299 & 0xFFFFFFFF) # MOV operation
ref_25839 = (ref_25647 & 0xFFFFFFFF) # MOV operation
ref_25847 = (((ref_25839 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_25854 = (ref_25847 & 0xFFFFFFFF) # MOV operation
ref_26074 = (ref_25299 & 0xFFFFFFFF) # MOV operation
ref_26146 = (ref_26074 & 0xFFFFFFFF) # MOV operation
ref_26158 = (ref_25854 & 0xFFFFFFFF) # MOV operation
ref_26160 = (((ref_26158 & 0xFFFFFFFF) + (ref_26146 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_26266 = (ref_26160 & 0xFFFFFFFF) # MOV operation
ref_26614 = (ref_26266 & 0xFFFFFFFF) # MOV operation
ref_26926 = (ref_26266 & 0xFFFFFFFF) # MOV operation
ref_26998 = (ref_26926 & 0xFFFFFFFF) # MOV operation
ref_27014 = ((ref_26998 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_27021 = (ref_27014 & 0xFFFFFFFF) # MOV operation
ref_27121 = (ref_26614 & 0xFFFFFFFF) # MOV operation
ref_27125 = (ref_27021 & 0xFFFFFFFF) # MOV operation
ref_27127 = ((ref_27125 & 0xFFFFFFFF) ^ (ref_27121 & 0xFFFFFFFF)) # XOR operation
ref_27232 = (ref_27127 & 0xFFFFFFFF) # MOV operation
ref_30107 = ref_279 # MOVZX operation
ref_30173 = (ref_30107 & 0xFF) # MOVZX operation
ref_30175 = (ref_30173 & 0xFF) # MOVZX operation
ref_30375 = (ref_27232 & 0xFFFFFFFF) # MOV operation
ref_30447 = (ref_30375 & 0xFFFFFFFF) # MOV operation
ref_30459 = (ref_30175 & 0xFFFFFFFF) # MOV operation
ref_30461 = (((ref_30459 & 0xFFFFFFFF) + (ref_30447 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_30567 = (ref_30461 & 0xFFFFFFFF) # MOV operation
ref_30915 = (ref_30567 & 0xFFFFFFFF) # MOV operation
ref_31107 = (ref_30915 & 0xFFFFFFFF) # MOV operation
ref_31115 = (((ref_31107 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_31122 = (ref_31115 & 0xFFFFFFFF) # MOV operation
ref_31342 = (ref_30567 & 0xFFFFFFFF) # MOV operation
ref_31414 = (ref_31342 & 0xFFFFFFFF) # MOV operation
ref_31426 = (ref_31122 & 0xFFFFFFFF) # MOV operation
ref_31428 = (((ref_31426 & 0xFFFFFFFF) + (ref_31414 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_31534 = (ref_31428 & 0xFFFFFFFF) # MOV operation
ref_31882 = (ref_31534 & 0xFFFFFFFF) # MOV operation
ref_32194 = (ref_31534 & 0xFFFFFFFF) # MOV operation
ref_32266 = (ref_32194 & 0xFFFFFFFF) # MOV operation
ref_32282 = ((ref_32266 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_32289 = (ref_32282 & 0xFFFFFFFF) # MOV operation
ref_32389 = (ref_31882 & 0xFFFFFFFF) # MOV operation
ref_32393 = (ref_32289 & 0xFFFFFFFF) # MOV operation
ref_32395 = ((ref_32393 & 0xFFFFFFFF) ^ (ref_32389 & 0xFFFFFFFF)) # XOR operation
ref_32500 = (ref_32395 & 0xFFFFFFFF) # MOV operation
ref_35375 = ref_278 # MOVZX operation
ref_35441 = (ref_35375 & 0xFF) # MOVZX operation
ref_35443 = (ref_35441 & 0xFF) # MOVZX operation
ref_35643 = (ref_32500 & 0xFFFFFFFF) # MOV operation
ref_35715 = (ref_35643 & 0xFFFFFFFF) # MOV operation
ref_35727 = (ref_35443 & 0xFFFFFFFF) # MOV operation
ref_35729 = (((ref_35727 & 0xFFFFFFFF) + (ref_35715 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_35835 = (ref_35729 & 0xFFFFFFFF) # MOV operation
ref_36183 = (ref_35835 & 0xFFFFFFFF) # MOV operation
ref_36375 = (ref_36183 & 0xFFFFFFFF) # MOV operation
ref_36383 = (((ref_36375 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_36390 = (ref_36383 & 0xFFFFFFFF) # MOV operation
ref_36610 = (ref_35835 & 0xFFFFFFFF) # MOV operation
ref_36682 = (ref_36610 & 0xFFFFFFFF) # MOV operation
ref_36694 = (ref_36390 & 0xFFFFFFFF) # MOV operation
ref_36696 = (((ref_36694 & 0xFFFFFFFF) + (ref_36682 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_36802 = (ref_36696 & 0xFFFFFFFF) # MOV operation
ref_37150 = (ref_36802 & 0xFFFFFFFF) # MOV operation
ref_37462 = (ref_36802 & 0xFFFFFFFF) # MOV operation
ref_37534 = (ref_37462 & 0xFFFFFFFF) # MOV operation
ref_37550 = ((ref_37534 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_37557 = (ref_37550 & 0xFFFFFFFF) # MOV operation
ref_37657 = (ref_37150 & 0xFFFFFFFF) # MOV operation
ref_37661 = (ref_37557 & 0xFFFFFFFF) # MOV operation
ref_37663 = ((ref_37661 & 0xFFFFFFFF) ^ (ref_37657 & 0xFFFFFFFF)) # XOR operation
ref_37768 = (ref_37663 & 0xFFFFFFFF) # MOV operation
ref_40643 = ref_277 # MOVZX operation
ref_40709 = (ref_40643 & 0xFF) # MOVZX operation
ref_40711 = (ref_40709 & 0xFF) # MOVZX operation
ref_40911 = (ref_37768 & 0xFFFFFFFF) # MOV operation
ref_40983 = (ref_40911 & 0xFFFFFFFF) # MOV operation
ref_40995 = (ref_40711 & 0xFFFFFFFF) # MOV operation
ref_40997 = (((ref_40995 & 0xFFFFFFFF) + (ref_40983 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_41103 = (ref_40997 & 0xFFFFFFFF) # MOV operation
ref_41451 = (ref_41103 & 0xFFFFFFFF) # MOV operation
ref_41643 = (ref_41451 & 0xFFFFFFFF) # MOV operation
ref_41651 = (((ref_41643 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_41658 = (ref_41651 & 0xFFFFFFFF) # MOV operation
ref_41878 = (ref_41103 & 0xFFFFFFFF) # MOV operation
ref_41950 = (ref_41878 & 0xFFFFFFFF) # MOV operation
ref_41962 = (ref_41658 & 0xFFFFFFFF) # MOV operation
ref_41964 = (((ref_41962 & 0xFFFFFFFF) + (ref_41950 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_42070 = (ref_41964 & 0xFFFFFFFF) # MOV operation
ref_42418 = (ref_42070 & 0xFFFFFFFF) # MOV operation
ref_42730 = (ref_42070 & 0xFFFFFFFF) # MOV operation
ref_42802 = (ref_42730 & 0xFFFFFFFF) # MOV operation
ref_42818 = ((ref_42802 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_42825 = (ref_42818 & 0xFFFFFFFF) # MOV operation
ref_42925 = (ref_42418 & 0xFFFFFFFF) # MOV operation
ref_42929 = (ref_42825 & 0xFFFFFFFF) # MOV operation
ref_42931 = ((ref_42929 & 0xFFFFFFFF) ^ (ref_42925 & 0xFFFFFFFF)) # XOR operation
ref_43036 = (ref_42931 & 0xFFFFFFFF) # MOV operation
ref_45911 = ref_276 # MOVZX operation
ref_45977 = (ref_45911 & 0xFF) # MOVZX operation
ref_45979 = (ref_45977 & 0xFF) # MOVZX operation
ref_46179 = (ref_43036 & 0xFFFFFFFF) # MOV operation
ref_46251 = (ref_46179 & 0xFFFFFFFF) # MOV operation
ref_46263 = (ref_45979 & 0xFFFFFFFF) # MOV operation
ref_46265 = (((ref_46263 & 0xFFFFFFFF) + (ref_46251 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_46371 = (ref_46265 & 0xFFFFFFFF) # MOV operation
ref_46719 = (ref_46371 & 0xFFFFFFFF) # MOV operation
ref_46911 = (ref_46719 & 0xFFFFFFFF) # MOV operation
ref_46919 = (((ref_46911 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_46926 = (ref_46919 & 0xFFFFFFFF) # MOV operation
ref_47146 = (ref_46371 & 0xFFFFFFFF) # MOV operation
ref_47218 = (ref_47146 & 0xFFFFFFFF) # MOV operation
ref_47230 = (ref_46926 & 0xFFFFFFFF) # MOV operation
ref_47232 = (((ref_47230 & 0xFFFFFFFF) + (ref_47218 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_47338 = (ref_47232 & 0xFFFFFFFF) # MOV operation
ref_47686 = (ref_47338 & 0xFFFFFFFF) # MOV operation
ref_47998 = (ref_47338 & 0xFFFFFFFF) # MOV operation
ref_48070 = (ref_47998 & 0xFFFFFFFF) # MOV operation
ref_48086 = ((ref_48070 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_48093 = (ref_48086 & 0xFFFFFFFF) # MOV operation
ref_48193 = (ref_47686 & 0xFFFFFFFF) # MOV operation
ref_48197 = (ref_48093 & 0xFFFFFFFF) # MOV operation
ref_48199 = ((ref_48197 & 0xFFFFFFFF) ^ (ref_48193 & 0xFFFFFFFF)) # XOR operation
ref_48304 = (ref_48199 & 0xFFFFFFFF) # MOV operation
ref_51179 = ref_275 # MOVZX operation
ref_51245 = (ref_51179 & 0xFF) # MOVZX operation
ref_51247 = (ref_51245 & 0xFF) # MOVZX operation
ref_51447 = (ref_48304 & 0xFFFFFFFF) # MOV operation
ref_51519 = (ref_51447 & 0xFFFFFFFF) # MOV operation
ref_51531 = (ref_51247 & 0xFFFFFFFF) # MOV operation
ref_51533 = (((ref_51531 & 0xFFFFFFFF) + (ref_51519 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_51639 = (ref_51533 & 0xFFFFFFFF) # MOV operation
ref_51987 = (ref_51639 & 0xFFFFFFFF) # MOV operation
ref_52179 = (ref_51987 & 0xFFFFFFFF) # MOV operation
ref_52187 = (((ref_52179 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_52194 = (ref_52187 & 0xFFFFFFFF) # MOV operation
ref_52414 = (ref_51639 & 0xFFFFFFFF) # MOV operation
ref_52486 = (ref_52414 & 0xFFFFFFFF) # MOV operation
ref_52498 = (ref_52194 & 0xFFFFFFFF) # MOV operation
ref_52500 = (((ref_52498 & 0xFFFFFFFF) + (ref_52486 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_52606 = (ref_52500 & 0xFFFFFFFF) # MOV operation
ref_52954 = (ref_52606 & 0xFFFFFFFF) # MOV operation
ref_53266 = (ref_52606 & 0xFFFFFFFF) # MOV operation
ref_53338 = (ref_53266 & 0xFFFFFFFF) # MOV operation
ref_53354 = ((ref_53338 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_53361 = (ref_53354 & 0xFFFFFFFF) # MOV operation
ref_53461 = (ref_52954 & 0xFFFFFFFF) # MOV operation
ref_53465 = (ref_53361 & 0xFFFFFFFF) # MOV operation
ref_53467 = ((ref_53465 & 0xFFFFFFFF) ^ (ref_53461 & 0xFFFFFFFF)) # XOR operation
ref_53572 = (ref_53467 & 0xFFFFFFFF) # MOV operation
ref_56447 = ref_274 # MOVZX operation
ref_56513 = (ref_56447 & 0xFF) # MOVZX operation
ref_56515 = (ref_56513 & 0xFF) # MOVZX operation
ref_56715 = (ref_53572 & 0xFFFFFFFF) # MOV operation
ref_56787 = (ref_56715 & 0xFFFFFFFF) # MOV operation
ref_56799 = (ref_56515 & 0xFFFFFFFF) # MOV operation
ref_56801 = (((ref_56799 & 0xFFFFFFFF) + (ref_56787 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_56907 = (ref_56801 & 0xFFFFFFFF) # MOV operation
ref_57255 = (ref_56907 & 0xFFFFFFFF) # MOV operation
ref_57447 = (ref_57255 & 0xFFFFFFFF) # MOV operation
ref_57455 = (((ref_57447 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_57462 = (ref_57455 & 0xFFFFFFFF) # MOV operation
ref_57682 = (ref_56907 & 0xFFFFFFFF) # MOV operation
ref_57754 = (ref_57682 & 0xFFFFFFFF) # MOV operation
ref_57766 = (ref_57462 & 0xFFFFFFFF) # MOV operation
ref_57768 = (((ref_57766 & 0xFFFFFFFF) + (ref_57754 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_57874 = (ref_57768 & 0xFFFFFFFF) # MOV operation
ref_58222 = (ref_57874 & 0xFFFFFFFF) # MOV operation
ref_58534 = (ref_57874 & 0xFFFFFFFF) # MOV operation
ref_58606 = (ref_58534 & 0xFFFFFFFF) # MOV operation
ref_58622 = ((ref_58606 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_58629 = (ref_58622 & 0xFFFFFFFF) # MOV operation
ref_58729 = (ref_58222 & 0xFFFFFFFF) # MOV operation
ref_58733 = (ref_58629 & 0xFFFFFFFF) # MOV operation
ref_58735 = ((ref_58733 & 0xFFFFFFFF) ^ (ref_58729 & 0xFFFFFFFF)) # XOR operation
ref_58840 = (ref_58735 & 0xFFFFFFFF) # MOV operation
ref_61715 = ref_273 # MOVZX operation
ref_61781 = (ref_61715 & 0xFF) # MOVZX operation
ref_61783 = (ref_61781 & 0xFF) # MOVZX operation
ref_61983 = (ref_58840 & 0xFFFFFFFF) # MOV operation
ref_62055 = (ref_61983 & 0xFFFFFFFF) # MOV operation
ref_62067 = (ref_61783 & 0xFFFFFFFF) # MOV operation
ref_62069 = (((ref_62067 & 0xFFFFFFFF) + (ref_62055 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_62175 = (ref_62069 & 0xFFFFFFFF) # MOV operation
ref_62523 = (ref_62175 & 0xFFFFFFFF) # MOV operation
ref_62715 = (ref_62523 & 0xFFFFFFFF) # MOV operation
ref_62723 = (((ref_62715 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_62730 = (ref_62723 & 0xFFFFFFFF) # MOV operation
ref_62950 = (ref_62175 & 0xFFFFFFFF) # MOV operation
ref_63022 = (ref_62950 & 0xFFFFFFFF) # MOV operation
ref_63034 = (ref_62730 & 0xFFFFFFFF) # MOV operation
ref_63036 = (((ref_63034 & 0xFFFFFFFF) + (ref_63022 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_63142 = (ref_63036 & 0xFFFFFFFF) # MOV operation
ref_63490 = (ref_63142 & 0xFFFFFFFF) # MOV operation
ref_63802 = (ref_63142 & 0xFFFFFFFF) # MOV operation
ref_63874 = (ref_63802 & 0xFFFFFFFF) # MOV operation
ref_63890 = ((ref_63874 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_63897 = (ref_63890 & 0xFFFFFFFF) # MOV operation
ref_63997 = (ref_63490 & 0xFFFFFFFF) # MOV operation
ref_64001 = (ref_63897 & 0xFFFFFFFF) # MOV operation
ref_64003 = ((ref_64001 & 0xFFFFFFFF) ^ (ref_63997 & 0xFFFFFFFF)) # XOR operation
ref_64108 = (ref_64003 & 0xFFFFFFFF) # MOV operation
ref_65342 = (ref_64108 & 0xFFFFFFFF) # MOV operation
ref_65534 = (ref_65342 & 0xFFFFFFFF) # MOV operation
ref_65542 = (((ref_65534 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_65549 = (ref_65542 & 0xFFFFFFFF) # MOV operation
ref_65769 = (ref_64108 & 0xFFFFFFFF) # MOV operation
ref_65841 = (ref_65769 & 0xFFFFFFFF) # MOV operation
ref_65853 = (ref_65549 & 0xFFFFFFFF) # MOV operation
ref_65855 = (((ref_65853 & 0xFFFFFFFF) + (ref_65841 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_65961 = (ref_65855 & 0xFFFFFFFF) # MOV operation
ref_66309 = (ref_65961 & 0xFFFFFFFF) # MOV operation
ref_66621 = (ref_65961 & 0xFFFFFFFF) # MOV operation
ref_66693 = (ref_66621 & 0xFFFFFFFF) # MOV operation
ref_66709 = ((ref_66693 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_66716 = (ref_66709 & 0xFFFFFFFF) # MOV operation
ref_66816 = (ref_66309 & 0xFFFFFFFF) # MOV operation
ref_66820 = (ref_66716 & 0xFFFFFFFF) # MOV operation
ref_66822 = ((ref_66820 & 0xFFFFFFFF) ^ (ref_66816 & 0xFFFFFFFF)) # XOR operation
ref_66927 = (ref_66822 & 0xFFFFFFFF) # MOV operation
ref_67275 = (ref_66927 & 0xFFFFFFFF) # MOV operation
ref_67467 = (ref_67275 & 0xFFFFFFFF) # MOV operation
ref_67475 = (((ref_67467 & 0xFFFFFFFF) << (0xF & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_67482 = (ref_67475 & 0xFFFFFFFF) # MOV operation
ref_67702 = (ref_66927 & 0xFFFFFFFF) # MOV operation
ref_67774 = (ref_67702 & 0xFFFFFFFF) # MOV operation
ref_67786 = (ref_67482 & 0xFFFFFFFF) # MOV operation
ref_67788 = (((ref_67786 & 0xFFFFFFFF) + (ref_67774 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_67894 = (ref_67788 & 0xFFFFFFFF) # MOV operation
ref_68198 = (ref_67894 & 0xFFFFFFFF) # MOV operation
ref_68266 = (ref_68198 & 0xFFFFFFFF) # MOV operation
ref_68290 = (ref_68266 & 0xFFFFFFFF) # MOV operation
ref_68298 = (ref_68290 & 0xFFFFFFFF) # MOV operation
ref_68300 = (ref_68298 & 0xFFFFFFFF) # MOV operation

print ref_68300 & 0xffffffffffffffff
