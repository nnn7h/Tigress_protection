; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = zext i8 13 to i64
  %".5" = and i64 %".4", 63
  %".6" = lshr i64 %"SymVar_0", %".5"
  %".7" = zext i8 51 to i64
  %".8" = and i64 %".7", 63
  %".9" = shl i64 %"SymVar_0", %".8"
  %".10" = or i64 %".6", %".9"
  %".11" = add i64 210061817713481728, %".10"
  %".12" = sub i64 %"SymVar_0", %".11"
  %".13" = zext i8 2 to i64
  %".14" = and i64 %".13", 63
  %".15" = lshr i64 %".12", %".14"
  %".16" = and i64 15, %".15"
  %".17" = or i64 1, %".16"
  %".18" = sub i64 64, %".17"
  %".19" = trunc i64 %".18" to i32
  %".20" = zext i32 %".19" to i64
  %".21" = trunc i64 %".20" to i8
  %".22" = zext i8 %".21" to i64
  %".23" = and i64 %".22", 63
  %".24" = shl i64 %".11", %".23"
  %".25" = zext i8 2 to i64
  %".26" = and i64 %".25", 63
  %".27" = lshr i64 %".12", %".26"
  %".28" = and i64 15, %".27"
  %".29" = or i64 1, %".28"
  %".30" = trunc i64 %".29" to i32
  %".31" = zext i32 %".30" to i64
  %".32" = trunc i64 %".31" to i8
  %".33" = zext i8 %".32" to i64
  %".34" = and i64 %".33", 63
  %".35" = lshr i64 %".11", %".34"
  %".36" = or i64 %".24", %".35"
  %".37" = zext i8 55 to i64
  %".38" = and i64 %".37", 63
  %".39" = lshr i64 %"SymVar_0", %".38"
  %".40" = zext i8 9 to i64
  %".41" = and i64 %".40", 63
  %".42" = shl i64 %"SymVar_0", %".41"
  %".43" = or i64 %".39", %".42"
  %".44" = or i64 %"SymVar_0", 1049658519
  %".45" = sub i64 %".43", %".44"
  %".46" = sub i64 %".36", %".45"
  %".47" = xor i64 %".45", %".46"
  %".48" = xor i64 %".36", %".47"
  %".49" = xor i64 %".36", %".46"
  %".50" = xor i64 %".36", %".45"
  %".51" = and i64 %".49", %".50"
  %".52" = xor i64 %".48", %".51"
  %".53" = lshr i64 %".52", 63
  %".54" = trunc i64 %".53" to i1
  %".55" = icmp eq i1 %".54", 1
  br i1 %".55", label %".3.if", label %".3.else"
.3.if:
  br label %".3.endif"
.3.else:
  br label %".3.endif"
.3.endif:
  %".59" = phi i8 [1, %".3.if"], [0, %".3.else"]
  %".60" = zext i8 %".59" to i64
  %".61" = lshr i64 %".45", 8
  %".62" = trunc i64 %".61" to i56
  %".63" = zext i56 %".62" to i64
  %".64" = shl i64 %".63", 8
  %".65" = or i64 %".60", %".64"
  %".66" = trunc i64 %".65" to i8
  %".67" = zext i8 %".66" to i32
  %".68" = zext i32 %".67" to i64
  %".69" = trunc i64 %".68" to i32
  %".70" = zext i32 %".69" to i64
  %".71" = trunc i64 %".70" to i32
  %".72" = zext i32 %".71" to i64
  %".73" = trunc i64 %".72" to i32
  %".74" = trunc i64 %".72" to i32
  %".75" = and i32 %".73", %".74"
  %".76" = icmp eq i32 %".75", 0
  br i1 %".76", label %".3.endif.if", label %".3.endif.else"
.3.endif.if:
  br label %".3.endif.endif"
.3.endif.else:
  br label %".3.endif.endif"
.3.endif.endif:
  %".80" = phi i1 [1, %".3.endif.if"], [0, %".3.endif.else"]
  %".81" = icmp eq i1 %".80", 1
  br i1 %".81", label %".3.endif.endif.if", label %".3.endif.endif.else"
.3.endif.endif.if:
  br label %".3.endif.endif.endif"
.3.endif.endif.else:
  br label %".3.endif.endif.endif"
.3.endif.endif.endif:
  %".85" = phi i1 [1, %".3.endif.endif.if"], [0, %".3.endif.endif.else"]
  br i1 %".85", label %".3.endif.endif.endif.if", label %".3.endif.endif.endif.else"
.3.endif.endif.endif.if:
  %".87" = zext i8 13 to i64
  %".88" = and i64 %".87", 63
  %".89" = lshr i64 %"SymVar_0", %".88"
  %".90" = zext i8 51 to i64
  %".91" = and i64 %".90", 63
  %".92" = shl i64 %"SymVar_0", %".91"
  %".93" = or i64 %".89", %".92"
  %".94" = add i64 210061817713481728, %".93"
  %".95" = sub i64 %"SymVar_0", %".94"
  %".96" = zext i8 4 to i64
  %".97" = and i64 %".96", 63
  %".98" = lshr i64 %".95", %".97"
  %".99" = and i64 15, %".98"
  %".100" = or i64 1, %".99"
  %".101" = sub i64 64, %".100"
  %".102" = trunc i64 %".101" to i32
  %".103" = zext i32 %".102" to i64
  %".104" = trunc i64 %".103" to i8
  %".105" = zext i8 %".104" to i64
  %".106" = and i64 %".105", 63
  %".107" = lshr i64 %".94", %".106"
  %".108" = zext i8 4 to i64
  %".109" = and i64 %".108", 63
  %".110" = lshr i64 %".95", %".109"
  %".111" = and i64 15, %".110"
  %".112" = or i64 %".111", 1
  %".113" = trunc i64 %".112" to i32
  %".114" = zext i32 %".113" to i64
  %".115" = trunc i64 %".114" to i8
  %".116" = zext i8 %".115" to i64
  %".117" = and i64 %".116", 63
  %".118" = shl i64 %".94", %".117"
  %".119" = or i64 %".107", %".118"
  %".120" = or i64 %"SymVar_0", 1049658519
  %".121" = zext i8 55 to i64
  %".122" = and i64 %".121", 63
  %".123" = lshr i64 %"SymVar_0", %".122"
  %".124" = zext i8 9 to i64
  %".125" = and i64 %".124", 63
  %".126" = shl i64 %"SymVar_0", %".125"
  %".127" = or i64 %".123", %".126"
  %".128" = or i64 %".120", %".127"
  %".129" = zext i8 4 to i64
  %".130" = and i64 %".129", 63
  %".131" = lshr i64 %".128", %".130"
  %".132" = and i64 7, %".131"
  %".133" = or i64 1, %".132"
  %".134" = trunc i64 %".133" to i32
  %".135" = zext i32 %".134" to i64
  %".136" = trunc i64 %".135" to i8
  %".137" = zext i8 %".136" to i64
  %".138" = and i64 %".137", 63
  %".139" = lshr i64 %".119", %".138"
  br label %".3.endif.endif.endif.endif"
.3.endif.endif.endif.else:
  %".141" = zext i8 55 to i64
  %".142" = and i64 %".141", 63
  %".143" = lshr i64 %"SymVar_0", %".142"
  %".144" = zext i8 9 to i64
  %".145" = and i64 %".144", 63
  %".146" = shl i64 %"SymVar_0", %".145"
  %".147" = or i64 %".143", %".146"
  %".148" = zext i8 13 to i64
  %".149" = and i64 %".148", 63
  %".150" = lshr i64 %"SymVar_0", %".149"
  %".151" = zext i8 51 to i64
  %".152" = and i64 %".151", 63
  %".153" = shl i64 %"SymVar_0", %".152"
  %".154" = or i64 %".150", %".153"
  %".155" = add i64 210061817713481728, %".154"
  %".156" = and i64 63, %".155"
  %".157" = zext i8 4 to i64
  %".158" = and i64 %".157", 63
  %".159" = shl i64 %".156", %".158"
  %".160" = or i64 %".155", %".159"
  %".161" = add i64 %".147", %".160"
  %".162" = and i64 31, %".161"
  %".163" = zext i8 3 to i64
  %".164" = and i64 %".163", 63
  %".165" = shl i64 %".162", %".164"
  %".166" = or i64 %".165", %".160"
  %".167" = sub i64 %"SymVar_0", %".155"
  %".168" = lshr i64 %".167", 32
  %".169" = trunc i64 %".168" to i8
  %".170" = zext i8 %".169" to i32
  %".171" = lshr i64 %".167", 40
  %".172" = trunc i64 %".171" to i8
  %".173" = zext i8 %".172" to i32
  %".174" = shl i32 %".173", 8
  %".175" = or i32 %".170", %".174"
  %".176" = lshr i64 %".167", 48
  %".177" = trunc i64 %".176" to i8
  %".178" = zext i8 %".177" to i32
  %".179" = shl i32 %".178", 16
  %".180" = or i32 %".175", %".179"
  %".181" = lshr i64 %".167", 56
  %".182" = trunc i64 %".181" to i8
  %".183" = zext i8 %".182" to i32
  %".184" = shl i32 %".183", 24
  %".185" = or i32 %".180", %".184"
  %".186" = zext i32 %".185" to i64
  %".187" = trunc i64 %".186" to i32
  %".188" = zext i32 %".187" to i64
  %".189" = trunc i64 %".188" to i32
  %".190" = zext i32 %".189" to i64
  %".191" = trunc i64 %".190" to i32
  %".192" = zext i32 %".191" to i64
  %".193" = trunc i64 %".192" to i32
  %".194" = trunc i32 %".193" to i8
  %".195" = zext i8 %".194" to i64
  %".196" = trunc i64 %".192" to i32
  %".197" = lshr i32 %".196", 8
  %".198" = trunc i32 %".197" to i8
  %".199" = zext i8 %".198" to i64
  %".200" = shl i64 %".199", 8
  %".201" = or i64 %".195", %".200"
  %".202" = trunc i64 %".192" to i32
  %".203" = lshr i32 %".202", 16
  %".204" = trunc i32 %".203" to i8
  %".205" = zext i8 %".204" to i64
  %".206" = shl i64 %".205", 16
  %".207" = or i64 %".201", %".206"
  %".208" = trunc i64 %".192" to i32
  %".209" = lshr i32 %".208", 24
  %".210" = trunc i32 %".209" to i8
  %".211" = zext i8 %".210" to i64
  %".212" = shl i64 %".211", 24
  %".213" = or i64 %".207", %".212"
  %".214" = trunc i64 %".167" to i8
  %".215" = zext i8 %".214" to i32
  %".216" = lshr i64 %".167", 8
  %".217" = trunc i64 %".216" to i8
  %".218" = zext i8 %".217" to i32
  %".219" = shl i32 %".218", 8
  %".220" = or i32 %".215", %".219"
  %".221" = lshr i64 %".167", 16
  %".222" = trunc i64 %".221" to i8
  %".223" = zext i8 %".222" to i32
  %".224" = shl i32 %".223", 16
  %".225" = or i32 %".220", %".224"
  %".226" = lshr i64 %".167", 24
  %".227" = trunc i64 %".226" to i8
  %".228" = zext i8 %".227" to i32
  %".229" = shl i32 %".228", 24
  %".230" = or i32 %".225", %".229"
  %".231" = zext i32 %".230" to i64
  %".232" = trunc i64 %".231" to i32
  %".233" = zext i32 %".232" to i64
  %".234" = trunc i64 %".233" to i32
  %".235" = trunc i32 %".234" to i8
  %".236" = zext i8 %".235" to i64
  %".237" = shl i64 %".236", 32
  %".238" = or i64 %".213", %".237"
  %".239" = trunc i64 %".233" to i32
  %".240" = lshr i32 %".239", 8
  %".241" = trunc i32 %".240" to i8
  %".242" = zext i8 %".241" to i64
  %".243" = shl i64 %".242", 40
  %".244" = or i64 %".238", %".243"
  %".245" = trunc i64 %".233" to i32
  %".246" = lshr i32 %".245", 16
  %".247" = trunc i32 %".246" to i8
  %".248" = zext i8 %".247" to i64
  %".249" = shl i64 %".248", 48
  %".250" = or i64 %".244", %".249"
  %".251" = trunc i64 %".233" to i32
  %".252" = lshr i32 %".251", 24
  %".253" = trunc i32 %".252" to i8
  %".254" = zext i8 %".253" to i64
  %".255" = shl i64 %".254", 56
  %".256" = or i64 %".250", %".255"
  %".257" = zext i8 4 to i64
  %".258" = and i64 %".257", 63
  %".259" = lshr i64 %".256", %".258"
  %".260" = and i64 15, %".259"
  %".261" = or i64 1, %".260"
  %".262" = sub i64 64, %".261"
  %".263" = trunc i64 %".262" to i32
  %".264" = zext i32 %".263" to i64
  %".265" = trunc i64 %".264" to i8
  %".266" = zext i8 %".265" to i64
  %".267" = and i64 %".266", 63
  %".268" = lshr i64 %".166", %".267"
  %".269" = zext i8 %".194" to i64
  %".270" = zext i8 %".198" to i64
  %".271" = shl i64 %".270", 8
  %".272" = or i64 %".269", %".271"
  %".273" = zext i8 %".204" to i64
  %".274" = shl i64 %".273", 16
  %".275" = or i64 %".272", %".274"
  %".276" = zext i8 %".210" to i64
  %".277" = shl i64 %".276", 24
  %".278" = or i64 %".275", %".277"
  %".279" = zext i8 %".235" to i64
  %".280" = shl i64 %".279", 32
  %".281" = or i64 %".278", %".280"
  %".282" = zext i8 %".241" to i64
  %".283" = shl i64 %".282", 40
  %".284" = or i64 %".281", %".283"
  %".285" = zext i8 %".247" to i64
  %".286" = shl i64 %".285", 48
  %".287" = or i64 %".284", %".286"
  %".288" = zext i8 %".253" to i64
  %".289" = shl i64 %".288", 56
  %".290" = or i64 %".287", %".289"
  %".291" = zext i8 4 to i64
  %".292" = and i64 %".291", 63
  %".293" = lshr i64 %".290", %".292"
  %".294" = and i64 15, %".293"
  %".295" = or i64 %".294", 1
  %".296" = trunc i64 %".295" to i32
  %".297" = zext i32 %".296" to i64
  %".298" = trunc i64 %".297" to i8
  %".299" = zext i8 %".298" to i64
  %".300" = and i64 %".299", 63
  %".301" = shl i64 %".166", %".300"
  %".302" = or i64 %".268", %".301"
  %".303" = and i64 31, %".160"
  %".304" = zext i8 3 to i64
  %".305" = and i64 %".304", 63
  %".306" = shl i64 %".303", %".305"
  %".307" = or i64 %"SymVar_0", 1049658519
  %".308" = or i64 %".306", %".307"
  %".309" = or i64 %".308", %".147"
  %".310" = zext i8 4 to i64
  %".311" = and i64 %".310", 63
  %".312" = lshr i64 %".309", %".311"
  %".313" = and i64 7, %".312"
  %".314" = or i64 1, %".313"
  %".315" = trunc i64 %".314" to i32
  %".316" = zext i32 %".315" to i64
  %".317" = trunc i64 %".316" to i8
  %".318" = zext i8 %".317" to i64
  %".319" = and i64 %".318", 63
  %".320" = lshr i64 %".302", %".319"
  br label %".3.endif.endif.endif.endif"
.3.endif.endif.endif.endif:
  %".322" = phi i64 [%".139", %".3.endif.endif.endif.if"], [%".320", %".3.endif.endif.endif.else"]
  ret i64 %".322"
}
