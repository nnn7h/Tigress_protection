; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = zext i8 57 to i64
  %".5" = and i64 %".4", 63
  %".6" = lshr i64 %"SymVar_0", %".5"
  %".7" = zext i8 7 to i64
  %".8" = and i64 %".7", 63
  %".9" = shl i64 %"SymVar_0", %".8"
  %".10" = or i64 %".6", %".9"
  %".11" = add i64 1059198491, %"SymVar_0"
  %".12" = sext i64 %".11" to i128
  %".13" = sext i64 931851530 to i128
  %".14" = mul i128 %".12", %".13"
  %".15" = trunc i128 %".14" to i64
  %".16" = sext i64 %".15" to i128
  %".17" = sext i64 234010507 to i128
  %".18" = mul i128 %".16", %".17"
  %".19" = trunc i128 %".18" to i64
  %".20" = zext i8 1 to i64
  %".21" = and i64 %".20", 63
  %".22" = lshr i64 %".19", %".21"
  %".23" = and i64 15, %".22"
  %".24" = or i64 1, %".23"
  %".25" = sub i64 64, %".24"
  %".26" = trunc i64 %".25" to i8
  %".27" = zext i8 %".26" to i64
  %".28" = and i64 %".27", 63
  %".29" = lshr i64 %".10", %".28"
  %".30" = zext i8 57 to i64
  %".31" = and i64 %".30", 63
  %".32" = lshr i64 %"SymVar_0", %".31"
  %".33" = zext i8 7 to i64
  %".34" = and i64 %".33", 63
  %".35" = shl i64 %"SymVar_0", %".34"
  %".36" = or i64 %".32", %".35"
  %".37" = sext i64 %".11" to i128
  %".38" = sext i64 931851530 to i128
  %".39" = mul i128 %".37", %".38"
  %".40" = trunc i128 %".39" to i64
  %".41" = sext i64 %".40" to i128
  %".42" = sext i64 234010507 to i128
  %".43" = mul i128 %".41", %".42"
  %".44" = trunc i128 %".43" to i64
  %".45" = zext i8 1 to i64
  %".46" = and i64 %".45", 63
  %".47" = lshr i64 %".44", %".46"
  %".48" = and i64 15, %".47"
  %".49" = or i64 1, %".48"
  %".50" = trunc i64 %".49" to i8
  %".51" = zext i8 %".50" to i64
  %".52" = and i64 %".51", 63
  %".53" = shl i64 %".36", %".52"
  %".54" = or i64 %".29", %".53"
  %".55" = add i64 11366125, %".54"
  %".56" = add i64 %".55", %"SymVar_0"
  %".57" = and i64 63, %".56"
  %".58" = zext i8 4 to i64
  %".59" = and i64 %".58", 63
  %".60" = shl i64 %".57", %".59"
  %".61" = add i64 728434157, %".54"
  %".62" = and i64 %".61", %".56"
  %".63" = or i64 %".11", %"SymVar_0"
  %".64" = add i64 %".62", %".63"
  %".65" = or i64 %".60", %".64"
  %".66" = add i64 %".65", %".56"
  %".67" = sext i64 %".66" to i128
  %".68" = zext i8 4 to i64
  %".69" = and i64 %".68", 63
  %".70" = lshr i64 %".54", %".69"
  %".71" = and i64 15, %".70"
  %".72" = or i64 1, %".71"
  %".73" = sub i64 64, %".72"
  %".74" = trunc i64 %".73" to i32
  %".75" = zext i32 %".74" to i64
  %".76" = trunc i64 %".75" to i8
  %".77" = zext i8 %".76" to i64
  %".78" = and i64 %".77", 63
  %".79" = lshr i64 %".11", %".78"
  %".80" = zext i8 4 to i64
  %".81" = and i64 %".80", 63
  %".82" = lshr i64 %".54", %".81"
  %".83" = and i64 15, %".82"
  %".84" = or i64 1, %".83"
  %".85" = trunc i64 %".84" to i32
  %".86" = zext i32 %".85" to i64
  %".87" = trunc i64 %".86" to i8
  %".88" = zext i8 %".87" to i64
  %".89" = and i64 %".88", 63
  %".90" = shl i64 %".11", %".89"
  %".91" = or i64 %".79", %".90"
  %".92" = sext i64 %".91" to i128
  %".93" = mul i128 %".67", %".92"
  %".94" = trunc i128 %".93" to i64
  ret i64 %".94"
}
