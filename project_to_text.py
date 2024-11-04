import os

def convert_project_to_text(directorio_proyecto, archivo_salida):
    importante = {
        "app": ["app"],
        "routes": ["routes"],
        "views": ["resources/views"],
        "public": ["public"],
        "config": [".env", "composer.json"]
    }

    def generar_estructura_importante(directorio, nivel=0):
        estructura = ""
        for nombre, paths in importante.items():
            for path in paths:
                ruta = os.path.join(directorio, path)
                if os.path.isdir(ruta):
                    estructura += "    " * nivel + f"- {nombre}/\n"
                    estructura += recorrer_directorio(ruta, nivel + 1)
                elif os.path.isfile(ruta):
                    estructura += "    " * nivel + f"- {path}\n"
        return estructura

    def recorrer_directorio(directorio, nivel):
        estructura = ""
        for item in sorted(os.listdir(directorio)):
            if item.startswith('.'):
                continue
            ruta_item = os.path.join(directorio, item)
            estructura += "    " * nivel + f"- {item}\n"
            if os.path.isdir(ruta_item):
                estructura += recorrer_directorio(ruta_item, nivel + 1)
        return estructura

    with open(archivo_salida, "w", encoding="utf-8") as salida:
        estructura = generar_estructura_importante(directorio_proyecto)
        salida.write(estructura)

    print(f"La estructura importante del proyecto se ha guardado en {archivo_salida}")
