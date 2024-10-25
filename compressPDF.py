
import fitz  
from PIL import Image
import os

def compress_pdf(input_pdf, output_pdf, quality=75, zoom=2):
    doc = fitz.open(input_pdf)
    compressed_images = []

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)

        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        img_path = f"temp_page_{page_num}.jpg"
        img.save(img_path, "JPEG", quality=quality)
        compressed_images.append(img_path)

    new_doc = fitz.open()
    for img_path in compressed_images:
        img_pdf = fitz.open(img_path)
        rect = img_pdf[0].rect
        pdfbytes = img_pdf.convert_to_pdf()
        img_pdf.close()
        new_doc.insert_pdf(fitz.open("pdf", pdfbytes))

        os.remove(img_path)

    new_doc.save(output_pdf)
    new_doc.close()
    doc.close()

def compress_all_pdfs_in_folder(input_folder, output_folder, quality=75):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_pdf = os.path.join(input_folder, filename)
            output_pdf = os.path.join(output_folder, filename)

            print(f"Compressing {filename}...")
            compress_pdf(input_pdf, output_pdf, quality)
            print(f"Finished compressing {filename}.")

input_folder = r"E:\DESA PAKUTANDANG 251-300"
output_folder = r"E:\DESA PAKUTANDANG COMPRESS"
compress_all_pdfs_in_folder(input_folder, output_folder, quality=75)


# In[ ]:




