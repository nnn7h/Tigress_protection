#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_9340 = ref_278 # MOV operation
ref_9488 = ref_9340 # MOV operation
ref_9496 = (ref_9488 >> (0x5 & 0x3F)) # SHR operation
ref_9503 = ref_9496 # MOV operation
ref_9573 = ref_9503 # MOV operation
ref_9587 = (0x1376783EF7559EA & ref_9573) # AND operation
ref_9670 = ref_9587 # MOV operation
ref_9672 = ((ref_9670 >> 56) & 0xFF) # Byte reference - MOV operation
ref_9673 = ((ref_9670 >> 48) & 0xFF) # Byte reference - MOV operation
ref_9674 = ((ref_9670 >> 40) & 0xFF) # Byte reference - MOV operation
ref_9675 = ((ref_9670 >> 32) & 0xFF) # Byte reference - MOV operation
ref_9676 = ((ref_9670 >> 24) & 0xFF) # Byte reference - MOV operation
ref_9677 = ((ref_9670 >> 16) & 0xFF) # Byte reference - MOV operation
ref_9678 = ((ref_9670 >> 8) & 0xFF) # Byte reference - MOV operation
ref_9679 = (ref_9670 & 0xFF) # Byte reference - MOV operation
ref_10935 = ref_278 # MOV operation
ref_11083 = ref_10935 # MOV operation
ref_11089 = (0x1A5612E2 | ref_11083) # OR operation
ref_11894 = ref_9670 # MOV operation
ref_11944 = ref_11894 # MOV operation
ref_11958 = (0x7063FB7 & ref_11944) # AND operation
ref_12041 = ref_11089 # MOV operation
ref_12045 = ref_11958 # MOV operation
ref_12047 = ((ref_12045 + ref_12041) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_12131 = ref_12047 # MOV operation
ref_12133 = ((ref_12131 >> 56) & 0xFF) # Byte reference - MOV operation
ref_12134 = ((ref_12131 >> 48) & 0xFF) # Byte reference - MOV operation
ref_12135 = ((ref_12131 >> 40) & 0xFF) # Byte reference - MOV operation
ref_12136 = ((ref_12131 >> 32) & 0xFF) # Byte reference - MOV operation
ref_12137 = ((ref_12131 >> 24) & 0xFF) # Byte reference - MOV operation
ref_12138 = ((ref_12131 >> 16) & 0xFF) # Byte reference - MOV operation
ref_12139 = ((ref_12131 >> 8) & 0xFF) # Byte reference - MOV operation
ref_12140 = (ref_12131 & 0xFF) # Byte reference - MOV operation
ref_13661 = ref_12131 # MOV operation
ref_13809 = ref_13661 # MOV operation
ref_13817 = (ref_13809 >> (0x3 & 0x3F)) # SHR operation
ref_13824 = ref_13817 # MOV operation
ref_13894 = ref_13824 # MOV operation
ref_13908 = (0xF & ref_13894) # AND operation
ref_14081 = ref_13908 # MOV operation
ref_14087 = (0x1 | ref_14081) # OR operation
ref_14264 = ref_14087 # MOV operation
ref_14266 = ((0x3162E74F << ((ref_14264 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_15161 = ref_12131 # MOV operation
ref_15309 = ref_15161 # MOV operation
ref_15317 = (ref_15309 >> (0x3 & 0x3F)) # SHR operation
ref_15324 = ref_15317 # MOV operation
ref_15394 = ref_15324 # MOV operation
ref_15408 = (0xF & ref_15394) # AND operation
ref_15581 = ref_15408 # MOV operation
ref_15587 = (0x1 | ref_15581) # OR operation
ref_15764 = ref_15587 # MOV operation
ref_15766 = ((0x40 - ref_15764) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15774 = ref_15766 # MOV operation
ref_15856 = ref_15774 # MOV operation
ref_15858 = (ref_15856 & 0xFFFFFFFF) # MOV operation
ref_15860 = (0x3162E74F >> ((ref_15858 & 0xFF) & 0x3F)) # SHR operation
ref_15867 = ref_15860 # MOV operation
ref_15945 = ref_14266 # MOV operation
ref_15949 = ref_15867 # MOV operation
ref_15951 = (ref_15949 | ref_15945) # OR operation
ref_16124 = ref_15951 # MOV operation
ref_16132 = (ref_16124 >> (0x4 & 0x3F)) # SHR operation
ref_16139 = ref_16132 # MOV operation
ref_16209 = ref_16139 # MOV operation
ref_16223 = (0x7 & ref_16209) # AND operation
ref_16396 = ref_16223 # MOV operation
ref_16402 = (0x1 | ref_16396) # OR operation
ref_17122 = ref_278 # MOV operation
ref_17172 = ref_17122 # MOV operation
ref_17186 = ((ref_17172 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_17194 = ref_17186 # MOV operation
ref_17264 = ref_17194 # MOV operation
ref_17276 = ref_16402 # MOV operation
ref_17278 = ((ref_17264 << ((ref_17276 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_17361 = ref_17278 # MOV operation
ref_18716 = ref_278 # MOV operation
ref_18766 = ref_18716 # MOV operation
ref_18780 = ((ref_18766 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_18788 = ref_18780 # MOV operation
ref_18866 = ref_18788 # MOV operation
ref_20967 = ref_18866 # MOV operation
ref_22079 = ref_12131 # MOV operation
ref_22129 = ref_22079 # MOV operation
ref_22143 = (0xF & ref_22129) # AND operation
ref_22218 = ref_22143 # MOV operation
ref_22232 = ((ref_22218 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_22315 = ref_20967 # MOV operation
ref_22319 = ref_22232 # MOV operation
ref_22321 = (ref_22319 | ref_22315) # OR operation
ref_22404 = ref_22321 # MOV operation
ref_23754 = ref_17361 # MOV operation
ref_24624 = ref_22404 # MOV operation
ref_24674 = ref_24624 # MOV operation
ref_24688 = (0x1F & ref_24674) # AND operation
ref_24763 = ref_24688 # MOV operation
ref_24777 = ((ref_24763 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_24860 = ref_23754 # MOV operation
ref_24864 = ref_24777 # MOV operation
ref_24866 = (ref_24864 | ref_24860) # OR operation
ref_24949 = ref_24866 # MOV operation
ref_26299 = ref_22404 # MOV operation
ref_27411 = ref_12131 # MOV operation
ref_27461 = ref_27411 # MOV operation
ref_27475 = (0xF & ref_27461) # AND operation
ref_27550 = ref_27475 # MOV operation
ref_27564 = ((ref_27550 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27647 = ref_26299 # MOV operation
ref_27651 = ref_27564 # MOV operation
ref_27653 = (ref_27651 | ref_27647) # OR operation
ref_27736 = ref_27653 # MOV operation
ref_30079 = ref_27736 # MOV operation
ref_31191 = ref_27736 # MOV operation
ref_31241 = ref_31191 # MOV operation
ref_31255 = (0xF & ref_31241) # AND operation
ref_31330 = ref_31255 # MOV operation
ref_31344 = ((ref_31330 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_31427 = ref_30079 # MOV operation
ref_31431 = ref_31344 # MOV operation
ref_31433 = (ref_31431 | ref_31427) # OR operation
ref_31516 = ref_31433 # MOV operation
ref_32866 = ref_24949 # MOV operation
ref_33736 = ref_31516 # MOV operation
ref_33786 = ref_33736 # MOV operation
ref_33800 = (0x1F & ref_33786) # AND operation
ref_33875 = ref_33800 # MOV operation
ref_33889 = ((ref_33875 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_33972 = ref_32866 # MOV operation
ref_33976 = ref_33889 # MOV operation
ref_33978 = (ref_33976 | ref_33972) # OR operation
ref_34061 = ref_33978 # MOV operation
ref_34063 = ((ref_34061 >> 56) & 0xFF) # Byte reference - MOV operation
ref_34064 = ((ref_34061 >> 48) & 0xFF) # Byte reference - MOV operation
ref_34065 = ((ref_34061 >> 40) & 0xFF) # Byte reference - MOV operation
ref_34066 = ((ref_34061 >> 32) & 0xFF) # Byte reference - MOV operation
ref_34067 = ((ref_34061 >> 24) & 0xFF) # Byte reference - MOV operation
ref_34068 = ((ref_34061 >> 16) & 0xFF) # Byte reference - MOV operation
ref_34069 = ((ref_34061 >> 8) & 0xFF) # Byte reference - MOV operation
ref_34070 = (ref_34061 & 0xFF) # Byte reference - MOV operation
ref_35411 = ref_31516 # MOV operation
ref_36523 = ref_31516 # MOV operation
ref_36573 = ref_36523 # MOV operation
ref_36587 = (0xF & ref_36573) # AND operation
ref_36662 = ref_36587 # MOV operation
ref_36676 = ((ref_36662 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_36759 = ref_35411 # MOV operation
ref_36763 = ref_36676 # MOV operation
ref_36765 = (ref_36763 | ref_36759) # OR operation
ref_36848 = ref_36765 # MOV operation
ref_42964 = ref_36848 # MOV operation
ref_43834 = ref_34061 # MOV operation
ref_44524 = ref_34061 # MOV operation
ref_44582 = ref_43834 # MOV operation
ref_44586 = ref_44524 # MOV operation
ref_44588 = ((ref_44586 + ref_44582) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_44664 = ref_44588 # MOV operation
ref_44678 = (0x7 & ref_44664) # AND operation
ref_44753 = ref_44678 # MOV operation
ref_44767 = ((ref_44753 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_44850 = ref_42964 # MOV operation
ref_44854 = ref_44767 # MOV operation
ref_44856 = (ref_44854 | ref_44850) # OR operation
ref_44939 = ref_44856 # MOV operation
ref_46099 = ((((ref_34063) << 8 | ref_34064) << 8 | ref_34065) << 8 | ref_34066) # MOV operation
ref_46255 = (ref_46099 & 0xFFFFFFFF) # MOV operation
ref_47411 = ((((ref_34067) << 8 | ref_34068) << 8 | ref_34069) << 8 | ref_34070) # MOV operation
ref_48555 = (ref_47411 & 0xFFFFFFFF) # MOV operation
ref_48557 = (((ref_48555 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_48558 = (((ref_48555 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_48559 = (((ref_48555 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_48560 = ((ref_48555 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_48723 = (ref_46255 & 0xFFFFFFFF) # MOV operation
ref_49867 = (ref_48723 & 0xFFFFFFFF) # MOV operation
ref_49869 = (((ref_49867 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_49870 = (((ref_49867 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_49871 = (((ref_49867 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_49872 = ((ref_49867 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_51125 = ref_9674 # MOVZX operation
ref_51175 = (ref_51125 & 0xFF) # MOVZX operation
ref_53417 = ref_9675 # MOVZX operation
ref_53467 = (ref_53417 & 0xFF) # MOVZX operation
ref_53469 = (ref_53467 & 0xFF) # Byte reference - MOV operation
ref_54721 = (ref_51175 & 0xFF) # MOVZX operation
ref_54771 = (ref_54721 & 0xFF) # MOVZX operation
ref_54773 = (ref_54771 & 0xFF) # Byte reference - MOV operation
ref_56025 = ref_9673 # MOVZX operation
ref_56075 = (ref_56025 & 0xFF) # MOVZX operation
ref_58317 = ref_9679 # MOVZX operation
ref_58367 = (ref_58317 & 0xFF) # MOVZX operation
ref_58369 = (ref_58367 & 0xFF) # Byte reference - MOV operation
ref_59621 = (ref_56075 & 0xFF) # MOVZX operation
ref_59671 = (ref_59621 & 0xFF) # MOVZX operation
ref_59673 = (ref_59671 & 0xFF) # Byte reference - MOV operation
ref_60823 = ((((ref_12137) << 8 | ref_12138) << 8 | ref_12139) << 8 | ref_12140) # MOV operation
ref_60979 = (ref_60823 & 0xFFFFFFFF) # MOV operation
ref_62135 = ((((ref_12133) << 8 | ref_12134) << 8 | ref_12135) << 8 | ref_12136) # MOV operation
ref_63279 = (ref_62135 & 0xFFFFFFFF) # MOV operation
ref_63281 = (((ref_63279 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_63282 = (((ref_63279 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_63283 = (((ref_63279 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_63284 = ((ref_63279 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_63447 = (ref_60979 & 0xFFFFFFFF) # MOV operation
ref_64591 = (ref_63447 & 0xFFFFFFFF) # MOV operation
ref_64593 = (((ref_64591 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_64594 = (((ref_64591 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_64595 = (((ref_64591 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_64596 = ((ref_64591 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_66870 = ((((((((ref_64593) << 8 | ref_64594) << 8 | ref_64595) << 8 | ref_64596) << 8 | ref_63281) << 8 | ref_63282) << 8 | ref_63283) << 8 | ref_63284) # MOV operation
ref_67982 = ((((((((ref_9672) << 8 | ref_58369) << 8 | ref_53469) << 8 | ref_54773) << 8 | ref_9676) << 8 | ref_9677) << 8 | ref_9678) << 8 | ref_59673) # MOV operation
ref_68032 = ref_67982 # MOV operation
ref_68046 = (0x3F & ref_68032) # AND operation
ref_68121 = ref_68046 # MOV operation
ref_68135 = ((ref_68121 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_68218 = ref_66870 # MOV operation
ref_68222 = ref_68135 # MOV operation
ref_68224 = (ref_68222 | ref_68218) # OR operation
ref_68307 = ref_68224 # MOV operation
ref_70759 = ((((((((ref_48557) << 8 | ref_48558) << 8 | ref_48559) << 8 | ref_48560) << 8 | ref_49869) << 8 | ref_49870) << 8 | ref_49871) << 8 | ref_49872) # MOV operation
ref_71629 = ref_44939 # MOV operation
ref_72409 = ref_68307 # MOV operation
ref_72557 = ref_72409 # MOV operation
ref_72565 = (ref_72557 >> (0x3 & 0x3F)) # SHR operation
ref_72572 = ref_72565 # MOV operation
ref_72642 = ref_72572 # MOV operation
ref_72656 = (0xF & ref_72642) # AND operation
ref_72829 = ref_72656 # MOV operation
ref_72835 = (0x1 | ref_72829) # OR operation
ref_72918 = ref_71629 # MOV operation
ref_72922 = ref_72835 # MOV operation
ref_72924 = (ref_72922 & 0xFFFFFFFF) # MOV operation
ref_72926 = (ref_72918 >> ((ref_72924 & 0xFF) & 0x3F)) # SHR operation
ref_72933 = ref_72926 # MOV operation
ref_73733 = ref_68307 # MOV operation
ref_73881 = ref_73733 # MOV operation
ref_73889 = (ref_73881 >> (0x3 & 0x3F)) # SHR operation
ref_73896 = ref_73889 # MOV operation
ref_73966 = ref_73896 # MOV operation
ref_73980 = (0xF & ref_73966) # AND operation
ref_74153 = ref_73980 # MOV operation
ref_74159 = (0x1 | ref_74153) # OR operation
ref_74336 = ref_74159 # MOV operation
ref_74338 = ((0x40 - ref_74336) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_74346 = ref_74338 # MOV operation
ref_75056 = ref_44939 # MOV operation
ref_75106 = ref_75056 # MOV operation
ref_75118 = ref_74346 # MOV operation
ref_75120 = ((ref_75106 << ((ref_75118 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_75203 = ref_72933 # MOV operation
ref_75207 = ref_75120 # MOV operation
ref_75209 = (ref_75207 | ref_75203) # OR operation
ref_75284 = ref_75209 # MOV operation
ref_75298 = (0xF & ref_75284) # AND operation
ref_75373 = ref_75298 # MOV operation
ref_75387 = ((ref_75373 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_75470 = ref_70759 # MOV operation
ref_75474 = ref_75387 # MOV operation
ref_75476 = (ref_75474 | ref_75470) # OR operation
ref_75559 = ref_75476 # MOV operation
ref_76923 = ref_68307 # MOV operation
ref_77071 = ref_76923 # MOV operation
ref_77079 = (ref_77071 >> (0x3 & 0x3F)) # SHR operation
ref_77086 = ref_77079 # MOV operation
ref_77156 = ref_77086 # MOV operation
ref_77170 = (0x7 & ref_77156) # AND operation
ref_77343 = ref_77170 # MOV operation
ref_77349 = (0x1 | ref_77343) # OR operation
ref_78064 = ((((((((ref_9672) << 8 | ref_58369) << 8 | ref_53469) << 8 | ref_54773) << 8 | ref_9676) << 8 | ref_9677) << 8 | ref_9678) << 8 | ref_59673) # MOV operation
ref_78114 = ref_78064 # MOV operation
ref_78126 = ref_77349 # MOV operation
ref_78128 = ((ref_78114 << ((ref_78126 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_78843 = ref_75559 # MOV operation
ref_79533 = ref_44939 # MOV operation
ref_79591 = ref_78843 # MOV operation
ref_79595 = ref_79533 # MOV operation
ref_79597 = (ref_79595 | ref_79591) # OR operation
ref_79680 = ref_78128 # MOV operation
ref_79684 = ref_79597 # MOV operation
ref_79686 = (ref_79684 | ref_79680) # OR operation
ref_79769 = ref_79686 # MOV operation
ref_79928 = ref_79769 # MOV operation
ref_79930 = ref_79928 # MOV operation

print ref_79930 & 0xffffffffffffffff
