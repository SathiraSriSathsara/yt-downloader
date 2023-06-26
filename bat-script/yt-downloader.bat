@echo off

echo Youtube Video Downloader Made By Sathira Sri Sathsara


set /p "URL=Enter YouTube video URL: "

echo Fetching video title...
for /f "delims=" %%a in ('yt-dlp --get-title "%URL%"') do set "TITLE=%%a"

echo Choose video quality:
echo 1. Best quality
echo 2. 4K
echo 3. 1080p
echo 4. 720p
echo 5. 480p
echo 6. 360p
echo 7. 240p
echo 8. 144p

set /p "QUALITY=Enter the number corresponding to the desired quality: "

if "%QUALITY%"=="1" (
    set "FORMAT=bestvideo+bestaudio/best"
) else if "%QUALITY%"=="2" (
    set "FORMAT=bestvideo[height<=2160]+bestaudio/best[height<=2160]"
) else if "%QUALITY%"=="3" (
    set "FORMAT=bestvideo[height<=1080]+bestaudio/best[height<=1080]"
) else if "%QUALITY%"=="4" (
    set "FORMAT=bestvideo[height<=720]+bestaudio/best[height<=720]"
) else if "%QUALITY%"=="5" (
    set "FORMAT=bestvideo[height<=480]+bestaudio/best[height<=480]"
) else if "%QUALITY%"=="6" (
    set "FORMAT=bestvideo[height<=360]+bestaudio/best[height<=360]"
) else if "%QUALITY%"=="7" (
    set "FORMAT=bestvideo[height<=240]+bestaudio/best[height<=240]"
) else if "%QUALITY%"=="8" (
    set "FORMAT=bestvideo[height<=144]+bestaudio/best[height<=144]"
) else (
    echo Invalid input. Please enter a number between 1 and 8.
    pause
    exit /b
)

echo Downloading video...
yt-dlp %URL% -f "%FORMAT%" -o "%TITLE%.%(ext)s"

echo Merging video and audio...
ffmpeg -i "%TITLE%.%(ext)s" -i "%TITLE%.webm" -c copy "%TITLE%.mp4"

echo Cleanup...
del "%TITLE%.%(ext)s"
del "%TITLE%.webm"

echo Done.
pause
