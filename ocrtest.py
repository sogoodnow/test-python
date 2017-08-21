from PIL import Image, ImageFilter
import subprocess


# def cleanfile(filepath, newpath):
#     image = Image.open(filepath)
#     image = image.point(lambda x: 0 if x < 143 else 255)
#     image.save(newpath)
#
#     subprocess.call(["tesseract", newpath, "output", "txt"])
#     outputfile = open("d:\output.txt", 'r')
#     outputfile.close()
#
# if __name__ == '__main__':
#     cleanfile(r'd:\test1.png', r'd:\out.png')

subprocess.call(["tesseract", r"d:\test2.png", "d:\out", "-l", "chi_sim"])
