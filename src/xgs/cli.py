try:
    from colorama import Fore, Style
except ImportError:
    class Fore:
        ...
    class Style:
        ...

from typing import Literal
from gi.repository import GLib
import sys
import os

class Arguments:
    config_file_path: str
    
    def __init__(self, name=sys.executable):
        self.name = name
    
    def add_arg(self, *names, help="", dest="", action: Literal["store","store-true"])
    
    def parse():
        ...
    def default():
        args = Arguments()
        args.config_file_path = os.path.join(GLib.get_home_dir(), ".config", "xgs")

        return args

