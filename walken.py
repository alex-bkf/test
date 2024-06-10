import random

player1 = list()
player2 = list()
cathletism_800 = 800

player1_result_list = list()
player2_result_list = list()

player1_count = 0
player2_count = 0

def result(list1, list2):
   global player1_count, player2_count
   for x in range(5):
       if list1[x] > list2[x]:
            player1_count += 1
       elif list1[x] < list2[x]:
            player2_count += 1
       else:
           continue

   print('Соперник:', list1)
   print('Вы:', list2)

   if player1_count > player2_count:
       print('Победил соперник, счет: {}:{}'.format(player1_count, player2_count))
   elif player1_count < player2_count:
       print('Вы победили, счет: {}:{}'.format(player1_count, player2_count))
   else:
       print('Ничья, счет: {}:{}'.format(player1_count, player2_count))


def input_stat():
    global player1, player2

    total_stat = float(random.randint(700, 800))
    for i in range(1, 6):
        if i == 5:
            player1.append(total_stat - sum(player1))
        else:
            end = ((total_stat - sum(player1)) // abs(i - 6))
            number_stat = float(random.randint(108, end))
            player1.append(number_stat)

    for i_com in range(1):
        print('Введите значение вашей команды:\n')
        for i in range(1, 6):
            stat = float(input('Введите стату {}-ого кота: '.format(i)))
            while stat < 108:
                print('Стата не должна быть ниже 108, введите повторно')
                stat = float(input('Введите стату {}-ого кота: '.format(i)))
            else:
                player2.append(stat)

    print('Соперник:', player1, '\n' + 'Вы:', player2, '\n')
    print('Сумарный катлетизм соперника = {}\n'
          'Ваш сумарный катлетизм = {}'.format(sum(player1), sum(player2)))

    return player1, player2


def who_is_win(list1, list2):                            # [140.0, 130.0, 108.0, 120.0, 110.0]
    global player1_result_list, player2_result_list      # [110.0, 120.0, 140.0, 150.0, 130.0]
    if sum(list1) <= cathletism_800 and sum(list2) <= cathletism_800:
        print('Бой в первой ставке, катлетизм до 800')
        if sum(list1) > sum(list2):
            print('Первым ходит ваш соперник')
            while len(list1) != 0:
                cart1 = random.choice(list1)
                print('Ход соперника: {}'.format(cart1))
                list1.remove(cart1)
                player1_result_list.append(cart1)

                cart2 = float(input('Делайте ваш ход: '))
                while not cart2 in list2:
                    print('Делайте ход своими картами:', list2)
                    cart2 = float(input('Делайте повторно ваш ход: '))
                else:
                    print('Вы походили: {}'.format(cart2))
                    list2.remove(cart2)
                    player2_result_list.append(cart2)

        elif sum(list1) < sum(list2):
            print('Первым ходите вы')
            while len(list2) != 0:
                cart2 = float(input('Делайте ваш ход: '))
                while not cart2 in list2:
                    print('Делайте ход своими картами:', list2)
                    cart2 = float(input('Делайте повторно ваш ход: '))
                else:
                    print('Вы походили: {}'.format(cart2))
                    list2.remove(cart2)
                    player2_result_list.append(cart2)

                cart1 = 0
                temp_list = list1.copy()
                while len(temp_list) != 0:
                    if len(temp_list) == 1:
                        cart1 = temp_list[0]
                        break
                    else:
                        cart1 = min(temp_list)
                        if cart1 > cart2:
                            break
                        else:
                            temp_list.remove(cart1)

                print('Ход соперника: {}'.format(cart1))
                list1.remove(cart1)
                player1_result_list.append(cart1)
        return player1_result_list, player2_result_list










player1_list, player2_list = input_stat()
player1_res, player2_res = who_is_win(player1_list, player2_list)
result(player1_res, player2_res)
