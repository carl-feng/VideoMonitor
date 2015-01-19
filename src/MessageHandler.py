import json
from ptz import PTZ
from Constant import FIELDS
from Constant import RETS
from Constant import MSGTYPE
from Video import Video


class MessageHandler(object):
    
    def __init__(self):
        self.ptz = PTZ()
    
    def process_msg(self, msg):
        ret = {}
        try:
            message = json.loads(msg)
            msg_type = message[FIELDS.TYPE]
            msg_value = message[FIELDS.VALUE]
        except Exception:
            print "Receive invalid event -> %s" % msg
            ret[FIELDS.RETURN] = RETS.BAD_REQUEST
            return ret
        
        print "Receive valid event -> %s" % msg
        #print "Incoming event <msg_type=%s, msg_value=%s>"%(msg_type, msg_value)

        if msg_type == None or msg_value == None:
            ret[FIELDS.RETURN] = RETS.BAD_REQUEST
            return ret
        
        if msg_type.upper() == MSGTYPE.PTZ:
            self.handle_ptz_event(ret, msg_value)
        
        if msg_type.upper() == MSGTYPE.VIDEO:
            self.handle_video_event(ret, msg_value)

        ret[FIELDS.TYPE] = msg_type
        return ret
    
    def handle_ptz_event(self, ret, action):
        self.ptz.DoAction(action)
        ret[FIELDS.RETURN] = RETS.OK
    
    def handle_video_event(self, ret, action):
        video = Video()
        video.handle_video_event(ret, action)