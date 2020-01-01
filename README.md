# Leigod Reminder

 雷神加速器暂停时长提醒

 ## 创作背景

 > 2019年最后一天，和小伙伴又重新捡起来了吃鸡玩了几把。陡然想起，之前使用的UU加速器过期了。听小伙伴推荐，使用了雷神加速器，英文名Leigod，也是够雷的。雷神加速器不同于UU加速器的包月制，是购买时长使用，并且支持无限次暂停时长。然而，美中不足的是，加速器在退出的时候并不会主动暂停时长。我原来在借小伙伴的加速器的时候，也出现过忘记暂停，跑了几百个小时的事情...于是乎，遂想起，用python和powershell写一个当雷神加速器退出时，自动调用Windows10通知，提示关闭雷神加速器的命令行程序。

<div align="center">![加速器界面](https://raw.githubusercontent.com/Kevinjyp/Leigod-Reminder/master/pic/interface.PNG "加速器界面")  加速器界面 </div>

<div align="center">![通知效果展示](https://raw.githubusercontent.com/Kevinjyp/Leigod-Reminder/master/pic/notification.PNG "通知效果展示") 通知效果展示 </div>

## 使用方法
在Leigod-Reminder文件夹，打开cmd或者powershell。控制台输入```python a.py```，即可。

程序在控制台有三种输出，如下所示，每一秒钟刷新一次。

```Shell
#未检测到雷神加速器
Leigod hasn't been Using

#检测到雷神加速器
Leigod is been Using
Leigod.exe                   23732 Console                    1    175,064 K

#检测到雷神加速器已经关闭，发出提示，程序结束
Leigod is Closed
```

## 一点Bug
> 不知道为什么，在点击关闭雷神加速器之后，在约15S之后，Leigod这个进程才会被彻底结束。可能是软件厂商为了让软件显得相应很快，就先让界面消失了，假装结束。

检测会延后15秒钟左右。

## 可以继续研究地方
- Powershell脚本：可以做一个通知上点击的来确认已经暂停的控件，如果没有点击则过一小会再发出一次提醒。
- 进程检测：通过检测Leigod进程的逻辑其实不是很完备，应该检测需要加速的游戏进程。在游戏结束之后，发出提示，暂停加速器时间。
    >要不，得在关闭加速器15s后，才得到提醒，还得再打开加速器，去暂停，浪费不少时间。
