; ModuleID = 'llvm_expressions/sample21-virt-nested-vm-2.ll'
source_filename = "llvm_expressions/sample21-virt-nested-vm-2.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.6 = shl i64 %SymVar_0, 61
  %.9 = lshr i64 %SymVar_0, 3
  %.10 = or i64 %.6, %.9
  %.11 = add i64 %.10, -1072693119
  %.12 = or i64 %.11, %SymVar_0
  %.13 = add i64 %.12, -300260246
  %.26 = shl i64 %SymVar_0, 4
  %.27 = add i64 %.26, 32
  %.30 = and i64 %.27, 1008
  %.31 = lshr i64 %.13, 32
  %.77 = and i64 %.31, 16711680
  %.78 = and i64 %.31, 16777215
  %.8011 = lshr i64 %.13, 56
  %.83 = shl nuw nsw i64 %.8011, 24
  %.84 = or i64 %.78, %.83
  %.111 = shl i64 %.13, 32
  %.112 = and i64 %.111, 1095216660480
  %.113 = or i64 %.84, %.112
  %.118 = and i64 %.111, 280375465082880
  %.119 = or i64 %.113, %.118
  %.124 = and i64 %.111, 71776119061217280
  %.125 = or i64 %.119, %.124
  %.127 = lshr i64 %.13, 24
  %.130 = shl i64 %.127, 56
  %.131 = or i64 %.125, %.130
  %.132 = or i64 %.131, %.30
  %.134 = and i64 %.132, 255
  %0 = lshr i64 %.119, 32
  %.162 = and i64 %0, 65280
  %1 = shl i64 %.132, 32
  %.194 = and i64 %1, 280375465082880
  %.198 = and i64 %.125, 71776119061217280
  %.201 = and i64 %.131, -72057594037927936
  %.163 = or i64 %.83, %.77
  %.168 = or i64 %.163, %.112
  %.173 = or i64 %.168, %.162
  %.178 = or i64 %.173, %.198
  %.195 = or i64 %.178, %.201
  %.200 = or i64 %.195, %.134
  %.205 = or i64 %.200, %.194
  %.211 = lshr i64 %.11, 32
  %.258 = and i64 %.211, 16777215
  %.26030 = lshr i64 %.11, 56
  %.263 = shl nuw nsw i64 %.26030, 24
  %.264 = or i64 %.258, %.263
  %.291 = shl i64 %.11, 32
  %.292 = and i64 %.291, 1095216660480
  %.293 = or i64 %.264, %.292
  %.298 = and i64 %.291, 280375465082880
  %.299 = or i64 %.293, %.298
  %.304 = and i64 %.291, 71776119061217280
  %.305 = or i64 %.299, %.304
  %.307 = lshr i64 %.11, 24
  %.310 = shl i64 %.307, 56
  %.311 = or i64 %.305, %.310
  %.313 = add i64 %.205, %.311
  %.321 = lshr i64 %.313, 63
  %.353 = shl i64 %.313, 1
  %.354 = or i64 %.321, %.353
  ret i64 %.354
}

attributes #0 = { norecurse nounwind readnone }
