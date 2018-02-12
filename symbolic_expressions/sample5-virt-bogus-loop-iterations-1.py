#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_273 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_274 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_275 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_276 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_277 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_278 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_279 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_280 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_78113 = ref_280 # MOVZX operation
ref_79744 = (ref_78113 & 0xFF) # MOVZX operation
ref_79746 = (ref_79744 & 0xFF) # MOVZX operation
ref_81395 = (ref_79746 & 0xFFFFFFFF) # MOV operation
ref_81397 = (((ref_81395 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_83068 = (ref_81397 & 0xFFFFFFFF) # MOV operation
ref_88111 = (ref_83068 & 0xFFFFFFFF) # MOV operation
ref_91441 = (ref_83068 & 0xFFFFFFFF) # MOV operation
ref_94763 = (ref_91441 & 0xFFFFFFFF) # MOV operation
ref_94771 = (((ref_94763 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_94778 = (ref_94771 & 0xFFFFFFFF) # MOV operation
ref_96443 = (ref_88111 & 0xFFFFFFFF) # MOV operation
ref_96447 = (ref_94778 & 0xFFFFFFFF) # MOV operation
ref_96449 = (((ref_96447 & 0xFFFFFFFF) + (ref_96443 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_98120 = (ref_96449 & 0xFFFFFFFF) # MOV operation
ref_103163 = (ref_98120 & 0xFFFFFFFF) # MOV operation
ref_106485 = (ref_103163 & 0xFFFFFFFF) # MOV operation
ref_106493 = ((ref_106485 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_106500 = (ref_106493 & 0xFFFFFFFF) # MOV operation
ref_109850 = (ref_98120 & 0xFFFFFFFF) # MOV operation
ref_111487 = (ref_109850 & 0xFFFFFFFF) # MOV operation
ref_111499 = (ref_106500 & 0xFFFFFFFF) # MOV operation
ref_111501 = ((ref_111499 & 0xFFFFFFFF) ^ (ref_111487 & 0xFFFFFFFF)) # XOR operation
ref_113171 = (ref_111501 & 0xFFFFFFFF) # MOV operation
ref_146648 = (ref_113171 & 0xFFFFFFFF) # MOV operation
ref_161631 = ref_279 # MOVZX operation
ref_163262 = (ref_161631 & 0xFF) # MOVZX operation
ref_163264 = (ref_163262 & 0xFF) # MOVZX operation
ref_164909 = (ref_146648 & 0xFFFFFFFF) # MOV operation
ref_164913 = (ref_163264 & 0xFFFFFFFF) # MOV operation
ref_164915 = (((ref_164913 & 0xFFFFFFFF) + (ref_164909 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_166586 = (ref_164915 & 0xFFFFFFFF) # MOV operation
ref_171629 = (ref_166586 & 0xFFFFFFFF) # MOV operation
ref_174959 = (ref_166586 & 0xFFFFFFFF) # MOV operation
ref_178281 = (ref_174959 & 0xFFFFFFFF) # MOV operation
ref_178289 = (((ref_178281 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_178296 = (ref_178289 & 0xFFFFFFFF) # MOV operation
ref_179961 = (ref_171629 & 0xFFFFFFFF) # MOV operation
ref_179965 = (ref_178296 & 0xFFFFFFFF) # MOV operation
ref_179967 = (((ref_179965 & 0xFFFFFFFF) + (ref_179961 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_181638 = (ref_179967 & 0xFFFFFFFF) # MOV operation
ref_186681 = (ref_181638 & 0xFFFFFFFF) # MOV operation
ref_190003 = (ref_186681 & 0xFFFFFFFF) # MOV operation
ref_190011 = ((ref_190003 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_190018 = (ref_190011 & 0xFFFFFFFF) # MOV operation
ref_193368 = (ref_181638 & 0xFFFFFFFF) # MOV operation
ref_195005 = (ref_193368 & 0xFFFFFFFF) # MOV operation
ref_195017 = (ref_190018 & 0xFFFFFFFF) # MOV operation
ref_195019 = ((ref_195017 & 0xFFFFFFFF) ^ (ref_195005 & 0xFFFFFFFF)) # XOR operation
ref_196689 = (ref_195019 & 0xFFFFFFFF) # MOV operation
ref_230166 = (ref_196689 & 0xFFFFFFFF) # MOV operation
ref_245149 = ref_278 # MOVZX operation
ref_246780 = (ref_245149 & 0xFF) # MOVZX operation
ref_246782 = (ref_246780 & 0xFF) # MOVZX operation
ref_248427 = (ref_230166 & 0xFFFFFFFF) # MOV operation
ref_248431 = (ref_246782 & 0xFFFFFFFF) # MOV operation
ref_248433 = (((ref_248431 & 0xFFFFFFFF) + (ref_248427 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_250104 = (ref_248433 & 0xFFFFFFFF) # MOV operation
ref_255147 = (ref_250104 & 0xFFFFFFFF) # MOV operation
ref_258477 = (ref_250104 & 0xFFFFFFFF) # MOV operation
ref_261799 = (ref_258477 & 0xFFFFFFFF) # MOV operation
ref_261807 = (((ref_261799 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_261814 = (ref_261807 & 0xFFFFFFFF) # MOV operation
ref_263479 = (ref_255147 & 0xFFFFFFFF) # MOV operation
ref_263483 = (ref_261814 & 0xFFFFFFFF) # MOV operation
ref_263485 = (((ref_263483 & 0xFFFFFFFF) + (ref_263479 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_265156 = (ref_263485 & 0xFFFFFFFF) # MOV operation
ref_270199 = (ref_265156 & 0xFFFFFFFF) # MOV operation
ref_273521 = (ref_270199 & 0xFFFFFFFF) # MOV operation
ref_273529 = ((ref_273521 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_273536 = (ref_273529 & 0xFFFFFFFF) # MOV operation
ref_276886 = (ref_265156 & 0xFFFFFFFF) # MOV operation
ref_278523 = (ref_276886 & 0xFFFFFFFF) # MOV operation
ref_278535 = (ref_273536 & 0xFFFFFFFF) # MOV operation
ref_278537 = ((ref_278535 & 0xFFFFFFFF) ^ (ref_278523 & 0xFFFFFFFF)) # XOR operation
ref_280207 = (ref_278537 & 0xFFFFFFFF) # MOV operation
ref_313684 = (ref_280207 & 0xFFFFFFFF) # MOV operation
ref_328667 = ref_277 # MOVZX operation
ref_330298 = (ref_328667 & 0xFF) # MOVZX operation
ref_330300 = (ref_330298 & 0xFF) # MOVZX operation
ref_331945 = (ref_313684 & 0xFFFFFFFF) # MOV operation
ref_331949 = (ref_330300 & 0xFFFFFFFF) # MOV operation
ref_331951 = (((ref_331949 & 0xFFFFFFFF) + (ref_331945 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_333622 = (ref_331951 & 0xFFFFFFFF) # MOV operation
ref_338665 = (ref_333622 & 0xFFFFFFFF) # MOV operation
ref_341995 = (ref_333622 & 0xFFFFFFFF) # MOV operation
ref_345317 = (ref_341995 & 0xFFFFFFFF) # MOV operation
ref_345325 = (((ref_345317 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_345332 = (ref_345325 & 0xFFFFFFFF) # MOV operation
ref_346997 = (ref_338665 & 0xFFFFFFFF) # MOV operation
ref_347001 = (ref_345332 & 0xFFFFFFFF) # MOV operation
ref_347003 = (((ref_347001 & 0xFFFFFFFF) + (ref_346997 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_348674 = (ref_347003 & 0xFFFFFFFF) # MOV operation
ref_353717 = (ref_348674 & 0xFFFFFFFF) # MOV operation
ref_357039 = (ref_353717 & 0xFFFFFFFF) # MOV operation
ref_357047 = ((ref_357039 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_357054 = (ref_357047 & 0xFFFFFFFF) # MOV operation
ref_360404 = (ref_348674 & 0xFFFFFFFF) # MOV operation
ref_362041 = (ref_360404 & 0xFFFFFFFF) # MOV operation
ref_362053 = (ref_357054 & 0xFFFFFFFF) # MOV operation
ref_362055 = ((ref_362053 & 0xFFFFFFFF) ^ (ref_362041 & 0xFFFFFFFF)) # XOR operation
ref_363725 = (ref_362055 & 0xFFFFFFFF) # MOV operation
ref_397202 = (ref_363725 & 0xFFFFFFFF) # MOV operation
ref_412185 = ref_276 # MOVZX operation
ref_413816 = (ref_412185 & 0xFF) # MOVZX operation
ref_413818 = (ref_413816 & 0xFF) # MOVZX operation
ref_415463 = (ref_397202 & 0xFFFFFFFF) # MOV operation
ref_415467 = (ref_413818 & 0xFFFFFFFF) # MOV operation
ref_415469 = (((ref_415467 & 0xFFFFFFFF) + (ref_415463 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_417140 = (ref_415469 & 0xFFFFFFFF) # MOV operation
ref_422183 = (ref_417140 & 0xFFFFFFFF) # MOV operation
ref_425513 = (ref_417140 & 0xFFFFFFFF) # MOV operation
ref_428835 = (ref_425513 & 0xFFFFFFFF) # MOV operation
ref_428843 = (((ref_428835 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_428850 = (ref_428843 & 0xFFFFFFFF) # MOV operation
ref_430515 = (ref_422183 & 0xFFFFFFFF) # MOV operation
ref_430519 = (ref_428850 & 0xFFFFFFFF) # MOV operation
ref_430521 = (((ref_430519 & 0xFFFFFFFF) + (ref_430515 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_432192 = (ref_430521 & 0xFFFFFFFF) # MOV operation
ref_437235 = (ref_432192 & 0xFFFFFFFF) # MOV operation
ref_440557 = (ref_437235 & 0xFFFFFFFF) # MOV operation
ref_440565 = ((ref_440557 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_440572 = (ref_440565 & 0xFFFFFFFF) # MOV operation
ref_443922 = (ref_432192 & 0xFFFFFFFF) # MOV operation
ref_445559 = (ref_443922 & 0xFFFFFFFF) # MOV operation
ref_445571 = (ref_440572 & 0xFFFFFFFF) # MOV operation
ref_445573 = ((ref_445571 & 0xFFFFFFFF) ^ (ref_445559 & 0xFFFFFFFF)) # XOR operation
ref_447243 = (ref_445573 & 0xFFFFFFFF) # MOV operation
ref_480720 = (ref_447243 & 0xFFFFFFFF) # MOV operation
ref_495703 = ref_275 # MOVZX operation
ref_497334 = (ref_495703 & 0xFF) # MOVZX operation
ref_497336 = (ref_497334 & 0xFF) # MOVZX operation
ref_498981 = (ref_480720 & 0xFFFFFFFF) # MOV operation
ref_498985 = (ref_497336 & 0xFFFFFFFF) # MOV operation
ref_498987 = (((ref_498985 & 0xFFFFFFFF) + (ref_498981 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_500658 = (ref_498987 & 0xFFFFFFFF) # MOV operation
ref_505701 = (ref_500658 & 0xFFFFFFFF) # MOV operation
ref_509031 = (ref_500658 & 0xFFFFFFFF) # MOV operation
ref_512353 = (ref_509031 & 0xFFFFFFFF) # MOV operation
ref_512361 = (((ref_512353 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_512368 = (ref_512361 & 0xFFFFFFFF) # MOV operation
ref_514033 = (ref_505701 & 0xFFFFFFFF) # MOV operation
ref_514037 = (ref_512368 & 0xFFFFFFFF) # MOV operation
ref_514039 = (((ref_514037 & 0xFFFFFFFF) + (ref_514033 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_515710 = (ref_514039 & 0xFFFFFFFF) # MOV operation
ref_520753 = (ref_515710 & 0xFFFFFFFF) # MOV operation
ref_524075 = (ref_520753 & 0xFFFFFFFF) # MOV operation
ref_524083 = ((ref_524075 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_524090 = (ref_524083 & 0xFFFFFFFF) # MOV operation
ref_527440 = (ref_515710 & 0xFFFFFFFF) # MOV operation
ref_529077 = (ref_527440 & 0xFFFFFFFF) # MOV operation
ref_529089 = (ref_524090 & 0xFFFFFFFF) # MOV operation
ref_529091 = ((ref_529089 & 0xFFFFFFFF) ^ (ref_529077 & 0xFFFFFFFF)) # XOR operation
ref_530761 = (ref_529091 & 0xFFFFFFFF) # MOV operation
ref_564238 = (ref_530761 & 0xFFFFFFFF) # MOV operation
ref_579221 = ref_274 # MOVZX operation
ref_580852 = (ref_579221 & 0xFF) # MOVZX operation
ref_580854 = (ref_580852 & 0xFF) # MOVZX operation
ref_582499 = (ref_564238 & 0xFFFFFFFF) # MOV operation
ref_582503 = (ref_580854 & 0xFFFFFFFF) # MOV operation
ref_582505 = (((ref_582503 & 0xFFFFFFFF) + (ref_582499 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_584176 = (ref_582505 & 0xFFFFFFFF) # MOV operation
ref_589219 = (ref_584176 & 0xFFFFFFFF) # MOV operation
ref_592549 = (ref_584176 & 0xFFFFFFFF) # MOV operation
ref_595871 = (ref_592549 & 0xFFFFFFFF) # MOV operation
ref_595879 = (((ref_595871 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_595886 = (ref_595879 & 0xFFFFFFFF) # MOV operation
ref_597551 = (ref_589219 & 0xFFFFFFFF) # MOV operation
ref_597555 = (ref_595886 & 0xFFFFFFFF) # MOV operation
ref_597557 = (((ref_597555 & 0xFFFFFFFF) + (ref_597551 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_599228 = (ref_597557 & 0xFFFFFFFF) # MOV operation
ref_604271 = (ref_599228 & 0xFFFFFFFF) # MOV operation
ref_607593 = (ref_604271 & 0xFFFFFFFF) # MOV operation
ref_607601 = ((ref_607593 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_607608 = (ref_607601 & 0xFFFFFFFF) # MOV operation
ref_610958 = (ref_599228 & 0xFFFFFFFF) # MOV operation
ref_612595 = (ref_610958 & 0xFFFFFFFF) # MOV operation
ref_612607 = (ref_607608 & 0xFFFFFFFF) # MOV operation
ref_612609 = ((ref_612607 & 0xFFFFFFFF) ^ (ref_612595 & 0xFFFFFFFF)) # XOR operation
ref_614279 = (ref_612609 & 0xFFFFFFFF) # MOV operation
ref_647756 = (ref_614279 & 0xFFFFFFFF) # MOV operation
ref_662739 = ref_273 # MOVZX operation
ref_664370 = (ref_662739 & 0xFF) # MOVZX operation
ref_664372 = (ref_664370 & 0xFF) # MOVZX operation
ref_666017 = (ref_647756 & 0xFFFFFFFF) # MOV operation
ref_666021 = (ref_664372 & 0xFFFFFFFF) # MOV operation
ref_666023 = (((ref_666021 & 0xFFFFFFFF) + (ref_666017 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_667694 = (ref_666023 & 0xFFFFFFFF) # MOV operation
ref_672737 = (ref_667694 & 0xFFFFFFFF) # MOV operation
ref_676067 = (ref_667694 & 0xFFFFFFFF) # MOV operation
ref_679389 = (ref_676067 & 0xFFFFFFFF) # MOV operation
ref_679397 = (((ref_679389 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_679404 = (ref_679397 & 0xFFFFFFFF) # MOV operation
ref_681069 = (ref_672737 & 0xFFFFFFFF) # MOV operation
ref_681073 = (ref_679404 & 0xFFFFFFFF) # MOV operation
ref_681075 = (((ref_681073 & 0xFFFFFFFF) + (ref_681069 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_682746 = (ref_681075 & 0xFFFFFFFF) # MOV operation
ref_687789 = (ref_682746 & 0xFFFFFFFF) # MOV operation
ref_691111 = (ref_687789 & 0xFFFFFFFF) # MOV operation
ref_691119 = ((ref_691111 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_691126 = (ref_691119 & 0xFFFFFFFF) # MOV operation
ref_694476 = (ref_682746 & 0xFFFFFFFF) # MOV operation
ref_696113 = (ref_694476 & 0xFFFFFFFF) # MOV operation
ref_696125 = (ref_691126 & 0xFFFFFFFF) # MOV operation
ref_696127 = ((ref_696125 & 0xFFFFFFFF) ^ (ref_696113 & 0xFFFFFFFF)) # XOR operation
ref_697797 = (ref_696127 & 0xFFFFFFFF) # MOV operation
ref_717811 = (ref_697797 & 0xFFFFFFFF) # MOV operation
ref_721141 = (ref_697797 & 0xFFFFFFFF) # MOV operation
ref_724463 = (ref_721141 & 0xFFFFFFFF) # MOV operation
ref_724471 = (((ref_724463 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_724478 = (ref_724471 & 0xFFFFFFFF) # MOV operation
ref_726143 = (ref_717811 & 0xFFFFFFFF) # MOV operation
ref_726147 = (ref_724478 & 0xFFFFFFFF) # MOV operation
ref_726149 = (((ref_726147 & 0xFFFFFFFF) + (ref_726143 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_727820 = (ref_726149 & 0xFFFFFFFF) # MOV operation
ref_732863 = (ref_727820 & 0xFFFFFFFF) # MOV operation
ref_736185 = (ref_732863 & 0xFFFFFFFF) # MOV operation
ref_736193 = ((ref_736185 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_736200 = (ref_736193 & 0xFFFFFFFF) # MOV operation
ref_739550 = (ref_727820 & 0xFFFFFFFF) # MOV operation
ref_741187 = (ref_739550 & 0xFFFFFFFF) # MOV operation
ref_741199 = (ref_736200 & 0xFFFFFFFF) # MOV operation
ref_741201 = ((ref_741199 & 0xFFFFFFFF) ^ (ref_741187 & 0xFFFFFFFF)) # XOR operation
ref_742871 = (ref_741201 & 0xFFFFFFFF) # MOV operation
ref_747914 = (ref_742871 & 0xFFFFFFFF) # MOV operation
ref_751244 = (ref_742871 & 0xFFFFFFFF) # MOV operation
ref_754566 = (ref_751244 & 0xFFFFFFFF) # MOV operation
ref_754574 = (((ref_754566 & 0xFFFFFFFF) << (0xF & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_754581 = (ref_754574 & 0xFFFFFFFF) # MOV operation
ref_756246 = (ref_747914 & 0xFFFFFFFF) # MOV operation
ref_756250 = (ref_754581 & 0xFFFFFFFF) # MOV operation
ref_756252 = (((ref_756250 & 0xFFFFFFFF) + (ref_756246 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_757923 = (ref_756252 & 0xFFFFFFFF) # MOV operation
ref_762922 = (ref_757923 & 0xFFFFFFFF) # MOV operation
ref_764555 = (ref_762922 & 0xFFFFFFFF) # MOV operation
ref_764579 = (ref_764555 & 0xFFFFFFFF) # MOV operation
ref_764587 = (ref_764579 & 0xFFFFFFFF) # MOV operation
ref_764589 = (ref_764587 & 0xFFFFFFFF) # MOV operation

print ref_764589 & 0xffffffffffffffff
