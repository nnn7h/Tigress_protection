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
  %".214" = trunc i64 %".213" to i32
  %".215" = zext i32 %".214" to i64
  %".216" = trunc i64 %".215" to i8
  %".217" = zext i8 %".216" to i64
  %".218" = and i64 %".217", 63
  %".219" = lshr i64 %".196", %".218"
  %".220" = or i64 %".208", %".219"
  %".221" = zext i8 %".121" to i64
  %".222" = zext i8 %".124" to i64
  %".223" = shl i64 %".222", 8
  %".224" = or i64 %".221", %".223"
  %".225" = zext i8 %".129" to i64
  %".226" = shl i64 %".225", 16
  %".227" = or i64 %".224", %".226"
  %".228" = zext i8 %".134" to i64
  %".229" = shl i64 %".228", 24
  %".230" = or i64 %".227", %".229"
  %".231" = zext i8 %".139" to i64
  %".232" = shl i64 %".231", 32
  %".233" = or i64 %".230", %".232"
  %".234" = zext i8 %".144" to i64
  %".235" = shl i64 %".234", 40
  %".236" = or i64 %".233", %".235"
  %".237" = zext i8 %".149" to i64
  %".238" = shl i64 %".237", 48
  %".239" = or i64 %".236", %".238"
  %".240" = zext i8 %".159" to i64
  %".241" = shl i64 %".240", 56
  %".242" = or i64 %".239", %".241"
  %".243" = zext i8 %".37" to i64
  %".244" = zext i8 %".40" to i64
  %".245" = shl i64 %".244", 8
  %".246" = or i64 %".243", %".245"
  %".247" = zext i8 %".45" to i64
  %".248" = shl i64 %".247", 16
  %".249" = or i64 %".246", %".248"
  %".250" = zext i8 %".50" to i64
  %".251" = shl i64 %".250", 24
  %".252" = or i64 %".249", %".251"
  %".253" = zext i8 %".55" to i64
  %".254" = shl i64 %".253", 32
  %".255" = or i64 %".252", %".254"
  %".256" = zext i8 %".60" to i64
  %".257" = shl i64 %".256", 40
  %".258" = or i64 %".255", %".257"
  %".259" = zext i8 %".65" to i64
  %".260" = shl i64 %".259", 48
  %".261" = or i64 %".258", %".260"
  %".262" = zext i8 %".75" to i64
  %".263" = shl i64 %".262", 56
  %".264" = or i64 %".261", %".263"
  %".265" = or i64 %".242", %".264"
  %".266" = and i64 15, %".265"
  %".267" = or i64 1, %".266"
  %".268" = sub i64 64, %".267"
  %".269" = trunc i64 %".268" to i32
  %".270" = zext i32 %".269" to i64
  %".271" = trunc i64 %".270" to i8
  %".272" = zext i8 %".271" to i64
  %".273" = and i64 %".272", 63
  %".274" = lshr i64 %".220", %".273"
  %".275" = zext i8 1 to i64
  %".276" = and i64 %".275", 63
  %".277" = lshr i64 %".6", %".276"
  %".278" = and i64 15, %".277"
  %".279" = or i64 1, %".278"
  %".280" = sub i64 64, %".279"
  %".281" = trunc i64 %".280" to i32
  %".282" = zext i32 %".281" to i64
  %".283" = trunc i64 %".282" to i8
  %".284" = zext i8 %".283" to i64
  %".285" = and i64 %".284", 63
  %".286" = shl i64 %".196", %".285"
  %".287" = zext i8 1 to i64
  %".288" = and i64 %".287", 63
  %".289" = lshr i64 %".6", %".288"
  %".290" = and i64 15, %".289"
  %".291" = or i64 1, %".290"
  %".292" = trunc i64 %".291" to i32
  %".293" = zext i32 %".292" to i64
  %".294" = trunc i64 %".293" to i8
  %".295" = zext i8 %".294" to i64
  %".296" = and i64 %".295", 63
  %".297" = lshr i64 %".196", %".296"
  %".298" = or i64 %".286", %".297"
  %".299" = zext i8 %".121" to i64
  %".300" = zext i8 %".124" to i64
  %".301" = shl i64 %".300", 8
  %".302" = or i64 %".299", %".301"
  %".303" = zext i8 %".129" to i64
  %".304" = shl i64 %".303", 16
  %".305" = or i64 %".302", %".304"
  %".306" = zext i8 %".134" to i64
  %".307" = shl i64 %".306", 24
  %".308" = or i64 %".305", %".307"
  %".309" = zext i8 %".139" to i64
  %".310" = shl i64 %".309", 32
  %".311" = or i64 %".308", %".310"
  %".312" = zext i8 %".144" to i64
  %".313" = shl i64 %".312", 40
  %".314" = or i64 %".311", %".313"
  %".315" = zext i8 %".149" to i64
  %".316" = shl i64 %".315", 48
  %".317" = or i64 %".314", %".316"
  %".318" = zext i8 %".159" to i64
  %".319" = shl i64 %".318", 56
  %".320" = or i64 %".317", %".319"
  %".321" = zext i8 %".37" to i64
  %".322" = zext i8 %".40" to i64
  %".323" = shl i64 %".322", 8
  %".324" = or i64 %".321", %".323"
  %".325" = zext i8 %".45" to i64
  %".326" = shl i64 %".325", 16
  %".327" = or i64 %".324", %".326"
  %".328" = zext i8 %".50" to i64
  %".329" = shl i64 %".328", 24
  %".330" = or i64 %".327", %".329"
  %".331" = zext i8 %".55" to i64
  %".332" = shl i64 %".331", 32
  %".333" = or i64 %".330", %".332"
  %".334" = zext i8 %".60" to i64
  %".335" = shl i64 %".334", 40
  %".336" = or i64 %".333", %".335"
  %".337" = zext i8 %".65" to i64
  %".338" = shl i64 %".337", 48
  %".339" = or i64 %".336", %".338"
  %".340" = zext i8 %".75" to i64
  %".341" = shl i64 %".340", 56
  %".342" = or i64 %".339", %".341"
  %".343" = or i64 %".320", %".342"
  %".344" = and i64 15, %".343"
  %".345" = or i64 1, %".344"
  %".346" = trunc i64 %".345" to i32
  %".347" = zext i32 %".346" to i64
  %".348" = trunc i64 %".347" to i8
  %".349" = zext i8 %".348" to i64
  %".350" = and i64 %".349", 63
  %".351" = shl i64 %".298", %".350"
  %".352" = or i64 %".274", %".351"
  ret i64 %".352"
}
