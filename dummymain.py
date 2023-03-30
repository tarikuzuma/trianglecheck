import tkinter as gui

def clear():
    entries = [entry_a, entry_b, entry_c]
    for entry in entries:
        entry.delete(0, "end")

root = gui.Tk()
root.geometry("350x350")
root.title("Triangle Checker")

text_a = gui.Label(root, text="Input Side A = ", font=('Helvetica', 15))
text_a.grid(row=1, column=0, padx=5, pady=5)

entry_a = gui.Entry(root, width=30)
entry_a.grid(row=1, column=1, padx=5, pady=5)

text_b = gui.Label(root, text="Input Side B = ", font=('Helvetica', 15))
text_b.grid(row=2, column=0, padx=5, pady=5)

entry_b = gui.Entry(root, width=30)
entry_b.grid(row=2, column=1, padx=5, pady=5)

text_c = gui.Label(root, text="Input Side B = ", font=('Helvetica', 15))
text_c.grid(row=3, column=0, padx=5, pady=5)

entry_c = gui.Entry(root, width=30)
entry_c.grid(row=3, column=1, padx=5, pady=5)

btn_clr = gui.Button(root, text = "Clear", width=5, height=2, command=lambda: clear())
btn_clr.grid(row=4, column=0, padx=5, pady=5)

btn_cal = gui.Button(root, text = "Calculate", width=7, height=2)
btn_cal.grid(row=4, column=1, padx=5, pady=5)

output_label = gui.Label(root, text="Output: ")
output_label.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()
