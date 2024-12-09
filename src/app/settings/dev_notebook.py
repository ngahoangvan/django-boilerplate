from .dev import *  # noqa

try:
    import jupyterlab  # noqa

    notebook_default_url = "/lab"
except ImportError:
    notebook_default_url = "/tree"

NOTEBOOK_ARGUMENTS = [
    "--ip",
    "0.0.0.0",
    "--port",
    "8888",
    "--NotebookApp.default_url",
    notebook_default_url,
]
IPYTHON_KERNEL_DISPLAY_NAME = "Django Kernel"
