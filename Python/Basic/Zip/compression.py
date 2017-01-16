# -*- coding: utf-8 -*-
import zipfile

def main():
	zip = zipfile.ZipFile("abc.zip", "w", zipfile.ZIP_DEFLATED)
	zip.write("a.jpg")
	zip.write("b.png")
	zip.write("c.txt")
	zip.close()

if __name__ == "__main__":
    main()
