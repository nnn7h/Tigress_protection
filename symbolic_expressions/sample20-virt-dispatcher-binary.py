#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_15278 = ref_278 # MOV operation
ref_16736 = ref_15278 # MOV operation
ref_16742 = (0x1F02C962 | ref_16736) # OR operation
ref_18301 = ref_16742 # MOV operation
ref_18307 = (0x1F8797B2 & ref_18301) # AND operation
ref_19121 = ref_18307 # MOV operation
ref_29041 = ref_278 # MOV operation
ref_34221 = ref_19121 # MOV operation
ref_34972 = ref_29041 # MOV operation
ref_34976 = ref_34221 # MOV operation
ref_34978 = (ref_34976 & ref_34972) # AND operation
ref_35792 = ref_34978 # MOV operation
ref_45712 = ref_278 # MOV operation
ref_47030 = ref_45712 # MOV operation
ref_47036 = (((sx(0x40, 0x66AF1DF) * sx(0x40, ref_47030)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_53021 = ref_35792 # MOV operation
ref_53618 = ref_53021 # MOV operation
ref_53632 = (ref_53618 >> (0x7 & 0x3F)) # SHR operation
ref_59620 = ref_35792 # MOV operation
ref_60325 = ref_59620 # MOV operation
ref_60339 = ((ref_60325 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_61039 = ref_53632 # MOV operation
ref_61043 = ref_60339 # MOV operation
ref_61045 = (ref_61043 | ref_61039) # OR operation
ref_61821 = ref_47036 # MOV operation
ref_61825 = ref_61045 # MOV operation
ref_61827 = ((ref_61825 + ref_61821) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_62642 = ref_61827 # MOV operation
ref_119012 = ref_62642 # MOV operation
ref_126113 = ref_62642 # MOV operation
ref_126864 = ref_119012 # MOV operation
ref_126868 = ref_126113 # MOV operation
ref_126870 = ((ref_126868 + ref_126864) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_127685 = ref_126870 # MOV operation
ref_141164 = ref_62642 # MOV operation
ref_147482 = ref_35792 # MOV operation
ref_149016 = ref_147482 # MOV operation
ref_149022 = (0x7 & ref_149016) # AND operation
ref_149752 = ref_149022 # MOV operation
ref_149766 = ((ref_149752 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_150466 = ref_141164 # MOV operation
ref_150470 = ref_149766 # MOV operation
ref_150472 = (ref_150470 | ref_150466) # OR operation
ref_151286 = ref_150472 # MOV operation
ref_151288 = ((ref_151286 >> 56) & 0xFF) # Byte reference - MOV operation
ref_151289 = ((ref_151286 >> 48) & 0xFF) # Byte reference - MOV operation
ref_151290 = ((ref_151286 >> 40) & 0xFF) # Byte reference - MOV operation
ref_151291 = ((ref_151286 >> 32) & 0xFF) # Byte reference - MOV operation
ref_151292 = ((ref_151286 >> 24) & 0xFF) # Byte reference - MOV operation
ref_151293 = ((ref_151286 >> 16) & 0xFF) # Byte reference - MOV operation
ref_151294 = ((ref_151286 >> 8) & 0xFF) # Byte reference - MOV operation
ref_151295 = (ref_151286 & 0xFF) # Byte reference - MOV operation
ref_162178 = ref_151288 # MOVZX operation
ref_162883 = (ref_162178 & 0xFF) # MOVZX operation
ref_183614 = ref_151295 # MOVZX operation
ref_184319 = (ref_183614 & 0xFF) # MOVZX operation
ref_184321 = (ref_184319 & 0xFF) # Byte reference - MOV operation
ref_195203 = (ref_162883 & 0xFF) # MOVZX operation
ref_195908 = (ref_195203 & 0xFF) # MOVZX operation
ref_195910 = (ref_195908 & 0xFF) # Byte reference - MOV operation
ref_205537 = ref_19121 # MOV operation
ref_213421 = ((((((((ref_184321) << 8 | ref_151289) << 8 | ref_151290) << 8 | ref_151291) << 8 | ref_151292) << 8 | ref_151293) << 8 | ref_151294) << 8 | ref_195910) # MOV operation
ref_218956 = ref_35792 # MOV operation
ref_219707 = ref_213421 # MOV operation
ref_219711 = ref_218956 # MOV operation
ref_219713 = (ref_219711 & ref_219707) # AND operation
ref_221272 = ref_219713 # MOV operation
ref_221278 = (0x1F & ref_221272) # AND operation
ref_222008 = ref_221278 # MOV operation
ref_222022 = ((ref_222008 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_222722 = ref_205537 # MOV operation
ref_222726 = ref_222022 # MOV operation
ref_222728 = (ref_222726 | ref_222722) # OR operation
ref_223542 = ref_222728 # MOV operation
ref_242955 = ref_127685 # MOV operation
ref_250056 = ref_127685 # MOV operation
ref_250807 = ref_242955 # MOV operation
ref_250811 = ref_250056 # MOV operation
ref_250813 = ((ref_250811 + ref_250807) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_251628 = ref_250813 # MOV operation
ref_265107 = ref_251628 # MOV operation
ref_271425 = ((((((((ref_184321) << 8 | ref_151289) << 8 | ref_151290) << 8 | ref_151291) << 8 | ref_151292) << 8 | ref_151293) << 8 | ref_151294) << 8 | ref_195910) # MOV operation
ref_272959 = ref_271425 # MOV operation
ref_272965 = (0x7 & ref_272959) # AND operation
ref_273695 = ref_272965 # MOV operation
ref_273709 = ((ref_273695 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_274409 = ref_265107 # MOV operation
ref_274413 = ref_273709 # MOV operation
ref_274415 = (ref_274413 | ref_274409) # OR operation
ref_275229 = ref_274415 # MOV operation
ref_275231 = ((ref_275229 >> 56) & 0xFF) # Byte reference - MOV operation
ref_275232 = ((ref_275229 >> 48) & 0xFF) # Byte reference - MOV operation
ref_275233 = ((ref_275229 >> 40) & 0xFF) # Byte reference - MOV operation
ref_275234 = ((ref_275229 >> 32) & 0xFF) # Byte reference - MOV operation
ref_275235 = ((ref_275229 >> 24) & 0xFF) # Byte reference - MOV operation
ref_275236 = ((ref_275229 >> 16) & 0xFF) # Byte reference - MOV operation
ref_275237 = ((ref_275229 >> 8) & 0xFF) # Byte reference - MOV operation
ref_275238 = (ref_275229 & 0xFF) # Byte reference - MOV operation
ref_286121 = ref_275231 # MOVZX operation
ref_286826 = (ref_286121 & 0xFF) # MOVZX operation
ref_307557 = ref_275238 # MOVZX operation
ref_308262 = (ref_307557 & 0xFF) # MOVZX operation
ref_308264 = (ref_308262 & 0xFF) # Byte reference - MOV operation
ref_319146 = (ref_286826 & 0xFF) # MOVZX operation
ref_319851 = (ref_319146 & 0xFF) # MOVZX operation
ref_319853 = (ref_319851 & 0xFF) # Byte reference - MOV operation
ref_329480 = ref_223542 # MOV operation
ref_337364 = ((((((((ref_308264) << 8 | ref_275232) << 8 | ref_275233) << 8 | ref_275234) << 8 | ref_275235) << 8 | ref_275236) << 8 | ref_275237) << 8 | ref_319853) # MOV operation
ref_342899 = ((((((((ref_184321) << 8 | ref_151289) << 8 | ref_151290) << 8 | ref_151291) << 8 | ref_151292) << 8 | ref_151293) << 8 | ref_151294) << 8 | ref_195910) # MOV operation
ref_343650 = ref_337364 # MOV operation
ref_343654 = ref_342899 # MOV operation
ref_343656 = (ref_343654 & ref_343650) # AND operation
ref_345215 = ref_343656 # MOV operation
ref_345221 = (0x1F & ref_345215) # AND operation
ref_345951 = ref_345221 # MOV operation
ref_345965 = ((ref_345951 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_346665 = ref_329480 # MOV operation
ref_346669 = ref_345965 # MOV operation
ref_346671 = (ref_346669 | ref_346665) # OR operation
ref_347485 = ref_346671 # MOV operation
ref_366472 = ((((((((ref_184321) << 8 | ref_151289) << 8 | ref_151290) << 8 | ref_151291) << 8 | ref_151292) << 8 | ref_151293) << 8 | ref_151294) << 8 | ref_195910) # MOV operation
ref_371652 = ((((((((ref_308264) << 8 | ref_275232) << 8 | ref_275233) << 8 | ref_275234) << 8 | ref_275235) << 8 | ref_275236) << 8 | ref_275237) << 8 | ref_319853) # MOV operation
ref_372327 = ref_366472 # MOV operation
ref_372331 = ref_371652 # MOV operation
ref_372333 = (ref_372331 | ref_372327) # OR operation
ref_373892 = ref_372333 # MOV operation
ref_373898 = (0xF & ref_373892) # AND operation
ref_375381 = ref_373898 # MOV operation
ref_375387 = (0x1 | ref_375381) # OR operation
ref_381375 = ref_35792 # MOV operation
ref_381972 = ref_381375 # MOV operation
ref_381986 = (ref_381972 >> (0x1 & 0x3F)) # SHR operation
ref_383545 = ref_381986 # MOV operation
ref_383551 = (0xF & ref_383545) # AND operation
ref_385034 = ref_383551 # MOV operation
ref_385040 = (0x1 | ref_385034) # OR operation
ref_390245 = ref_347485 # MOV operation
ref_390842 = ref_390245 # MOV operation
ref_390854 = ref_385040 # MOV operation
ref_390856 = (ref_390842 >> ((ref_390854 & 0xFF) & 0x3F)) # SHR operation
ref_396844 = ref_35792 # MOV operation
ref_397441 = ref_396844 # MOV operation
ref_397455 = (ref_397441 >> (0x1 & 0x3F)) # SHR operation
ref_399014 = ref_397455 # MOV operation
ref_399020 = (0xF & ref_399014) # AND operation
ref_400503 = ref_399020 # MOV operation
ref_400509 = (0x1 | ref_400503) # OR operation
ref_401818 = ref_400509 # MOV operation
ref_401820 = ((0x40 - ref_401818) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_401828 = ref_401820 # MOV operation
ref_407028 = ref_347485 # MOV operation
ref_407733 = ref_407028 # MOV operation
ref_407745 = ref_401828 # MOV operation
ref_407747 = ((ref_407733 << ((ref_407745 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_408447 = ref_390856 # MOV operation
ref_408451 = ref_407747 # MOV operation
ref_408453 = (ref_408451 | ref_408447) # OR operation
ref_409183 = ref_408453 # MOV operation
ref_409195 = ref_375387 # MOV operation
ref_409197 = ((ref_409183 << ((ref_409195 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_414402 = ((((((((ref_184321) << 8 | ref_151289) << 8 | ref_151290) << 8 | ref_151291) << 8 | ref_151292) << 8 | ref_151293) << 8 | ref_151294) << 8 | ref_195910) # MOV operation
ref_419582 = ((((((((ref_308264) << 8 | ref_275232) << 8 | ref_275233) << 8 | ref_275234) << 8 | ref_275235) << 8 | ref_275236) << 8 | ref_275237) << 8 | ref_319853) # MOV operation
ref_420257 = ref_414402 # MOV operation
ref_420261 = ref_419582 # MOV operation
ref_420263 = (ref_420261 | ref_420257) # OR operation
ref_421822 = ref_420263 # MOV operation
ref_421828 = (0xF & ref_421822) # AND operation
ref_423311 = ref_421828 # MOV operation
ref_423317 = (0x1 | ref_423311) # OR operation
ref_424626 = ref_423317 # MOV operation
ref_424628 = ((0x40 - ref_424626) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_424636 = ref_424628 # MOV operation
ref_430619 = ref_35792 # MOV operation
ref_431216 = ref_430619 # MOV operation
ref_431230 = (ref_431216 >> (0x1 & 0x3F)) # SHR operation
ref_432789 = ref_431230 # MOV operation
ref_432795 = (0xF & ref_432789) # AND operation
ref_434278 = ref_432795 # MOV operation
ref_434284 = (0x1 | ref_434278) # OR operation
ref_439489 = ref_347485 # MOV operation
ref_440086 = ref_439489 # MOV operation
ref_440098 = ref_434284 # MOV operation
ref_440100 = (ref_440086 >> ((ref_440098 & 0xFF) & 0x3F)) # SHR operation
ref_446088 = ref_35792 # MOV operation
ref_446685 = ref_446088 # MOV operation
ref_446699 = (ref_446685 >> (0x1 & 0x3F)) # SHR operation
ref_448258 = ref_446699 # MOV operation
ref_448264 = (0xF & ref_448258) # AND operation
ref_449747 = ref_448264 # MOV operation
ref_449753 = (0x1 | ref_449747) # OR operation
ref_451062 = ref_449753 # MOV operation
ref_451064 = ((0x40 - ref_451062) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_451072 = ref_451064 # MOV operation
ref_456272 = ref_347485 # MOV operation
ref_456977 = ref_456272 # MOV operation
ref_456989 = ref_451072 # MOV operation
ref_456991 = ((ref_456977 << ((ref_456989 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_457691 = ref_440100 # MOV operation
ref_457695 = ref_456991 # MOV operation
ref_457697 = (ref_457695 | ref_457691) # OR operation
ref_458319 = ref_457697 # MOV operation
ref_458331 = ref_424636 # MOV operation
ref_458333 = (ref_458319 >> ((ref_458331 & 0xFF) & 0x3F)) # SHR operation
ref_459033 = ref_409197 # MOV operation
ref_459037 = ref_458333 # MOV operation
ref_459039 = (ref_459037 | ref_459033) # OR operation
ref_459853 = ref_459039 # MOV operation
ref_460960 = ref_459853 # MOV operation
ref_460962 = ref_460960 # MOV operation

print ref_460962 & 0xffffffffffffffff
