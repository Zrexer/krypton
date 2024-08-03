import hashlib

class HashClip(object):
    def __init__(self) -> None:
        pass

    def md5(self, text: str = ""):
        md5 = hashlib.md5()
        md5.update(text.encode())
        return md5.hexdigest()
    
    def sha1(self, text: str = ""):
        sha1 = hashlib.sha1()
        sha1.update(text.encode())
        return sha1.hexdigest()
    
    def sha224(self, text: str = ""):
        sha224 = hashlib.sha224()
        sha224.update(text.encode())
        return sha224.hexdigest()
    
    def sha256(self, text: str = ""):
        sha256 = hashlib.sha256()
        sha256.update(text.encode())
        return sha256.hexdigest()
    
    def sha384(self, text: str = ""):
        sha384 = hashlib.sha384()
        sha384.update(text.encode())
        return sha384.hexdigest()
    
    def sha512(self, text: str = ""):
        sha512 = hashlib.sha512()
        sha512.update(text.encode())
        return sha512.hexdigest()