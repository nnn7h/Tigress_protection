#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_264 = SymVar_0
ref_279 = ref_264 # MOV operation
ref_18329 = ref_279 # MOV operation
ref_18685 = ref_18329 # MOV operation
ref_18693 = (ref_18685 >> (0x5 & 0x3F)) # SHR operation
ref_18700 = ref_18693 # MOV operation
ref_20250 = ref_18700 # MOV operation
ref_21792 = ref_20250 # MOV operation
ref_22148 = ref_21792 # MOV operation
ref_22154 = (0xB4088A290E23905 ^ ref_22148) # XOR operation
ref_23679 = ref_279 # MOV operation
ref_24035 = ref_23679 # MOV operation
ref_24041 = ((ref_24035 - 0x10695A81) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_24049 = ref_24041 # MOV operation
ref_24223 = ref_24049 # MOV operation
ref_24235 = ref_22154 # MOV operation
ref_24237 = ((ref_24235 + ref_24223) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_25793 = ref_24237 # MOV operation
ref_27335 = ref_25793 # MOV operation
ref_28857 = ref_20250 # MOV operation
ref_29011 = ref_28857 # MOV operation
ref_29023 = ref_27335 # MOV operation
ref_29025 = ((ref_29023 + ref_29011) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_30551 = ref_279 # MOV operation
ref_30705 = ref_30551 # MOV operation
ref_30717 = ref_29025 # MOV operation
ref_30719 = ((ref_30717 + ref_30705) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_32275 = ref_30719 # MOV operation
ref_33795 = ref_279 # MOV operation
ref_35511 = ref_20250 # MOV operation
ref_35677 = ref_35511 # MOV operation
ref_35679 = (((sx(0x40, ref_35677) * sx(0x40, 0x3C8E8C76)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_36057 = ref_35679 # MOV operation
ref_36063 = (0x7 & ref_36057) # AND operation
ref_36444 = ref_36063 # MOV operation
ref_36450 = (0x1 | ref_36444) # OR operation
ref_36637 = ref_33795 # MOV operation
ref_36641 = ref_36450 # MOV operation
ref_36643 = (ref_36641 & 0xFFFFFFFF) # MOV operation
ref_36645 = (ref_36637 >> ((ref_36643 & 0xFF) & 0x3F)) # SHR operation
ref_36652 = ref_36645 # MOV operation
ref_38202 = ref_36652 # MOV operation
ref_39744 = ref_20250 # MOV operation
ref_41266 = ref_20250 # MOV operation
ref_42788 = ref_32275 # MOV operation
ref_42950 = ref_41266 # MOV operation
ref_42954 = ref_42788 # MOV operation
ref_42956 = (((sx(0x40, ref_42954) * sx(0x40, ref_42950)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_43334 = ref_42956 # MOV operation
ref_43340 = (0x7 & ref_43334) # AND operation
ref_43721 = ref_43340 # MOV operation
ref_43729 = ((ref_43721 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_43736 = ref_43729 # MOV operation
ref_43918 = ref_39744 # MOV operation
ref_43922 = ref_43736 # MOV operation
ref_43924 = (ref_43922 | ref_43918) # OR operation
ref_45479 = ref_43924 # MOV operation
ref_47021 = ref_25793 # MOV operation
ref_48543 = ref_38202 # MOV operation
ref_50065 = ref_25793 # MOV operation
ref_50421 = ref_50065 # MOV operation
ref_50429 = (ref_50421 >> (0x4 & 0x3F)) # SHR operation
ref_50436 = ref_50429 # MOV operation
ref_50812 = ref_50436 # MOV operation
ref_50818 = (0xF & ref_50812) # AND operation
ref_51199 = ref_50818 # MOV operation
ref_51205 = (0x1 | ref_51199) # OR operation
ref_51392 = ref_48543 # MOV operation
ref_51396 = ref_51205 # MOV operation
ref_51398 = (ref_51396 & 0xFFFFFFFF) # MOV operation
ref_51400 = ((ref_51392 << ((ref_51398 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_51407 = ref_51400 # MOV operation
ref_52949 = ref_38202 # MOV operation
ref_54665 = ref_25793 # MOV operation
ref_55021 = ref_54665 # MOV operation
ref_55029 = (ref_55021 >> (0x4 & 0x3F)) # SHR operation
ref_55036 = ref_55029 # MOV operation
ref_55412 = ref_55036 # MOV operation
ref_55418 = (0xF & ref_55412) # AND operation
ref_55799 = ref_55418 # MOV operation
ref_55805 = (0x1 | ref_55799) # OR operation
ref_55996 = ref_55805 # MOV operation
ref_55998 = ((0x40 - ref_55996) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_56006 = ref_55998 # MOV operation
ref_56188 = ref_52949 # MOV operation
ref_56192 = ref_56006 # MOV operation
ref_56194 = (ref_56192 & 0xFFFFFFFF) # MOV operation
ref_56196 = (ref_56188 >> ((ref_56194 & 0xFF) & 0x3F)) # SHR operation
ref_56203 = ref_56196 # MOV operation
ref_56385 = ref_51407 # MOV operation
ref_56389 = ref_56203 # MOV operation
ref_56391 = (ref_56389 | ref_56385) # OR operation
ref_56772 = ref_56391 # MOV operation
ref_56778 = (0xF & ref_56772) # AND operation
ref_57159 = ref_56778 # MOV operation
ref_57167 = ((ref_57159 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_57174 = ref_57167 # MOV operation
ref_57356 = ref_47021 # MOV operation
ref_57360 = ref_57174 # MOV operation
ref_57362 = (ref_57360 | ref_57356) # OR operation
ref_58917 = ref_57362 # MOV operation
ref_60621 = ref_32275 # MOV operation
ref_62143 = ref_38202 # MOV operation
ref_62499 = ref_62143 # MOV operation
ref_62507 = (ref_62499 >> (0x3 & 0x3F)) # SHR operation
ref_62514 = ref_62507 # MOV operation
ref_62890 = ref_62514 # MOV operation
ref_62896 = (0xF & ref_62890) # AND operation
ref_63277 = ref_62896 # MOV operation
ref_63283 = (0x1 | ref_63277) # OR operation
ref_63470 = ref_60621 # MOV operation
ref_63474 = ref_63283 # MOV operation
ref_63476 = (ref_63474 & 0xFFFFFFFF) # MOV operation
ref_63478 = ((ref_63470 << ((ref_63476 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_63485 = ref_63478 # MOV operation
ref_65027 = ref_32275 # MOV operation
ref_66743 = ref_38202 # MOV operation
ref_67099 = ref_66743 # MOV operation
ref_67107 = (ref_67099 >> (0x3 & 0x3F)) # SHR operation
ref_67114 = ref_67107 # MOV operation
ref_67490 = ref_67114 # MOV operation
ref_67496 = (0xF & ref_67490) # AND operation
ref_67877 = ref_67496 # MOV operation
ref_67883 = (0x1 | ref_67877) # OR operation
ref_68074 = ref_67883 # MOV operation
ref_68076 = ((0x40 - ref_68074) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_68084 = ref_68076 # MOV operation
ref_68266 = ref_65027 # MOV operation
ref_68270 = ref_68084 # MOV operation
ref_68272 = (ref_68270 & 0xFFFFFFFF) # MOV operation
ref_68274 = (ref_68266 >> ((ref_68272 & 0xFF) & 0x3F)) # SHR operation
ref_68281 = ref_68274 # MOV operation
ref_68463 = ref_63485 # MOV operation
ref_68467 = ref_68281 # MOV operation
ref_68469 = (ref_68467 | ref_68463) # OR operation
ref_70016 = ref_45479 # MOV operation
ref_71538 = ref_58917 # MOV operation
ref_71894 = ref_71538 # MOV operation
ref_71900 = (0xF & ref_71894) # AND operation
ref_72281 = ref_71900 # MOV operation
ref_72287 = (0x1 | ref_72281) # OR operation
ref_72474 = ref_70016 # MOV operation
ref_72478 = ref_72287 # MOV operation
ref_72480 = (ref_72478 & 0xFFFFFFFF) # MOV operation
ref_72482 = ((ref_72474 << ((ref_72480 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_72489 = ref_72482 # MOV operation
ref_74031 = ref_45479 # MOV operation
ref_75747 = ref_58917 # MOV operation
ref_76103 = ref_75747 # MOV operation
ref_76109 = (0xF & ref_76103) # AND operation
ref_76490 = ref_76109 # MOV operation
ref_76496 = (0x1 | ref_76490) # OR operation
ref_76687 = ref_76496 # MOV operation
ref_76689 = ((0x40 - ref_76687) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_76697 = ref_76689 # MOV operation
ref_76879 = ref_74031 # MOV operation
ref_76883 = ref_76697 # MOV operation
ref_76885 = (ref_76883 & 0xFFFFFFFF) # MOV operation
ref_76887 = (ref_76879 >> ((ref_76885 & 0xFF) & 0x3F)) # SHR operation
ref_76894 = ref_76887 # MOV operation
ref_77076 = ref_72489 # MOV operation
ref_77080 = ref_76894 # MOV operation
ref_77082 = (ref_77080 | ref_77076) # OR operation
ref_77261 = ref_77082 # MOV operation
ref_77273 = ref_68469 # MOV operation
ref_77275 = ((ref_77261 - ref_77273) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_77277 = ((((ref_77261 ^ (ref_77273 ^ ref_77275)) ^ ((ref_77261 ^ ref_77275) & (ref_77261 ^ ref_77273))) >> 63) & 0x1) # Carry flag
ref_77281 = (0x1 if (ref_77275 == 0x0) else 0x0) # Zero flag
ref_77283 = ((((ref_77273 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if ((ref_77277 | ref_77281) == 0x1) else 0x0)) # SETBE operation
ref_77285 = (ref_77283 & 0xFF) # MOVZX operation
ref_77451 = (ref_77285 & 0xFFFFFFFF) # MOV operation
ref_77453 = ((ref_77451 & 0xFFFFFFFF) & (ref_77451 & 0xFFFFFFFF)) # TEST operation
ref_77458 = (0x1 if (ref_77453 == 0x0) else 0x0) # Zero flag
ref_77460 = (0x402404 if (ref_77458 == 0x1) else 0x4023EC) # Program Counter


if (ref_77458 == 0x1):
    ref_145942 = SymVar_0
    ref_145957 = ref_145942 # MOV operation
    ref_164012 = ref_145957 # MOV operation
    ref_164368 = ref_164012 # MOV operation
    ref_164376 = (ref_164368 >> (0x5 & 0x3F)) # SHR operation
    ref_164383 = ref_164376 # MOV operation
    ref_165933 = ref_164383 # MOV operation
    ref_167475 = ref_165933 # MOV operation
    ref_167831 = ref_167475 # MOV operation
    ref_167837 = (0xB4088A290E23905 ^ ref_167831) # XOR operation
    ref_169362 = ref_145957 # MOV operation
    ref_169718 = ref_169362 # MOV operation
    ref_169724 = ((ref_169718 - 0x10695A81) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_169732 = ref_169724 # MOV operation
    ref_169906 = ref_169732 # MOV operation
    ref_169918 = ref_167837 # MOV operation
    ref_169920 = ((ref_169918 + ref_169906) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_171476 = ref_169920 # MOV operation
    ref_173018 = ref_171476 # MOV operation
    ref_174540 = ref_165933 # MOV operation
    ref_174694 = ref_174540 # MOV operation
    ref_174706 = ref_173018 # MOV operation
    ref_174708 = ((ref_174706 + ref_174694) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_176234 = ref_145957 # MOV operation
    ref_176388 = ref_176234 # MOV operation
    ref_176400 = ref_174708 # MOV operation
    ref_176402 = ((ref_176400 + ref_176388) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_177958 = ref_176402 # MOV operation
    ref_179478 = ref_145957 # MOV operation
    ref_181194 = ref_165933 # MOV operation
    ref_181360 = ref_181194 # MOV operation
    ref_181362 = (((sx(0x40, ref_181360) * sx(0x40, 0x3C8E8C76)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_181740 = ref_181362 # MOV operation
    ref_181746 = (0x7 & ref_181740) # AND operation
    ref_182127 = ref_181746 # MOV operation
    ref_182133 = (0x1 | ref_182127) # OR operation
    ref_182320 = ref_179478 # MOV operation
    ref_182324 = ref_182133 # MOV operation
    ref_182326 = (ref_182324 & 0xFFFFFFFF) # MOV operation
    ref_182328 = (ref_182320 >> ((ref_182326 & 0xFF) & 0x3F)) # SHR operation
    ref_182335 = ref_182328 # MOV operation
    ref_183885 = ref_182335 # MOV operation
    ref_185427 = ref_165933 # MOV operation
    ref_186949 = ref_165933 # MOV operation
    ref_188471 = ref_177958 # MOV operation
    ref_188633 = ref_186949 # MOV operation
    ref_188637 = ref_188471 # MOV operation
    ref_188639 = (((sx(0x40, ref_188637) * sx(0x40, ref_188633)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_189017 = ref_188639 # MOV operation
    ref_189023 = (0x7 & ref_189017) # AND operation
    ref_189404 = ref_189023 # MOV operation
    ref_189412 = ((ref_189404 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_189419 = ref_189412 # MOV operation
    ref_189601 = ref_185427 # MOV operation
    ref_189605 = ref_189419 # MOV operation
    ref_189607 = (ref_189605 | ref_189601) # OR operation
    ref_191162 = ref_189607 # MOV operation
    ref_191164 = ((ref_191162 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_191165 = ((ref_191162 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_191166 = ((ref_191162 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_191167 = ((ref_191162 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_191168 = ((ref_191162 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_191169 = ((ref_191162 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_191170 = ((ref_191162 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_191171 = (ref_191162 & 0xFF) # Byte reference - MOV operation
    ref_192704 = ref_171476 # MOV operation
    ref_194226 = ref_183885 # MOV operation
    ref_195748 = ref_171476 # MOV operation
    ref_196104 = ref_195748 # MOV operation
    ref_196112 = (ref_196104 >> (0x4 & 0x3F)) # SHR operation
    ref_196119 = ref_196112 # MOV operation
    ref_196495 = ref_196119 # MOV operation
    ref_196501 = (0xF & ref_196495) # AND operation
    ref_196882 = ref_196501 # MOV operation
    ref_196888 = (0x1 | ref_196882) # OR operation
    ref_197075 = ref_194226 # MOV operation
    ref_197079 = ref_196888 # MOV operation
    ref_197081 = (ref_197079 & 0xFFFFFFFF) # MOV operation
    ref_197083 = ((ref_197075 << ((ref_197081 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_197090 = ref_197083 # MOV operation
    ref_198632 = ref_183885 # MOV operation
    ref_200348 = ref_171476 # MOV operation
    ref_200704 = ref_200348 # MOV operation
    ref_200712 = (ref_200704 >> (0x4 & 0x3F)) # SHR operation
    ref_200719 = ref_200712 # MOV operation
    ref_201095 = ref_200719 # MOV operation
    ref_201101 = (0xF & ref_201095) # AND operation
    ref_201482 = ref_201101 # MOV operation
    ref_201488 = (0x1 | ref_201482) # OR operation
    ref_201679 = ref_201488 # MOV operation
    ref_201681 = ((0x40 - ref_201679) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_201689 = ref_201681 # MOV operation
    ref_201871 = ref_198632 # MOV operation
    ref_201875 = ref_201689 # MOV operation
    ref_201877 = (ref_201875 & 0xFFFFFFFF) # MOV operation
    ref_201879 = (ref_201871 >> ((ref_201877 & 0xFF) & 0x3F)) # SHR operation
    ref_201886 = ref_201879 # MOV operation
    ref_202068 = ref_197090 # MOV operation
    ref_202072 = ref_201886 # MOV operation
    ref_202074 = (ref_202072 | ref_202068) # OR operation
    ref_202455 = ref_202074 # MOV operation
    ref_202461 = (0xF & ref_202455) # AND operation
    ref_202842 = ref_202461 # MOV operation
    ref_202850 = ((ref_202842 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_202857 = ref_202850 # MOV operation
    ref_203039 = ref_192704 # MOV operation
    ref_203043 = ref_202857 # MOV operation
    ref_203045 = (ref_203043 | ref_203039) # OR operation
    ref_204600 = ref_203045 # MOV operation
    ref_224920 = ref_204600 # MOV operation
    ref_226442 = ref_204600 # MOV operation
    ref_226798 = ref_226442 # MOV operation
    ref_226804 = (0xF & ref_226798) # AND operation
    ref_227185 = ref_226804 # MOV operation
    ref_227193 = ((ref_227185 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_227200 = ref_227193 # MOV operation
    ref_227382 = ref_224920 # MOV operation
    ref_227386 = ref_227200 # MOV operation
    ref_227388 = (ref_227386 | ref_227382) # OR operation
    ref_228943 = ref_227388 # MOV operation
    ref_228945 = ((ref_228943 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_228946 = ((ref_228943 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_228947 = ((ref_228943 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_228948 = ((ref_228943 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_228949 = ((ref_228943 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_228950 = ((ref_228943 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_228951 = ((ref_228943 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_228952 = (ref_228943 & 0xFF) # Byte reference - MOV operation
    ref_253863 = ref_191164 # MOVZX operation
    ref_254223 = (ref_253863 & 0xFF) # MOVZX operation
    ref_256831 = ref_191171 # MOVZX operation
    ref_259427 = (ref_256831 & 0xFF) # MOVZX operation
    ref_259429 = (ref_259427 & 0xFF) # Byte reference - MOV operation
    ref_259799 = (ref_254223 & 0xFF) # MOVZX operation
    ref_262395 = (ref_259799 & 0xFF) # MOVZX operation
    ref_262397 = (ref_262395 & 0xFF) # Byte reference - MOV operation
    ref_271852 = ((((ref_228949) << 8 | ref_228950) << 8 | ref_228951) << 8 | ref_228952) # MOV operation
    ref_272010 = (ref_271852 & 0xFFFFFFFF) # MOV operation
    ref_277396 = ((((ref_228945) << 8 | ref_228946) << 8 | ref_228947) << 8 | ref_228948) # MOV operation
    ref_277554 = (ref_277396 & 0xFFFFFFFF) # MOV operation
    ref_280538 = (ref_272010 & 0xFFFFFFFF) # MOV operation
    ref_280696 = (ref_280538 & 0xFFFFFFFF) # MOV operation
    ref_283680 = (ref_280696 & 0xFFFFFFFF) # MOV operation
    ref_283838 = (ref_283680 & 0xFFFFFFFF) # MOV operation
    ref_289224 = (ref_277554 & 0xFFFFFFFF) # MOV operation
    ref_289382 = (ref_289224 & 0xFFFFFFFF) # MOV operation
    ref_289384 = (((ref_289382 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_289385 = (((ref_289382 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_289386 = (((ref_289382 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_289387 = ((ref_289382 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_292366 = (ref_283838 & 0xFFFFFFFF) # MOV operation
    ref_292524 = (ref_292366 & 0xFFFFFFFF) # MOV operation
    ref_292526 = (((ref_292524 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_292527 = (((ref_292524 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_292528 = (((ref_292524 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_292529 = ((ref_292524 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_294228 = ((((((((ref_289384) << 8 | ref_289385) << 8 | ref_289386) << 8 | ref_289387) << 8 | ref_292526) << 8 | ref_292527) << 8 | ref_292528) << 8 | ref_292529) # MOV operation
    ref_296304 = ((((((((ref_259429) << 8 | ref_191165) << 8 | ref_191166) << 8 | ref_191167) << 8 | ref_191168) << 8 | ref_191169) << 8 | ref_191170) << 8 | ref_262397) # MOV operation
    ref_296466 = ref_294228 # MOV operation
    ref_296470 = ref_296304 # MOV operation
    ref_296472 = ((ref_296466 - ref_296470) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_296480 = ref_296472 # MOV operation
    ref_298584 = ref_296480 # MOV operation
    ref_300680 = ((((((((ref_259429) << 8 | ref_191165) << 8 | ref_191166) << 8 | ref_191167) << 8 | ref_191168) << 8 | ref_191169) << 8 | ref_191170) << 8 | ref_262397) # MOV operation
    ref_302202 = ref_298584 # MOV operation
    ref_302558 = ref_302202 # MOV operation
    ref_302564 = (0x3F & ref_302558) # AND operation
    ref_302945 = ref_302564 # MOV operation
    ref_302953 = ((ref_302945 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_302960 = ref_302953 # MOV operation
    ref_303142 = ref_300680 # MOV operation
    ref_303146 = ref_302960 # MOV operation
    ref_303148 = (ref_303146 | ref_303142) # OR operation
    ref_305257 = ref_303148 # MOV operation
    ref_309421 = ref_298584 # MOV operation
    ref_310943 = ref_183885 # MOV operation
    ref_311105 = ref_309421 # MOV operation
    ref_311109 = ref_310943 # MOV operation
    ref_311111 = (ref_311109 | ref_311105) # OR operation
    ref_312658 = ref_305257 # MOV operation
    ref_314180 = ((((((((ref_289384) << 8 | ref_289385) << 8 | ref_289386) << 8 | ref_289387) << 8 | ref_292526) << 8 | ref_292527) << 8 | ref_292528) << 8 | ref_292529) # MOV operation
    ref_314536 = ref_314180 # MOV operation
    ref_314544 = (ref_314536 >> (0x2 & 0x3F)) # SHR operation
    ref_314551 = ref_314544 # MOV operation
    ref_314927 = ref_314551 # MOV operation
    ref_314933 = (0x7 & ref_314927) # AND operation
    ref_315314 = ref_314933 # MOV operation
    ref_315320 = (0x1 | ref_315314) # OR operation
    ref_315507 = ref_312658 # MOV operation
    ref_315511 = ref_315320 # MOV operation
    ref_315513 = (ref_315511 & 0xFFFFFFFF) # MOV operation
    ref_315515 = ((ref_315507 << ((ref_315513 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_315522 = ref_315515 # MOV operation
    ref_315696 = ref_315522 # MOV operation
    ref_315708 = ref_311111 # MOV operation
    ref_315710 = ((ref_315708 + ref_315696) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_317253 = ref_315710 # MOV operation
    ref_317619 = ref_317253 # MOV operation
    ref_317621 = ref_317619 # MOV operation
    endb = ref_317621


else:
    ref_264 = SymVar_0
    ref_279 = ref_264 # MOV operation
    ref_18329 = ref_279 # MOV operation
    ref_18685 = ref_18329 # MOV operation
    ref_18693 = (ref_18685 >> (0x5 & 0x3F)) # SHR operation
    ref_18700 = ref_18693 # MOV operation
    ref_20250 = ref_18700 # MOV operation
    ref_21792 = ref_20250 # MOV operation
    ref_22148 = ref_21792 # MOV operation
    ref_22154 = (0xB4088A290E23905 ^ ref_22148) # XOR operation
    ref_23679 = ref_279 # MOV operation
    ref_24035 = ref_23679 # MOV operation
    ref_24041 = ((ref_24035 - 0x10695A81) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_24049 = ref_24041 # MOV operation
    ref_24223 = ref_24049 # MOV operation
    ref_24235 = ref_22154 # MOV operation
    ref_24237 = ((ref_24235 + ref_24223) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_25793 = ref_24237 # MOV operation
    ref_27335 = ref_25793 # MOV operation
    ref_28857 = ref_20250 # MOV operation
    ref_29011 = ref_28857 # MOV operation
    ref_29023 = ref_27335 # MOV operation
    ref_29025 = ((ref_29023 + ref_29011) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_30551 = ref_279 # MOV operation
    ref_30705 = ref_30551 # MOV operation
    ref_30717 = ref_29025 # MOV operation
    ref_30719 = ((ref_30717 + ref_30705) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_32275 = ref_30719 # MOV operation
    ref_33795 = ref_279 # MOV operation
    ref_35511 = ref_20250 # MOV operation
    ref_35677 = ref_35511 # MOV operation
    ref_35679 = (((sx(0x40, ref_35677) * sx(0x40, 0x3C8E8C76)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_36057 = ref_35679 # MOV operation
    ref_36063 = (0x7 & ref_36057) # AND operation
    ref_36444 = ref_36063 # MOV operation
    ref_36450 = (0x1 | ref_36444) # OR operation
    ref_36637 = ref_33795 # MOV operation
    ref_36641 = ref_36450 # MOV operation
    ref_36643 = (ref_36641 & 0xFFFFFFFF) # MOV operation
    ref_36645 = (ref_36637 >> ((ref_36643 & 0xFF) & 0x3F)) # SHR operation
    ref_36652 = ref_36645 # MOV operation
    ref_38202 = ref_36652 # MOV operation
    ref_39744 = ref_20250 # MOV operation
    ref_41266 = ref_20250 # MOV operation
    ref_42788 = ref_32275 # MOV operation
    ref_42950 = ref_41266 # MOV operation
    ref_42954 = ref_42788 # MOV operation
    ref_42956 = (((sx(0x40, ref_42954) * sx(0x40, ref_42950)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_43334 = ref_42956 # MOV operation
    ref_43340 = (0x7 & ref_43334) # AND operation
    ref_43721 = ref_43340 # MOV operation
    ref_43729 = ((ref_43721 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_43736 = ref_43729 # MOV operation
    ref_43918 = ref_39744 # MOV operation
    ref_43922 = ref_43736 # MOV operation
    ref_43924 = (ref_43922 | ref_43918) # OR operation
    ref_45479 = ref_43924 # MOV operation
    ref_47021 = ref_25793 # MOV operation
    ref_48543 = ref_38202 # MOV operation
    ref_50065 = ref_25793 # MOV operation
    ref_50421 = ref_50065 # MOV operation
    ref_50429 = (ref_50421 >> (0x4 & 0x3F)) # SHR operation
    ref_50436 = ref_50429 # MOV operation
    ref_50812 = ref_50436 # MOV operation
    ref_50818 = (0xF & ref_50812) # AND operation
    ref_51199 = ref_50818 # MOV operation
    ref_51205 = (0x1 | ref_51199) # OR operation
    ref_51392 = ref_48543 # MOV operation
    ref_51396 = ref_51205 # MOV operation
    ref_51398 = (ref_51396 & 0xFFFFFFFF) # MOV operation
    ref_51400 = ((ref_51392 << ((ref_51398 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_51407 = ref_51400 # MOV operation
    ref_52949 = ref_38202 # MOV operation
    ref_54665 = ref_25793 # MOV operation
    ref_55021 = ref_54665 # MOV operation
    ref_55029 = (ref_55021 >> (0x4 & 0x3F)) # SHR operation
    ref_55036 = ref_55029 # MOV operation
    ref_55412 = ref_55036 # MOV operation
    ref_55418 = (0xF & ref_55412) # AND operation
    ref_55799 = ref_55418 # MOV operation
    ref_55805 = (0x1 | ref_55799) # OR operation
    ref_55996 = ref_55805 # MOV operation
    ref_55998 = ((0x40 - ref_55996) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_56006 = ref_55998 # MOV operation
    ref_56188 = ref_52949 # MOV operation
    ref_56192 = ref_56006 # MOV operation
    ref_56194 = (ref_56192 & 0xFFFFFFFF) # MOV operation
    ref_56196 = (ref_56188 >> ((ref_56194 & 0xFF) & 0x3F)) # SHR operation
    ref_56203 = ref_56196 # MOV operation
    ref_56385 = ref_51407 # MOV operation
    ref_56389 = ref_56203 # MOV operation
    ref_56391 = (ref_56389 | ref_56385) # OR operation
    ref_56772 = ref_56391 # MOV operation
    ref_56778 = (0xF & ref_56772) # AND operation
    ref_57159 = ref_56778 # MOV operation
    ref_57167 = ((ref_57159 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_57174 = ref_57167 # MOV operation
    ref_57356 = ref_47021 # MOV operation
    ref_57360 = ref_57174 # MOV operation
    ref_57362 = (ref_57360 | ref_57356) # OR operation
    ref_58917 = ref_57362 # MOV operation
    ref_58919 = ((ref_58917 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_58920 = ((ref_58917 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_58921 = ((ref_58917 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_58922 = ((ref_58917 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_58923 = ((ref_58917 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_58924 = ((ref_58917 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_58925 = ((ref_58917 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_58926 = (ref_58917 & 0xFF) # Byte reference - MOV operation
    ref_79081 = ref_38202 # MOV operation
    ref_80603 = ref_45479 # MOV operation
    ref_82125 = ref_32275 # MOV operation
    ref_82287 = ref_80603 # MOV operation
    ref_82291 = ref_82125 # MOV operation
    ref_82293 = ((ref_82287 - ref_82291) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_82301 = ref_82293 # MOV operation
    ref_82677 = ref_82301 # MOV operation
    ref_82683 = (0x1F & ref_82677) # AND operation
    ref_83064 = ref_82683 # MOV operation
    ref_83072 = ((ref_83064 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_83079 = ref_83072 # MOV operation
    ref_83261 = ref_79081 # MOV operation
    ref_83265 = ref_83079 # MOV operation
    ref_83267 = (ref_83265 | ref_83261) # OR operation
    ref_84822 = ref_83267 # MOV operation
    ref_86364 = ref_45479 # MOV operation
    ref_87886 = ref_58917 # MOV operation
    ref_88242 = ref_87886 # MOV operation
    ref_88248 = (0x1F & ref_88242) # AND operation
    ref_88629 = ref_88248 # MOV operation
    ref_88637 = ((ref_88629 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_88644 = ref_88637 # MOV operation
    ref_88826 = ref_86364 # MOV operation
    ref_88830 = ref_88644 # MOV operation
    ref_88832 = (ref_88830 | ref_88826) # OR operation
    ref_90387 = ref_88832 # MOV operation
    ref_99852 = ((((ref_58923) << 8 | ref_58924) << 8 | ref_58925) << 8 | ref_58926) # MOV operation
    ref_100010 = (ref_99852 & 0xFFFFFFFF) # MOV operation
    ref_105396 = ((((ref_58919) << 8 | ref_58920) << 8 | ref_58921) << 8 | ref_58922) # MOV operation
    ref_105554 = (ref_105396 & 0xFFFFFFFF) # MOV operation
    ref_108538 = (ref_100010 & 0xFFFFFFFF) # MOV operation
    ref_108696 = (ref_108538 & 0xFFFFFFFF) # MOV operation
    ref_111680 = (ref_108696 & 0xFFFFFFFF) # MOV operation
    ref_111838 = (ref_111680 & 0xFFFFFFFF) # MOV operation
    ref_117224 = (ref_105554 & 0xFFFFFFFF) # MOV operation
    ref_117382 = (ref_117224 & 0xFFFFFFFF) # MOV operation
    ref_117384 = (((ref_117382 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_117385 = (((ref_117382 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_117386 = (((ref_117382 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_117387 = ((ref_117382 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_120366 = (ref_111838 & 0xFFFFFFFF) # MOV operation
    ref_120524 = (ref_120366 & 0xFFFFFFFF) # MOV operation
    ref_120526 = (((ref_120524 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_120527 = (((ref_120524 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_120528 = (((ref_120524 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_120529 = ((ref_120524 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_122228 = ((((((((ref_117384) << 8 | ref_117385) << 8 | ref_117386) << 8 | ref_117387) << 8 | ref_120526) << 8 | ref_120527) << 8 | ref_120528) << 8 | ref_120529) # MOV operation
    ref_124304 = ref_90387 # MOV operation
    ref_124466 = ref_122228 # MOV operation
    ref_124470 = ref_124304 # MOV operation
    ref_124472 = ((ref_124466 - ref_124470) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_124480 = ref_124472 # MOV operation
    ref_126584 = ref_124480 # MOV operation
    ref_128680 = ref_90387 # MOV operation
    ref_130202 = ref_126584 # MOV operation
    ref_130558 = ref_130202 # MOV operation
    ref_130564 = (0x3F & ref_130558) # AND operation
    ref_130945 = ref_130564 # MOV operation
    ref_130953 = ((ref_130945 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_130960 = ref_130953 # MOV operation
    ref_131142 = ref_128680 # MOV operation
    ref_131146 = ref_130960 # MOV operation
    ref_131148 = (ref_131146 | ref_131142) # OR operation
    ref_133257 = ref_131148 # MOV operation
    ref_137421 = ref_126584 # MOV operation
    ref_138943 = ref_84822 # MOV operation
    ref_139105 = ref_137421 # MOV operation
    ref_139109 = ref_138943 # MOV operation
    ref_139111 = (ref_139109 | ref_139105) # OR operation
    ref_140658 = ref_133257 # MOV operation
    ref_142180 = ((((((((ref_117384) << 8 | ref_117385) << 8 | ref_117386) << 8 | ref_117387) << 8 | ref_120526) << 8 | ref_120527) << 8 | ref_120528) << 8 | ref_120529) # MOV operation
    ref_142536 = ref_142180 # MOV operation
    ref_142544 = (ref_142536 >> (0x2 & 0x3F)) # SHR operation
    ref_142551 = ref_142544 # MOV operation
    ref_142927 = ref_142551 # MOV operation
    ref_142933 = (0x7 & ref_142927) # AND operation
    ref_143314 = ref_142933 # MOV operation
    ref_143320 = (0x1 | ref_143314) # OR operation
    ref_143507 = ref_140658 # MOV operation
    ref_143511 = ref_143320 # MOV operation
    ref_143513 = (ref_143511 & 0xFFFFFFFF) # MOV operation
    ref_143515 = ((ref_143507 << ((ref_143513 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_143522 = ref_143515 # MOV operation
    ref_143696 = ref_143522 # MOV operation
    ref_143708 = ref_139111 # MOV operation
    ref_143710 = ((ref_143708 + ref_143696) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_145253 = ref_143710 # MOV operation
    ref_145619 = ref_145253 # MOV operation
    ref_145621 = ref_145619 # MOV operation
    endb = ref_145621


print endb & 0xffffffffffffffff
