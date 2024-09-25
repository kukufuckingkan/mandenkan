import http.server
import socketserver
import os
import asyncio
import laucher
from laucher import launch
# Function to convert HTML to PDF with increased timeout
async def convert_html_to_pdf(html_file, pdf_file):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(f'file:///{html_file}', {'waitUntil': 'networkidle2', 'timeout': 60000})  # Increase timeout here
    await page.pdf({'path': pdf_file, 'format': 'A4'})
    await browser.close()

# Serve HTML files
html_dir = os.path.join(os.getcwd(), '_build', 'html')
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

os.chdir(html_dir)  # Change the current directory to the HTML directory

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTML files at http://localhost:{PORT}")
    
    # Run the conversion in an asyncio event loop
    html_file = "index.html"  # Specify your HTML file
    pdf_file = "output.pdf"    # Specify your desired output PDF file
    asyncio.run(convert_html_to_pdf(html_file, pdf_file))  # Convert HTML to PDF
    
    httpd.serve_forever()