Write-Host "Starting backup..."
 Copy-Item ".\documents\*" ".\backup\" -Recurse
 Write-Host "Backup completed."