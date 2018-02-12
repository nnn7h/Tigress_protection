#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5406 = ref_278 # MOV operation
ref_5448 = ref_5406 # MOV operation
ref_5456 = ((ref_5448 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_5463 = ref_5456 # MOV operation
ref_5850 = ref_278 # MOV operation
ref_5892 = ref_5850 # MOV operation
ref_5900 = (ref_5892 >> (0x7 & 0x3F)) # SHR operation
ref_5907 = ref_5900 # MOV operation
ref_5939 = ref_5907 # MOV operation
ref_5951 = ref_5463 # MOV operation
ref_5953 = (ref_5951 | ref_5939) # OR operation
ref_5992 = ref_5953 # MOV operation
ref_6636 = ref_5992 # MOV operation
ref_6698 = ref_6636 # MOV operation
ref_6700 = ((ref_6698 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6734 = ref_6700 # MOV operation
ref_6736 = (ref_6734 & 0x1D5ABF66) # AND operation
ref_7170 = ref_278 # MOV operation
ref_7212 = ref_7170 # MOV operation
ref_7220 = ((ref_7212 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7227 = ref_7220 # MOV operation
ref_7614 = ref_278 # MOV operation
ref_7656 = ref_7614 # MOV operation
ref_7664 = (ref_7656 >> (0xB & 0x3F)) # SHR operation
ref_7671 = ref_7664 # MOV operation
ref_7703 = ref_7671 # MOV operation
ref_7715 = ref_7227 # MOV operation
ref_7717 = (ref_7715 | ref_7703) # OR operation
ref_7754 = ref_7717 # MOV operation
ref_7766 = ref_6736 # MOV operation
ref_7768 = ((ref_7754 - ref_7766) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7776 = ref_7768 # MOV operation
ref_7810 = ref_7776 # MOV operation
ref_8503 = ref_278 # MOV operation
ref_8535 = ref_8503 # MOV operation
ref_8549 = ((ref_8535 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_8557 = ref_8549 # MOV operation
ref_8591 = ref_8557 # MOV operation
ref_9235 = ref_5992 # MOV operation
ref_9259 = ref_9235 # MOV operation
ref_9265 = ((0x20453EE3 + ref_9259) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9700 = ref_278 # MOV operation
ref_9732 = ref_9700 # MOV operation
ref_9744 = ref_9265 # MOV operation
ref_9746 = ((ref_9732 - ref_9744) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_9754 = ref_9746 # MOV operation
ref_9788 = ref_9754 # MOV operation
ref_10952 = ref_5992 # MOV operation
ref_11422 = ref_8591 # MOV operation
ref_11454 = ref_11422 # MOV operation
ref_11466 = ref_10952 # MOV operation
ref_11468 = (ref_11466 | ref_11454) # OR operation
ref_11523 = ref_11468 # MOV operation
ref_11537 = (0x3F & ref_11523) # AND operation
ref_11592 = ref_11537 # MOV operation
ref_11606 = ((ref_11592 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_12045 = ref_5992 # MOV operation
ref_12069 = ref_12045 # MOV operation
ref_12073 = ref_11606 # MOV operation
ref_12075 = (ref_12073 | ref_12069) # OR operation
ref_12106 = ref_12075 # MOV operation
ref_12772 = ref_7810 # MOV operation
ref_13202 = ref_12106 # MOV operation
ref_13252 = ref_13202 # MOV operation
ref_13266 = (ref_13252 >> (0x1 & 0x3F)) # SHR operation
ref_13321 = ref_13266 # MOV operation
ref_13335 = (0xF & ref_13321) # AND operation
ref_13364 = ref_13335 # MOV operation
ref_13370 = (0x1 | ref_13364) # OR operation
ref_13421 = ref_13370 # MOV operation
ref_13423 = ((0x40 - ref_13421) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_13431 = ref_13423 # MOV operation
ref_13457 = ref_12772 # MOV operation
ref_13461 = ref_13431 # MOV operation
ref_13463 = (ref_13461 & 0xFFFFFFFF) # MOV operation
ref_13465 = ((ref_13457 << ((ref_13463 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13472 = ref_13465 # MOV operation
ref_13852 = ref_7810 # MOV operation
ref_14304 = ref_12106 # MOV operation
ref_14354 = ref_14304 # MOV operation
ref_14368 = (ref_14354 >> (0x1 & 0x3F)) # SHR operation
ref_14423 = ref_14368 # MOV operation
ref_14437 = (0xF & ref_14423) # AND operation
ref_14466 = ref_14437 # MOV operation
ref_14472 = (0x1 | ref_14466) # OR operation
ref_14503 = ref_13852 # MOV operation
ref_14507 = ref_14472 # MOV operation
ref_14509 = (ref_14507 & 0xFFFFFFFF) # MOV operation
ref_14511 = (ref_14503 >> ((ref_14509 & 0xFF) & 0x3F)) # SHR operation
ref_14518 = ref_14511 # MOV operation
ref_14550 = ref_14518 # MOV operation
ref_14562 = ref_13472 # MOV operation
ref_14564 = (ref_14562 | ref_14550) # OR operation
ref_14603 = ref_14564 # MOV operation
ref_15229 = ref_9788 # MOV operation
ref_15699 = ref_14603 # MOV operation
ref_15731 = ref_15699 # MOV operation
ref_15743 = ref_15229 # MOV operation
ref_15745 = ((ref_15731 - ref_15743) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15753 = ref_15745 # MOV operation
ref_15787 = ref_15753 # MOV operation
ref_17271 = ref_12106 # MOV operation
ref_17563 = ref_7810 # MOV operation
ref_17713 = ref_17563 # MOV operation
ref_17719 = (0xF & ref_17713) # AND operation
ref_17756 = ref_17719 # MOV operation
ref_17770 = (0x1 | ref_17756) # OR operation
ref_17837 = ref_17770 # MOV operation
ref_17839 = ((0x40 - ref_17837) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_17847 = ref_17839 # MOV operation
ref_17879 = ref_17271 # MOV operation
ref_17891 = ref_17847 # MOV operation
ref_17893 = ((ref_17879 << ((ref_17891 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18162 = ref_12106 # MOV operation
ref_18560 = ref_7810 # MOV operation
ref_18610 = ref_18560 # MOV operation
ref_18624 = (0xF & ref_18610) # AND operation
ref_18653 = ref_18624 # MOV operation
ref_18659 = (0x1 | ref_18653) # OR operation
ref_18690 = ref_18162 # MOV operation
ref_18694 = ref_18659 # MOV operation
ref_18696 = (ref_18694 & 0xFFFFFFFF) # MOV operation
ref_18698 = (ref_18690 >> ((ref_18696 & 0xFF) & 0x3F)) # SHR operation
ref_18705 = ref_18698 # MOV operation
ref_18737 = ref_18705 # MOV operation
ref_18749 = ref_17893 # MOV operation
ref_18751 = (ref_18749 | ref_18737) # OR operation
ref_19154 = ref_9788 # MOV operation
ref_19428 = ref_15787 # MOV operation
ref_19460 = ref_19428 # MOV operation
ref_19472 = ref_19154 # MOV operation
ref_19474 = (ref_19472 | ref_19460) # OR operation
ref_19529 = ref_19474 # MOV operation
ref_19543 = (ref_19529 >> (0x1 & 0x3F)) # SHR operation
ref_19698 = ref_19543 # MOV operation
ref_19704 = (0x7 & ref_19698) # AND operation
ref_19741 = ref_19704 # MOV operation
ref_19755 = (0x1 | ref_19741) # OR operation
ref_19792 = ref_18751 # MOV operation
ref_19804 = ref_19755 # MOV operation
ref_19806 = ((ref_19792 << ((ref_19804 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_19845 = ref_19806 # MOV operation
ref_20072 = ref_19845 # MOV operation
ref_20074 = ref_20072 # MOV operation

print ref_20074 & 0xffffffffffffffff
