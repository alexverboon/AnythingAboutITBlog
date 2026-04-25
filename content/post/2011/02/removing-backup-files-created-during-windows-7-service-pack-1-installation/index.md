---
title: "Removing Backup Files Created during Windows 7 Service Pack 1 Installation"
layout: "post"
date: 2011-02-19T18:24:06Z
slug: "removing-backup-files-created-during-windows-7-service-pack-1-installation"
aliases:
  - "/2011/02/removing-backup-files-created-during-windows-7-service-pack-1-installation/"
description: "For the Windows Vista Service Packs there was [vsp1cln.exe](https://www.verboon.info/index.php/2008/11/vista-sp1-cleanup-tool-vsp1clnexe/) (SP1) and [..."
author: "Alex Verboon"
image: "img/post-heroes/removing-backup-files-created-during-windows-7-service-pack-1-installation.png"
tags:
  - backup
  - cleanup
  - dism
  - service-pack-1
  - windows-7
categories:
  - dism-2
  - service-pack
  - windows7
---
For the Windows Vista Service Packs there was [vsp1cln.exe](https://www.verboon.info/index.php/2008/11/vista-sp1-cleanup-tool-vsp1clnexe/) (SP1) and [compcln.exe](https://www.verboon.info/index.php/2009/05/windows-vista-service-pack-2-cleanup/) (SP2) to cleanup the backup files created during the Service Pack installation. For Windows 7 Microsoft did not provide a separate cleanup tool, but instead leverages the windows-build-in DISM tool.

To remove the backup files created during the Windows 7 Service Pack 1 installation run the following command from an elevated command prompt.

dism.exe /online /cleanup-image /spsuperseded

[
![2011-02-19 18h37_59](images/2011-02-19-18h37_59_thumb.png)
](https://www.verboon.info/wp-content/uploads/2011/02/2011-02-19-18h37_59.png)

After successful completion you should get some disk space back.

