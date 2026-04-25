Back in 2011 I wrote a blog post on [how to mute Windows System Volume](https://www.verboon.info/index.php/2011/01/mute-windows-system-volume/) programmatically.  This week I found another approach on GitHub using PowerShell. 

 The PowerShell Module [WindowsAudioDevice-Powershell-Cmdlet](https://github.com/cdhunt/WindowsAudioDevice-Powershell-Cmdlet)** **provides a number of cmdlets to control the Windows System volume. 

  
- Get-DefaultAudioDevice  
- Get-AudioDeviceList  
- Set-DefaultAudioDevice [-Index] <Int>  
- Set-DefaultAudioDevice [-Name] <String>  
- Set-DefaultAudioDevice [-InputObject] <AudioDevice>  
- Set-DefaultAudioDeviceVolume -Volume <float>  
- Get-DefaultAudioDeviceVolume  
- Set-DefaultAudioDeviceMute  
- Write-DefaultAudioDeviceValue [-StreamValue

 I wrote the below PowerShell script to solve a request to set the system volume to mute. 

 SetPCVolumeMute.ps1

 ****

```

 <#   
    .SYNOPSIS   
        Sets the PC Volume to "MUTE"
         
    .DESCRIPTION   
        Sets the PC Volume to mute and volume to 0
        This script uses the AudioDevice Cmdlet from https://github.com/cdhunt/WindowsAudioDevice-Powershell-Cmdlet
        
    .PARAMETER (none)
      
         
    .NOTES   
        Author: Alex Verboon
        Version: 1.0       
            - initial version
     
    .EXAMPLE 
    SetPCVolumeMute.ps1     
  
    #>         

# Get the current script Name
$ScriptName = $MyInvocation.MyCommand.Name

# Get Current Script Path
$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition

# Import module (module DLL is stored in same path as the script)
$AudioModuleName = $scriptPath + "\AudioDeviceCmdlets.dll"
Import-Module -Name $AudioModuleName
Set-DefaultAudioDeviceMute
# if the volume was already muted, the above command unmutes it, so we also 
# set the volume to 0
Set-DefaultAudioDeviceVolume 0

```

If you do not want to permanently install the module on the device, just place the following files into the same directory as the SetPCVolumeMute.ps1 

"\PCVolumeMute\AudioDeviceCmdlets.dll"
"\PCVolumeMute\AudioDeviceCmdlets.dll-Help.xml"
"\PCVolumeMute\CoreAudioApi.dll"
"\PCVolumeMute\SetPCVolumeMute.ps1"

I have tested the script on Windows 8 64 bit and Windows 7 64 Bit and on 3 different hardware models. 

That’s it