import pikepdf

def remove_pdf_password(input_pdf, output_pdf, password=""):
    """
    Elimina la contraseña de un archivo PDF protegido y guarda una copia sin contraseña.

    :param input_pdf: Ruta del archivo PDF con contraseña.
    :param output_pdf: Ruta del archivo PDF sin contraseña.
    :param password: La contraseña actual del PDF.
    """
    try:
        with pikepdf.open(input_pdf, password=password) as pdf:
            pdf.save(output_pdf)
        print(f"Se eliminó la contraseña del archivo PDF: {input_pdf}")
    except pikepdf._qpdf.PasswordError:
        print("Contraseña incorrecta. No se pudo abrir el archivo PDF.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo PDF: {e}")
