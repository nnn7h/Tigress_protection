; ModuleID = 'llvm_expressions/tigress-4-challenge-4.ll'
source_filename = "llvm_expressions/tigress-4-challenge-4.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = lshr i64 %SymVar_0, 5
  %.8 = and i64 %.6, 117709218
  %.9 = or i64 %SymVar_0, 441848546
  %.10 = add i64 %.8, %.9
  %.11 = shl i64 %.10, 3
  %.14 = and i64 %.11, 120
  %.19 = add i64 %SymVar_0, -63267836
  %.20 = or i64 %.14, %.19
  %.22 = shl i64 %.20, 3
  %.25 = and i64 %.22, 120
  %.26 = or i64 %.25, %.20
  %.27 = shl i64 %.26, 3
  %.35 = add i64 %SymVar_0, -43022659
  %.38 = lshr i64 %.10, 3
  %.39 = and i64 %.38, 14
  %.40 = or i64 %.39, 1
  %.58 = shl i64 828565327, %.40
  %.62 = lshr i64 %.58, 4
  %0 = and i64 %.62, 6
  %.65 = or i64 %0, 1
  %.70 = shl i64 %.35, %.65
  %.72 = or i64 %.27, %.70
  %.73 = shl i64 %.70, 3
  %.74 = and i64 %.73, 16
  %.81 = and i64 %.27, 120
  %.82 = or i64 %.81, %.26
  %.83 = or i64 %.82, %.74
  %.84 = lshr i64 %SymVar_0, 53
  %.110 = and i64 %.84, 55
  %.113 = and i64 %.6, 22784
  %.115 = or i64 %.110, %.113
  %.118 = and i64 %.6, 7667712
  %.120 = or i64 %.115, %.118
  %.123 = and i64 %.6, 4009754624
  %.125 = or i64 %.120, %.123
  %1 = lshr i64 %SymVar_0, 13
  %.153 = and i64 %1, 442381631488
  %.154 = or i64 %.125, %.153
  %2 = shl i64 %.6, 8
  %.170 = and i64 %2, 144036023238656
  %.173 = shl i64 %.6, 48
  %.186 = and i64 %.173, 65865144550293504
  %.188 = and i64 %.6, 72057594037927936
  %.171 = or i64 %.154, %.188
  %.187 = or i64 %.171, %.170
  %.192 = or i64 %.187, %.186
  %.196 = shl nuw nsw i64 %.110, 1
  %.197 = lshr i64 %.10, 35
  %.236 = and i64 %.197, 2097151
  %.2389 = lshr i64 %.10, 56
  %.241 = shl nuw nsw i64 %.2389, 21
  %.242 = or i64 %.241, %.196
  %.298 = or i64 %.242, %.236
  %.302 = and i64 %.298, 14
  %.303 = or i64 %.302, 1
  %.304 = sub nsw i64 0, %.303
  %.309 = and i64 %.304, 63
  %.310 = shl i64 %.83, %.309
  %.321 = lshr i64 %.83, %.303
  %.322 = or i64 %.310, %.321
  %.323 = shl i64 %.322, 2
  %.326 = and i64 %.323, 60
  %.327 = lshr i64 %.70, 32
  %.374 = and i64 %.327, 16777215
  %.37624 = lshr i64 %.70, 56
  %.379 = shl nuw nsw i64 %.37624, 24
  %.380 = or i64 %.374, %.379
  %.407 = shl i64 %.72, 32
  %.408 = and i64 %.407, 1090921693184
  %3 = shl i64 %.70, 32
  %.414 = and i64 %3, 280375465082880
  %.420 = and i64 %3, 71776119061217280
  %.423 = lshr i64 %.70, 24
  %.426 = shl i64 %.423, 56
  %4 = and i64 %.298, 6
  %.457 = or i64 %4, 1
  %.462 = shl i64 %.192, %.457
  %.409 = or i64 %.380, %.414
  %.415 = or i64 %.409, %.420
  %.421 = or i64 %.415, %.426
  %.427 = or i64 %.421, %.83
  %.428 = or i64 %.427, %.408
  %.429 = or i64 %.428, %.462
  %.463 = or i64 %.429, %.326
  ret i64 %.463
}

attributes #0 = { norecurse nounwind readnone }
