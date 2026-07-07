import subprocess
import time
import os

# ⚠️ ضع هنا مفتاح البث الخاص بك بنظام RTMP من يوتيوب
STREAM_KEY = os.environ.get("YOUTUBE_STREAM_KEY", "هنا_تضع_مفتاح_البث_السري")

YOUTUBE_URL = "rtmp://://youtube.com"
STREAM_URL = YOUTUBE_URL + STREAM_KEY

# أمر FFmpeg المصلح كلياً لضبط تكرار الفيديو وتردد الصوت الصحيح لليوتيوب
ffmpeg_command = [
    'ffmpeg',
    '-re',                                # قراءة الملف بالسرعة الطبيعية لحماية السيرفر
    '-stream_loop', '-1',                  # تكرار الفيديو بشكل لانهائي وبدون توقف
    '-i', 'video.mp4',                    # اسم ملف الفيديو الخاص بك
    '-f', 'lavfi', '-i', 'sine=frequency=440:sample_rate=44100', # توليد دفق صوتي مستمر 44100Hz متوافق مع يوتيوب
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '-preset', 'veryfast',
    '-b:v', '2000k',
    '-c:a', 'aac',                        # ترميز الصوت بصيغة AAC القياسية لليوتيوب
    '-b:a', '128k',
    '-ar', '44100',                       # ضبط التردد لمنع خطأ الـ Muxer السابق
    '-f', 'flv',
    STREAM_URL
]

print("🚀 انطلاق البث السحابي المستقر إلى يوتيوب عبر Render...")
while True:
    try:
        subprocess.run(ffmpeg_command, check=True)
    except Exception as e:
        print(f"إعادة تشغيل تلقائية بسبب: {e}")
        time.sleep(2)
      
