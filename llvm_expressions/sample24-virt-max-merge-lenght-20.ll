; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = zext i8 53 to i64
  %".5" = and i64 %".4", 63
  %".6" = lshr i64 %"SymVar_0", %".5"
  %".7" = zext i8 11 to i64
  %".8" = and i64 %".7", 63
  %".9" = shl i64 %"SymVar_0", %".8"
  %".10" = or i64 %".6", %".9"
  %".11" = zext i8 1 to i64
  %".12" = and i64 %".11", 63
  %".13" = lshr i64 %".10", %".12"
  %".14" = zext i64 %"SymVar_0" to i128
  %".15" = zext i64 0 to i128
  %".16" = shl i128 %".15", 64
  %".17" = or i128 %".14", %".16"
  %".18" = zext i64 3 to i128
  %".19" = udiv i128 %".17", %".18"
  %".20" = trunc i128 %".19" to i64
  %".21" = sext i64 112410438 to i128
  %".22" = sext i64 %".13" to i128
  %".23" = mul i128 %".21", %".22"
  %".24" = trunc i128 %".23" to i64
  %".25" = sub i64 %".20", %".24"
  %".26" = zext i8 3 to i64
  %".27" = and i64 %".26", 63
  %".28" = lshr i64 %".25", %".27"
  %".29" = and i64 15, %".28"
  %".30" = or i64 1, %".29"
  %".31" = sub i64 64, %".30"
  %".32" = trunc i64 %".31" to i32
  %".33" = zext i32 %".32" to i64
  %".34" = trunc i64 %".33" to i8
  %".35" = zext i8 %".34" to i64
  %".36" = and i64 %".35", 63
  %".37" = shl i64 %".13", %".36"
  %".38" = zext i8 3 to i64
  %".39" = and i64 %".38", 63
  %".40" = lshr i64 %".25", %".39"
  %".41" = and i64 15, %".40"
  %".42" = or i64 1, %".41"
  %".43" = trunc i64 %".42" to i32
  %".44" = zext i32 %".43" to i64
  %".45" = trunc i64 %".44" to i8
  %".46" = zext i8 %".45" to i64
  %".47" = and i64 %".46", 63
  %".48" = lshr i64 %".13", %".47"
  %".49" = or i64 %".37", %".48"
  %".50" = zext i8 2 to i64
  %".51" = and i64 %".50", 63
  %".52" = lshr i64 %".25", %".51"
  %".53" = and i64 15, %".52"
  %".54" = or i64 1, %".53"
  %".55" = sub i64 64, %".54"
  %".56" = trunc i64 %".55" to i32
  %".57" = zext i32 %".56" to i64
  %".58" = trunc i64 %".57" to i8
  %".59" = zext i8 %".58" to i64
  %".60" = and i64 %".59", 63
  %".61" = lshr i64 %".13", %".60"
  %".62" = zext i8 2 to i64
  %".63" = and i64 %".62", 63
  %".64" = lshr i64 %".25", %".63"
  %".65" = and i64 15, %".64"
  %".66" = or i64 1, %".65"
  %".67" = trunc i64 %".66" to i8
  %".68" = zext i8 %".67" to i64
  %".69" = and i64 %".68", 63
  %".70" = shl i64 %".13", %".69"
  %".71" = or i64 %".61", %".70"
  %".72" = and i64 7, %".71"
  %".73" = zext i8 2 to i64
  %".74" = and i64 %".73", 63
  %".75" = shl i64 %".72", %".74"
  %".76" = add i64 160536708, %"SymVar_0"
  %".77" = zext i8 7 to i64
  %".78" = and i64 %".77", 63
  %".79" = lshr i64 %".25", %".78"
  %".80" = zext i8 2 to i64
  %".81" = and i64 %".80", 63
  %".82" = lshr i64 %".79", %".81"
  %".83" = and i64 7, %".82"
  %".84" = or i64 1, %".83"
  %".85" = trunc i64 %".84" to i8
  %".86" = zext i8 %".85" to i64
  %".87" = and i64 %".86", 63
  %".88" = lshr i64 %".76", %".87"
  %".89" = and i64 63, %".88"
  %".90" = zext i8 4 to i64
  %".91" = and i64 %".90", 63
  %".92" = shl i64 %".89", %".91"
  %".93" = or i64 %".92", %".88"
  %".94" = or i64 %".75", %".93"
  %".95" = add i64 8152287480, %"SymVar_0"
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
  %".107" = shl i64 %".94", %".106"
  %".108" = zext i8 4 to i64
  %".109" = and i64 %".108", 63
  %".110" = lshr i64 %".95", %".109"
  %".111" = and i64 15, %".110"
  %".112" = or i64 1, %".111"
  %".113" = trunc i64 %".112" to i32
  %".114" = zext i32 %".113" to i64
  %".115" = trunc i64 %".114" to i8
  %".116" = zext i8 %".115" to i64
  %".117" = and i64 %".116", 63
  %".118" = lshr i64 %".94", %".117"
  %".119" = or i64 %".107", %".118"
  %".120" = sub i64 %".49", %".119"
  %".121" = xor i64 %".119", %".120"
  %".122" = xor i64 %".49", %".121"
  %".123" = xor i64 %".49", %".120"
  %".124" = xor i64 %".49", %".119"
  %".125" = and i64 %".123", %".124"
  %".126" = xor i64 %".122", %".125"
  %".127" = lshr i64 %".126", 63
  %".128" = trunc i64 %".127" to i1
  %".129" = xor i1 %".128", -1
  %".130" = icmp eq i64 %".120", 0
  br i1 %".130", label %".3.if", label %".3.else"
.3.if:
  br label %".3.endif"
.3.else:
  br label %".3.endif"
.3.endif:
  %".134" = phi i1 [1, %".3.if"], [0, %".3.else"]
  %".135" = xor i1 %".134", -1
  %".136" = and i1 %".129", %".135"
  %".137" = icmp eq i1 %".136", 1
  br i1 %".137", label %".3.endif.if", label %".3.endif.else"
.3.endif.if:
  br label %".3.endif.endif"
.3.endif.else:
  br label %".3.endif.endif"
.3.endif.endif:
  %".141" = phi i8 [1, %".3.endif.if"], [0, %".3.endif.else"]
  %".142" = zext i8 %".141" to i64
  %".143" = lshr i64 %".119", 8
  %".144" = trunc i64 %".143" to i56
  %".145" = zext i56 %".144" to i64
  %".146" = shl i64 %".145", 8
  %".147" = or i64 %".142", %".146"
  %".148" = trunc i64 %".147" to i8
  %".149" = zext i8 %".148" to i32
  %".150" = zext i32 %".149" to i64
  %".151" = trunc i64 %".150" to i32
  %".152" = zext i32 %".151" to i64
  %".153" = trunc i64 %".152" to i32
  %".154" = trunc i64 %".152" to i32
  %".155" = and i32 %".153", %".154"
  %".156" = icmp eq i32 %".155", 0
  br i1 %".156", label %".3.endif.endif.if", label %".3.endif.endif.else"
.3.endif.endif.if:
  br label %".3.endif.endif.endif"
.3.endif.endif.else:
  br label %".3.endif.endif.endif"
.3.endif.endif.endif:
  %".160" = phi i1 [1, %".3.endif.endif.if"], [0, %".3.endif.endif.else"]
  %".161" = icmp eq i1 %".160", 1
  br i1 %".161", label %".3.endif.endif.endif.if", label %".3.endif.endif.endif.else"
.3.endif.endif.endif.if:
  br label %".3.endif.endif.endif.endif"
.3.endif.endif.endif.else:
  br label %".3.endif.endif.endif.endif"
.3.endif.endif.endif.endif:
  %".165" = phi i1 [1, %".3.endif.endif.endif.if"], [0, %".3.endif.endif.endif.else"]
  br i1 %".165", label %".3.endif.endif.endif.endif.if", label %".3.endif.endif.endif.endif.else"
.3.endif.endif.endif.endif.if:
  %".167" = add i64 8152287480, %"SymVar_0"
  %".168" = sext i64 %".167" to i128
  %".169" = zext i8 53 to i64
  %".170" = and i64 %".169", 63
  %".171" = lshr i64 %"SymVar_0", %".170"
  %".172" = zext i8 11 to i64
  %".173" = and i64 %".172", 63
  %".174" = shl i64 %"SymVar_0", %".173"
  %".175" = or i64 %".171", %".174"
  %".176" = zext i8 1 to i64
  %".177" = and i64 %".176", 63
  %".178" = lshr i64 %".175", %".177"
  %".179" = zext i64 %"SymVar_0" to i128
  %".180" = zext i64 0 to i128
  %".181" = shl i128 %".180", 64
  %".182" = or i128 %".179", %".181"
  %".183" = zext i64 3 to i128
  %".184" = udiv i128 %".182", %".183"
  %".185" = trunc i128 %".184" to i64
  %".186" = sext i64 112410438 to i128
  %".187" = sext i64 %".178" to i128
  %".188" = mul i128 %".186", %".187"
  %".189" = trunc i128 %".188" to i64
  %".190" = sub i64 %".185", %".189"
  %".191" = zext i8 2 to i64
  %".192" = and i64 %".191", 63
  %".193" = lshr i64 %".190", %".192"
  %".194" = and i64 15, %".193"
  %".195" = or i64 1, %".194"
  %".196" = sub i64 64, %".195"
  %".197" = trunc i64 %".196" to i32
  %".198" = zext i32 %".197" to i64
  %".199" = trunc i64 %".198" to i8
  %".200" = zext i8 %".199" to i64
  %".201" = and i64 %".200", 63
  %".202" = lshr i64 %".178", %".201"
  %".203" = zext i8 2 to i64
  %".204" = and i64 %".203", 63
  %".205" = lshr i64 %".190", %".204"
  %".206" = and i64 15, %".205"
  %".207" = or i64 1, %".206"
  %".208" = trunc i64 %".207" to i8
  %".209" = zext i8 %".208" to i64
  %".210" = and i64 %".209", 63
  %".211" = shl i64 %".178", %".210"
  %".212" = or i64 %".202", %".211"
  %".213" = and i64 7, %".212"
  %".214" = zext i8 2 to i64
  %".215" = and i64 %".214", 63
  %".216" = shl i64 %".213", %".215"
  %".217" = add i64 160536708, %"SymVar_0"
  %".218" = zext i8 7 to i64
  %".219" = and i64 %".218", 63
  %".220" = lshr i64 %".190", %".219"
  %".221" = zext i8 2 to i64
  %".222" = and i64 %".221", 63
  %".223" = lshr i64 %".220", %".222"
  %".224" = and i64 7, %".223"
  %".225" = or i64 1, %".224"
  %".226" = trunc i64 %".225" to i8
  %".227" = zext i8 %".226" to i64
  %".228" = and i64 %".227", 63
  %".229" = lshr i64 %".217", %".228"
  %".230" = and i64 63, %".229"
  %".231" = zext i8 4 to i64
  %".232" = and i64 %".231", 63
  %".233" = shl i64 %".230", %".232"
  %".234" = or i64 %".233", %".229"
  %".235" = or i64 %".216", %".234"
  %".236" = sext i64 %".235" to i128
  %".237" = mul i128 %".168", %".236"
  %".238" = trunc i128 %".237" to i64
  %".239" = sext i64 %".238" to i128
  %".240" = and i64 15, %".190"
  %".241" = zext i8 3 to i64
  %".242" = and i64 %".241", 63
  %".243" = shl i64 %".240", %".242"
  %".244" = or i64 %".243", %".190"
  %".245" = and i64 %".244", %".235"
  %".246" = and i64 31, %".245"
  %".247" = zext i8 4 to i64
  %".248" = and i64 %".247", 63
  %".249" = shl i64 %".246", %".248"
  %".250" = or i64 %".249", %".178"
  %".251" = or i64 %".244", %".250"
  %".252" = sext i64 %".251" to i128
  %".253" = mul i128 %".239", %".252"
  %".254" = trunc i128 %".253" to i64
  br label %".3.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.else:
  %".256" = add i64 8152287480, %"SymVar_0"
  %".257" = sext i64 %".256" to i128
  %".258" = zext i8 53 to i64
  %".259" = and i64 %".258", 63
  %".260" = lshr i64 %"SymVar_0", %".259"
  %".261" = zext i8 11 to i64
  %".262" = and i64 %".261", 63
  %".263" = shl i64 %"SymVar_0", %".262"
  %".264" = or i64 %".260", %".263"
  %".265" = zext i8 1 to i64
  %".266" = and i64 %".265", 63
  %".267" = lshr i64 %".264", %".266"
  %".268" = zext i64 %"SymVar_0" to i128
  %".269" = zext i64 0 to i128
  %".270" = shl i128 %".269", 64
  %".271" = or i128 %".268", %".270"
  %".272" = zext i64 3 to i128
  %".273" = udiv i128 %".271", %".272"
  %".274" = trunc i128 %".273" to i64
  %".275" = sext i64 112410438 to i128
  %".276" = sext i64 %".267" to i128
  %".277" = mul i128 %".275", %".276"
  %".278" = trunc i128 %".277" to i64
  %".279" = sub i64 %".274", %".278"
  %".280" = zext i8 2 to i64
  %".281" = and i64 %".280", 63
  %".282" = lshr i64 %".279", %".281"
  %".283" = and i64 15, %".282"
  %".284" = or i64 1, %".283"
  %".285" = sub i64 64, %".284"
  %".286" = trunc i64 %".285" to i32
  %".287" = zext i32 %".286" to i64
  %".288" = trunc i64 %".287" to i8
  %".289" = zext i8 %".288" to i64
  %".290" = and i64 %".289", 63
  %".291" = lshr i64 %".267", %".290"
  %".292" = zext i8 2 to i64
  %".293" = and i64 %".292", 63
  %".294" = lshr i64 %".279", %".293"
  %".295" = and i64 15, %".294"
  %".296" = or i64 1, %".295"
  %".297" = trunc i64 %".296" to i8
  %".298" = zext i8 %".297" to i64
  %".299" = and i64 %".298", 63
  %".300" = shl i64 %".267", %".299"
  %".301" = or i64 %".291", %".300"
  %".302" = and i64 7, %".301"
  %".303" = zext i8 2 to i64
  %".304" = and i64 %".303", 63
  %".305" = shl i64 %".302", %".304"
  %".306" = add i64 160536708, %"SymVar_0"
  %".307" = zext i8 7 to i64
  %".308" = and i64 %".307", 63
  %".309" = lshr i64 %".279", %".308"
  %".310" = zext i8 2 to i64
  %".311" = and i64 %".310", 63
  %".312" = lshr i64 %".309", %".311"
  %".313" = and i64 7, %".312"
  %".314" = or i64 1, %".313"
  %".315" = trunc i64 %".314" to i8
  %".316" = zext i8 %".315" to i64
  %".317" = and i64 %".316", 63
  %".318" = lshr i64 %".306", %".317"
  %".319" = and i64 63, %".318"
  %".320" = zext i8 4 to i64
  %".321" = and i64 %".320", 63
  %".322" = shl i64 %".319", %".321"
  %".323" = or i64 %".322", %".318"
  %".324" = or i64 %".305", %".323"
  %".325" = trunc i64 %".324" to i8
  %".326" = zext i8 %".325" to i64
  %".327" = lshr i64 %".324", 24
  %".328" = trunc i64 %".327" to i8
  %".329" = zext i8 %".328" to i32
  %".330" = zext i32 %".329" to i64
  %".331" = trunc i64 %".330" to i8
  %".332" = zext i8 %".331" to i32
  %".333" = zext i32 %".332" to i64
  %".334" = trunc i64 %".333" to i8
  %".335" = zext i8 %".334" to i64
  %".336" = shl i64 %".335", 8
  %".337" = or i64 %".326", %".336"
  %".338" = lshr i64 %".324", 16
  %".339" = trunc i64 %".338" to i8
  %".340" = zext i8 %".339" to i64
  %".341" = shl i64 %".340", 16
  %".342" = or i64 %".337", %".341"
  %".343" = lshr i64 %".324", 8
  %".344" = trunc i64 %".343" to i8
  %".345" = zext i8 %".344" to i32
  %".346" = zext i32 %".345" to i64
  %".347" = trunc i64 %".346" to i8
  %".348" = zext i8 %".347" to i32
  %".349" = zext i32 %".348" to i64
  %".350" = trunc i64 %".349" to i8
  %".351" = zext i8 %".350" to i32
  %".352" = zext i32 %".351" to i64
  %".353" = trunc i64 %".352" to i8
  %".354" = zext i8 %".353" to i32
  %".355" = zext i32 %".354" to i64
  %".356" = trunc i64 %".355" to i8
  %".357" = zext i8 %".356" to i64
  %".358" = shl i64 %".357", 24
  %".359" = or i64 %".342", %".358"
  %".360" = lshr i64 %".324", 32
  %".361" = trunc i64 %".360" to i8
  %".362" = zext i8 %".361" to i64
  %".363" = shl i64 %".362", 32
  %".364" = or i64 %".359", %".363"
  %".365" = lshr i64 %".324", 40
  %".366" = trunc i64 %".365" to i8
  %".367" = zext i8 %".366" to i64
  %".368" = shl i64 %".367", 40
  %".369" = or i64 %".364", %".368"
  %".370" = lshr i64 %".324", 48
  %".371" = trunc i64 %".370" to i8
  %".372" = zext i8 %".371" to i64
  %".373" = shl i64 %".372", 48
  %".374" = or i64 %".369", %".373"
  %".375" = lshr i64 %".324", 56
  %".376" = trunc i64 %".375" to i8
  %".377" = zext i8 %".376" to i64
  %".378" = shl i64 %".377", 56
  %".379" = or i64 %".374", %".378"
  %".380" = sext i64 %".379" to i128
  %".381" = mul i128 %".257", %".380"
  %".382" = trunc i128 %".381" to i64
  %".383" = sext i64 %".382" to i128
  %".384" = zext i8 3 to i64
  %".385" = and i64 %".384", 63
  %".386" = lshr i64 %".256", %".385"
  %".387" = and i64 15, %".386"
  %".388" = or i64 1, %".387"
  %".389" = sub i64 64, %".388"
  %".390" = trunc i64 %".389" to i32
  %".391" = zext i32 %".390" to i64
  %".392" = trunc i64 %".391" to i8
  %".393" = zext i8 %".392" to i64
  %".394" = and i64 %".393", 63
  %".395" = lshr i64 %".256", %".394"
  %".396" = zext i8 3 to i64
  %".397" = and i64 %".396", 63
  %".398" = lshr i64 %".256", %".397"
  %".399" = and i64 15, %".398"
  %".400" = or i64 1, %".399"
  %".401" = trunc i64 %".400" to i8
  %".402" = zext i8 %".401" to i64
  %".403" = and i64 %".402", 63
  %".404" = shl i64 %".256", %".403"
  %".405" = or i64 %".395", %".404"
  %".406" = or i64 %".279", %".405"
  %".407" = sext i64 %".406" to i128
  %".408" = mul i128 %".383", %".407"
  %".409" = trunc i128 %".408" to i64
  br label %".3.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.endif:
  %".411" = phi i64 [%".254", %".3.endif.endif.endif.endif.if"], [%".409", %".3.endif.endif.endif.endif.else"]
  ret i64 %".411"
}
