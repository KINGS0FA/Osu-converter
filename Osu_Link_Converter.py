import webbrowser
import PySimpleGUI as sg

label = sg.Text('Enter Osu Link to convert')
input_text = sg.InputText(tooltip='Enter Link ex:[https://osu.ppy.sh/beatmapsets/xxxxxx#osu/xxxxxxx', key='link')

button_1 = sg.Button('Nerinyan')
button_2 = sg.Button('Chimu')
button_3 = sg.Button('BeatConnect')

message = sg.Text(key='alert', font=('Helvetica', 10))
message2 = sg.Text(key='clink', font=('Helvetica', 10))
# convert_button = sg.Button('Convert')
window = sg.Window('Osu Link Converter',
                   layout=[[label],
                           [input_text],
                           [button_1, button_2, button_3],
                           [message],
                           [message2]],
                   size=(850, 250),
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print(event)
    print(values)
    link = values['link']
    start_marker = "beatmapsets/"
    end_marker = "#osu"
    start_index = link.find(start_marker) + len(start_marker)
    end_index = link.find(end_marker)
    extracted_string = link[start_index:end_index]

    print(extracted_string)
    print(event)
    print(values)
    print(values['link'])

    if len(values['link']) == 0:
        message.update(value='Enter URL!', text_color='red')
        continue
    elif 'beatmapsets/' not in values['link']:
        message.update(value='Invalid URL!', text_color='red')
        continue
    match event:
        case 'Nerinyan':
            webbrowser.open(f'https://nerinyan.moe/d/{extracted_string}')
            new_link = f'https://nerinyan.moe/d/{extracted_string}'
            input_text.update(value=link)
            message.update(value=f'Link converted to Nerinyan!', text_color='yellow')
            message2.update(value=new_link, text_color='Green')
        case 'Chimu':
            webbrowser.open(f'https://chimu.moe/d/{extracted_string}')
            new_link = f'https://chimu.moe/d/{extracted_string}'
            input_text.update(value=link)
            message.update(value=f'Link converted to Chimu!', text_color='yellow')
            message2.update(value=new_link, text_color='Green')


        case 'BeatConnect':
            webbrowser.open(f'https://beatconnect.io/b/{extracted_string}')
            new_link = f'https://beatconnect.io/b/{extracted_string}'
            input_text.update(value=link)
            message.update(value=f'Link converted to BeatConnect!', text_color='yellow')
            message2.update(value=new_link,  text_color='Green')


window.close()
