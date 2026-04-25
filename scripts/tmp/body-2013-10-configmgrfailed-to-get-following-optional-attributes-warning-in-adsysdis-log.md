Should you ever get a warning message in your adsysdis.log that starts with 

  WARN:  Failed to get following optional attributes

  then you have probably added an additional active directory object attribute to your Active Directory System Discovery but the value of that attribute of the discovered object is empty. 

  Let’s look at this in more detail. Within the configuration manager console under Administration \ Hierarchy Configuration \ Discovery Methods \ Active Directory System Discovery the Active Directory computer object property “**company**” was added. 

  [
![image](images/image_thumb3.png)
](https://www.verboon.info/wp-content/uploads/2013/10/image3.png)

  After ConfigMgr has extended the database, the next time the Active Directory discovery ran, the additional information got stored into the ConfigMgr database and became visible within the Computer object properties. 

  [
![image](images/image_thumb4.png)
](https://www.verboon.info/wp-content/uploads/2013/10/image4.png)

  However the following messages started to appear within the adsysdis.log 

  WARN:  Failed to get following optional attributes, company,    SMS_AD_SYSTEM_DISCOVERY_AGENT    10/9/2013 5:38:04 PM    5932 (0x172C)

  [
![image](images/image_thumb5.png)
](https://www.verboon.info/wp-content/uploads/2013/10/image5.png)

  Next I created two collections. The first collection contains all devices where the company attribute has no value, the second collection those that do contain the company name “Foo Corp”. 

  select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,   
SMS_R_SYSTEM.SMSUniqueIdentifier,    
SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client     
from SMS_R_System where SMS_R_System.company IS NULL

  select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,   
SMS_R_SYSTEM.SMSUniqueIdentifier,    
SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client     
from SMS_R_System where SMS_R_System.company = "Foo Corp"

  This allowed me to quickly identify which systems did not have information stored within the company attribute, and as it turned out, these systems were also referenced in the warning messages. 

  So once the Company value was set on the active directory object of all affected systems no further warnings did appear. 

  [
![image](images/image_thumb6.png)
](https://www.verboon.info/wp-content/uploads/2013/10/image6.png)

  Conclusion, before adding an additional active directory attribute, make sure that you only add those that do actually have information stored in it.