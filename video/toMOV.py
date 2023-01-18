from os import system, name
from sys import argv as args
import json

def file_extension(path: str) -> str:
    return path.strip().split('.')[-1].lower()

audio_input_extensions = ['mp3','wav','ogg','flac','aac','tco','rco','mp2','aptxhd','m2a','mpa','sbc',
                    'msbc','thd','aa','m4a','mov','3gp','3g2','mj2','psp','m4b','ism','ismv','isma','f4v','aiff','tun','pcm','wma']

video_input_extentions = ['mp4','avi','avs2','drc','vc2','dnxhd','dnxhr','h264','264','hevc','h265','265','m4v','mjpg','mjpeg',
                    'mpg','mpeg','m1v','m2v','yuv','rgb','flv','live_flv','kux','mov','3gp','3g2','mj2','psp','m4b','ism','ismv',
                    'isma','f4v','m4a','wmv']

input_file = ''
output_file = ''

with open('paths.json', 'rt') as f:
    paths = json.load(f)

input_file = args[1]
if file_extension(input_file) in audio_input_extensions or file_extension(input_file) in video_input_extentions:
        pass
else:
    exit()
output_file = args[2]
if file_extension(output_file) == 'mov':
        pass
else:
    exit()



ffmpeg_path = paths['ffmpeg']
system(rf'{ffmpeg_path} -i {input_file} {output_file}')