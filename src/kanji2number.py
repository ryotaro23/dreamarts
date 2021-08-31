import json
import logging
import re
import urllib.parse

from typing import List


def change_rule_kanji(kanji: str):
    numbox = ["0"]*4

    num_alab_dic = {
        "零": "0",
        "壱": "1",
        "弐": "2",
        "参": "3",
        "四": "4",
        "五": "5",
        "六": "6",
        "七": "7",
        "八": "8",
        "拾": "9"
    }

    if "千" in kanji:
        numbox[0] = num_alab_dic[kanji[kanji.find("千") - 1]]

    if "百" in kanji:
        numbox[1] = num_alab_dic[kanji[kanji.find("百") - 1]]

    if "拾" in kanji:
        numbox[2] = num_alab_dic[kanji[kanji.find("拾") - 1]]

    if not kanji[-1] in ["千", "百", "拾"]:
        numbox[3] = num_alab_dic[kanji[-1]]

    return "".join(numbox)


def num_kanji(kanji_box: List[str]):
    _result = ""
    result = ""
    flag = True
    for k in kanji_box:
        _result += change_rule_kanji(k)

    for i in range(len(_result)):
        if _result[i] == "0" and flag:
            pass
        elif _result[i] != "0" and flag:
            result += _result[i]
            flag = False
        else:
            result += _result[i]
    return result
