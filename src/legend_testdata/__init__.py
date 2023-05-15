"""Bare-bones Python package to access LEGEND test data files."""

from legend_testdata._version import version as __version__
from legend_testdata.core import LegendTestData

__all__ = ["__version__", "LegendTestData"]

import logging
log = logging.getLogger(__name__)
log.warning("the legend_testdata module has been renamed to legendtestdata, "
            "install pylegendtestdata and import legendtestdata to suppress this warning")
