import tkinter as tk
pyinstaller --onefile --windowed app.py
root = tk.Tk()
root.title("월급계산기")
root.geometry("350x400+780+280")
root.configure(bg="#EFFFF5")
label = tk.Label(root, text="이번달 내 월급은?", font=("리디바탕", 16), bg="#EFFFF5")
label.pack(pady=10)
count = 0

frame = tk.Frame(root, bg="#EFFFF5")
frame.pack()
buttons = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    [".5", "0", "#"]
]

def on_key_press(event):
    current_text = entry.get()
    key = event.char  # 입력된 문자 가져오기
    entry.delete(len(current_text), tk.END)  # 마지막 글자 삭제
    if key in button_dict:  # 해당 키가 버튼과 매핑되어 있으면
        button_dict[key].invoke()
    elif key == ".":
        button_dict[".5"].invoke()
def on_click(value):
    entry.insert(tk.END, value)
def plus(event):    
    global count
    count += float(entry.get())
    label.config(text=str(int(count * 10030 * 0.967)))
    entry.delete(0, 15)    
def remove():
    global count
    count = 0
    label.config(text=str(int(count * 10030 * 0.967)))
def delete(event):
    entry.delete(len(entry.get()) - 1, tk.END)
button_dict = {}
for row in range(4):
    for col in range(3):
        btn_text = buttons[row][col]
        button = tk.Button(frame, text=btn_text, font=("리디바탕", 16), width=2, height=1, command=lambda v=btn_text: on_click(v), bg="#FFFFFF")
        button.grid(row=row+1, column=col, padx=2, pady=1)
        button_dict[btn_text] = button


entry = tk.Entry(root, width=10)
entry.pack(pady=10)
entry.bind("<Button-1>", lambda e: "break")
root.bind("<Return>", plus)
root.bind("<space>", plus)
root.bind("<KeyPress>", on_key_press)
root.bind("<BackSpace>", delete)

initbutton = tk.Button(root, text="초기화", width=4, height=1, command=lambda v="초기화": remove())
initbutton.pack(pady=10)
root.mainloop()