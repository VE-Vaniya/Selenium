Get-Content .env | ForEach-Object {
    $line = $_.Trim()
    if ($line -and !$line.StartsWith('#')) {
        $parts = $line -split '=', 2
        if ($parts.Count -eq 2) {
            $key = $parts[0].Trim()
            $value = ($parts[1] -split '#')[0].Trim()
            Set-Variable -Name $key -Value $value -Scope Script
        }
    }
}

Write-Host "Starting Edge Node..." -ForegroundColor Green
Write-Host "Grid IP: $GRID_IP"
Write-Host "Port: $PORT_EDGE"

java "-Dwebdriver.edge.driver=$EDGE_DRIVER" `
    -jar $JAR_PATH node `
    --port $PORT_EDGE `
    --publish-events "tcp://${GRID_IP}:4442" `
    --subscribe-events "tcp://${GRID_IP}:4443"