#-*-coding:utf-8-*-
from PIL import Image

codeLib =list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,\"^`'. ")

def get_char(r,g,b,alpha=256):
    if alpha==0:
        return ""
    length=len(codeLib)
    gray=int(0.2126*r+0.7152*g+0.0722*b)
    unit=(alpha+1.0)/length
    return codeLib[int(gray/unit)]
def main(file_name="text.jpg",width=100,height=80,out_file_name="out_file"):
    text=""
    im = Image.open(file_name)
    im=im.resize((width,height),Image.NEAREST)
    for i in range(height):
        for j in range(width):
            content = im.getpixel((j,i))
            text=text+get_char(*content)
        text=text+"\n"
    print(text)
    write_file(out_file_name,text)

def write_file(out_file_name,text):
    with open(out_file_name,"w") as f:
           f.write(text)
if __name__=='__main__':
    main(file_name="d:/xi.jpg",out_file_name='D:/123.txt')



