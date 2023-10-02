import PyPDF2

# Список имен файлов, которые нужно объединить
pdf_files = ["page1.pdf", "page 2.2.pdf"]

# Создайте объект PdfMerger
pdf_merger = PyPDF2.PdfMerger()

# Объедините файлы
for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

# Сохраните объединенный документ
with open("merged.pdf", "wb") as output_pdf:
    pdf_merger.write(output_pdf)

# Закройте объект PdfFileMerger
pdf_merger.close()
