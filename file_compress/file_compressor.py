import FreeSimpleGUI as fsg
import zip_creator

label1 = fsg.Text("Select files to compress: ")
input1 = fsg.Input()
choose_btn1 = fsg.FilesBrowse("Choose files", key='files')

label2 = fsg.Text("Select destination folder: ")
input2 = fsg.Input()
choose_btn2 = fsg.FolderBrowse("Choose destination", key='folder')

compress_btn = fsg.Button("Compress")
output = fsg.Text(key='output', text_color='green')

window = fsg.Window("File Compressor", layout=[[label1, input1, choose_btn1],
                                               [label2, input2, choose_btn2],
                                               [compress_btn, output]])


while True:
    event, values = window.read()
    files = values['files'].split(';')
    folder = values['folder']
    zip_creator.make_archive(files, folder)
    window['output'].update(value='Compression Completed')






window.close()

