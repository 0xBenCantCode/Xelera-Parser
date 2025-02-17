import re

def get_address(constants):    
    web_page = constants[52]
    return re.search(r'[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}', web_page)[0]


if __name__ == "__main__":
    import tools

    pyc_path = input("Enter path to imports.pyc: ")
    constants = tools.get_constants(pyc_path)
    
    print(get_address(constants))