from math import gcd


def slow(array):
    """
    compute the winner of a game
    :param array: [x1, ... xN]
    :return: result (bool)
    """
    result = False
    for index in range(1, len(array)):
        g = gcd(array[index], array[index - 1])
        if g > 1:
            array[index] //= g
            array[index - 1] //= g
            if not slow(array):
                result = True
            array[index] *= g
            array[index - 1] *= g

    return result


def alice_or_bob(array):
    """
    returns the winner of a game
    :param array: [x1, ... xN]
    :return: 'Alice' or 'Bob'
    """
    return 'Alice' if slow(array) else 'Bob'


def main():
    # print(alice_or_bob(array=[2, 4, 2]))
    print(alice_or_bob(array=[2, 3, 9, 6, 18]))
    print(alice_or_bob(array=[2, 630, 680, 735, 578, 510]))
    print(alice_or_bob(array=[2, 49, 70, 80, 70, 70, 70, 70, 56, 98, 5]))
    print(alice_or_bob(array=[2, 2, 3]))
    print(alice_or_bob(array=[2, 2, 4, 6, 8]))
    print(alice_or_bob(array=[2, 12, 16, 18, 34]))
    print(alice_or_bob(array=[2, 2, 4, 2, 1, 3, 6, 6]))
    print(alice_or_bob(array=[2, 1, 1, 1, 1, 1, 1, 1]))
    print(alice_or_bob(array=[1, 2, 3, 4, ]))
    print(alice_or_bob(array=[1, 2, 3, 4, ]))
    print(alice_or_bob(array=[1, 2, 3, 4, ]))
    # print(alice_or_bob(array=[7, 7]))
    # print(alice_or_bob(
    #     array=[315, 792, 150, 660, 420, 570, 950, 570, 990, 960, 300, 180, 90, 90, 585, 195, 741, 741, 57, 297]))
    # print(alice_or_bob(
    #     array=[281418291, 17336200, 922370955, 503111430, 364095290, 651410760,
    #            196051310, 612636310, 752491740, 336596260, 52169260, 47607560,
    #            484430232, 1560780, 425000394, 294332610]))

    # how to solve n == 50?
    # https://e-maxx.ru/algo/sprague_grundy + Dynamic Programming on substrings
    # more on that theme http://acm.timus.ru/problem.aspx?space=1&num=1465&locale=en


if __name__ == '__main__':
    main()
