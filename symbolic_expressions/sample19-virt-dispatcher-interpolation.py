#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_14987 = ref_278 # MOV operation
ref_15586 = ref_14987 # MOV operation
ref_15600 = ((ref_15586 - 0x35CEDE6D) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15608 = ref_15600 # MOV operation
ref_16197 = ref_15608 # MOV operation
ref_25187 = ref_278 # MOV operation
ref_26433 = ref_25187 # MOV operation
ref_26441 = ((((0x0) << 64 | ref_26433) / 0x7) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_27031 = ref_26441 # MOV operation
ref_37384 = ref_27031 # MOV operation
ref_37983 = ref_37384 # MOV operation
ref_37997 = (ref_37983 >> (0x3 & 0x3F)) # SHR operation
ref_39268 = ref_37997 # MOV operation
ref_39274 = (0xF & ref_39268) # AND operation
ref_40290 = ref_39274 # MOV operation
ref_40296 = (0x1 | ref_40290) # OR operation
ref_41571 = ref_40296 # MOV operation
ref_41573 = ((0x7A11169 << ((ref_41571 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_47064 = ref_27031 # MOV operation
ref_47663 = ref_47064 # MOV operation
ref_47677 = (ref_47663 >> (0x3 & 0x3F)) # SHR operation
ref_48948 = ref_47677 # MOV operation
ref_48954 = (0xF & ref_48948) # AND operation
ref_49970 = ref_48954 # MOV operation
ref_49976 = (0x1 | ref_49970) # OR operation
ref_51251 = ref_49976 # MOV operation
ref_51253 = ((0x40 - ref_51251) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_51261 = ref_51253 # MOV operation
ref_52531 = ref_51261 # MOV operation
ref_52533 = (0x7A11169 >> ((ref_52531 & 0xFF) & 0x3F)) # SHR operation
ref_52910 = ref_41573 # MOV operation
ref_52914 = ref_52533 # MOV operation
ref_52916 = (ref_52914 | ref_52910) # OR operation
ref_53540 = ref_52916 # MOV operation
ref_53554 = (ref_53540 >> (0x4 & 0x3F)) # SHR operation
ref_54825 = ref_53554 # MOV operation
ref_54831 = (0xF & ref_54825) # AND operation
ref_55847 = ref_54831 # MOV operation
ref_55853 = (0x1 | ref_55847) # OR operation
ref_60620 = ref_278 # MOV operation
ref_61219 = ref_60620 # MOV operation
ref_61231 = ref_55853 # MOV operation
ref_61233 = ((ref_61219 << ((ref_61231 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_67363 = ref_27031 # MOV operation
ref_67962 = ref_67363 # MOV operation
ref_67976 = (ref_67962 >> (0x3 & 0x3F)) # SHR operation
ref_69247 = ref_67976 # MOV operation
ref_69253 = (0xF & ref_69247) # AND operation
ref_70269 = ref_69253 # MOV operation
ref_70275 = (0x1 | ref_70269) # OR operation
ref_71550 = ref_70275 # MOV operation
ref_71552 = ((0x7A11169 << ((ref_71550 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_77043 = ref_27031 # MOV operation
ref_77642 = ref_77043 # MOV operation
ref_77656 = (ref_77642 >> (0x3 & 0x3F)) # SHR operation
ref_78927 = ref_77656 # MOV operation
ref_78933 = (0xF & ref_78927) # AND operation
ref_79949 = ref_78933 # MOV operation
ref_79955 = (0x1 | ref_79949) # OR operation
ref_81230 = ref_79955 # MOV operation
ref_81232 = ((0x40 - ref_81230) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_81240 = ref_81232 # MOV operation
ref_82510 = ref_81240 # MOV operation
ref_82512 = (0x7A11169 >> ((ref_82510 & 0xFF) & 0x3F)) # SHR operation
ref_82889 = ref_71552 # MOV operation
ref_82893 = ref_82512 # MOV operation
ref_82895 = (ref_82893 | ref_82889) # OR operation
ref_83519 = ref_82895 # MOV operation
ref_83533 = (ref_83519 >> (0x4 & 0x3F)) # SHR operation
ref_84804 = ref_83533 # MOV operation
ref_84810 = (0xF & ref_84804) # AND operation
ref_85826 = ref_84810 # MOV operation
ref_85832 = (0x1 | ref_85826) # OR operation
ref_87107 = ref_85832 # MOV operation
ref_87109 = ((0x40 - ref_87107) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_87117 = ref_87109 # MOV operation
ref_91879 = ref_278 # MOV operation
ref_92478 = ref_91879 # MOV operation
ref_92490 = ref_87117 # MOV operation
ref_92492 = (ref_92478 >> ((ref_92490 & 0xFF) & 0x3F)) # SHR operation
ref_92869 = ref_61233 # MOV operation
ref_92873 = ref_92492 # MOV operation
ref_92875 = (ref_92873 | ref_92869) # OR operation
ref_93469 = ref_92875 # MOV operation
ref_103098 = ref_278 # MOV operation
ref_103697 = ref_103098 # MOV operation
ref_103711 = ((ref_103697 - 0x297EE8A1) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_103719 = ref_103711 # MOV operation
ref_104985 = ref_103719 # MOV operation
ref_104991 = (((sx(0x40, 0x1471C5DA) * sx(0x40, ref_104985)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_105582 = ref_104991 # MOV operation
ref_105584 = ((ref_105582 >> 56) & 0xFF) # Byte reference - MOV operation
ref_105585 = ((ref_105582 >> 48) & 0xFF) # Byte reference - MOV operation
ref_105586 = ((ref_105582 >> 40) & 0xFF) # Byte reference - MOV operation
ref_105587 = ((ref_105582 >> 32) & 0xFF) # Byte reference - MOV operation
ref_105588 = ((ref_105582 >> 24) & 0xFF) # Byte reference - MOV operation
ref_105589 = ((ref_105582 >> 16) & 0xFF) # Byte reference - MOV operation
ref_105590 = ((ref_105582 >> 8) & 0xFF) # Byte reference - MOV operation
ref_105591 = (ref_105582 & 0xFF) # Byte reference - MOV operation
ref_113880 = ((ref_105586) << 8 | ref_105587) # MOVZX operation
ref_115387 = (ref_113880 & 0xFFFF) # MOVZX operation
ref_123679 = ((ref_105588) << 8 | ref_105589) # MOVZX operation
ref_131959 = (ref_123679 & 0xFFFF) # MOVZX operation
ref_133478 = (ref_115387 & 0xFFFF) # MOVZX operation
ref_141758 = (ref_133478 & 0xFFFF) # MOVZX operation
ref_141760 = (((ref_141758 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_141761 = ((ref_141758 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_189592 = ref_27031 # MOV operation
ref_195058 = ref_93469 # MOV operation
ref_196304 = ref_195058 # MOV operation
ref_196310 = (0x1F & ref_196304) # AND operation
ref_196934 = ref_196310 # MOV operation
ref_196948 = ((ref_196934 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_197325 = ref_189592 # MOV operation
ref_197329 = ref_196948 # MOV operation
ref_197331 = (ref_197329 | ref_197325) # OR operation
ref_197925 = ref_197331 # MOV operation
ref_207000 = ref_197925 # MOV operation
ref_212466 = ref_197925 # MOV operation
ref_213712 = ref_212466 # MOV operation
ref_213718 = (0xF & ref_213712) # AND operation
ref_214342 = ref_213718 # MOV operation
ref_214356 = ((ref_214342 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_214733 = ref_207000 # MOV operation
ref_214737 = ref_214356 # MOV operation
ref_214739 = (ref_214737 | ref_214733) # OR operation
ref_215333 = ref_214739 # MOV operation
ref_224238 = ((ref_105584) << 8 | ref_105585) # MOVZX operation
ref_225745 = (ref_224238 & 0xFFFF) # MOVZX operation
ref_234037 = ((ref_105590) << 8 | ref_105591) # MOVZX operation
ref_242317 = (ref_234037 & 0xFFFF) # MOVZX operation
ref_242319 = (((ref_242317 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_242320 = ((ref_242317 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_243836 = (ref_225745 & 0xFFFF) # MOVZX operation
ref_252116 = (ref_243836 & 0xFFFF) # MOVZX operation
ref_260408 = (ref_252116 & 0xFFFF) # MOVZX operation
ref_261915 = (ref_260408 & 0xFFFF) # MOVZX operation
ref_270207 = (ref_131959 & 0xFFFF) # MOVZX operation
ref_278487 = (ref_270207 & 0xFFFF) # MOVZX operation
ref_278489 = (((ref_278487 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_278490 = ((ref_278487 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_280006 = (ref_261915 & 0xFFFF) # MOVZX operation
ref_288286 = (ref_280006 & 0xFFFF) # MOVZX operation
ref_288288 = (((ref_288286 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_288289 = ((ref_288286 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_298557 = ((((((((ref_242319) << 8 | ref_242320) << 8 | ref_288288) << 8 | ref_288289) << 8 | ref_141760) << 8 | ref_141761) << 8 | ref_278489) << 8 | ref_278490) # MOV operation
ref_299156 = ref_298557 # MOV operation
ref_299170 = (ref_299156 >> (0x2 & 0x3F)) # SHR operation
ref_300441 = ref_299170 # MOV operation
ref_300447 = (0xF & ref_300441) # AND operation
ref_301463 = ref_300447 # MOV operation
ref_301469 = (0x1 | ref_301463) # OR operation
ref_306321 = ref_93469 # MOV operation
ref_306920 = ref_306321 # MOV operation
ref_306932 = ref_301469 # MOV operation
ref_306934 = ((ref_306920 << ((ref_306932 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_312425 = ((((((((ref_242319) << 8 | ref_242320) << 8 | ref_288288) << 8 | ref_288289) << 8 | ref_141760) << 8 | ref_141761) << 8 | ref_278489) << 8 | ref_278490) # MOV operation
ref_313024 = ref_312425 # MOV operation
ref_313038 = (ref_313024 >> (0x2 & 0x3F)) # SHR operation
ref_314309 = ref_313038 # MOV operation
ref_314315 = (0xF & ref_314309) # AND operation
ref_315331 = ref_314315 # MOV operation
ref_315337 = (0x1 | ref_315331) # OR operation
ref_316612 = ref_315337 # MOV operation
ref_316614 = ((0x40 - ref_316612) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_316622 = ref_316614 # MOV operation
ref_321469 = ref_93469 # MOV operation
ref_322068 = ref_321469 # MOV operation
ref_322080 = ref_316622 # MOV operation
ref_322082 = (ref_322068 >> ((ref_322080 & 0xFF) & 0x3F)) # SHR operation
ref_322459 = ref_306934 # MOV operation
ref_322463 = ref_322082 # MOV operation
ref_322465 = (ref_322463 | ref_322459) # OR operation
ref_323089 = ref_322465 # MOV operation
ref_323103 = (ref_323089 >> (0x4 & 0x3F)) # SHR operation
ref_324374 = ref_323103 # MOV operation
ref_324380 = (0xF & ref_324374) # AND operation
ref_325396 = ref_324380 # MOV operation
ref_325402 = (0x1 | ref_325396) # OR operation
ref_330254 = ref_215333 # MOV operation
ref_331500 = ref_330254 # MOV operation
ref_331506 = (0xF & ref_331500) # AND operation
ref_332522 = ref_331506 # MOV operation
ref_332528 = (0x1 | ref_332522) # OR operation
ref_337380 = ref_16197 # MOV operation
ref_337979 = ref_337380 # MOV operation
ref_337991 = ref_332528 # MOV operation
ref_337993 = ((ref_337979 << ((ref_337991 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_342845 = ref_215333 # MOV operation
ref_344091 = ref_342845 # MOV operation
ref_344097 = (0xF & ref_344091) # AND operation
ref_345113 = ref_344097 # MOV operation
ref_345119 = (0x1 | ref_345113) # OR operation
ref_346394 = ref_345119 # MOV operation
ref_346396 = ((0x40 - ref_346394) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_346404 = ref_346396 # MOV operation
ref_351251 = ref_16197 # MOV operation
ref_351850 = ref_351251 # MOV operation
ref_351862 = ref_346404 # MOV operation
ref_351864 = (ref_351850 >> ((ref_351862 & 0xFF) & 0x3F)) # SHR operation
ref_352241 = ref_337993 # MOV operation
ref_352245 = ref_351864 # MOV operation
ref_352247 = (ref_352245 | ref_352241) # OR operation
ref_352871 = ref_352247 # MOV operation
ref_352883 = ref_325402 # MOV operation
ref_352885 = (ref_352871 >> ((ref_352883 & 0xFF) & 0x3F)) # SHR operation
ref_359015 = ((((((((ref_242319) << 8 | ref_242320) << 8 | ref_288288) << 8 | ref_288289) << 8 | ref_141760) << 8 | ref_141761) << 8 | ref_278489) << 8 | ref_278490) # MOV operation
ref_359614 = ref_359015 # MOV operation
ref_359628 = (ref_359614 >> (0x2 & 0x3F)) # SHR operation
ref_360899 = ref_359628 # MOV operation
ref_360905 = (0xF & ref_360899) # AND operation
ref_361921 = ref_360905 # MOV operation
ref_361927 = (0x1 | ref_361921) # OR operation
ref_366779 = ref_93469 # MOV operation
ref_367378 = ref_366779 # MOV operation
ref_367390 = ref_361927 # MOV operation
ref_367392 = ((ref_367378 << ((ref_367390 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_372883 = ((((((((ref_242319) << 8 | ref_242320) << 8 | ref_288288) << 8 | ref_288289) << 8 | ref_141760) << 8 | ref_141761) << 8 | ref_278489) << 8 | ref_278490) # MOV operation
ref_373482 = ref_372883 # MOV operation
ref_373496 = (ref_373482 >> (0x2 & 0x3F)) # SHR operation
ref_374767 = ref_373496 # MOV operation
ref_374773 = (0xF & ref_374767) # AND operation
ref_375789 = ref_374773 # MOV operation
ref_375795 = (0x1 | ref_375789) # OR operation
ref_377070 = ref_375795 # MOV operation
ref_377072 = ((0x40 - ref_377070) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_377080 = ref_377072 # MOV operation
ref_381927 = ref_93469 # MOV operation
ref_382526 = ref_381927 # MOV operation
ref_382538 = ref_377080 # MOV operation
ref_382540 = (ref_382526 >> ((ref_382538 & 0xFF) & 0x3F)) # SHR operation
ref_382917 = ref_367392 # MOV operation
ref_382921 = ref_382540 # MOV operation
ref_382923 = (ref_382921 | ref_382917) # OR operation
ref_383547 = ref_382923 # MOV operation
ref_383561 = (ref_383547 >> (0x4 & 0x3F)) # SHR operation
ref_384832 = ref_383561 # MOV operation
ref_384838 = (0xF & ref_384832) # AND operation
ref_385854 = ref_384838 # MOV operation
ref_385860 = (0x1 | ref_385854) # OR operation
ref_387135 = ref_385860 # MOV operation
ref_387137 = ((0x40 - ref_387135) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_387145 = ref_387137 # MOV operation
ref_391992 = ref_215333 # MOV operation
ref_393238 = ref_391992 # MOV operation
ref_393244 = (0xF & ref_393238) # AND operation
ref_394260 = ref_393244 # MOV operation
ref_394266 = (0x1 | ref_394260) # OR operation
ref_399118 = ref_16197 # MOV operation
ref_399717 = ref_399118 # MOV operation
ref_399729 = ref_394266 # MOV operation
ref_399731 = ((ref_399717 << ((ref_399729 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_404583 = ref_215333 # MOV operation
ref_405829 = ref_404583 # MOV operation
ref_405835 = (0xF & ref_405829) # AND operation
ref_406851 = ref_405835 # MOV operation
ref_406857 = (0x1 | ref_406851) # OR operation
ref_408132 = ref_406857 # MOV operation
ref_408134 = ((0x40 - ref_408132) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_408142 = ref_408134 # MOV operation
ref_412989 = ref_16197 # MOV operation
ref_413588 = ref_412989 # MOV operation
ref_413600 = ref_408142 # MOV operation
ref_413602 = (ref_413588 >> ((ref_413600 & 0xFF) & 0x3F)) # SHR operation
ref_413979 = ref_399731 # MOV operation
ref_413983 = ref_413602 # MOV operation
ref_413985 = (ref_413983 | ref_413979) # OR operation
ref_414609 = ref_413985 # MOV operation
ref_414621 = ref_387145 # MOV operation
ref_414623 = ((ref_414609 << ((ref_414621 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_415000 = ref_352885 # MOV operation
ref_415004 = ref_414623 # MOV operation
ref_415006 = (ref_415004 | ref_415000) # OR operation
ref_415600 = ref_415006 # MOV operation
ref_416602 = ref_415600 # MOV operation
ref_416604 = ref_416602 # MOV operation

print ref_416604 & 0xffffffffffffffff
