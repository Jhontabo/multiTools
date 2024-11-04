import os
from yt_dlp import YoutubeDL

def download_youtube_content(url, type_download="audio", progress_callback=None):
    # Directorio base para organizar música y videos
    base_dir = "./../../../Documents/Music"
    all_music_dir = os.path.join(base_dir, "allMusic")
    all_videos_dir = os.path.join(base_dir, "Videos")
    os.makedirs(all_music_dir, exist_ok=True)
    os.makedirs(all_videos_dir, exist_ok=True)

    # Configuración de opciones de descarga para yt-dlp
    if type_download == "audio":
        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(all_music_dir, '%(title)s.%(ext)s'),
            'ignoreerrors': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [progress_callback] if progress_callback else []
        }
    else:
        opciones = {
            'format': 'best',
            'outtmpl': os.path.join(all_videos_dir, '%(title)s.%(ext)s'),
            'ignoreerrors': True,
            'progress_hooks': [progress_callback] if progress_callback else []
        }

    try:
        with YoutubeDL(opciones) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            
            # Verifica que la información del video se haya extraído correctamente
            if info_dict is None:
                print("Error: No se pudo obtener información del video.")
                return "No se pudo obtener información del video."

            title = info_dict.get("title", "Desconocido")
            print(f"Descarga completa: {title}")
            return "Descarga completa"

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return str(e)
