import bcrypt
from cryptography.fernet import Fernet
import os
from typing import Union
import base64
from functools import wraps
from flask_jwt_extended import get_jwt
from flask import jsonify

def hash_password(password: str) -> str:
    bytes_pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes_pwd, salt)
    return hashed_password.decode('utf-8')

def verify_password(hashed_password: str, password: str) -> bool:
    bytes_hashed_pwd = hashed_password.encode('utf-8')
    bytes_pwd = password.encode('utf-8')
    return bcrypt.checkpw(bytes_pwd, bytes_hashed_pwd)

def roles_required(*allowed_roles: int):

        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                claims = get_jwt()
                user_role = claims.get('role_id')

                if user_role not in allowed_roles:
                    return {
                        'error': 'Forbidden: You do not have permission to access this resource'
                    }, 403 
                
                return fn(*args, **kwargs)
            return wrapper
        return decorator


class Crypto:
    
    def __init__(self):
        
        self._key = os.getenv('FERNET_SECRET_KEY')
        self.validate_key()
        self.fernet = Fernet(self._key)
        
    
    def encrypt(self, value: Union[str, int, float, bool]) -> str:
        string_value = str(value)
        bytes_value = string_value.encode('utf-8')
        encrypted_value = self.fernet.encrypt(bytes_value)
        return encrypted_value.decode('utf-8')
    
    def decrypt(self, value: str) -> Union[str, int, float, bool]:
        bytes_value = value.encode('utf-8')
        decrypted_value = self.fernet.decrypt(bytes_value)
        return decrypted_value.decode('utf-8')
    
    def validate_key(self):
        if not self._key:
            raise ValueError('FERNET_SECRET_KEY is not set')
        
        try:
            bytes_key = base64.urlsafe_b64decode(self._key)
            
            if len(bytes_key) != 32:
                raise ValueError('Invalid key length')
                        
        except ValueError as e:
            raise ValueError(f'Invalid key: {e}')
    
    
    