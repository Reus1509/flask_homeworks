from random import randint
import datetime
import multiprocessing


def create_random_list():
    my_list = []
    for i in range(0, 100000):
        my_list.append(randint(1, 100))
    return my_list


def summ_of_list_numbers(some_list):
    total = 0

    for num in some_list:
        total += num
    print(total)


if __name__ == "__main__":
    start = datetime.datetime.now()
    print('Время старта: ' + str(start))

    my_list = create_random_list()
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=summ_of_list_numbers, args=(my_list,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    # фиксирует время окончания работы и время работы программы
    finish = datetime.datetime.now()

    print(f'сверка суммы{sum(my_list)}')
    print('Время окончания: ' + str(finish))
    print('Время работы: ' + str(finish - start))
