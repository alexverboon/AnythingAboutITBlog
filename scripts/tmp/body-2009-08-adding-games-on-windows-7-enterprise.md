When you run a default Windows 7 Enterprise installation, you will notice that by default no games are being installed. System administrators using the Windows Automated Installation Toolkit can use the image manager to enable games within their customized Windows 7 Enterprise installation, but here’s another trick how you can get the games enabled. 

  Open a command prompt with elevated Administrative privileges and execute the following command:

  dism /online /enable-feature /featurename:InboxGames

  when completed, you should see all the default games appear within the Start Menu. To disable the games, simply run the following command:

  dism /online /disable-feature /featurename:InboxGames

  This was just an example with games. Run DISM /Online /get-features | more to find other features you can enable or disable.