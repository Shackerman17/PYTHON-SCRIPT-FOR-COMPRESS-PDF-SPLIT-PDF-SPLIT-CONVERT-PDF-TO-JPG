import PyPDF2
import os

def split_last_page_from_folder(input_folder, output_folder):
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


                    last_page = reader.pages[total_pages - 1]

                    writer = PyPDF2.PdfWriter()
                    writer.add_page(last_page)

                    output_pdf = os.path.join(output_folder, f'last_page_{filename}')
                    with open(output_pdf, 'wb') as output_file:
                        writer.write(output_file)

                print(f"Extracted the last page of '{input_pdf}' to '{output_pdf}'.")

            except Exception as e:
                print(f"Failed to process '{input_pdf}': {e}")

input_folder = 'C:\MBKM PROJECT\SUBT PAKUTANDANG'  
output_folder = 'C:\MBKM PROJECT\OUTPUT SPLIT PDF'  
split_last_page_from_folder(input_folder, output_folder)