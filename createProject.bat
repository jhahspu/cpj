@ECHO OFF

CD /d %~dp0

IF "%1" == "" (
  ECHO "error, should be 'cpj folder_name l(optional for local-only project)'"
) ELSE (
    py createProject.py %*%
  )
)