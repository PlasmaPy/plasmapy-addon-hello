"""
The `plasmapy-add-hello` package is an example demonstrating how to setup
an independent (from PlasmaPy) distribution that extends the capabilities of
`PlasmaPy <https://github.com/PlasmaPy/PlasmaPy>`_.  This is done by utilizing
the `plasmapy.addons` `entry_points` setup in the `plasmapy` package.  To see
the actually setting of the entry points look form the `[options.entry_points]`
heading in this distributions `setup.cfg file <>`_.
"""
__all__ = ['HELLO_STATEMENT', 'hello']

from pkg_resources import (DistributionNotFound, get_distribution)
from textwrap import fill as _tw_fill

# -- Generate Version ----------------------------------------------------------
try:
    # this places a runtime dependency on setuptools
    #
    # note: if there's any distribution metadata in your source files, then
    #       this will find a version based on those files.  Keep distribution
    #       metadata out of your repository unless you've intentionally
    #       installed the package as editable (e.g.
    #       `pip install -e {root_directory}`), but then __version__ will
    #       not be updated with each commit, it is frozen to the version at
    #       time of install.
    __version__ = get_distribution("plasmapy-addon-hello").version
except DistributionNotFound:
    # package is not installed
    fallback_version = 'unknown'
    try:
        # code most likely being used from source
        # if setuptools_scm is installed then generate a version
        from setuptools_scm import get_version
        __version__ = get_version(root='..',
                                  relative_to=__file__,
                                  fallback_version=fallback_version)
        del get_version
        warn_add = 'setuptools_scm failed to detect the version'
    except ModuleNotFoundError:
        # setuptools_scm is not installed
        __version__ = fallback_version
        warn_add = 'setuptools_scm is not installed'

    if __version__ == fallback_version:
        from warnings import warn
        warn(f"__version__ not generated (set to 'unknown'), "
             f"plasmapy-addon-hello is not an installed package and "
             f"{warn_add}.", RuntimeWarning)

        del warn
    del fallback_version, warn_add

# -- Package Contents ----------------------------------------------------------
#: `plamapy-add-hello`'s hello statement
HELLO_STATEMENT = (
    "Hello...I'm an example of a PlasmaPy addon package.  My primary function "
    "is to extend the functionality of PlasmaPy by adding myself to the "
    "plasmapy.addons sub-package."
)


def hello(width: int = 80):
    """
    Print to screen the :data:`HELLO_STATEMENT`.

    Parameters
    ----------
    width: int, optional
        set the width of the printed text (default 80)
    """
    print(_tw_fill(HELLO_STATEMENT, width=width))


# -- Cleanup Namespace ---------------------------------------------------------
del DistributionNotFound, get_distribution
