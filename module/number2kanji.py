import json
import logging
import re
import urllib.parse

from typing import List


def scan_number(num):
    if type(num) != int:
        return error
    elif num < 0 or len(str(num)) > 16:
        return error
    else:
        numbox = [str(num)[i] for i in range(len(str(num)))]
        return numbox


def split_numbox(numbox: List[str]):
    que_box = []
    tmp_que = []
    numbox.reverse()
    for n in numbox:
        tmp_que.insert(0, n)
        if len(tmp_que) == 4:
            que_box.insert(0, tmp_que)
            tmp_que = []
        else:
            pass
    if len(tmp_que) >= 1:
        que_box.insert(0, tmp_que)
    return que_box


def change_rule_number(que: List[str], alab_num_dic: dict):
    _str = ""

    while True:
        if len(que) >= 1:
            if que[0] == "0":
                pass
            elif len(que) == 4:
                _str += alab_num_dic[int(que[0])] + "千"
            elif len(que) == 3:
                _str += alab_num_dic[int(que[0])] + "百"
            elif len(que) == 2:
                _str += alab_num_dic[int(que[0])] + "拾"
            elif len(que) == 1:
                _str += alab_num_dic[int(que[0])]

            que.pop(0)
        else:
            break
    return _str


def count_kanji(que_box: List[list]):

    alab_num_dic = {
        0: "零",
        1: "壱",
        2: "弐",
        3: "参",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九"
    }

    result_box = []

    digit = len(que_box)

    for i in range(digit):
        if digit - i - 1 == 3:
            result_box.append(change_rule_number(
                que_box[i], alab_num_dic) + "兆")
        elif digit - i - 1 == 2:
            result_box.append(change_rule_number(
                que_box[i], alab_num_dic) + "億")
        elif digit - i - 1 == 1:
            result_box.append(change_rule_number(
                que_box[i], alab_num_dic) + "万")
        elif digit - i - 1 == 0:
            result_box.append(change_rule_number(que_box[i], alab_num_dic))

    return result_box
