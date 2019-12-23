import imageio
def create_gif(image_list,gif_name,durations):
    frames=[]
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name,frames,'GIF',duration=durations)
    return
def main():
    image_list=['/eclipse-workspace/pictures/horse.png','/eclipse-workspace/pictures/horse_wordcloud.png','/eclipse-workspace/pictures/leave.png','/eclipse-workspace/pictures/leave_wordcloud.png','/eclipse-workspace/pictures/python.png','/eclipse-workspace/pictures/python_wordcloud.png']
    gif_name='/eclipse-workspace/pictures/new.gif'
    duration=1
    create_gif(image_list, gif_name,duration)
    print('完成')
if __name__=='__main__':
    main()    