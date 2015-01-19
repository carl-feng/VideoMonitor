import subprocess, re
import time
from Constant import ACTIONS
from Constant import RETS
from Constant import FIELDS

class Video(object):
    
    def __init__(self):
        pass
    
    def handle_video_event(self, ret, action):
        if ACTIONS.OPEN == action.upper():
            self.kill_ngrok()
            self.start_ngrok()
            time.sleep(1)
            try:
                urlMapFile = open("/tmp/url.map")
                line = urlMapFile.readline()
                bExist = False
                while line:
                    if line.startswith("tcp"):
                        line.replace("tcp", "rtsp")
                        line = line.rstrip()
                        line += "/camera.264"
                        ret[FIELDS.URL] = line
                        bExist = True
                        break;
                    line = urlMapFile.readline()
                urlMapFile.close()
                
                if bExist:
                    ret[FIELDS.RETURN] = RETS.OK
                else:
                    ret[FIELDS.RETURN] = RETS.FORBIDDEN
                    self.kill_ngrok()
            except Exception:
                ret[FIELDS.RETURN] = RETS.FORBIDDEN
                return
            
                
        elif ACTIONS.CLOSE == action.upper():
            self.kill_ngrok()
            ret[FIELDS.RETURN] = RETS.OK
        
    def kill_ngrok(self):
        if self.check_process("ngrok"):
            subprocess.call(r"killall ngrok", shell=True)
    
    def check_process(self, process):
        bProcessExist = False
        s = subprocess.Popen(["ps", "ax"], stdout = subprocess.PIPE)
        for x in s.stdout:
            if re.search(process, x):
                bProcessExist = True
        return bProcessExist
    
    def start_ngrok(self):
        subprocess.call(r"ngrok -config=/home/pi/.ngrok -log=stdout -proto tcp 8554  > /dev/zero &", shell=True)
