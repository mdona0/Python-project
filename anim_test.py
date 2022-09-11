import glob
from PIL import Image
 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
#フォルダ名
folderName = "3danime"
     
#ファイル形式を指定
picList = glob.glob(folderName + "\*.png")

fig = plt.figure(figsize=(16, 9), dpi=120)
     
#アニメーション作成
ims = []     
for i in range(len(picList):
    tmp = Image.open(picList[i])
    ims.append([plt.imshow(tmp)])     
     

ani = animation.ArtistAnimation(fig, ims, interval=300, repeat_delay=1000)
 
#保存ファイル名
ani.save("3dtest.gif")