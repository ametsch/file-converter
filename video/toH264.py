from os import system, name

def file_extension(path: str) -> str:
    return path.strip().split('.')[-1].lower()

video_input_extentions = ['mp4','avi','avs2','drc','vc2','dnxhd','dnxhr','h264','264','hevc','h265','265','m4v','mjpg','mjpeg',
                    'mpg','mpeg','m1v','m2v','yuv','rgb','flv','live_flv','kux','mov','3gp','3g2','mj2','psp','m4b','ism','ismv',
                    'isma','f4v','m4a','wmv']

input_file = ''
output_file = ''

isValidinput = False
while not isValidinput:
    input_file = input('Input file:  ')
    if file_extension(input_file) in video_input_extentions:
        isValidinput = True
isValidinput = False

isValidinput = False
while not isValidinput:
    output_file = input('Output file:  ')
    if file_extension(output_file) in ['264', 'h264']:
        isValidinput = True

if name == 'nt':
    ffmpeg_path = input('Path to ffmpeg.exe:  ')
    system(rf'{ffmpeg_path} -i {input_file} {output_file}')
elif name == 'posix':
    system(rf'ffmpeg -i {input_file} {output_file}')