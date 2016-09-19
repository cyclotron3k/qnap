# Python implementation of QNAP's encoding function
# Converted from http://eu1.qnap.com/Storage/SDK/get_sid.js
# (it's just Base64 encoding)

from base64 import b64encode

def ezEncode(str):
    return b64encode(str)
