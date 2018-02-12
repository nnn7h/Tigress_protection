#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_267286 = ref_278 # MOV operation
ref_300094 = ref_267286 # MOV operation
ref_300102 = (ref_300094 >> (0x3 & 0x3F)) # SHR operation
ref_300109 = ref_300102 # MOV operation
ref_447794 = ref_278 # MOV operation
ref_464174 = ref_447794 # MOV operation
ref_464188 = ((ref_464174 << (0x3D & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_480601 = ref_300109 # MOV operation
ref_480605 = ref_464188 # MOV operation
ref_480607 = (ref_480605 | ref_480601) # OR operation
ref_497012 = ref_480607 # MOV operation
ref_497026 = ((ref_497012 - 0x3FEFFF7F) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_497034 = ref_497026 # MOV operation
ref_513442 = ref_497034 # MOV operation
ref_513444 = ((ref_513442 >> 56) & 0xFF) # Byte reference - MOV operation
ref_513445 = ((ref_513442 >> 48) & 0xFF) # Byte reference - MOV operation
ref_513446 = ((ref_513442 >> 40) & 0xFF) # Byte reference - MOV operation
ref_513447 = ((ref_513442 >> 32) & 0xFF) # Byte reference - MOV operation
ref_513448 = ((ref_513442 >> 24) & 0xFF) # Byte reference - MOV operation
ref_513449 = ((ref_513442 >> 16) & 0xFF) # Byte reference - MOV operation
ref_513450 = ((ref_513442 >> 8) & 0xFF) # Byte reference - MOV operation
ref_513451 = (ref_513442 & 0xFF) # Byte reference - MOV operation
ref_776077 = ref_278 # MOV operation
ref_907407 = ref_513442 # MOV operation
ref_923795 = ref_776077 # MOV operation
ref_923799 = ref_907407 # MOV operation
ref_923801 = (ref_923799 | ref_923795) # OR operation
ref_940206 = ref_923801 # MOV operation
ref_940220 = ((ref_940206 - 0x11E59B96) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_940228 = ref_940220 # MOV operation
ref_956636 = ref_940228 # MOV operation
ref_956638 = ((ref_956636 >> 56) & 0xFF) # Byte reference - MOV operation
ref_956639 = ((ref_956636 >> 48) & 0xFF) # Byte reference - MOV operation
ref_956640 = ((ref_956636 >> 40) & 0xFF) # Byte reference - MOV operation
ref_956641 = ((ref_956636 >> 32) & 0xFF) # Byte reference - MOV operation
ref_956642 = ((ref_956636 >> 24) & 0xFF) # Byte reference - MOV operation
ref_956643 = ((ref_956636 >> 16) & 0xFF) # Byte reference - MOV operation
ref_956644 = ((ref_956636 >> 8) & 0xFF) # Byte reference - MOV operation
ref_956645 = (ref_956636 & 0xFF) # Byte reference - MOV operation
ref_1202851 = ref_278 # MOV operation
ref_1334181 = ref_513442 # MOV operation
ref_1350569 = ref_1202851 # MOV operation
ref_1350573 = ref_1334181 # MOV operation
ref_1350575 = (((sx(0x40, ref_1350573) * sx(0x40, ref_1350569)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_1498347 = ref_956636 # MOV operation
ref_1514727 = ref_1498347 # MOV operation
ref_1514741 = ((ref_1514727 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1531154 = ref_1350575 # MOV operation
ref_1531158 = ref_1514741 # MOV operation
ref_1531160 = (((sx(0x40, ref_1531158) * sx(0x40, ref_1531154)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_1547570 = ref_1531160 # MOV operation
ref_1810205 = ref_278 # MOV operation
ref_1826585 = ref_1810205 # MOV operation
ref_1826599 = ((ref_1826585 - 0x2000000007A4C37E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1826607 = ref_1826599 # MOV operation
ref_1843015 = ref_1826607 # MOV operation
ref_2236908 = ((((ref_513444) << 8 | ref_513445) << 8 | ref_513446) << 8 | ref_513447) # MOV operation
ref_2269724 = (ref_2236908 & 0xFFFFFFFF) # MOV operation
ref_2515892 = ((((ref_513448) << 8 | ref_513449) << 8 | ref_513450) << 8 | ref_513451) # MOV operation
ref_2762048 = (ref_2515892 & 0xFFFFFFFF) # MOV operation
ref_2762050 = (((ref_2762048 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_2762051 = (((ref_2762048 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_2762052 = (((ref_2762048 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_2762053 = ((ref_2762048 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_2794876 = (ref_2269724 & 0xFFFFFFFF) # MOV operation
ref_3041032 = (ref_2794876 & 0xFFFFFFFF) # MOV operation
ref_3041034 = (((ref_3041032 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_3041035 = (((ref_3041032 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_3041036 = (((ref_3041032 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_3041037 = ((ref_3041032 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_3320112 = ((((((((ref_2762050) << 8 | ref_2762051) << 8 | ref_2762052) << 8 | ref_2762053) << 8 | ref_3041034) << 8 | ref_3041035) << 8 | ref_3041036) << 8 | ref_3041037) # MOV operation
ref_3517094 = ref_1547570 # MOV operation
ref_3648424 = ref_1547570 # MOV operation
ref_3664812 = ref_3517094 # MOV operation
ref_3664816 = ref_3648424 # MOV operation
ref_3664818 = ((ref_3664816 + ref_3664812) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_3697652 = ref_3664818 # MOV operation
ref_3697658 = (0x3F & ref_3697652) # AND operation
ref_3714063 = ref_3697658 # MOV operation
ref_3714077 = ((ref_3714063 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_3730490 = ref_3320112 # MOV operation
ref_3730494 = ref_3714077 # MOV operation
ref_3730496 = (ref_3730494 | ref_3730490) # OR operation
ref_3746909 = ref_3730496 # MOV operation
ref_4190034 = ((((ref_956638) << 8 | ref_956639) << 8 | ref_956640) << 8 | ref_956641) # MOV operation
ref_4222850 = (ref_4190034 & 0xFFFFFFFF) # MOV operation
ref_4469018 = ((((ref_956642) << 8 | ref_956643) << 8 | ref_956644) << 8 | ref_956645) # MOV operation
ref_4715174 = (ref_4469018 & 0xFFFFFFFF) # MOV operation
ref_4715176 = (((ref_4715174 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_4715177 = (((ref_4715174 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_4715178 = (((ref_4715174 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_4715179 = ((ref_4715174 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_4748002 = (ref_4222850 & 0xFFFFFFFF) # MOV operation
ref_4994158 = (ref_4748002 & 0xFFFFFFFF) # MOV operation
ref_4994160 = (((ref_4994158 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_4994161 = (((ref_4994158 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_4994162 = (((ref_4994158 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_4994163 = ((ref_4994158 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_5273238 = ((((((((ref_4715176) << 8 | ref_4715177) << 8 | ref_4715178) << 8 | ref_4715179) << 8 | ref_4994160) << 8 | ref_4994161) << 8 | ref_4994162) << 8 | ref_4994163) # MOV operation
ref_5470220 = ref_1843015 # MOV operation
ref_5601550 = ref_1547570 # MOV operation
ref_5617938 = ref_5470220 # MOV operation
ref_5617942 = ref_5601550 # MOV operation
ref_5617944 = ((ref_5617942 + ref_5617938) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5650778 = ref_5617944 # MOV operation
ref_5650784 = (0x3F & ref_5650778) # AND operation
ref_5667189 = ref_5650784 # MOV operation
ref_5667203 = ((ref_5667189 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_5683616 = ref_5273238 # MOV operation
ref_5683620 = ref_5667203 # MOV operation
ref_5683622 = (ref_5683620 | ref_5683616) # OR operation
ref_5700035 = ref_5683622 # MOV operation
ref_5700037 = ((ref_5700035 >> 56) & 0xFF) # Byte reference - MOV operation
ref_5700038 = ((ref_5700035 >> 48) & 0xFF) # Byte reference - MOV operation
ref_5700039 = ((ref_5700035 >> 40) & 0xFF) # Byte reference - MOV operation
ref_5700040 = ((ref_5700035 >> 32) & 0xFF) # Byte reference - MOV operation
ref_5700041 = ((ref_5700035 >> 24) & 0xFF) # Byte reference - MOV operation
ref_5700042 = ((ref_5700035 >> 16) & 0xFF) # Byte reference - MOV operation
ref_5700043 = ((ref_5700035 >> 8) & 0xFF) # Byte reference - MOV operation
ref_5700044 = (ref_5700035 & 0xFF) # Byte reference - MOV operation
ref_6159537 = ref_5700039 # MOVZX operation
ref_6192349 = (ref_6159537 & 0xFF) # MOVZX operation
ref_6422121 = ref_5700043 # MOVZX operation
ref_6651881 = (ref_6422121 & 0xFF) # MOVZX operation
ref_6651883 = (ref_6651881 & 0xFF) # Byte reference - MOV operation
ref_6684705 = (ref_6192349 & 0xFF) # MOVZX operation
ref_6914465 = (ref_6684705 & 0xFF) # MOVZX operation
ref_6914467 = (ref_6914465 & 0xFF) # Byte reference - MOV operation
ref_7160681 = ref_1547570 # MOV operation
ref_7292011 = ref_1843015 # MOV operation
ref_7308399 = ref_7160681 # MOV operation
ref_7308403 = ref_7292011 # MOV operation
ref_7308405 = (ref_7308403 & ref_7308399) # AND operation
ref_7341238 = ref_7308405 # MOV operation
ref_7341244 = (0xF & ref_7341238) # AND operation
ref_7374077 = ref_7341244 # MOV operation
ref_7374083 = (0x1 | ref_7374077) # OR operation
ref_7505438 = ref_3746909 # MOV operation
ref_7636768 = ((((((((ref_5700037) << 8 | ref_5700038) << 8 | ref_6651883) << 8 | ref_5700040) << 8 | ref_5700041) << 8 | ref_5700042) << 8 | ref_6914467) << 8 | ref_5700044) # MOV operation
ref_7653156 = ref_7505438 # MOV operation
ref_7653160 = ref_7636768 # MOV operation
ref_7653162 = ((ref_7653160 + ref_7653156) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7669568 = ref_7653162 # MOV operation
ref_7669580 = ref_7374083 # MOV operation
ref_7669582 = ((ref_7669568 << ((ref_7669580 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7800937 = ref_3746909 # MOV operation
ref_7932267 = ((((((((ref_5700037) << 8 | ref_5700038) << 8 | ref_6651883) << 8 | ref_5700040) << 8 | ref_5700041) << 8 | ref_5700042) << 8 | ref_6914467) << 8 | ref_5700044) # MOV operation
ref_7948655 = ref_7800937 # MOV operation
ref_7948659 = ref_7932267 # MOV operation
ref_7948661 = ((ref_7948659 + ref_7948655) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8080017 = ref_1547570 # MOV operation
ref_8211347 = ref_1843015 # MOV operation
ref_8227735 = ref_8080017 # MOV operation
ref_8227739 = ref_8211347 # MOV operation
ref_8227741 = (ref_8227739 & ref_8227735) # AND operation
ref_8260574 = ref_8227741 # MOV operation
ref_8260580 = (0xF & ref_8260574) # AND operation
ref_8293413 = ref_8260580 # MOV operation
ref_8293419 = (0x1 | ref_8293413) # OR operation
ref_8326256 = ref_8293419 # MOV operation
ref_8326258 = ((0x40 - ref_8326256) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_8326266 = ref_8326258 # MOV operation
ref_8342674 = ref_7948661 # MOV operation
ref_8342678 = ref_8326266 # MOV operation
ref_8342680 = (ref_8342678 & 0xFFFFFFFF) # MOV operation
ref_8342682 = (ref_8342674 >> ((ref_8342680 & 0xFF) & 0x3F)) # SHR operation
ref_8342689 = ref_8342682 # MOV operation
ref_8359097 = ref_7669582 # MOV operation
ref_8359101 = ref_8342689 # MOV operation
ref_8359103 = (ref_8359101 | ref_8359097) # OR operation
ref_8375516 = ref_8359103 # MOV operation
ref_8408335 = ref_8375516 # MOV operation
ref_8408337 = ref_8408335 # MOV operation

print ref_8408337 & 0xffffffffffffffff
