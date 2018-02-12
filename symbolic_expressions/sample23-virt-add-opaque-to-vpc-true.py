#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_7132 = ref_278 # MOV operation
ref_7417 = ref_7132 # MOV operation
ref_7423 = ((0x3F22161B + ref_7417) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7621 = ref_7423 # MOV operation
ref_10645 = ref_7621 # MOV operation
ref_10775 = ref_10645 # MOV operation
ref_10777 = (((sx(0x40, ref_10775) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10929 = ref_10777 # MOV operation
ref_10931 = (((sx(0x40, ref_10929) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11259 = ref_10931 # MOV operation
ref_11267 = (ref_11259 >> (0x1 & 0x3F)) # SHR operation
ref_11274 = ref_11267 # MOV operation
ref_11459 = ref_11274 # MOV operation
ref_11473 = (0xF & ref_11459) # AND operation
ref_11806 = ref_11473 # MOV operation
ref_11812 = (0x1 | ref_11806) # OR operation
ref_13256 = ref_278 # MOV operation
ref_13398 = ref_13256 # MOV operation
ref_13412 = ((ref_13398 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14701 = ref_278 # MOV operation
ref_15007 = ref_14701 # MOV operation
ref_15015 = (ref_15007 >> (0x39 & 0x3F)) # SHR operation
ref_15022 = ref_15015 # MOV operation
ref_15195 = ref_13412 # MOV operation
ref_15199 = ref_15022 # MOV operation
ref_15201 = (ref_15199 | ref_15195) # OR operation
ref_15368 = ref_15201 # MOV operation
ref_15380 = ref_11812 # MOV operation
ref_15382 = ((ref_15368 << ((ref_15380 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_16826 = ref_278 # MOV operation
ref_16968 = ref_16826 # MOV operation
ref_16982 = ((ref_16968 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18271 = ref_278 # MOV operation
ref_18577 = ref_18271 # MOV operation
ref_18585 = (ref_18577 >> (0x39 & 0x3F)) # SHR operation
ref_18592 = ref_18585 # MOV operation
ref_18765 = ref_16982 # MOV operation
ref_18769 = ref_18592 # MOV operation
ref_18771 = (ref_18769 | ref_18765) # OR operation
ref_20597 = ref_7621 # MOV operation
ref_20727 = ref_20597 # MOV operation
ref_20729 = (((sx(0x40, ref_20727) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_20881 = ref_20729 # MOV operation
ref_20883 = (((sx(0x40, ref_20881) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_21211 = ref_20883 # MOV operation
ref_21219 = (ref_21211 >> (0x1 & 0x3F)) # SHR operation
ref_21226 = ref_21219 # MOV operation
ref_21411 = ref_21226 # MOV operation
ref_21425 = (0xF & ref_21411) # AND operation
ref_21758 = ref_21425 # MOV operation
ref_21764 = (0x1 | ref_21758) # OR operation
ref_22117 = ref_21764 # MOV operation
ref_22119 = ((0x40 - ref_22117) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_22127 = ref_22119 # MOV operation
ref_22298 = ref_18771 # MOV operation
ref_22302 = ref_22127 # MOV operation
ref_22304 = (ref_22302 & 0xFFFFFFFF) # MOV operation
ref_22306 = (ref_22298 >> ((ref_22304 & 0xFF) & 0x3F)) # SHR operation
ref_22313 = ref_22306 # MOV operation
ref_22486 = ref_15382 # MOV operation
ref_22490 = ref_22313 # MOV operation
ref_22492 = (ref_22490 | ref_22486) # OR operation
ref_22689 = ref_22492 # MOV operation
ref_25176 = ref_278 # MOV operation
ref_26512 = ref_22689 # MOV operation
ref_26797 = ref_26512 # MOV operation
ref_26803 = ((0xAD6EED + ref_26797) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_26959 = ref_25176 # MOV operation
ref_26963 = ref_26803 # MOV operation
ref_26965 = ((ref_26963 + ref_26959) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_27163 = ref_26965 # MOV operation
ref_29650 = ref_278 # MOV operation
ref_30986 = ref_7621 # MOV operation
ref_31139 = ref_29650 # MOV operation
ref_31143 = ref_30986 # MOV operation
ref_31145 = (ref_31143 | ref_31139) # OR operation
ref_32506 = ref_22689 # MOV operation
ref_32791 = ref_32506 # MOV operation
ref_32797 = ((0x2B6B05ED + ref_32791) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_34159 = ref_27163 # MOV operation
ref_34324 = ref_34159 # MOV operation
ref_34336 = ref_32797 # MOV operation
ref_34338 = (ref_34336 & ref_34324) # AND operation
ref_34493 = ref_31145 # MOV operation
ref_34497 = ref_34338 # MOV operation
ref_34499 = ((ref_34497 + ref_34493) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_34697 = ref_34499 # MOV operation
ref_37256 = ref_34697 # MOV operation
ref_38902 = ref_27163 # MOV operation
ref_39067 = ref_38902 # MOV operation
ref_39081 = (0x3F & ref_39067) # AND operation
ref_39248 = ref_39081 # MOV operation
ref_39262 = ((ref_39248 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_39440 = ref_37256 # MOV operation
ref_39444 = ref_39262 # MOV operation
ref_39446 = (ref_39444 | ref_39440) # OR operation
ref_39643 = ref_39446 # MOV operation
ref_42294 = ref_22689 # MOV operation
ref_42600 = ref_42294 # MOV operation
ref_42608 = (ref_42600 >> (0x4 & 0x3F)) # SHR operation
ref_42615 = ref_42608 # MOV operation
ref_42800 = ref_42615 # MOV operation
ref_42814 = (0xF & ref_42800) # AND operation
ref_43147 = ref_42814 # MOV operation
ref_43153 = (0x1 | ref_43147) # OR operation
ref_44514 = ref_7621 # MOV operation
ref_44656 = ref_44514 # MOV operation
ref_44668 = ref_43153 # MOV operation
ref_44670 = ((ref_44656 << ((ref_44668 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_46031 = ref_7621 # MOV operation
ref_47522 = ref_22689 # MOV operation
ref_47828 = ref_47522 # MOV operation
ref_47836 = (ref_47828 >> (0x4 & 0x3F)) # SHR operation
ref_47843 = ref_47836 # MOV operation
ref_48028 = ref_47843 # MOV operation
ref_48042 = (0xF & ref_48028) # AND operation
ref_48375 = ref_48042 # MOV operation
ref_48381 = (0x1 | ref_48375) # OR operation
ref_48734 = ref_48381 # MOV operation
ref_48736 = ((0x40 - ref_48734) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_48744 = ref_48736 # MOV operation
ref_48915 = ref_46031 # MOV operation
ref_48919 = ref_48744 # MOV operation
ref_48921 = (ref_48919 & 0xFFFFFFFF) # MOV operation
ref_48923 = (ref_48915 >> ((ref_48921 & 0xFF) & 0x3F)) # SHR operation
ref_48930 = ref_48923 # MOV operation
ref_49103 = ref_44670 # MOV operation
ref_49107 = ref_48930 # MOV operation
ref_49109 = (ref_49107 | ref_49103) # OR operation
ref_50470 = ref_27163 # MOV operation
ref_51806 = ref_39643 # MOV operation
ref_51936 = ref_50470 # MOV operation
ref_51940 = ref_51806 # MOV operation
ref_51942 = ((ref_51940 + ref_51936) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_52094 = ref_49109 # MOV operation
ref_52098 = ref_51942 # MOV operation
ref_52100 = (((sx(0x40, ref_52098) * sx(0x40, ref_52094)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_52294 = ref_52100 # MOV operation
ref_52593 = ref_52294 # MOV operation
ref_52595 = ref_52593 # MOV operation

print ref_52595 & 0xffffffffffffffff
