import tools
import os
import time

from get_bot_token import get_token
from get_crypto_address import get_address

if __name__ == "__main__":
    path = input("Enter path to Xelera executable: ")
    extract_dir = f"{os.path.basename(path)}_extracted"
    
    tools.extract_pyc(path) # changes into extracted dir

    import_dir = f"PYZ-00.pyz_extracted/imports/imports.pyc"
    import_constants = tools.get_constants(import_dir)

    print(f"Found Discord Bot Token: {get_token(import_constants)}")
    print(f"Found Litecoin Address: {get_address(import_constants)}")
    