# Build script for AppLab
# Usage: .\build.ps1

$ErrorActionPreference = "Stop"

Write-Host "Building AppLab..." -ForegroundColor Cyan

# Navigate to Laboratorio directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# Ensure PyInstaller is installed
Write-Host "Checking PyInstaller..." -ForegroundColor Yellow
python -m pip install pyinstaller --quiet

# Clean previous builds
if (Test-Path "dist") {
    Write-Host "Cleaning previous dist..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force "dist"
}
if (Test-Path "build") {
    Write-Host "Cleaning previous build..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force "build"
}

# Build with PyInstaller using spec file
Write-Host "Running PyInstaller..." -ForegroundColor Yellow
python -m PyInstaller AppLab.spec --noconfirm --clean

if ($LASTEXITCODE -eq 0) {
    Write-Host "Build successful! Output in dist/AppLab/" -ForegroundColor Green
    Write-Host "Run: .\dist\AppLab\AppLab.exe" -ForegroundColor Cyan
} else {
    Write-Host "Build failed!" -ForegroundColor Red
    exit 1
}
