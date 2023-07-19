# coding:UTF-8 #
"""
@filename:main.py
@autor:stormcar
@time:2023-07-19
"""
# 数字炸弹游戏
import random, os, time, sys


def num_bomb():

    while True:
        #模式选择
        while True:
            gamemode = input("请选择游戏模式（1-单人，2-双人，3-与Bot对战，Q/q-退出游戏）：")
            match gamemode:
                case "1" | "2" | "3":
                    break
                case "Q" | "q":
                    return
                case _:
                    print("无效符号，请重新输入")
                    continue
        # 初始化
        os.system("cls")  # windows清屏
        bomb_min, bomb_max = 1, 100
        bomb = random.randint(bomb_min, bomb_max)
        gnum, n = 0, 1
        warning_p1,warning_p2 = 0,0
        print("\n----数字炸弹游戏开始----")

        while True:
            print("\nRound-{}\n(请输入一个{}到{}的数字)".format(n, bomb_min, bomb_max))
            # player1
            while True:
                while True:
                    try:
                        gnum = int(input("player1："))
                        break
                    except ValueError as err:
                        print("输入错误！")
                        continue
                if gnum == bomb:
                    print("----踩到雷啦！游戏结束~---\n----(Bomb is {}，第{}回合player1踩雷)----\n".format(bomb,n))
                    n = 0
                    break
                elif gnum < bomb_min or gnum > bomb_max:
                    if warning_p1 < 1:
                        warning_p1 += 1
                        print("***超出范围警告player1一次,注：若再次犯规，炸弹将直接爆炸！***")
                    else:
                        print("----两次超出范围，雷爆啦！游戏结束~----\n----(第{}回合player1犯规自爆)----\n".format(n))
                        n = 0
                        break
                elif gnum < bomb:
                    bomb_min = gnum + 1
                    break
                elif gnum > bomb:
                    bomb_max = gnum - 1
                    break
            if n==0:
                break

            if gamemode=="1":
                n+=1
                continue

            # player2
            if gamemode=="2":
                print("(请输入一个{}到{}的数字)".format(bomb_min, bomb_max))
                while True:
                    while True:
                        try:
                            gnum = int(input("player2："))
                            break
                        except ValueError as err:
                            print("输入错误！")
                            continue
                    if gnum == bomb:
                        print("----踩到雷啦！player1获胜，游戏结束~---\n----(Bomb is {}，第{}回合player2踩雷)----\n".format(bomb,n))
                        n = 0
                        break
                    elif gnum < bomb_min or gnum > bomb_max:
                        if warning_p2 < 1:
                            warning_p2 += 1
                            print("***超出范围警告player2一次,注：若再次犯规，炸弹将直接爆炸！***")
                        else:
                            print("----两次超出范围，雷爆啦！player1获胜，游戏结束~----\n----(第{}回合player2犯规自爆)----\n".format(n))
                            n = 0
                            break
                    elif gnum < bomb:
                        bomb_min = gnum + 1
                        break
                    elif gnum > bomb:
                        bomb_max = gnum - 1
                        break
                if n == 0:
                    break
                n += 1

            # Bot
            if gamemode=="3":
                print("(请输入一个{}到{}的数字)".format(bomb_min, bomb_max))
                gnum = random.randint(bomb_min, bomb_max)
                print("Bot：运气真好，到我啦：", end=" ")
                sys.stdout.flush()
                time.sleep(2)
                print(gnum, "\n")
                n += 1
                if gnum == bomb:
                    print("----Bot踩雷，恭喜你，获胜了~---\n----(Bomb is {}，第{}回合Bot踩雷)----\n".format(bomb,n))
                    break
                elif gnum < bomb:
                    bomb_min = gnum + 1
                elif gnum > bomb:
                    bomb_max = gnum - 1

num_bomb()


