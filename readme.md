## Automate project setup steps with Python, Powershell and Batch

### Setup
- Check/Register \*alias_name\* in powershell.
- If \*Get-Alias\* returns error than \*alias_name\* **unused**
- It will also point to a **batch** file that will handle the Python scripts
```
Get-Alias -Name cpj
Set-Alias -Name cpj  
```

### subtitle
```
somethin here
```