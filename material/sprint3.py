
# -*- coding: utf-8 -*-

import random
import sys


"""
中獎號碼
中獎號碼
特別號碼
請輸入自己的號碼(玩一次350元)
已經有此號碼，請重新輸入！
遊戲已結束
請輸入範圍內的號碼
" ----------------------"
"""

def get_lottery_num(temp_total_num, temp_lottery_num):
    pool = list()
    lottery_pool = list()

    for i in range(int(temp_total_num)):
        pool.append(i)

    random.shuffle(pool)

    for j in range(int(temp_lottery_num)):
        print("todo1#{}:\t{}".format(j+1, pool[j]+1))
        lottery_pool.append(pool[j]+1)

    return lottery_pool



def compare_lottery_num(temp_choice, temp_lottery):
    count = 0

    temp_choice.sort()
    temp_lottery.sort()

    #print(temp_choice)
    #print(temp_lottery)

    for i in temp_choice:
        if compare_single_num(i, temp_lottery):
            count+=1

        else: continue

    return count


def compare_single_num(temp_choice, temp_lottery):

    for i in temp_lottery:
        if int(temp_choice) == i:
            return True

        else: continue

    return False

def get_TWlottery_num():
    pool = list()
    lottery_pool = list()

    for i in range(49):
        pool.append(i)

    random.shuffle(pool)

    for j in range(6):
        print("todo2#{}:\t{}".format(j+1, pool[j]+1))
        lottery_pool.append(pool[j]+1)

    print("todo3:\t{}".format(pool[6]+1))
    lottery_pool.append(pool[6]+1)

    return lottery_pool
'''
假設總獎金為 1億
頭獎為 82000000
貳獎為 6500000
參獎為 7000000
肆獎為 4500000
伍獎為 2000
陸獎為 1000
柒獎為 400
普獎為 400

'''
def compare_TWlottery_num(temp_choice, temp_twlottery):
    normal_num = list()


    special_num = temp_twlottery.pop()
    normal_num = temp_twlottery

    result_num = compare_lottery_num(temp_choice, normal_num)

    print("todo4")

    if result_num == 3:
        print("|     『恭喜中普獎』     |")
        return 400

    elif result_num == 2 and compare_single_num(special_num, temp_choice):
        print("|     『恭喜中柒獎』     |")
        return 400

    elif result_num == 3 and compare_single_num(special_num, temp_choice):
        print("|     『恭喜中陸獎』     |")
        return 1000

    elif result_num == 4:
        print("|     『恭喜中伍獎』     |")
        return 2000

    elif result_num == 4 and compare_single_num(special_num, temp_choice):
        print("|     『恭喜中肆獎』     |")
        return 4500000

    elif result_num == 5:
        print("|     _恭喜中參獎_     |")
        return 7000000

    elif result_num == 5 and compare_single_num(special_num, temp_choice):
        print("|    ~恭喜中貳獎~      |")
        return 6500000

    elif result_num == 6:
        print("|  !!!恭喜中頭獎!!!  |")
        return 82000000

    else:
        print("|     「本期沒中獎」     |")
        return 0


if __name__ == '__main__':

    money = 0
    total_choice = list()

    while True:
        print("todo5")
        money -= 350

        for i in range(6):
            while True:
                choice = input("todo6{}:\t".format( i+1))
                if compare_single_num(choice, total_choice):
                    print("todo7")

                else:
                    if int(choice) <= 49 and int(choice) > 0:
                        total_choice.append(int(choice))
                        break

                    elif int(choice) == -1:
                        print("todo8")
                        sys.exit(0)
                    else:
                        print("todo9")
                        continue

        final_lottery_num = get_TWlottery_num()

        print(" ======================")
        print("|{:3}{:3}{:3}{:3}{:3}{:3}|{:3}|".format( final_lottery_num[0], final_lottery_num[1], final_lottery_num[2],final_lottery_num[3],final_lottery_num[4],final_lottery_num[5], final_lottery_num[6] ))
        print("|{:3}{:3}{:3}{:3}{:3}{:3}|   |".format( total_choice[0], total_choice[1], total_choice[2],total_choice[3],total_choice[4],total_choice[5] ))


        #print(final_lottery_num)
        #print(total_choice)


        money += compare_TWlottery_num(total_choice, final_lottery_num)
        print("todo10")
        print("|現在持有現金為 {} 元   |".format( money))
        print(" ======================")

        total_choice.clear()

        #print("～對中 {} 個號碼～".format(compare_lottery_num(total_choice, final_lottery_num)))

