param(
  [string]$HostName = "127.0.0.1",
  [switch]$Production
)

$ErrorActionPreference = "Stop"
$blogRoot = Split-Path -Parent $PSScriptRoot
$rubyBin = "C:\Ruby34-x64\bin"

if (-not (Get-Command bundle -ErrorAction SilentlyContinue)) {
  if (Test-Path (Join-Path $rubyBin "bundle.bat")) {
    $env:Path = "$rubyBin;$env:Path"
  } else {
    throw "Ruby/Bundler not found. Install Ruby 3.4 with DevKit and reopen VS Code."
  }
}

$previousJekyllEnv = $env:JEKYLL_ENV
Push-Location $blogRoot
try {
  if ($Production) {
    $env:JEKYLL_ENV = "production"
  }

  & bundle exec jekyll s -l -H $HostName
  if ($LASTEXITCODE -ne 0) {
    throw "Jekyll exited with code $LASTEXITCODE."
  }
} finally {
  Pop-Location
  if ($null -eq $previousJekyllEnv) {
    Remove-Item Env:JEKYLL_ENV -ErrorAction SilentlyContinue
  } else {
    $env:JEKYLL_ENV = $previousJekyllEnv
  }
}
