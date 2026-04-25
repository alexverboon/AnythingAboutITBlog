For years I have been using the following script from [myITforum](http://www.myitforum.com/articles/42/view.asp?id=11729) to list Task Sequence Environment Variables and Values 

  Set oTSEnv = CreateObject("Microsoft.SMS.TSEnvironment")     
For Each oVar In oTSEnv.GetVariables      
WScript.Echo oVar & "=" & oTSEnv(oVar)      
Next

  Because there are so many variables, the only useful way to use the script is to pipe the output into a file, then open that file and search for the variable and its value. 

  So I have created the created the script below that can do the following: 

     
- List both the System and Task Sequence variables    
- If you provide no command line option, all system environment variables and task sequence variables are listed.      
cscript ts_var.vbs    
- If you provide the first letter, all system environment variables and task sequence variables starting with that letter are listed     
cscript ts_var.vbs P    
- If you write the first letters of a variable only those environment variables and task sequence variables matching these letters are listed.      
cscript ts_var.vbs Processor 

  [
![clip_image002](images/clip_image002_thumb6.jpg)
](https://www.verboon.info/wp-content/uploads/2012/12/clip_image0026.jpg)

  Copy the below script into a file and save it as TS_var.vbs, then store the file into a location where you can access it while running an MDT or SCCM Task Sequence such as the <DeploymentShare>\Scripts folder. 

   

  On error resume next

  Set wshShell = CreateObject( "WScript.Shell")

  Set env = wshShell.Environment("System")

  Set env1 = CreateObject("Microsoft.SMS.TSEnvironment")

  If Err Then

         wscript.echo "TS Environment not availble"

         wscript.echo "The script can only be used while the Task Sequence components are loaded"

         wscript.quit()

  End if

   

  If Wscript.Arguments.Count = 0 Then

                wscript.echo "No first letter(s) of variable provided so showing all"

   

                wscript.echo "list all environment variables"

                For Each strItem In env

                       WScript.Echo strItem

                Next

   

                wscript.echo "list all TS variables"

                For each v in env1.GetVariables 

                       WScript.Echo v & " = " & env1(v) 

                Next 

   

   Else

       If Wscript.Arguments.Count > 0 Then

          VarLetter=WScript.Arguments.Item(0)

         If Len(Varletter) = 1 Then

   

                wscript.echo "list all environment variables starting with: " & Varletter

                For Each strItem In env

                If Ucase(Left(strItem,1)) = Ucase(Varletter) Then

                       WScript.Echo strItem

                End if

                Next

   

                wscript.echo "list all TS variables starting with: " & Varletter

   

                For each v in env1.GetVariables 

                If Ucase(Left(v,1)) = Ucase(Varletter) Then

                       WScript.Echo v & " = " & env1(v) 

                End if

                Next 

   

         Else

   

                wscript.echo "list variable: " &Varletter

                varlen=Len(Varletter)

                For Each strItem In env

                       If Ucase(Left(strItem,varlen)) = Ucase(Varletter) Then

                             WScript.Echo strItem

                       End if

                Next

   

                wscript.echo "list TS variable: " &Varletter

                varlen=Len(Varletter)

                For each v in env1.GetVariables 

                       If Ucase(Left(v,varlen)) = Ucase(Varletter) Then

                             WScript.Echo v & " = " & env1(v) 

                       End if

                Next

         End if

     End If

   End If