---
title: How to check the status of BIOS & UEFI & Secure Boot with PowerShell
layout: post
date: '2013-01-11T14:22:06Z'
slug: how-to-check-the-status-of-bios-uefi-secure-boot-with-powershell
aliases:
- /2013/01/how-to-check-the-status-of-bios-uefi-secure-boot-with-powershell/
description: During the past weeks I spend a bit of time deploying Windows 8 to UEFI
  enabled clients. With PowerShell 3.0 on Windows 8 you will find some [new cmdl...
author: Alex Verboon
categories:
  - 'Windows'
tags:
  - 'PowerShell'
  - 'Secure-Boot'
---
During the past weeks I spend a bit of time deploying Windows 8 to UEFI enabled clients. With PowerShell 3.0 on Windows 8 you will find some [new cmdlets](http://technet.microsoft.com/en-us/library/jj603042.aspx) that provide information about the status of your system’s BIOS/UEFI/Secure boot configuration.

  The below table shows the return values depending on whether the system’s firmware is using BIOS, UEFI and if Secure boot is enabled or not.



                       **BIOS / UEFI Setup**

                        BIOS

                        UEFI with CSM

                        UEFI native

          Secure boot enabled

                        UEFI native

          Secure boot

          disabled


                                  **PowerShell Command**

                        Result

                                  Confirm-SecureBootUEFI

                        Cmdlet not supported on this platform

                        False

                        True

                        False

                                  Get-SecureBootUEFI –Name SetupMode

                        Cmdlet not supported on this platform

                        1

                        0

                        1

                                  Get-SecureBootUEFI –Name SecureBoot

                        Cmdlet not supported on this platform

                        0

                        1

                        0

                 Executing any of these cmdlets on a Windows 8 system that uses BIOS generates an error.

  The return value of the SetupMode variable tells us if the system is operating in Setup mode or in UserMode meaning that the platform key is enrolled. (For more details read the Firmware/OS Key Exchange: creating trust relationships chapter within the UEFI Specification that can be found [here](http://www.uefi.org/specs/))

  The return value of the SecureBoot variable tells us if the platform firmware is operating in secure boot mode. If the return value is 1 then SecureBoot is enabled meaning that the firmware performs driver and boot application signature verification. If the value is 0 then secure boot is not enabled.

  Additional Information:

  [Secure Boot Cmdlets in Windows PowerShell](http://technet.microsoft.com/en-us/library/jj603042.aspx)

  [Protecting the pre-OS environment with UEFI](http://blogs.msdn.com/b/b8/archive/2011/09/22/protecting-the-pre-os-environment-with-uefi.aspx)


