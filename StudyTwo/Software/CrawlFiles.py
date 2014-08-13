#akthom - 12 april 2014


def crawlLinks(): 
        import re #import regex module
        import urllib #request #import url request module
        from bs4 import BeautifulSoup
        import os
        import csv
#        import urllib.error

        outfile = open("GCMDDatasets.csv","a") 

#        w=csv.writer(outfile, dialect='excel-tab')
        
#
        tags=["Entry_Title","Entry_ID", "default/dif/summary_text.jsp", "Related URL", "Parent_DIF", "Aggregation", "Spatial Coverage", "Temporal Coverage", "Paleo Temporal Coverage","Location Keywords","Data Resolution","Parameters","Sources","Sensors","Project\/Campaign","Quality","Keywords"]

        for i in tags:
                outfile.write(i)
        outfile.write('\n')
        for dirname, dirnames, filenames in os.walk('./processedfiles'):
                for filename in filenames:
                        if filename.endswith('.html'):
                                infile=os.path.join(dirname,filename)
                                
                                datalist=[filename," | "]
                                soup = BeautifulSoup(open(infile, "r"))

                                for tag in tags:
                                        var=soup.findAll("metadata",attrs={"tag": tag})
                                        soupvar=BeautifulSoup(str(var)).getText().encode("utf","ignore")
                                
                                        datalist.append(soupvar + " | ")


                                for i in datalist:
                                        outfile.write(str(i))
                                outfile.write("\n")

#                                thingToWrite=str(datalist)+'\n' #writes list + a new line to file
#                                w.writerow(thingToWrite)
 
                        

        print("done")
#        errorfile.close()
        outfile.close()
#        return iarDict



tester= """

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta http-equiv="x-ua-compatible" content="IE=8"></metadata><metadata tag="fixes IE">
 
 
 
<title>Global Change Master Directory (GCMD)</title>
<script type="text/javascript" src="default/javascript.js"></script>
<script type="text/javascript" src="GCMD/custom.js"></script>
</metadata><metadata tag="OpenSearch instructions">
<link rel="search"
 type="application/opensearchdescription+xml"
 title="Global Change Master Directory"
 href="/KeywordSearch/default/openSearch.jsp?Portal=GCMD" />
<link rel="stylesheet" type="text/css" href="default/base.css">
<link rel="stylesheet" type="text/css" href="default/base_print.css" media="print">
<link rel="stylesheet" type="text/css" href="default/styles.css">
 
</metadata><metadata tag="other styles">
<link rel="stylesheet" type="text/css" href="GCMD/common.css">
<link rel="stylesheet" type="text/css" href="GCMD/style/preview.css">
<link rel="stylesheet" type="text/css" href="default/style/feedback.css">
 
 
</metadata><metadata tag="[if lte IE 7]>
<link rel="stylesheet" type="text/css" href="GCMD/ie_specific.css">
 
<![endif]">
 
<script type="text/javascript" src="WidgetWrappers/WidgetWrappers.nocache.js"></script>
 
<link rel="icon" type="image/vnd.microsoft.icon" href="favicon.ico">
 
 
<link type="text/html" rel="bookmark" href='/r/d/[GCMD]NCAR_DS292.0'>
<link type="text/html" rel="alternate" href='/getdif.htm?[GCMD]NCAR_DS292.0'>
<link type="text/html" rel="alternate" href='/records/GCMD_NCAR_DS292.0.html'>
 
 
</metadata><metadata tag="BEGIN - maptime advanced search related javascript">
<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
<script type="text/javascript" src="gcmd_google_map_v3.js"></script>
<script type="text/javascript" src="temporal.js"></script>
</metadata><metadata tag="END maptime advanced search related javascript">
 
</head>
<body class="search" onLoad="browserDetect();doOnLoad();">
<div id="siteContainer">
<div class="hidden">
<a href="#maincontent" title="Skip to Main Content" accesskey="3">
 Skip to Main Content Navigation (press 3)
</a>
</div>
 
</metadata><metadata tag="
<div class="hidden"><a href="#leftnav" title="Skip to Left Navigation" accesskey="2">Skip to Left Navigation (press 2)</a></div>
<div class="hidden"><a href="#maincontent" title="Skip to Main Content" accesskey="3">Skip to Main Content Navigation (press 3)</a></div>
">
	<div id="sitelinks">
		<ul>
			<li><a href="/learn/faqs/faqpage.html" title="Frequently Asked Questions about Earth Science and About the GCMD">FAQ</a></li>
			<li><a href="/sitemap.html" title="Looking for a specific page or information?: Use the sitemap to find it quickly.">Site Map</a></li>
			<li><a href="/MailComments/MailComments.jsf?rcpt=gcmduso" target="_blank" title="Have suggestions, comments, and questions about GCMD contact us here.">Contact Us</a></li>
		</ul>
	</div>	
<div id="gcmdhead">
<div id="metaltop"><span></span></div>
<div id="banner">
<div id="bannerImg">
<a href="/index.html">
<img width="1000" height="123" alt="" title="GCMD Banner Image" src="default/images/spacer.gif" border="0" /></a>
</div>
</div>
</div>
<div id="topNav">
<div id="topNavCenter">
<div id="topNavBtns">
<a href="/index.html" class="homeBtn" title="GCMD Home page: Welcome to the GCMD."><span class="context">Home</span></a>
<a href="Keywords.do?Portal=GCMD&KeywordPath=Parameters|Home&MetadataType=0#maincontent" class="searchBtn" title="Locate Earth science data, data services, and more through descriptive records."><span class="context">Search GCMD</span></a>
<a href="/learn/index.html" class="learnBtn" title="Learn about GCMD"><span class="context">Learn about GCMD</span></a>
<a href="/add/portals.html" class="portalsBtn" title="Learn about GCMD's Portal Collaborations."><span class="context">Portals</span></a>
<a href="/collaborate/docbuilder.html" class="collaborateBtn" title="Collaborate with GCMD"><span class="context">Collaborate</span></a>
</div>
</div>
</div>
 
<div id="page" class="alignCenter">
<div id="content">
<a name="maincontent"></a>
<div id="mainTabs" class="left">
 
<div class='tab' onclick="window.location='Keywords.do?Portal=GCMD&KeywordPath=Parameters|Home&MetadataType=0&Columns=0#maincontent';">
<span class="tabTitle"><a href="Keywords.do?Portal=GCMD&KeywordPath=Parameters|Home&MetadataType=0&Columns=0#maincontent">Data Sets</a></span>
</div>
<div class='tabOff' onclick="window.location='Keywords.do?Portal=GCMD&KeywordPath=ServiceParameters|Home&MetadataType=1&Columns=0#maincontent';">
<span class="tabTitle"><a href="Keywords.do?Portal=GCMD&KeywordPath=ServiceParameters|Home&MetadataType=1&Columns=0#maincontent">Services / Tools</a></span>
</div>
<div class='tabOff' onclick="window.location='Ancillary.do?Portal=GCMD&MetadataType=0&Columns=0#maincontent';">
<span class="tabTitle"><a href="Ancillary.do?Portal=GCMD&MetadataType=0&Columns=0#maincontent">Ancillary Descriptions</a></span>
</div>
</div>
<div id="mainContainer">
<div class="shadowBox_top blue clear"><span class="nested"></span></div>
<div class="shadowBox_contents blue">
</metadata><metadata tag="CONTENT AREA START">
 
 
<script language="JavaScript" src="default/newcollapse_expand_single_item.js"></script>
<script language="JavaScript" src="default/newcollapse_expand_single_item.js"></script>
<script language="JavaScript" src="default/newcollapse_expand_summary.js"></script>
<script type="text/javascript" src="default/supplemental_common.js"></script>
<script src="gmaps_util.js" type="text/javascript"></script>
<noscript>
<div class="jsalert">
<strong>Are you using a browser that doesn't support JavaScript or have you disabled JavaScript?</strong>



 If you have disabled JavaScript, you must re-enable JavaScript to use this page.

 Or you can view this record using the <span style="color:#090">
<a href="Metadata.do?Portal=GCMD&KeywordPath=&EntryId=NCAR_DS292.0&MetadataView=Text&MetadataType=0&lbnode=mdlb3" >Text Only Format</a></span>.
</div>
</noscript>
<gcmd:debug msg="start"/>
</div>
</metadata><metadata tag="This is the closing DIV tag for "shadowBox_contents blue" in layout.jsp">
<gcmd:debug msg="end"/>
<div class="shadowBox_contents alignLeft">
<span class="nested" style="padding-top:12px;">
<div class="breadCrumb"></div>
</metadata><metadata tag="Start record table">
<table width="598">
<tr>
<td>
 
 
</metadata><metadata tag="Entry_Title">
<tr><td width="589" colspan="2" class="mediumText">
<strong>
Warren's Global Climatological Cloud Data, 1930-1983Nov

</strong>
</metadata><metadata tag="Entry_ID">
<span class="field">Entry ID: </span>
<span class="textrecord">
NCAR_DS292.0
</span>
</p><p />
</td>
</tr>
</metadata><metadata tag="DIF tab bar">
 
</metadata><metadata tag="start to GCMD/dif/dif_tab_bar_full_record.jsp">
<table border="0" cellpadding="1" cellspacing="1">
<tr>
<td class="mediumText"> 
<strong>
</metadata><metadata tag="Test for Get Data Tab">
 
	
</metadata><metadata tag="Print Update Record Tab">
<strong>
 
<div style="text-align:center">
 
<span class="tab" id="updateTabTop">
<span class="textrecord">[</span>
<span class="textrecord">
<span class="textabs" onClick="dbDetails(this)">
 Update this Record
</span>
<span class="textrecord">]</span>
</span>
</span>
</div>
</strong>
</strong>
</td>
</tr>
<tr>
<td width="570" align="center" class="mediumText">
<script type="text/javascript">
 function dbDetails(obj)
 {
 var dbDetailsWindow =document.getElementById("dbDetailsWindow");
 var tab2 = document.getElementById("updateTabTop");
 
 if (dbDetailsWindow!=null)
 {
 if (dbDetailsWindow.state && dbDetailsWindow.statetrue)
 {
 dbDetailsWindow.style.display="none";
 dbDetailsWindow.state = false;
 tab2.style.backgroundColor = "";
 tab2.style.border="";
 }
 else
 {
 dbDetailsWindow.style.display="block";
 dbDetailsWindow.state = true;
 tab2.style.backgroundColor
 = dbDetailsWindow.style.backgroundColor;
 tab2.style.border="1px solid";
 tab2.style.borderBottom="0px";
 }
 }
 }
</script> 
 
<div id="dbDetailsWindow" class="textrecord" style="margin-right:2%;display:none;padding:0.5em 0;width:280px;border:1px solid black; background-color:rgb(236, 233, 216);">
 
<div>Updating this record requires registration.</div>
 
<div style="float:left;margin:0.5em;border-right:1px solid;width:125px;">
 (Account holders)
<div class="texttabs">
 
 
 
 
 
<a target="recorddrillsearch"
 href="/DocumentBuilder/Metadata.do?OrigMetadataNode=GCMD&amp;EntryId=NCAR_DS292.0&amp;Portal=GCMD&amp;RequestAction=Build&amp;MetadataType=0&amp;UseCacheDocument=true&amp;interface=FROMGETDIF">
 Update this Record.</a>
 
 
 
</div>
</div>
<div style="float:right;margin:0.5em;border-left:1px solid;width:125px;">
<div>
<a class="texttabs"
 href="/collaborate/docbuilder.html">Need an account?</a>
<div>&nbsp;</div>
</div>
</div>
<div style="clear:both"><a href="javascript:dbDetails()">close</a>
</div>
</td>
</tr>
</table>


</metadata><metadata tag="end to GCMD/dif/dif_tab_bar_full_record.jsp">
<p />
</metadata><metadata tag="Summary">
</metadata><metadata tag="default/dif/summary_text.jsp">
<div class="fieldSection">
<div class="field">Summary</div>
<div class="fieldSummary">
 
 
<table BORDER="0" WIDTH="100%"><TR><TD>
 
<span class="textrecord">
<strong>Abstract: </strong>
 Total cloud cover and cloud type amounts over both land and ocean, based on data
from FNOC and COADS.
An update is coming. See RELATED SITES below for a preliminary and
partial updated maps.
</span>

 
 
</TD></TR></table>
 
 
 
</div>
</div>
</metadata><metadata tag="Related URL">
<p>
<span class="field">Related URL</span>
<table border="0" width="80%">
<tr><td>
 
 
<span class="textrecord"><strong>Link: </strong>
<a href="RedirectAction.do?target=i%2Flo2J3CXYe4l3nD7aYMsNRM8fRu2pqjPZembXd7mFiJMfqRaPlQrg%3D%3D" target="_blank">
VIEW RELATED INFORMATION
</metadata><metadata tag="else">
<! -- CLICK HERE">
</a></span>
 
<p />


 
 
 
<span class="textrecord"><strong>Link: </strong>
<a href="RedirectAction.do?target=i%2Flo2J3CXYe4l3nD7aYMsNRM8fRu2pqjPZembXd7mFjbRX0w3FzPVQ%3D%3D" target="_blank">
VIEW RELATED INFORMATION
</metadata><metadata tag="else">
<! -- CLICK HERE">
</a></span>
 
<p />


 
 
 
<span class="textrecord"><strong>Link: </strong>
<a href="RedirectAction.do?target=S6cqF6vMwKzUL8qdufxCP0Cu%2FLmEkuHbnro7Qo44DoRpRwmLU39Srsw0l5mrk9Fc" target="_blank">
VIEW RELATED INFORMATION
</metadata><metadata tag="else">
<! -- CLICK HERE">
</a></span>
<span class="textrecord"><strong>Description: </strong>
Climate Atlas of Clouds Over Land and Ocean at the University of Washington 
</span>
 
</td></tr></table>
</p><p />


</metadata><metadata tag="Parent_DIF">
</metadata><metadata tag="Aggregation">
</metadata><metadata tag="Spatial Coverage">
</metadata><metadata tag="Citation">
 
<p>
<span class="field">Data Set Citation</span>
 
 
<table width="100%" cellspacing="0" cellpadding="0" border="0">
<tr> <td>
 
<span class="textrecord"><strong>Dataset Originator/Creator: </strong>
 UCAR/NCAR/CISL/DSS > Data Support Section,Scientific Computing Division, National Center for Atmospheric Research, University Corporation for Atmospheric Research
</span> 
 
 
 
<span class="textrecord"><strong>Dataset Title: </strong>
 Warren's Global Climatological Cloud Data, 1930-1983Nov
</span> 
 
 
 
 
 
<span class="textrecord"><strong>Dataset Publisher: </strong>
 UCAR/NCAR/CISL/DSS > Data Support Section,Scientific Computing Division, National Center for Atmospheric Research, University Corporation for Atmospheric Research
</span> 
 
 
 
 
 
 
 
 
<span class="textrecord"><strong>Online Resource: </strong>
<span class="textrecord">
<a href="RedirectAction.do?target=i%2Flo2J3CXYe4l3nD7aYMsNRM8fRu2pqjPZembXd7mFjbEeVMLFXPtQ%3D%3D" target="recorddrillsearch"> 
 http://rda.ucar.edu/datasets/ds292.0/</span></a>
 

 
</td></tr></table>
 
</p><p />


</metadata><metadata tag="Temporal Coverage">
<p>
<span class="field">Temporal Coverage </span>
<table BORDER="0" WIDTH="100%">
 
<tr> <td>
<span class="textrecord"><strong>Start Date: </strong>
 1930-01-01
</span></td></tr>
 
 
<tr><td><span class="textrecord"><strong>Stop Date: </strong>
 1983-11-30
</span></td></tr>
 
</table>
 
</p><p />


</metadata><metadata tag="Paleo Temporal Coverage">
</metadata><metadata tag="Location Keywords">
</metadata><metadata tag="Data Resolution">
</metadata><metadata tag="Parameters">
<p>
<span class="field">Science Keywords </span>
<table BORDER="0" WIDTH="570"> <TR><TD class="textrecord">
<a href="Keywords.do?KeywordPath=%5BParameters%3A+Topic%3D%27ATMOSPHERE%27%2C+Term%3D%27CLOUDS%27%2C+Variable_Level_1%3D%27CLOUD+PROPERTIES%27%2C+Variable_Level_2%3D%27CLOUD+FREQUENCY%27%5D&Portal=GCMD&MetadataType=0" target="recorddrillsearch" >
 
 ATMOSPHERE
 
 
 >CLOUDS
 
 
 >CLOUD PROPERTIES
 
 
 >CLOUD FREQUENCY
 
 
 
</a>
 
 &nbsp;&nbsp;<a href="Definitions.do?Portal=GCMD&KeywordPath=&NumericId=63273&MetadataType=0&lbnode=mdlb3" onClick="exit(this.href,760,500); return false" ><span class="textrecord"> [Definition]</span>
</a>
 
</TD></TR></table>
<table BORDER="0" WIDTH="570"> <TR><TD class="textrecord">
<a href="Keywords.do?KeywordPath=%5BParameters%3A+Topic%3D%27ATMOSPHERE%27%2C+Term%3D%27CLOUDS%27%2C+Variable_Level_1%3D%27CLOUD+TYPES%27%5D&Portal=GCMD&MetadataType=0" target="recorddrillsearch" >
 
 ATMOSPHERE
 
 
 >CLOUDS
 
 
 >CLOUD TYPES
 
 
 
 
</a>
 
 &nbsp;&nbsp;<a href="Definitions.do?Portal=GCMD&KeywordPath=&NumericId=63293&MetadataType=0&lbnode=mdlb3" onClick="exit(this.href,760,500); return false" ><span class="textrecord"> [Definition]</span>
</a>
 
</TD></TR></table>
</p><p />


</metadata><metadata tag="ISO_Topic_Category">
<p>
<span class="field">ISO Topic Category </span>
<table BORDER="0" WIDTH="100%"> <TR><TD>
<span class="textrecord">
<a href="Keywords.do?KeywordPath=%5BISO_Topic_Category%3D%27CLIMATOLOGY%2FMETEOROLOGY%2FATMOSPHERE%27%5D&Portal=GCMD&MetadataType=0" target="recorddrillsearch" >
 CLIMATOLOGY/METEOROLOGY/ATMOSPHERE
</a>
</span>

</TD></TR></table>
</p><p />


</metadata><metadata tag="Sources">
</metadata><metadata tag="Sensors">
</metadata><metadata tag="Project/Campaign">
<p>
<span class="field">Project</span>
<table BORDER="0" WIDTH="100%">
<TR><TD>
<a href="Keywords.do?KeywordPath=%5BProject%3A+Short_Name%3D%27ESIP%27%5D&Portal=GCMD&MetadataType=0" target="recorddrillsearch" ><span class="textrecord">
 ESIP
 
 >Earth Science Information Partners Program
</span>
</a>
 
 &nbsp;&nbsp;<a href="Supplementals.do?Portal=GCMD&KeywordPath=Projects&NumericId=6355&MetadataType=0&lbnode=mdlb3" onClick="exit(this.href,760,500); return false" ><span class="textrecord"> [Information]</span>
</a>
 
</TD></TR></table>
</p><p />


</metadata><metadata tag="Quality">
</metadata><metadata tag="Access Constraints">
</metadata><metadata tag="Use Constraints">
</metadata><metadata tag="Keywords">
<p>
<span class="field">Keywords</span>
<table BORDER="0" WIDTH="100%"> <TR><TD>
<a href="Keywords.do?KeywordPath=%5BKeyword%3D%27GRIDDING+METHODS%27%5D&Portal=GCMD&MetadataType=0" target="recorddrillsearch" ><span class="textrecord">GRIDDING METHODS</span></a>
</TD></TR></table>
</p><p />


</metadata><metadata tag="Dataset Progress">
<p>
<span class="field">Data Set Progress</span>
<table BORDER="0" WIDTH="100%">
<TR><TD><span class="textrecord">
COMPLETE
</span>
</TD></TR></table>
</p><p />


</metadata><metadata tag="Originating Center">
</metadata><metadata tag="Data Center">
 
<p><span class="field">Data Center</span>
 
 
<table border="0" width="100%" cellpadding="0" cellspacing="0">
<tr> <td>
<span class="textrecord">
<a href="Keywords.do?KeywordPath=%5BData_Center%3A+Short_Name%3D%27UCAR%2FNCAR%2FCISL%2FRDA%27%5D&Portal=GCMD&MetadataType=0" target="recorddrillsearch" >
</metadata><metadata tag="UCAR/NCAR/CISL/RDA">
 
 Research Data Archive, Computational and Information Systems Laboratory, National Center for Atmospheric Research, University Corporation for Atmospheric Research
</span>
</a>
 
 &nbsp;&nbsp; <a href="Supplementals.do?Portal=GCMD&KeywordPath=DataCenters&NumericId=367&MetadataType=0&lbnode=mdlb3" onClick="exit(this.href,760,500); return false" ><span class="textrecord"> [Information]</span></a>

 
 
<span class="textrecord">Data Center URL: </span>
<span class="textrecord"><a href="RedirectAction.do?target=i%2Flo2J3CXYe4l3nD7aYMsMS82LVPGETz" target="_blank">http://rda.ucar.edu/</a></sp
an>
 
 
 
 
<span class="textrecord"><strong>Dataset ID: </strong></span>
<span class="textrecord">292.0</span> 
 
 
</metadata><metadata tag="Personnel Table">
 
 
 
<table width="90%" align="center" cellpadding="0" cellspacing="0" border="0">
<tr> <td height="2" colspan="2" valign="top" class="field">Data Center Personnel</td>
</tr>
<tr> <td>
<span class="textrecord"><strong>Name: </strong>
<a href="Keywords.do?KeywordPath=%5BPersonnel%3A+Last_Name%3D%27RDA+HELP+DESK%27%5D&Portal=GCMD&MetadataType=0" target="recorddrillsearch" >
 
 
 RDA HELP DESK</span>
</a>
 <span class="textrecord"><strong>Phone: </strong>
 (303)-497-1231
</span>
<span class="textrecord"><strong>Fax: </strong>
 (303)-497-1291
</span>
<span class="textrecord"><strong>Email: </strong>
 dssweb at ucar.edu
</span>
 
<span class="textrecord"><strong>Contact Address: </strong>
 
<span class="textrecord">
 National Center for Atmospheric Research
 
 CISL/DSS
 
 P.O. Box 3000
 
</span>
 
<span class="textrecord"><strong>City: </strong>
 Boulder
</span>
 
<span class="textrecord"><strong>Province or State: </strong>
 CO
</span>
<span class="textrecord"><strong>Postal Code: </strong>
 80307
</span>
<span class="textrecord"><strong>Country: </strong>
 U.S.A.
</span>
</td> </tr></table> </metadata><metadata tag="End personnel table">
</table> </metadata><metadata tag="end data center table">
<p /><p />
</metadata><metadata tag="Distribution">
</metadata><metadata tag="Personnel">
<p>
<span class="field">Personnel</span>
<table BORDER="0" WIDTH="100%">
<tr><td><span class="textrecord">
<a href="Keywords.do?KeywordPath=%5BPersonnel%3A+Last_Name%3D%27DATTORE%27%2C+First_Name%3D%27BOB%27%5D&Portal=GCMD&MetadataType=0" target="recorddrillsearch" >
 BOB
 
 DATTORE 
</a></span>
<span class="textrecord"><strong>Role: </strong>
DIF AUTHOR
</span> 
<span class="textrecord"><strong>Phone: </strong>
(303)-497-1825
</span>
<span class="textrecord"><strong>Fax: </strong>
(303)-497-1291
</span>
<span class="textrecord"><strong>Email: </strong>
dattore at ucar.edu
</span>
<span class="textrecord"><strong>Contact Address: </strong>
National Center for Atmospheric Research 
CISL/DSS 
P.O. Box 3000 
</span>
<span class="textrecord"><strong>City: </strong>
Boulder
</span>
<span class="textrecord"><strong>Province or State: </strong>
CO
</span>
<span class="textrecord"><strong>Postal Code: </strong>
80307
</span>
<span class="textrecord"><strong>Country: </strong>
U.S.A.
</span>
</td></tr></table>
<p/>


<table BORDER="0" WIDTH="100%">
<tr><td><span class="textrecord">
<a href="Keywords.do?KeywordPath=%5BPersonnel%3A+Last_Name%3D%27SHIH%27%2C+First_Name%3D%27CHI-FAN%27%5D&Portal=GCMD&MetadataType=0" target="recorddrillsearch" >
 CHI-FAN
 
 SHIH 
</a></span>
<span class="textrecord"><strong>Role: </strong>
TECHNICAL CONTACT
</span> 
<span class="textrecord"><strong>Phone: </strong>
(303)-497-1833
</span>
<span class="textrecord"><strong>Fax: </strong>
(303)-497-1291
</span>
<span class="textrecord"><strong>Email: </strong>
chifan at ucar.edu
</span>
<span class="textrecord"><strong>Contact Address: </strong>
National Center for Atmospheric Research 
CISL/DSS 
P.O. Box 3000 
</span>
<span class="textrecord"><strong>City: </strong>
Boulder
</span>
<span class="textrecord"><strong>Province or State: </strong>
CO
</span>
<span class="textrecord"><strong>Postal Code: </strong>
80307
</span>
<span class="textrecord"><strong>Country: </strong>
U.S.A.
</span>
</td></tr></table>
</p><p />


</metadata><metadata tag="Reference/Publications">
</metadata><metadata tag="default/dif/reference_text.jsp">
<div class="fieldSection">
<div class="field">Publications/References</div>
<div class="textrecord">
 Warren, S.G., C.J. Hahn, J. London, R.M. Chervin and R. Jenne, 1988: Global 
 distribution of total cloud cover and cloud type amounts over the 
 ocean. TN-317+STR, National Center for Atmospheric Research, 212 
 pp.. 

Warren, S.G., C.J. Hahn, J. London, R.M. Chervin and R. Jenne, 1986: Global 
 distribution of total cloud cover and cloud type amounts over land. 
 TN-273+STR, National Center for Atmospheric Research, 229 pp.. 

Hahn, C.J., S.G. Warren, J. London, R.M. Chervin and R. Jenne, 1984: Atlas of simultaneous occurrence of different cloud types over land. 
 TN-241+STR, National Center for Atmospheric Research, 209 pp.. 

Hahn, C.J., S.G. Warren, J. London, R.M. Chervin and R. Jenne, 1982: Atlas of simultaneous occurrence of different cloud types over the ocean. 
 TN-201+STR, National Center for Atmospheric Research, 212 pp.. 

</div>
</div>


</metadata><metadata tag="Metadata Name 
<p>
<span class="field">Metadata Name and Version </span>
<table border="0" width="100%">
<tr><td>
<span class="textrecord"><strong>Metadata Name: </strong>
CEOS IDN DIF
</span>
<! -- Metadata Version 
<span class="textrecord"><strong>Metadata Version: </strong>
VERSION 9.7
</span>
</td></tr></table>
</p><p />


">
</metadata><metadata tag="Creation/Review Dates">
<div class="fieldSection">
<div class="field">Creation and Review Dates</div>
<div>
 
<div class="textrecord">
<strong>DIF Creation Date:</strong>
 2008-02-14
</div>
 
 
<div class="textrecord">
<strong>Last DIF Revision Date:</strong>
 2013-05-23
</div>
 
 
</div>
 
</div>

 
 
</metadata><metadata tag="DIF tab bar">
 
</metadata><metadata tag="start to GCMD/dif/dif_tab_bar_full_record.jsp">
<table border="0" cellpadding="1" cellspacing="1">
<tr>
<td class="mediumText" align="center"> 
<strong>
<span class="tab" id="updateTabBottom">
<span class="textrecord">[</span>
<span class="textrecord">
<span class="textabs" onClick="dbDetails2(this)">
 Update this Record</span>
</span>
<span class="textrecord">]</span>
</span>
</strong>
</td>
</tr>
<tr>
<td width="570" align="center" class="mediumText">
<script type="text/javascript">
 function dbDetails2(obj)
 {
 var dbDetails2Window =document.getElementById("dbDetails2Window");
 var tab2 = document.getElementById("updateTabBottom");
 
 if (dbDetails2Window!=null)
 {
 if (dbDetails2Window.state && dbDetails2Window.statetrue)
 {
 dbDetails2Window.style.display="none";
 dbDetails2Window.state = false;
 tab2.style.backgroundColor = "";
 tab2.style.border="";
 }
 else
 {
 dbDetails2Window.style.display="block";
 dbDetails2Window.state = true;
 tab2.style.backgroundColor
 = dbDetails2Window.style.backgroundColor;
 tab2.style.border="1px solid";
 tab2.style.borderBottom="0";
 }
 }
 }
</script> 
<div id="dbDetails2Window" class="textrecord"
 style="display:none;left:50%;padding:0.5em 0;width:280px;border:1px solid black;background-color:rgb(236, 233, 216);">
<div>Updating this record requires registration.</div>
 
<div style="float:left;margin:0.5em;border-right:1px solid;width:125px;">
 (Account holders)
<div class="texttabs">
 
 
 
 
<a target="_blank"
 href="/DocumentBuilder/Metadata.do?OrigMetadataNode=GCMD&amp;EntryId=NCAR_DS292.0&amp;RequestAction=Build&Portal=GCMD&amp;MetadataType=0&amp;UseCacheDocument=true&amp;interface=FROMGETDIF">
 Update this Record.</a>
 
 
 
</div>
</div>
<div style="float:right;margin:0.5em;border-left:1px solid;width:125px;">
<div>
<a class="texttabs"
 href="/collaborate/docbuilder.html">Need an account?</a>
<div>&nbsp;</div>
</div>
</div>
<div style="clear:both"><a href="javascript:dbDetails2()">close</a>
</div>
</td>
</tr>
</table>


</metadata><metadata tag="end to GCMD/dif/dif_tab_bar_full_record.jsp">
 
</metadata><metadata tag="End Main Content Area">
 
</td>
</tr>
</table>
</div>
 
</metadata><metadata tag="END Content Area">
<div class="shadowBox_bottom clear"><span class="nested"></span></div>
</div>
<hr />
</div>
</div>
 
<div id="metalbottom"><span></span></div>
 
<script type="text/javascript">
 function openAnchor(tag, config)
 {
 var href = null;
 try
 {
 var rawAttrib = tag.getAttribute("href");
 if (rawAttrib!=null && 0<rawAttrib.length)
 {
 href = rawAttrib;
 }
 else
 {
 var list = tag.getElementsByTagName("a");
 for (var y=0; y<list.length; ++y)
 {
 var item = list[y].href
 if (item!=null && 0<item.length)
 {
 href = item;
 break;
 }
 }
 }
 if (href!=null && 0<href.length)
 {
 //append suffix if configured
 if (config.s!=null && 0<config.s.length){href += config.s;}
 viewPage(
 href
 , Math.min(window.screen.width,config.w)
 , config.h);
 }
 }
 catch (e){return true;}
 return false;
 }
</script>
<div id="totalfooter">
<div align="center">
<ul id="nav">
<li><a href="/KeywordSearch/Keywords.do?Portal=GCMD&KeywordPath=Parameters|Home&MetadataType=0&Columns=0&KeywordPath=Parameters|Home" title="Locate Earth science data, data services, and more through descriptive records.">Search</a></li>
<li><a href="/collaborate/docbuilder.html" title="Collaborate with GCMD">Collaborate</a></li>
<li><a href="/add/portals.html" title="Learn About GCMD's Portal Collaborations">Portals</a></li>
<li><a href="/MailComments/MailComments.jsf?rcpt=gcmduso" target="_blank" title="Have suggestions, comments, and questions about GCMD contact us here.">Contact Us</a></li>
</ul>
</div>
</div>
<div id="nasafoot">
<div id="nasafootleft">
<ul>
<li>
<a href="/KeywordSearch/Home.do?Portal=GCMD_legacy&MetadataType=0"><img src="/images/gui/togcmd.png" alt="Return to legacy GCMD" site"></a>
 
 + <a href="http://www.nasa.gov/about/highlights/HP_Privacy.html" target="_blank">
 NASA Privacy Policy and Important Notices </a></li>
</ul>
</div>
 
<div id="nasafootright">
<div class="logo">
<a class="external" href="http://www.nasa.gov/" target="_blank">
<img src="GCMD/images/gui/nasa_footer_logo.png" width="55" height="50" alt="NASA Logo - nasa.gov" /></a>
</div>
<ul>
<li onclick="return openAnchor(this, {w:1000,h:550,s:'#maincontent'})">
 Webmaster:
<a class="email" href="/MailComments/MailComments.jsf?rcpt=holland" target="_blank">Monica Holland</a>
</li>
<li onclick="return openAnchor(this, {w:1000,h:550,s:'#maincontent'})">
 Responsible NASA Official:
<a class="email" href="/MailComments/MailComments.jsf?rcpt=olsen" target="_blank">Lola Olsen</a>
</li>
<li>Last updated: April 2014</li>
</ul>
</div>
</div>
</metadata><metadata tag="nettracker.jsp">
</metadata><metadata tag="BEGIN: NetTracker Page Tag">
<script type="text/javascript" language="JavaScript" src="/ntpagetag.js"></script>
<noscript>
<img src="http://ws1.ems.eosdis.nasa.gov/images/ntpagetag.gif?js=0" height="1" width="1" border="0" hspace="0" vspace="0" alt="">
</noscript>
</metadata><metadata tag="END: NetTracker Page Tag">
</div>
</metadata><metadata tag="nettracker.jsp">
</metadata><metadata tag="BEGIN: NetTracker Page Tag">
<script type="text/javascript" language="JavaScript" src="/ntpagetag.js"></script>
<noscript>
<img src="http://ws1.ems.eosdis.nasa.gov/images/ntpagetag.gif?js=0" height="1" width="1" border="0" hspace="0" vspace="0" alt="">
</noscript>
</metadata><metadata tag="END: NetTracker Page Tag">
<script type="text/javascript">
if (window.globalsnull){window.globals = new Object();}
if (globals.feedbacknull)
{
 globals.feedback =
 {
 doHover: function()
 {
 var wrapper = document.getElementById("feedback");
 wrapper.style.marginLeft = "0";
 }
 ,doOut: function()
 {
 var wrapper = document.getElementById("feedback");
 wrapper.style.marginLeft = "-4px";
 }
 ,doClick: function()
 {
 gcmd.gwt.widgetwrappers.pageViewerApp.viewPage(
 "Feedback"
 , "/r/l/report"
 , 1160, 610);
 return false;
 }
 };
}
</script>
<div class="screenControl" id="feedback"
 onmouseover="globals.feedback.doHover()"
 onmouseout="globals.feedback.doOut()">
<a href="/r/l/report" onclick="return globals.feedback.doClick();">
<img src="default/images/feedback.png?portal=GCMD" alt="Link to Web Site" border="0"/></a>
</metadata><metadata tag="/a">
</div>
<iframe width="1" height="1" style="display:none;" name="cache" id="cache"
 src='./GCMD/manifest.jsp'></iframe>
</body>
</html>

"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(tester)
