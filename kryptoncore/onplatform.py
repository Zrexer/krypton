import platform

class onPlatform(object):
    def __init__(self) -> None:
        pass

    @property
    def os(self):
        return platform.system()