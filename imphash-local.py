import sys
import pefile
import os

def filename(fileName):
    return os.path.basename(fileName)

def calculate_imphash(file):
    ImpHash = pefile.PE(file).get_imphash()
    print("   File: ", filename(file))
    print("ImpHash: ", ImpHash, "\n")

def main():
    print("Drag-and-Drop binary and press [Enter] to process hash ('q' to quit)\n ")
    
    if len(sys.argv) > 1:
        for arg_file in sys.argv[1:]:
            if os.path.isfile(arg_file):
                calculate_imphash(arg_file)
            else:
                print(f"Invalid file path: {arg_file}\n")
    else:
        while True:
            filepath = input("[Drop Binary]: ")
            if filepath.lower() == 'q':
                break
            elif os.path.isfile(filepath):
                calculate_imphash(filepath)
            else:
                print("Invalid file path.\n")

if __name__ == "__main__":
    main()
