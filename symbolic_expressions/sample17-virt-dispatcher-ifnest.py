#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_7366 = ref_278 # MOV operation
ref_7684 = ref_7366 # MOV operation
ref_7692 = ((ref_7684 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7699 = ref_7692 # MOV operation
ref_9040 = ref_278 # MOV operation
ref_9286 = ref_9040 # MOV operation
ref_9294 = (ref_9286 >> (0x7 & 0x3F)) # SHR operation
ref_9301 = ref_9294 # MOV operation
ref_9510 = ref_9301 # MOV operation
ref_9522 = ref_7699 # MOV operation
ref_9524 = (ref_9522 | ref_9510) # OR operation
ref_9701 = ref_9524 # MOV operation
ref_12861 = ref_9701 # MOV operation
ref_13102 = ref_12861 # MOV operation
ref_13104 = ((ref_13102 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_13268 = ref_13104 # MOV operation
ref_13270 = (ref_13268 & 0x1D5ABF66) # AND operation
ref_14616 = ref_278 # MOV operation
ref_14934 = ref_14616 # MOV operation
ref_14942 = ((ref_14934 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14949 = ref_14942 # MOV operation
ref_16290 = ref_278 # MOV operation
ref_16536 = ref_16290 # MOV operation
ref_16544 = (ref_16536 >> (0xB & 0x3F)) # SHR operation
ref_16551 = ref_16544 # MOV operation
ref_16760 = ref_16551 # MOV operation
ref_16772 = ref_14949 # MOV operation
ref_16774 = (ref_16772 | ref_16760) # OR operation
ref_16934 = ref_16774 # MOV operation
ref_16946 = ref_13270 # MOV operation
ref_16948 = ((ref_16934 - ref_16946) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_16956 = ref_16948 # MOV operation
ref_17128 = ref_16956 # MOV operation
ref_19996 = ref_278 # MOV operation
ref_20131 = ref_19996 # MOV operation
ref_20145 = ((ref_20131 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_20153 = ref_20145 # MOV operation
ref_20325 = ref_20153 # MOV operation
ref_23485 = ref_9701 # MOV operation
ref_23566 = ref_23485 # MOV operation
ref_23580 = ((0x20453EE3 + ref_23566) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_24927 = ref_278 # MOV operation
ref_25062 = ref_24927 # MOV operation
ref_25074 = ref_23580 # MOV operation
ref_25076 = ((ref_25062 - ref_25074) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_25084 = ref_25076 # MOV operation
ref_25256 = ref_25084 # MOV operation
ref_30600 = ref_9701 # MOV operation
ref_32791 = ref_20325 # MOV operation
ref_32980 = ref_32791 # MOV operation
ref_32992 = ref_30600 # MOV operation
ref_32994 = (ref_32992 | ref_32980) # OR operation
ref_33301 = ref_32994 # MOV operation
ref_33307 = (0x3F & ref_33301) # AND operation
ref_33650 = ref_33307 # MOV operation
ref_33658 = ((ref_33650 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_33665 = ref_33658 # MOV operation
ref_35607 = ref_9701 # MOV operation
ref_35796 = ref_35607 # MOV operation
ref_35808 = ref_33665 # MOV operation
ref_35810 = (ref_35808 | ref_35796) # OR operation
ref_35987 = ref_35810 # MOV operation
ref_39577 = ref_17128 # MOV operation
ref_41647 = ref_35987 # MOV operation
ref_41893 = ref_41647 # MOV operation
ref_41901 = (ref_41893 >> (0x1 & 0x3F)) # SHR operation
ref_41908 = ref_41901 # MOV operation
ref_42210 = ref_41908 # MOV operation
ref_42216 = (0xF & ref_42210) # AND operation
ref_42430 = ref_42216 # MOV operation
ref_42444 = (0x1 | ref_42430) # OR operation
ref_42764 = ref_42444 # MOV operation
ref_42766 = ((0x40 - ref_42764) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_42774 = ref_42766 # MOV operation
ref_42964 = ref_39577 # MOV operation
ref_42968 = ref_42774 # MOV operation
ref_42970 = (ref_42968 & 0xFFFFFFFF) # MOV operation
ref_42972 = ((ref_42964 << ((ref_42970 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_42979 = ref_42972 # MOV operation
ref_44612 = ref_17128 # MOV operation
ref_46682 = ref_35987 # MOV operation
ref_46928 = ref_46682 # MOV operation
ref_46936 = (ref_46928 >> (0x1 & 0x3F)) # SHR operation
ref_46943 = ref_46936 # MOV operation
ref_47245 = ref_46943 # MOV operation
ref_47251 = (0xF & ref_47245) # AND operation
ref_47465 = ref_47251 # MOV operation
ref_47479 = (0x1 | ref_47465) # OR operation
ref_47602 = ref_44612 # MOV operation
ref_47606 = ref_47479 # MOV operation
ref_47608 = (ref_47606 & 0xFFFFFFFF) # MOV operation
ref_47610 = (ref_47602 >> ((ref_47608 & 0xFF) & 0x3F)) # SHR operation
ref_47617 = ref_47610 # MOV operation
ref_47826 = ref_47617 # MOV operation
ref_47838 = ref_42979 # MOV operation
ref_47840 = (ref_47838 | ref_47826) # OR operation
ref_48017 = ref_47840 # MOV operation
ref_51029 = ref_25256 # MOV operation
ref_53220 = ref_48017 # MOV operation
ref_53355 = ref_53220 # MOV operation
ref_53367 = ref_51029 # MOV operation
ref_53369 = ((ref_53355 - ref_53367) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_53377 = ref_53369 # MOV operation
ref_53549 = ref_53377 # MOV operation
ref_59011 = ref_35987 # MOV operation
ref_60772 = ref_17128 # MOV operation
ref_61054 = ref_60772 # MOV operation
ref_61060 = (0xF & ref_61054) # AND operation
ref_61274 = ref_61060 # MOV operation
ref_61288 = (0x1 | ref_61274) # OR operation
ref_61608 = ref_61288 # MOV operation
ref_61610 = ((0x40 - ref_61608) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_61618 = ref_61610 # MOV operation
ref_61808 = ref_59011 # MOV operation
ref_61812 = ref_61618 # MOV operation
ref_61814 = (ref_61812 & 0xFFFFFFFF) # MOV operation
ref_61816 = ((ref_61808 << ((ref_61814 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_61823 = ref_61816 # MOV operation
ref_63456 = ref_35987 # MOV operation
ref_65217 = ref_17128 # MOV operation
ref_65499 = ref_65217 # MOV operation
ref_65505 = (0xF & ref_65499) # AND operation
ref_65719 = ref_65505 # MOV operation
ref_65733 = (0x1 | ref_65719) # OR operation
ref_65856 = ref_63456 # MOV operation
ref_65860 = ref_65733 # MOV operation
ref_65862 = (ref_65860 & 0xFFFFFFFF) # MOV operation
ref_65864 = (ref_65856 >> ((ref_65862 & 0xFF) & 0x3F)) # SHR operation
ref_65871 = ref_65864 # MOV operation
ref_66080 = ref_65871 # MOV operation
ref_66092 = ref_61823 # MOV operation
ref_66094 = (ref_66092 | ref_66080) # OR operation
ref_67880 = ref_25256 # MOV operation
ref_69493 = ref_53549 # MOV operation
ref_69682 = ref_69493 # MOV operation
ref_69694 = ref_67880 # MOV operation
ref_69696 = (ref_69694 | ref_69682) # OR operation
ref_69967 = ref_69696 # MOV operation
ref_69975 = (ref_69967 >> (0x1 & 0x3F)) # SHR operation
ref_69982 = ref_69975 # MOV operation
ref_70284 = ref_69982 # MOV operation
ref_70290 = (0x7 & ref_70284) # AND operation
ref_70504 = ref_70290 # MOV operation
ref_70518 = (0x1 | ref_70504) # OR operation
ref_70713 = ref_66094 # MOV operation
ref_70717 = ref_70518 # MOV operation
ref_70719 = (ref_70717 & 0xFFFFFFFF) # MOV operation
ref_70721 = ((ref_70713 << ((ref_70719 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_70728 = ref_70721 # MOV operation
ref_70900 = ref_70728 # MOV operation
ref_71400 = ref_70900 # MOV operation
ref_71402 = ref_71400 # MOV operation

print ref_71402 & 0xffffffffffffffff
