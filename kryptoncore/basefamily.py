import base64

class BaseFamily(object):
    def __init__(self) -> None:
        pass
    
    def base85enc(self, text: str):
        return base64.b85encode(text.encode()).decode()

    def base85dec(self, encoded_string: str):
        return base64.b85decode(encoded_string).decode()
    
    def base64enc(self, text: str):
        return base64.b64encode(text.encode()).decode()

    def base64dec(self, encoded_string: str):
        return base64.b64decode(encoded_string).decode()
    
    def base32enc(self, text: str):
        return base64.b32encode(text.encode()).decode()

    def base32dec(self, encoded_string: str):
        return base64.b32decode(encoded_string).decode()
    
    def base16enc(self, text: str):
        return base64.b16encode(text.encode()).decode()

    def base16dec(self, encoded_string: str):
        return base64.b16decode(encoded_string).decode()
