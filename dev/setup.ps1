# groundWork setup — checks and installs what this assistant needs to read documents:
# Python, and MarkItDown with its PDF, Word, PowerPoint and Excel support.
# Run from the assistant folder:  powershell -ExecutionPolicy Bypass -File dev\setup.ps1
# Safe to run again: it installs only what is missing, and records the result in
# dev\local.json under "setup". The last line it prints is always: SETUP OK or SETUP FAILED.

$ErrorActionPreference = 'Continue'
$here = Split-Path -Parent $PSCommandPath
$localJson = Join-Path $here 'local.json'
$extras = 'markitdown[docx,pdf,pptx,xlsx,xls]'

function Refresh-Path {
    $env:Path = [Environment]::GetEnvironmentVariable('Path', 'User') + ';' +
                [Environment]::GetEnvironmentVariable('Path', 'Machine')
}

function Find-Python {
    # The Microsoft Store shortcut in WindowsApps is not Python: it opens the Store.
    foreach ($name in 'python', 'py') {
        foreach ($cmd in @(Get-Command $name -All -ErrorAction SilentlyContinue)) {
            if ($cmd.Source -like '*\WindowsApps\*') { continue }
            $v = & $cmd.Source --version 2>&1
            if ($LASTEXITCODE -eq 0 -and "$v" -match 'Python 3\.(\d+)' -and [int]$Matches[1] -ge 10) {
                return $cmd.Source
            }
        }
    }
    return $null
}

function Save-Result($ok, $python, $note) {
    $data = @{}
    if (Test-Path -LiteralPath $localJson) {
        $old = Get-Content -LiteralPath $localJson -Raw -Encoding UTF8 | ConvertFrom-Json
        foreach ($p in $old.PSObject.Properties) { $data[$p.Name] = $p.Value }
    } else {
        $data['preferences'] = @{ examples = $true }
    }
    $data.Remove('location')   # no longer used
    $data['setup'] = @{ ok = $ok; date = (Get-Date -Format 'yyyy-MM-dd'); python = "$python"; note = "$note" }
    $json = $data | ConvertTo-Json -Depth 5
    [System.IO.File]::WriteAllText($localJson, $json, (New-Object System.Text.UTF8Encoding $false))
}

# 1 — Python
$python = Find-Python
$installedPython = $false
if (-not $python) {
    $installedPython = $true
    Write-Output 'Python 3.10 or later not found. Installing Python for this user with winget...'
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        winget install -e --id Python.Python.3.12 --scope user --silent `
            --accept-package-agreements --accept-source-agreements | Out-Null
        Refresh-Path
        $python = Find-Python
        if (-not $python) {
            $guess = Join-Path $env:LOCALAPPDATA 'Programs\Python\Python312\python.exe'
            if (Test-Path -LiteralPath $guess) { $python = $guess }
        }
    }
    if (-not $python) {
        $note = 'Python could not be installed automatically. Install Python 3.12 from https://www.python.org/downloads/ (tick "Add python.exe to PATH"), or ask IT, then run this again.'
        Write-Output $note
        Save-Result $false '' $note
        Write-Output 'SETUP FAILED'
        exit 1
    }
}
Write-Output "Python: $python"

# 2 — MarkItDown
& $python -c "import markitdown" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Output 'Installing MarkItDown...'
    & $python -m pip install --user --quiet $extras 2>&1 | Select-Object -Last 3 | ForEach-Object { Write-Output "  $_" }
    & $python -c "import markitdown" 2>$null
    if ($LASTEXITCODE -ne 0) {
        $note = 'MarkItDown could not be installed. If your network uses a proxy, pip may need it: ask IT for the proxy address and run  python -m pip install --user --proxy http://PROXY:PORT "' + $extras + '"'
        Write-Output $note
        Save-Result $false $python $note
        Write-Output 'SETUP FAILED'
        exit 1
    }
}
& $python -c "import pdfminer, markitdown" 2>$null
if ($LASTEXITCODE -ne 0) {
    & $python -m pip install --user --quiet $extras 2>&1 | Out-Null
}
Write-Output 'MarkItDown: installed'
$note = ''
if ($installedPython) { $note = 'Python was installed just now: close and reopen Claude Code so it finds it.' ; Write-Output $note }
Save-Result $true $python $note
Write-Output 'SETUP OK'
