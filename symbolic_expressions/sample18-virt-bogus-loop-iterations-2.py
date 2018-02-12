#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_42134 = ref_278 # MOV operation
ref_46798 = ref_42134 # MOV operation
ref_46806 = ((ref_46798 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_46813 = ref_46806 # MOV operation
ref_65502 = ref_278 # MOV operation
ref_70166 = ref_65502 # MOV operation
ref_70174 = (ref_70166 >> (0xD & 0x3F)) # SHR operation
ref_70181 = ref_70174 # MOV operation
ref_72509 = ref_70181 # MOV operation
ref_72521 = ref_46813 # MOV operation
ref_72523 = (ref_72521 | ref_72509) # OR operation
ref_74856 = ref_72523 # MOV operation
ref_74870 = ((0x2EA4A1C39AF5800 + ref_74856) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_77212 = ref_74870 # MOV operation
ref_112432 = ref_77212 # MOV operation
ref_131101 = ref_278 # MOV operation
ref_133409 = ref_131101 # MOV operation
ref_133421 = ref_112432 # MOV operation
ref_133423 = ((ref_133409 - ref_133421) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_133431 = ref_133423 # MOV operation
ref_135767 = ref_133431 # MOV operation
ref_170902 = ref_278 # MOV operation
ref_175566 = ref_170902 # MOV operation
ref_175574 = (ref_175566 >> (0x37 & 0x3F)) # SHR operation
ref_175581 = ref_175574 # MOV operation
ref_194270 = ref_278 # MOV operation
ref_198934 = ref_194270 # MOV operation
ref_198942 = ((ref_198934 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_198949 = ref_198942 # MOV operation
ref_201277 = ref_198949 # MOV operation
ref_201289 = ref_175581 # MOV operation
ref_201291 = (ref_201289 | ref_201277) # OR operation
ref_203632 = ref_201291 # MOV operation
ref_241115 = ref_278 # MOV operation
ref_243423 = ref_241115 # MOV operation
ref_243437 = (0x3E908497 | ref_243423) # OR operation
ref_245778 = ref_243437 # MOV operation
ref_266868 = ref_245778 # MOV operation
ref_285622 = ref_203632 # MOV operation
ref_287930 = ref_285622 # MOV operation
ref_287942 = ref_266868 # MOV operation
ref_287944 = ((ref_287930 - ref_287942) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_287952 = ref_287944 # MOV operation
ref_306726 = ref_77212 # MOV operation
ref_327828 = ref_135767 # MOV operation
ref_332492 = ref_327828 # MOV operation
ref_332500 = (ref_332492 >> (0x2 & 0x3F)) # SHR operation
ref_332507 = ref_332500 # MOV operation
ref_337191 = ref_332507 # MOV operation
ref_337197 = (0xF & ref_337191) # AND operation
ref_339530 = ref_337197 # MOV operation
ref_339544 = (0x1 | ref_339530) # OR operation
ref_344237 = ref_339544 # MOV operation
ref_344239 = ((0x40 - ref_344237) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_344247 = ref_344239 # MOV operation
ref_346583 = ref_306726 # MOV operation
ref_346587 = ref_344247 # MOV operation
ref_346589 = (ref_346587 & 0xFFFFFFFF) # MOV operation
ref_346591 = ((ref_346583 << ((ref_346589 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_346598 = ref_346591 # MOV operation
ref_365372 = ref_77212 # MOV operation
ref_386474 = ref_135767 # MOV operation
ref_391138 = ref_386474 # MOV operation
ref_391146 = (ref_391138 >> (0x2 & 0x3F)) # SHR operation
ref_391153 = ref_391146 # MOV operation
ref_395837 = ref_391153 # MOV operation
ref_395843 = (0xF & ref_395837) # AND operation
ref_398176 = ref_395843 # MOV operation
ref_398190 = (0x1 | ref_398176) # OR operation
ref_400531 = ref_365372 # MOV operation
ref_400535 = ref_398190 # MOV operation
ref_400537 = (ref_400535 & 0xFFFFFFFF) # MOV operation
ref_400539 = (ref_400531 >> ((ref_400537 & 0xFF) & 0x3F)) # SHR operation
ref_400546 = ref_400539 # MOV operation
ref_402874 = ref_400546 # MOV operation
ref_402886 = ref_346598 # MOV operation
ref_402888 = (ref_402886 | ref_402874) # OR operation
ref_405221 = ref_402888 # MOV operation
ref_405233 = ref_287952 # MOV operation
ref_405235 = ((ref_405221 - ref_405233) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_405237 = ((((ref_405221 ^ (ref_405233 ^ ref_405235)) ^ ((ref_405221 ^ ref_405235) & (ref_405221 ^ ref_405233))) >> 63) & 0x1) # Carry flag
ref_405243 = ((((ref_405233 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (ref_405237 == 0x1) else 0x0)) # SETB operation
ref_405245 = (ref_405243 & 0xFF) # MOVZX operation
ref_407565 = (ref_405245 & 0xFFFFFFFF) # MOV operation
ref_407567 = ((ref_407565 & 0xFFFFFFFF) & (ref_407565 & 0xFFFFFFFF)) # TEST operation
ref_407572 = (0x1 if (ref_407567 == 0x0) else 0x0) # Zero flag
ref_407574 = (0x205F if (ref_407572 == 0x1) else 0x2041) # Program Counter


if (ref_407572 == 0x1):
    ref_970444 = SymVar_0
    ref_970459 = ref_970444 # MOV operation
    ref_1012320 = ref_970459 # MOV operation
    ref_1016984 = ref_1012320 # MOV operation
    ref_1016992 = ((ref_1016984 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1016999 = ref_1016992 # MOV operation
    ref_1035688 = ref_970459 # MOV operation
    ref_1040352 = ref_1035688 # MOV operation
    ref_1040360 = (ref_1040352 >> (0xD & 0x3F)) # SHR operation
    ref_1040367 = ref_1040360 # MOV operation
    ref_1042695 = ref_1040367 # MOV operation
    ref_1042707 = ref_1016999 # MOV operation
    ref_1042709 = (ref_1042707 | ref_1042695) # OR operation
    ref_1045042 = ref_1042709 # MOV operation
    ref_1045056 = ((0x2EA4A1C39AF5800 + ref_1045042) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_1047398 = ref_1045056 # MOV operation
    ref_1082618 = ref_1047398 # MOV operation
    ref_1101287 = ref_970459 # MOV operation
    ref_1103595 = ref_1101287 # MOV operation
    ref_1103607 = ref_1082618 # MOV operation
    ref_1103609 = ((ref_1103595 - ref_1103607) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_1103617 = ref_1103609 # MOV operation
    ref_1105953 = ref_1103617 # MOV operation
    ref_1141088 = ref_970459 # MOV operation
    ref_1145752 = ref_1141088 # MOV operation
    ref_1145760 = (ref_1145752 >> (0x37 & 0x3F)) # SHR operation
    ref_1145767 = ref_1145760 # MOV operation
    ref_1164456 = ref_970459 # MOV operation
    ref_1169120 = ref_1164456 # MOV operation
    ref_1169128 = ((ref_1169120 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1169135 = ref_1169128 # MOV operation
    ref_1171463 = ref_1169135 # MOV operation
    ref_1171475 = ref_1145767 # MOV operation
    ref_1171477 = (ref_1171475 | ref_1171463) # OR operation
    ref_1173818 = ref_1171477 # MOV operation
    ref_1211301 = ref_970459 # MOV operation
    ref_1213609 = ref_1211301 # MOV operation
    ref_1213623 = (0x3E908497 | ref_1213609) # OR operation
    ref_1215964 = ref_1213623 # MOV operation
    ref_1415229 = ref_1047398 # MOV operation
    ref_1436331 = ref_1105953 # MOV operation
    ref_1440995 = ref_1436331 # MOV operation
    ref_1441003 = (ref_1440995 >> (0x4 & 0x3F)) # SHR operation
    ref_1441010 = ref_1441003 # MOV operation
    ref_1445694 = ref_1441010 # MOV operation
    ref_1445700 = (0xF & ref_1445694) # AND operation
    ref_1448033 = ref_1445700 # MOV operation
    ref_1448047 = (0x1 | ref_1448033) # OR operation
    ref_1452740 = ref_1448047 # MOV operation
    ref_1452742 = ((0x40 - ref_1452740) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_1452750 = ref_1452742 # MOV operation
    ref_1455086 = ref_1415229 # MOV operation
    ref_1455090 = ref_1452750 # MOV operation
    ref_1455092 = (ref_1455090 & 0xFFFFFFFF) # MOV operation
    ref_1455094 = (ref_1455086 >> ((ref_1455092 & 0xFF) & 0x3F)) # SHR operation
    ref_1455101 = ref_1455094 # MOV operation
    ref_1473875 = ref_1047398 # MOV operation
    ref_1494977 = ref_1105953 # MOV operation
    ref_1499641 = ref_1494977 # MOV operation
    ref_1499649 = (ref_1499641 >> (0x4 & 0x3F)) # SHR operation
    ref_1499656 = ref_1499649 # MOV operation
    ref_1504340 = ref_1499656 # MOV operation
    ref_1504346 = (0xF & ref_1504340) # AND operation
    ref_1506679 = ref_1504346 # MOV operation
    ref_1506693 = (0x1 | ref_1506679) # OR operation
    ref_1509034 = ref_1473875 # MOV operation
    ref_1509038 = ref_1506693 # MOV operation
    ref_1509040 = (ref_1509038 & 0xFFFFFFFF) # MOV operation
    ref_1509042 = ((ref_1509034 << ((ref_1509040 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1509049 = ref_1509042 # MOV operation
    ref_1511377 = ref_1509049 # MOV operation
    ref_1511389 = ref_1455101 # MOV operation
    ref_1511391 = (ref_1511389 | ref_1511377) # OR operation
    ref_1532518 = ref_1215964 # MOV operation
    ref_1551272 = ref_1173818 # MOV operation
    ref_1553580 = ref_1551272 # MOV operation
    ref_1553592 = ref_1532518 # MOV operation
    ref_1553594 = (ref_1553592 | ref_1553580) # OR operation
    ref_1558283 = ref_1553594 # MOV operation
    ref_1558291 = (ref_1558283 >> (0x4 & 0x3F)) # SHR operation
    ref_1558298 = ref_1558291 # MOV operation
    ref_1562982 = ref_1558298 # MOV operation
    ref_1562988 = (0x7 & ref_1562982) # AND operation
    ref_1565321 = ref_1562988 # MOV operation
    ref_1565335 = (0x1 | ref_1565321) # OR operation
    ref_1567676 = ref_1511391 # MOV operation
    ref_1567680 = ref_1565335 # MOV operation
    ref_1567682 = (ref_1567680 & 0xFFFFFFFF) # MOV operation
    ref_1567684 = (ref_1567676 >> ((ref_1567682 & 0xFF) & 0x3F)) # SHR operation
    ref_1567691 = ref_1567684 # MOV operation
    ref_1570027 = ref_1567691 # MOV operation
    ref_1574702 = ref_1570027 # MOV operation
    ref_1574704 = ref_1574702 # MOV operation
    endb = ref_1574704


else:
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_42134 = ref_278 # MOV operation
    ref_46798 = ref_42134 # MOV operation
    ref_46806 = ((ref_46798 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_46813 = ref_46806 # MOV operation
    ref_65502 = ref_278 # MOV operation
    ref_70166 = ref_65502 # MOV operation
    ref_70174 = (ref_70166 >> (0xD & 0x3F)) # SHR operation
    ref_70181 = ref_70174 # MOV operation
    ref_72509 = ref_70181 # MOV operation
    ref_72521 = ref_46813 # MOV operation
    ref_72523 = (ref_72521 | ref_72509) # OR operation
    ref_74856 = ref_72523 # MOV operation
    ref_74870 = ((0x2EA4A1C39AF5800 + ref_74856) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_77212 = ref_74870 # MOV operation
    ref_112432 = ref_77212 # MOV operation
    ref_131101 = ref_278 # MOV operation
    ref_133409 = ref_131101 # MOV operation
    ref_133421 = ref_112432 # MOV operation
    ref_133423 = ((ref_133409 - ref_133421) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_133431 = ref_133423 # MOV operation
    ref_135767 = ref_133431 # MOV operation
    ref_135769 = ((ref_135767 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_135770 = ((ref_135767 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_135771 = ((ref_135767 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_135772 = ((ref_135767 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_135773 = ((ref_135767 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_135774 = ((ref_135767 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_135775 = ((ref_135767 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_135776 = (ref_135767 & 0xFF) # Byte reference - MOV operation
    ref_170902 = ref_278 # MOV operation
    ref_175566 = ref_170902 # MOV operation
    ref_175574 = (ref_175566 >> (0x37 & 0x3F)) # SHR operation
    ref_175581 = ref_175574 # MOV operation
    ref_194270 = ref_278 # MOV operation
    ref_198934 = ref_194270 # MOV operation
    ref_198942 = ((ref_198934 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_198949 = ref_198942 # MOV operation
    ref_201277 = ref_198949 # MOV operation
    ref_201289 = ref_175581 # MOV operation
    ref_201291 = (ref_201289 | ref_201277) # OR operation
    ref_203632 = ref_201291 # MOV operation
    ref_241115 = ref_278 # MOV operation
    ref_243423 = ref_241115 # MOV operation
    ref_243437 = (0x3E908497 | ref_243423) # OR operation
    ref_245778 = ref_243437 # MOV operation
    ref_440362 = ((((ref_135769) << 8 | ref_135770) << 8 | ref_135771) << 8 | ref_135772) # MOV operation
    ref_445034 = (ref_440362 & 0xFFFFFFFF) # MOV operation
    ref_477802 = ((((ref_135773) << 8 | ref_135774) << 8 | ref_135775) << 8 | ref_135776) # MOV operation
    ref_510558 = (ref_477802 & 0xFFFFFFFF) # MOV operation
    ref_510560 = (((ref_510558 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_510561 = (((ref_510558 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_510562 = (((ref_510558 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_510563 = ((ref_510558 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_515242 = (ref_445034 & 0xFFFFFFFF) # MOV operation
    ref_547998 = (ref_515242 & 0xFFFFFFFF) # MOV operation
    ref_548000 = (((ref_547998 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_548001 = (((ref_547998 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_548002 = (((ref_547998 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_548003 = ((ref_547998 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_583214 = ref_77212 # MOV operation
    ref_587878 = ref_583214 # MOV operation
    ref_587884 = (0x3F & ref_587878) # AND operation
    ref_592573 = ref_587884 # MOV operation
    ref_592581 = ((ref_592573 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_592588 = ref_592581 # MOV operation
    ref_611362 = ref_77212 # MOV operation
    ref_613670 = ref_611362 # MOV operation
    ref_613682 = ref_592588 # MOV operation
    ref_613684 = (ref_613682 | ref_613670) # OR operation
    ref_616025 = ref_613684 # MOV operation
    ref_651245 = ref_616025 # MOV operation
    ref_655909 = ref_651245 # MOV operation
    ref_655915 = (0x1F & ref_655909) # AND operation
    ref_660604 = ref_655915 # MOV operation
    ref_660612 = ((ref_660604 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_660619 = ref_660612 # MOV operation
    ref_679393 = ref_245778 # MOV operation
    ref_681701 = ref_679393 # MOV operation
    ref_681713 = ref_660619 # MOV operation
    ref_681715 = (ref_681713 | ref_681701) # OR operation
    ref_684056 = ref_681715 # MOV operation
    ref_719276 = ref_203632 # MOV operation
    ref_738030 = ref_616025 # MOV operation
    ref_740338 = ref_738030 # MOV operation
    ref_740350 = ref_719276 # MOV operation
    ref_740352 = ((ref_740350 + ref_740338) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_745042 = ref_740352 # MOV operation
    ref_745048 = (0x1F & ref_745042) # AND operation
    ref_749737 = ref_745048 # MOV operation
    ref_749745 = ((ref_749737 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_749752 = ref_749745 # MOV operation
    ref_768526 = ref_616025 # MOV operation
    ref_770834 = ref_768526 # MOV operation
    ref_770846 = ref_749752 # MOV operation
    ref_770848 = (ref_770846 | ref_770834) # OR operation
    ref_773189 = ref_770848 # MOV operation
    ref_810649 = ref_773189 # MOV operation
    ref_831751 = ((((((((ref_510560) << 8 | ref_510561) << 8 | ref_510562) << 8 | ref_510563) << 8 | ref_548000) << 8 | ref_548001) << 8 | ref_548002) << 8 | ref_548003) # MOV operation
    ref_836415 = ref_831751 # MOV operation
    ref_836423 = (ref_836415 >> (0x4 & 0x3F)) # SHR operation
    ref_836430 = ref_836423 # MOV operation
    ref_841114 = ref_836430 # MOV operation
    ref_841120 = (0xF & ref_841114) # AND operation
    ref_843453 = ref_841120 # MOV operation
    ref_843467 = (0x1 | ref_843453) # OR operation
    ref_848160 = ref_843467 # MOV operation
    ref_848162 = ((0x40 - ref_848160) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_848170 = ref_848162 # MOV operation
    ref_850506 = ref_810649 # MOV operation
    ref_850510 = ref_848170 # MOV operation
    ref_850512 = (ref_850510 & 0xFFFFFFFF) # MOV operation
    ref_850514 = (ref_850506 >> ((ref_850512 & 0xFF) & 0x3F)) # SHR operation
    ref_850521 = ref_850514 # MOV operation
    ref_869295 = ref_773189 # MOV operation
    ref_890397 = ((((((((ref_510560) << 8 | ref_510561) << 8 | ref_510562) << 8 | ref_510563) << 8 | ref_548000) << 8 | ref_548001) << 8 | ref_548002) << 8 | ref_548003) # MOV operation
    ref_895061 = ref_890397 # MOV operation
    ref_895069 = (ref_895061 >> (0x4 & 0x3F)) # SHR operation
    ref_895076 = ref_895069 # MOV operation
    ref_899760 = ref_895076 # MOV operation
    ref_899766 = (0xF & ref_899760) # AND operation
    ref_902099 = ref_899766 # MOV operation
    ref_902113 = (0x1 | ref_902099) # OR operation
    ref_904454 = ref_869295 # MOV operation
    ref_904458 = ref_902113 # MOV operation
    ref_904460 = (ref_904458 & 0xFFFFFFFF) # MOV operation
    ref_904462 = ((ref_904454 << ((ref_904460 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_904469 = ref_904462 # MOV operation
    ref_906797 = ref_904469 # MOV operation
    ref_906809 = ref_850521 # MOV operation
    ref_906811 = (ref_906809 | ref_906797) # OR operation
    ref_927938 = ref_684056 # MOV operation
    ref_946692 = ref_203632 # MOV operation
    ref_949000 = ref_946692 # MOV operation
    ref_949012 = ref_927938 # MOV operation
    ref_949014 = (ref_949012 | ref_949000) # OR operation
    ref_953703 = ref_949014 # MOV operation
    ref_953711 = (ref_953703 >> (0x4 & 0x3F)) # SHR operation
    ref_953718 = ref_953711 # MOV operation
    ref_958402 = ref_953718 # MOV operation
    ref_958408 = (0x7 & ref_958402) # AND operation
    ref_960741 = ref_958408 # MOV operation
    ref_960755 = (0x1 | ref_960741) # OR operation
    ref_963096 = ref_906811 # MOV operation
    ref_963100 = ref_960755 # MOV operation
    ref_963102 = (ref_963100 & 0xFFFFFFFF) # MOV operation
    ref_963104 = (ref_963096 >> ((ref_963102 & 0xFF) & 0x3F)) # SHR operation
    ref_963111 = ref_963104 # MOV operation
    ref_965447 = ref_963111 # MOV operation
    ref_970122 = ref_965447 # MOV operation
    ref_970124 = ref_970122 # MOV operation
    endb = ref_970124


print endb & 0xffffffffffffffff
