import os, sys, subprocess, requests, time, json
import nbformat, io
from nbconvert import HTMLExporter, RSTExporter, writers
from traitlets.config import Config
from contextlib import redirect_stdout
from bs4 import BeautifulSoup

#
# Takes a Jupyter notebook (.ipynb) as a raw Unicode text string
# Returns rendered HTML version of notebook as an HTML string output
#
def auto_convert(response):
    start = time.time()

    # nbformat.reads converts the raw Unicode text to NotebookNode object
    jake_notebook = nbformat.reads(response, as_version=4)

    # Config object to set template object to identify source code inputs
    c = Config()
    c.TemplateExporter.template_file = 'tag_code.tpl'

    # Create new HTMLExporter with this configuration and export
    html_exporter = HTMLExporter(config = c)
    (body, resources) = html_exporter.from_notebook_node(jake_notebook)

    # Take raw body content and resourses, then print output as all-inclusive HTML text
    # Images and other resources are encoded as inline base-64
    output = writers.StdoutWriter()

    # Capture printed output and return as a string
    f = io.StringIO()
    with redirect_stdout(f):
        output.write(body, resources)

    final_html = f.getvalue()
    soup = BeautifulSoup(final_html, 'html.parser')

    # Split img tag
    img_tag_split = str(soup.find("img")).split(';base64,')

    # If there is a base64 image in the HTML
    if (len(img_tag_split) > 1):
        # Get the raw binary sequence from the <img> tag of the HTML
        binary_image = img_tag_split[1][:-4]

        # Get the file type from the <img> tag of the HTML
        image_type = img_tag_split[0].split('/')[1]

        # Pack up our work and get ready to deliver
        render_package = {
            "preview_img": {
                "binary": binary_image,
                "type": image_type
            },
            "final_html": final_html
        }
        
    # If there's no base64 image in HTML
    else:
        render_package = {
            "final_html": final_html
        }
    
    # Convert Python dict to JSON string
    render_package = json.dumps(render_package)

    end = time.time()
    print ("*****\nTotal Execution Time: " + str(round((end - start),2)) + "\n*****")

    # Pass HTML string to calling function
    return render_package
        
