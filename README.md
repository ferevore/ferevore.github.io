

# Alexandra Ryyberg

<html>
<head>
<style>
body {
  background-color: lightpink;
}

h1 {
  color: red;
  text-align: left;
}

p {
  font-family: Times New Roman;
  font-size: 20px;
}
</style>
</head>
<body>

<h1>My First page</h1>
<p>This is my first page. Jehuuu! </p>

</body>
</html>

from tkinter import *

raam = Tk()
raam.title("Saue lipp")
tahvel = Canvas(raam, width=880, height=560)

tahvel.create_rectangle(0, 0, 880, 560, fill="green", outline="green")
tahvel.create_rectangle(0, 0, 880, 290, fill='yellow', outline='yellow')

i = 0
x = 80
while i < 15: # sobib ka for i in range(0, 15):
    if (i % 2) == 0:
        tahvel.create_rectangle(-80 + x, 220, 0 + x, 290, fill="green", outline="green")
        i += 1
        x += 80
    else:
        tahvel.create_rectangle(-80 + x, 220, 0 + x, 290, outline="yellow")
        i += 1
        x += 80
tahvel.pack()
raam.mainloop()'''
