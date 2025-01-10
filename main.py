import os
from pikepdf import Pdf
from fpdf import FPDF

OUTPUT_DIR = "output"
SOURCE_DIR = "source"
CURRENT_DIR = os.getcwd()

# init
if (os.path.isdir(OUTPUT_DIR) == False):
    os.mkdir(OUTPUT_DIR)
if (os.path.isdir(SOURCE_DIR) == False):
    os.mkdir(SOURCE_DIR)

files = os.listdir(SOURCE_DIR)
if (len(files) == 0):
    print(f"No source file in folder \"{SOURCE_DIR}\"")
files.sort()
os.chdir(SOURCE_DIR)

# input
first_page_text = input("Input first page text (leave empty if you want skip):\n")
def create_first_page(first_page_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=20)

    text_height = pdf.font_size
    page_height = pdf.h
    center_y = (page_height-text_height)/2

    pdf.set_xy(0, center_y)
    pdf.cell(w=0, h=10, text=first_page_text, border=0, align="C")
    pdf.output("title.pdf")

# process
output = Pdf.new()

if (first_page_text != ""):
    create_first_page(first_page_text)
    file = Pdf.open("title.pdf")
    output.pages.append(file.pages[0])
    output.add_blank_page()
    os.remove("title.pdf")

for file_name in files:
    file = Pdf.open(file_name)

    for page in file.pages:
        output.pages.append(page)
    if (len(file.pages)%2 == 1):
        output.add_blank_page()

os.chdir(CURRENT_DIR+"/"+OUTPUT_DIR)
output.save("output.pdf")

print(f"Task done, result file in folder \"{OUTPUT_DIR}\"")