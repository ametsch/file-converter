from os import system, name
from sys import argv as args
import json

def file_extension(path: str) -> str:
    return path.strip().split('.')[-1].lower()

video_input_extentions = ['mp4','avi','avs2','drc','vc2','dnxhd','dnxhr','h264','264','hevc','h265','265','m4v','mjpg','mjpeg',
                    'mpg','mpeg','m1v','m2v','yuv','rgb','flv','live_flv','kux','mov','3gp','3g2','mj2','psp','m4b','ism','ismv',
                    'isma','f4v','m4a','wmv']

input_file = ''
output_file = ''

with open('paths.json', 'rt') as f:
    paths = json.load(f)

input_file = args[1]
if file_extension(input_file) in video_input_extentions:
        pass
else:
    exit()
output_file = args[2]
if file_extension(output_file) in ['264', 'h264']:
        pass
else:
    exit()

ffmpeg_path = paths['ffmpeg']
system(rf'{ffmpeg_path} -i {input_file} {output_file}')