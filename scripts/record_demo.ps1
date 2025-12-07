<#
PowerShell recording helper using ffmpeg.
Usage examples:
# 1) Interactive: start the app and then start recording until you press Ctrl+C
    .\record_demo.ps1
# 2) Record for fixed duration in seconds (e.g., 420 seconds = 7 minutes)
    .\record_demo.ps1 -DurationSeconds 420

Notes:
- Requires ffmpeg available in PATH.
- Replace the microphone name below if detection returns a different label.
- By default this script captures a window titled "Personal Finance Tracker". If the window title differs, either change the -WindowTitle parameter when calling or run with -CaptureDesktop to capture whole screen.
#>
param(
    [int]$DurationSeconds = 0,
    [string]$Output = "recording.mkv",
    [string]$VenvActivate = ".\.venv\Scripts\Activate.ps1",
    [string]$WindowTitle = "Personal Finance Tracker",
    [switch]$CaptureDesktop
)

# Locate ffmpeg
$ffmpeg = "ffmpeg"

# Microphone device name - you may need to list devices with FFmpeg first:
# ffmpeg -list_devices true -f dshow -i dummy
$mic = "Microphone (Realtek(R) Audio)"

# Activate venv and launch the app in background
Write-Host "Starting app..."
Start-Process -FilePath powershell -ArgumentList "-NoExit", "-Command", "& { . $PWD\$VenvActivate; python .\src\main.py }"

Start-Sleep -Seconds 3

# Build ffmpeg capture arguments
if ($CaptureDesktop) {
    $videoInput = "-f gdigrab -framerate 30 -i desktop"
} else {
    $videoInput = "-f gdigrab -framerate 30 -i title='$WindowTitle'"
}

$audioInput = "-f dshow -i audio=\"$mic\""

$videoCodec = "-c:v libx264 -preset veryfast -crf 18"
$audioCodec = "-c:a aac -b:a 192k"

if ($DurationSeconds -gt 0) {
    $timeOpt = "-t $DurationSeconds"
} else {
    $timeOpt = ""
}

$cmd = "$ffmpeg $videoInput $audioInput $timeOpt $videoCodec $audioCodec -y $Output"
Write-Host "Running: $cmd"

# Start ffmpeg as a process
cmd /c $cmd

Write-Host "Recording finished. Output: $Output"
Write-Host "Tip: remux to MP4: ffmpeg -i $Output -c copy output.mp4"
