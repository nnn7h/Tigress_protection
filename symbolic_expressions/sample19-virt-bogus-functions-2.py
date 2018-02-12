#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_10839 = ref_278 # MOV operation
ref_11599 = ref_10839 # MOV operation
ref_11607 = ((ref_11599 - 0x35CEDE6D) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_11615 = ref_11607 # MOV operation
ref_12003 = ref_11615 # MOV operation
ref_18025 = ref_278 # MOV operation
ref_18841 = ref_18025 # MOV operation
ref_18851 = ((((0x0) << 64 | ref_18841) / 0x7) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_19246 = ref_18851 # MOV operation
ref_25348 = ref_278 # MOV operation
ref_30736 = ref_19246 # MOV operation
ref_31082 = ref_30736 # MOV operation
ref_31100 = (ref_31082 >> (0x3 & 0x3F)) # SHR operation
ref_31107 = ref_31100 # MOV operation
ref_31499 = ref_31107 # MOV operation
ref_31515 = (0xF & ref_31499) # AND operation
ref_32383 = ref_31515 # MOV operation
ref_32391 = (0x1 | ref_32383) # OR operation
ref_32822 = ref_32391 # MOV operation
ref_32824 = (ref_32822 & 0xFFFFFFFF) # MOV operation
ref_32826 = ((0x7A11169 << ((ref_32824 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_32833 = ref_32826 # MOV operation
ref_37348 = ref_19246 # MOV operation
ref_37724 = ref_37348 # MOV operation
ref_37742 = (ref_37724 >> (0x3 & 0x3F)) # SHR operation
ref_37749 = ref_37742 # MOV operation
ref_38125 = ref_37749 # MOV operation
ref_38141 = (0xF & ref_38125) # AND operation
ref_38948 = ref_38141 # MOV operation
ref_38956 = (0x1 | ref_38948) # OR operation
ref_39371 = ref_38956 # MOV operation
ref_39373 = ((0x40 - ref_39371) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_39381 = ref_39373 # MOV operation
ref_40253 = ref_39381 # MOV operation
ref_40255 = (ref_40253 & 0xFFFFFFFF) # MOV operation
ref_40257 = (0x7A11169 >> ((ref_40255 & 0xFF) & 0x3F)) # SHR operation
ref_40264 = ref_40257 # MOV operation
ref_40626 = ref_32833 # MOV operation
ref_40632 = ref_40264 # MOV operation
ref_40634 = (ref_40632 | ref_40626) # OR operation
ref_41059 = ref_40634 # MOV operation
ref_41077 = (ref_41059 >> (0x4 & 0x3F)) # SHR operation
ref_41084 = ref_41077 # MOV operation
ref_41492 = ref_41084 # MOV operation
ref_41508 = (0xF & ref_41492) # AND operation
ref_42284 = ref_41508 # MOV operation
ref_42292 = (0x1 | ref_42284) # OR operation
ref_42782 = ref_25348 # MOV operation
ref_42788 = ref_42292 # MOV operation
ref_42790 = (ref_42788 & 0xFFFFFFFF) # MOV operation
ref_42792 = ((ref_42782 << ((ref_42790 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_42799 = ref_42792 # MOV operation
ref_48490 = ref_19246 # MOV operation
ref_48890 = ref_48490 # MOV operation
ref_48908 = (ref_48890 >> (0x3 & 0x3F)) # SHR operation
ref_48915 = ref_48908 # MOV operation
ref_49326 = ref_48915 # MOV operation
ref_49342 = (0xF & ref_49326) # AND operation
ref_50137 = ref_49342 # MOV operation
ref_50145 = (0x1 | ref_50137) # OR operation
ref_50576 = ref_50145 # MOV operation
ref_50578 = (ref_50576 & 0xFFFFFFFF) # MOV operation
ref_50580 = ((0x7A11169 << ((ref_50578 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_50587 = ref_50580 # MOV operation
ref_55214 = ref_19246 # MOV operation
ref_55556 = ref_55214 # MOV operation
ref_55574 = (ref_55556 >> (0x3 & 0x3F)) # SHR operation
ref_55581 = ref_55574 # MOV operation
ref_55977 = ref_55581 # MOV operation
ref_55993 = (0xF & ref_55977) # AND operation
ref_56809 = ref_55993 # MOV operation
ref_56817 = (0x1 | ref_56809) # OR operation
ref_57212 = ref_56817 # MOV operation
ref_57214 = ((0x40 - ref_57212) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_57222 = ref_57214 # MOV operation
ref_58011 = ref_57222 # MOV operation
ref_58013 = (ref_58011 & 0xFFFFFFFF) # MOV operation
ref_58015 = (0x7A11169 >> ((ref_58013 & 0xFF) & 0x3F)) # SHR operation
ref_58022 = ref_58015 # MOV operation
ref_58440 = ref_50587 # MOV operation
ref_58446 = ref_58022 # MOV operation
ref_58448 = (ref_58446 | ref_58440) # OR operation
ref_58860 = ref_58448 # MOV operation
ref_58878 = (ref_58860 >> (0x4 & 0x3F)) # SHR operation
ref_58885 = ref_58878 # MOV operation
ref_59279 = ref_58885 # MOV operation
ref_59295 = (0xF & ref_59279) # AND operation
ref_60109 = ref_59295 # MOV operation
ref_60117 = (0x1 | ref_60109) # OR operation
ref_60505 = ref_60117 # MOV operation
ref_60507 = ((0x40 - ref_60505) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_60515 = ref_60507 # MOV operation
ref_63738 = ref_278 # MOV operation
ref_64173 = ref_63738 # MOV operation
ref_64187 = ref_60515 # MOV operation
ref_64189 = (ref_64187 & 0xFFFFFFFF) # MOV operation
ref_64191 = (ref_64173 >> ((ref_64189 & 0xFF) & 0x3F)) # SHR operation
ref_64198 = ref_64191 # MOV operation
ref_64585 = ref_42799 # MOV operation
ref_64591 = ref_64198 # MOV operation
ref_64593 = (ref_64591 | ref_64585) # OR operation
ref_65038 = ref_64593 # MOV operation
ref_71462 = ref_278 # MOV operation
ref_72317 = ref_71462 # MOV operation
ref_72325 = ((ref_72317 - 0x297EE8A1) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_72333 = ref_72325 # MOV operation
ref_72687 = ref_72333 # MOV operation
ref_72703 = (((sx(0x40, 0x1471C5DA) * sx(0x40, ref_72687)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_73128 = ref_72703 # MOV operation
ref_73130 = ((ref_73128 >> 56) & 0xFF) # Byte reference - MOV operation
ref_73131 = ((ref_73128 >> 48) & 0xFF) # Byte reference - MOV operation
ref_73132 = ((ref_73128 >> 40) & 0xFF) # Byte reference - MOV operation
ref_73133 = ((ref_73128 >> 32) & 0xFF) # Byte reference - MOV operation
ref_73134 = ((ref_73128 >> 24) & 0xFF) # Byte reference - MOV operation
ref_73135 = ((ref_73128 >> 16) & 0xFF) # Byte reference - MOV operation
ref_73136 = ((ref_73128 >> 8) & 0xFF) # Byte reference - MOV operation
ref_73137 = (ref_73128 & 0xFF) # Byte reference - MOV operation
ref_78832 = ((ref_73132) << 8 | ref_73133) # MOVZX operation
ref_79647 = (ref_78832 & 0xFFFF) # MOVZX operation
ref_85380 = ((ref_73134) << 8 | ref_73135) # MOVZX operation
ref_91023 = (ref_85380 & 0xFFFF) # MOVZX operation
ref_91876 = (ref_79647 & 0xFFFF) # MOVZX operation
ref_97633 = (ref_91876 & 0xFFFF) # MOVZX operation
ref_97635 = (((ref_97633 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_97636 = ((ref_97633 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_130343 = ref_19246 # MOV operation
ref_134002 = ref_65038 # MOV operation
ref_134385 = ref_134002 # MOV operation
ref_134401 = (0x1F & ref_134385) # AND operation
ref_135162 = ref_134401 # MOV operation
ref_135172 = ((ref_135162 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_135179 = ref_135172 # MOV operation
ref_135611 = ref_130343 # MOV operation
ref_135617 = ref_135179 # MOV operation
ref_135619 = (ref_135617 | ref_135611) # OR operation
ref_136034 = ref_135619 # MOV operation
ref_142211 = ref_136034 # MOV operation
ref_145834 = ref_136034 # MOV operation
ref_146202 = ref_145834 # MOV operation
ref_146218 = (0xF & ref_146202) # AND operation
ref_147074 = ref_146218 # MOV operation
ref_147084 = ((ref_147074 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_147091 = ref_147084 # MOV operation
ref_147475 = ref_142211 # MOV operation
ref_147481 = ref_147091 # MOV operation
ref_147483 = (ref_147481 | ref_147475) # OR operation
ref_147898 = ref_147483 # MOV operation
ref_153937 = ((ref_73130) << 8 | ref_73131) # MOVZX operation
ref_154698 = (ref_153937 & 0xFFFF) # MOVZX operation
ref_160423 = ((ref_73136) << 8 | ref_73137) # MOVZX operation
ref_166040 = (ref_160423 & 0xFFFF) # MOVZX operation
ref_166042 = (((ref_166040 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_166043 = ((ref_166040 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_166826 = (ref_154698 & 0xFFFF) # MOVZX operation
ref_172477 = (ref_166826 & 0xFFFF) # MOVZX operation
ref_178026 = (ref_172477 & 0xFFFF) # MOVZX operation
ref_178790 = (ref_178026 & 0xFFFF) # MOVZX operation
ref_184428 = (ref_91023 & 0xFFFF) # MOVZX operation
ref_190118 = (ref_184428 & 0xFFFF) # MOVZX operation
ref_190120 = (((ref_190118 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_190121 = ((ref_190118 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_190987 = (ref_178790 & 0xFFFF) # MOVZX operation
ref_196573 = (ref_190987 & 0xFFFF) # MOVZX operation
ref_196575 = (((ref_196573 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_196576 = ((ref_196573 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_203624 = ref_65038 # MOV operation
ref_207690 = ((((((((ref_166042) << 8 | ref_166043) << 8 | ref_196575) << 8 | ref_196576) << 8 | ref_97635) << 8 | ref_97636) << 8 | ref_190120) << 8 | ref_190121) # MOV operation
ref_208079 = ref_207690 # MOV operation
ref_208097 = (ref_208079 >> (0x2 & 0x3F)) # SHR operation
ref_208104 = ref_208097 # MOV operation
ref_208471 = ref_208104 # MOV operation
ref_208487 = (0xF & ref_208471) # AND operation
ref_209304 = ref_208487 # MOV operation
ref_209312 = (0x1 | ref_209304) # OR operation
ref_209740 = ref_203624 # MOV operation
ref_209746 = ref_209312 # MOV operation
ref_209748 = (ref_209746 & 0xFFFFFFFF) # MOV operation
ref_209750 = ((ref_209740 << ((ref_209748 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_209757 = ref_209750 # MOV operation
ref_214328 = ((((((((ref_166042) << 8 | ref_166043) << 8 | ref_196575) << 8 | ref_196576) << 8 | ref_97635) << 8 | ref_97636) << 8 | ref_190120) << 8 | ref_190121) # MOV operation
ref_214713 = ref_214328 # MOV operation
ref_214731 = (ref_214713 >> (0x2 & 0x3F)) # SHR operation
ref_214738 = ref_214731 # MOV operation
ref_215130 = ref_214738 # MOV operation
ref_215146 = (0xF & ref_215130) # AND operation
ref_215969 = ref_215146 # MOV operation
ref_215977 = (0x1 | ref_215969) # OR operation
ref_216360 = ref_215977 # MOV operation
ref_216362 = ((0x40 - ref_216360) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_216370 = ref_216362 # MOV operation
ref_219687 = ref_65038 # MOV operation
ref_220087 = ref_219687 # MOV operation
ref_220101 = ref_216370 # MOV operation
ref_220103 = (ref_220101 & 0xFFFFFFFF) # MOV operation
ref_220105 = (ref_220087 >> ((ref_220103 & 0xFF) & 0x3F)) # SHR operation
ref_220112 = ref_220105 # MOV operation
ref_220528 = ref_209757 # MOV operation
ref_220534 = ref_220112 # MOV operation
ref_220536 = (ref_220534 | ref_220528) # OR operation
ref_220936 = ref_220536 # MOV operation
ref_220954 = (ref_220936 >> (0x4 & 0x3F)) # SHR operation
ref_220961 = ref_220954 # MOV operation
ref_221393 = ref_220961 # MOV operation
ref_221409 = (0xF & ref_221393) # AND operation
ref_222172 = ref_221409 # MOV operation
ref_222180 = (0x1 | ref_222172) # OR operation
ref_225546 = ref_12003 # MOV operation
ref_229182 = ref_147898 # MOV operation
ref_229595 = ref_229182 # MOV operation
ref_229611 = (0xF & ref_229595) # AND operation
ref_230356 = ref_229611 # MOV operation
ref_230364 = (0x1 | ref_230356) # OR operation
ref_230794 = ref_225546 # MOV operation
ref_230800 = ref_230364 # MOV operation
ref_230802 = (ref_230800 & 0xFFFFFFFF) # MOV operation
ref_230804 = ((ref_230794 << ((ref_230802 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_230811 = ref_230804 # MOV operation
ref_234997 = ref_147898 # MOV operation
ref_235335 = ref_234997 # MOV operation
ref_235351 = (0xF & ref_235335) # AND operation
ref_236201 = ref_235351 # MOV operation
ref_236209 = (0x1 | ref_236201) # OR operation
ref_236578 = ref_236209 # MOV operation
ref_236580 = ((0x40 - ref_236578) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_236588 = ref_236580 # MOV operation
ref_239864 = ref_12003 # MOV operation
ref_240263 = ref_239864 # MOV operation
ref_240277 = ref_236588 # MOV operation
ref_240279 = (ref_240277 & 0xFFFFFFFF) # MOV operation
ref_240281 = (ref_240263 >> ((ref_240279 & 0xFF) & 0x3F)) # SHR operation
ref_240288 = ref_240281 # MOV operation
ref_240660 = ref_230811 # MOV operation
ref_240666 = ref_240288 # MOV operation
ref_240668 = (ref_240666 | ref_240660) # OR operation
ref_241069 = ref_240668 # MOV operation
ref_241083 = ref_222180 # MOV operation
ref_241085 = (ref_241083 & 0xFFFFFFFF) # MOV operation
ref_241087 = (ref_241069 >> ((ref_241085 & 0xFF) & 0x3F)) # SHR operation
ref_241094 = ref_241087 # MOV operation
ref_244504 = ref_12003 # MOV operation
ref_248154 = ref_147898 # MOV operation
ref_248492 = ref_248154 # MOV operation
ref_248508 = (0xF & ref_248492) # AND operation
ref_249323 = ref_248508 # MOV operation
ref_249331 = (0x1 | ref_249323) # OR operation
ref_249759 = ref_244504 # MOV operation
ref_249765 = ref_249331 # MOV operation
ref_249767 = (ref_249765 & 0xFFFFFFFF) # MOV operation
ref_249769 = ((ref_249759 << ((ref_249767 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_249776 = ref_249769 # MOV operation
ref_253946 = ref_147898 # MOV operation
ref_254252 = ref_253946 # MOV operation
ref_254268 = (0xF & ref_254252) # AND operation
ref_255149 = ref_254268 # MOV operation
ref_255157 = (0x1 | ref_255149) # OR operation
ref_255556 = ref_255157 # MOV operation
ref_255558 = ((0x40 - ref_255556) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_255566 = ref_255558 # MOV operation
ref_258891 = ref_12003 # MOV operation
ref_259233 = ref_258891 # MOV operation
ref_259247 = ref_255566 # MOV operation
ref_259249 = (ref_259247 & 0xFFFFFFFF) # MOV operation
ref_259251 = (ref_259233 >> ((ref_259249 & 0xFF) & 0x3F)) # SHR operation
ref_259258 = ref_259251 # MOV operation
ref_259666 = ref_249776 # MOV operation
ref_259672 = ref_259258 # MOV operation
ref_259674 = (ref_259672 | ref_259666) # OR operation
ref_264299 = ref_65038 # MOV operation
ref_268365 = ((((((((ref_166042) << 8 | ref_166043) << 8 | ref_196575) << 8 | ref_196576) << 8 | ref_97635) << 8 | ref_97636) << 8 | ref_190120) << 8 | ref_190121) # MOV operation
ref_268745 = ref_268365 # MOV operation
ref_268763 = (ref_268745 >> (0x2 & 0x3F)) # SHR operation
ref_268770 = ref_268763 # MOV operation
ref_269155 = ref_268770 # MOV operation
ref_269171 = (0xF & ref_269155) # AND operation
ref_269928 = ref_269171 # MOV operation
ref_269936 = (0x1 | ref_269928) # OR operation
ref_270357 = ref_264299 # MOV operation
ref_270363 = ref_269936 # MOV operation
ref_270365 = (ref_270363 & 0xFFFFFFFF) # MOV operation
ref_270367 = ((ref_270357 << ((ref_270365 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_270374 = ref_270367 # MOV operation
ref_274920 = ((((((((ref_166042) << 8 | ref_166043) << 8 | ref_196575) << 8 | ref_196576) << 8 | ref_97635) << 8 | ref_97636) << 8 | ref_190120) << 8 | ref_190121) # MOV operation
ref_275310 = ref_274920 # MOV operation
ref_275328 = (ref_275310 >> (0x2 & 0x3F)) # SHR operation
ref_275335 = ref_275328 # MOV operation
ref_275701 = ref_275335 # MOV operation
ref_275717 = (0xF & ref_275701) # AND operation
ref_276604 = ref_275717 # MOV operation
ref_276612 = (0x1 | ref_276604) # OR operation
ref_277001 = ref_276612 # MOV operation
ref_277003 = ((0x40 - ref_277001) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_277011 = ref_277003 # MOV operation
ref_280267 = ref_65038 # MOV operation
ref_280609 = ref_280267 # MOV operation
ref_280623 = ref_277011 # MOV operation
ref_280625 = (ref_280623 & 0xFFFFFFFF) # MOV operation
ref_280627 = (ref_280609 >> ((ref_280625 & 0xFF) & 0x3F)) # SHR operation
ref_280634 = ref_280627 # MOV operation
ref_281050 = ref_270374 # MOV operation
ref_281056 = ref_280634 # MOV operation
ref_281058 = (ref_281056 | ref_281050) # OR operation
ref_281431 = ref_281058 # MOV operation
ref_281449 = (ref_281431 >> (0x4 & 0x3F)) # SHR operation
ref_281456 = ref_281449 # MOV operation
ref_281859 = ref_281456 # MOV operation
ref_281875 = (0xF & ref_281859) # AND operation
ref_282706 = ref_281875 # MOV operation
ref_282714 = (0x1 | ref_282706) # OR operation
ref_283151 = ref_282714 # MOV operation
ref_283153 = ((0x40 - ref_283151) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_283161 = ref_283153 # MOV operation
ref_283507 = ref_259674 # MOV operation
ref_283513 = ref_283161 # MOV operation
ref_283515 = (ref_283513 & 0xFFFFFFFF) # MOV operation
ref_283517 = ((ref_283507 << ((ref_283515 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_283524 = ref_283517 # MOV operation
ref_283934 = ref_241094 # MOV operation
ref_283940 = ref_283524 # MOV operation
ref_283942 = (ref_283940 | ref_283934) # OR operation
ref_284378 = ref_283942 # MOV operation
ref_285166 = ref_284378 # MOV operation
ref_285168 = ref_285166 # MOV operation

print ref_285168 & 0xffffffffffffffff
