; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = sext i64 18014398509482166540 to i128
  %".5" = zext i64 %"SymVar_0" to i128
  %".6" = zext i64 0 to i128
  %".7" = shl i128 %".6", 64
  %".8" = or i128 %".5", %".7"
  %".9" = zext i64 6 to i128
  %".10" = udiv i128 %".8", %".9"
  %".11" = trunc i128 %".10" to i64
  %".12" = sext i64 %".11" to i128
  %".13" = mul i128 %".4", %".12"
  %".14" = trunc i128 %".13" to i64
  %".15" = sext i64 %".14" to i128
  %".16" = zext i8 51 to i64
  %".17" = and i64 %".16", 63
  %".18" = lshr i64 %"SymVar_0", %".17"
  %".19" = zext i8 13 to i64
  %".20" = and i64 %".19", 63
  %".21" = shl i64 %"SymVar_0", %".20"
  %".22" = or i64 %".18", %".21"
  %".23" = sext i64 %".22" to i128
  %".24" = mul i128 %".15", %".23"
  %".25" = trunc i128 %".24" to i64
  %".26" = sext i64 81897458 to i128
  %".27" = add i64 %".14", %"SymVar_0"
  %".28" = sub i64 %".22", 785763710
  %".29" = sub i64 686160936, %".28"
  %".30" = zext i8 2 to i64
  %".31" = and i64 %".30", 63
  %".32" = lshr i64 %".29", %".31"
  %".33" = and i64 7, %".32"
  %".34" = or i64 1, %".33"
  %".35" = trunc i64 %".34" to i8
  %".36" = zext i8 %".35" to i64
  %".37" = and i64 %".36", 63
  %".38" = lshr i64 %".27", %".37"
  %".39" = zext i8 1 to i64
  %".40" = and i64 %".39", 63
  %".41" = lshr i64 %".38", %".40"
  %".42" = and i64 7, %".41"
  %".43" = or i64 1, %".42"
  %".44" = trunc i64 %".43" to i8
  %".45" = zext i8 %".44" to i64
  %".46" = and i64 %".45", 63
  %".47" = lshr i64 %".38", %".46"
  %".48" = trunc i64 %".47" to i8
  %".49" = zext i8 %".48" to i32
  %".50" = lshr i64 %".47", 8
  %".51" = trunc i64 %".50" to i8
  %".52" = zext i8 %".51" to i32
  %".53" = shl i32 %".52", 8
  %".54" = or i32 %".49", %".53"
  %".55" = lshr i64 %".47", 16
  %".56" = trunc i64 %".55" to i8
  %".57" = zext i8 %".56" to i32
  %".58" = shl i32 %".57", 16
  %".59" = or i32 %".54", %".58"
  %".60" = lshr i64 %".47", 24
  %".61" = trunc i64 %".60" to i8
  %".62" = zext i8 %".61" to i32
  %".63" = shl i32 %".62", 24
  %".64" = or i32 %".59", %".63"
  %".65" = zext i32 %".64" to i64
  %".66" = trunc i64 %".65" to i32
  %".67" = zext i32 %".66" to i64
  %".68" = trunc i64 %".67" to i32
  %".69" = zext i32 %".68" to i64
  %".70" = trunc i64 %".69" to i32
  %".71" = zext i32 %".70" to i64
  %".72" = trunc i64 %".71" to i32
  %".73" = zext i32 %".72" to i64
  %".74" = trunc i64 %".73" to i32
  %".75" = zext i32 %".74" to i64
  %".76" = trunc i64 %".75" to i32
  %".77" = zext i32 %".76" to i64
  %".78" = trunc i64 %".77" to i32
  %".79" = zext i32 %".78" to i64
  %".80" = trunc i64 %".79" to i32
  %".81" = zext i32 %".80" to i64
  %".82" = trunc i64 %".81" to i32
  %".83" = zext i32 %".82" to i64
  %".84" = trunc i64 %".83" to i32
  %".85" = zext i32 %".84" to i64
  %".86" = trunc i64 %".85" to i32
  %".87" = zext i32 %".86" to i64
  %".88" = trunc i64 %".87" to i32
  %".89" = trunc i32 %".88" to i8
  %".90" = zext i8 %".89" to i64
  %".91" = trunc i64 %".87" to i32
  %".92" = lshr i32 %".91", 8
  %".93" = trunc i32 %".92" to i8
  %".94" = zext i8 %".93" to i64
  %".95" = shl i64 %".94", 8
  %".96" = or i64 %".90", %".95"
  %".97" = trunc i64 %".87" to i32
  %".98" = lshr i32 %".97", 16
  %".99" = trunc i32 %".98" to i8
  %".100" = zext i8 %".99" to i64
  %".101" = shl i64 %".100", 16
  %".102" = or i64 %".96", %".101"
  %".103" = trunc i64 %".87" to i32
  %".104" = lshr i32 %".103", 24
  %".105" = trunc i32 %".104" to i8
  %".106" = zext i8 %".105" to i64
  %".107" = shl i64 %".106", 24
  %".108" = or i64 %".102", %".107"
  %".109" = lshr i64 %".47", 32
  %".110" = trunc i64 %".109" to i8
  %".111" = zext i8 %".110" to i32
  %".112" = lshr i64 %".47", 40
  %".113" = trunc i64 %".112" to i8
  %".114" = zext i8 %".113" to i32
  %".115" = shl i32 %".114", 8
  %".116" = or i32 %".111", %".115"
  %".117" = lshr i64 %".47", 48
  %".118" = trunc i64 %".117" to i8
  %".119" = zext i8 %".118" to i32
  %".120" = shl i32 %".119", 16
  %".121" = or i32 %".116", %".120"
  %".122" = lshr i64 %".47", 56
  %".123" = trunc i64 %".122" to i8
  %".124" = zext i8 %".123" to i32
  %".125" = shl i32 %".124", 24
  %".126" = or i32 %".121", %".125"
  %".127" = zext i32 %".126" to i64
  %".128" = trunc i64 %".127" to i32
  %".129" = zext i32 %".128" to i64
  %".130" = trunc i64 %".129" to i32
  %".131" = zext i32 %".130" to i64
  %".132" = trunc i64 %".131" to i32
  %".133" = zext i32 %".132" to i64
  %".134" = trunc i64 %".133" to i32
  %".135" = zext i32 %".134" to i64
  %".136" = trunc i64 %".135" to i32
  %".137" = zext i32 %".136" to i64
  %".138" = trunc i64 %".137" to i32
  %".139" = zext i32 %".138" to i64
  %".140" = trunc i64 %".139" to i32
  %".141" = zext i32 %".140" to i64
  %".142" = trunc i64 %".141" to i32
  %".143" = zext i32 %".142" to i64
  %".144" = trunc i64 %".143" to i32
  %".145" = zext i32 %".144" to i64
  %".146" = trunc i64 %".145" to i32
  %".147" = zext i32 %".146" to i64
  %".148" = trunc i64 %".147" to i32
  %".149" = zext i32 %".148" to i64
  %".150" = trunc i64 %".149" to i32
  %".151" = trunc i32 %".150" to i8
  %".152" = zext i8 %".151" to i64
  %".153" = shl i64 %".152", 32
  %".154" = or i64 %".108", %".153"
  %".155" = trunc i64 %".149" to i32
  %".156" = lshr i32 %".155", 8
  %".157" = trunc i32 %".156" to i8
  %".158" = zext i8 %".157" to i64
  %".159" = shl i64 %".158", 40
  %".160" = or i64 %".154", %".159"
  %".161" = trunc i64 %".149" to i32
  %".162" = lshr i32 %".161", 16
  %".163" = trunc i32 %".162" to i8
  %".164" = zext i8 %".163" to i64
  %".165" = shl i64 %".164", 48
  %".166" = or i64 %".160", %".165"
  %".167" = trunc i64 %".149" to i32
  %".168" = lshr i32 %".167", 24
  %".169" = trunc i32 %".168" to i8
  %".170" = zext i8 %".169" to i64
  %".171" = shl i64 %".170", 56
  %".172" = or i64 %".166", %".171"
  %".173" = sext i64 %".172" to i128
  %".174" = mul i128 %".26", %".173"
  %".175" = trunc i128 %".174" to i64
  %".176" = and i64 7, %".22"
  %".177" = zext i8 2 to i64
  %".178" = and i64 %".177", 63
  %".179" = shl i64 %".176", %".178"
  %".180" = or i64 %".14", %".22"
  %".181" = add i64 %".180", %"SymVar_0"
  %".182" = or i64 %".179", %".181"
  %".183" = and i64 7, %".182"
  %".184" = zext i8 2 to i64
  %".185" = and i64 %".184", 63
  %".186" = shl i64 %".183", %".185"
  %".187" = or i64 %".186", %".182"
  %".188" = xor i64 %".175", %".187"
  %".189" = and i64 15, %".188"
  %".190" = or i64 1, %".189"
  %".191" = sub i64 64, %".190"
  %".192" = trunc i64 %".191" to i8
  %".193" = zext i8 %".192" to i64
  %".194" = and i64 %".193", 63
  %".195" = lshr i64 %".25", %".194"
  %".196" = sext i64 %".14" to i128
  %".197" = sext i64 %".22" to i128
  %".198" = mul i128 %".196", %".197"
  %".199" = trunc i128 %".198" to i64
  %".200" = sext i64 81897458 to i128
  %".201" = zext i8 %".89" to i64
  %".202" = zext i8 %".93" to i64
  %".203" = shl i64 %".202", 8
  %".204" = or i64 %".201", %".203"
  %".205" = zext i8 %".99" to i64
  %".206" = shl i64 %".205", 16
  %".207" = or i64 %".204", %".206"
  %".208" = zext i8 %".105" to i64
  %".209" = shl i64 %".208", 24
  %".210" = or i64 %".207", %".209"
  %".211" = zext i8 %".151" to i64
  %".212" = shl i64 %".211", 32
  %".213" = or i64 %".210", %".212"
  %".214" = zext i8 %".157" to i64
  %".215" = shl i64 %".214", 40
  %".216" = or i64 %".213", %".215"
  %".217" = zext i8 %".163" to i64
  %".218" = shl i64 %".217", 48
  %".219" = or i64 %".216", %".218"
  %".220" = zext i8 %".169" to i64
  %".221" = shl i64 %".220", 56
  %".222" = or i64 %".219", %".221"
  %".223" = sext i64 %".222" to i128
  %".224" = mul i128 %".200", %".223"
  %".225" = trunc i128 %".224" to i64
  %".226" = xor i64 %".225", %".187"
  %".227" = and i64 15, %".226"
  %".228" = or i64 1, %".227"
  %".229" = trunc i64 %".228" to i8
  %".230" = zext i8 %".229" to i64
  %".231" = and i64 %".230", 63
  %".232" = shl i64 %".199", %".231"
  %".233" = or i64 %".195", %".232"
  ret i64 %".233"
}
