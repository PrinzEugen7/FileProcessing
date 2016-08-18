# -*- coding: utf-8 -*-

def main():
    # ファイルを開く(読み込みモード)
    f = open("data.txt","w")
    text = "test data"
    f.write(text)
    # ファイルを閉じる
    f.close()

if __name__ == "__main__":
    main()
