from imghdr import tests
from pathlib import Path


def resource_path(file_name):
    return str(Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute())
