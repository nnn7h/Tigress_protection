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
  %".50" = trunc i64 %".49" to i32
  %".51" = zext i32 %".50" to i64
  %".52" = trunc i64 %".51" to i8
  %".53" = zext i8 %".52" to i64
  %".54" = and i64 %".53", 63
  %".55" = shl i64 %".32", %".54"
  %".56" = or i64 %".44", %".55"
  %".57" = and i64 15, %".56"
  %".58" = zext i8 3 to i64
  %".59" = and i64 %".58", 63
  %".60" = shl i64 %".57", %".59"
  %".61" = or i64 %".60", %".9"
  %".62" = and i64 15, %".61"
  %".63" = or i64 1, %".62"
  %".64" = sub i64 64, %".63"
  %".65" = trunc i64 %".64" to i32
  %".66" = zext i32 %".65" to i64
  %".67" = trunc i64 %".66" to i8
  %".68" = zext i8 %".67" to i64
  %".69" = and i64 %".68", 63
  %".70" = lshr i64 %".20", %".69"
  %".71" = and i64 15, %".61"
  %".72" = or i64 1, %".71"
  %".73" = trunc i64 %".72" to i32
  %".74" = zext i32 %".73" to i64
  %".75" = trunc i64 %".74" to i8
  %".76" = zext i8 %".75" to i64
  %".77" = and i64 %".76", 63
  %".78" = shl i64 %".20", %".77"
  %".79" = or i64 %".70", %".78"
  %".80" = zext i8 3 to i64
  %".81" = and i64 %".80", 63
  %".82" = lshr i64 %".32", %".81"
  %".83" = and i64 15, %".82"
  %".84" = or i64 1, %".83"
  %".85" = sub i64 64, %".84"
  %".86" = trunc i64 %".85" to i32
  %".87" = zext i32 %".86" to i64
  %".88" = trunc i64 %".87" to i8
  %".89" = zext i8 %".88" to i64
  %".90" = and i64 %".89", 63
  %".91" = lshr i64 %".11", %".90"
  %".92" = zext i8 3 to i64
  %".93" = and i64 %".92", 63
  %".94" = lshr i64 %".32", %".93"
  %".95" = and i64 15, %".94"
  %".96" = or i64 1, %".95"
  %".97" = trunc i64 %".96" to i32
  %".98" = zext i32 %".97" to i64
  %".99" = trunc i64 %".98" to i8
  %".100" = zext i8 %".99" to i64
  %".101" = and i64 %".100", 63
  %".102" = shl i64 %".11", %".101"
  %".103" = or i64 %".91", %".102"
  %".104" = sub i64 %".79", %".103"
  %".105" = xor i64 %".103", %".104"
  %".106" = xor i64 %".79", %".105"
  %".107" = xor i64 %".79", %".104"
  %".108" = xor i64 %".79", %".103"
  %".109" = and i64 %".107", %".108"
  %".110" = xor i64 %".106", %".109"
  %".111" = lshr i64 %".110", 63
  %".112" = trunc i64 %".111" to i1
  %".113" = icmp eq i64 %".104", 0
  br i1 %".113", label %".3.if", label %".3.else"
.3.if:
  br label %".3.endif"
.3.else:
  br label %".3.endif"
.3.endif:
  %".117" = phi i1 [1, %".3.if"], [0, %".3.else"]
  %".118" = or i1 %".112", %".117"
  %".119" = icmp eq i1 %".118", 1
  br i1 %".119", label %".3.endif.if", label %".3.endif.else"
.3.endif.if:
  br label %".3.endif.endif"
.3.endif.else:
  br label %".3.endif.endif"
.3.endif.endif:
  %".123" = phi i8 [1, %".3.endif.if"], [0, %".3.endif.else"]
  %".124" = zext i8 %".123" to i64
  %".125" = lshr i64 %".103", 8
  %".126" = trunc i64 %".125" to i56
  %".127" = zext i56 %".126" to i64
  %".128" = shl i64 %".127", 8
  %".129" = or i64 %".124", %".128"
  %".130" = trunc i64 %".129" to i8
  %".131" = zext i8 %".130" to i32
  %".132" = zext i32 %".131" to i64
  %".133" = trunc i64 %".132" to i32
  %".134" = zext i32 %".133" to i64
  %".135" = trunc i64 %".134" to i32
  %".136" = zext i32 %".135" to i64
  %".137" = trunc i64 %".136" to i32
  %".138" = zext i32 %".137" to i64
  %".139" = trunc i64 %".138" to i32
  %".140" = trunc i64 %".138" to i32
  %".141" = and i32 %".139", %".140"
  %".142" = icmp eq i32 %".141", 0
  br i1 %".142", label %".3.endif.endif.if", label %".3.endif.endif.else"
.3.endif.endif.if:
  br label %".3.endif.endif.endif"
.3.endif.endif.else:
  br label %".3.endif.endif.endif"
.3.endif.endif.endif:
  %".146" = phi i1 [1, %".3.endif.endif.if"], [0, %".3.endif.endif.else"]
  %".147" = icmp eq i1 %".146", 1
  br i1 %".147", label %".3.endif.endif.endif.if", label %".3.endif.endif.endif.else"
.3.endif.endif.endif.if:
  br label %".3.endif.endif.endif.endif"
.3.endif.endif.endif.else:
  br label %".3.endif.endif.endif.endif"
.3.endif.endif.endif.endif:
  %".151" = phi i1 [1, %".3.endif.endif.endif.if"], [0, %".3.endif.endif.endif.else"]
  br i1 %".151", label %".3.endif.endif.endif.endif.if", label %".3.endif.endif.endif.endif.else"
.3.endif.endif.endif.endif.if:
  %".153" = zext i8 5 to i64
  %".154" = and i64 %".153", 63
  %".155" = lshr i64 %"SymVar_0", %".154"
  %".156" = sext i64 %".155" to i128
  %".157" = sext i64 1015975030 to i128
  %".158" = mul i128 %".156", %".157"
  %".159" = trunc i128 %".158" to i64
  %".160" = and i64 7, %".159"
  %".161" = or i64 1, %".160"
  %".162" = trunc i64 %".161" to i32
  %".163" = zext i32 %".162" to i64
  %".164" = trunc i64 %".163" to i8
  %".165" = zext i8 %".164" to i64
  %".166" = and i64 %".165", 63
  %".167" = lshr i64 %"SymVar_0", %".166"
  %".168" = xor i64 810798164723513605, %".155"
  %".169" = sub i64 %"SymVar_0", 275339905
  %".170" = add i64 %".168", %".169"
  %".171" = zext i8 4 to i64
  %".172" = and i64 %".171", 63
  %".173" = lshr i64 %".170", %".172"
  %".174" = and i64 15, %".173"
  %".175" = or i64 1, %".174"
  %".176" = sub i64 64, %".175"
  %".177" = trunc i64 %".176" to i32
  %".178" = zext i32 %".177" to i64
  %".179" = trunc i64 %".178" to i8
  %".180" = zext i8 %".179" to i64
  %".181" = and i64 %".180", 63
  %".182" = lshr i64 %".167", %".181"
  %".183" = zext i8 4 to i64
  %".184" = and i64 %".183", 63
  %".185" = lshr i64 %".170", %".184"
  %".186" = and i64 15, %".185"
  %".187" = or i64 1, %".186"
  %".188" = trunc i64 %".187" to i32
  %".189" = zext i32 %".188" to i64
  %".190" = trunc i64 %".189" to i8
  %".191" = zext i8 %".190" to i64
  %".192" = and i64 %".191", 63
  %".193" = shl i64 %".167", %".192"
  %".194" = or i64 %".182", %".193"
  %".195" = and i64 15, %".194"
  %".196" = zext i8 3 to i64
  %".197" = and i64 %".196", 63
  %".198" = shl i64 %".195", %".197"
  %".199" = or i64 %".198", %".170"
  %".200" = and i64 15, %".199"
  %".201" = zext i8 3 to i64
  %".202" = and i64 %".201", 63
  %".203" = shl i64 %".200", %".202"
  %".204" = or i64 %".203", %".199"
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
  %".238" = zext i32 %".237" to i64
  %".239" = trunc i64 %".238" to i32
  %".240" = zext i32 %".239" to i64
  %".241" = trunc i64 %".240" to i32
  %".242" = zext i32 %".241" to i64
  %".243" = trunc i64 %".242" to i32
  %".244" = zext i32 %".243" to i64
  %".245" = trunc i64 %".244" to i32
  %".246" = zext i32 %".245" to i64
  %".247" = trunc i64 %".246" to i32
  %".248" = zext i32 %".247" to i64
  %".249" = trunc i64 %".248" to i32
  %".250" = zext i32 %".249" to i64
  %".251" = trunc i64 %".250" to i32
  %".252" = zext i32 %".251" to i64
  %".253" = trunc i64 %".252" to i32
  %".254" = trunc i32 %".253" to i8
  %".255" = zext i8 %".254" to i64
  %".256" = trunc i64 %".252" to i32
  %".257" = lshr i32 %".256", 8
  %".258" = trunc i32 %".257" to i8
  %".259" = zext i8 %".258" to i64
  %".260" = shl i64 %".259", 8
  %".261" = or i64 %".255", %".260"
  %".262" = trunc i64 %".252" to i32
  %".263" = lshr i32 %".262", 16
  %".264" = trunc i32 %".263" to i8
  %".265" = zext i8 %".264" to i64
  %".266" = shl i64 %".265", 16
  %".267" = or i64 %".261", %".266"
  %".268" = trunc i64 %".252" to i32
  %".269" = lshr i32 %".268", 24
  %".270" = trunc i32 %".269" to i8
  %".271" = zext i8 %".270" to i64
  %".272" = shl i64 %".271", 24
  %".273" = or i64 %".267", %".272"
  %".274" = lshr i64 %".204", 32
  %".275" = trunc i64 %".274" to i8
  %".276" = zext i8 %".275" to i32
  %".277" = lshr i64 %".204", 40
  %".278" = trunc i64 %".277" to i8
  %".279" = zext i8 %".278" to i32
  %".280" = shl i32 %".279", 8
  %".281" = or i32 %".276", %".280"
  %".282" = lshr i64 %".204", 48
  %".283" = trunc i64 %".282" to i8
  %".284" = zext i8 %".283" to i32
  %".285" = shl i32 %".284", 16
  %".286" = or i32 %".281", %".285"
  %".287" = lshr i64 %".204", 56
  %".288" = trunc i64 %".287" to i8
  %".289" = zext i8 %".288" to i32
  %".290" = shl i32 %".289", 24
  %".291" = or i32 %".286", %".290"
  %".292" = zext i32 %".291" to i64
  %".293" = trunc i64 %".292" to i32
  %".294" = zext i32 %".293" to i64
  %".295" = trunc i64 %".294" to i32
  %".296" = zext i32 %".295" to i64
  %".297" = trunc i64 %".296" to i32
  %".298" = zext i32 %".297" to i64
  %".299" = trunc i64 %".298" to i32
  %".300" = zext i32 %".299" to i64
  %".301" = trunc i64 %".300" to i32
  %".302" = zext i32 %".301" to i64
  %".303" = trunc i64 %".302" to i32
  %".304" = zext i32 %".303" to i64
  %".305" = trunc i64 %".304" to i32
  %".306" = zext i32 %".305" to i64
  %".307" = trunc i64 %".306" to i32
  %".308" = trunc i32 %".307" to i8
  %".309" = zext i8 %".308" to i64
  %".310" = shl i64 %".309", 32
  %".311" = or i64 %".273", %".310"
  %".312" = trunc i64 %".306" to i32
  %".313" = lshr i32 %".312", 8
  %".314" = trunc i32 %".313" to i8
  %".315" = zext i8 %".314" to i64
  %".316" = shl i64 %".315", 40
  %".317" = or i64 %".311", %".316"
  %".318" = trunc i64 %".306" to i32
  %".319" = lshr i32 %".318", 16
  %".320" = trunc i32 %".319" to i8
  %".321" = zext i8 %".320" to i64
  %".322" = shl i64 %".321", 48
  %".323" = or i64 %".317", %".322"
  %".324" = trunc i64 %".306" to i32
  %".325" = lshr i32 %".324", 24
  %".326" = trunc i32 %".325" to i8
  %".327" = zext i8 %".326" to i64
  %".328" = shl i64 %".327", 56
  %".329" = or i64 %".323", %".328"
  %".330" = add i64 %".170", %".155"
  %".331" = add i64 %".330", %"SymVar_0"
  %".332" = sext i64 %".331" to i128
  %".333" = sext i64 %".155" to i128
  %".334" = mul i128 %".332", %".333"
  %".335" = trunc i128 %".334" to i64
  %".336" = and i64 7, %".335"
  %".337" = zext i8 2 to i64
  %".338" = and i64 %".337", 63
  %".339" = shl i64 %".336", %".338"
  %".340" = or i64 %".339", %".155"
  %".341" = lshr i64 %".340", 56
  %".342" = trunc i64 %".341" to i8
  %".343" = zext i8 %".342" to i32
  %".344" = zext i32 %".343" to i64
  %".345" = trunc i64 %".344" to i8
  %".346" = zext i8 %".345" to i32
  %".347" = zext i32 %".346" to i64
  %".348" = trunc i64 %".347" to i8
  %".349" = zext i8 %".348" to i32
  %".350" = zext i32 %".349" to i64
  %".351" = trunc i64 %".350" to i8
  %".352" = zext i8 %".351" to i32
  %".353" = zext i32 %".352" to i64
  %".354" = trunc i64 %".353" to i8
  %".355" = zext i8 %".354" to i32
  %".356" = zext i32 %".355" to i64
  %".357" = trunc i64 %".356" to i8
  %".358" = zext i8 %".357" to i32
  %".359" = zext i32 %".358" to i64
  %".360" = trunc i64 %".359" to i8
  %".361" = zext i8 %".360" to i32
  %".362" = zext i32 %".361" to i64
  %".363" = trunc i64 %".362" to i8
  %".364" = zext i8 %".363" to i32
  %".365" = zext i32 %".364" to i64
  %".366" = trunc i64 %".365" to i8
  %".367" = zext i8 %".366" to i64
  %".368" = lshr i64 %".340", 8
  %".369" = trunc i64 %".368" to i8
  %".370" = zext i8 %".369" to i64
  %".371" = shl i64 %".370", 8
  %".372" = or i64 %".367", %".371"
  %".373" = lshr i64 %".340", 16
  %".374" = trunc i64 %".373" to i8
  %".375" = zext i8 %".374" to i64
  %".376" = shl i64 %".375", 16
  %".377" = or i64 %".372", %".376"
  %".378" = lshr i64 %".340", 24
  %".379" = trunc i64 %".378" to i8
  %".380" = zext i8 %".379" to i64
  %".381" = shl i64 %".380", 24
  %".382" = or i64 %".377", %".381"
  %".383" = lshr i64 %".340", 32
  %".384" = trunc i64 %".383" to i8
  %".385" = zext i8 %".384" to i64
  %".386" = shl i64 %".385", 32
  %".387" = or i64 %".382", %".386"
  %".388" = lshr i64 %".340", 40
  %".389" = trunc i64 %".388" to i8
  %".390" = zext i8 %".389" to i64
  %".391" = shl i64 %".390", 40
  %".392" = or i64 %".387", %".391"
  %".393" = lshr i64 %".340", 48
  %".394" = trunc i64 %".393" to i8
  %".395" = zext i8 %".394" to i64
  %".396" = shl i64 %".395", 48
  %".397" = or i64 %".392", %".396"
  %".398" = trunc i64 %".340" to i8
  %".399" = zext i8 %".398" to i32
  %".400" = zext i32 %".399" to i64
  %".401" = trunc i64 %".400" to i8
  %".402" = zext i8 %".401" to i32
  %".403" = zext i32 %".402" to i64
  %".404" = trunc i64 %".403" to i8
  %".405" = zext i8 %".404" to i32
  %".406" = zext i32 %".405" to i64
  %".407" = trunc i64 %".406" to i8
  %".408" = zext i8 %".407" to i32
  %".409" = zext i32 %".408" to i64
  %".410" = trunc i64 %".409" to i8
  %".411" = zext i8 %".410" to i64
  %".412" = shl i64 %".411", 56
  %".413" = or i64 %".397", %".412"
  %".414" = sub i64 %".329", %".413"
  %".415" = or i64 %".167", %".414"
  %".416" = and i64 63, %".414"
  %".417" = zext i8 4 to i64
  %".418" = and i64 %".417", 63
  %".419" = shl i64 %".416", %".418"
  %".420" = zext i8 %".366" to i64
  %".421" = zext i8 %".369" to i64
  %".422" = shl i64 %".421", 8
  %".423" = or i64 %".420", %".422"
  %".424" = zext i8 %".374" to i64
  %".425" = shl i64 %".424", 16
  %".426" = or i64 %".423", %".425"
  %".427" = zext i8 %".379" to i64
  %".428" = shl i64 %".427", 24
  %".429" = or i64 %".426", %".428"
  %".430" = zext i8 %".384" to i64
  %".431" = shl i64 %".430", 32
  %".432" = or i64 %".429", %".431"
  %".433" = zext i8 %".389" to i64
  %".434" = shl i64 %".433", 40
  %".435" = or i64 %".432", %".434"
  %".436" = zext i8 %".394" to i64
  %".437" = shl i64 %".436", 48
  %".438" = or i64 %".435", %".437"
  %".439" = zext i8 %".410" to i64
  %".440" = shl i64 %".439", 56
  %".441" = or i64 %".438", %".440"
  %".442" = or i64 %".419", %".441"
  %".443" = zext i8 %".254" to i64
  %".444" = zext i8 %".258" to i64
  %".445" = shl i64 %".444", 8
  %".446" = or i64 %".443", %".445"
  %".447" = zext i8 %".264" to i64
  %".448" = shl i64 %".447", 16
  %".449" = or i64 %".446", %".448"
  %".450" = zext i8 %".270" to i64
  %".451" = shl i64 %".450", 24
  %".452" = or i64 %".449", %".451"
  %".453" = zext i8 %".308" to i64
  %".454" = shl i64 %".453", 32
  %".455" = or i64 %".452", %".454"
  %".456" = zext i8 %".314" to i64
  %".457" = shl i64 %".456", 40
  %".458" = or i64 %".455", %".457"
  %".459" = zext i8 %".320" to i64
  %".460" = shl i64 %".459", 48
  %".461" = or i64 %".458", %".460"
  %".462" = zext i8 %".326" to i64
  %".463" = shl i64 %".462", 56
  %".464" = or i64 %".461", %".463"
  %".465" = zext i8 2 to i64
  %".466" = and i64 %".465", 63
  %".467" = lshr i64 %".464", %".466"
  %".468" = and i64 7, %".467"
  %".469" = or i64 1, %".468"
  %".470" = trunc i64 %".469" to i32
  %".471" = zext i32 %".470" to i64
  %".472" = trunc i64 %".471" to i8
  %".473" = zext i8 %".472" to i64
  %".474" = and i64 %".473", 63
  %".475" = shl i64 %".442", %".474"
  %".476" = add i64 %".415", %".475"
  br label %".3.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.else:
  %".478" = zext i8 5 to i64
  %".479" = and i64 %".478", 63
  %".480" = lshr i64 %"SymVar_0", %".479"
  %".481" = xor i64 810798164723513605, %".480"
  %".482" = sub i64 %"SymVar_0", 275339905
  %".483" = add i64 %".481", %".482"
  %".484" = add i64 %".483", %".480"
  %".485" = add i64 %".484", %"SymVar_0"
  %".486" = sext i64 %".485" to i128
  %".487" = sext i64 %".480" to i128
  %".488" = mul i128 %".486", %".487"
  %".489" = trunc i128 %".488" to i64
  %".490" = and i64 7, %".489"
  %".491" = zext i8 2 to i64
  %".492" = and i64 %".491", 63
  %".493" = shl i64 %".490", %".492"
  %".494" = or i64 %".493", %".480"
  %".495" = sub i64 %".494", %".485"
  %".496" = and i64 31, %".495"
  %".497" = zext i8 3 to i64
  %".498" = and i64 %".497", 63
  %".499" = shl i64 %".496", %".498"
  %".500" = sext i64 %".480" to i128
  %".501" = sext i64 1015975030 to i128
  %".502" = mul i128 %".500", %".501"
  %".503" = trunc i128 %".502" to i64
  %".504" = and i64 7, %".503"
  %".505" = or i64 1, %".504"
  %".506" = trunc i64 %".505" to i32
  %".507" = zext i32 %".506" to i64
  %".508" = trunc i64 %".507" to i8
  %".509" = zext i8 %".508" to i64
  %".510" = and i64 %".509", 63
  %".511" = lshr i64 %"SymVar_0", %".510"
  %".512" = or i64 %".499", %".511"
  %".513" = zext i8 4 to i64
  %".514" = and i64 %".513", 63
  %".515" = lshr i64 %".483", %".514"
  %".516" = and i64 15, %".515"
  %".517" = or i64 1, %".516"
  %".518" = sub i64 64, %".517"
  %".519" = trunc i64 %".518" to i32
  %".520" = zext i32 %".519" to i64
  %".521" = trunc i64 %".520" to i8
  %".522" = zext i8 %".521" to i64
  %".523" = and i64 %".522", 63
  %".524" = lshr i64 %".511", %".523"
  %".525" = zext i8 4 to i64
  %".526" = and i64 %".525", 63
  %".527" = lshr i64 %".483", %".526"
  %".528" = and i64 15, %".527"
  %".529" = or i64 1, %".528"
  %".530" = trunc i64 %".529" to i32
  %".531" = zext i32 %".530" to i64
  %".532" = trunc i64 %".531" to i8
  %".533" = zext i8 %".532" to i64
  %".534" = and i64 %".533", 63
  %".535" = shl i64 %".511", %".534"
  %".536" = or i64 %".524", %".535"
  %".537" = and i64 15, %".536"
  %".538" = zext i8 3 to i64
  %".539" = and i64 %".538", 63
  %".540" = shl i64 %".537", %".539"
  %".541" = or i64 %".540", %".483"
  %".542" = trunc i64 %".541" to i8
  %".543" = zext i8 %".542" to i32
  %".544" = lshr i64 %".541", 8
  %".545" = trunc i64 %".544" to i8
  %".546" = zext i8 %".545" to i32
  %".547" = shl i32 %".546", 8
  %".548" = or i32 %".543", %".547"
  %".549" = lshr i64 %".541", 16
  %".550" = trunc i64 %".549" to i8
  %".551" = zext i8 %".550" to i32
  %".552" = shl i32 %".551", 16
  %".553" = or i32 %".548", %".552"
  %".554" = lshr i64 %".541", 24
  %".555" = trunc i64 %".554" to i8
  %".556" = zext i8 %".555" to i32
  %".557" = shl i32 %".556", 24
  %".558" = or i32 %".553", %".557"
  %".559" = zext i32 %".558" to i64
  %".560" = trunc i64 %".559" to i32
  %".561" = zext i32 %".560" to i64
  %".562" = trunc i64 %".561" to i32
  %".563" = zext i32 %".562" to i64
  %".564" = trunc i64 %".563" to i32
  %".565" = zext i32 %".564" to i64
  %".566" = trunc i64 %".565" to i32
  %".567" = zext i32 %".566" to i64
  %".568" = trunc i64 %".567" to i32
  %".569" = zext i32 %".568" to i64
  %".570" = trunc i64 %".569" to i32
  %".571" = zext i32 %".570" to i64
  %".572" = trunc i64 %".571" to i32
  %".573" = zext i32 %".572" to i64
  %".574" = trunc i64 %".573" to i32
  %".575" = zext i32 %".574" to i64
  %".576" = trunc i64 %".575" to i32
  %".577" = zext i32 %".576" to i64
  %".578" = trunc i64 %".577" to i32
  %".579" = zext i32 %".578" to i64
  %".580" = trunc i64 %".579" to i32
  %".581" = zext i32 %".580" to i64
  %".582" = trunc i64 %".581" to i32
  %".583" = zext i32 %".582" to i64
  %".584" = trunc i64 %".583" to i32
  %".585" = zext i32 %".584" to i64
  %".586" = trunc i64 %".585" to i32
  %".587" = zext i32 %".586" to i64
  %".588" = trunc i64 %".587" to i32
  %".589" = zext i32 %".588" to i64
  %".590" = trunc i64 %".589" to i32
  %".591" = trunc i32 %".590" to i8
  %".592" = zext i8 %".591" to i64
  %".593" = trunc i64 %".589" to i32
  %".594" = lshr i32 %".593", 8
  %".595" = trunc i32 %".594" to i8
  %".596" = zext i8 %".595" to i64
  %".597" = shl i64 %".596", 8
  %".598" = or i64 %".592", %".597"
  %".599" = trunc i64 %".589" to i32
  %".600" = lshr i32 %".599", 16
  %".601" = trunc i32 %".600" to i8
  %".602" = zext i8 %".601" to i64
  %".603" = shl i64 %".602", 16
  %".604" = or i64 %".598", %".603"
  %".605" = trunc i64 %".589" to i32
  %".606" = lshr i32 %".605", 24
  %".607" = trunc i32 %".606" to i8
  %".608" = zext i8 %".607" to i64
  %".609" = shl i64 %".608", 24
  %".610" = or i64 %".604", %".609"
  %".611" = lshr i64 %".541", 32
  %".612" = trunc i64 %".611" to i8
  %".613" = zext i8 %".612" to i32
  %".614" = lshr i64 %".541", 40
  %".615" = trunc i64 %".614" to i8
  %".616" = zext i8 %".615" to i32
  %".617" = shl i32 %".616", 8
  %".618" = or i32 %".613", %".617"
  %".619" = lshr i64 %".541", 48
  %".620" = trunc i64 %".619" to i8
  %".621" = zext i8 %".620" to i32
  %".622" = shl i32 %".621", 16
  %".623" = or i32 %".618", %".622"
  %".624" = lshr i64 %".541", 56
  %".625" = trunc i64 %".624" to i8
  %".626" = zext i8 %".625" to i32
  %".627" = shl i32 %".626", 24
  %".628" = or i32 %".623", %".627"
  %".629" = zext i32 %".628" to i64
  %".630" = trunc i64 %".629" to i32
  %".631" = zext i32 %".630" to i64
  %".632" = trunc i64 %".631" to i32
  %".633" = zext i32 %".632" to i64
  %".634" = trunc i64 %".633" to i32
  %".635" = zext i32 %".634" to i64
  %".636" = trunc i64 %".635" to i32
  %".637" = zext i32 %".636" to i64
  %".638" = trunc i64 %".637" to i32
  %".639" = zext i32 %".638" to i64
  %".640" = trunc i64 %".639" to i32
  %".641" = zext i32 %".640" to i64
  %".642" = trunc i64 %".641" to i32
  %".643" = zext i32 %".642" to i64
  %".644" = trunc i64 %".643" to i32
  %".645" = trunc i32 %".644" to i8
  %".646" = zext i8 %".645" to i64
  %".647" = shl i64 %".646", 32
  %".648" = or i64 %".610", %".647"
  %".649" = trunc i64 %".643" to i32
  %".650" = lshr i32 %".649", 8
  %".651" = trunc i32 %".650" to i8
  %".652" = zext i8 %".651" to i64
  %".653" = shl i64 %".652", 40
  %".654" = or i64 %".648", %".653"
  %".655" = trunc i64 %".643" to i32
  %".656" = lshr i32 %".655", 16
  %".657" = trunc i32 %".656" to i8
  %".658" = zext i8 %".657" to i64
  %".659" = shl i64 %".658", 48
  %".660" = or i64 %".654", %".659"
  %".661" = trunc i64 %".643" to i32
  %".662" = lshr i32 %".661", 24
  %".663" = trunc i32 %".662" to i8
  %".664" = zext i8 %".663" to i64
  %".665" = shl i64 %".664", 56
  %".666" = or i64 %".660", %".665"
  %".667" = and i64 31, %".541"
  %".668" = zext i8 4 to i64
  %".669" = and i64 %".668", 63
  %".670" = shl i64 %".667", %".669"
  %".671" = or i64 %".670", %".494"
  %".672" = sub i64 %".666", %".671"
  %".673" = or i64 %".512", %".672"
  %".674" = and i64 63, %".672"
  %".675" = zext i8 4 to i64
  %".676" = and i64 %".675", 63
  %".677" = shl i64 %".674", %".676"
  %".678" = or i64 %".677", %".671"
  %".679" = zext i8 %".591" to i64
  %".680" = zext i8 %".595" to i64
  %".681" = shl i64 %".680", 8
  %".682" = or i64 %".679", %".681"
  %".683" = zext i8 %".601" to i64
  %".684" = shl i64 %".683", 16
  %".685" = or i64 %".682", %".684"
  %".686" = zext i8 %".607" to i64
  %".687" = shl i64 %".686", 24
  %".688" = or i64 %".685", %".687"
  %".689" = zext i8 %".645" to i64
  %".690" = shl i64 %".689", 32
  %".691" = or i64 %".688", %".690"
  %".692" = zext i8 %".651" to i64
  %".693" = shl i64 %".692", 40
  %".694" = or i64 %".691", %".693"
  %".695" = zext i8 %".657" to i64
  %".696" = shl i64 %".695", 48
  %".697" = or i64 %".694", %".696"
  %".698" = zext i8 %".663" to i64
  %".699" = shl i64 %".698", 56
  %".700" = or i64 %".697", %".699"
  %".701" = zext i8 2 to i64
  %".702" = and i64 %".701", 63
  %".703" = lshr i64 %".700", %".702"
  %".704" = and i64 7, %".703"
  %".705" = or i64 1, %".704"
  %".706" = trunc i64 %".705" to i32
  %".707" = zext i32 %".706" to i64
  %".708" = trunc i64 %".707" to i8
  %".709" = zext i8 %".708" to i64
  %".710" = and i64 %".709", 63
  %".711" = shl i64 %".678", %".710"
  %".712" = add i64 %".673", %".711"
  br label %".3.endif.endif.endif.endif.endif"
.3.endif.endif.endif.endif.endif:
  %".714" = phi i64 [%".476", %".3.endif.endif.endif.endif.if"], [%".712", %".3.endif.endif.endif.endif.else"]
  ret i64 %".714"
}
