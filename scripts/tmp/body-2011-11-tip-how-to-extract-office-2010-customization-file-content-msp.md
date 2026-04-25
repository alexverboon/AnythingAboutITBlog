If you have an Office 2010 installation that is customized by use of the Office customization tool the customizations are stored within an MSP file that uses Extensible Markup Language (XML) format. 

  To extract the content you can use a vbscript that Microsoft has published on TechNet - [View Office Customization Tool output in Office 2010](http://technet.microsoft.com/en-us/library/cc179027.aspx)

  Simply copy paste the code provided within the article into a file called ExtractOctXml.vbs and then run the following command to extract the content:

  ExtractOctXml.vbs <MSP filename>