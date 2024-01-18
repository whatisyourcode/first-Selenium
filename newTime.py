import time
from datetime import datetime
import urllib.request
import newUi


class user:
    hour =   10
    minute =  25
    second =  00 
    run_time = datetime.now().replace(hour=hour,minute=minute,second=second)
    unix_RunTime = int(time.mktime(run_time.timetuple()))



class gTime:   
    def get_LocalTime(): ## 로컬 unix time을 return 하는 함수
        local_unix_Time = time.time()
        return local_unix_Time

    def get_ServerTime(): ## 서버 시간을 unix time 으로 바꿔서 return 하는 함수
        url = 'https://weverse.io'
        rfc_time = urllib.request.urlopen(url).headers['Date'] ## Tue, 21 Feb 2023 17:06:31 GMT
        rfc_format = datetime.strptime(rfc_time, '%a, %d %b %Y %H:%M:%S %Z') ## 2023-02-21 17:06:31
        unix_Time = int(time.mktime(rfc_format.timetuple()))
        return unix_Time
    


class values:
        diff_Time = gTime.get_LocalTime() - gTime.get_ServerTime()
        result_Time = user.unix_RunTime - diff_Time

        def print_ServerTime(): ## 서버 시간 출력하는 함수
            url = 'https://weverse.io'
            rfc_time = urllib.request.urlopen(url).headers['Date'] ## Tue, 21 Feb 2023 17:06:31 GMT
            rfc_format = datetime.strptime(rfc_time, '%a, %d %b %Y %H:%M:%S %Z') ## 2023-02-21 17:06:31
            unix_PlusTime = int(time.mktime(rfc_format.timetuple()) + values.diff_Time)
            dt = datetime.fromtimestamp(unix_PlusTime)
            print("시간 : ",dt)

        def request_Server(result_time,diff_time): ## 서버 시간 측정 알고리즘
            while True:
                if result_time < (time.time()-diff_time):
                   values.print_ServerTime()
                   break
                else:
                   time.sleep(1)
                   print(datetime.now())


def main():
      global values
      values.request_Server(values.result_Time,values.diff_Time)
    

main()