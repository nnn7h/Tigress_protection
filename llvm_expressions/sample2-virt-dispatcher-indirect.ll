; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = zext i8 5 to i64
  %".5" = and i64 %".4", 63
  %".6" = lshr i64 %"SymVar_0", %".5"
  %".7" = xor i64 810798164723513605, %".6"
  %".8" = sub i64 %"SymVar_0", 275339905
  %".9" = add i64 %".7", %".8"
  %".10" = add i64 %".9", %".6"
  %".11" = add i64 %".10", %"SymVar_0"
  %".12" = sext i64 %".11" to i128
  %".13" = sext i64 %".6" to i128
  %".14" = mul i128 %".12", %".13"
  %".15" = trunc i128 %".14" to i64
  %".16" = and i64 7, %".15"
  %".17" = zext i8 2 to i64
  %".18" = and i64 %".17", 63
  %".19" = shl i64 %".16", %".18"
  %".20" = or i64 %".19", %".6"
  %".21" = sext i64 %".6" to i128
  %".22" = sext i64 1015975030 to i128
  %".23" = mul i128 %".21", %".22"
  %".24" = trunc i128 %".23" to i64
  %".25" = and i64 7, %".24"
  %".26" = or i64 1, %".25"
  %".27" = trunc i64 %".26" to i32
  %".28" = zext i32 %".27" to i64
  %".29" = trunc i64 %".28" to i8
  %".30" = zext i8 %".29" to i64
  %".31" = and i64 %".30", 63
  %".32" = lshr i64 %"SymVar_0", %".31"
  %".33" = zext i8 4 to i64
  %".34" = and i64 %".33", 63
  %".35" = lshr i64 %".9", %".34"
  %".36" = and i64 15, %".35"
  %".37" = or i64 1, %".36"
  %".38" = sub i64 64, %".37"
  %".39" = trunc i64 %".38" to i32
  %".40" = zext i32 %".39" to i64
  %".41" = trunc i64 %".40" to i8
  %".42" = zext i8 %".41" to i64
  %".43" = and i64 %".42", 63
  %".44" = lshr i64 %".32", %".43"
  %".45" = zext i8 4 to i64
  %".46" = and i64 %".45", 63
  %".47" = lshr i64 %".9", %".46"
  %".48" = and i64 15, %".47"
  %".49" = or i64 1, %".48"
  %".50" = trunc i64 %".49" to i8
  %".51" = zext i8 %".50" to i64
  %".52" = and i64 %".51", 63
  %".53" = shl i64 %".32", %".52"
  %".54" = or i64 %".44", %".53"
  %".55" = and i64 15, %".54"
  %".56" = zext i8 3 to i64
  %".57" = and i64 %".56", 63
  %".58" = shl i64 %".55", %".57"
  %".59" = or i64 %".58", %".9"
  %".60" = and i64 15, %".59"
  %".61" = or i64 1, %".60"
  %".62" = sub i64 64, %".61"
  %".63" = trunc i64 %".62" to i32
  %".64" = zext i32 %".63" to i64
  %".65" = trunc i64 %".64" to i8
  %".66" = zext i8 %".65" to i64
  %".67" = and i64 %".66", 63
  %".68" = lshr i64 %".20", %".67"
  %".69" = and i64 15, %".59"
  %".70" = or i64 1, %".69"
  %".71" = trunc i64 %".70" to i8
  %".72" = zext i8 %".71" to i64
  %".73" = and i64 %".72", 63
  %".74" = shl i64 %".20", %".73"
  %".75" = or i64 %".68", %".74"
  %".76" = zext i8 3 to i64
  %".77" = and i64 %".76", 63
  %".78" = lshr i64 %".32", %".77"
  %".79" = and i64 15, %".78"
  %".80" = or i64 1, %".79"
  %".81" = sub i64 64, %".80"
  %".82" = trunc i64 %".81" to i32
  %".83" = zext i32 %".82" to i64
  %".84" = trunc i64 %".83" to i8
  %".85" = zext i8 %".84" to i64
  %".86" = and i64 %".85", 63
  %".87" = lshr i64 %".11", %".86"
  %".88" = zext i8 3 to i64
  %".89" = and i64 %".88", 63
  %".90" = lshr i64 %".32", %".89"
  %".91" = and i64 15, %".90"
  %".92" = or i64 1, %".91"
  %".93" = trunc i64 %".92" to i8
  %".94" = zext i8 %".93" to i64
  %".95" = and i64 %".94", 63
  %".96" = shl i64 %".11", %".95"
  %".97" = or i64 %".87", %".96"
  %".98" = sub i64 %".75", %".97"
  %".99" = xor i64 %".97", %".98"
  %".100" = xor i64 %".75", %".99"
  %".101" = xor i64 %".75", %".98"
  %".102" = xor i64 %".75", %".97"
  %".103" = and i64 %".101", %".102"
  %".104" = xor i64 %".100", %".103"
  %".105" = lshr i64 %".104", 63
  %".106" = trunc i64 %".105" to i1
  %".107" = icmp eq i64 %".98", 0
  br i1 %".107", label %".3.if", label %".3.else"
.3.if:
  br label %".3.endif"
.3.else:
  br label %".3.endif"
.3.endif:
  %".111" = phi i1 [1, %".3.if"], [0, %".3.else"]
  %".112" = or i1 %".106", %".111"
  %".113" = icmp eq i1 %".112", 1
  br i1 %".113", label %".3.endif.if", label %".3.endif.else"
.3.endif.if:
  br label %".3.endif.endif"
.3.endif.else:
  br label %".3.endif.endif"
.3.endif.endif:
  %".117" = phi i8 [1, %".3.endif.if"], [0, %".3.endif.else"]
  %".118" = zext i8 %".117" to i64
  %".119" = lshr i64 %".97", 8
  %".120" = trunc i64 %".119" to i56
  %".121" = zext i56 %".120" to i64
  %".122" = shl i64 %".121", 8
  %".123" = or i64 %".118", %".122"
  %".124" = trunc i64 %".123" to i8
  %".125" = zext i8 %".124" to i32
  %".126" = zext i32 %".125" to i64
  %".127" = trunc i64 %".126" to i32
  %".128" = zext i32 %".127" to i64
  %".129" = trunc i64 %".128" to i32
  %".130" = trunc i64 %".128" to i32
  %".131" = and i32 %".129", %".130"
  %".132" = icmp eq i32 %".131", 0
  br i1 %".132", label %".3.endif.endif.if", label %".3.endif.endif.else"
.3.endif.endif.if:
  br label %".3.endif.endif.endif"
.3.endif.endif.else:
  br label %".3.endif.endif.endif"
.3.endif.endif.endif:
  %".136" = phi i1 [1, %".3.endif.endif.if"], [0, %".3.endif.endif.else"]
  %".137" = icmp eq i1 %".136", 0
  br i1 %".137", label %".3.endif.endif.endif.if", label %".3.endif.endif.endif.else"
.3.endif.endif.endif.if:
  br label %".3.endif.endif.endif.endif"
.3.endif.endif.endif.else:
  br label %".3.endif.endif.endif.endif"
.3.endif.endif.endif.endif:
  %".141" = phi i1 [1, %".3.endif.endif.endif.if"], [0, %".3.endif.endif.endif.else"]
  br i1 %".141", label %".3.endif.endif.endif.endif.if", label %".3.endif.endif.endif.endif.else"
.3.endif.endif.endif.endif.if:
  %".143" = zext i8 5 to i64
  %".144" = and i64 %".143", 63
  %".145" = lshr i64 %"SymVar_0", %".144"
  %".146" = xor i64 810798164723513605, %".145"
  %".147" = sub i64 %"SymVar_0", 275339905
  %".148" = add i64 %".146", %".147"
  %".149" = add i64 %".148", %".145"
  %".150" = add i64 %".149", %"SymVar_0"
  %".151" = sext i64 %".150" to i128
  %".152" = sext i64 %".145" to i128
  %".153" = mul i128 %".151", %".152"
  %".154" = trunc i128 %".153" to i64
  %".155" = and i64 7, %".154"
  %".156" = zext i8 2 to i64
  %".157" = and i64 %".156", 63
  %".158" = shl i64 %".155", %".157"
  %".159" = or i64 %".158", %".145"
  %".160" = sub i64 %".159", %".150"
  %".161" = and i64 31, %".160"
  %".162" = zext i8 3 to i64
  %".163" = and i64 %".162", 63
  %".164" = shl i64 %".161", %".163"
  %".165" = sext i64 %".145" to i128
  %".166" = sext i64 1015975030 to i128
  %".167" = mul i128 %".165", %".166"
  %".168" = trunc i128 %".167" to i64
  %".169" = and i64 7, %".168"
  %".170" = or i64 1, %".169"
  %".171" = trunc i64 %".170" to i32
  %".172" = zext i32 %".171" to i64
  %".173" = trunc i64 %".172" to i8
  %".174" = zext i8 %".173" to i64
  %".175" = and i64 %".174", 63
  %".176" = lshr i64 %"SymVar_0", %".175"
  %".177" = or i64 %".164", %".176"
  %".178" = zext i8 4 to i64
  %".179" = and i64 %".178", 63
  %".180" = lshr i64 %".148", %".179"
  %".181" = and i64 15, %".180"
  %".182" = or i64 1, %".181"
  %".183" = sub i64 64, %".182"
  %".184" = trunc i64 %".183" to i32
  %".185" = zext i32 %".184" to i64
  %".186" = trunc i64 %".185" to i8
  %".187" = zext i8 %".186" to i64
  %".188" = and i64 %".187", 63
  %".189" = lshr i64 %".176", %".188"
  %".190" = zext i8 4 to i64
  %".191" = and i64 %".190", 63
  %".192" = lshr i64 %".148", %".191"
  %".193" = and i64 15, %".192"
  %".194" = or i64 1, %".193"
  %".195" = trunc i64 %".194" to i8
  %".196" = zext i8 %".195" to i64
  %".197" = and i64 %".196", 63
  %".198" = shl i64 %".176", %".197"
  %".199" = or i64 %".189", %".198"
  %".200" = and i64 15, %".199"
  %".201" = zext i8 3 to i64
  %".202" = and i64 %".201", 63
  %".203" = shl i64 %".200", %".202"
  %".204" = or i64 %".203", %".148"
  %".205" = trunc i64 %".204" to i8
  %".206" = zext i8 %".205" to i32
  %".207" = lshr i64 %".204", 8
  %".208" = trunc i64 %".207" to i8
  %".209" = zext i8 %".208" to i32
  %".210" = shl i32 %".209", 8
  %".211" = or i32 %".206", %".210"
  %".212" = lshr i64 %".204", 16
  %".213" = trunc i64 %".212" to i8
  %".214" = zext i8 %".213" to i32
  %".215" = shl i32 %".214", 16
  %".216" = or i32 %".211", %".215"
  %".217" = lshr i64 %".204", 24
  %".218" = trunc i64 %".217" to i8
  %".219" = zext i8 %".218" to i32
  %".220" = shl i32 %".219", 24
  %".221" = or i32 %".216", %".220"
  %".222" = zext i32 %".221" to i64
  %".223" = trunc i64 %".222" to i32
  %".224" = zext i32 %".223" to i64
  %".225" = trunc i64 %".224" to i32
  %".226" = zext i32 %".225" to i64
  %".227" = trunc i64 %".226" to i32
  %".228" = zext i32 %".227" to i64
  %".229" = trunc i64 %".228" to i32
  %".230" = zext i32 %".229" to i64
  %".231" = trunc i64 %".230" to i32
  %".232" = zext i32 %".231" to i64
  %".233" = trunc i64 %".232" to i32
  %".234" = zext i32 %".233" to i64
  %".235" = trunc i64 %".234" to i32
  %".236" = zext i32 %".235" to i64
  %".237" = trunc i64 %".236" to i32
  %".238" = trunc i32 %".237" to i8
  %".239" = zext i8 %".238" to i64
  %".240" = trunc i64 %".236" to i32
  %".241" = lshr i32 %".240", 8
  %".242" = trunc i32 %".241" to i8
  %".243" = zext i8 %".242" to i64
  %".244" = shl i64 %".243", 8
  %".245" = or i64 %".239", %".244"
  %".246" = trunc i64 %".236" to i32
  %".247" = lshr i32 %".246", 16
  %".248" = trunc i32 %".247" to i8
  %".249" = zext i8 %".248" to i64
  %".250" = shl i64 %".249", 16
  %".251" = or i64 %".245", %".250"
  %".252" = trunc i64 %".236" to i32
  %".253" = lshr i32 %".252", 24
  %".254" = trunc i32 %".253" to i8
  %".255" = zext i8 %".254" to i64
  %".256" = shl i64 %".255", 24
  %".257" = or i64 %".251", %".256"
  %".258" = lshr i64 %".204", 32
  %".259" = trunc i64 %".258" to i8
  %".260" = zext i8 %".259" to i32
  %".261" = lshr i64 %".204", 40
  %".262" = trunc i64 %".261" to i8
  %".263" = zext i8 %".262" to i32
  %".264" = shl i32 %".263", 8
  %".265" = or i32 %".260", %".264"
  %".266" = lshr i64 %".204", 48
  %".267" = trunc i64 %".266" to i8
  %".268" = zext i8 %".267" to i32
  %".269" = shl i32 %".268", 16
  %".270" = or i32 %".265", %".269"
  %".271" = lshr i64 %".204", 56
  %".272" = trunc i64 %".271" to i8
  %".273" = zext i8 %".272" to i32
  %".274" = shl i32 %".273", 24
  %".275" = or i32 %".270", %".274"
  %".276" = zext i32 %".275" to i64
  %".277" = trunc i64 %".276" to i32
  %".278" = zext i32 %".277" to i64
  %".279" = trunc i64 %".278" to i32
  %".280" = zext i32 %".279" to i64
  %".281" = trunc i64 %".280" to i32
  %".282" = zext i32 %".281" to i64
  %".283" = trunc i64 %".282" to i32
  %".284" = trunc i32 %".283" to i8
  %".285" = zext i8 %".284" to i64
  %".286" = shl i64 %".285", 32
  %".287" = or i64 %".257", %".286"
  %".288" = trunc i64 %".282" to i32
  %".289" = lshr i32 %".288", 8
  %".290" = trunc i32 %".289" to i8
  %".291" = zext i8 %".290" to i64
  %".292" = shl i64 %".291", 40
  %".293" = or i64 %".287", %".292"
  %".294" = trunc i64 %".282" to i32
  %".295" = lshr i32 %".294", 16
  %".296" = trunc i32 %".295" to i8
  %".297" = zext i8 %".296" to i64
  %".298" = shl i64 %".297", 48
  %".299" = or i64 %".293", %".298"
  %".300" = trunc i64 %".282" to i32
  %".301" = lshr i32 %".300", 24
  %".302" = trunc i32 %".301" to i8
  %".303" = zext i8 %".302" to i64
  %".304" = shl i64 %".303", 56
  %".305" = or i64 %".299", %".304"
  %".306" = and i64 31, %".204"
  %".307" = zext i8 4 to i64
  %".308" = and i64 %".307", 63
  %".309" = shl i64 %".306", %".308"
  %".310" = or i64 %".309", %".159"
  %".311" = sub i64 %".305", %".310"
  %".312" = or i64 %".177", %".311"
  %".313" = and i64 63, %".311"
  %".314" = zext i8 4 to i64
  %".315" = and i64 %".314", 63
  %".316" = shl i64 %".313", %".315"
  %".317" = or i64 %".316", %".310"
  %".318" = zext i8 %".238" to i64
  %".319" = zext i8 %".242" to i64
  %".320" = shl i64 %".319", 8
  %".321" = or i64 %".318", %".320"
  %".322" = zext i8 %".248" to i64
  %".323" = shl i64 %".322", 16
  %".324" = or i64 %".321", %".323"
  %".325" = zext i8 %".254" to i64
  %".326" = shl i64 %".325", 24
  %".327" = or i64 %".324", %".326"
  %".328" = zext i8 %".284" to i64
  %".329" = shl i64 %".328", 32
  %".330" = or i64 %".327", %".329"
  %".331" = zext i8 %".290" to i64
  %".332" = shl i64 %".331", 40
  %".333" = or i64 %".330", %".332"
  %".334" = zext i8 %".296" to i64
  %".335" = shl i64 %".334", 48
  %".336" = or i64 %".333", %".335"
  %".337" = zext i8 %".302" to i64
  %".338" = shl i64 %".337", 56
  %".339" = or i64 %".336", %".338"
  %".340" = zext i8 2 to i64
  %".341" = and i64 %".340", 63
  %".342" = lshr i64 %".339", %".341"
  %".343" = and i64 7, %".342"
  %".344" = or i64 1, %".343"
  %".345" = trunc i64 %".344" to i8
  %".346" = zext i8 %".345" to i64
  %".347" = and i64 %".346", 63
  %".348" = shl i64 %".317", %".347"
  %".349" = add i64 %".312", %".348"
  br label %".3.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.else:
  %".351" = zext i8 5 to i64
  %".352" = and i64 %".351", 63
  %".353" = lshr i64 %"SymVar_0", %".352"
  %".354" = sext i64 %".353" to i128
  %".355" = sext i64 1015975030 to i128
  %".356" = mul i128 %".354", %".355"
  %".357" = trunc i128 %".356" to i64
  %".358" = and i64 7, %".357"
  %".359" = or i64 1, %".358"
  %".360" = trunc i64 %".359" to i32
  %".361" = zext i32 %".360" to i64
  %".362" = trunc i64 %".361" to i8
  %".363" = zext i8 %".362" to i64
  %".364" = and i64 %".363", 63
  %".365" = lshr i64 %"SymVar_0", %".364"
  %".366" = xor i64 810798164723513605, %".353"
  %".367" = sub i64 %"SymVar_0", 275339905
  %".368" = add i64 %".366", %".367"
  %".369" = zext i8 4 to i64
  %".370" = and i64 %".369", 63
  %".371" = lshr i64 %".368", %".370"
  %".372" = and i64 15, %".371"
  %".373" = or i64 1, %".372"
  %".374" = sub i64 64, %".373"
  %".375" = trunc i64 %".374" to i32
  %".376" = zext i32 %".375" to i64
  %".377" = trunc i64 %".376" to i8
  %".378" = zext i8 %".377" to i64
  %".379" = and i64 %".378", 63
  %".380" = lshr i64 %".365", %".379"
  %".381" = zext i8 4 to i64
  %".382" = and i64 %".381", 63
  %".383" = lshr i64 %".368", %".382"
  %".384" = and i64 15, %".383"
  %".385" = or i64 1, %".384"
  %".386" = trunc i64 %".385" to i8
  %".387" = zext i8 %".386" to i64
  %".388" = and i64 %".387", 63
  %".389" = shl i64 %".365", %".388"
  %".390" = or i64 %".380", %".389"
  %".391" = and i64 15, %".390"
  %".392" = zext i8 3 to i64
  %".393" = and i64 %".392", 63
  %".394" = shl i64 %".391", %".393"
  %".395" = or i64 %".394", %".368"
  %".396" = and i64 15, %".395"
  %".397" = zext i8 3 to i64
  %".398" = and i64 %".397", 63
  %".399" = shl i64 %".396", %".398"
  %".400" = or i64 %".399", %".395"
  %".401" = trunc i64 %".400" to i8
  %".402" = zext i8 %".401" to i32
  %".403" = lshr i64 %".400", 8
  %".404" = trunc i64 %".403" to i8
  %".405" = zext i8 %".404" to i32
  %".406" = shl i32 %".405", 8
  %".407" = or i32 %".402", %".406"
  %".408" = lshr i64 %".400", 16
  %".409" = trunc i64 %".408" to i8
  %".410" = zext i8 %".409" to i32
  %".411" = shl i32 %".410", 16
  %".412" = or i32 %".407", %".411"
  %".413" = lshr i64 %".400", 24
  %".414" = trunc i64 %".413" to i8
  %".415" = zext i8 %".414" to i32
  %".416" = shl i32 %".415", 24
  %".417" = or i32 %".412", %".416"
  %".418" = zext i32 %".417" to i64
  %".419" = trunc i64 %".418" to i32
  %".420" = zext i32 %".419" to i64
  %".421" = trunc i64 %".420" to i32
  %".422" = zext i32 %".421" to i64
  %".423" = trunc i64 %".422" to i32
  %".424" = zext i32 %".423" to i64
  %".425" = trunc i64 %".424" to i32
  %".426" = zext i32 %".425" to i64
  %".427" = trunc i64 %".426" to i32
  %".428" = zext i32 %".427" to i64
  %".429" = trunc i64 %".428" to i32
  %".430" = zext i32 %".429" to i64
  %".431" = trunc i64 %".430" to i32
  %".432" = zext i32 %".431" to i64
  %".433" = trunc i64 %".432" to i32
  %".434" = trunc i32 %".433" to i8
  %".435" = zext i8 %".434" to i64
  %".436" = trunc i64 %".432" to i32
  %".437" = lshr i32 %".436", 8
  %".438" = trunc i32 %".437" to i8
  %".439" = zext i8 %".438" to i64
  %".440" = shl i64 %".439", 8
  %".441" = or i64 %".435", %".440"
  %".442" = trunc i64 %".432" to i32
  %".443" = lshr i32 %".442", 16
  %".444" = trunc i32 %".443" to i8
  %".445" = zext i8 %".444" to i64
  %".446" = shl i64 %".445", 16
  %".447" = or i64 %".441", %".446"
  %".448" = trunc i64 %".432" to i32
  %".449" = lshr i32 %".448", 24
  %".450" = trunc i32 %".449" to i8
  %".451" = zext i8 %".450" to i64
  %".452" = shl i64 %".451", 24
  %".453" = or i64 %".447", %".452"
  %".454" = lshr i64 %".400", 32
  %".455" = trunc i64 %".454" to i8
  %".456" = zext i8 %".455" to i32
  %".457" = lshr i64 %".400", 40
  %".458" = trunc i64 %".457" to i8
  %".459" = zext i8 %".458" to i32
  %".460" = shl i32 %".459", 8
  %".461" = or i32 %".456", %".460"
  %".462" = lshr i64 %".400", 48
  %".463" = trunc i64 %".462" to i8
  %".464" = zext i8 %".463" to i32
  %".465" = shl i32 %".464", 16
  %".466" = or i32 %".461", %".465"
  %".467" = lshr i64 %".400", 56
  %".468" = trunc i64 %".467" to i8
  %".469" = zext i8 %".468" to i32
  %".470" = shl i32 %".469", 24
  %".471" = or i32 %".466", %".470"
  %".472" = zext i32 %".471" to i64
  %".473" = trunc i64 %".472" to i32
  %".474" = zext i32 %".473" to i64
  %".475" = trunc i64 %".474" to i32
  %".476" = zext i32 %".475" to i64
  %".477" = trunc i64 %".476" to i32
  %".478" = zext i32 %".477" to i64
  %".479" = trunc i64 %".478" to i32
  %".480" = trunc i32 %".479" to i8
  %".481" = zext i8 %".480" to i64
  %".482" = shl i64 %".481", 32
  %".483" = or i64 %".453", %".482"
  %".484" = trunc i64 %".478" to i32
  %".485" = lshr i32 %".484", 8
  %".486" = trunc i32 %".485" to i8
  %".487" = zext i8 %".486" to i64
  %".488" = shl i64 %".487", 40
  %".489" = or i64 %".483", %".488"
  %".490" = trunc i64 %".478" to i32
  %".491" = lshr i32 %".490", 16
  %".492" = trunc i32 %".491" to i8
  %".493" = zext i8 %".492" to i64
  %".494" = shl i64 %".493", 48
  %".495" = or i64 %".489", %".494"
  %".496" = trunc i64 %".478" to i32
  %".497" = lshr i32 %".496", 24
  %".498" = trunc i32 %".497" to i8
  %".499" = zext i8 %".498" to i64
  %".500" = shl i64 %".499", 56
  %".501" = or i64 %".495", %".500"
  %".502" = add i64 %".368", %".353"
  %".503" = add i64 %".502", %"SymVar_0"
  %".504" = sext i64 %".503" to i128
  %".505" = sext i64 %".353" to i128
  %".506" = mul i128 %".504", %".505"
  %".507" = trunc i128 %".506" to i64
  %".508" = and i64 7, %".507"
  %".509" = zext i8 2 to i64
  %".510" = and i64 %".509", 63
  %".511" = shl i64 %".508", %".510"
  %".512" = or i64 %".511", %".353"
  %".513" = lshr i64 %".512", 56
  %".514" = trunc i64 %".513" to i8
  %".515" = zext i8 %".514" to i32
  %".516" = zext i32 %".515" to i64
  %".517" = trunc i64 %".516" to i8
  %".518" = zext i8 %".517" to i32
  %".519" = zext i32 %".518" to i64
  %".520" = trunc i64 %".519" to i8
  %".521" = zext i8 %".520" to i32
  %".522" = zext i32 %".521" to i64
  %".523" = trunc i64 %".522" to i8
  %".524" = zext i8 %".523" to i32
  %".525" = zext i32 %".524" to i64
  %".526" = trunc i64 %".525" to i8
  %".527" = zext i8 %".526" to i64
  %".528" = lshr i64 %".512", 8
  %".529" = trunc i64 %".528" to i8
  %".530" = zext i8 %".529" to i64
  %".531" = shl i64 %".530", 8
  %".532" = or i64 %".527", %".531"
  %".533" = lshr i64 %".512", 16
  %".534" = trunc i64 %".533" to i8
  %".535" = zext i8 %".534" to i64
  %".536" = shl i64 %".535", 16
  %".537" = or i64 %".532", %".536"
  %".538" = lshr i64 %".512", 24
  %".539" = trunc i64 %".538" to i8
  %".540" = zext i8 %".539" to i64
  %".541" = shl i64 %".540", 24
  %".542" = or i64 %".537", %".541"
  %".543" = lshr i64 %".512", 32
  %".544" = trunc i64 %".543" to i8
  %".545" = zext i8 %".544" to i64
  %".546" = shl i64 %".545", 32
  %".547" = or i64 %".542", %".546"
  %".548" = lshr i64 %".512", 40
  %".549" = trunc i64 %".548" to i8
  %".550" = zext i8 %".549" to i64
  %".551" = shl i64 %".550", 40
  %".552" = or i64 %".547", %".551"
  %".553" = lshr i64 %".512", 48
  %".554" = trunc i64 %".553" to i8
  %".555" = zext i8 %".554" to i64
  %".556" = shl i64 %".555", 48
  %".557" = or i64 %".552", %".556"
  %".558" = trunc i64 %".512" to i8
  %".559" = zext i8 %".558" to i32
  %".560" = zext i32 %".559" to i64
  %".561" = trunc i64 %".560" to i8
  %".562" = zext i8 %".561" to i32
  %".563" = zext i32 %".562" to i64
  %".564" = trunc i64 %".563" to i8
  %".565" = zext i8 %".564" to i64
  %".566" = shl i64 %".565", 56
  %".567" = or i64 %".557", %".566"
  %".568" = sub i64 %".501", %".567"
  %".569" = or i64 %".365", %".568"
  %".570" = and i64 63, %".568"
  %".571" = zext i8 4 to i64
  %".572" = and i64 %".571", 63
  %".573" = shl i64 %".570", %".572"
  %".574" = zext i8 %".526" to i64
  %".575" = zext i8 %".529" to i64
  %".576" = shl i64 %".575", 8
  %".577" = or i64 %".574", %".576"
  %".578" = zext i8 %".534" to i64
  %".579" = shl i64 %".578", 16
  %".580" = or i64 %".577", %".579"
  %".581" = zext i8 %".539" to i64
  %".582" = shl i64 %".581", 24
  %".583" = or i64 %".580", %".582"
  %".584" = zext i8 %".544" to i64
  %".585" = shl i64 %".584", 32
  %".586" = or i64 %".583", %".585"
  %".587" = zext i8 %".549" to i64
  %".588" = shl i64 %".587", 40
  %".589" = or i64 %".586", %".588"
  %".590" = zext i8 %".554" to i64
  %".591" = shl i64 %".590", 48
  %".592" = or i64 %".589", %".591"
  %".593" = zext i8 %".564" to i64
  %".594" = shl i64 %".593", 56
  %".595" = or i64 %".592", %".594"
  %".596" = or i64 %".573", %".595"
  %".597" = zext i8 %".434" to i64
  %".598" = zext i8 %".438" to i64
  %".599" = shl i64 %".598", 8
  %".600" = or i64 %".597", %".599"
  %".601" = zext i8 %".444" to i64
  %".602" = shl i64 %".601", 16
  %".603" = or i64 %".600", %".602"
  %".604" = zext i8 %".450" to i64
  %".605" = shl i64 %".604", 24
  %".606" = or i64 %".603", %".605"
  %".607" = zext i8 %".480" to i64
  %".608" = shl i64 %".607", 32
  %".609" = or i64 %".606", %".608"
  %".610" = zext i8 %".486" to i64
  %".611" = shl i64 %".610", 40
  %".612" = or i64 %".609", %".611"
  %".613" = zext i8 %".492" to i64
  %".614" = shl i64 %".613", 48
  %".615" = or i64 %".612", %".614"
  %".616" = zext i8 %".498" to i64
  %".617" = shl i64 %".616", 56
  %".618" = or i64 %".615", %".617"
  %".619" = zext i8 2 to i64
  %".620" = and i64 %".619", 63
  %".621" = lshr i64 %".618", %".620"
  %".622" = and i64 7, %".621"
  %".623" = or i64 1, %".622"
  %".624" = trunc i64 %".623" to i8
  %".625" = zext i8 %".624" to i64
  %".626" = and i64 %".625", 63
  %".627" = shl i64 %".596", %".626"
  %".628" = add i64 %".569", %".627"
  br label %".3.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.endif:
  %".630" = phi i64 [%".349", %".3.endif.endif.endif.endif.if"], [%".628", %".3.endif.endif.endif.endif.else"]
  ret i64 %".630"
}
