import python_bitbankcc
import json
import os

BITBANK_API_KEY = os.environ['BITBANK_API_KEY']
BITBANK_API_SECRET = os.environ['BITBANK_API_SECRET']

cc_pub = python_bitbankcc.public()
cc_prv = python_bitbankcc.private(BITBANK_API_KEY, BITBANK_API_SECRET)
