import legend_testdata as ldata
import pytest


def test_get_file():
    assert ldata.get_path('fcio/th228.fcio') == '/tmp/legend-testdata/data/fcio/th228.fcio'


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        ldata.get_path('non-existing-file.ext')
