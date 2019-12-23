import turtle         #import turtle 是导入turtle包，不能使用未声明的变量.因此，要对每项加上包的前缀
turtle.tracer(False)  #直接画完，不显示过程，只显示结果
turtle.begin_fill()
turtle.circle(100)
turtle.pencolor("green")
turtle.fillcolor("yellow")
turtle.end_fill()
turtle.done()  #解决窗口一闪而过问题
ts = turtle.getscreen()
ts.getcanvas().postscript(file=r"D:\circle.eps") 