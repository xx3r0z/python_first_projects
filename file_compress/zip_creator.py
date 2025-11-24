import zipfile
import pathlib

def make_archive(filepaths, destination):
    # This creates a path from the incoming string and it also takes argument as to what to name the file
    dest_path = pathlib.Path(destination, "compressed.zip")
    # This operates similarly as file reading or writing and the method takes destination location and read or write,
    # read is used to decrypt
    with zipfile.ZipFile(dest_path, 'w') as archive:
        # For loop is to feed the files to the compressor as incoming argument is a list
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            print(filepath)
            archive.write(filepath, arcname=filepath.name)


