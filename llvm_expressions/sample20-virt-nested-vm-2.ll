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
  %".38" = zext i8 %".37" to i32
  %".39" = zext i32 %".38" to i64
  %".40" = trunc i64 %".39" to i8
  %".41" = zext i8 %".40" to i32
  %".42" = zext i32 %".41" to i64
  %".43" = trunc i64 %".42" to i8
  %".44" = zext i8 %".43" to i32
  %".45" = zext i32 %".44" to i64
  %".46" = trunc i64 %".45" to i8
  %".47" = zext i8 %".46" to i32
  %".48" = zext i32 %".47" to i64
  %".49" = trunc i64 %".48" to i8
  %".50" = zext i8 %".49" to i64
  %".51" = lshr i64 %".23", 8
  %".52" = trunc i64 %".51" to i8
  %".53" = zext i8 %".52" to i64
  %".54" = shl i64 %".53", 8
  %".55" = or i64 %".50", %".54"
  %".56" = lshr i64 %".23", 16
  %".57" = trunc i64 %".56" to i8
  %".58" = zext i8 %".57" to i64
  %".59" = shl i64 %".58", 16
  %".60" = or i64 %".55", %".59"
  %".61" = lshr i64 %".23", 24
  %".62" = trunc i64 %".61" to i8
  %".63" = zext i8 %".62" to i64
  %".64" = shl i64 %".63", 24
  %".65" = or i64 %".60", %".64"
  %".66" = lshr i64 %".23", 32
  %".67" = trunc i64 %".66" to i8
  %".68" = zext i8 %".67" to i64
  %".69" = shl i64 %".68", 32
  %".70" = or i64 %".65", %".69"
  %".71" = lshr i64 %".23", 40
  %".72" = trunc i64 %".71" to i8
  %".73" = zext i8 %".72" to i64
  %".74" = shl i64 %".73", 40
  %".75" = or i64 %".70", %".74"
  %".76" = lshr i64 %".23", 48
  %".77" = trunc i64 %".76" to i8
  %".78" = zext i8 %".77" to i64
  %".79" = shl i64 %".78", 48
  %".80" = or i64 %".75", %".79"
  %".81" = trunc i64 %".23" to i8
  %".82" = zext i8 %".81" to i32
  %".83" = zext i32 %".82" to i64
  %".84" = trunc i64 %".83" to i8
  %".85" = zext i8 %".84" to i32
  %".86" = zext i32 %".85" to i64
  %".87" = trunc i64 %".86" to i8
  %".88" = zext i8 %".87" to i32
  %".89" = zext i32 %".88" to i64
  %".90" = trunc i64 %".89" to i8
  %".91" = zext i8 %".90" to i32
  %".92" = zext i32 %".91" to i64
  %".93" = trunc i64 %".92" to i8
  %".94" = zext i8 %".93" to i64
  %".95" = shl i64 %".94", 56
  %".96" = or i64 %".80", %".95"
  %".97" = zext i8 %".49" to i64
  %".98" = zext i8 %".52" to i64
  %".99" = shl i64 %".98", 8
  %".100" = or i64 %".97", %".99"
  %".101" = zext i8 %".57" to i64
  %".102" = shl i64 %".101", 16
  %".103" = or i64 %".100", %".102"
  %".104" = zext i8 %".62" to i64
  %".105" = shl i64 %".104", 24
  %".106" = or i64 %".103", %".105"
  %".107" = zext i8 %".67" to i64
  %".108" = shl i64 %".107", 32
  %".109" = or i64 %".106", %".108"
  %".110" = zext i8 %".72" to i64
  %".111" = shl i64 %".110", 40
  %".112" = or i64 %".109", %".111"
  %".113" = zext i8 %".77" to i64
  %".114" = shl i64 %".113", 48
  %".115" = or i64 %".112", %".114"
  %".116" = zext i8 %".93" to i64
  %".117" = shl i64 %".116", 56
  %".118" = or i64 %".115", %".117"
  %".119" = and i64 7, %".118"
  %".120" = zext i8 2 to i64
  %".121" = and i64 %".120", 63
  %".122" = shl i64 %".119", %".121"
  %".123" = add i64 %".22", %".22"
  %".124" = add i64 %".123", %".123"
  %".125" = or i64 %".122", %".124"
  %".126" = lshr i64 %".125", 56
  %".127" = trunc i64 %".126" to i8
  %".128" = zext i8 %".127" to i32
  %".129" = zext i32 %".128" to i64
  %".130" = trunc i64 %".129" to i8
  %".131" = zext i8 %".130" to i32
  %".132" = zext i32 %".131" to i64
  %".133" = trunc i64 %".132" to i8
  %".134" = zext i8 %".133" to i32
  %".135" = zext i32 %".134" to i64
  %".136" = trunc i64 %".135" to i8
  %".137" = zext i8 %".136" to i32
  %".138" = zext i32 %".137" to i64
  %".139" = trunc i64 %".138" to i8
  %".140" = zext i8 %".139" to i32
  %".141" = zext i32 %".140" to i64
  %".142" = trunc i64 %".141" to i8
  %".143" = zext i8 %".142" to i32
  %".144" = zext i32 %".143" to i64
  %".145" = trunc i64 %".144" to i8
  %".146" = zext i8 %".145" to i32
  %".147" = zext i32 %".146" to i64
  %".148" = trunc i64 %".147" to i8
  %".149" = zext i8 %".148" to i32
  %".150" = zext i32 %".149" to i64
  %".151" = trunc i64 %".150" to i8
  %".152" = zext i8 %".151" to i64
  %".153" = lshr i64 %".125", 8
  %".154" = trunc i64 %".153" to i8
  %".155" = zext i8 %".154" to i64
  %".156" = shl i64 %".155", 8
  %".157" = or i64 %".152", %".156"
  %".158" = lshr i64 %".125", 16
  %".159" = trunc i64 %".158" to i8
  %".160" = zext i8 %".159" to i64
  %".161" = shl i64 %".160", 16
  %".162" = or i64 %".157", %".161"
  %".163" = lshr i64 %".125", 24
  %".164" = trunc i64 %".163" to i8
  %".165" = zext i8 %".164" to i64
  %".166" = shl i64 %".165", 24
  %".167" = or i64 %".162", %".166"
  %".168" = lshr i64 %".125", 32
  %".169" = trunc i64 %".168" to i8
  %".170" = zext i8 %".169" to i64
  %".171" = shl i64 %".170", 32
  %".172" = or i64 %".167", %".171"
  %".173" = lshr i64 %".125", 40
  %".174" = trunc i64 %".173" to i8
  %".175" = zext i8 %".174" to i64
  %".176" = shl i64 %".175", 40
  %".177" = or i64 %".172", %".176"
  %".178" = lshr i64 %".125", 48
  %".179" = trunc i64 %".178" to i8
  %".180" = zext i8 %".179" to i64
  %".181" = shl i64 %".180", 48
  %".182" = or i64 %".177", %".181"
  %".183" = trunc i64 %".125" to i8
  %".184" = zext i8 %".183" to i32
  %".185" = zext i32 %".184" to i64
  %".186" = trunc i64 %".185" to i8
  %".187" = zext i8 %".186" to i32
  %".188" = zext i32 %".187" to i64
  %".189" = trunc i64 %".188" to i8
  %".190" = zext i8 %".189" to i32
  %".191" = zext i32 %".190" to i64
  %".192" = trunc i64 %".191" to i8
  %".193" = zext i8 %".192" to i32
  %".194" = zext i32 %".193" to i64
  %".195" = trunc i64 %".194" to i8
  %".196" = zext i8 %".195" to i64
  %".197" = shl i64 %".196", 56
  %".198" = or i64 %".182", %".197"
  %".199" = and i64 %".96", %".198"
  %".200" = and i64 31, %".199"
  %".201" = zext i8 4 to i64
  %".202" = and i64 %".201", 63
  %".203" = shl i64 %".200", %".202"
  %".204" = zext i8 %".49" to i64
  %".205" = zext i8 %".52" to i64
  %".206" = shl i64 %".205", 8
  %".207" = or i64 %".204", %".206"
  %".208" = zext i8 %".57" to i64
  %".209" = shl i64 %".208", 16
  %".210" = or i64 %".207", %".209"
  %".211" = zext i8 %".62" to i64
  %".212" = shl i64 %".211", 24
  %".213" = or i64 %".210", %".212"
  %".214" = zext i8 %".67" to i64
  %".215" = shl i64 %".214", 32
  %".216" = or i64 %".213", %".215"
  %".217" = zext i8 %".72" to i64
  %".218" = shl i64 %".217", 40
  %".219" = or i64 %".216", %".218"
  %".220" = zext i8 %".77" to i64
  %".221" = shl i64 %".220", 48
  %".222" = or i64 %".219", %".221"
  %".223" = zext i8 %".93" to i64
  %".224" = shl i64 %".223", 56
  %".225" = or i64 %".222", %".224"
  %".226" = and i64 %".6", %".225"
  %".227" = and i64 31, %".226"
  %".228" = zext i8 4 to i64
  %".229" = and i64 %".228", 63
  %".230" = shl i64 %".227", %".229"
  %".231" = or i64 %".230", %".5"
  %".232" = or i64 %".203", %".231"
  %".233" = zext i8 1 to i64
  %".234" = and i64 %".233", 63
  %".235" = lshr i64 %".6", %".234"
  %".236" = and i64 15, %".235"
  %".237" = or i64 1, %".236"
  %".238" = sub i64 64, %".237"
  %".239" = trunc i64 %".238" to i8
  %".240" = zext i8 %".239" to i64
  %".241" = and i64 %".240", 63
  %".242" = shl i64 %".232", %".241"
  %".243" = zext i8 1 to i64
  %".244" = and i64 %".243", 63
  %".245" = lshr i64 %".6", %".244"
  %".246" = and i64 15, %".245"
  %".247" = or i64 1, %".246"
  %".248" = trunc i64 %".247" to i32
  %".249" = zext i32 %".248" to i64
  %".250" = trunc i64 %".249" to i8
  %".251" = zext i8 %".250" to i64
  %".252" = and i64 %".251", 63
  %".253" = lshr i64 %".232", %".252"
  %".254" = or i64 %".242", %".253"
  %".255" = zext i8 %".151" to i64
  %".256" = zext i8 %".154" to i64
  %".257" = shl i64 %".256", 8
  %".258" = or i64 %".255", %".257"
  %".259" = zext i8 %".159" to i64
  %".260" = shl i64 %".259", 16
  %".261" = or i64 %".258", %".260"
  %".262" = zext i8 %".164" to i64
  %".263" = shl i64 %".262", 24
  %".264" = or i64 %".261", %".263"
  %".265" = zext i8 %".169" to i64
  %".266" = shl i64 %".265", 32
  %".267" = or i64 %".264", %".266"
  %".268" = zext i8 %".174" to i64
  %".269" = shl i64 %".268", 40
  %".270" = or i64 %".267", %".269"
  %".271" = zext i8 %".179" to i64
  %".272" = shl i64 %".271", 48
  %".273" = or i64 %".270", %".272"
  %".274" = zext i8 %".195" to i64
  %".275" = shl i64 %".274", 56
  %".276" = or i64 %".273", %".275"
  %".277" = zext i8 %".49" to i64
  %".278" = zext i8 %".52" to i64
  %".279" = shl i64 %".278", 8
  %".280" = or i64 %".277", %".279"
  %".281" = zext i8 %".57" to i64
  %".282" = shl i64 %".281", 16
  %".283" = or i64 %".280", %".282"
  %".284" = zext i8 %".62" to i64
  %".285" = shl i64 %".284", 24
  %".286" = or i64 %".283", %".285"
  %".287" = zext i8 %".67" to i64
  %".288" = shl i64 %".287", 32
  %".289" = or i64 %".286", %".288"
  %".290" = zext i8 %".72" to i64
  %".291" = shl i64 %".290", 40
  %".292" = or i64 %".289", %".291"
  %".293" = zext i8 %".77" to i64
  %".294" = shl i64 %".293", 48
  %".295" = or i64 %".292", %".294"
  %".296" = zext i8 %".93" to i64
  %".297" = shl i64 %".296", 56
  %".298" = or i64 %".295", %".297"
  %".299" = or i64 %".276", %".298"
  %".300" = and i64 15, %".299"
  %".301" = or i64 1, %".300"
  %".302" = sub i64 64, %".301"
  %".303" = trunc i64 %".302" to i32
  %".304" = zext i32 %".303" to i64
  %".305" = trunc i64 %".304" to i8
  %".306" = zext i8 %".305" to i64
  %".307" = and i64 %".306", 63
  %".308" = lshr i64 %".254", %".307"
  %".309" = zext i8 1 to i64
  %".310" = and i64 %".309", 63
  %".311" = lshr i64 %".6", %".310"
  %".312" = and i64 15, %".311"
  %".313" = or i64 1, %".312"
  %".314" = sub i64 64, %".313"
  %".315" = trunc i64 %".314" to i8
  %".316" = zext i8 %".315" to i64
  %".317" = and i64 %".316", 63
  %".318" = shl i64 %".232", %".317"
  %".319" = zext i8 1 to i64
  %".320" = and i64 %".319", 63
  %".321" = lshr i64 %".6", %".320"
  %".322" = and i64 15, %".321"
  %".323" = or i64 1, %".322"
  %".324" = trunc i64 %".323" to i32
  %".325" = zext i32 %".324" to i64
  %".326" = trunc i64 %".325" to i8
  %".327" = zext i8 %".326" to i64
  %".328" = and i64 %".327", 63
  %".329" = lshr i64 %".232", %".328"
  %".330" = or i64 %".318", %".329"
  %".331" = zext i8 %".151" to i64
  %".332" = zext i8 %".154" to i64
  %".333" = shl i64 %".332", 8
  %".334" = or i64 %".331", %".333"
  %".335" = zext i8 %".159" to i64
  %".336" = shl i64 %".335", 16
  %".337" = or i64 %".334", %".336"
  %".338" = zext i8 %".164" to i64
  %".339" = shl i64 %".338", 24
  %".340" = or i64 %".337", %".339"
  %".341" = zext i8 %".169" to i64
  %".342" = shl i64 %".341", 32
  %".343" = or i64 %".340", %".342"
  %".344" = zext i8 %".174" to i64
  %".345" = shl i64 %".344", 40
  %".346" = or i64 %".343", %".345"
  %".347" = zext i8 %".179" to i64
  %".348" = shl i64 %".347", 48
  %".349" = or i64 %".346", %".348"
  %".350" = zext i8 %".195" to i64
  %".351" = shl i64 %".350", 56
  %".352" = or i64 %".349", %".351"
  %".353" = zext i8 %".49" to i64
  %".354" = zext i8 %".52" to i64
  %".355" = shl i64 %".354", 8
  %".356" = or i64 %".353", %".355"
  %".357" = zext i8 %".57" to i64
  %".358" = shl i64 %".357", 16
  %".359" = or i64 %".356", %".358"
  %".360" = zext i8 %".62" to i64
  %".361" = shl i64 %".360", 24
  %".362" = or i64 %".359", %".361"
  %".363" = zext i8 %".67" to i64
  %".364" = shl i64 %".363", 32
  %".365" = or i64 %".362", %".364"
  %".366" = zext i8 %".72" to i64
  %".367" = shl i64 %".366", 40
  %".368" = or i64 %".365", %".367"
  %".369" = zext i8 %".77" to i64
  %".370" = shl i64 %".369", 48
  %".371" = or i64 %".368", %".370"
  %".372" = zext i8 %".93" to i64
  %".373" = shl i64 %".372", 56
  %".374" = or i64 %".371", %".373"
  %".375" = or i64 %".352", %".374"
  %".376" = and i64 15, %".375"
  %".377" = or i64 1, %".376"
  %".378" = trunc i64 %".377" to i8
  %".379" = zext i8 %".378" to i64
  %".380" = and i64 %".379", 63
  %".381" = shl i64 %".330", %".380"
  %".382" = or i64 %".308", %".381"
  ret i64 %".382"
}
