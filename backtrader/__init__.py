from importlib import import_module

_pwb = import_module("pwb_backtrader")
globals().update(_pwb.__dict__)
