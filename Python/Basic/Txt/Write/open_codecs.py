# -*- coding: utf-8 -*-
import codecs

def main():
    # ファイルを開く(書き込みモード)
    f = codecs.open("data.txt","w","utf-8")
    text = "test data"
    f.write(text)
    # ファイルを閉じる
    f.close()

if __name__ == "__main__":
    main()
