from loc import Loc


def compiler_error(loc: Loc, msg: str):
    """Print a compiler error at a location, DOES NOT EXIT AUTOMATICALLY"""
    print(f"error: {msg}\n at {loc}")

def compiler_warning(loc: Loc, msg: str):
    """Print a compiler warning at a location, DOES NOT EXIT AUTOMATICALLY"""
    print(f"warning: {msg}\n at {loc}")
