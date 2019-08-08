from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the gapminder.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "HRRR_dashboard.ipynb", "--allow-websocket-origin=*"])
