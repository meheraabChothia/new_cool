import fitz
import time
from termcolor import colored
import argparse
from dotenv import load_dotenv
import os

load_dotenv()

p = argparse.ArgumentParser()
p.add_argument("pdf", nargs="?", default=os.getenv("PRESET_DIR"),
               help="Path to PDF (defaults to the PRESET_DIR env var)")


pdf_args = p.parse_args()

doc = fitz.open(pdf_args.pdf)

for i in range(doc.page_count):
    page = doc.get_page_text(i)
    for j in page:
        asc = (ord(j))
        binary = bin(asc)[2:]
        print(colored(binary, "green"), end=" ", flush=True)
        time.sleep(0.005)
    print(" --- ", end="")
