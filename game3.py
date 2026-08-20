import tkinter as tk
import random

choices = ["가위", "바위", "보"]
icons = {"가위": "✌️", "바위": "✊", "보": "🖐️"}

def play(user_choice):
    com_choice = random.choice(choices)
    
    label_user.config(text=f"나: {icons[user_choice]} {user_choice}")
    label_com.config(text=f"컴퓨터: {icons[com_choice]} {com_choice}")
    
    if user_choice == com_choice:
        result_text = "무승부! 다시 해보세요."
        result_color = "#f39c12"
    elif (user_choice == "가위" and com_choice == "보") or \
         (user_choice == "바위" and com_choice == "가위") or \
         (user_choice == "보" and com_choice == "바위"):
        result_text = "🎉 이겼습니다! 🎉"
        result_color = "#27ae60"
    else:
        result_text = "😢 졌습니다... 😢"
        result_color = "#e74c3c"
        
    label_result.config(text=result_text, fg=result_color)

root = tk.Tk()
root.title("가위바위보 게임")
root.geometry("380x360")
root.resizable(False, False)

tk.Label(root, text="가위, 바위, 보 중 하나를 선택하세요!", font=("Arial", 13, "bold"), pady=15).pack()

frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="✌️ 가위", font=("Arial", 11), width=8, height=2, command=lambda: play("가위")).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="✊ 바위", font=("Arial", 11), width=8, height=2, command=lambda: play("바위")).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="🖐️ 보", font=("Arial", 11), width=8, height=2, command=lambda: play("보")).grid(row=0, column=2, padx=5)

label_user = tk.Label(root, text="나: ❓", font=("Arial", 12), pady=5)
label_user.pack()

label_com = tk.Label(root, text="컴퓨터: ❓", font=("Arial", 12), pady=5)
label_com.pack()

label_result = tk.Label(root, text="버튼을 눌러 대결을 시작하세요", font=("Arial", 15, "bold"), pady=20)
label_result.pack()

root.mainloop()