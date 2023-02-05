
import requests
from datetime import *

epoch = date(1970, 1, 1)
current_date = date.today()
past_date = date.today()-timedelta(days=2)
start_date = int((past_date-epoch).total_seconds())
end_date = str(int((current_date -epoch).total_seconds()))

url=f'https://api.stackexchange.com/2.3/questions?fromdate={start_date}&todate={end_date}&tagged=Python&site=stackoverflow'

result = requests.get(url).json()
result_list = [q['title'] for q in result['items']]
for index, item in enumerate(result_list,1):
    print (index, item)
    print()