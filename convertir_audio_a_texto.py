import speech_recognition as sr
from pydub import AudioSegment
import os

def convertir_audio_a_texto(ruta_audio):
    # Convertir el audio a formato WAV si no lo es
    if not ruta_audio.endswith('.wav'):
        audio = AudioSegment.from_file(ruta_audio)
        ruta_audio = 'temp.wav'
        audio.export(ruta_audio, format='wav')
    
    # Crear el reconocedor
    recognizer = sr.Recognizer()

    # Cargar el archivo de audio
    with sr.AudioFile(ruta_audio) as source:
        audio_data = recognizer.record(source)

    # Intentar convertir audio a texto
    try:
        texto = recognizer.recognize_google(audio_data, language="es-ES")  # Cambia "es-ES" si el audio está en otro idioma
        print("Texto reconocido: ", texto)

        # Guardar el texto en un archivo .txt con el mismo nombre del audio
        nombre_salida = os.path.splitext(os.path.basename(ruta_audio))[0] + '.txt'
        with open(nombre_salida, 'w', encoding='utf-8') as f:
            f.write(texto)
        
        print(f"Texto guardado en: {nombre_salida}")
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return None
    except sr.RequestError:
        print("Error en la solicitud a Google Speech Recognition")
        return None

# Ejemplo de uso
ruta_audio = './Audio2.dat'  # Cambia a la ruta de tu archivo de audio
texto = convertir_audio_a_texto(ruta_audio)
