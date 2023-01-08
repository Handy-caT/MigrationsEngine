import filecmp
import os

import pytest

from migration.script.script_builder.script_builder import ScriptBuilder
from migration.script.translator_to_command import TranslatorToCommand

tempdir = 'temp'
script_name = 'test_script.py'
script_path = tempdir + '/' + script_name


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


def test_script_builder(composite_ddl):
    true_dir = 'true_files'

    script_builder = ScriptBuilder(script_name, script_path)
    translator = TranslatorToCommand()

    result = translator.translate(composite_ddl)

    script_builder.build_info()
    script_builder.build_imports(result)
    script_builder.build_upgrade()
    script_builder.build_command(result)
    script_builder.close()

    assert os.path.exists(tempdir)
    assert os.path.exists(script_path)

    assert os.path.getsize(script_path) > 0
    assert filecmp.cmpfiles(true_dir, tempdir, script_name, shallow=False)



