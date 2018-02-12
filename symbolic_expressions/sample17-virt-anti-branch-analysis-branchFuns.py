#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_269 = SymVar_0
ref_284 = ref_269 # MOV operation
ref_13479 = ref_284 # MOV operation
ref_14661 = ref_13479 # MOV operation
ref_14669 = (ref_14661 >> (0x7 & 0x3F)) # SHR operation
ref_14676 = ref_14669 # MOV operation
ref_20246 = ref_284 # MOV operation
ref_20845 = ref_20246 # MOV operation
ref_20859 = ((ref_20845 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_21406 = ref_14676 # MOV operation
ref_21410 = ref_20859 # MOV operation
ref_21412 = (ref_21410 | ref_21406) # OR operation
ref_26236 = ref_21412 # MOV operation
ref_31654 = ref_26236 # MOV operation
ref_32238 = ref_31654 # MOV operation
ref_32240 = ((ref_32238 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_33451 = ref_32240 # MOV operation
ref_33453 = (ref_33451 & 0x1D5ABF66) # AND operation
ref_38419 = ref_284 # MOV operation
ref_39601 = ref_38419 # MOV operation
ref_39609 = (ref_39601 >> (0xB & 0x3F)) # SHR operation
ref_39616 = ref_39609 # MOV operation
ref_45186 = ref_284 # MOV operation
ref_45785 = ref_45186 # MOV operation
ref_45799 = ((ref_45785 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_46346 = ref_39616 # MOV operation
ref_46350 = ref_45799 # MOV operation
ref_46352 = (ref_46350 | ref_46346) # OR operation
ref_46940 = ref_46352 # MOV operation
ref_46952 = ref_33453 # MOV operation
ref_46954 = ((ref_46940 - ref_46952) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_46962 = ref_46954 # MOV operation
ref_51732 = ref_46962 # MOV operation
ref_57302 = ref_284 # MOV operation
ref_57864 = ref_57302 # MOV operation
ref_57878 = ((ref_57864 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_57886 = ref_57878 # MOV operation
ref_62656 = ref_57886 # MOV operation
ref_67461 = ref_26236 # MOV operation
ref_68654 = ref_67461 # MOV operation
ref_68660 = ((0x20453EE3 + ref_68654) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_73658 = ref_284 # MOV operation
ref_74220 = ref_73658 # MOV operation
ref_74232 = ref_68660 # MOV operation
ref_74234 = ((ref_74220 - ref_74232) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_74242 = ref_74234 # MOV operation
ref_79012 = ref_74242 # MOV operation
ref_90099 = ref_26236 # MOV operation
ref_97992 = ref_62656 # MOV operation
ref_103434 = ref_26236 # MOV operation
ref_103991 = ref_97992 # MOV operation
ref_103995 = ref_103434 # MOV operation
ref_103997 = (ref_103995 | ref_103991) # OR operation
ref_104583 = ref_103997 # MOV operation
ref_104597 = (0x3F & ref_104583) # AND operation
ref_105190 = ref_104597 # MOV operation
ref_105204 = ((ref_105190 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_105751 = ref_90099 # MOV operation
ref_105755 = ref_105204 # MOV operation
ref_105757 = (ref_105755 | ref_105751) # OR operation
ref_111203 = ref_105757 # MOV operation
ref_116008 = ref_51732 # MOV operation
ref_122063 = ref_111203 # MOV operation
ref_123245 = ref_122063 # MOV operation
ref_123253 = (ref_123245 >> (0x1 & 0x3F)) # SHR operation
ref_123260 = ref_123253 # MOV operation
ref_123805 = ref_123260 # MOV operation
ref_123819 = (0xF & ref_123805) # AND operation
ref_124983 = ref_123819 # MOV operation
ref_124989 = (0x1 | ref_124983) # OR operation
ref_125584 = ref_116008 # MOV operation
ref_125588 = ref_124989 # MOV operation
ref_125590 = (ref_125588 & 0xFFFFFFFF) # MOV operation
ref_125592 = (ref_125584 >> ((ref_125590 & 0xFF) & 0x3F)) # SHR operation
ref_125599 = ref_125592 # MOV operation
ref_131639 = ref_111203 # MOV operation
ref_132821 = ref_131639 # MOV operation
ref_132829 = (ref_132821 >> (0x1 & 0x3F)) # SHR operation
ref_132836 = ref_132829 # MOV operation
ref_133381 = ref_132836 # MOV operation
ref_133395 = (0xF & ref_133381) # AND operation
ref_134559 = ref_133395 # MOV operation
ref_134565 = (0x1 | ref_134559) # OR operation
ref_135778 = ref_134565 # MOV operation
ref_135780 = ((0x40 - ref_135778) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_135788 = ref_135780 # MOV operation
ref_140580 = ref_51732 # MOV operation
ref_141179 = ref_140580 # MOV operation
ref_141191 = ref_135788 # MOV operation
ref_141193 = ((ref_141179 << ((ref_141191 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_141740 = ref_125599 # MOV operation
ref_141744 = ref_141193 # MOV operation
ref_141746 = (ref_141744 | ref_141740) # OR operation
ref_148417 = ref_141746 # MOV operation
ref_153222 = ref_79012 # MOV operation
ref_159889 = ref_148417 # MOV operation
ref_160451 = ref_159889 # MOV operation
ref_160463 = ref_153222 # MOV operation
ref_160465 = ((ref_160451 - ref_160463) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_160473 = ref_160465 # MOV operation
ref_165243 = ref_160473 # MOV operation
ref_179230 = ref_165243 # MOV operation
ref_184050 = ref_79012 # MOV operation
ref_184607 = ref_179230 # MOV operation
ref_184611 = ref_184050 # MOV operation
ref_184613 = (ref_184611 | ref_184607) # OR operation
ref_185821 = ref_184613 # MOV operation
ref_185829 = (ref_185821 >> (0x1 & 0x3F)) # SHR operation
ref_185836 = ref_185829 # MOV operation
ref_186381 = ref_185836 # MOV operation
ref_186395 = (0x7 & ref_186381) # AND operation
ref_187559 = ref_186395 # MOV operation
ref_187565 = (0x1 | ref_187559) # OR operation
ref_192411 = ref_111203 # MOV operation
ref_197844 = ref_51732 # MOV operation
ref_198404 = ref_197844 # MOV operation
ref_198418 = (0xF & ref_198404) # AND operation
ref_199582 = ref_198418 # MOV operation
ref_199588 = (0x1 | ref_199582) # OR operation
ref_200183 = ref_192411 # MOV operation
ref_200187 = ref_199588 # MOV operation
ref_200189 = (ref_200187 & 0xFFFFFFFF) # MOV operation
ref_200191 = (ref_200183 >> ((ref_200189 & 0xFF) & 0x3F)) # SHR operation
ref_200198 = ref_200191 # MOV operation
ref_205616 = ref_51732 # MOV operation
ref_206176 = ref_205616 # MOV operation
ref_206190 = (0xF & ref_206176) # AND operation
ref_207354 = ref_206190 # MOV operation
ref_207360 = (0x1 | ref_207354) # OR operation
ref_208573 = ref_207360 # MOV operation
ref_208575 = ((0x40 - ref_208573) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_208583 = ref_208575 # MOV operation
ref_213375 = ref_111203 # MOV operation
ref_213974 = ref_213375 # MOV operation
ref_213986 = ref_208583 # MOV operation
ref_213988 = ((ref_213974 << ((ref_213986 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_214535 = ref_200198 # MOV operation
ref_214539 = ref_213988 # MOV operation
ref_214541 = (ref_214539 | ref_214535) # OR operation
ref_215166 = ref_214541 # MOV operation
ref_215178 = ref_187565 # MOV operation
ref_215180 = ((ref_215166 << ((ref_215178 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_220089 = ref_215180 # MOV operation
ref_221261 = ref_220089 # MOV operation
ref_221263 = ref_221261 # MOV operation

print ref_221263 & 0xffffffffffffffff
