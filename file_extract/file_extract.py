import FreeSimpleGUI as fsg
import extractor as ext

select_label1 = fsg.Text('Select Archive')
select_input1 = fsg.Input()
select_btn1 = fsg.FilesBrowse('Choose file to extract', key='files')

select_label2 = fsg.Text('Select Path')
select_input2 = fsg.Input()
select_btn2 = fsg.FolderBrowse('Choose Path', key='filePath')

extract_btn = fsg.Button('Extract Button', key='extractBtn')
success_label = fsg.Text('',key='output', text_color='green')
exit_btn = fsg.Button('Exit')

col1 = fsg.Column([[select_label1], [select_label2]])
col2 = fsg.Column([[select_input1], [select_input2]])
col3 = fsg.Column([[select_btn1], [select_btn2]])

window = fsg.Window('File Extractor', [[col1, col2, col3], [extract_btn, success_label], [exit_btn]])

while True:
    event, values = window.read()
    print('event: ', event)
    print('values: ', values)

    match event:
        case 'extractBtn':
            try:
                if values['filePath'] == '':
                    window["output"].update(value="Select a destination!!", text_color='white')
                else:
                    filepath = values['files']
                    dest_path = values['filePath']
                    print('filepath: ', filepath)
                    print('destination: ', dest_path)
                    ext.extract(filepath, dest_path)

                    window["output"].update(value="Extraction Successful!")
            except FileNotFoundError:
                window["output"].update(value="Select a file to extract, and a directory!", text_color='white')

        case 'Exit':
            break

window.close()

