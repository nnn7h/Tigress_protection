#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_60839 = ref_278 # MOV operation
ref_61096 = ref_60839 # MOV operation
ref_61102 = ((0x3F22161B + ref_61096) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_62253 = ref_61102 # MOV operation
ref_63747 = ref_62253 # MOV operation
ref_63877 = ref_63747 # MOV operation
ref_63879 = (((sx(0x40, ref_63877) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_64031 = ref_63879 # MOV operation
ref_64033 = (((sx(0x40, ref_64031) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_64303 = ref_64033 # MOV operation
ref_64311 = (ref_64303 >> (0x1 & 0x3F)) # SHR operation
ref_64318 = ref_64311 # MOV operation
ref_64456 = ref_64318 # MOV operation
ref_64470 = (0xF & ref_64456) # AND operation
ref_64743 = ref_64470 # MOV operation
ref_64749 = (0x1 | ref_64743) # OR operation
ref_65892 = ref_278 # MOV operation
ref_65965 = ref_65892 # MOV operation
ref_65979 = ((ref_65965 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_66991 = ref_278 # MOV operation
ref_67239 = ref_66991 # MOV operation
ref_67247 = (ref_67239 >> (0x39 & 0x3F)) # SHR operation
ref_67254 = ref_67247 # MOV operation
ref_67391 = ref_65979 # MOV operation
ref_67395 = ref_67254 # MOV operation
ref_67397 = (ref_67395 | ref_67391) # OR operation
ref_67495 = ref_67397 # MOV operation
ref_67507 = ref_64749 # MOV operation
ref_67509 = ((ref_67495 << ((ref_67507 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_68652 = ref_278 # MOV operation
ref_68725 = ref_68652 # MOV operation
ref_68739 = ((ref_68725 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_69751 = ref_278 # MOV operation
ref_69999 = ref_69751 # MOV operation
ref_70007 = (ref_69999 >> (0x39 & 0x3F)) # SHR operation
ref_70014 = ref_70007 # MOV operation
ref_70151 = ref_68739 # MOV operation
ref_70155 = ref_70014 # MOV operation
ref_70157 = (ref_70155 | ref_70151) # OR operation
ref_71656 = ref_62253 # MOV operation
ref_71786 = ref_71656 # MOV operation
ref_71788 = (((sx(0x40, ref_71786) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_71940 = ref_71788 # MOV operation
ref_71942 = (((sx(0x40, ref_71940) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_72212 = ref_71942 # MOV operation
ref_72220 = (ref_72212 >> (0x1 & 0x3F)) # SHR operation
ref_72227 = ref_72220 # MOV operation
ref_72365 = ref_72227 # MOV operation
ref_72379 = (0xF & ref_72365) # AND operation
ref_72652 = ref_72379 # MOV operation
ref_72658 = (0x1 | ref_72652) # OR operation
ref_72899 = ref_72658 # MOV operation
ref_72901 = ((0x40 - ref_72899) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_72909 = ref_72901 # MOV operation
ref_73046 = ref_70157 # MOV operation
ref_73050 = ref_72909 # MOV operation
ref_73052 = (ref_73050 & 0xFFFFFFFF) # MOV operation
ref_73054 = (ref_73046 >> ((ref_73052 & 0xFF) & 0x3F)) # SHR operation
ref_73061 = ref_73054 # MOV operation
ref_73198 = ref_67509 # MOV operation
ref_73202 = ref_73061 # MOV operation
ref_73204 = (ref_73202 | ref_73198) # OR operation
ref_74354 = ref_73204 # MOV operation
ref_75361 = ref_278 # MOV operation
ref_76442 = ref_74354 # MOV operation
ref_76699 = ref_76442 # MOV operation
ref_76705 = ((0xAD6EED + ref_76699) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_76857 = ref_75361 # MOV operation
ref_76861 = ref_76705 # MOV operation
ref_76863 = ((ref_76861 + ref_76857) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_78014 = ref_76863 # MOV operation
ref_79021 = ref_278 # MOV operation
ref_80102 = ref_62253 # MOV operation
ref_80219 = ref_79021 # MOV operation
ref_80223 = ref_80102 # MOV operation
ref_80225 = (ref_80223 | ref_80219) # OR operation
ref_81331 = ref_74354 # MOV operation
ref_81588 = ref_81331 # MOV operation
ref_81594 = ((0x2B6B05ED + ref_81588) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_82701 = ref_78014 # MOV operation
ref_82819 = ref_82701 # MOV operation
ref_82831 = ref_81594 # MOV operation
ref_82833 = (ref_82831 & ref_82819) # AND operation
ref_82984 = ref_80225 # MOV operation
ref_82988 = ref_82833 # MOV operation
ref_82990 = ((ref_82988 + ref_82984) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_84141 = ref_82990 # MOV operation
ref_85242 = ref_84141 # MOV operation
ref_86585 = ref_78014 # MOV operation
ref_86703 = ref_86585 # MOV operation
ref_86717 = (0x3F & ref_86703) # AND operation
ref_86815 = ref_86717 # MOV operation
ref_86829 = ((ref_86815 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_86971 = ref_85242 # MOV operation
ref_86975 = ref_86829 # MOV operation
ref_86977 = (ref_86975 | ref_86971) # OR operation
ref_88127 = ref_86977 # MOV operation
ref_89359 = ref_74354 # MOV operation
ref_89607 = ref_89359 # MOV operation
ref_89615 = (ref_89607 >> (0x4 & 0x3F)) # SHR operation
ref_89622 = ref_89615 # MOV operation
ref_89760 = ref_89622 # MOV operation
ref_89774 = (0xF & ref_89760) # AND operation
ref_90047 = ref_89774 # MOV operation
ref_90053 = (0x1 | ref_90047) # OR operation
ref_91159 = ref_62253 # MOV operation
ref_91232 = ref_91159 # MOV operation
ref_91244 = ref_90053 # MOV operation
ref_91246 = ((ref_91232 << ((ref_91244 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_92352 = ref_62253 # MOV operation
ref_93564 = ref_74354 # MOV operation
ref_93812 = ref_93564 # MOV operation
ref_93820 = (ref_93812 >> (0x4 & 0x3F)) # SHR operation
ref_93827 = ref_93820 # MOV operation
ref_93965 = ref_93827 # MOV operation
ref_93979 = (0xF & ref_93965) # AND operation
ref_94252 = ref_93979 # MOV operation
ref_94258 = (0x1 | ref_94252) # OR operation
ref_94499 = ref_94258 # MOV operation
ref_94501 = ((0x40 - ref_94499) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_94509 = ref_94501 # MOV operation
ref_94646 = ref_92352 # MOV operation
ref_94650 = ref_94509 # MOV operation
ref_94652 = (ref_94650 & 0xFFFFFFFF) # MOV operation
ref_94654 = (ref_94646 >> ((ref_94652 & 0xFF) & 0x3F)) # SHR operation
ref_94661 = ref_94654 # MOV operation
ref_94798 = ref_91246 # MOV operation
ref_94802 = ref_94661 # MOV operation
ref_94804 = (ref_94802 | ref_94798) # OR operation
ref_95910 = ref_78014 # MOV operation
ref_96991 = ref_88127 # MOV operation
ref_97117 = ref_95910 # MOV operation
ref_97121 = ref_96991 # MOV operation
ref_97123 = ((ref_97121 + ref_97117) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_97275 = ref_94804 # MOV operation
ref_97279 = ref_97123 # MOV operation
ref_97281 = (((sx(0x40, ref_97279) * sx(0x40, ref_97275)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_98343 = ref_97281 # MOV operation
ref_98611 = ref_98343 # MOV operation
ref_98613 = ref_98611 # MOV operation

print ref_98613 & 0xffffffffffffffff
