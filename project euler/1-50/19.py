from datetime import datetime
import pandas as pd

ans = 0
start = datetime(1901,1,1)
end = datetime(2000,12,31)
for date in pd.date_range(start,end):
    if date.day == 1 and date.weekday() == 6:
        print (date)
        ans += 1

print (ans)
