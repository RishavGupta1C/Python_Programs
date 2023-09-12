# Method 1
from datetime import datetime
for _ in range(int(input())):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print (int(abs((t1-t2).total_seconds())))



# Method 2
# from dateutil import parser
# for _ in range(int(input())):
#     d1 = parser.parse(input().strip())
#     d2 = parser.parse(input().strip())
#     print(abs(int((d2-d1).total_seconds())))



# Method 3
# from datetime import datetime as dt
# fmt = '%a %d %b %Y %H:%M:%S %z'
# for i in range(int(input())):
#     print(int(abs((dt.strptime(input(), fmt) 
#         dt.strptime(input(), fmt)).total_seconds())))