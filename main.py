import markdown
from pyscript import document
from js import window

def convert_markdown(event=None):
    # Get input content
    content = document.querySelector("#editor").value
    
    # Convert to HTML
    html_content = markdown.markdown(content, extensions=['extra', 'codehilite', 'toc'])
    
    # Update preview
    preview_element = document.querySelector("#preview")
    preview_element.innerHTML = html_content

# Initial conversion
convert_markdown()

# Hook into window for button access
window.convert_markdown = convert_markdown
