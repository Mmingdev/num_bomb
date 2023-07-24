# coding:UTF-8 #
"""
@filename:main.py
@autor:stormcar
@time:2023-07-19
"""
# 数字炸弹游戏
import random, os, time, sys

#获取输入函数
def shuru(name):
    while True:
        try:
            g = int(input("{}：".format(name)))
            return g
        except ValueError as err:
            print("输入错误！")
            continue

#获取对比结果函数
def panduan(gnum, bomb, bomb_min, bomb_max, warning):
    if gnum == bomb:
        return 0
    elif gnum <= bomb_min or gnum >= bomb_max:
        if warning < 1:
            return 3
        else:
            return 4
    elif gnum < bomb:
        return 1
    elif gnum > bomb:
        return 2

#单人游戏函数
def singleplayer(bomb_min,bomb_max):
    #初始化
    os.system("cls")  # windows清屏
    # bomb_min, bomb_max = 10, 100
    bomb = random.randint(bomb_min+1, bomb_max-1)
    gnum,n,re = 0, 1,0
    warning = 0

    print("\n----数字炸弹游戏开始----")
    while True:
        print("\nRound-{}\n(请输入一个{}到{}的数字)".format(n, bomb_min, bomb_max))
        while True:
            gnum = shuru("player")
            re=panduan(gnum, bomb, bomb_min, bomb_max, warning)
            match re:
                case 0:
                    print("----踩到雷啦！游戏结束~---\n----(Bomb is {}，第{}回合玩家踩雷)----\n".format(bomb, n))
                    return
                case 1:
                    bomb_min = gnum
                    break
                case 2:
                    bomb_max = gnum
                    break
                case 3:
                    warning += 1
                    print("***超出范围警告一次,注：若再次犯规，炸弹将直接爆炸！***")
                case 4:
                    print("----两次超出范围，雷爆啦！游戏结束~----\n----(第{}回合玩家两次犯规自爆)----\n".format(n))
                    return
        n += 1

#双人游戏函数
def twoplayer(bomb_min,bomb_max):
    # 初始化
    os.system("cls")  # windows清屏
    # bomb_min, bomb_max = 10, 100
    bomb = random.randint(bomb_min + 1, bomb_max - 1)
    gnum1,gnum2, re1,re2, n = 0,0, 0,0,1
    warning_p1,warning_p2 = 0,0

    print("\n----数字炸弹游戏开始----")
    while True:
        print("\nRound-{}\n(请输入一个{}到{}的数字)".format(n, bomb_min, bomb_max))
        #player1
        while True:
            gnum1 = shuru("player1")
            re1 = panduan(gnum1, bomb, bomb_min, bomb_max, warning_p1)
            match re1:
                case 3:
                    warning_p1 += 1
                    print("***超出范围警告player1一次,注：若再次犯规，炸弹将直接爆炸！***")
                    continue
                case 4:
                    print("----两次超出范围，雷爆啦！player2获胜，游戏结束~----\n----(第{}回合player1两次犯规自爆)----\n".format(n))
                    return
                case _:
                    break

        #player2
        while True:
            gnum2 = shuru("player2")
            if gnum2==gnum1:
                print("与player1重复，请重新输入")
                continue
            re2 = panduan(gnum2, bomb, bomb_min, bomb_max, warning_p2)
            match re2:
                case 3:
                    warning_p2 += 1
                    print("***超出范围警告player2一次,注：若再次犯规，炸弹将直接爆炸！***")
                    continue
                case 4:
                    print("----两次超出范围，雷爆啦！player1获胜，游戏结束~----\n----(第{}回合player2犯规自爆)----\n".format(n))
                    return
                case _:
                    break

        if re1==0:
            print("----player1踩到雷啦！player2获胜，游戏结束~---\n----(Bomb is {}，第{}回合player1踩雷)----\n".format(bomb, n))
            return
        elif re2==0:
            print("----player2踩到雷啦！player1获胜，游戏结束~---\n----(Bomb is {}，第{}回合player2踩雷)----\n".format(bomb,n))
            return
        else:
            list=[gnum1,gnum2,bomb,bomb_min,bomb_max]
            list.sort()
            new=list.index(bomb)
            bomb_min=list[new-1]
            bomb_max=list[new+1]
        n += 1

#与bot对战函数
def playewithbot(bomb_min,bomb_max):
    # 初始化
    os.system("cls")  # windows清屏
    # bomb_min, bomb_max = 10, 100
    bomb = random.randint(bomb_min + 1, bomb_max - 1)
    gnum,gnumbot, re,rebot, n = 0,0, 0,0,1
    warning = 0

    print("\n----数字炸弹游戏开始----")
    while True:
        print("Round-{}\n(请输入一个{}到{}的数字)".format(n, bomb_min, bomb_max))
        #player
        while True:
            gnum = shuru("player")
            re = panduan(gnum, bomb, bomb_min, bomb_max, warning)
            match re:
                case 3:
                    warning += 1
                    print("***超出范围警告一次,注：若再次犯规，炸弹将直接爆炸！***")
                    continue
                case 4:
                    print("----两次超出范围，雷爆啦！bot获胜，游戏结束~----\n----(第{}回合player犯规自爆)----\n".format(n))
                    return
                case _:
                    break
        #bot
        list_fanwei =list(range(bomb_min, bomb_max))
        list_fanwei.remove(gnum)
        gnumbot = random.choice(list_fanwei)
        print("Bot：到我啦：", end=" ")
        sys.stdout.flush()
        time.sleep(random.uniform(1, 2))
        print(gnumbot, "\n")
        rebot = panduan(gnumbot, bomb, bomb_min, bomb_max, "0")

        if re==0:
            print("----你踩到雷啦！bot获胜，游戏结束~---\n----(Bomb is {}，第{}回合玩家踩雷)----\n".format(bomb, n))
            return
        elif rebot==0:
            print("----bot踩到雷啦！玩家胜，游戏结束~---\n----(Bomb is {}，第{}回合bot踩雷)----\n".format(bomb,n))
            return
        else:
            list2=[gnum,gnumbot,bomb,bomb_min,bomb_max]
            list2.sort()
            new=list2.index(bomb)
            bomb_min=list2[new-1]
            bomb_max=list2[new+1]
        n += 1

#主流程
rule="""
    规则
        1.系统会生成一个随机的炸弹数字，当有人说到此数字将触发炸弹爆炸，游戏结束，另一方获胜。
        2.说出的数字超出当前提示的范围(不包含头尾)时警告一次，再次犯规将直接触发炸弹爆炸，游戏结束，另一方获胜。
        3.双人模式和bot对战模式，将轮流说数字，其中bot会自动说数字。
"""
print("****欢迎来到数字炸弹游戏****",rule,"****祝你游戏愉快****\n")
bomb_min, bomb_max = 10, 100
while True:
    # 模式选择
    gamemode = input("请选择游戏模式（1-单人，2-双人，3-与Bot对战，4-看规则，5-设置炸弹范围，Q/q-退出游戏）：")
    match gamemode:
        case "1":
            singleplayer(bomb_min,bomb_max)
        case "2":
            twoplayer(bomb_min,bomb_max)
        case "3":
            playewithbot(bomb_min,bomb_max)
        case "4":
            print(rule)
        case "5":
            bomb_min =shuru("设置下限（不包含）")
            bomb_max=shuru("设置上限（不包含）")
        case "Q" | "q":
            sys.exit()
        case _:
            print("无效输入，请重新选择")
            continue


