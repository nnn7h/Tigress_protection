; ModuleID = 'llvm_expressions/sample8-virt-bogus-loop-iterations-0.ll'
source_filename = "llvm_expressions/sample8-virt-bogus-loop-iterations-0.ll"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone
define i64 @SECRET(i64 %SymVar_0) local_unnamed_addr #0 {
.3:
  %.48 = xor i64 %SymVar_0, 8893317812261383291
  %.49 = add i64 %.48, 7746018054687388513
  %.50 = add i64 %.48, 6604156963082918679
  %.51 = shl i64 %.50, 32
  %.52 = lshr i64 %.50, 32
  %.531 = or i64 %.51, %.52
  %.77 = shl i64 %.48, 16
  %.78 = lshr i64 %.48, 48
  %.792 = or i64 %.77, %.78
  %.103 = xor i64 %.792, %.49
  %.104 = shl i64 %.103, 21
  %.105 = lshr i64 %.103, 43
  %.1063 = or i64 %.104, %.105
  %.129 = add i64 %.103, -2819311800304343090
  %.130 = xor i64 %.1063, %.129
  %.131 = add i64 %.130, %.531
  %.156 = xor i64 %.50, -7582328775477698482
  %.157 = shl i64 %.156, 13
  %.158 = lshr i64 %.156, 51
  %.1594 = or i64 %.157, %.158
  %.183 = add i64 %.129, %.156
  %.184 = xor i64 %.183, %.1594
  %.185 = add i64 %.131, %.184
  %.186 = shl i64 %.185, 32
  %.187 = lshr i64 %.185, 32
  %.1885 = or i64 %.186, %.187
  %.189 = shl i64 %.130, 16
  %.190 = lshr i64 %.130, 48
  %.1916 = or i64 %.189, %.190
  %.220 = xor i64 %.1916, %.131
  %.221 = shl i64 %.220, 21
  %.222 = lshr i64 %.220, 43
  %.2237 = or i64 %.221, %.222
  %.248 = shl i64 %.183, 32
  %.249 = lshr i64 %.183, 32
  %.2508 = or i64 %.248, %.249
  %.251 = add i64 %.220, %.2508
  %.252 = xor i64 %.2237, %.251
  %.253 = xor i64 %.252, 576460752303423488
  %.254 = add i64 %.253, %.1885
  %.255 = shl i64 %.184, 17
  %.256 = lshr i64 %.184, 47
  %.2579 = or i64 %.255, %.256
  %.287 = xor i64 %.2579, %.185
  %.288 = shl i64 %.287, 13
  %.289 = lshr i64 %.287, 51
  %.29010 = or i64 %.288, %.289
  %.319 = xor i64 %.251, %SymVar_0
  %.320 = add i64 %.319, %.287
  %.321 = xor i64 %.320, %.29010
  %.322 = add i64 %.254, %.321
  %.323 = shl i64 %.322, 32
  %.324 = lshr i64 %.322, 32
  %.32511 = or i64 %.323, %.324
  %.327 = shl i64 %.252, 16
  %.328 = lshr i64 %.253, 48
  %.32912 = or i64 %.328, %.327
  %.363 = xor i64 %.32912, %.254
  %.364 = shl i64 %.363, 21
  %.365 = lshr i64 %.363, 43
  %.36613 = or i64 %.364, %.365
  %.397 = shl i64 %.320, 32
  %.398 = lshr i64 %.320, 32
  %.39914 = or i64 %.397, %.398
  %.400 = add i64 %.363, %.39914
  %.401 = xor i64 %.36613, %.400
  %.402 = add i64 %.401, %.32511
  %.403 = shl i64 %.321, 17
  %.404 = lshr i64 %.321, 47
  %.40515 = or i64 %.403, %.404
  %.440 = xor i64 %.40515, %.322
  %.441 = shl i64 %.440, 13
  %.442 = lshr i64 %.440, 51
  %.44316 = or i64 %.441, %.442
  %.478 = add i64 %.400, %.440
  %.479 = xor i64 %.44316, %.478
  %.480 = add i64 %.402, %.479
  %.481 = shl i64 %.480, 32
  %.482 = lshr i64 %.480, 32
  %.48317 = or i64 %.481, %.482
  %.484 = xor i64 %.48317, 255
  %.485 = shl i64 %.401, 16
  %.486 = lshr i64 %.401, 48
  %.48718 = or i64 %.485, %.486
  %.526 = xor i64 %.48718, %.402
  %.527 = shl i64 %.526, 21
  %.528 = lshr i64 %.526, 43
  %.52919 = or i64 %.527, %.528
  %.565 = shl i64 %.478, 32
  %.566 = lshr i64 %.478, 32
  %.56720 = or i64 %.565, %.566
  %.568 = add i64 %.526, %.56720
  %.569 = xor i64 %.52919, %.568
  %.570 = add i64 %.569, %.484
  %.571 = shl i64 %.479, 17
  %.572 = lshr i64 %.479, 47
  %.57321 = or i64 %.571, %.572
  %.613 = xor i64 %.57321, %.480
  %.614 = shl i64 %.613, 13
  %.615 = lshr i64 %.613, 51
  %.61622 = or i64 %.614, %.615
  %.656 = xor i64 %.568, 576460752303423488
  %.657 = add i64 %.656, %.613
  %.658 = xor i64 %.657, %.61622
  %.659 = add i64 %.570, %.658
  %.660 = shl i64 %.659, 32
  %.661 = lshr i64 %.659, 32
  %.66223 = or i64 %.660, %.661
  %.663 = shl i64 %.569, 16
  %.664 = lshr i64 %.569, 48
  %.66524 = or i64 %.663, %.664
  %.710 = xor i64 %.66524, %.570
  %.711 = shl i64 %.710, 21
  %.712 = lshr i64 %.710, 43
  %.71325 = or i64 %.711, %.712
  %.755 = shl i64 %.657, 32
  %.756 = lshr i64 %.657, 32
  %.75726 = or i64 %.755, %.756
  %.758 = add i64 %.710, %.75726
  %.759 = xor i64 %.71325, %.758
  %.760 = add i64 %.759, %.66223
  %.761 = shl i64 %.658, 17
  %.762 = lshr i64 %.658, 47
  %.76327 = or i64 %.761, %.762
  %.809 = xor i64 %.76327, %.659
  %.810 = shl i64 %.809, 13
  %.811 = lshr i64 %.809, 51
  %.81228 = or i64 %.810, %.811
  %.858 = add i64 %.758, %.809
  %.859 = xor i64 %.81228, %.858
  %.860 = add i64 %.760, %.859
  %.861 = shl i64 %.860, 32
  %.862 = lshr i64 %.860, 32
  %.86329 = or i64 %.861, %.862
  %.864 = shl i64 %.759, 16
  %.865 = lshr i64 %.759, 48
  %.86630 = or i64 %.864, %.865
  %.916 = xor i64 %.86630, %.760
  %.917 = shl i64 %.916, 21
  %.918 = lshr i64 %.916, 43
  %.91931 = or i64 %.917, %.918
  %.966 = shl i64 %.858, 32
  %.967 = lshr i64 %.858, 32
  %.96832 = or i64 %.966, %.967
  %.969 = add i64 %.916, %.96832
  %.970 = xor i64 %.91931, %.969
  %.971 = add i64 %.970, %.86329
  %.972 = shl i64 %.859, 17
  %.973 = lshr i64 %.859, 47
  %.97433 = or i64 %.972, %.973
  %.1025 = xor i64 %.97433, %.860
  %.1026 = shl i64 %.1025, 13
  %.1027 = lshr i64 %.1025, 51
  %.102834 = or i64 %.1026, %.1027
  %.1079 = add i64 %.969, %.1025
  %.1080 = xor i64 %.102834, %.1079
  %.1081 = add i64 %.971, %.1080
  %.1082 = shl i64 %.1081, 32
  %.1083 = lshr i64 %.1081, 32
  %.108435 = or i64 %.1082, %.1083
  %.1085 = shl i64 %.970, 16
  %.1086 = lshr i64 %.970, 48
  %.108736 = or i64 %.1085, %.1086
  %.1142 = xor i64 %.108736, %.971
  %.1143 = shl i64 %.1142, 21
  %.1144 = lshr i64 %.1142, 43
  %.114537 = or i64 %.1143, %.1144
  %.1197 = shl i64 %.1079, 32
  %.1198 = lshr i64 %.1079, 32
  %.119938 = or i64 %.1197, %.1198
  %.1200 = add i64 %.1142, %.119938
  %.1201 = xor i64 %.114537, %.1200
  %.1202 = add i64 %.1201, %.108435
  %.1203 = shl i64 %.1080, 17
  %.1204 = lshr i64 %.1080, 47
  %.120539 = or i64 %.1203, %.1204
  %.1261 = xor i64 %.120539, %.1081
  %.1262 = shl i64 %.1261, 13
  %.1263 = lshr i64 %.1261, 51
  %.126440 = or i64 %.1262, %.1263
  %.1320 = add i64 %.1200, %.1261
  %.1321 = xor i64 %.126440, %.1320
  %.1322 = add i64 %.1202, %.1321
  %.1323 = shl i64 %.1322, 32
  %.1324 = lshr i64 %.1322, 32
  %.132541 = or i64 %.1323, %.1324
  %.1326 = shl i64 %.1201, 16
  %.1327 = lshr i64 %.1201, 48
  %.132842 = or i64 %.1326, %.1327
  %.1388 = xor i64 %.132842, %.1202
  %.1389 = shl i64 %.1388, 21
  %.1390 = lshr i64 %.1388, 43
  %.139143 = or i64 %.1389, %.1390
  %.1514 = shl i64 %.1321, 17
  %.1515 = lshr i64 %.1321, 47
  %.151645 = or i64 %.1514, %.1515
  %.1577 = xor i64 %.151645, %.1322
  %.1578 = xor i64 %.1577, %.132541
  %.1579 = xor i64 %.1578, %.139143
  ret i64 %.1579
}

attributes #0 = { norecurse nounwind readnone }
