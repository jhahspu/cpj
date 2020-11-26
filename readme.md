## Automate project setup steps with Python, Powershell and Batch

### Powershell
- Check/Register __**alias_name**__ in powershell.
- If **Get-Alias** returns error than __**alias_name**__ is **unused**
- It will also point to a **batch** file that will handle the Python scripts
```powershell
Get-Alias -Name cpj
Set-Alias -Name cpj -Value \path-to-bat-file\createProject.bat
```

### Batch
- Read parameters after __**alias_name**__, **dir_name** and **l** (optional for local-only project)
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