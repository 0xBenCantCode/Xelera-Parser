import tools
import base64

def get_token(constants):
    enc_token = constants[46]
    return (base64.b64decode(base64.b64decode(base64.b64decode(enc_token))).decode('utf-8'))

if __name__ == "__main__":
    import tools

    pyc_path = input("Enter path to imports.pyc: ")
    constants = tools.get_constants("final.exe_extracted/PYZ-00.pyz_extracted/imports/imports.pyc")
    
    print(get_token(constants))