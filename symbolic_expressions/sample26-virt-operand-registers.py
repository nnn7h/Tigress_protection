#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_6464 = ref_278 # MOV operation
ref_6672 = ref_6464 # MOV operation
ref_6692 = (ref_6672 >> (0x5 & 0x3F)) # SHR operation
ref_6807 = ref_6692 # MOV operation
ref_6825 = (ref_6807 & 0x1376783EF7559EA) # AND operation
ref_6944 = ref_6825 # MOV operation
ref_6946 = ((ref_6944 >> 56) & 0xFF) # Byte reference - MOV operation
ref_6947 = ((ref_6944 >> 48) & 0xFF) # Byte reference - MOV operation
ref_6948 = ((ref_6944 >> 40) & 0xFF) # Byte reference - MOV operation
ref_6949 = ((ref_6944 >> 32) & 0xFF) # Byte reference - MOV operation
ref_6950 = ((ref_6944 >> 24) & 0xFF) # Byte reference - MOV operation
ref_6951 = ((ref_6944 >> 16) & 0xFF) # Byte reference - MOV operation
ref_6952 = ((ref_6944 >> 8) & 0xFF) # Byte reference - MOV operation
ref_6953 = (ref_6944 & 0xFF) # Byte reference - MOV operation
ref_8763 = ref_278 # MOV operation
ref_8873 = ref_8763 # MOV operation
ref_8891 = (ref_8873 | 0x1A5612E2) # OR operation
ref_9918 = ref_6944 # MOV operation
ref_10028 = ref_9918 # MOV operation
ref_10046 = (ref_10028 & 0x7063FB7) # AND operation
ref_10169 = ref_8891 # MOV operation
ref_10177 = ref_10046 # MOV operation
ref_10179 = ((ref_10169 + ref_10177) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10299 = ref_10179 # MOV operation
ref_10301 = ((ref_10299 >> 56) & 0xFF) # Byte reference - MOV operation
ref_10302 = ((ref_10299 >> 48) & 0xFF) # Byte reference - MOV operation
ref_10303 = ((ref_10299 >> 40) & 0xFF) # Byte reference - MOV operation
ref_10304 = ((ref_10299 >> 32) & 0xFF) # Byte reference - MOV operation
ref_10305 = ((ref_10299 >> 24) & 0xFF) # Byte reference - MOV operation
ref_10306 = ((ref_10299 >> 16) & 0xFF) # Byte reference - MOV operation
ref_10307 = ((ref_10299 >> 8) & 0xFF) # Byte reference - MOV operation
ref_10308 = (ref_10299 & 0xFF) # Byte reference - MOV operation
ref_12020 = ref_278 # MOV operation
ref_12236 = ref_12020 # MOV operation
ref_12246 = ((ref_12236 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_13764 = ref_10299 # MOV operation
ref_13972 = ref_13764 # MOV operation
ref_13992 = (ref_13972 >> (0x3 & 0x3F)) # SHR operation
ref_14107 = ref_13992 # MOV operation
ref_14125 = (ref_14107 & 0xF) # AND operation
ref_14240 = ref_14125 # MOV operation
ref_14258 = (ref_14240 | 0x1) # OR operation
ref_14389 = ref_14258 # MOV operation
ref_14391 = ((0x40 - ref_14389) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_14523 = ref_14391 # MOV operation
ref_14525 = (ref_14523 & 0xFFFFFFFF) # MOV operation
ref_14527 = (0x3162E74F >> ((ref_14525 & 0xFF) & 0x3F)) # SHR operation
ref_15750 = ref_10299 # MOV operation
ref_15958 = ref_15750 # MOV operation
ref_15978 = (ref_15958 >> (0x3 & 0x3F)) # SHR operation
ref_16093 = ref_15978 # MOV operation
ref_16111 = (ref_16093 & 0xF) # AND operation
ref_16226 = ref_16111 # MOV operation
ref_16244 = (ref_16226 | 0x1) # OR operation
ref_16375 = ref_16244 # MOV operation
ref_16377 = (ref_16375 & 0xFFFFFFFF) # MOV operation
ref_16379 = ((0x3162E74F << ((ref_16377 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_16494 = ref_16379 # MOV operation
ref_16510 = ref_14527 # MOV operation
ref_16512 = (ref_16494 | ref_16510) # OR operation
ref_16725 = ref_16512 # MOV operation
ref_16745 = (ref_16725 >> (0x4 & 0x3F)) # SHR operation
ref_16860 = ref_16745 # MOV operation
ref_16878 = (ref_16860 & 0x7) # AND operation
ref_16993 = ref_16878 # MOV operation
ref_17011 = (ref_16993 | 0x1) # OR operation
ref_17126 = ref_12246 # MOV operation
ref_17142 = ref_17011 # MOV operation
ref_17144 = (ref_17142 & 0xFFFFFFFF) # MOV operation
ref_17146 = ((ref_17126 << ((ref_17144 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_17265 = ref_17146 # MOV operation
ref_18986 = ref_278 # MOV operation
ref_19202 = ref_18986 # MOV operation
ref_19212 = ((ref_19202 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_19332 = ref_19212 # MOV operation
ref_22511 = ref_10299 # MOV operation
ref_22621 = ref_22511 # MOV operation
ref_22639 = (ref_22621 & 0xF) # AND operation
ref_22852 = ref_22639 # MOV operation
ref_22872 = ((ref_22852 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_23801 = ref_19332 # MOV operation
ref_23911 = ref_23801 # MOV operation
ref_23927 = ref_22872 # MOV operation
ref_23929 = (ref_23911 | ref_23927) # OR operation
ref_24048 = ref_23929 # MOV operation
ref_25880 = ref_24048 # MOV operation
ref_25990 = ref_25880 # MOV operation
ref_26008 = (ref_25990 & 0x1F) # AND operation
ref_26221 = ref_26008 # MOV operation
ref_26241 = ((ref_26221 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27170 = ref_17265 # MOV operation
ref_27280 = ref_27170 # MOV operation
ref_27296 = ref_26241 # MOV operation
ref_27298 = (ref_27280 | ref_27296) # OR operation
ref_27417 = ref_27298 # MOV operation
ref_29613 = ref_10299 # MOV operation
ref_29723 = ref_29613 # MOV operation
ref_29741 = (ref_29723 & 0xF) # AND operation
ref_29954 = ref_29741 # MOV operation
ref_29974 = ((ref_29954 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_30903 = ref_24048 # MOV operation
ref_31013 = ref_30903 # MOV operation
ref_31029 = ref_29974 # MOV operation
ref_31031 = (ref_31013 | ref_31029) # OR operation
ref_31150 = ref_31031 # MOV operation
ref_34693 = ref_31150 # MOV operation
ref_34803 = ref_34693 # MOV operation
ref_34821 = (ref_34803 & 0xF) # AND operation
ref_35034 = ref_34821 # MOV operation
ref_35054 = ((ref_35034 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_35983 = ref_31150 # MOV operation
ref_36093 = ref_35983 # MOV operation
ref_36109 = ref_35054 # MOV operation
ref_36111 = (ref_36093 | ref_36109) # OR operation
ref_36230 = ref_36111 # MOV operation
ref_38062 = ref_36230 # MOV operation
ref_38172 = ref_38062 # MOV operation
ref_38190 = (ref_38172 & 0x1F) # AND operation
ref_38403 = ref_38190 # MOV operation
ref_38423 = ((ref_38403 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_39352 = ref_27417 # MOV operation
ref_39462 = ref_39352 # MOV operation
ref_39478 = ref_38423 # MOV operation
ref_39480 = (ref_39462 | ref_39478) # OR operation
ref_39599 = ref_39480 # MOV operation
ref_39601 = ((ref_39599 >> 56) & 0xFF) # Byte reference - MOV operation
ref_39602 = ((ref_39599 >> 48) & 0xFF) # Byte reference - MOV operation
ref_39603 = ((ref_39599 >> 40) & 0xFF) # Byte reference - MOV operation
ref_39604 = ((ref_39599 >> 32) & 0xFF) # Byte reference - MOV operation
ref_39605 = ((ref_39599 >> 24) & 0xFF) # Byte reference - MOV operation
ref_39606 = ((ref_39599 >> 16) & 0xFF) # Byte reference - MOV operation
ref_39607 = ((ref_39599 >> 8) & 0xFF) # Byte reference - MOV operation
ref_39608 = (ref_39599 & 0xFF) # Byte reference - MOV operation
ref_41795 = ref_36230 # MOV operation
ref_41905 = ref_41795 # MOV operation
ref_41923 = (ref_41905 & 0xF) # AND operation
ref_42136 = ref_41923 # MOV operation
ref_42156 = ((ref_42136 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_43085 = ref_36230 # MOV operation
ref_43195 = ref_43085 # MOV operation
ref_43211 = ref_42156 # MOV operation
ref_43213 = (ref_43195 | ref_43211) # OR operation
ref_43332 = ref_43213 # MOV operation
ref_51574 = ref_39599 # MOV operation
ref_52498 = ref_39599 # MOV operation
ref_52616 = ref_51574 # MOV operation
ref_52624 = ref_52498 # MOV operation
ref_52626 = ((ref_52616 + ref_52624) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_52742 = ref_52626 # MOV operation
ref_52760 = (ref_52742 & 0x7) # AND operation
ref_52973 = ref_52760 # MOV operation
ref_52993 = ((ref_52973 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_53922 = ref_43332 # MOV operation
ref_54032 = ref_53922 # MOV operation
ref_54048 = ref_52993 # MOV operation
ref_54050 = (ref_54032 | ref_54048) # OR operation
ref_54169 = ref_54050 # MOV operation
ref_55895 = ((((ref_39601) << 8 | ref_39602) << 8 | ref_39603) << 8 | ref_39604) # MOV operation
ref_56005 = (ref_55895 & 0xFFFFFFFF) # MOV operation
ref_59107 = ((((ref_39605) << 8 | ref_39606) << 8 | ref_39607) << 8 | ref_39608) # MOV operation
ref_59217 = (ref_59107 & 0xFFFFFFFF) # MOV operation
ref_59219 = (((ref_59217 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_59220 = (((ref_59217 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_59221 = (((ref_59217 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_59222 = ((ref_59217 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_60939 = (ref_56005 & 0xFFFFFFFF) # MOV operation
ref_61049 = (ref_60939 & 0xFFFFFFFF) # MOV operation
ref_61051 = (((ref_61049 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_61052 = (((ref_61049 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_61053 = (((ref_61049 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_61054 = ((ref_61049 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_62653 = ref_6948 # MOVZX operation
ref_62877 = (ref_62653 & 0xFF) # MOVZX operation
ref_64477 = ref_6949 # MOVZX operation
ref_66081 = (ref_64477 & 0xFF) # MOVZX operation
ref_66083 = (ref_66081 & 0xFF) # Byte reference - MOV operation
ref_66301 = (ref_62877 & 0xFF) # MOVZX operation
ref_67905 = (ref_66301 & 0xFF) # MOVZX operation
ref_67907 = (ref_67905 & 0xFF) # Byte reference - MOV operation
ref_69505 = ref_6947 # MOVZX operation
ref_69729 = (ref_69505 & 0xFF) # MOVZX operation
ref_71329 = ref_6953 # MOVZX operation
ref_72933 = (ref_71329 & 0xFF) # MOVZX operation
ref_72935 = (ref_72933 & 0xFF) # Byte reference - MOV operation
ref_73153 = (ref_69729 & 0xFF) # MOVZX operation
ref_74757 = (ref_73153 & 0xFF) # MOVZX operation
ref_74759 = (ref_74757 & 0xFF) # Byte reference - MOV operation
ref_76475 = ((((ref_10305) << 8 | ref_10306) << 8 | ref_10307) << 8 | ref_10308) # MOV operation
ref_76585 = (ref_76475 & 0xFFFFFFFF) # MOV operation
ref_79687 = ((((ref_10301) << 8 | ref_10302) << 8 | ref_10303) << 8 | ref_10304) # MOV operation
ref_79797 = (ref_79687 & 0xFFFFFFFF) # MOV operation
ref_79799 = (((ref_79797 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_79800 = (((ref_79797 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_79801 = (((ref_79797 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_79802 = ((ref_79797 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_81519 = (ref_76585 & 0xFFFFFFFF) # MOV operation
ref_81629 = (ref_81519 & 0xFFFFFFFF) # MOV operation
ref_81631 = (((ref_81629 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_81632 = (((ref_81629 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_81633 = (((ref_81629 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_81634 = ((ref_81629 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_85020 = ((((((((ref_6946) << 8 | ref_72935) << 8 | ref_66083) << 8 | ref_67907) << 8 | ref_6950) << 8 | ref_6951) << 8 | ref_6952) << 8 | ref_74759) # MOV operation
ref_85130 = ref_85020 # MOV operation
ref_85148 = (ref_85130 & 0x3F) # AND operation
ref_85361 = ref_85148 # MOV operation
ref_85381 = ((ref_85361 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_86442 = ((((((((ref_81631) << 8 | ref_81632) << 8 | ref_81633) << 8 | ref_81634) << 8 | ref_79799) << 8 | ref_79800) << 8 | ref_79801) << 8 | ref_79802) # MOV operation
ref_86552 = ref_86442 # MOV operation
ref_86568 = ref_85381 # MOV operation
ref_86570 = (ref_86552 | ref_86568) # OR operation
ref_86689 = ref_86570 # MOV operation
ref_90029 = ref_54169 # MOV operation
ref_91247 = ref_86689 # MOV operation
ref_91455 = ref_91247 # MOV operation
ref_91475 = (ref_91455 >> (0x3 & 0x3F)) # SHR operation
ref_91590 = ref_91475 # MOV operation
ref_91608 = (ref_91590 & 0xF) # AND operation
ref_91723 = ref_91608 # MOV operation
ref_91741 = (ref_91723 | 0x1) # OR operation
ref_91872 = ref_91741 # MOV operation
ref_91874 = ((0x40 - ref_91872) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_91990 = ref_90029 # MOV operation
ref_92006 = ref_91874 # MOV operation
ref_92008 = (ref_92006 & 0xFFFFFFFF) # MOV operation
ref_92010 = ((ref_91990 << ((ref_92008 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_92939 = ref_54169 # MOV operation
ref_94059 = ref_86689 # MOV operation
ref_94267 = ref_94059 # MOV operation
ref_94287 = (ref_94267 >> (0x3 & 0x3F)) # SHR operation
ref_94402 = ref_94287 # MOV operation
ref_94420 = (ref_94402 & 0xF) # AND operation
ref_94535 = ref_94420 # MOV operation
ref_94553 = (ref_94535 | 0x1) # OR operation
ref_94668 = ref_92939 # MOV operation
ref_94684 = ref_94553 # MOV operation
ref_94686 = (ref_94684 & 0xFFFFFFFF) # MOV operation
ref_94688 = (ref_94668 >> ((ref_94686 & 0xFF) & 0x3F)) # SHR operation
ref_94803 = ref_94688 # MOV operation
ref_94819 = ref_92010 # MOV operation
ref_94821 = (ref_94803 | ref_94819) # OR operation
ref_94936 = ref_94821 # MOV operation
ref_94954 = (ref_94936 & 0xF) # AND operation
ref_95167 = ref_94954 # MOV operation
ref_95187 = ((ref_95167 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_96116 = ((((((((ref_59219) << 8 | ref_59220) << 8 | ref_59221) << 8 | ref_59222) << 8 | ref_61051) << 8 | ref_61052) << 8 | ref_61053) << 8 | ref_61054) # MOV operation
ref_96226 = ref_96116 # MOV operation
ref_96242 = ref_95187 # MOV operation
ref_96244 = (ref_96226 | ref_96242) # OR operation
ref_96363 = ref_96244 # MOV operation
ref_98093 = ref_54169 # MOV operation
ref_99017 = ref_96363 # MOV operation
ref_99127 = ref_99017 # MOV operation
ref_99143 = ref_98093 # MOV operation
ref_99145 = (ref_99127 | ref_99143) # OR operation
ref_100074 = ((((((((ref_6946) << 8 | ref_72935) << 8 | ref_66083) << 8 | ref_67907) << 8 | ref_6950) << 8 | ref_6951) << 8 | ref_6952) << 8 | ref_74759) # MOV operation
ref_101194 = ref_86689 # MOV operation
ref_101402 = ref_101194 # MOV operation
ref_101422 = (ref_101402 >> (0x3 & 0x3F)) # SHR operation
ref_101537 = ref_101422 # MOV operation
ref_101555 = (ref_101537 & 0x7) # AND operation
ref_101670 = ref_101555 # MOV operation
ref_101688 = (ref_101670 | 0x1) # OR operation
ref_101803 = ref_100074 # MOV operation
ref_101819 = ref_101688 # MOV operation
ref_101821 = (ref_101819 & 0xFFFFFFFF) # MOV operation
ref_101823 = ((ref_101803 << ((ref_101821 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_101938 = ref_101823 # MOV operation
ref_101954 = ref_99145 # MOV operation
ref_101956 = (ref_101938 | ref_101954) # OR operation
ref_102075 = ref_101956 # MOV operation
ref_102286 = ref_102075 # MOV operation
ref_102288 = ref_102286 # MOV operation

print ref_102288 & 0xffffffffffffffff
