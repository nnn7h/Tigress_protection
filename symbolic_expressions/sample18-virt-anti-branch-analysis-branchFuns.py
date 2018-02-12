#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_269 = SymVar_0
ref_284 = ref_269 # MOV operation
ref_12939 = ref_284 # MOV operation
ref_13266 = ref_12939 # MOV operation
ref_13280 = (ref_13266 >> (0xD & 0x3F)) # SHR operation
ref_16763 = ref_284 # MOV operation
ref_17532 = ref_16763 # MOV operation
ref_17540 = ((ref_17532 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_17547 = ref_17540 # MOV operation
ref_17962 = ref_13280 # MOV operation
ref_17966 = ref_17547 # MOV operation
ref_17968 = (ref_17966 | ref_17962) # OR operation
ref_18346 = ref_17968 # MOV operation
ref_18360 = ((0x2EA4A1C39AF5800 + ref_18346) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_21700 = ref_18360 # MOV operation
ref_25078 = ref_21700 # MOV operation
ref_28524 = ref_284 # MOV operation
ref_28897 = ref_28524 # MOV operation
ref_28909 = ref_25078 # MOV operation
ref_28911 = ((ref_28897 - ref_28909) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_28919 = ref_28911 # MOV operation
ref_32258 = ref_28919 # MOV operation
ref_35773 = ref_284 # MOV operation
ref_36542 = ref_35773 # MOV operation
ref_36550 = ((ref_36542 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_36557 = ref_36550 # MOV operation
ref_40415 = ref_284 # MOV operation
ref_40742 = ref_40415 # MOV operation
ref_40756 = (ref_40742 >> (0x37 & 0x3F)) # SHR operation
ref_41176 = ref_36557 # MOV operation
ref_41180 = ref_40756 # MOV operation
ref_41182 = (ref_41180 | ref_41176) # OR operation
ref_44522 = ref_41182 # MOV operation
ref_48037 = ref_284 # MOV operation
ref_48800 = ref_48037 # MOV operation
ref_48806 = (0x3E908497 | ref_48800) # OR operation
ref_52146 = ref_48806 # MOV operation
ref_56712 = ref_32258 # MOV operation
ref_57039 = ref_56712 # MOV operation
ref_57053 = (ref_57039 >> (0x2 & 0x3F)) # SHR operation
ref_57435 = ref_57053 # MOV operation
ref_57449 = (0xF & ref_57435) # AND operation
ref_58249 = ref_57449 # MOV operation
ref_58255 = (0x1 | ref_58249) # OR operation
ref_61602 = ref_21700 # MOV operation
ref_61929 = ref_61602 # MOV operation
ref_61941 = ref_58255 # MOV operation
ref_61943 = (ref_61929 >> ((ref_61941 & 0xFF) & 0x3F)) # SHR operation
ref_65289 = ref_21700 # MOV operation
ref_69358 = ref_32258 # MOV operation
ref_69685 = ref_69358 # MOV operation
ref_69699 = (ref_69685 >> (0x2 & 0x3F)) # SHR operation
ref_70081 = ref_69699 # MOV operation
ref_70095 = (0xF & ref_70081) # AND operation
ref_70895 = ref_70095 # MOV operation
ref_70901 = (0x1 | ref_70895) # OR operation
ref_71704 = ref_70901 # MOV operation
ref_71706 = ((0x40 - ref_71704) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_71714 = ref_71706 # MOV operation
ref_72140 = ref_65289 # MOV operation
ref_72144 = ref_71714 # MOV operation
ref_72146 = (ref_72144 & 0xFFFFFFFF) # MOV operation
ref_72148 = ((ref_72140 << ((ref_72146 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_72155 = ref_72148 # MOV operation
ref_72570 = ref_61943 # MOV operation
ref_72574 = ref_72155 # MOV operation
ref_72576 = (ref_72574 | ref_72570) # OR operation
ref_75923 = ref_52146 # MOV operation
ref_79232 = ref_44522 # MOV operation
ref_79605 = ref_79232 # MOV operation
ref_79617 = ref_75923 # MOV operation
ref_79619 = ((ref_79605 - ref_79617) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_79627 = ref_79619 # MOV operation
ref_80017 = ref_72576 # MOV operation
ref_80021 = ref_79627 # MOV operation
ref_80023 = ((ref_80017 - ref_80021) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_80025 = ((((ref_80017 ^ (ref_80021 ^ ref_80023)) ^ ((ref_80017 ^ ref_80023) & (ref_80017 ^ ref_80021))) >> 63) & 0x1) # Carry flag
ref_80031 = ((((ref_80021 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (ref_80025 == 0x1) else 0x0)) # SETB operation
ref_80033 = (ref_80031 & 0xFF) # MOVZX operation
ref_80465 = (ref_80033 & 0xFFFFFFFF) # MOV operation
ref_80467 = ((ref_80465 & 0xFFFFFFFF) & (ref_80465 & 0xFFFFFFFF)) # TEST operation
ref_80472 = (0x1 if (ref_80467 == 0x0) else 0x0) # Zero flag
ref_80474 = (0x2780 if (ref_80472 == 0x1) else 0x271F) # Program Counter


if (ref_80472 == 0x1):
    ref_179265 = SymVar_0
    ref_179280 = ref_179265 # MOV operation
    ref_191942 = ref_179280 # MOV operation
    ref_192269 = ref_191942 # MOV operation
    ref_192283 = (ref_192269 >> (0xD & 0x3F)) # SHR operation
    ref_195766 = ref_179280 # MOV operation
    ref_196535 = ref_195766 # MOV operation
    ref_196543 = ((ref_196535 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_196550 = ref_196543 # MOV operation
    ref_196965 = ref_192283 # MOV operation
    ref_196969 = ref_196550 # MOV operation
    ref_196971 = (ref_196969 | ref_196965) # OR operation
    ref_197349 = ref_196971 # MOV operation
    ref_197363 = ((0x2EA4A1C39AF5800 + ref_197349) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_200703 = ref_197363 # MOV operation
    ref_204081 = ref_200703 # MOV operation
    ref_207527 = ref_179280 # MOV operation
    ref_207900 = ref_207527 # MOV operation
    ref_207912 = ref_204081 # MOV operation
    ref_207914 = ((ref_207900 - ref_207912) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_207922 = ref_207914 # MOV operation
    ref_211261 = ref_207922 # MOV operation
    ref_214776 = ref_179280 # MOV operation
    ref_215545 = ref_214776 # MOV operation
    ref_215553 = ((ref_215545 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_215560 = ref_215553 # MOV operation
    ref_219418 = ref_179280 # MOV operation
    ref_219745 = ref_219418 # MOV operation
    ref_219759 = (ref_219745 >> (0x37 & 0x3F)) # SHR operation
    ref_220179 = ref_215560 # MOV operation
    ref_220183 = ref_219759 # MOV operation
    ref_220185 = (ref_220183 | ref_220179) # OR operation
    ref_223525 = ref_220185 # MOV operation
    ref_227040 = ref_179280 # MOV operation
    ref_227803 = ref_227040 # MOV operation
    ref_227809 = (0x3E908497 | ref_227803) # OR operation
    ref_231149 = ref_227809 # MOV operation
    ref_264188 = ref_223525 # MOV operation
    ref_267497 = ref_231149 # MOV operation
    ref_267880 = ref_264188 # MOV operation
    ref_267884 = ref_267497 # MOV operation
    ref_267886 = (ref_267884 | ref_267880) # OR operation
    ref_268251 = ref_267886 # MOV operation
    ref_268265 = (ref_268251 >> (0x4 & 0x3F)) # SHR operation
    ref_268647 = ref_268265 # MOV operation
    ref_268661 = (0x7 & ref_268647) # AND operation
    ref_269461 = ref_268661 # MOV operation
    ref_269467 = (0x1 | ref_269461) # OR operation
    ref_272814 = ref_200703 # MOV operation
    ref_276883 = ref_211261 # MOV operation
    ref_277210 = ref_276883 # MOV operation
    ref_277224 = (ref_277210 >> (0x4 & 0x3F)) # SHR operation
    ref_277606 = ref_277224 # MOV operation
    ref_277620 = (0xF & ref_277606) # AND operation
    ref_278420 = ref_277620 # MOV operation
    ref_278426 = (0x1 | ref_278420) # OR operation
    ref_278853 = ref_272814 # MOV operation
    ref_278857 = ref_278426 # MOV operation
    ref_278859 = (ref_278857 & 0xFFFFFFFF) # MOV operation
    ref_278861 = ((ref_278853 << ((ref_278859 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_278868 = ref_278861 # MOV operation
    ref_282969 = ref_211261 # MOV operation
    ref_283296 = ref_282969 # MOV operation
    ref_283310 = (ref_283296 >> (0x4 & 0x3F)) # SHR operation
    ref_283692 = ref_283310 # MOV operation
    ref_283706 = (0xF & ref_283692) # AND operation
    ref_284506 = ref_283706 # MOV operation
    ref_284512 = (0x1 | ref_284506) # OR operation
    ref_285315 = ref_284512 # MOV operation
    ref_285317 = ((0x40 - ref_285315) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_285325 = ref_285317 # MOV operation
    ref_288671 = ref_200703 # MOV operation
    ref_288998 = ref_288671 # MOV operation
    ref_289010 = ref_285325 # MOV operation
    ref_289012 = (ref_288998 >> ((ref_289010 & 0xFF) & 0x3F)) # SHR operation
    ref_289432 = ref_278868 # MOV operation
    ref_289436 = ref_289012 # MOV operation
    ref_289438 = (ref_289436 | ref_289432) # OR operation
    ref_289803 = ref_289438 # MOV operation
    ref_289815 = ref_269467 # MOV operation
    ref_289817 = (ref_289803 >> ((ref_289815 & 0xFF) & 0x3F)) # SHR operation
    ref_293342 = ref_289817 # MOV operation
    ref_294215 = ref_293342 # MOV operation
    ref_294217 = ref_294215 # MOV operation
    endb = ref_294217


else:
    ref_269 = SymVar_0
    ref_284 = ref_269 # MOV operation
    ref_12939 = ref_284 # MOV operation
    ref_13266 = ref_12939 # MOV operation
    ref_13280 = (ref_13266 >> (0xD & 0x3F)) # SHR operation
    ref_16763 = ref_284 # MOV operation
    ref_17532 = ref_16763 # MOV operation
    ref_17540 = ((ref_17532 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_17547 = ref_17540 # MOV operation
    ref_17962 = ref_13280 # MOV operation
    ref_17966 = ref_17547 # MOV operation
    ref_17968 = (ref_17966 | ref_17962) # OR operation
    ref_18346 = ref_17968 # MOV operation
    ref_18360 = ((0x2EA4A1C39AF5800 + ref_18346) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_21700 = ref_18360 # MOV operation
    ref_25078 = ref_21700 # MOV operation
    ref_28524 = ref_284 # MOV operation
    ref_28897 = ref_28524 # MOV operation
    ref_28909 = ref_25078 # MOV operation
    ref_28911 = ((ref_28897 - ref_28909) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_28919 = ref_28911 # MOV operation
    ref_32258 = ref_28919 # MOV operation
    ref_32260 = ((ref_32258 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_32261 = ((ref_32258 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_32262 = ((ref_32258 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_32263 = ((ref_32258 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_32264 = ((ref_32258 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_32265 = ((ref_32258 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_32266 = ((ref_32258 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_32267 = (ref_32258 & 0xFF) # Byte reference - MOV operation
    ref_35773 = ref_284 # MOV operation
    ref_36542 = ref_35773 # MOV operation
    ref_36550 = ((ref_36542 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_36557 = ref_36550 # MOV operation
    ref_40415 = ref_284 # MOV operation
    ref_40742 = ref_40415 # MOV operation
    ref_40756 = (ref_40742 >> (0x37 & 0x3F)) # SHR operation
    ref_41176 = ref_36557 # MOV operation
    ref_41180 = ref_40756 # MOV operation
    ref_41182 = (ref_41180 | ref_41176) # OR operation
    ref_44522 = ref_41182 # MOV operation
    ref_48037 = ref_284 # MOV operation
    ref_48800 = ref_48037 # MOV operation
    ref_48806 = (0x3E908497 | ref_48800) # OR operation
    ref_52146 = ref_48806 # MOV operation
    ref_86724 = ((((ref_32260) << 8 | ref_32261) << 8 | ref_32262) << 8 | ref_32263) # MOV operation
    ref_87085 = (ref_86724 & 0xFFFFFFFF) # MOV operation
    ref_97890 = ((((ref_32264) << 8 | ref_32265) << 8 | ref_32266) << 8 | ref_32267) # MOV operation
    ref_98251 = (ref_97890 & 0xFFFFFFFF) # MOV operation
    ref_98253 = (((ref_98251 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_98254 = (((ref_98251 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_98255 = (((ref_98251 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_98256 = ((ref_98251 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_104298 = (ref_87085 & 0xFFFFFFFF) # MOV operation
    ref_104659 = (ref_104298 & 0xFFFFFFFF) # MOV operation
    ref_104661 = (((ref_104659 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_104662 = (((ref_104659 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_104663 = (((ref_104659 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_104664 = ((ref_104659 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_107997 = ref_21700 # MOV operation
    ref_111686 = ref_21700 # MOV operation
    ref_112031 = ref_111686 # MOV operation
    ref_112045 = (0x3F & ref_112031) # AND operation
    ref_112851 = ref_112045 # MOV operation
    ref_112859 = ((ref_112851 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_112866 = ref_112859 # MOV operation
    ref_113281 = ref_107997 # MOV operation
    ref_113285 = ref_112866 # MOV operation
    ref_113287 = (ref_113285 | ref_113281) # OR operation
    ref_116627 = ref_113287 # MOV operation
    ref_120005 = ref_52146 # MOV operation
    ref_123694 = ref_116627 # MOV operation
    ref_124039 = ref_123694 # MOV operation
    ref_124053 = (0x1F & ref_124039) # AND operation
    ref_124859 = ref_124053 # MOV operation
    ref_124867 = ((ref_124859 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_124874 = ref_124867 # MOV operation
    ref_125289 = ref_120005 # MOV operation
    ref_125293 = ref_124874 # MOV operation
    ref_125295 = (ref_125293 | ref_125289) # OR operation
    ref_128635 = ref_125295 # MOV operation
    ref_132013 = ref_116627 # MOV operation
    ref_135702 = ref_44522 # MOV operation
    ref_139011 = ref_116627 # MOV operation
    ref_139351 = ref_139011 # MOV operation
    ref_139363 = ref_135702 # MOV operation
    ref_139365 = ((ref_139363 + ref_139351) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_139748 = ref_139365 # MOV operation
    ref_139762 = (0x1F & ref_139748) # AND operation
    ref_140568 = ref_139762 # MOV operation
    ref_140576 = ((ref_140568 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_140583 = ref_140576 # MOV operation
    ref_140998 = ref_132013 # MOV operation
    ref_141002 = ref_140583 # MOV operation
    ref_141004 = (ref_141002 | ref_140998) # OR operation
    ref_144344 = ref_141004 # MOV operation
    ref_148910 = ref_44522 # MOV operation
    ref_152219 = ref_128635 # MOV operation
    ref_152602 = ref_148910 # MOV operation
    ref_152606 = ref_152219 # MOV operation
    ref_152608 = (ref_152606 | ref_152602) # OR operation
    ref_152973 = ref_152608 # MOV operation
    ref_152987 = (ref_152973 >> (0x4 & 0x3F)) # SHR operation
    ref_153369 = ref_152987 # MOV operation
    ref_153383 = (0x7 & ref_153369) # AND operation
    ref_154183 = ref_153383 # MOV operation
    ref_154189 = (0x1 | ref_154183) # OR operation
    ref_157536 = ref_144344 # MOV operation
    ref_161605 = ((((((((ref_98253) << 8 | ref_98254) << 8 | ref_98255) << 8 | ref_98256) << 8 | ref_104661) << 8 | ref_104662) << 8 | ref_104663) << 8 | ref_104664) # MOV operation
    ref_161932 = ref_161605 # MOV operation
    ref_161946 = (ref_161932 >> (0x4 & 0x3F)) # SHR operation
    ref_162328 = ref_161946 # MOV operation
    ref_162342 = (0xF & ref_162328) # AND operation
    ref_163142 = ref_162342 # MOV operation
    ref_163148 = (0x1 | ref_163142) # OR operation
    ref_163575 = ref_157536 # MOV operation
    ref_163579 = ref_163148 # MOV operation
    ref_163581 = (ref_163579 & 0xFFFFFFFF) # MOV operation
    ref_163583 = ((ref_163575 << ((ref_163581 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_163590 = ref_163583 # MOV operation
    ref_167691 = ((((((((ref_98253) << 8 | ref_98254) << 8 | ref_98255) << 8 | ref_98256) << 8 | ref_104661) << 8 | ref_104662) << 8 | ref_104663) << 8 | ref_104664) # MOV operation
    ref_168018 = ref_167691 # MOV operation
    ref_168032 = (ref_168018 >> (0x4 & 0x3F)) # SHR operation
    ref_168414 = ref_168032 # MOV operation
    ref_168428 = (0xF & ref_168414) # AND operation
    ref_169228 = ref_168428 # MOV operation
    ref_169234 = (0x1 | ref_169228) # OR operation
    ref_170037 = ref_169234 # MOV operation
    ref_170039 = ((0x40 - ref_170037) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_170047 = ref_170039 # MOV operation
    ref_173393 = ref_144344 # MOV operation
    ref_173720 = ref_173393 # MOV operation
    ref_173732 = ref_170047 # MOV operation
    ref_173734 = (ref_173720 >> ((ref_173732 & 0xFF) & 0x3F)) # SHR operation
    ref_174154 = ref_163590 # MOV operation
    ref_174158 = ref_173734 # MOV operation
    ref_174160 = (ref_174158 | ref_174154) # OR operation
    ref_174525 = ref_174160 # MOV operation
    ref_174537 = ref_154189 # MOV operation
    ref_174539 = (ref_174525 >> ((ref_174537 & 0xFF) & 0x3F)) # SHR operation
    ref_178064 = ref_174539 # MOV operation
    ref_178937 = ref_178064 # MOV operation
    ref_178939 = ref_178937 # MOV operation
    endb = ref_178939


print endb & 0xffffffffffffffff
