from os import system, name
from sys import argv as args
import json

def file_extension(path: str) -> str:
    return path.strip().split('.')[-1].lower()

audio_input_extensions = ['mp3','wav','ogg','flac','aac','tco','rco','mp2','aptxhd','m2a','mpa','sbc',
                    'msbc','thd','aa','m4a','mov','3gp','3g2','mj2','psp','m4b','ism','ismv','isma','f4v','aiff','tun','pcm','wma']

input_file = ''
output_file = ''

with open('paths.json', 'rt') as f:
    paths = json.load(f)

input_file = args[1]
if file_extension(input_file) in audio_input_extensions:
        pass
else:
    exit()
output_file = args[2]
if file_extension(output_file) == 'ogg':
        pass
else:
    exit()

ffmpeg_path = paths['ffmpeg']
system(rf'{ffmpeg_path} -i {input_file} {output_file}')