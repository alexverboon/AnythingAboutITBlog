---
title: PowerShell - Creating Scheduled Tasks with PowerShell version 3
layout: post
date: '2013-12-29T17:45:30Z'
slug: powershell-creating-scheduled-tasks-with-powershell-version-3
aliases:
- /2013/12/powershell-creating-scheduled-tasks-with-powershell-version-3/
description: I am currently working on a script where I need to create a scheduled
  task that runs a powershell script at a given time. With PowerShell 4.0 a schedu...
author: Alex Verboon
categories:
  - 'PowerShell'
tags:
  - 'Schedule'
  - 'Scheduled-Tasks'
---
I am currently working on a script where I need to create a scheduled task that runs a powershell script at a given time. With PowerShell 4.0 a scheduled task can be easily created with the new cmdlets [New-ScheduledTaskAction](http://technet.microsoft.com/en-us/library/jj649817.aspx), [New-ScheduledTaskTrigger](http://technet.microsoft.com/en-us/library/jj649821.aspx) and [Register-ScheduledTask](http://technet.microsoft.com/en-us/library/jj649811.aspx), but unfortunately i have to create a solution that works on clients running PowerSshell version 3.0. 

 When searching the web for examples how others have solved this I found many examples where people invoke the [schtasks.exe](http://msdn.microsoft.com/en-us/library/windows/desktop/bb736357(v=vs.85).aspx) command but in order to further improve my PowerShell skills I wanted to avoid calling external executables and do as much in PowerShell as possible. So after a bit of further searching I found an interesting [post](http://letitknow.wordpress.com/2011/05/20/create-scheduled-task-by-using-powershell/) from @letitknowblog who uses the Task Scheduler’s com object for creating a scheduled task. 

 To simplify sharing my lessons learned I’ve created a simple script that does the following. 

  
- Define variables for the Schedled Task name, description, command,  command argument to be executed  
- Define the time when the scheduled task must run, the below task will only run once.  
- Create the scheduled task, actions and triggers

```powershell
# The name of the scheduled task
$TaskName = "MyScheduledTask"
# The description of the task
$TaskDescr = "Run a powershell script through a scheduled task"
# The Task Action command
$TaskCommand = "c:\windows\system32\WindowsPowerShell\v1.0\powershell.exe"
# The PowerShell script to be executed
$TaskScript = "C:\scripts\myscript.ps1"
# The Task Action command argument
$TaskArg = "-WindowStyle Hidden -NonInteractive -Executionpolicy unrestricted -file $TaskScript"

# The time when the task starts, for demonstration purposes we run it 1 minute after we created the task
$TaskStartTime = [datetime]::Now.AddMinutes(1) 

# attach the Task Scheduler com object
$service = new-object -ComObject("Schedule.Service")
# connect to the local machine. 
# http://msdn.microsoft.com/en-us/library/windows/desktop/aa381833(v=vs.85).aspx
$service.Connect()
$rootFolder = $service.GetFolder("\")

$TaskDefinition = $service.NewTask(0) 
$TaskDefinition.RegistrationInfo.Description = "$TaskDescr"
$TaskDefinition.Settings.Enabled = $true
$TaskDefinition.Settings.AllowDemandStart = $true

$triggers = $TaskDefinition.Triggers
#http://msdn.microsoft.com/en-us/library/windows/desktop/aa383915(v=vs.85).aspx
$trigger = $triggers.Create(1) # Creates a "One time" trigger
$trigger.StartBoundary = $TaskStartTime.ToString("yyyy-MM-dd'T'HH:mm:ss")
$trigger.Enabled = $true

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa381841(v=vs.85).aspx
$Action = $TaskDefinition.Actions.Create(0)
$action.Path = "$TaskCommand"
$action.Arguments = "$TaskArg"

#http://msdn.microsoft.com/en-us/library/windows/desktop/aa381365(v=vs.85).aspx
$rootFolder.RegisterTaskDefinition("$TaskName",$TaskDefinition,6,"System",$null,5)

```powershell
Now if we wanted to run the Task more than just once, let’s say on a monthly basis, we have to change and add a bit of code  The code above uses Create(1) which means that the trigger is set to run once. 

```powershell
$trigger = $triggers.Create(1) # Creates a "One time" trigger

```powershell

If we want to use another schedule we must use one of the following values as explained in more detail [here](http://msdn.microsoft.com/en-us/library/windows/desktop/aa383915(v=vs.85).aspx). 

TASK_TRIGGER_EVENT 
0

TASK_TRIGGER_TIME
1

TASK_TRIGGER_DAILY 
2

TASK_TRIGGER_WEEKLY
3

TASK_TRIGGER_MONTHLY 
4

TASK_TRIGGER_MONTHLYDOW
5

TASK_TRIGGER_IDLE
6

TASK_TRIGGER_REGISTRATION
7

TASK_TRIGGER_BOOT
8

TASK_TRIGGER_LOGON 
9

TASK_TRIGGER_SESSION_STATE_CHANGE
11
So let’s suppose we want to run the task the first day of every month, we then have to change the code as following. 

```powershell
$trigger = $triggers.Create(4)
$trigger.DaysOfMonth = 1

```powershell
If we want to run the task when the system is idle we set the value of Create to 6.

```powershell
$trigger = $triggers.Create(6)

```powershell

If more than one action is required, just add an action, action path and action argument as in the example below. 

```powershell
$Action = $TaskDefinition.Actions.Create(0)
$action.Path = "$TaskCommand"
$action.Arguments = "$TaskArg"
$Action = $TaskDefinition.Actions.Create(0)
$action.Path = "notepad.exe"
$action.Arguments = ""

```

The following code registers the scheduled task

```
$rootFolder.RegisterTaskDefinition("$TaskName",$TaskDefinition,6,"System",$null,5)

```powershell

If the first parameter is set to $null, a random GUID is assigned as the Task name. 

```powershell
$rootFolder.RegisterTaskDefinition($null,$TaskDefinition,6,"System",$null,5)

```powershell
The $Taskdefinition holds all the previously defined settings for the scheduled task. 

The value 6 referts to the task creation constant which means that Task Scheduler either registers the task as a new task or as an updated version if the task already exists. A complete listing of possible values can be found [here](http://msdn.microsoft.com/en-us/library/windows/desktop/aa381365(v=vs.85).aspx). 

The next value defines the user context in wich the task runs, in this case we run the scheduled task within the system context. 

The last value defines the logon type. The value of 5 Indicates that a Local System, Local Service, or Network Service account is being used as a security context to run the task. A complete listing of possible values can be found [here](http://msdn.microsoft.com/en-us/library/windows/desktop/aa381365(v=vs.85).aspx)

# Much simpler when using PowerShell version 4

With PowerShell version 4 things get a bit simpler, to accomplish the same as in the aboe scrpt only 3 lines of code are needed. 

```powershell
$TaskAction = New-ScheduledTaskAction -Execute "$TaskCommand" -Argument "$TaskArg" 
$TaskTrigger = New-ScheduledTaskTrigger -At $TaskStartTime -Once
Register-ScheduledTask -Action $TaskAction -Trigger $Tasktrigger -TaskName "$TaskName" -User "System" -RunLevel Highest

```
