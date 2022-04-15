'''Testing packageitstructureexample__init__()'''

from pathlib import Path
from beetools.beearchiver import Archiver
from packageitstructureexample import foo, bar


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)


def project_desc():
    return _PROJ_DESC


b_tls = Archiver(_PROJ_DESC, _PROJ_PATH)


class TestPackageItStructureExample:
    def test_exec_bar(self):
        """Assert class __init__"""
        assert bar.exec_bar()
        pass

    def test_exec_foo(self):
        """Assert class __init__"""
        assert foo.exec_foo()
        pass


del b_tls
