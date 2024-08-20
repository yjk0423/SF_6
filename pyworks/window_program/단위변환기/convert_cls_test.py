# 클래스 샘플 - 객체를 생성해서 버튼 이벤트 구현

from tkinter import *

class App:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack() # 한줄을 꽉채움(가운데 정렬)

        Label(frame, text="KB").grid(row=0, column=0)
        Button(frame,text="변환", command=self.convert).grid(row=1, column=0)

    def convert(self):
        print("test")

root = Tk()
root.title("단위 변환기")
root.geometry('300x150+200+200')

app = App(root)


root.mainloop()
