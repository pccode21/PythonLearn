import turtle
def draw_pentagram(size):
    count=1
    while count<=5:
        turtle.forward(size)  #从落笔点向前（也就是默认向右）走
        turtle.right(144)     #顺时针旋转144度
        count+=1
def main():
    turtle.tracer(False)      #不显示画图轨迹
    turtle.begin_fill()
    turtle.penup()            #先提笔
    turtle.back(100)          #在原点沿着X轴后移100像素
    turtle.pendown()          #落笔
    turtle.pencolor('yellow')
    turtle.fillcolor('red')
    size=200
    draw_pentagram(size)
    turtle.end_fill()
    turtle.exitonclick()
if __name__=='__main__':
    main()