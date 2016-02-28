"""
    The high level modeling context
	Provides global context for all objects within the same feature tree
"""
class Context(object):
    """
        A shared context for modeling.

        All objects in the same CQ chain share a reference to this same object instance
        which allows for shared state when needed
    """
    def __init__(self):
        self.tolerance = 0.0001  # user specified tolerance