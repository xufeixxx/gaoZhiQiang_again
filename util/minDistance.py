def computeMinDistance_BS_ID(twoPointDisList):
    list_length = len(twoPointDisList)
    quick_sort(twoPointDisList, 0, list_length-1)
    return twoPointDisList[0].BS_id


def quick_sort(twoPointDisList, low, high):
    if low < high:
        i, j, x = low, high, twoPointDisList[low].dis
        m = twoPointDisList[low]
        while i < j:
            while i < j and twoPointDisList[j].dis >= x:
                j -= 1
            if i < j:
                twoPointDisList[i] = twoPointDisList[j]
                i += 1
            while i < j and twoPointDisList[i].dis < x:
                i += 1
            if i < j:
                twoPointDisList[j] = twoPointDisList[i]
                j -= 1

        twoPointDisList[i] = m
        quick_sort(twoPointDisList, low, i-1)
        quick_sort(twoPointDisList, i + 1, high)
