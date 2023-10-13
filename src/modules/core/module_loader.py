import glob
import importlib
from os.path import basename, isfile, join

from src.modules.core.base_module import BaseModule

modules = glob.glob(join('./src/modules/', "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


def check_module_class(module) -> bool:
    if not getattr(module, "__cls_name__") or getattr(module, getattr(module, "__cls_name__")):
        return False
    return True


def get_module(module_name: str) -> BaseModule | None:
    module = importlib.import_module(f'src.modules.{module_name}')
    if not module or check_module_class(module):
        return None

    return getattr(module, getattr(module, "__cls_name__"))()


loaded_models = [get_module(module_name) for module_name in __all__]
