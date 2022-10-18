<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.6.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="50" name="dxf" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="53" name="tGND_GNDA" color="7" fill="9" visible="no" active="no"/>
<layer number="54" name="bGND_GNDA" color="1" fill="9" visible="no" active="no"/>
<layer number="56" name="wert" color="7" fill="1" visible="no" active="no"/>
<layer number="57" name="tCAD" color="7" fill="1" visible="no" active="no"/>
<layer number="59" name="tFaceplate" color="11" fill="1" visible="no" active="no"/>
<layer number="60" name="bFaceplate" color="13" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
<layer number="99" name="SpiceOrder" color="7" fill="1" visible="no" active="no"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="Lab01">
<packages>
<package name="PJ-102A">
<text x="-11.43" y="-11.43" size="1.27" layer="25" font="vector">&gt;NAME</text>
<wire x1="-14.55824375" y1="-0.052128125" x2="-14.57559375" y2="-9.07015" width="0.127" layer="21"/>
<wire x1="-14.56" y1="-0.045" x2="0.04" y2="-0.045" width="0.127" layer="21"/>
<wire x1="-15.24" y1="-10.16" x2="1.27" y2="-10.16" width="0.127" layer="39"/>
<wire x1="-15.24" y1="1.27" x2="-15.24" y2="-10.16" width="0.127" layer="39"/>
<wire x1="0.04" y1="-0.045" x2="0.04" y2="-9.045" width="0.127" layer="21"/>
<wire x1="0.04" y1="-9.045" x2="-14.56" y2="-9.045" width="0.127" layer="21"/>
<wire x1="1.27" y1="-10.16" x2="1.27" y2="1.27" width="0.127" layer="39"/>
<wire x1="1.27" y1="1.27" x2="-15.24" y2="1.27" width="0.127" layer="39"/>
<pad name="RING" x="-6.77" y="-4.345" drill="2" diameter="3.5" rot="R270"/>
<pad name="RING_SW" x="-3.87" y="-9.045" drill="2" diameter="3.5" rot="R270"/>
<pad name="TIP" x="-0.87" y="-4.345" drill="2" diameter="3.5" rot="R270"/>
</package>
<package name="BUTTON-TACTILE-SQUARE-ADAFRUIT1010">
<description>Square, colorful tactile button from adafruit
&lt;br&gt;

The size of the faceplate opening is 0.5mm larger than it "should" be to allow for small misalignments between the faceplace and board.</description>
<text x="-2.54" y="-7.62" size="1.27" layer="25" font="vector">&gt;NAME</text>
<wire x1="-5" y1="-5" x2="-5" y2="5" width="0.127" layer="21"/>
<wire x1="-5" y1="5" x2="5" y2="5" width="0.127" layer="21"/>
<rectangle x1="-7.5" y1="-7" x2="7.5" y2="7" layer="39"/>
<hole x="0" y="-4.5" drill="1.4"/>
<hole x="0" y="4.5" drill="1.4"/>
<wire x1="5" y1="-5" x2="-5" y2="-5" width="0.127" layer="21"/>
<wire x1="5" y1="5" x2="5" y2="-5" width="0.127" layer="21"/>
<pad name="P" x="-6" y="2.5" drill="1.3" shape="square"/>
<pad name="P2" x="6" y="2.5" drill="1.3"/>
<pad name="S" x="-6" y="-2.5" drill="1.3"/>
<pad name="S2" x="6" y="-2.5" drill="1.3"/>
</package>
<package name="LED5MM">
<description>&lt;B&gt;LED&lt;/B&gt;&lt;p&gt;
5 mm, round</description>
<wire x1="-1.143" y1="0" x2="0" y2="1.143" width="0.1524" layer="51" curve="-90" cap="flat"/>
<wire x1="-1.651" y1="0" x2="0" y2="1.651" width="0.1524" layer="51" curve="-90" cap="flat"/>
<wire x1="-2.159" y1="0" x2="0" y2="2.159" width="0.1524" layer="51" curve="-90" cap="flat"/>
<wire x1="0" y1="-1.143" x2="1.143" y2="0" width="0.1524" layer="51" curve="90" cap="flat"/>
<wire x1="0" y1="-1.651" x2="1.651" y2="0" width="0.1524" layer="51" curve="90" cap="flat"/>
<wire x1="0" y1="-2.159" x2="2.159" y2="0" width="0.1524" layer="51" curve="90" cap="flat"/>
<circle x="0" y="0" radius="2.54" width="0.1524" layer="21"/>
<circle x="0" y="0" radius="3.5921" width="0.127" layer="39"/>
<wire x1="2.54" y1="-1.905" x2="2.54" y2="1.905" width="0.2032" layer="21"/>
<wire x1="2.54" y1="-1.905" x2="2.54" y2="1.905" width="0.254" layer="21" curve="-286.260205" cap="flat"/>
<text x="3.175" y="0.5334" size="1.27" layer="25" font="vector">&gt;NAME</text>
<pad name="A" x="-1.27" y="0" drill="0.8128" diameter="1.6764" shape="octagon"/>
<pad name="K" x="1.27" y="0" drill="0.8128" diameter="1.6764" shape="octagon"/>
<text x="3.175" y="-2.0066" size="1.27" layer="27" font="vector">&gt;VALUE</text>
</package>
<package name="RESAD1160W55L680D260_HS">
<description>Resistor, Axial;11.60 mm C X 0.55 mm W 6.80 mm L X 2.60 mm Dia body&lt;p&gt;&lt;i&gt;PCB Libraries Packages&lt;/i&gt;</description>
<wire x1="-2.27" y1="1.3" x2="-3.4" y2="1.3" width="0.12" layer="21"/>
<wire x1="-3.4" y1="-1.3" x2="-2.27" y2="-1.3" width="0.12" layer="21"/>
<wire x1="-3.4" y1="-1.3" x2="-3.4" y2="0" width="0.12" layer="51"/>
<wire x1="-3.4" y1="0" x2="-3.4" y2="1.3" width="0.12" layer="51"/>
<wire x1="-3.4" y1="0" x2="-5.02" y2="0" width="0.12" layer="21"/>
<wire x1="-3.4" y1="0" x2="-5.2" y2="0" width="0.12" layer="51"/>
<wire x1="-3.4" y1="1.3" x2="-3.4" y2="-1.3" width="0.12" layer="21"/>
<wire x1="-3.4" y1="1.3" x2="3.4" y2="1.3" width="0.12" layer="51"/>
<wire x1="-3.65" y1="-0.85" x2="-6.65" y2="-0.85" width="0.05" layer="39"/>
<wire x1="-3.65" y1="-1.55" x2="-3.65" y2="-0.85" width="0.05" layer="39"/>
<wire x1="-3.65" y1="0.85" x2="-3.65" y2="1.55" width="0.05" layer="39"/>
<wire x1="-3.65" y1="1.55" x2="3.65" y2="1.55" width="0.05" layer="39"/>
<wire x1="-6.65" y1="-0.85" x2="-6.65" y2="0.85" width="0.05" layer="39"/>
<wire x1="-6.65" y1="0.85" x2="-3.65" y2="0.85" width="0.05" layer="39"/>
<circle x="0" y="0" radius="0.25" width="0.05" layer="39"/>
<wire x1="0" y1="0.35" x2="0" y2="-0.35" width="0.05" layer="39"/>
<polygon width="0.01" layer="29">
<vertex x="-5.205" y="0"/>
<vertex x="-5.214" y="0.1033"/>
<vertex x="-5.2409" y="0.2035"/>
<vertex x="-5.2847" y="0.2975"/>
<vertex x="-5.3442" y="0.3825"/>
<vertex x="-5.4175" y="0.4558"/>
<vertex x="-5.5025" y="0.5153"/>
<vertex x="-5.5965" y="0.5591"/>
<vertex x="-5.6967" y="0.586"/>
<vertex x="-5.8" y="0.595"/>
<vertex x="-5.9033" y="0.586"/>
<vertex x="-6.0035" y="0.5591"/>
<vertex x="-6.0975" y="0.5153"/>
<vertex x="-6.1825" y="0.4558"/>
<vertex x="-6.2558" y="0.3825"/>
<vertex x="-6.3153" y="0.2975"/>
<vertex x="-6.3591" y="0.2035"/>
<vertex x="-6.386" y="0.1033"/>
<vertex x="-6.395" y="0"/>
<vertex x="-6.386" y="-0.1033"/>
<vertex x="-6.3591" y="-0.2035"/>
<vertex x="-6.3153" y="-0.2975"/>
<vertex x="-6.2558" y="-0.3825"/>
<vertex x="-6.1825" y="-0.4558"/>
<vertex x="-6.0975" y="-0.5153"/>
<vertex x="-6.0035" y="-0.5591"/>
<vertex x="-5.9033" y="-0.586"/>
<vertex x="-5.8" y="-0.595"/>
<vertex x="-5.6967" y="-0.586"/>
<vertex x="-5.5965" y="-0.5591"/>
<vertex x="-5.5025" y="-0.5153"/>
<vertex x="-5.4175" y="-0.4558"/>
<vertex x="-5.3442" y="-0.3825"/>
<vertex x="-5.2847" y="-0.2975"/>
<vertex x="-5.2409" y="-0.2035"/>
<vertex x="-5.214" y="-0.1033"/>
</polygon>
<polygon width="0.01" layer="29">
<vertex x="6.395" y="0"/>
<vertex x="6.386" y="0.1033"/>
<vertex x="6.3591" y="0.2035"/>
<vertex x="6.3153" y="0.2975"/>
<vertex x="6.2558" y="0.3825"/>
<vertex x="6.1825" y="0.4558"/>
<vertex x="6.0975" y="0.5153"/>
<vertex x="6.0035" y="0.5591"/>
<vertex x="5.9033" y="0.586"/>
<vertex x="5.8" y="0.595"/>
<vertex x="5.6967" y="0.586"/>
<vertex x="5.5965" y="0.5591"/>
<vertex x="5.5025" y="0.5153"/>
<vertex x="5.4175" y="0.4558"/>
<vertex x="5.3442" y="0.3825"/>
<vertex x="5.2847" y="0.2975"/>
<vertex x="5.2409" y="0.2035"/>
<vertex x="5.214" y="0.1033"/>
<vertex x="5.205" y="0"/>
<vertex x="5.214" y="-0.1033"/>
<vertex x="5.2409" y="-0.2035"/>
<vertex x="5.2847" y="-0.2975"/>
<vertex x="5.3442" y="-0.3825"/>
<vertex x="5.4175" y="-0.4558"/>
<vertex x="5.5025" y="-0.5153"/>
<vertex x="5.5965" y="-0.5591"/>
<vertex x="5.6967" y="-0.586"/>
<vertex x="5.8" y="-0.595"/>
<vertex x="5.9033" y="-0.586"/>
<vertex x="6.0035" y="-0.5591"/>
<vertex x="6.0975" y="-0.5153"/>
<vertex x="6.1825" y="-0.4558"/>
<vertex x="6.2558" y="-0.3825"/>
<vertex x="6.3153" y="-0.2975"/>
<vertex x="6.3591" y="-0.2035"/>
<vertex x="6.386" y="-0.1033"/>
</polygon>
<wire x1="0.35" y1="0" x2="-0.35" y2="0" width="0.05" layer="39"/>
<wire x1="2.27" y1="1.3" x2="3.4" y2="1.3" width="0.12" layer="21"/>
<wire x1="3.4" y1="-1.3" x2="-3.4" y2="-1.3" width="0.12" layer="51"/>
<wire x1="3.4" y1="-1.3" x2="2.27" y2="-1.3" width="0.12" layer="21"/>
<wire x1="3.4" y1="0" x2="3.4" y2="-1.3" width="0.12" layer="51"/>
<wire x1="3.4" y1="0" x2="5.02" y2="0" width="0.12" layer="21"/>
<wire x1="3.4" y1="0" x2="5.2" y2="0" width="0.12" layer="51"/>
<wire x1="3.4" y1="1.3" x2="3.4" y2="-1.3" width="0.12" layer="21"/>
<wire x1="3.4" y1="1.3" x2="3.4" y2="0" width="0.12" layer="51"/>
<wire x1="3.65" y1="-0.85" x2="3.65" y2="-1.55" width="0.05" layer="39"/>
<wire x1="3.65" y1="-1.55" x2="-3.65" y2="-1.55" width="0.05" layer="39"/>
<wire x1="3.65" y1="0.85" x2="6.65" y2="0.85" width="0.05" layer="39"/>
<wire x1="3.65" y1="1.55" x2="3.65" y2="0.85" width="0.05" layer="39"/>
<wire x1="6.65" y1="-0.85" x2="3.65" y2="-0.85" width="0.05" layer="39"/>
<wire x1="6.65" y1="0.85" x2="6.65" y2="-0.85" width="0.05" layer="39"/>
<pad name="1" x="-5.8" y="0" drill="0.8" diameter="1.2" rot="R80" stop="no" first="yes"/>
<pad name="2" x="5.8" y="0" drill="0.8" diameter="1.2" rot="R80" stop="no"/>
<text x="0" y="0" size="1.27" layer="25" font="vector">&gt;NAME</text>
<text x="0" y="-2.54" size="1.27" layer="27" font="vector">&gt;VALUE</text>
</package>
</packages>
<symbols>
<symbol name="FRAME_B_L">
<frame x1="0" y1="0" x2="431.8" y2="279.4" columns="9" rows="6" layer="94" border-bottom="no"/>
</symbol>
<symbol name="DOCFIELD">
<wire x1="0" y1="0" x2="0" y2="5.08" width="0.1016" layer="94"/>
<wire x1="0" y1="0" x2="71.12" y2="0" width="0.1016" layer="94"/>
<wire x1="0" y1="15.24" x2="0" y2="22.86" width="0.1016" layer="94"/>
<wire x1="0" y1="22.86" x2="0" y2="35.56" width="0.1016" layer="94"/>
<wire x1="0" y1="22.86" x2="101.6" y2="22.86" width="0.1016" layer="94"/>
<wire x1="0" y1="5.08" x2="0" y2="15.24" width="0.1016" layer="94"/>
<wire x1="0" y1="5.08" x2="71.12" y2="5.08" width="0.1016" layer="94"/>
<text x="1.27" y="1.27" size="2.54" layer="94">Date:</text>
<text x="1.27" y="11.43" size="2.54" layer="94">Document Number:</text>
<text x="1.27" y="19.05" size="2.54" layer="94">TITLE:</text>
<wire x1="101.6" y1="15.24" x2="101.6" y2="5.08" width="0.1016" layer="94"/>
<wire x1="101.6" y1="15.24" x2="87.63" y2="15.24" width="0.1016" layer="94"/>
<wire x1="101.6" y1="22.86" x2="101.6" y2="15.24" width="0.1016" layer="94"/>
<wire x1="101.6" y1="35.56" x2="0" y2="35.56" width="0.1016" layer="94"/>
<wire x1="101.6" y1="35.56" x2="101.6" y2="22.86" width="0.1016" layer="94"/>
<wire x1="101.6" y1="5.08" x2="101.6" y2="0" width="0.1016" layer="94"/>
<text x="12.7" y="1.27" size="2.54" layer="94">&gt;LAST_DATE_TIME</text>
<text x="17.78" y="19.05" size="2.54" layer="94">&gt;DRAWING_NAME</text>
<wire x1="71.12" y1="0" x2="101.6" y2="0" width="0.1016" layer="94"/>
<wire x1="71.12" y1="5.08" x2="71.12" y2="0" width="0.1016" layer="94"/>
<wire x1="71.12" y1="5.08" x2="87.63" y2="5.08" width="0.1016" layer="94"/>
<text x="72.39" y="1.27" size="2.54" layer="94">Sheet:</text>
<text x="86.36" y="1.27" size="2.54" layer="94">&gt;SHEET</text>
<wire x1="87.63" y1="15.24" x2="0" y2="15.24" width="0.1016" layer="94"/>
<wire x1="87.63" y1="15.24" x2="87.63" y2="5.08" width="0.1016" layer="94"/>
<wire x1="87.63" y1="5.08" x2="101.6" y2="5.08" width="0.1016" layer="94"/>
<text x="88.9" y="11.43" size="2.54" layer="94">REV:</text>
</symbol>
<symbol name="POWERJACK-1">
<wire x1="-1.27" y1="2.54" x2="0" y2="1.905" width="0.254" layer="94"/>
<text x="-2.54" y="5.08" size="1.27" layer="95">&gt;NAME</text>
<wire x1="0" y1="-1.27" x2="-1.27" y2="-2.54" width="0.254" layer="94"/>
<wire x1="0" y1="1.905" x2="2.54" y2="1.905" width="0.254" layer="94"/>
<wire x1="0" y1="3.175" x2="-1.27" y2="2.54" width="0.254" layer="94"/>
<wire x1="1.27" y1="-2.54" x2="0" y2="-1.27" width="0.254" layer="94"/>
<wire x1="2.54" y1="-2.54" x2="1.27" y2="-2.54" width="0.254" layer="94"/>
<wire x1="2.54" y1="0" x2="2.54" y2="-1.27" width="0.254" layer="94"/>
<wire x1="2.54" y1="1.905" x2="2.54" y2="3.175" width="0.254" layer="94"/>
<wire x1="2.54" y1="3.175" x2="0" y2="3.175" width="0.254" layer="94"/>
<pin name="RING" x="5.08" y="-2.54" visible="off" length="short" rot="R180"/>
<pin name="RING_SW" x="5.08" y="0" visible="off" length="short" rot="R180"/>
<pin name="TIP" x="5.08" y="2.54" visible="off" length="short" rot="R180"/>
</symbol>
<symbol name="TS2">
<wire x1="-1.27" y1="0" x2="-0.635" y2="0" width="0.1524" layer="94"/>
<wire x1="-2.54" y1="0" x2="-1.905" y2="0" width="0.1524" layer="94"/>
<wire x1="-4.445" y1="-1.905" x2="-3.175" y2="-1.905" width="0.254" layer="94"/>
<wire x1="-4.445" y1="0" x2="-3.175" y2="0" width="0.1524" layer="94"/>
<wire x1="-4.445" y1="0" x2="-4.445" y2="-1.905" width="0.254" layer="94"/>
<wire x1="-4.445" y1="1.905" x2="-3.175" y2="1.905" width="0.254" layer="94"/>
<wire x1="-4.445" y1="1.905" x2="-4.445" y2="0" width="0.254" layer="94"/>
<text x="-6.35" y="-2.54" size="1.778" layer="95" rot="R90">&gt;NAME</text>
<wire x1="0" y1="-2.54" x2="-1.27" y2="1.905" width="0.254" layer="94"/>
<circle x="0" y="-2.54" radius="0.127" width="0.4064" layer="94"/>
<wire x1="0" y1="1.905" x2="0" y2="2.54" width="0.254" layer="94"/>
<circle x="0" y="2.54" radius="0.127" width="0.4064" layer="94"/>
<wire x1="2.54" y1="-2.54" x2="0" y2="-2.54" width="0.1524" layer="94"/>
<wire x1="2.54" y1="2.54" x2="0" y2="2.54" width="0.1524" layer="94"/>
<pin name="P" x="0" y="-5.08" visible="pad" length="short" direction="pas" swaplevel="2" rot="R90"/>
<pin name="P1" x="2.54" y="-5.08" visible="pad" length="short" direction="pas" swaplevel="2" rot="R90"/>
<pin name="S" x="0" y="5.08" visible="pad" length="short" direction="pas" swaplevel="1" rot="R270"/>
<pin name="S1" x="2.54" y="5.08" visible="pad" length="short" direction="pas" swaplevel="1" rot="R270"/>
</symbol>
<symbol name="LED">
<wire x1="-1.905" y1="-1.905" x2="-3.302" y2="-3.302" width="0.1524" layer="94"/>
<wire x1="-2.032" y1="-0.762" x2="-3.429" y2="-2.159" width="0.1524" layer="94"/>
<wire x1="0" y1="-2.54" x2="-1.27" y2="-2.54" width="0.254" layer="94"/>
<wire x1="0" y1="-2.54" x2="-1.27" y2="0" width="0.254" layer="94"/>
<wire x1="0" y1="0" x2="-1.27" y2="0" width="0.254" layer="94"/>
<wire x1="0" y1="0" x2="0" y2="-2.54" width="0.1524" layer="94"/>
<polygon width="0.1524" layer="94">
<vertex x="-3.429" y="-2.159"/>
<vertex x="-3.048" y="-1.27"/>
<vertex x="-2.54" y="-1.778"/>
</polygon>
<polygon width="0.1524" layer="94">
<vertex x="-3.302" y="-3.302"/>
<vertex x="-2.921" y="-2.413"/>
<vertex x="-2.413" y="-2.921"/>
</polygon>
<wire x1="1.27" y1="-2.54" x2="0" y2="-2.54" width="0.254" layer="94"/>
<wire x1="1.27" y1="0" x2="0" y2="-2.54" width="0.254" layer="94"/>
<wire x1="1.27" y1="0" x2="0" y2="0" width="0.254" layer="94"/>
<text x="3.556" y="-4.572" size="1.778" layer="95" rot="R90">&gt;NAME</text>
<text x="5.715" y="-4.572" size="1.778" layer="96" rot="R90">&gt;VALUE</text>
<pin name="A" x="0" y="2.54" visible="off" length="short" direction="pas" rot="R270"/>
<pin name="C" x="0" y="-5.08" visible="off" length="short" direction="pas" rot="R90"/>
</symbol>
<symbol name="RESISTOR">
<wire x1="-0.254" y1="-1.016" x2="0.381" y2="1.016" width="0.2032" layer="94"/>
<wire x1="-0.889" y1="1.016" x2="-0.254" y2="-1.016" width="0.2032" layer="94"/>
<wire x1="-1.524" y1="-1.016" x2="-0.889" y2="1.016" width="0.2032" layer="94"/>
<wire x1="-2.159" y1="1.016" x2="-1.524" y2="-1.016" width="0.2032" layer="94"/>
<wire x1="-2.54" y1="0" x2="-2.159" y2="1.016" width="0.2032" layer="94"/>
<text x="-3.81" y="-3.302" size="1.778" layer="96">&gt;VALUE</text>
<text x="-3.81" y="1.4986" size="1.778" layer="95">&gt;NAME</text>
<wire x1="0.381" y1="1.016" x2="1.016" y2="-1.016" width="0.2032" layer="94"/>
<wire x1="1.016" y1="-1.016" x2="1.651" y2="1.016" width="0.2032" layer="94"/>
<wire x1="1.651" y1="1.016" x2="2.286" y2="-1.016" width="0.2032" layer="94"/>
<wire x1="2.286" y1="-1.016" x2="2.54" y2="0" width="0.2032" layer="94"/>
<pin name="1" x="-5.08" y="0" visible="off" length="short" direction="pas" swaplevel="1"/>
<pin name="2" x="5.08" y="0" visible="off" length="short" direction="pas" swaplevel="1" rot="R180"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="FRAME_B_L" prefix="FRAME">
<description>&lt;b&gt;FRAME&lt;/b&gt; B Size , 11 x 17 INCH, Landscape&lt;p&gt;</description>
<gates>
<gate name="G$1" symbol="FRAME_B_L" x="0" y="0" addlevel="always"/>
<gate name="G$2" symbol="DOCFIELD" x="325.12" y="0" addlevel="always"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name="">
<attribute name="CREATOR" value="Unknown"/>
<attribute name="DIST" value="Unknown"/>
<attribute name="DISTPN" value="Unknown"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="2.1MMJACK" prefix="J">
<description>2.1mm x 5.5mm THM DC jack with internal switch. Digikey part #PJ-102A, 4UCON part #05537 &lt;br&gt;
2.1mm x 5.5mm SMT DC jack with internal switch. Digikey part #PJ-002A-SMT, 4UCON part #03267
&lt;p&gt;By microbuilder.eu &amp; adafruit.com&lt;/p&gt;</description>
<gates>
<gate name="G$1" symbol="POWERJACK-1" x="0" y="0"/>
</gates>
<devices>
<device name="THM" package="PJ-102A">
<connects>
<connect gate="G$1" pin="RING" pad="RING"/>
<connect gate="G$1" pin="RING_SW" pad="RING_SW"/>
<connect gate="G$1" pin="TIP" pad="TIP"/>
</connects>
<technologies>
<technology name="">
<attribute name="CREATOR" value="Swanson"/>
<attribute name="DIST" value="Digikey"/>
<attribute name="DISTPN" value="CP-102A-ND"/>
<attribute name="REVIEWER" value="Swanson"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="PUSH-BUTTON" prefix="S">
<gates>
<gate name="G$1" symbol="TS2" x="0" y="0"/>
</gates>
<devices>
<device name="-SQUARE" package="BUTTON-TACTILE-SQUARE-ADAFRUIT1010">
<connects>
<connect gate="G$1" pin="P" pad="P"/>
<connect gate="G$1" pin="P1" pad="P2"/>
<connect gate="G$1" pin="S" pad="S"/>
<connect gate="G$1" pin="S1" pad="S2"/>
</connects>
<technologies>
<technology name="">
<attribute name="CREATOR" value="Swanson"/>
<attribute name="DIST" value="Adafruit"/>
<attribute name="DISTPN" value="1010"/>
<attribute name="REVIEWER" value="Swanson"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="LED" prefix="D" uservalue="yes">
<description>/</description>
<gates>
<gate name="G$1" symbol="LED" x="0" y="0"/>
</gates>
<devices>
<device name="5MM" package="LED5MM">
<connects>
<connect gate="G$1" pin="A" pad="A"/>
<connect gate="G$1" pin="C" pad="K"/>
</connects>
<technologies>
<technology name="">
<attribute name="CREATOR" value="Swanson"/>
<attribute name="DIST" value="Adafruit"/>
<attribute name="DISTPN" value="297"/>
<attribute name="REVIEWER" value="Swanson"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="RESISTOR" prefix="R" uservalue="yes">
<gates>
<gate name="G$1" symbol="RESISTOR" x="0" y="0"/>
</gates>
<devices>
<device name="TH-1/4W-CARBON" package="RESAD1160W55L680D260_HS">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="CREATOR" value="Swanson"/>
<attribute name="DIST" value="Digikey"/>
<attribute name="DISTPN" value="100QTR-ND"/>
<attribute name="REVIEWER" value="Swanson"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="FRAME1" library="Lab01" deviceset="FRAME_B_L" device=""/>
<part name="J1" library="Lab01" deviceset="2.1MMJACK" device="THM"/>
<part name="S1" library="Lab01" deviceset="PUSH-BUTTON" device="-SQUARE"/>
<part name="D1" library="Lab01" deviceset="LED" device="5MM"/>
<part name="R1" library="Lab01" deviceset="RESISTOR" device="TH-1/4W-CARBON"/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="FRAME1" gate="G$1" x="0" y="0" smashed="yes"/>
<instance part="FRAME1" gate="G$2" x="325.12" y="0" smashed="yes">
<attribute name="LAST_DATE_TIME" x="337.82" y="1.27" size="2.54" layer="94"/>
<attribute name="DRAWING_NAME" x="342.9" y="19.05" size="2.54" layer="94"/>
<attribute name="SHEET" x="411.48" y="1.27" size="2.54" layer="94"/>
</instance>
<instance part="J1" gate="G$1" x="187.96" y="132.08" smashed="yes">
<attribute name="NAME" x="185.42" y="137.16" size="1.27" layer="95"/>
</instance>
<instance part="S1" gate="G$1" x="233.68" y="124.46" smashed="yes" rot="R270">
<attribute name="NAME" x="231.14" y="130.81" size="1.778" layer="95"/>
</instance>
<instance part="D1" gate="G$1" x="203.2" y="134.62" smashed="yes" rot="R90">
<attribute name="NAME" x="207.772" y="138.176" size="1.778" layer="95" rot="R180"/>
<attribute name="VALUE" x="207.772" y="140.335" size="1.778" layer="96" rot="R180"/>
</instance>
<instance part="R1" gate="G$1" x="223.52" y="134.62" smashed="yes">
<attribute name="VALUE" x="219.71" y="131.318" size="1.778" layer="96"/>
<attribute name="NAME" x="219.71" y="136.1186" size="1.778" layer="95"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="5V" class="0">
<segment>
<pinref part="J1" gate="G$1" pin="TIP"/>
<pinref part="D1" gate="G$1" pin="A"/>
<wire x1="193.04" y1="134.62" x2="200.66" y2="134.62" width="0.1524" layer="91"/>
<label x="193.04" y="134.62" size="1.778" layer="95"/>
</segment>
</net>
<net name="N$1" class="0">
<segment>
<pinref part="D1" gate="G$1" pin="C"/>
<pinref part="R1" gate="G$1" pin="1"/>
<wire x1="208.28" y1="134.62" x2="218.44" y2="134.62" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="R1" gate="G$1" pin="2"/>
<pinref part="S1" gate="G$1" pin="P"/>
<wire x1="228.6" y1="134.62" x2="228.6" y2="124.46" width="0.1524" layer="91"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="S1" gate="G$1" pin="S"/>
<pinref part="S1" gate="G$1" pin="S1"/>
<wire x1="238.76" y1="124.46" x2="238.76" y2="121.92" width="0.1524" layer="91"/>
<wire x1="238.76" y1="121.92" x2="238.76" y2="116.84" width="0.1524" layer="91"/>
<wire x1="238.76" y1="116.84" x2="193.04" y2="116.84" width="0.1524" layer="91"/>
<junction x="238.76" y="121.92"/>
<pinref part="J1" gate="G$1" pin="RING_SW"/>
<pinref part="J1" gate="G$1" pin="RING"/>
<wire x1="193.04" y1="132.08" x2="193.04" y2="129.54" width="0.1524" layer="91"/>
<wire x1="193.04" y1="116.84" x2="193.04" y2="129.54" width="0.1524" layer="91"/>
<junction x="193.04" y="129.54"/>
<label x="193.04" y="121.92" size="1.778" layer="95"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
