@echo off
setlocal
cd /d "%~dp0"
echo ========================================================
echo       Installing Sadhana Journal CSL Style to Zotero
echo ========================================================
echo.

where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python install_style.py
    goto :end
)

where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    py install_style.py
    goto :end
)

echo [INFO] Python not detected, falling back to PowerShell installer...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$csl = Join-Path $PSScriptRoot 'sadhana-journal.csl'; " ^
    "$zoteroStyles = Join-Path $HOME 'Zotero\styles'; " ^
    "if (-not (Test-Path $zoteroStyles)) { New-Item -ItemType Directory -Path $zoteroStyles -Force | Out-Null }; " ^
    "$dest = Join-Path $zoteroStyles 'sadhana-journal.csl'; " ^
    "Copy-Item -Path $csl -Destination $dest -Force; " ^
    "Write-Host '[SUCCESS] Installed Sadhana style to:' $dest -ForegroundColor Green; " ^
    "$proc = Get-Process -Name zotero -ErrorAction SilentlyContinue; " ^
    "if ($proc) { Write-Host '[WARNING] Zotero is currently running. Please restart Zotero.' -ForegroundColor Yellow } else { Write-Host '[SUCCESS] Complete. Open Zotero to use the style.' -ForegroundColor Green }"

:end
echo.
echo Press any key to exit...
pause >nul
