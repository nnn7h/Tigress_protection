; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = or i64 520276322, %"SymVar_0"
  %".5" = and i64 528979890, %".4"
  %".6" = and i64 %".5", %"SymVar_0"
  %".7" = and i64 7, %".6"
  %".8" = zext i8 2 to i64
  %".9" = and i64 %".8", 63
  %".10" = shl i64 %".7", %".9"
  %".11" = zext i8 57 to i64
  %".12" = and i64 %".11", 63
  %".13" = shl i64 %".6", %".12"
  %".14" = zext i8 7 to i64
  %".15" = and i64 %".14", 63
  %".16" = lshr i64 %".6", %".15"
  %".17" = or i64 %".13", %".16"
  %".18" = sext i64 107672031 to i128
  %".19" = sext i64 %"SymVar_0" to i128
  %".20" = mul i128 %".18", %".19"
  %".21" = trunc i128 %".20" to i64
  %".22" = add i64 %".17", %".21"
  %".23" = or i64 %".10", %".22"
  %".24" = lshr i64 %".23", 56
  %".25" = trunc i64 %".24" to i8
  %".26" = zext i8 %".25" to i32
  %".27" = zext i32 %".26" to i64
  %".28" = trunc i64 %".27" to i8
  %".29" = zext i8 %".28" to i32
  %".30" = zext i32 %".29" to i64
  %".31" = trunc i64 %".30" to i8
  %".32" = zext i8 %".31" to i32
  %".33" = zext i32 %".32" to i64
  %".34" = trunc i64 %".33" to i8
  %".35" = zext i8 %".34" to i32
  %".36" = zext i32 %".35" to i64
  %".37" = trunc i64 %".36" to i8
  %".38" = zext i8 %".37" to i64
  %".39" = lshr i64 %".23", 8
  %".40" = trunc i64 %".39" to i8
  %".41" = zext i8 %".40" to i64
  %".42" = shl i64 %".41", 8
  %".43" = or i64 %".38", %".42"
  %".44" = lshr i64 %".23", 16
  %".45" = trunc i64 %".44" to i8
  %".46" = zext i8 %".45" to i64
  %".47" = shl i64 %".46", 16
  %".48" = or i64 %".43", %".47"
  %".49" = lshr i64 %".23", 24
  %".50" = trunc i64 %".49" to i8
  %".51" = zext i8 %".50" to i64
  %".52" = shl i64 %".51", 24
  %".53" = or i64 %".48", %".52"
  %".54" = lshr i64 %".23", 32
  %".55" = trunc i64 %".54" to i8
  %".56" = zext i8 %".55" to i64
  %".57" = shl i64 %".56", 32
  %".58" = or i64 %".53", %".57"
  %".59" = lshr i64 %".23", 40
  %".60" = trunc i64 %".59" to i8
  %".61" = zext i8 %".60" to i64
  %".62" = shl i64 %".61", 40
  %".63" = or i64 %".58", %".62"
  %".64" = lshr i64 %".23", 48
  %".65" = trunc i64 %".64" to i8
  %".66" = zext i8 %".65" to i64
  %".67" = shl i64 %".66", 48
  %".68" = or i64 %".63", %".67"
  %".69" = trunc i64 %".23" to i8
  %".70" = zext i8 %".69" to i32
  %".71" = zext i32 %".70" to i64
  %".72" = trunc i64 %".71" to i8
  %".73" = zext i8 %".72" to i32
  %".74" = zext i32 %".73" to i64
  %".75" = trunc i64 %".74" to i8
  %".76" = zext i8 %".75" to i64
  %".77" = shl i64 %".76", 56
  %".78" = or i64 %".68", %".77"
  %".79" = zext i8 %".37" to i64
  %".80" = zext i8 %".40" to i64
  %".81" = shl i64 %".80", 8
  %".82" = or i64 %".79", %".81"
  %".83" = zext i8 %".45" to i64
  %".84" = shl i64 %".83", 16
  %".85" = or i64 %".82", %".84"
  %".86" = zext i8 %".50" to i64
  %".87" = shl i64 %".86", 24
  %".88" = or i64 %".85", %".87"
  %".89" = zext i8 %".55" to i64
  %".90" = shl i64 %".89", 32
  %".91" = or i64 %".88", %".90"
  %".92" = zext i8 %".60" to i64
  %".93" = shl i64 %".92", 40
  %".94" = or i64 %".91", %".93"
  %".95" = zext i8 %".65" to i64
  %".96" = shl i64 %".95", 48
  %".97" = or i64 %".94", %".96"
  %".98" = zext i8 %".75" to i64
  %".99" = shl i64 %".98", 56
  %".100" = or i64 %".97", %".99"
  %".101" = and i64 7, %".100"
  %".102" = zext i8 2 to i64
  %".103" = and i64 %".102", 63
  %".104" = shl i64 %".101", %".103"
  %".105" = add i64 %".22", %".22"
  %".106" = add i64 %".105", %".105"
  %".107" = or i64 %".104", %".106"
  %".108" = lshr i64 %".107", 56
  %".109" = trunc i64 %".108" to i8
  %".110" = zext i8 %".109" to i32
  %".111" = zext i32 %".110" to i64
  %".112" = trunc i64 %".111" to i8
  %".113" = zext i8 %".112" to i32
  %".114" = zext i32 %".113" to i64
  %".115" = trunc i64 %".114" to i8
  %".116" = zext i8 %".115" to i32
  %".117" = zext i32 %".116" to i64
  %".118" = trunc i64 %".117" to i8
  %".119" = zext i8 %".118" to i32
  %".120" = zext i32 %".119" to i64
  %".121" = trunc i64 %".120" to i8
  %".122" = zext i8 %".121" to i64
  %".123" = lshr i64 %".107", 8
  %".124" = trunc i64 %".123" to i8
  %".125" = zext i8 %".124" to i64
  %".126" = shl i64 %".125", 8
  %".127" = or i64 %".122", %".126"
  %".128" = lshr i64 %".107", 16
  %".129" = trunc i64 %".128" to i8
  %".130" = zext i8 %".129" to i64
  %".131" = shl i64 %".130", 16
  %".132" = or i64 %".127", %".131"
  %".133" = lshr i64 %".107", 24
  %".134" = trunc i64 %".133" to i8
  %".135" = zext i8 %".134" to i64
  %".136" = shl i64 %".135", 24
  %".137" = or i64 %".132", %".136"
  %".138" = lshr i64 %".107", 32
  %".139" = trunc i64 %".138" to i8
  %".140" = zext i8 %".139" to i64
  %".141" = shl i64 %".140", 32
  %".142" = or i64 %".137", %".141"
  %".143" = lshr i64 %".107", 40
  %".144" = trunc i64 %".143" to i8
  %".145" = zext i8 %".144" to i64
  %".146" = shl i64 %".145", 40
  %".147" = or i64 %".142", %".146"
  %".148" = lshr i64 %".107", 48
  %".149" = trunc i64 %".148" to i8
  %".150" = zext i8 %".149" to i64
  %".151" = shl i64 %".150", 48
  %".152" = or i64 %".147", %".151"
  %".153" = trunc i64 %".107" to i8
  %".154" = zext i8 %".153" to i32
  %".155" = zext i32 %".154" to i64
  %".156" = trunc i64 %".155" to i8
  %".157" = zext i8 %".156" to i32
  %".158" = zext i32 %".157" to i64
  %".159" = trunc i64 %".158" to i8
  %".160" = zext i8 %".159" to i64
  %".161" = shl i64 %".160", 56
  %".162" = or i64 %".152", %".161"
  %".163" = and i64 %".78", %".162"
  %".164" = and i64 31, %".163"
  %".165" = zext i8 4 to i64
  %".166" = and i64 %".165", 63
  %".167" = shl i64 %".164", %".166"
  %".168" = zext i8 %".37" to i64
  %".169" = zext i8 %".40" to i64
  %".170" = shl i64 %".169", 8
  %".171" = or i64 %".168", %".170"
  %".172" = zext i8 %".45" to i64
  %".173" = shl i64 %".172", 16
  %".174" = or i64 %".171", %".173"
  %".175" = zext i8 %".50" to i64
  %".176" = shl i64 %".175", 24
  %".177" = or i64 %".174", %".176"
  %".178" = zext i8 %".55" to i64
  %".179" = shl i64 %".178", 32
  %".180" = or i64 %".177", %".179"
  %".181" = zext i8 %".60" to i64
  %".182" = shl i64 %".181", 40
  %".183" = or i64 %".180", %".182"
  %".184" = zext i8 %".65" to i64
  %".185" = shl i64 %".184", 48
  %".186" = or i64 %".183", %".185"
  %".187" = zext i8 %".75" to i64
  %".188" = shl i64 %".187", 56
  %".189" = or i64 %".186", %".188"
  %".190" = and i64 %".6", %".189"
  %".191" = and i64 31, %".190"
  %".192" = zext i8 4 to i64
  %".193" = and i64 %".192", 63
  %".194" = shl i64 %".191", %".193"
  %".195" = or i64 %".194", %".5"
  %".196" = or i64 %".167", %".195"
  %".197" = zext i8 1 to i64
  %".198" = and i64 %".197", 63
  %".199" = lshr i64 %".6", %".198"
  %".200" = and i64 15, %".199"
  %".201" = or i64 1, %".200"
  %".202" = sub i64 64, %".201"
  %".203" = trunc i64 %".202" to i32
  %".204" = zext i32 %".203" to i64
  %".205" = trunc i64 %".204" to i8
  %".206" = zext i8 %".205" to i64
  %".207" = and i64 %".206", 63
  %".208" = shl i64 %".196", %".207"
  %".209" = zext i8 1 to i64
  %".210" = and i64 %".209", 63
  %".211" = lshr i64 %".6", %".210"
  %".212" = and i64 15, %".211"
  %".213" = or i64 1, %".212"
  %".214" = trunc i64 %".213" to i8
  %".215" = zext i8 %".214" to i64
  %".216" = and i64 %".215", 63
  %".217" = lshr i64 %".196", %".216"
  %".218" = or i64 %".208", %".217"
  %".219" = zext i8 %".121" to i64
  %".220" = zext i8 %".124" to i64
  %".221" = shl i64 %".220", 8
  %".222" = or i64 %".219", %".221"
  %".223" = zext i8 %".129" to i64
  %".224" = shl i64 %".223", 16
  %".225" = or i64 %".222", %".224"
  %".226" = zext i8 %".134" to i64
  %".227" = shl i64 %".226", 24
  %".228" = or i64 %".225", %".227"
  %".229" = zext i8 %".139" to i64
  %".230" = shl i64 %".229", 32
  %".231" = or i64 %".228", %".230"
  %".232" = zext i8 %".144" to i64
  %".233" = shl i64 %".232", 40
  %".234" = or i64 %".231", %".233"
  %".235" = zext i8 %".149" to i64
  %".236" = shl i64 %".235", 48
  %".237" = or i64 %".234", %".236"
  %".238" = zext i8 %".159" to i64
  %".239" = shl i64 %".238", 56
  %".240" = or i64 %".237", %".239"
  %".241" = zext i8 %".37" to i64
  %".242" = zext i8 %".40" to i64
  %".243" = shl i64 %".242", 8
  %".244" = or i64 %".241", %".243"
  %".245" = zext i8 %".45" to i64
  %".246" = shl i64 %".245", 16
  %".247" = or i64 %".244", %".246"
  %".248" = zext i8 %".50" to i64
  %".249" = shl i64 %".248", 24
  %".250" = or i64 %".247", %".249"
  %".251" = zext i8 %".55" to i64
  %".252" = shl i64 %".251", 32
  %".253" = or i64 %".250", %".252"
  %".254" = zext i8 %".60" to i64
  %".255" = shl i64 %".254", 40
  %".256" = or i64 %".253", %".255"
  %".257" = zext i8 %".65" to i64
  %".258" = shl i64 %".257", 48
  %".259" = or i64 %".256", %".258"
  %".260" = zext i8 %".75" to i64
  %".261" = shl i64 %".260", 56
  %".262" = or i64 %".259", %".261"
  %".263" = or i64 %".240", %".262"
  %".264" = and i64 15, %".263"
  %".265" = or i64 1, %".264"
  %".266" = sub i64 64, %".265"
  %".267" = trunc i64 %".266" to i8
  %".268" = zext i8 %".267" to i64
  %".269" = and i64 %".268", 63
  %".270" = lshr i64 %".218", %".269"
  %".271" = zext i8 1 to i64
  %".272" = and i64 %".271", 63
  %".273" = lshr i64 %".6", %".272"
  %".274" = and i64 15, %".273"
  %".275" = or i64 1, %".274"
  %".276" = sub i64 64, %".275"
  %".277" = trunc i64 %".276" to i8
  %".278" = zext i8 %".277" to i64
  %".279" = and i64 %".278", 63
  %".280" = shl i64 %".196", %".279"
  %".281" = zext i8 1 to i64
  %".282" = and i64 %".281", 63
  %".283" = lshr i64 %".6", %".282"
  %".284" = and i64 15, %".283"
  %".285" = or i64 1, %".284"
  %".286" = trunc i64 %".285" to i8
  %".287" = zext i8 %".286" to i64
  %".288" = and i64 %".287", 63
  %".289" = lshr i64 %".196", %".288"
  %".290" = or i64 %".280", %".289"
  %".291" = zext i8 %".121" to i64
  %".292" = zext i8 %".124" to i64
  %".293" = shl i64 %".292", 8
  %".294" = or i64 %".291", %".293"
  %".295" = zext i8 %".129" to i64
  %".296" = shl i64 %".295", 16
  %".297" = or i64 %".294", %".296"
  %".298" = zext i8 %".134" to i64
  %".299" = shl i64 %".298", 24
  %".300" = or i64 %".297", %".299"
  %".301" = zext i8 %".139" to i64
  %".302" = shl i64 %".301", 32
  %".303" = or i64 %".300", %".302"
  %".304" = zext i8 %".144" to i64
  %".305" = shl i64 %".304", 40
  %".306" = or i64 %".303", %".305"
  %".307" = zext i8 %".149" to i64
  %".308" = shl i64 %".307", 48
  %".309" = or i64 %".306", %".308"
  %".310" = zext i8 %".159" to i64
  %".311" = shl i64 %".310", 56
  %".312" = or i64 %".309", %".311"
  %".313" = zext i8 %".37" to i64
  %".314" = zext i8 %".40" to i64
  %".315" = shl i64 %".314", 8
  %".316" = or i64 %".313", %".315"
  %".317" = zext i8 %".45" to i64
  %".318" = shl i64 %".317", 16
  %".319" = or i64 %".316", %".318"
  %".320" = zext i8 %".50" to i64
  %".321" = shl i64 %".320", 24
  %".322" = or i64 %".319", %".321"
  %".323" = zext i8 %".55" to i64
  %".324" = shl i64 %".323", 32
  %".325" = or i64 %".322", %".324"
  %".326" = zext i8 %".60" to i64
  %".327" = shl i64 %".326", 40
  %".328" = or i64 %".325", %".327"
  %".329" = zext i8 %".65" to i64
  %".330" = shl i64 %".329", 48
  %".331" = or i64 %".328", %".330"
  %".332" = zext i8 %".75" to i64
  %".333" = shl i64 %".332", 56
  %".334" = or i64 %".331", %".333"
  %".335" = or i64 %".312", %".334"
  %".336" = and i64 15, %".335"
  %".337" = or i64 1, %".336"
  %".338" = trunc i64 %".337" to i32
  %".339" = zext i32 %".338" to i64
  %".340" = trunc i64 %".339" to i8
  %".341" = zext i8 %".340" to i64
  %".342" = and i64 %".341", 63
  %".343" = shl i64 %".290", %".342"
  %".344" = or i64 %".270", %".343"
  ret i64 %".344"
}
