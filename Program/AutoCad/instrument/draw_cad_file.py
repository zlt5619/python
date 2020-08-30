from pyautocad import Autocad,APoint
from .signal import signal

d={'PO010': {0: ['PO010', '=', 'MT001', '&&', 'MT005', '&&', '信号1'], 1: ['信号1', '=', 'PO001', '&&', '信号2'], 2: ['信号2', '=', 'MT003', '||', 'MT004']}, 'PO016': {0: ['PO016', '=', 'MT001', '&&', '信号1', '||', '信号2'], 1: ['信号1', '=', 'MT002', '&&', 'MT003', '||', 'MT004'], 2: ['信号2', '=', 'MT005', '||', 'MT004']}}

def draw_cad(data):

    #打印相关数据
    print(data)
    output_signal=data.keys()
    print(output_signal)

draw_cad(d)