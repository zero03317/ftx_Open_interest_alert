import requests
from time import sleep
import sys

product_name='tomo-perp'

def ftx_product(product_name):
    r=requests.get('https://ftx.com/api/futures/'+product_name+'/stats')
    return r.json()

def warning_std(paramter):
        a=ftx_product(paramter[1])
        before_fundingrate=a['result']['nextFundingRate']
        before_openinterest=round(float(a['result']['openInterest']),3)
        print (before_openinterest)
        sleep(paramter[2])
        b=ftx_product(paramter[1])
        after_fundingrate = b['result']['nextFundingRate']
        after_openinterest = round(float(b['result']['openInterest']),3)
        print (after_openinterest)
        total_openinterest=round(((after_openinterest-before_openinterest)/after_openinterest)*100,4)
        print (total_openinterest)
        if total_openinterest > paramter[0]:
            if total_openinterest < 0:
                return "{} 持倉量減少了{} 百分比 ， 目前資金費率為{}".format(product_name,total_openinterest,after_fundingrate)
            elif total_openinterest >0:
                return "{} 持倉量增加了{} 百分比 ， 目前資金費率為{}".format(product_name, total_openinterest, after_fundingrate)
        elif total_openinterest < paramter[0]:
            return 0

def get_paramter():
    warning_std_openInterest=sys.argv[0]
    product_name=sys.argv[1]
    sleep_time=sys.argv[2]
    cmd=[warning_std_openInterest,product_name,sleep_time]
    return cmd

def main_funtion():
    a=get_paramter()
    warning_std(a)
if __name__ == '__main__':
    main()