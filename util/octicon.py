import os
from jinja2 import Markup

def get_octicon_svg(octicon, style=""):
    
    try:
        with open("{}/octicons/{}.svg".format(os.path.dirname(__file__), octicon),"rb") as f:
            return Markup("<span style={}>".format(style) + f.readline().decode('utf-8') + "</span>")
    except:
        raise Exception("Octicon Not Found")
