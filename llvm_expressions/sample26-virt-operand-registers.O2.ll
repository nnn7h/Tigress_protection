; ModuleID = 'llvm_expressions/sample26-virt-operand-registers.ll'
source_filename = "llvm_expressions/sample26-virt-operand-registers.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 5
  %.8 = lshr i64 %SymVar_0, 53
  %.10 = and i64 %.8, 55
  %.25 = and i64 %.6, 22784
  %.27 = or i64 %.10, %.25
  %.30 = and i64 %.6, 7667712
  %.32 = or i64 %.27, %.30
  %.35 = and i64 %.6, 4009754624
  %.37 = or i64 %.32, %.35
  %0 = lshr i64 %SymVar_0, 13
  %.53 = and i64 %0, 442381631488
  %.54 = or i64 %.37, %.53
  %1 = shl i64 %SymVar_0, 3
  %.64 = and i64 %1, 144036023238656
  %.65 = or i64 %.54, %.64
  %.67 = shl i64 %.6, 48
  %.74 = and i64 %.67, 65865144550293504
  %.76 = and i64 %.6, 72057594037927936
  %.75 = or i64 %.65, %.76
  %.80 = or i64 %.75, %.74
  %.81 = or i64 %SymVar_0, 441848546
  %.82 = and i64 %.6, 117709218
  %.83 = add i64 %.82, %.81
  %.84 = lshr i64 %.83, 35
  %.119 = and i64 %.84, 2097151
  %.12111 = lshr i64 %.83, 56
  %.124 = shl nuw nsw i64 %.12111, 21
  %.198 = shl nuw nsw i64 %.10, 1
  %.125 = or i64 %.124, %.198
  %.199 = or i64 %.125, %.119
  %.203 = and i64 %.199, 6
  %.204 = or i64 %.203, 1
  %.210 = shl i64 %.80, %.204
  %.211 = add i64 %SymVar_0, -43022659
  %.214 = lshr i64 %.83, 3
  %.215 = and i64 %.214, 14
  %.216 = or i64 %.215, 1
  %.222 = shl i64 828565327, %.216
  %.238 = lshr i64 %.222, 4
  %.239 = and i64 %.238, 6
  %.240 = or i64 %.239, 1
  %.246 = shl i64 %.211, %.240
  %.247 = add i64 %SymVar_0, -63267836
  %.248 = shl i64 %.83, 3
  %.251 = and i64 %.248, 120
  %.252 = or i64 %.251, %.247
  %.253 = shl i64 %.252, 3
  %.266 = and i64 %.253, 120
  %.267 = or i64 %.266, %.252
  %.268 = shl i64 %.267, 3
  %.272 = or i64 %.268, %.246
  %.273 = lshr i64 %.246, 32
  %.312 = and i64 %.273, 16777215
  %.31430 = lshr i64 %.246, 56
  %.317 = shl nuw nsw i64 %.31430, 24
  %.318 = or i64 %.312, %.317
  %.320 = shl i64 %.272, 32
  %.342 = and i64 %.320, 1090921693184
  %2 = shl i64 %.246, 32
  %.348 = and i64 %2, 280375465082880
  %.354 = and i64 %2, 71776119061217280
  %.357 = lshr i64 %.246, 24
  %.360 = shl i64 %.357, 56
  %.365 = and i64 %.268, 120
  %.366 = or i64 %.365, %.267
  %.367 = shl i64 %.246, 3
  %.368 = and i64 %.367, 16
  %.372 = or i64 %.366, %.368
  %.376 = and i64 %.199, 14
  %.377 = or i64 %.376, 1
  %.383 = lshr i64 %.372, %.377
  %.389 = sub nsw i64 64, %.377
  %.395 = shl i64 %.372, %.389
  %.396 = or i64 %.395, %.383
  %.397 = shl i64 %.396, 2
  %.400 = and i64 %.397, 60
  %.343 = or i64 %.318, %.348
  %.349 = or i64 %.343, %.354
  %.355 = or i64 %.349, %.360
  %.361 = or i64 %.355, %.372
  %.401 = or i64 %.361, %.342
  %.402 = or i64 %.401, %.210
  %.403 = or i64 %.402, %.400
  ret i64 %.403
}

attributes #0 = { norecurse nounwind readnone }
