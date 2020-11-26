## Automate project setup steps with Python, Powershell and Batch

### Batch
- This will read the parameters after the command we'll create for PowerShell
- So create this basic file, and we'll update it afterwards
```powershell
@ECHO OFF
CD /d %~dp0
IF "%1" == "" (
  ECHO "error, should be 'cpj folder_name l(optional for local-only project)'"
) ELSE (
    py createProject.py %*%
  )
)
```
- Example file in project

### Powershell

- Enable Developer mode from Settings -> Update & Security
- Create a Powershell profile and Edit
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
- This will also point to a **batch** file that will handle the rest
```powershell
New-Alias -Name cpj -Value \path-to-bat-file\createProject.bat
```
- Example files in project

## Python

- With **sys** library we can read the passed paramateres
```python
if (len(sys.argv) > 2):
    print('creating local project: ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]))
else:
    print('creating remote project: ' + str(sys.argv[1]))
```
- Example file in project
