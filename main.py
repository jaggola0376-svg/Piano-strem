import subprocess
import os
import time

# السيرفر بيقرا المفتاح من الإعدادات بأمان
STREAM_KEY = os.environ.get("YOUTUBE_STREAM_KEY")

if not STREAM_KEY:
    print("⚠️ خطأ: لم يتم العثور على مفتاح البث!")
    while True: time.sleep(60)

STREAM_URL = f"rtmp://://youtube.com{STREAM_KEY}"

ffmpeg_command = [
    'ffmpeg',
    '-re',
    '-stream_loop', '-1',
    '-i', 'video.mp4',
    '-f', 'lavfi', '-i', 'sine=frequency=440:sample_rate=44100',
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '-preset', 'veryfast',
    '-b:v', '2000k',
    '-c:a', 'aac',
    '-b:a', '128k',
    '-ar', '44100',
    '-f', 'flv',
    STREAM_URL
]

print("🚀 انطلاق البث المستقر عبر Koyeb...")
try:
    subprocess.run(ffmpeg_command, check=True)
except Exception as e:
    print(f"خطأ: {e}")
    
