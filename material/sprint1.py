
# -*- coding: utf-8 -*-

import random

"""
"中獎號碼" 
"請輸入樂透母池最大數"
"請輸入樂透抽取數"
"請輸入自己的號碼"
"自選號碼"
"""




def get_lottery_num(temp_total_num, temp_lottery_num):
    pool = list()
    lottery_pool = list()

    for i in range(int(temp_total_num)):
        pool.append(i)

    random.shuffle(pool)

    for j in range(int(temp_lottery_num)):
        print("todo1#{}: {}".format(j+1, pool[j]+1))
        lottery_pool.append(pool[j]+1)

    return lottery_pool

def compare_lottery_num(temp_choice, temp_lottery):
    count = 0


    for i in range(len(temp_choice)):
        if temp_choice[i] == temp_lottery[i]:
            count+=1

        else:
            continue

    return count





if __name__ == '__main__':

    while True:
        total_choice = list()
        final_lottery_num = list()

        total_num = int(input("todo2: "))
        lottery_num = int(input("todo3: "))

        #print(total_choice)

        #print(pool)

        print("todo4")

        for i in range(lottery_num):
            choice = input("todo5#{}: ".format(i+1))

            total_choice.append(int(choice))


        final_lottery_num = get_lottery_num( total_num, lottery_num)
        print(final_lottery_num)

        print("～對中 {} 個號碼～".format(compare_lottery_num(total_choice, final_lottery_num)))
