Get-Content .env | ForEach-Object {
    if ($_ -match "^(.*?)=(.*)$") {
        Set-Item -Path "Env:$($matches[1])" -Value $matches[2]
    }
}

# Run Selenium Hub
java -jar $Env:Jar_PATH hub