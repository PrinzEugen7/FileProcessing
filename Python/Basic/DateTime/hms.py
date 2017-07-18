# -*- coding: utf-8 -*- 
import datetime

def main():
    today = datetime.datetime.today()
    print(today)
    print(today.year, "年", today.month,"月",today.day, "日")
    print(today.hour, "時", today.minute, "分", today.second, "秒", today.microsecond, "マイクロ秒")

if __name__ == "__main__":
    main()
