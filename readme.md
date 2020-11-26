## Automate any project setup steps with Python, Powershell and Batch

### Batch
- This will read the parameters after the command we'll create for PowerShell
- So create this basic batch file, and we'll update it afterwards
- Named it __createProject.bat__ & saved it in my Projects folder
```powershell
@ECHO OFF
CD /d %~dp0
IF "%1" == "" (
  ECHO "error, should be 'cpj folder_name project_type l (where l is optional for local-only project)'"
) ELSE (
    py createProject.py %*%
  )
)
```

### Powershell

- Enable Windows Developer mode from Settings -> Update & Security
- Create a Powershell profile
```powershell
new-item -type file -force $profile
```

- Check __**alias_name**__ in powershell
- Should return error if not duplicate
```powershell
Get-Alias -Name cpj
```

- Register __**alias_name**__ in the PowerShell $profile
- $Profile file is in /USER_NAME/Documents/WindowsPowerShell/*.ps1
- This should also point to the previously created **batch** file
```powershell
New-Alias -Name cpj -Value \path\to\bat\file\createProject.bat
```

## Python

- With **sys** library we can read the passed paramateres
- Named it __createProject.py__ and saved it in my Projects folder
```python
import sys

if (len(sys.argv) > 3):
    print('creating local project: ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' ' + str(sys.argv[3]))
else:
    print('creating remote project: ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]))

ToDo: Function to handle arguments
```

## The command

```powershell
cpj folder_name project_type l
```
- arg[0] - **cpj** - is the name we chose for this task
- arg[1] - **folder_name** - name of project and folder
- arg[2] - **project_type** - for example 'html'
- arg[3] - **l** - (L - optional) for local only project // if ommited should create repo and set origin main
