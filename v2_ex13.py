# pip install pdfkit
# sudo apt-get install wkhtmltopdf 
# run from wr folder

import pdfkit

url = open("config_v2_ex13.txt","r")
pdfkit.from_url(url.read(), 'out.pdf')