import os
import configparser
# pip install opencc-python-reimplemented
from opencc import OpenCC

# 建立 ConfigParser
# config = configparser.ConfigParser()  # 無法處理特殊字元，如: '%'
config = configparser.RawConfigParser()

# 模組翻譯檔的路徑
path = ''

# 設定轉換模式: 簡體中文 -> 繁體中文 (台灣)
cc = OpenCC('s2tw')

# 依序列出該路徑下的檔案
for fname in os.listdir(path):
    fpath = path + '\\' + fname

    # 讀取 cfg 設定檔
    config.read(fpath, encoding='utf-8')

    # 取得所有 sections
    sections = config.sections()

    # 列出 每個 區段下所有 items
    for section in sections:
        for k in config[section]:
            # 將 items 的值轉換成繁體中文
            config[section][k] = cc.convert(config[section][k])
    
    # 寫檔
    modifypath = 'cn2tw/' + fname
    with open(modifypath, 'w', encoding='utf-8') as configfile:
        config.write(configfile)

    # 將所有 sections 刪除
    for section in sections:
        config.remove_section(section)