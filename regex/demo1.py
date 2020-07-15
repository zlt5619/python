import re
"""
替换相关文件名
"""
a="【6v电影www.6vdy.com】八爪女.720p.国英双语.BD中英双字.mkv"

num = re.sub(r'【.*】', "", a)
print(num)