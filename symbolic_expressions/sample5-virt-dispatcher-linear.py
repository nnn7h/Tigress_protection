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
ref_35090 = ref_280 # MOVZX operation
ref_36151 = (ref_35090 & 0xFF) # MOVZX operation
ref_36153 = (ref_36151 & 0xFF) # MOVZX operation
ref_36382 = (ref_36153 & 0xFFFFFFFF) # MOV operation
ref_36384 = (((ref_36382 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_37635 = (ref_36384 & 0xFFFFFFFF) # MOV operation
ref_39718 = (ref_37635 & 0xFFFFFFFF) # MOV operation
ref_41058 = (ref_37635 & 0xFFFFFFFF) # MOV operation
ref_41640 = (ref_41058 & 0xFFFFFFFF) # MOV operation
ref_41648 = (((ref_41640 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_41655 = (ref_41648 & 0xFFFFFFFF) # MOV operation
ref_41900 = (ref_39718 & 0xFFFFFFFF) # MOV operation
ref_41904 = (ref_41655 & 0xFFFFFFFF) # MOV operation
ref_41906 = (((ref_41904 & 0xFFFFFFFF) + (ref_41900 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_43157 = (ref_41906 & 0xFFFFFFFF) # MOV operation
ref_45240 = (ref_43157 & 0xFFFFFFFF) # MOV operation
ref_47072 = (ref_45240 & 0xFFFFFFFF) # MOV operation
ref_47080 = ((ref_47072 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_47087 = (ref_47080 & 0xFFFFFFFF) # MOV operation
ref_48447 = (ref_43157 & 0xFFFFFFFF) # MOV operation
ref_49314 = (ref_48447 & 0xFFFFFFFF) # MOV operation
ref_49326 = (ref_47087 & 0xFFFFFFFF) # MOV operation
ref_49328 = ((ref_49326 & 0xFFFFFFFF) ^ (ref_49314 & 0xFFFFFFFF)) # XOR operation
ref_50578 = (ref_49328 & 0xFFFFFFFF) # MOV operation
ref_62405 = (ref_50578 & 0xFFFFFFFF) # MOV operation
ref_69958 = ref_279 # MOVZX operation
ref_71019 = (ref_69958 & 0xFF) # MOVZX operation
ref_71021 = (ref_71019 & 0xFF) # MOVZX operation
ref_71246 = (ref_62405 & 0xFFFFFFFF) # MOV operation
ref_71250 = (ref_71021 & 0xFFFFFFFF) # MOV operation
ref_71252 = (((ref_71250 & 0xFFFFFFFF) + (ref_71246 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_72503 = (ref_71252 & 0xFFFFFFFF) # MOV operation
ref_74586 = (ref_72503 & 0xFFFFFFFF) # MOV operation
ref_75926 = (ref_72503 & 0xFFFFFFFF) # MOV operation
ref_76508 = (ref_75926 & 0xFFFFFFFF) # MOV operation
ref_76516 = (((ref_76508 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_76523 = (ref_76516 & 0xFFFFFFFF) # MOV operation
ref_76768 = (ref_74586 & 0xFFFFFFFF) # MOV operation
ref_76772 = (ref_76523 & 0xFFFFFFFF) # MOV operation
ref_76774 = (((ref_76772 & 0xFFFFFFFF) + (ref_76768 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_78025 = (ref_76774 & 0xFFFFFFFF) # MOV operation
ref_80108 = (ref_78025 & 0xFFFFFFFF) # MOV operation
ref_81940 = (ref_80108 & 0xFFFFFFFF) # MOV operation
ref_81948 = ((ref_81940 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_81955 = (ref_81948 & 0xFFFFFFFF) # MOV operation
ref_83315 = (ref_78025 & 0xFFFFFFFF) # MOV operation
ref_84182 = (ref_83315 & 0xFFFFFFFF) # MOV operation
ref_84194 = (ref_81955 & 0xFFFFFFFF) # MOV operation
ref_84196 = ((ref_84194 & 0xFFFFFFFF) ^ (ref_84182 & 0xFFFFFFFF)) # XOR operation
ref_85446 = (ref_84196 & 0xFFFFFFFF) # MOV operation
ref_97273 = (ref_85446 & 0xFFFFFFFF) # MOV operation
ref_104826 = ref_278 # MOVZX operation
ref_105887 = (ref_104826 & 0xFF) # MOVZX operation
ref_105889 = (ref_105887 & 0xFF) # MOVZX operation
ref_106114 = (ref_97273 & 0xFFFFFFFF) # MOV operation
ref_106118 = (ref_105889 & 0xFFFFFFFF) # MOV operation
ref_106120 = (((ref_106118 & 0xFFFFFFFF) + (ref_106114 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_107371 = (ref_106120 & 0xFFFFFFFF) # MOV operation
ref_109454 = (ref_107371 & 0xFFFFFFFF) # MOV operation
ref_110794 = (ref_107371 & 0xFFFFFFFF) # MOV operation
ref_111376 = (ref_110794 & 0xFFFFFFFF) # MOV operation
ref_111384 = (((ref_111376 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_111391 = (ref_111384 & 0xFFFFFFFF) # MOV operation
ref_111636 = (ref_109454 & 0xFFFFFFFF) # MOV operation
ref_111640 = (ref_111391 & 0xFFFFFFFF) # MOV operation
ref_111642 = (((ref_111640 & 0xFFFFFFFF) + (ref_111636 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_112893 = (ref_111642 & 0xFFFFFFFF) # MOV operation
ref_114976 = (ref_112893 & 0xFFFFFFFF) # MOV operation
ref_116808 = (ref_114976 & 0xFFFFFFFF) # MOV operation
ref_116816 = ((ref_116808 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_116823 = (ref_116816 & 0xFFFFFFFF) # MOV operation
ref_118183 = (ref_112893 & 0xFFFFFFFF) # MOV operation
ref_119050 = (ref_118183 & 0xFFFFFFFF) # MOV operation
ref_119062 = (ref_116823 & 0xFFFFFFFF) # MOV operation
ref_119064 = ((ref_119062 & 0xFFFFFFFF) ^ (ref_119050 & 0xFFFFFFFF)) # XOR operation
ref_120314 = (ref_119064 & 0xFFFFFFFF) # MOV operation
ref_132141 = (ref_120314 & 0xFFFFFFFF) # MOV operation
ref_139694 = ref_277 # MOVZX operation
ref_140755 = (ref_139694 & 0xFF) # MOVZX operation
ref_140757 = (ref_140755 & 0xFF) # MOVZX operation
ref_140982 = (ref_132141 & 0xFFFFFFFF) # MOV operation
ref_140986 = (ref_140757 & 0xFFFFFFFF) # MOV operation
ref_140988 = (((ref_140986 & 0xFFFFFFFF) + (ref_140982 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_142239 = (ref_140988 & 0xFFFFFFFF) # MOV operation
ref_144322 = (ref_142239 & 0xFFFFFFFF) # MOV operation
ref_145662 = (ref_142239 & 0xFFFFFFFF) # MOV operation
ref_146244 = (ref_145662 & 0xFFFFFFFF) # MOV operation
ref_146252 = (((ref_146244 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_146259 = (ref_146252 & 0xFFFFFFFF) # MOV operation
ref_146504 = (ref_144322 & 0xFFFFFFFF) # MOV operation
ref_146508 = (ref_146259 & 0xFFFFFFFF) # MOV operation
ref_146510 = (((ref_146508 & 0xFFFFFFFF) + (ref_146504 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_147761 = (ref_146510 & 0xFFFFFFFF) # MOV operation
ref_149844 = (ref_147761 & 0xFFFFFFFF) # MOV operation
ref_151676 = (ref_149844 & 0xFFFFFFFF) # MOV operation
ref_151684 = ((ref_151676 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_151691 = (ref_151684 & 0xFFFFFFFF) # MOV operation
ref_153051 = (ref_147761 & 0xFFFFFFFF) # MOV operation
ref_153918 = (ref_153051 & 0xFFFFFFFF) # MOV operation
ref_153930 = (ref_151691 & 0xFFFFFFFF) # MOV operation
ref_153932 = ((ref_153930 & 0xFFFFFFFF) ^ (ref_153918 & 0xFFFFFFFF)) # XOR operation
ref_155182 = (ref_153932 & 0xFFFFFFFF) # MOV operation
ref_167009 = (ref_155182 & 0xFFFFFFFF) # MOV operation
ref_174562 = ref_276 # MOVZX operation
ref_175623 = (ref_174562 & 0xFF) # MOVZX operation
ref_175625 = (ref_175623 & 0xFF) # MOVZX operation
ref_175850 = (ref_167009 & 0xFFFFFFFF) # MOV operation
ref_175854 = (ref_175625 & 0xFFFFFFFF) # MOV operation
ref_175856 = (((ref_175854 & 0xFFFFFFFF) + (ref_175850 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_177107 = (ref_175856 & 0xFFFFFFFF) # MOV operation
ref_179190 = (ref_177107 & 0xFFFFFFFF) # MOV operation
ref_180530 = (ref_177107 & 0xFFFFFFFF) # MOV operation
ref_181112 = (ref_180530 & 0xFFFFFFFF) # MOV operation
ref_181120 = (((ref_181112 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_181127 = (ref_181120 & 0xFFFFFFFF) # MOV operation
ref_181372 = (ref_179190 & 0xFFFFFFFF) # MOV operation
ref_181376 = (ref_181127 & 0xFFFFFFFF) # MOV operation
ref_181378 = (((ref_181376 & 0xFFFFFFFF) + (ref_181372 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_182629 = (ref_181378 & 0xFFFFFFFF) # MOV operation
ref_184712 = (ref_182629 & 0xFFFFFFFF) # MOV operation
ref_186544 = (ref_184712 & 0xFFFFFFFF) # MOV operation
ref_186552 = ((ref_186544 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_186559 = (ref_186552 & 0xFFFFFFFF) # MOV operation
ref_187919 = (ref_182629 & 0xFFFFFFFF) # MOV operation
ref_188786 = (ref_187919 & 0xFFFFFFFF) # MOV operation
ref_188798 = (ref_186559 & 0xFFFFFFFF) # MOV operation
ref_188800 = ((ref_188798 & 0xFFFFFFFF) ^ (ref_188786 & 0xFFFFFFFF)) # XOR operation
ref_190050 = (ref_188800 & 0xFFFFFFFF) # MOV operation
ref_201877 = (ref_190050 & 0xFFFFFFFF) # MOV operation
ref_209430 = ref_275 # MOVZX operation
ref_210491 = (ref_209430 & 0xFF) # MOVZX operation
ref_210493 = (ref_210491 & 0xFF) # MOVZX operation
ref_210718 = (ref_201877 & 0xFFFFFFFF) # MOV operation
ref_210722 = (ref_210493 & 0xFFFFFFFF) # MOV operation
ref_210724 = (((ref_210722 & 0xFFFFFFFF) + (ref_210718 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_211975 = (ref_210724 & 0xFFFFFFFF) # MOV operation
ref_214058 = (ref_211975 & 0xFFFFFFFF) # MOV operation
ref_215398 = (ref_211975 & 0xFFFFFFFF) # MOV operation
ref_215980 = (ref_215398 & 0xFFFFFFFF) # MOV operation
ref_215988 = (((ref_215980 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_215995 = (ref_215988 & 0xFFFFFFFF) # MOV operation
ref_216240 = (ref_214058 & 0xFFFFFFFF) # MOV operation
ref_216244 = (ref_215995 & 0xFFFFFFFF) # MOV operation
ref_216246 = (((ref_216244 & 0xFFFFFFFF) + (ref_216240 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_217497 = (ref_216246 & 0xFFFFFFFF) # MOV operation
ref_219580 = (ref_217497 & 0xFFFFFFFF) # MOV operation
ref_221412 = (ref_219580 & 0xFFFFFFFF) # MOV operation
ref_221420 = ((ref_221412 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_221427 = (ref_221420 & 0xFFFFFFFF) # MOV operation
ref_222787 = (ref_217497 & 0xFFFFFFFF) # MOV operation
ref_223654 = (ref_222787 & 0xFFFFFFFF) # MOV operation
ref_223666 = (ref_221427 & 0xFFFFFFFF) # MOV operation
ref_223668 = ((ref_223666 & 0xFFFFFFFF) ^ (ref_223654 & 0xFFFFFFFF)) # XOR operation
ref_224918 = (ref_223668 & 0xFFFFFFFF) # MOV operation
ref_236745 = (ref_224918 & 0xFFFFFFFF) # MOV operation
ref_244298 = ref_274 # MOVZX operation
ref_245359 = (ref_244298 & 0xFF) # MOVZX operation
ref_245361 = (ref_245359 & 0xFF) # MOVZX operation
ref_245586 = (ref_236745 & 0xFFFFFFFF) # MOV operation
ref_245590 = (ref_245361 & 0xFFFFFFFF) # MOV operation
ref_245592 = (((ref_245590 & 0xFFFFFFFF) + (ref_245586 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_246843 = (ref_245592 & 0xFFFFFFFF) # MOV operation
ref_248926 = (ref_246843 & 0xFFFFFFFF) # MOV operation
ref_250266 = (ref_246843 & 0xFFFFFFFF) # MOV operation
ref_250848 = (ref_250266 & 0xFFFFFFFF) # MOV operation
ref_250856 = (((ref_250848 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_250863 = (ref_250856 & 0xFFFFFFFF) # MOV operation
ref_251108 = (ref_248926 & 0xFFFFFFFF) # MOV operation
ref_251112 = (ref_250863 & 0xFFFFFFFF) # MOV operation
ref_251114 = (((ref_251112 & 0xFFFFFFFF) + (ref_251108 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_252365 = (ref_251114 & 0xFFFFFFFF) # MOV operation
ref_254448 = (ref_252365 & 0xFFFFFFFF) # MOV operation
ref_256280 = (ref_254448 & 0xFFFFFFFF) # MOV operation
ref_256288 = ((ref_256280 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_256295 = (ref_256288 & 0xFFFFFFFF) # MOV operation
ref_257655 = (ref_252365 & 0xFFFFFFFF) # MOV operation
ref_258522 = (ref_257655 & 0xFFFFFFFF) # MOV operation
ref_258534 = (ref_256295 & 0xFFFFFFFF) # MOV operation
ref_258536 = ((ref_258534 & 0xFFFFFFFF) ^ (ref_258522 & 0xFFFFFFFF)) # XOR operation
ref_259786 = (ref_258536 & 0xFFFFFFFF) # MOV operation
ref_271613 = (ref_259786 & 0xFFFFFFFF) # MOV operation
ref_279166 = ref_273 # MOVZX operation
ref_280227 = (ref_279166 & 0xFF) # MOVZX operation
ref_280229 = (ref_280227 & 0xFF) # MOVZX operation
ref_280454 = (ref_271613 & 0xFFFFFFFF) # MOV operation
ref_280458 = (ref_280229 & 0xFFFFFFFF) # MOV operation
ref_280460 = (((ref_280458 & 0xFFFFFFFF) + (ref_280454 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_281711 = (ref_280460 & 0xFFFFFFFF) # MOV operation
ref_283794 = (ref_281711 & 0xFFFFFFFF) # MOV operation
ref_285134 = (ref_281711 & 0xFFFFFFFF) # MOV operation
ref_285716 = (ref_285134 & 0xFFFFFFFF) # MOV operation
ref_285724 = (((ref_285716 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_285731 = (ref_285724 & 0xFFFFFFFF) # MOV operation
ref_285976 = (ref_283794 & 0xFFFFFFFF) # MOV operation
ref_285980 = (ref_285731 & 0xFFFFFFFF) # MOV operation
ref_285982 = (((ref_285980 & 0xFFFFFFFF) + (ref_285976 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_287233 = (ref_285982 & 0xFFFFFFFF) # MOV operation
ref_289316 = (ref_287233 & 0xFFFFFFFF) # MOV operation
ref_291148 = (ref_289316 & 0xFFFFFFFF) # MOV operation
ref_291156 = ((ref_291148 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_291163 = (ref_291156 & 0xFFFFFFFF) # MOV operation
ref_292523 = (ref_287233 & 0xFFFFFFFF) # MOV operation
ref_293390 = (ref_292523 & 0xFFFFFFFF) # MOV operation
ref_293402 = (ref_291163 & 0xFFFFFFFF) # MOV operation
ref_293404 = ((ref_293402 & 0xFFFFFFFF) ^ (ref_293390 & 0xFFFFFFFF)) # XOR operation
ref_294654 = (ref_293404 & 0xFFFFFFFF) # MOV operation
ref_302728 = (ref_294654 & 0xFFFFFFFF) # MOV operation
ref_304068 = (ref_294654 & 0xFFFFFFFF) # MOV operation
ref_304650 = (ref_304068 & 0xFFFFFFFF) # MOV operation
ref_304658 = (((ref_304650 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_304665 = (ref_304658 & 0xFFFFFFFF) # MOV operation
ref_304910 = (ref_302728 & 0xFFFFFFFF) # MOV operation
ref_304914 = (ref_304665 & 0xFFFFFFFF) # MOV operation
ref_304916 = (((ref_304914 & 0xFFFFFFFF) + (ref_304910 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_306167 = (ref_304916 & 0xFFFFFFFF) # MOV operation
ref_308250 = (ref_306167 & 0xFFFFFFFF) # MOV operation
ref_310082 = (ref_308250 & 0xFFFFFFFF) # MOV operation
ref_310090 = ((ref_310082 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_310097 = (ref_310090 & 0xFFFFFFFF) # MOV operation
ref_311457 = (ref_306167 & 0xFFFFFFFF) # MOV operation
ref_312324 = (ref_311457 & 0xFFFFFFFF) # MOV operation
ref_312336 = (ref_310097 & 0xFFFFFFFF) # MOV operation
ref_312338 = ((ref_312336 & 0xFFFFFFFF) ^ (ref_312324 & 0xFFFFFFFF)) # XOR operation
ref_313588 = (ref_312338 & 0xFFFFFFFF) # MOV operation
ref_315671 = (ref_313588 & 0xFFFFFFFF) # MOV operation
ref_317011 = (ref_313588 & 0xFFFFFFFF) # MOV operation
ref_317593 = (ref_317011 & 0xFFFFFFFF) # MOV operation
ref_317601 = (((ref_317593 & 0xFFFFFFFF) << (0xF & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_317608 = (ref_317601 & 0xFFFFFFFF) # MOV operation
ref_317853 = (ref_315671 & 0xFFFFFFFF) # MOV operation
ref_317857 = (ref_317608 & 0xFFFFFFFF) # MOV operation
ref_317859 = (((ref_317857 & 0xFFFFFFFF) + (ref_317853 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_319110 = (ref_317859 & 0xFFFFFFFF) # MOV operation
ref_321299 = (ref_319110 & 0xFFFFFFFF) # MOV operation
ref_322562 = (ref_321299 & 0xFFFFFFFF) # MOV operation
ref_322586 = (ref_322562 & 0xFFFFFFFF) # MOV operation
ref_322594 = (ref_322586 & 0xFFFFFFFF) # MOV operation
ref_322596 = (ref_322594 & 0xFFFFFFFF) # MOV operation

print ref_322596 & 0xffffffffffffffff
