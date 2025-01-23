import fitz  # PyMuPDF
import os

def save_pdf_pages_as_images(pdf_path, output_folder, start_page, end_page):
    try:
        # Abrir el archivo PDF
        pdf_document = fitz.open(pdf_path)
        
        # Crear carpeta de salida si no existe
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Asegurarse de que las páginas especificadas estén dentro del rango válido
        start_page = max(1, start_page)  # Las páginas comienzan en 1
        end_page = min(len(pdf_document), end_page)
        
        # Iterar por las páginas especificadas
        for page_number in range(start_page - 1, end_page):  # fitz usa índice desde 0
            page = pdf_document[page_number]
            # Renderizar la página como imagen
            pix = page.get_pixmap()
            # Nombre del archivo de salida
            output_path = os.path.join(output_folder, f"Pagína_{page_number + 1}.png")
            # Guardar la imagen
            pix.save(output_path)
            print(f"Página {page_number + 1} guardada como imagen en {output_path}")
        
        pdf_document.close()
        print("Proceso completado.")
    
    except Exception as e:
        print(f"Error: {e}")

# Solicitar datos al usuario
pdf_path = input("Ingrese la ruta completa del archivo PDF: ")
output_folder = input("Ingrese la ruta de la carpeta donde se guardarán las imágenes: ")

while True:
    try:
        start_page = int(input("Ingrese el número de la página inicial: "))
        end_page = int(input("Ingrese el número de la página final: "))
        if start_page > 0 and end_page >= start_page:
            break
        else:
            print("Por favor, ingrese un rango de páginas válido (números positivos y start <= end).")
    except ValueError:
        print("Por favor, ingrese números válidos para el rango de páginas.")

# Ejecutar la función
save_pdf_pages_as_images(pdf_path, output_folder, start_page, end_page)
