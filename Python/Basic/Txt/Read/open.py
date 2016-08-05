# -*- coding: utf-8 -*-

def main():
    # ファイルを開く(読み込みモード)
    f = open("data.txt","r")
    # 読み込んだデータを表示
    for line in f:
        print(line) # 1行ずつ表示
    # ファイルを閉じる
    f.close()

if __name__ == "__main__":
    main()
