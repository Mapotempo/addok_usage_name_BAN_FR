from addok.helpers import yielder

from . import utils
try:
    import pkg_resources
except ImportError:  # pragma: no cover
    pass
else:
    if __package__:
        VERSION = pkg_resources.get_distribution(__package__).version


make_labels = utils.make_labels
