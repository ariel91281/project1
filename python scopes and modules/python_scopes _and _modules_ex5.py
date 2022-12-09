import os

def find_files(filename, search_path):
    result = ""
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result = os.path.join(root, filename)
            if os.access(result, os.X_OK):
                print("executable")
            else:
                print("not executable")
                os.chmod(result, 0o776)
            break

print(find_files("myfile","/home/ariel"))

