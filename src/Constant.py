def enum(**enums):
    return type('Enum', (), enums)

'''200 OK, 403 Forbidden, 400 Bad Request'''
RETS = enum(OK=200, BAD_REQUEST=400, FORBIDDEN=403)

FIELDS = enum(TYPE="type", VALUE="value", URL="url", RETURN="return") 

MSGTYPE = enum(PTZ="PTZ", VIDEO="VIDEO", AUDIO="AUDIO") 

ACTIONS = enum(OPEN="OPEN", CLOSE="CLOSE")
