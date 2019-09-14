# coding=utf-8
from os.path import realpath, dirname
import json


def get_config(name):
    '''
    读取json文件的方法
    '''
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())