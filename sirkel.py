from ezgraphics import GraphicsWindow
win = GraphicsWindow(400,200)



canvas= win.canvas()



canvas.setColor("red")
canvas.drawOval(70,70,80,80)
win.wait()