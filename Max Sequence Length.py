
def maxSeq(data):
    if not data:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)
    pass


def do_one_test(data):
    print("The max subsequence of {} has length {}".format(data, maxSeq(data)))
    pass

def main():
    do_one_test([])
    do_one_test([1])
    do_one_test([1, 2, 3])
    do_one_test([1, 1, 1])
    do_one_test([1, 2, 1, 2, 3, 4, 1, 2])
    do_one_test([-2, -1, 0, 1, 2])
    do_one_test([1, 2, 3, 1, 2, 3, 4])
    do_one_test([1, 2, 3, 4, 1, 2, 3])
    do_one_test([-10, -4, 0, 5, 34, 89])
    do_one_test([3, 0, 4, 5])
    do_one_test([3, 5, -12])
    do_one_test([1, 2, 1, 3, 5, 6, 2, 5, 8, 12])
    do_one_test([1, 2, 1, 5, 5, 6, 7, 9, 7, 5, 12])
    pass

if __name__ == "__main__":
    main()
    pass

