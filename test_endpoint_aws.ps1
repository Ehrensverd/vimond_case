$uri = 'http://vimond-test.eba-vndd7pnc.eu-central-1.elasticbeanstalk.com/api/process_intervals/'

$body = @{
    includes = @( @(4, 22), @(-4, -1), @(34, 76) )
    excludes = @( @(5, 10), @(35, 40) )
}

$jsonBody = $body | ConvertTo-Json -Depth 10


$headers = @{
    "Content-Type" = "application/json"
}


$response = Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $jsonBody
$response.Content
