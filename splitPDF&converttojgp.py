import PyPDF2
import os
from pdf2image import convert_from_path

def split_last_page_to_jpg(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_pdf = os.path.join(input_folder, filename)
            try:

                with open(input_pdf, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    total_pages = len(reader.pages)

                    if total_pages == 0:
                        print(f"The PDF '{input_pdf}' is empty.")
                        continue

                    last_page_number = total_pages - 1

                    images = convert_from_path(input_pdf, first_page=last_page_number + 1, last_page=last_page_number + 1)

                    output_image = os.path.join(output_folder, f'last_page_{filename[:-4]}.jpg')
                    images[0].save(output_image, 'JPEG')

                print(f"Extracted the last page of '{input_pdf}' and saved as '{output_image}'.")

            except Exception as e:
                print(f"Failed to process '{input_pdf}': {e}")


input_folder = r'C:\2. PTSL CIPARAY\MBKM PROJECT\SUBT PAKUTANDANG'  
output_folder = r'C:\2. PTSL CIPARAY\MBKM PROJECT\OUTPUT' 
split_last_page_to_jpg(input_folder, output_folder)