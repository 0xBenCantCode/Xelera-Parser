import marshal
import types
from pyinstxtractor_ng.pyinstxtractor_ng import PyInstArchive

def extract_pyc(executable: str) -> None:
    extractor = PyInstArchive(executable)

    if extractor.open():
        if extractor.checkFile():
            if extractor.getCArchiveInfo():
                extractor.parseTOC()
                extractor.extractFiles("-d")
                extractor.close()
                print(
                    "[+] Successfully extracted pyinstaller archive: {0}".format(
                        executable
                    )
                )
                print("")
                print(
                    "You can now use a python decompiler on the pyc files within the extracted directory"
                )

        extractor.close()
    extractor.close()

def get_constants(file: str) -> list:
    with open(file, 'rb') as f:
        f.read(16)  # Skip the header
        code_object = marshal.load(f)  # Load the main code object

    stack = [code_object]
    constants = []

    while stack:
        current = stack.pop()
        for const in current.co_consts:
            if isinstance(const, types.CodeType):  # If it's a nested code object, add it to the stack
                stack.append(const)
            else:
                constants.append(const)

    return constants