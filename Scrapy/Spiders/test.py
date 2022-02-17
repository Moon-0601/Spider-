import os
import re

str="1. 我是 123"
b=re.compile('.\.(.+)')
c=b.findall(str)[0].strip()
print(c)