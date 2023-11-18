Invoke-WebRequest -Uri "http://localhost:8000/api/process_intervals/" -Method POST -Body @{
    "includes" = "200-300,10-100,400-500"
    "excludes" = "410-420,95-205,14,100-150"
}