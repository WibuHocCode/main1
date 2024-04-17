from tkinter import *
from tkinter import messagebox
import random

selections_yes = ["Yes.",
                  "Of course.",
                  "Sure.",
                  "Why not?",
                  "Ok.",
                  "Okey.",
                  "Yes, of course.",
                  "Certainly."]
selections_no = [
    "No way.",
    "Not at all.",
    "Certainly not.",
    "Absolutely not.",
    "By no means.",
    "Negative.",
    "Nope.",
    "I'm afraid not.",
    "No chance.",
    "Nuh-uh."
]

Questions = [
    "Would you like to be my girlfriend?",
    "Could you be my girlfriend?",
    "Are you interested in being my girlfriend?",
    "Would you consider being my girlfriend?",
    "Are you open to being my girlfriend?",
    "Do you want to be my girlfriend?",
    "Will you go out with me?",
    "Would you be my partner?"
]

def yes(): # Hàm dùng khi người trả lời đồng ý nè
    win.destroy() # hủy cửa số hỏi
    messagebox.showinfo("YOU AGREED", "I LOVE YOU <3 !!!")#hiển thị cửa số chốt nè
    
def no(): # Người ta mà từ chối là nó hiện hoài nè
    win.destroy() # hủy cửa sổ cũ
    main()# tạo lại cửa số đó
    
def main(): # cửa số ban đầu nè
    global win # mình tạo biến global (toàn cục) để các hàm khác có thể hủy của sổ win
    win = Tk()
    win.geometry("400x400") 
    win.title("YES / YES QUESTION")
    ques = Label(text = Questions[random.randint(0, len(Questions)-1)] + "\n<3 <3 <3", font=25)
    # Mình sẽ ramdom một câu hỏi từ list câu hỏi để hiển thị
    ques.grid(row = 0, column=0, rowspan=1, columnspan=2, sticky="nsew")
    # Dòng này để hiện câu hỏi lên cửa sổ nè
    # rowspan và columnspan là đối tượng này sẽ chiếm bao nhiu hàng và bao nhiu cột
    # ở đây nó chiếm 2 cột và 1 dòng nè, sticky là để khi mình chỉnh kích thước cửa số đối tượng đổi kích thước theo nè
    
    ans1 = Button(text = selections_yes[random.randint(0, len(selections_yes)-1)], command=yes, font=25, border=5)
    ans1.grid(row=1, column=0, sticky="nsew")
    ans2 = Button(text = selections_no[random.randint(0, len(selections_no)-1)], command=no, font=25, border=5)
    ans2.grid(row=1, column=1, sticky="nsew")
    # phần code 2 nút này mọi người hong hiểu có thể vô kênh của tui coi lại nha
    # phần 2 nút này chiếm 1 cột tui nói ở trên thì do mặc định tham số đó là 1 nên hong cần viết lại nha
    
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    # 4 dòng này là mình để set kích thước cho cột và hàng bằng nhau (weight = 1)
    win.mainloop()
    
main()