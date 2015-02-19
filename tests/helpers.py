import contextlib
import tempfile
import shutil


@contextlib.contextmanager
def make_temp_directory():
    # from http://stackoverflow.com/questions/13379742
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)
