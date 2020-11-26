## Automate project setup steps with Python, Powershell and Batch

### Setup
- Check/Register __**alias_name**__ in powershell.
- If **Get-Alias** returns error than __**alias_name**__ is **unused**
- It will also point to a **batch** file that will handle the Python scripts
```powershell
Get-Alias -Name cpj
Set-Alias -Name cpj -Value \path-to-bat-file\createProject.bat
```

### subtitle
```
somethin here
```