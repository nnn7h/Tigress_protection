#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_85142 = ref_278 # MOV operation
ref_90138 = ref_85142 # MOV operation
ref_90152 = ((ref_90138 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_135386 = ref_278 # MOV operation
ref_140382 = ref_135386 # MOV operation
ref_140396 = (ref_140382 >> (0x33 & 0x3F)) # SHR operation
ref_145425 = ref_90152 # MOV operation
ref_145429 = ref_140396 # MOV operation
ref_145431 = (ref_145429 | ref_145425) # OR operation
ref_150460 = ref_145431 # MOV operation
ref_230951 = ref_278 # MOV operation
ref_235947 = ref_230951 # MOV operation
ref_235963 = ((((0x0) << 64 | ref_235947) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_246024 = ref_235963 # MOV operation
ref_246030 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_246024)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_251056 = ref_246030 # MOV operation
ref_326596 = ref_150460 # MOV operation
ref_366854 = ref_251056 # MOV operation
ref_371858 = ref_326596 # MOV operation
ref_371862 = ref_366854 # MOV operation
ref_371864 = (ref_371862 | ref_371858) # OR operation
ref_412062 = ref_278 # MOV operation
ref_417058 = ref_412062 # MOV operation
ref_417070 = ref_371864 # MOV operation
ref_417072 = ((ref_417070 + ref_417058) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_422102 = ref_417072 # MOV operation
ref_507714 = ref_150460 # MOV operation
ref_517754 = ref_507714 # MOV operation
ref_517760 = ((ref_517754 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_517768 = ref_517760 # MOV operation
ref_522796 = ref_517768 # MOV operation
ref_522798 = ((0x28E5FC28 - ref_522796) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_522806 = ref_522798 # MOV operation
ref_527822 = ref_522806 # MOV operation
ref_527836 = (ref_527822 >> (0x2 & 0x3F)) # SHR operation
ref_537901 = ref_527836 # MOV operation
ref_537907 = (0x7 & ref_537901) # AND operation
ref_547972 = ref_537907 # MOV operation
ref_547978 = (0x1 | ref_547972) # OR operation
ref_588261 = ref_251056 # MOV operation
ref_628434 = ref_278 # MOV operation
ref_633430 = ref_628434 # MOV operation
ref_633442 = ref_588261 # MOV operation
ref_633444 = ((ref_633442 + ref_633430) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_638466 = ref_633444 # MOV operation
ref_638478 = ref_547978 # MOV operation
ref_638480 = (ref_638466 >> ((ref_638478 & 0xFF) & 0x3F)) # SHR operation
ref_643509 = ref_638480 # MOV operation
ref_724085 = ref_643509 # MOV operation
ref_729081 = ref_724085 # MOV operation
ref_729095 = (ref_729081 >> (0x1 & 0x3F)) # SHR operation
ref_739160 = ref_729095 # MOV operation
ref_739166 = (0x7 & ref_739160) # AND operation
ref_749231 = ref_739166 # MOV operation
ref_749237 = (0x1 | ref_749231) # OR operation
ref_789520 = ref_643509 # MOV operation
ref_794516 = ref_789520 # MOV operation
ref_794528 = ref_749237 # MOV operation
ref_794530 = (ref_794516 >> ((ref_794528 & 0xFF) & 0x3F)) # SHR operation
ref_799559 = ref_794530 # MOV operation
ref_799561 = ((ref_799559 >> 56) & 0xFF) # Byte reference - MOV operation
ref_799562 = ((ref_799559 >> 48) & 0xFF) # Byte reference - MOV operation
ref_799563 = ((ref_799559 >> 40) & 0xFF) # Byte reference - MOV operation
ref_799564 = ((ref_799559 >> 32) & 0xFF) # Byte reference - MOV operation
ref_799565 = ((ref_799559 >> 24) & 0xFF) # Byte reference - MOV operation
ref_799566 = ((ref_799559 >> 16) & 0xFF) # Byte reference - MOV operation
ref_799567 = ((ref_799559 >> 8) & 0xFF) # Byte reference - MOV operation
ref_799568 = (ref_799559 & 0xFF) # Byte reference - MOV operation
ref_920364 = ref_422102 # MOV operation
ref_970666 = ref_150460 # MOV operation
ref_980706 = ref_970666 # MOV operation
ref_980712 = (0x7 & ref_980706) # AND operation
ref_985733 = ref_980712 # MOV operation
ref_985747 = ((ref_985733 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_990776 = ref_920364 # MOV operation
ref_990780 = ref_985747 # MOV operation
ref_990782 = (ref_990780 | ref_990776) # OR operation
ref_995811 = ref_990782 # MOV operation
ref_1071263 = ((((ref_799561) << 8 | ref_799562) << 8 | ref_799563) << 8 | ref_799564) # MOV operation
ref_1076263 = (ref_1071263 & 0xFFFFFFFF) # MOV operation
ref_1212051 = ((((ref_799565) << 8 | ref_799566) << 8 | ref_799567) << 8 | ref_799568) # MOV operation
ref_1217051 = (ref_1212051 & 0xFFFFFFFF) # MOV operation
ref_1292499 = (ref_1076263 & 0xFFFFFFFF) # MOV operation
ref_1297499 = (ref_1292499 & 0xFFFFFFFF) # MOV operation
ref_1433380 = ref_995811 # MOV operation
ref_1483682 = ref_995811 # MOV operation
ref_1493722 = ref_1483682 # MOV operation
ref_1493728 = (0x7 & ref_1493722) # AND operation
ref_1498749 = ref_1493728 # MOV operation
ref_1498763 = ((ref_1498749 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1503792 = ref_1433380 # MOV operation
ref_1503796 = ref_1498763 # MOV operation
ref_1503798 = (ref_1503796 | ref_1503792) # OR operation
ref_1508827 = ref_1503798 # MOV operation
ref_1584279 = (ref_1217051 & 0xFFFFFFFF) # MOV operation
ref_1589279 = (ref_1584279 & 0xFFFFFFFF) # MOV operation
ref_1725067 = (ref_1297499 & 0xFFFFFFFF) # MOV operation
ref_1730067 = (ref_1725067 & 0xFFFFFFFF) # MOV operation
ref_1730069 = (((ref_1730067 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_1730070 = (((ref_1730067 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_1730071 = (((ref_1730067 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_1730072 = ((ref_1730067 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_1805515 = (ref_1589279 & 0xFFFFFFFF) # MOV operation
ref_1810515 = (ref_1805515 & 0xFFFFFFFF) # MOV operation
ref_1810517 = (((ref_1810515 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_1810518 = (((ref_1810515 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_1810519 = (((ref_1810515 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_1810520 = ((ref_1810515 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_1956321 = ref_1508827 # MOV operation
ref_1996579 = ((((((((ref_1730069) << 8 | ref_1730070) << 8 | ref_1730071) << 8 | ref_1730072) << 8 | ref_1810517) << 8 | ref_1810518) << 8 | ref_1810519) << 8 | ref_1810520) # MOV operation
ref_2006619 = ref_1996579 # MOV operation
ref_2006625 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_2006619)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_2011651 = ref_1956321 # MOV operation
ref_2011655 = ref_2006625 # MOV operation
ref_2011657 = (ref_2011655 ^ ref_2011651) # XOR operation
ref_2021722 = ref_2011657 # MOV operation
ref_2021728 = (0xF & ref_2021722) # AND operation
ref_2031793 = ref_2021728 # MOV operation
ref_2031799 = (0x1 | ref_2031793) # OR operation
ref_2072082 = ref_150460 # MOV operation
ref_2112340 = ref_251056 # MOV operation
ref_2117344 = ref_2072082 # MOV operation
ref_2117348 = ref_2112340 # MOV operation
ref_2117350 = (((sx(0x40, ref_2117348) * sx(0x40, ref_2117344)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_2122368 = ref_2117350 # MOV operation
ref_2122380 = ref_2031799 # MOV operation
ref_2122382 = ((ref_2122368 << ((ref_2122380 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_2167701 = ref_1508827 # MOV operation
ref_2207959 = ((((((((ref_1730069) << 8 | ref_1730070) << 8 | ref_1730071) << 8 | ref_1730072) << 8 | ref_1810517) << 8 | ref_1810518) << 8 | ref_1810519) << 8 | ref_1810520) # MOV operation
ref_2217999 = ref_2207959 # MOV operation
ref_2218005 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_2217999)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_2223031 = ref_2167701 # MOV operation
ref_2223035 = ref_2218005 # MOV operation
ref_2223037 = (ref_2223035 ^ ref_2223031) # XOR operation
ref_2233102 = ref_2223037 # MOV operation
ref_2233108 = (0xF & ref_2233102) # AND operation
ref_2243173 = ref_2233108 # MOV operation
ref_2243179 = (0x1 | ref_2243173) # OR operation
ref_2248212 = ref_2243179 # MOV operation
ref_2248214 = ((0x40 - ref_2248212) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_2248222 = ref_2248214 # MOV operation
ref_2288500 = ref_150460 # MOV operation
ref_2328758 = ref_251056 # MOV operation
ref_2333762 = ref_2288500 # MOV operation
ref_2333766 = ref_2328758 # MOV operation
ref_2333768 = (((sx(0x40, ref_2333766) * sx(0x40, ref_2333762)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_2338786 = ref_2333768 # MOV operation
ref_2338798 = ref_2248222 # MOV operation
ref_2338800 = (ref_2338786 >> ((ref_2338798 & 0xFF) & 0x3F)) # SHR operation
ref_2343829 = ref_2122382 # MOV operation
ref_2343833 = ref_2338800 # MOV operation
ref_2343835 = (ref_2343833 | ref_2343829) # OR operation
ref_2348864 = ref_2343835 # MOV operation
ref_2358915 = ref_2348864 # MOV operation
ref_2358917 = ref_2358915 # MOV operation

print ref_2358917 & 0xffffffffffffffff
