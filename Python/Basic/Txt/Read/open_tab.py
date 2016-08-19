# -*- coding: utf-8 -*-
def main():
    data = []
    # ファイルを開く(書き込みモード)
    for line in open("data.txt", "r"):
        data += line[:-1].split("\t")

    # 表示
    print data

if __name__ == "__main__":
    main()
