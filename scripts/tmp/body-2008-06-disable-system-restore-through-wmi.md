If you are sure about what you are doing and you want to speed up the installation of multiple security patches or applications, you can use the following WMI command to disable Windows XP system restore.

on error resume next
set sr=GetObject("winmgmts:\\.\root\default:SystemRestore")
e=sr.disable("")

To turn on System Restore again, use the following command:

on error resume next
set sr=GetObject("winmgmts:\\.\root\default:SystemRestore")
e=sr.enable("")