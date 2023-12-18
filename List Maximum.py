def listMax(lst):
    if lst is None or len(lst) == 0:
        return None
    else:
        max_element = lst[0]
        for element in lst:
            if element > max_element:
                max_element = element
        return max_element
def doTest(lst):
    print('listMax(', end='')
    if lst is None:
        print('None) is ', end='')
    else:
        n = len(lst)
        print('[', end='')
        for i in range(0, n):
            print('{}'.format(lst[i]), end='')
            if i < n - 1:
                print(', ', end='')
        print(']) is ', end='')

    maximum = listMax(lst)
    if maximum is None:
        print('None')
    else:
        print('{}'.format(maximum))

def main():
    list1 = [77, 33, 19, 99, 42, 6, 27, 4]
    list2 = [-3, -42, -99, -1000, -999, -88, -77]
    list3 = [425, 59, -3, 77, 0, 36]
    
    doTest(list1)
    doTest(list2)
    doTest(list3)
    doTest(None)
    doTest([])

if __name__ == '__main__':
    main()
