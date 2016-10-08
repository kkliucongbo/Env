# -*- coding: utf-8 -*-
import os,re,subprocess
length_regexp ='Duration\:\s(\d+)\:(\d+)\:([\d\.]+)'#正则取视频时长
re_length = re.compile(length_regexp)
for name in os.listdir():
    file = os.path.splitext(name)
    if file[1] == ".mp4":
        cmd = "ffmpeg -i " + name
        x=subprocess.Popen(cmd,stderr=subprocess.PIPE)
        out=x.stderr.readlines()
        for line in out:
            matches = re_length.findall(str(line))
            if matches:
                print(str(matches))
                for c in matches:
                    print('minutes, Duration:', c[0], c[1], c[2])
                    duration = int(c[0]) * 3600 + int(c[1]) * 60 + float(c[2])
                print(duration)
                for i in range(int(duration / (300)) + 1):
                    _t = ''
                    if duration > 300 * (i + 1):
                        _t = str(300)
                    else:
                        _t = str(duration - 300 * i)
                    cmd_express = "ffmpeg -ss " + str(i * 300) + ' -i "' + name + '" -vcodec copy -acodec copy -t ' + str(
                        (i+1) * 300)+" "+ file[0] + '_' + str(i)+ file[1]
#                    cmd_express = "ffmpeg -ss " + str(i * 300) + ' -i "' + name + '" -c:v libx265 -preset ultrafast -crf 28 -acodec copy -t ' + str((i+1) * 300)+" "+ file[0] + '_' + str(i)+ file[1]
                    print(cmd_express)
                    subprocess.Popen(cmd_express,stderr=subprocess.PIPE)