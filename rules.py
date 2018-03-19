# encoding=utf-8

import re

def execute(s):
    return [
     check_year_stayed(s),
     is_local_uni(s),
     is_poly(s),
     is_malaysian_chn(s),
     is_msc(s),
     is_phd(s),
     was_wp(s),
     salary(s),
     is_couple(s),
     with_child(s),
     is_dpr(s),
     check_result(s)
    ]

def check_result(s):
    if s.find('通过') return 1
    return 0

def check_year_stayed(s):
    regex = r"\w([\d\w])来新\s+"
    matches = re.finditer(regex, s)
    if matches.group():
        return match.group(0)
    return 0
    
def is_local_uni(s):
    keys = ['nus本', 'NUS本', 'NTU本', 'ntu本', 'sm', 'SM', '本地大学', 'SMU', "公立本科"]
    for key in keys:
        if s.find(k):
            return 1
    return 0

def is_poly(s):
    keys = ['poly', '本地大专']
    for key in keys:
        if s.find(k):
            return 1
    return 0

def is_malaysian_chn(s):
    keys = ["马来西亚", "malaysian"]
    for key in keys:
        if s.find(k):
            return 1
    return 0

def is_msc(s):
    keys = ["NTU msc", "NUS msc", "NTU硕士", "NUS硕士", "NUS master", "NTU master"]
    for key in keys:
        if s.find(k):
            return 1
    return 0

def is_phd(s):
    keys = ['NTU PHD', 'NUS PHD', 'NUS博士', 'NTU博士', 'nus博士', 'phd在读', '本地PHD']
    for key in keys:
        if s.find(k):
            return 1
    return 0

def was_wp(s):
    keys = ['wp']
    for key in keys:
        if s.find(k):
            return 1
    return 0

def salary(s):
    regex1 = r"\w(\d{4})"
    regex2 = r"\s+S$\dk\s+"
    matches1 = re.finditer(regex1, s)
    matches2 = re.finditer(regex2, s)

    if matches1 or matches2:
        return matches1.group(0) or matches2.group(0)
    return 0

def is_couple(s):
    keys = ['家庭', '夫妻', '带老婆']
    for key in keys:
        if s.find(k):
            return 1
    return 0

def with_child(s):
    keys = ['家庭', '儿子', '女儿']
    for key in keys:
        if s.find(k):
            return 1
    return 0

def is_dpr(s):
    keys = ['dpr', 'sponsor']
    for key in keys:
        if s.find(k):
            return 1
    return 0
