# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NCS Example Application'
copyright = '2024, The Zephyr Community'
author = 'The Zephyr Community'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.intersphinx', 'breathe']

templates_path = ['_templates']
exclude_patterns = ['_build_sphinx', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

# -- Options for Intersphinx -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html

intersphinx_mapping = {
    'ncs': ('https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/', None),
    'nrfx': ('https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrfx/', None),
    'nrfxlib': ('https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrfxlib/', None),
    'zephyr': ('https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/zephyr/', None),
    'mcuboot': ('https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/mcuboot/', None),
    'tfm': ('https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/tfm/', None),
    'matter': ('https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/matter/', None),
}

## -- Options for Breathe ----------------------------------------------------
# https://breathe.readthedocs.io/en/latest/index.html
#
# WARNING: please, check breathe maintainership status before using this
# extension in production!

breathe_projects = {'ncs-example-application': '_build_doxygen/xml'}
breathe_default_project = 'ncs-example-application'
breathe_default_members = ('members', )
