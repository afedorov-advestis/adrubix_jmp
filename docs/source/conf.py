# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os.path
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('../../'))
# sys.path.extend(
#     [
#         # numpy standard doc extensions
#         os.path.join(os.path.dirname(__file__), "..", "../..", "sphinxext")
#     ]
# )

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'complex'
copyright = f"{datetime.now().year}, Advestis"
author = 'Advestis'
source_suffix = [".md", ".rst"]
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx_mdinclude'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

html_static_path = ["_static"]

html_favicon = "_static/favicon.png"

html_logo = "_static/logo_Advestis_HD.png"

# html_css_files = [
#     'css/custom.css'
# ]

html_theme_options = {
    "icon_links": [
        {
            "name": "Site web",
            "url": "https://www.advestis.com/",
            "icon": "fab fa-google",
        }, ],
    "github_url": "https://github.com/Advestis",

}

autodoc_mock_imports = ["pandas"]
html_context = {
   "default_mode": "light"
}
html_sidebars = {
    "**": ["search-field.html"]
}

intersphinx_mapping = {'pandas': ('https://pandas.pydata.org/docs/', None),
                       'numpy': ('https://numpy.org/doc/stable/', None)}

napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True
