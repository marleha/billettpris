from ezgraphics import GraphicsWindow
win = GraphicsWindow(400,200)



canvas= win.canvas()




canvas.drawOval(100,100,200,200)
canvas.setColor("red")

win.wait()