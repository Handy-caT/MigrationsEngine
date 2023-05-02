import filecmp
import os

import pytest

from migration.script.script_facade import ScriptFacade


tempdir = 'temp'
script_name = 'test_script.py'
script_path = tempdir + '/' + script_name
true_dir = 'true_files'
true_path = true_dir + '/' + script_name


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    """Fixture to execute asserts before and after a test is run"""
    if os.path.exists(tempdir):
        if os.path.exists(script_path):
            os.remove(script_path)

    yield  # this is where the testing happens

    if os.path.exists(tempdir):
        if os.path.exists(script_path):
            os.remove(script_path)

        os.rmdir(tempdir)


def test_parse_script(composite_ddl):
    facade = ScriptFacade(script_name, 'tests/integration/' + true_path)

    component = facade.parse_script()

    assert component is not None
    assert component == composite_ddl


def test_create_script(composite_ddl):
    facade = ScriptFacade(script_name, script_path)

    facade.create_script(composite_ddl)

    assert os.path.exists(tempdir)
    assert os.path.exists(script_path)

    assert os.path.getsize(script_path) > 0
    assert filecmp.cmpfiles(true_dir, tempdir, script_name, shallow=False)
