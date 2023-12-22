from random import randint
import asyncio
import datetime


def create_random_list():
    my_list = []
    for i in range(0, 100000):
        my_list.append(randint(1, 100))
    return my_list


async def summ_of_list_numbers(some_list):
    total = 0

    for num in some_list:
        total += num
    print(total)
    await asyncio.sleep(0.1)


async def main():
    start = datetime.datetime.now()
    my_list = create_random_list()
    result = await asyncio.gather(summ_of_list_numbers(my_list), summ_of_list_numbers(my_list), summ_of_list_numbers(my_list))
    finish = datetime.datetime.now()
    print('Время работы: ' + str(finish - start))


asyncio.run(main())
