import formcreation as tk1
from doctest import master

from tt import window

window=tk1.Tk()

'''frame_a=tk1.Frame()
label_a=tk1.Label(master=frame_a,text=" this is frame a",bg="#4682B4")
label_a.pack()
frame_b=tk1.Frame()
label_b=tk1.Label(master=frame_b,text="this s frame b",bg="purple")
label_b.pack()
frame_a.pack()
frame_b.pack()'''
border={
    "flat":tk1.FLAT,
    "sunken":tk1.SUNKEN,
    "rasied":tk1.RAISED,
    "groove":tk1.GROOVE,
    "ridge":tk1.RIDGE
}
for relief_name,relief in border.items():
    frame=tk1.Frame(master=window,relief=relief,borderwidth=5)
    frame.pack(side=tk1.LEFT)
    label=tk1.Label(master=frame,text=relief_name)
    label.pack()
frame1=tk1.Frame(master=window,width=100,height=100,bg="red")
frame1.pack(fill=tk1.X)
frame2=tk1.Frame(master=window,width=100,height=100,bg="yellow")
frame2.pack(fill=tk1.X)
window.mainloop()