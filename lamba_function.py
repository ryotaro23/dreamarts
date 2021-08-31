import json
import logging
import re
import urllib.parse

from typing import List

from src.kanji2number import *
from src.number2kanji import *


logger = logging.getLogger()


def lambda_handler(event, context):

    route = event["path"].split("/")[-2]

    if route == "number2kanji":
        try:
            str_num = event["path"].split("/")[-1]
            num = int(str_num)
            scan_num = scan_number(num)
            numbox = split_numbox(scan_num)

            return {
                'isBase64Encoded': False,
                'statusCode': 200,
                'headers': {},
                'body': "".join(count_kanji(numbox))
            }
        except:
            return {
                'statusCode': 204
            }

    elif route == "kanji2number":
        try:
            import re
            kanji = urllib.parse.unquote(event["path"].split("/")[-1])
            kanji_box = re.split('; |, |兆|億|万|- ', kanji)
            return {
                'isBase64Encoded': False,
                'statusCode': 200,
                'headers': {},
                'body': num_kanji(kanji_box)
            }
        except:
            return {
                'statusCode': 204
            }
