import FreeSimpleGUI as fsg

label1 = fsg.Text("Select files to compress: ")
input1 = fsg.Input()
choose_btn1 = fsg.FilesBrowse("Choose files")

label2 = fsg.Text("Select destination folder: ")
input2 = fsg.Input()
choose_btn2 = fsg.FolderBrowse("Choose destination")

compress_btn = fsg.Button("Compress")

window = fsg.Window("File Compressor", layout=[[label1, input1, choose_btn1],
                                               [label2, input2, choose_btn2], [compress_btn]])

window.read()
window.close()

