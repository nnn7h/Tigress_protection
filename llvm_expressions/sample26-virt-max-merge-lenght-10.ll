; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = zext i8 5 to i64
  %".5" = and i64 %".4", 63
  %".6" = lshr i64 %"SymVar_0", %".5"
  %".7" = and i64 87652534112836074, %".6"
  %".8" = and i64 117850039, %".7"
  %".9" = or i64 441848546, %"SymVar_0"
  %".10" = add i64 %".8", %".9"
  %".11" = and i64 15, %".10"
  %".12" = zext i8 3 to i64
  %".13" = and i64 %".12", 63
  %".14" = shl i64 %".11", %".13"
  %".15" = and i64 15, %".10"
  %".16" = zext i8 3 to i64
  %".17" = and i64 %".16", 63
  %".18" = shl i64 %".15", %".17"
  %".19" = sub i64 %"SymVar_0", 63267836
  %".20" = or i64 %".18", %".19"
  %".21" = or i64 %".14", %".20"
  %".22" = and i64 15, %".21"
  %".23" = zext i8 3 to i64
  %".24" = and i64 %".23", 63
  %".25" = shl i64 %".22", %".24"
  %".26" = or i64 %".25", %".21"
  %".27" = and i64 31, %".26"
  %".28" = zext i8 3 to i64
  %".29" = and i64 %".28", 63
  %".30" = shl i64 %".27", %".29"
  %".31" = and i64 31, %".20"
  %".32" = zext i8 3 to i64
  %".33" = and i64 %".32", 63
  %".34" = shl i64 %".31", %".33"
  %".35" = sub i64 %"SymVar_0", 43022659
  %".36" = zext i8 3 to i64
  %".37" = and i64 %".36", 63
  %".38" = lshr i64 %".10", %".37"
  %".39" = and i64 15, %".38"
  %".40" = or i64 1, %".39"
  %".41" = sub i64 64, %".40"
  %".42" = trunc i64 %".41" to i8
  %".43" = zext i8 %".42" to i64
  %".44" = and i64 %".43", 63
  %".45" = lshr i64 828565327, %".44"
  %".46" = zext i8 3 to i64
  %".47" = and i64 %".46", 63
  %".48" = lshr i64 %".10", %".47"
  %".49" = and i64 15, %".48"
  %".50" = or i64 1, %".49"
  %".51" = trunc i64 %".50" to i8
  %".52" = zext i8 %".51" to i64
  %".53" = and i64 %".52", 63
  %".54" = shl i64 828565327, %".53"
  %".55" = or i64 %".45", %".54"
  %".56" = zext i8 4 to i64
  %".57" = and i64 %".56", 63
  %".58" = lshr i64 %".55", %".57"
  %".59" = and i64 7, %".58"
  %".60" = or i64 1, %".59"
  %".61" = trunc i64 %".60" to i8
  %".62" = zext i8 %".61" to i64
  %".63" = and i64 %".62", 63
  %".64" = shl i64 %".35", %".63"
  %".65" = or i64 %".34", %".64"
  %".66" = or i64 %".30", %".65"
  %".67" = add i64 %".66", %".66"
  %".68" = and i64 7, %".67"
  %".69" = zext i8 2 to i64
  %".70" = and i64 %".69", 63
  %".71" = shl i64 %".68", %".70"
  %".72" = and i64 15, %".26"
  %".73" = zext i8 3 to i64
  %".74" = and i64 %".73", 63
  %".75" = shl i64 %".72", %".74"
  %".76" = or i64 %".75", %".26"
  %".77" = or i64 %".71", %".76"
  %".78" = lshr i64 %".7", 48
  %".79" = trunc i64 %".78" to i8
  %".80" = zext i8 %".79" to i32
  %".81" = zext i32 %".80" to i64
  %".82" = trunc i64 %".81" to i8
  %".83" = zext i8 %".82" to i32
  %".84" = zext i32 %".83" to i64
  %".85" = trunc i64 %".84" to i8
  %".86" = zext i8 %".85" to i32
  %".87" = zext i32 %".86" to i64
  %".88" = trunc i64 %".87" to i8
  %".89" = zext i8 %".88" to i32
  %".90" = zext i32 %".89" to i64
  %".91" = trunc i64 %".90" to i8
  %".92" = zext i8 %".91" to i64
  %".93" = lshr i64 %".7", 8
  %".94" = trunc i64 %".93" to i8
  %".95" = zext i8 %".94" to i64
  %".96" = shl i64 %".95", 8
  %".97" = or i64 %".92", %".96"
  %".98" = lshr i64 %".7", 16
  %".99" = trunc i64 %".98" to i8
  %".100" = zext i8 %".99" to i64
  %".101" = shl i64 %".100", 16
  %".102" = or i64 %".97", %".101"
  %".103" = lshr i64 %".7", 24
  %".104" = trunc i64 %".103" to i8
  %".105" = zext i8 %".104" to i64
  %".106" = shl i64 %".105", 24
  %".107" = or i64 %".102", %".106"
  %".108" = lshr i64 %".7", 40
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
  %".123" = shl i64 %".122", 32
  %".124" = or i64 %".107", %".123"
  %".125" = lshr i64 %".7", 32
  %".126" = trunc i64 %".125" to i8
  %".127" = zext i8 %".126" to i32
  %".128" = zext i32 %".127" to i64
  %".129" = trunc i64 %".128" to i8
  %".130" = zext i8 %".129" to i32
  %".131" = zext i32 %".130" to i64
  %".132" = trunc i64 %".131" to i8
  %".133" = zext i8 %".132" to i64
  %".134" = shl i64 %".133", 40
  %".135" = or i64 %".124", %".134"
  %".136" = trunc i64 %".7" to i8
  %".137" = zext i8 %".136" to i32
  %".138" = zext i32 %".137" to i64
  %".139" = trunc i64 %".138" to i8
  %".140" = zext i8 %".139" to i32
  %".141" = zext i32 %".140" to i64
  %".142" = trunc i64 %".141" to i8
  %".143" = zext i8 %".142" to i64
  %".144" = shl i64 %".143", 48
  %".145" = or i64 %".135", %".144"
  %".146" = lshr i64 %".7", 56
  %".147" = trunc i64 %".146" to i8
  %".148" = zext i8 %".147" to i64
  %".149" = shl i64 %".148", 56
  %".150" = or i64 %".145", %".149"
  %".151" = and i64 63, %".150"
  %".152" = zext i8 4 to i64
  %".153" = and i64 %".152", 63
  %".154" = shl i64 %".151", %".153"
  %".155" = lshr i64 %".10", 32
  %".156" = trunc i64 %".155" to i8
  %".157" = zext i8 %".156" to i32
  %".158" = lshr i64 %".10", 40
  %".159" = trunc i64 %".158" to i8
  %".160" = zext i8 %".159" to i32
  %".161" = shl i32 %".160", 8
  %".162" = or i32 %".157", %".161"
  %".163" = lshr i64 %".10", 48
  %".164" = trunc i64 %".163" to i8
  %".165" = zext i8 %".164" to i32
  %".166" = shl i32 %".165", 16
  %".167" = or i32 %".162", %".166"
  %".168" = lshr i64 %".10", 56
  %".169" = trunc i64 %".168" to i8
  %".170" = zext i8 %".169" to i32
  %".171" = shl i32 %".170", 24
  %".172" = or i32 %".167", %".171"
  %".173" = zext i32 %".172" to i64
  %".174" = trunc i64 %".173" to i32
  %".175" = zext i32 %".174" to i64
  %".176" = trunc i64 %".175" to i32
  %".177" = trunc i32 %".176" to i8
  %".178" = zext i8 %".177" to i64
  %".179" = trunc i64 %".175" to i32
  %".180" = lshr i32 %".179", 8
  %".181" = trunc i32 %".180" to i8
  %".182" = zext i8 %".181" to i64
  %".183" = shl i64 %".182", 8
  %".184" = or i64 %".178", %".183"
  %".185" = trunc i64 %".175" to i32
  %".186" = lshr i32 %".185", 16
  %".187" = trunc i32 %".186" to i8
  %".188" = zext i8 %".187" to i64
  %".189" = shl i64 %".188", 16
  %".190" = or i64 %".184", %".189"
  %".191" = trunc i64 %".175" to i32
  %".192" = lshr i32 %".191", 24
  %".193" = trunc i32 %".192" to i8
  %".194" = zext i8 %".193" to i64
  %".195" = shl i64 %".194", 24
  %".196" = or i64 %".190", %".195"
  %".197" = trunc i64 %".10" to i8
  %".198" = zext i8 %".197" to i32
  %".199" = lshr i64 %".10", 8
  %".200" = trunc i64 %".199" to i8
  %".201" = zext i8 %".200" to i32
  %".202" = shl i32 %".201", 8
  %".203" = or i32 %".198", %".202"
  %".204" = lshr i64 %".10", 16
  %".205" = trunc i64 %".204" to i8
  %".206" = zext i8 %".205" to i32
  %".207" = shl i32 %".206", 16
  %".208" = or i32 %".203", %".207"
  %".209" = lshr i64 %".10", 24
  %".210" = trunc i64 %".209" to i8
  %".211" = zext i8 %".210" to i32
  %".212" = shl i32 %".211", 24
  %".213" = or i32 %".208", %".212"
  %".214" = zext i32 %".213" to i64
  %".215" = trunc i64 %".214" to i32
  %".216" = zext i32 %".215" to i64
  %".217" = trunc i64 %".216" to i32
  %".218" = zext i32 %".217" to i64
  %".219" = trunc i64 %".218" to i32
  %".220" = zext i32 %".219" to i64
  %".221" = trunc i64 %".220" to i32
  %".222" = trunc i32 %".221" to i8
  %".223" = zext i8 %".222" to i64
  %".224" = shl i64 %".223", 32
  %".225" = or i64 %".196", %".224"
  %".226" = trunc i64 %".220" to i32
  %".227" = lshr i32 %".226", 8
  %".228" = trunc i32 %".227" to i8
  %".229" = zext i8 %".228" to i64
  %".230" = shl i64 %".229", 40
  %".231" = or i64 %".225", %".230"
  %".232" = trunc i64 %".220" to i32
  %".233" = lshr i32 %".232", 16
  %".234" = trunc i32 %".233" to i8
  %".235" = zext i8 %".234" to i64
  %".236" = shl i64 %".235", 48
  %".237" = or i64 %".231", %".236"
  %".238" = trunc i64 %".220" to i32
  %".239" = lshr i32 %".238", 24
  %".240" = trunc i32 %".239" to i8
  %".241" = zext i8 %".240" to i64
  %".242" = shl i64 %".241", 56
  %".243" = or i64 %".237", %".242"
  %".244" = or i64 %".154", %".243"
  %".245" = zext i8 3 to i64
  %".246" = and i64 %".245", 63
  %".247" = lshr i64 %".244", %".246"
  %".248" = and i64 15, %".247"
  %".249" = or i64 1, %".248"
  %".250" = sub i64 64, %".249"
  %".251" = trunc i64 %".250" to i32
  %".252" = zext i32 %".251" to i64
  %".253" = trunc i64 %".252" to i8
  %".254" = zext i8 %".253" to i64
  %".255" = and i64 %".254", 63
  %".256" = shl i64 %".77", %".255"
  %".257" = zext i8 3 to i64
  %".258" = and i64 %".257", 63
  %".259" = lshr i64 %".244", %".258"
  %".260" = and i64 15, %".259"
  %".261" = or i64 1, %".260"
  %".262" = trunc i64 %".261" to i8
  %".263" = zext i8 %".262" to i64
  %".264" = and i64 %".263", 63
  %".265" = lshr i64 %".77", %".264"
  %".266" = or i64 %".256", %".265"
  %".267" = and i64 15, %".266"
  %".268" = zext i8 2 to i64
  %".269" = and i64 %".268", 63
  %".270" = shl i64 %".267", %".269"
  %".271" = lshr i64 %".66", 32
  %".272" = trunc i64 %".271" to i8
  %".273" = zext i8 %".272" to i32
  %".274" = lshr i64 %".66", 40
  %".275" = trunc i64 %".274" to i8
  %".276" = zext i8 %".275" to i32
  %".277" = shl i32 %".276", 8
  %".278" = or i32 %".273", %".277"
  %".279" = lshr i64 %".66", 48
  %".280" = trunc i64 %".279" to i8
  %".281" = zext i8 %".280" to i32
  %".282" = shl i32 %".281", 16
  %".283" = or i32 %".278", %".282"
  %".284" = lshr i64 %".66", 56
  %".285" = trunc i64 %".284" to i8
  %".286" = zext i8 %".285" to i32
  %".287" = shl i32 %".286", 24
  %".288" = or i32 %".283", %".287"
  %".289" = zext i32 %".288" to i64
  %".290" = trunc i64 %".289" to i32
  %".291" = zext i32 %".290" to i64
  %".292" = trunc i64 %".291" to i32
  %".293" = zext i32 %".292" to i64
  %".294" = trunc i64 %".293" to i32
  %".295" = zext i32 %".294" to i64
  %".296" = trunc i64 %".295" to i32
  %".297" = trunc i32 %".296" to i8
  %".298" = zext i8 %".297" to i64
  %".299" = trunc i64 %".295" to i32
  %".300" = lshr i32 %".299", 8
  %".301" = trunc i32 %".300" to i8
  %".302" = zext i8 %".301" to i64
  %".303" = shl i64 %".302", 8
  %".304" = or i64 %".298", %".303"
  %".305" = trunc i64 %".295" to i32
  %".306" = lshr i32 %".305", 16
  %".307" = trunc i32 %".306" to i8
  %".308" = zext i8 %".307" to i64
  %".309" = shl i64 %".308", 16
  %".310" = or i64 %".304", %".309"
  %".311" = trunc i64 %".295" to i32
  %".312" = lshr i32 %".311", 24
  %".313" = trunc i32 %".312" to i8
  %".314" = zext i8 %".313" to i64
  %".315" = shl i64 %".314", 24
  %".316" = or i64 %".310", %".315"
  %".317" = trunc i64 %".66" to i8
  %".318" = zext i8 %".317" to i32
  %".319" = lshr i64 %".66", 8
  %".320" = trunc i64 %".319" to i8
  %".321" = zext i8 %".320" to i32
  %".322" = shl i32 %".321", 8
  %".323" = or i32 %".318", %".322"
  %".324" = lshr i64 %".66", 16
  %".325" = trunc i64 %".324" to i8
  %".326" = zext i8 %".325" to i32
  %".327" = shl i32 %".326", 16
  %".328" = or i32 %".323", %".327"
  %".329" = lshr i64 %".66", 24
  %".330" = trunc i64 %".329" to i8
  %".331" = zext i8 %".330" to i32
  %".332" = shl i32 %".331", 24
  %".333" = or i32 %".328", %".332"
  %".334" = zext i32 %".333" to i64
  %".335" = trunc i64 %".334" to i32
  %".336" = zext i32 %".335" to i64
  %".337" = trunc i64 %".336" to i32
  %".338" = trunc i32 %".337" to i8
  %".339" = zext i8 %".338" to i64
  %".340" = shl i64 %".339", 32
  %".341" = or i64 %".316", %".340"
  %".342" = trunc i64 %".336" to i32
  %".343" = lshr i32 %".342", 8
  %".344" = trunc i32 %".343" to i8
  %".345" = zext i8 %".344" to i64
  %".346" = shl i64 %".345", 40
  %".347" = or i64 %".341", %".346"
  %".348" = trunc i64 %".336" to i32
  %".349" = lshr i32 %".348", 16
  %".350" = trunc i32 %".349" to i8
  %".351" = zext i8 %".350" to i64
  %".352" = shl i64 %".351", 48
  %".353" = or i64 %".347", %".352"
  %".354" = trunc i64 %".336" to i32
  %".355" = lshr i32 %".354", 24
  %".356" = trunc i32 %".355" to i8
  %".357" = zext i8 %".356" to i64
  %".358" = shl i64 %".357", 56
  %".359" = or i64 %".353", %".358"
  %".360" = or i64 %".270", %".359"
  %".361" = or i64 %".77", %".360"
  %".362" = zext i8 %".91" to i64
  %".363" = zext i8 %".94" to i64
  %".364" = shl i64 %".363", 8
  %".365" = or i64 %".362", %".364"
  %".366" = zext i8 %".99" to i64
  %".367" = shl i64 %".366", 16
  %".368" = or i64 %".365", %".367"
  %".369" = zext i8 %".104" to i64
  %".370" = shl i64 %".369", 24
  %".371" = or i64 %".368", %".370"
  %".372" = zext i8 %".121" to i64
  %".373" = shl i64 %".372", 32
  %".374" = or i64 %".371", %".373"
  %".375" = zext i8 %".132" to i64
  %".376" = shl i64 %".375", 40
  %".377" = or i64 %".374", %".376"
  %".378" = zext i8 %".142" to i64
  %".379" = shl i64 %".378", 48
  %".380" = or i64 %".377", %".379"
  %".381" = zext i8 %".147" to i64
  %".382" = shl i64 %".381", 56
  %".383" = or i64 %".380", %".382"
  %".384" = zext i8 3 to i64
  %".385" = and i64 %".384", 63
  %".386" = lshr i64 %".244", %".385"
  %".387" = and i64 7, %".386"
  %".388" = or i64 1, %".387"
  %".389" = trunc i64 %".388" to i32
  %".390" = zext i32 %".389" to i64
  %".391" = trunc i64 %".390" to i8
  %".392" = zext i8 %".391" to i64
  %".393" = and i64 %".392", 63
  %".394" = shl i64 %".383", %".393"
  %".395" = or i64 %".361", %".394"
  ret i64 %".395"
}
