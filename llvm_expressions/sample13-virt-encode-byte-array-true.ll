; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = add i64 16045690984833335023, %"SymVar_0"
  %".5" = xor i64 16622151737136758511, %".4"
  %".6" = shl i64 %".4", 15
  %".7" = lshr i64 %".4", 49
  %".8" = xor i64 %".6", %".7"
  %".9" = add i64 %".5", %".8"
  %".10" = xor i64 4660, %".9"
  %".11" = shl i64 %".9", 52
  %".12" = lshr i64 %".9", 12
  %".13" = xor i64 %".11", %".12"
  %".14" = add i64 %".10", %".13"
  %".15" = shl i64 %".14", 26
  %".16" = lshr i64 %".14", 38
  %".17" = xor i64 %".15", %".16"
  %".18" = xor i64 4660, %".14"
  %".19" = add i64 %".18", %".17"
  %".20" = xor i64 %".8", %".19"
  %".21" = shl i64 %".19", 51
  %".22" = lshr i64 %".19", 13
  %".23" = xor i64 %".21", %".22"
  %".24" = add i64 %".20", %".23"
  %".25" = xor i64 %".13", %".24"
  %".26" = shl i64 %".24", 28
  %".27" = lshr i64 %".24", 36
  %".28" = xor i64 %".26", %".27"
  %".29" = add i64 %".25", %".28"
  %".30" = xor i64 %".17", %".29"
  %".31" = shl i64 %".29", 9
  %".32" = lshr i64 %".29", 55
  %".33" = xor i64 %".31", %".32"
  %".34" = add i64 %".30", %".33"
  %".35" = shl i64 %".34", 47
  %".36" = lshr i64 %".34", 17
  %".37" = xor i64 %".35", %".36"
  %".38" = xor i64 %".23", %".34"
  %".39" = add i64 %".38", %".37"
  %".40" = xor i64 %".28", %".39"
  %".41" = shl i64 %".39", 54
  %".42" = lshr i64 %".39", 10
  %".43" = xor i64 %".41", %".42"
  %".44" = add i64 %".40", %".43"
  %".45" = xor i64 %".33", %".44"
  %".46" = shl i64 %".44", 32
  %".47" = lshr i64 %".44", 32
  %".48" = xor i64 %".46", %".47"
  %".49" = add i64 %".45", %".48"
  %".50" = xor i64 %".37", %".49"
  %".51" = shl i64 %".49", 25
  %".52" = lshr i64 %".49", 39
  %".53" = xor i64 %".51", %".52"
  %".54" = add i64 %".50", %".53"
  %".55" = shl i64 %".54", 63
  %".56" = lshr i64 %".54", 1
  %".57" = xor i64 %".55", %".56"
  ret i64 %".57"
}
