$targetPath = Join-Path $PSScriptRoot "src\ahmad\Workload\WEB_DRIVERS"

if ($PWD.Path -ne $targetPath) {
    Set-Location -Path $targetPath
}

python "checkbox.py"
