## Automate project setup steps with Python, Powershell and Batch

### Powershell
- Enable Developer mode from Settings -> Update & Security
- Create a Powershell profile
- Check __**alias_name**__ in powershell and make sure it's not a duplicate
- If **Get-Alias** returns error than __**alias_name**__ is **unused**
- Register __**alias_name**__ in powershell, ex: __cpj__ that will also point to a **batch** file that will handle the rest
- Make sure to have the batch file created
```powershell
// Check Alias
Get-Alias -Name cpj

// Create a Powershell profile
new-item -type file -force $profile

// Open Powershell profile created in /USER_NAME/WindowsPowerShell/*.ps1
// AND
// Register ALIAS_NAME that will also point to a BATCH file to handle the rest -> Save
New-Alias -Name cpj -Value \path-to-bat-file\createProject.bat
```

### Batch
- Read parameters after __**alias_name**__, **dir_name** and **l**
- __L__ will be optional for local-only project)
```powershell
@echo off
set dn = %1
set fl = %2
cd /d %~dp0

If "%1" == "" (
  echo "error, should be 'cpj folder_name l(optional for local-only project)'"
) Else (
  If "%2" == "" (
    echo "RUN py remote.py" %dn%
  ) else (
    echo "RUN py local.py" %dn%
  )
)
```