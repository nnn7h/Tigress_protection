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
  %".251" = trunc i64 %".250" to i8
  %".252" = zext i8 %".251" to i64
  %".253" = and i64 %".252", 63
  %".254" = shl i64 %".77", %".253"
  %".255" = zext i8 3 to i64
  %".256" = and i64 %".255", 63
  %".257" = lshr i64 %".244", %".256"
  %".258" = and i64 15, %".257"
  %".259" = or i64 1, %".258"
  %".260" = trunc i64 %".259" to i8
  %".261" = zext i8 %".260" to i64
  %".262" = and i64 %".261", 63
  %".263" = lshr i64 %".77", %".262"
  %".264" = or i64 %".254", %".263"
  %".265" = and i64 15, %".264"
  %".266" = zext i8 2 to i64
  %".267" = and i64 %".266", 63
  %".268" = shl i64 %".265", %".267"
  %".269" = lshr i64 %".66", 32
  %".270" = trunc i64 %".269" to i8
  %".271" = zext i8 %".270" to i32
  %".272" = lshr i64 %".66", 40
  %".273" = trunc i64 %".272" to i8
  %".274" = zext i8 %".273" to i32
  %".275" = shl i32 %".274", 8
  %".276" = or i32 %".271", %".275"
  %".277" = lshr i64 %".66", 48
  %".278" = trunc i64 %".277" to i8
  %".279" = zext i8 %".278" to i32
  %".280" = shl i32 %".279", 16
  %".281" = or i32 %".276", %".280"
  %".282" = lshr i64 %".66", 56
  %".283" = trunc i64 %".282" to i8
  %".284" = zext i8 %".283" to i32
  %".285" = shl i32 %".284", 24
  %".286" = or i32 %".281", %".285"
  %".287" = zext i32 %".286" to i64
  %".288" = trunc i64 %".287" to i32
  %".289" = zext i32 %".288" to i64
  %".290" = trunc i64 %".289" to i32
  %".291" = zext i32 %".290" to i64
  %".292" = trunc i64 %".291" to i32
  %".293" = zext i32 %".292" to i64
  %".294" = trunc i64 %".293" to i32
  %".295" = trunc i32 %".294" to i8
  %".296" = zext i8 %".295" to i64
  %".297" = trunc i64 %".293" to i32
  %".298" = lshr i32 %".297", 8
  %".299" = trunc i32 %".298" to i8
  %".300" = zext i8 %".299" to i64
  %".301" = shl i64 %".300", 8
  %".302" = or i64 %".296", %".301"
  %".303" = trunc i64 %".293" to i32
  %".304" = lshr i32 %".303", 16
  %".305" = trunc i32 %".304" to i8
  %".306" = zext i8 %".305" to i64
  %".307" = shl i64 %".306", 16
  %".308" = or i64 %".302", %".307"
  %".309" = trunc i64 %".293" to i32
  %".310" = lshr i32 %".309", 24
  %".311" = trunc i32 %".310" to i8
  %".312" = zext i8 %".311" to i64
  %".313" = shl i64 %".312", 24
  %".314" = or i64 %".308", %".313"
  %".315" = trunc i64 %".66" to i8
  %".316" = zext i8 %".315" to i32
  %".317" = lshr i64 %".66", 8
  %".318" = trunc i64 %".317" to i8
  %".319" = zext i8 %".318" to i32
  %".320" = shl i32 %".319", 8
  %".321" = or i32 %".316", %".320"
  %".322" = lshr i64 %".66", 16
  %".323" = trunc i64 %".322" to i8
  %".324" = zext i8 %".323" to i32
  %".325" = shl i32 %".324", 16
  %".326" = or i32 %".321", %".325"
  %".327" = lshr i64 %".66", 24
  %".328" = trunc i64 %".327" to i8
  %".329" = zext i8 %".328" to i32
  %".330" = shl i32 %".329", 24
  %".331" = or i32 %".326", %".330"
  %".332" = zext i32 %".331" to i64
  %".333" = trunc i64 %".332" to i32
  %".334" = zext i32 %".333" to i64
  %".335" = trunc i64 %".334" to i32
  %".336" = trunc i32 %".335" to i8
  %".337" = zext i8 %".336" to i64
  %".338" = shl i64 %".337", 32
  %".339" = or i64 %".314", %".338"
  %".340" = trunc i64 %".334" to i32
  %".341" = lshr i32 %".340", 8
  %".342" = trunc i32 %".341" to i8
  %".343" = zext i8 %".342" to i64
  %".344" = shl i64 %".343", 40
  %".345" = or i64 %".339", %".344"
  %".346" = trunc i64 %".334" to i32
  %".347" = lshr i32 %".346", 16
  %".348" = trunc i32 %".347" to i8
  %".349" = zext i8 %".348" to i64
  %".350" = shl i64 %".349", 48
  %".351" = or i64 %".345", %".350"
  %".352" = trunc i64 %".334" to i32
  %".353" = lshr i32 %".352", 24
  %".354" = trunc i32 %".353" to i8
  %".355" = zext i8 %".354" to i64
  %".356" = shl i64 %".355", 56
  %".357" = or i64 %".351", %".356"
  %".358" = or i64 %".268", %".357"
  %".359" = or i64 %".77", %".358"
  %".360" = zext i8 %".91" to i64
  %".361" = zext i8 %".94" to i64
  %".362" = shl i64 %".361", 8
  %".363" = or i64 %".360", %".362"
  %".364" = zext i8 %".99" to i64
  %".365" = shl i64 %".364", 16
  %".366" = or i64 %".363", %".365"
  %".367" = zext i8 %".104" to i64
  %".368" = shl i64 %".367", 24
  %".369" = or i64 %".366", %".368"
  %".370" = zext i8 %".121" to i64
  %".371" = shl i64 %".370", 32
  %".372" = or i64 %".369", %".371"
  %".373" = zext i8 %".132" to i64
  %".374" = shl i64 %".373", 40
  %".375" = or i64 %".372", %".374"
  %".376" = zext i8 %".142" to i64
  %".377" = shl i64 %".376", 48
  %".378" = or i64 %".375", %".377"
  %".379" = zext i8 %".147" to i64
  %".380" = shl i64 %".379", 56
  %".381" = or i64 %".378", %".380"
  %".382" = zext i8 3 to i64
  %".383" = and i64 %".382", 63
  %".384" = lshr i64 %".244", %".383"
  %".385" = and i64 7, %".384"
  %".386" = or i64 1, %".385"
  %".387" = trunc i64 %".386" to i8
  %".388" = zext i8 %".387" to i64
  %".389" = and i64 %".388", 63
  %".390" = shl i64 %".381", %".389"
  %".391" = or i64 %".359", %".390"
  ret i64 %".391"
}
