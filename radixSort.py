import Queue

def radixSort(numlist):

    mainbin = Queue.Queue()
    bin0 = Queue.Queue()
    bin1 = Queue.Queue()
    bin2 = Queue.Queue()
    bin3 = Queue.Queue()
    bin4 = Queue.Queue()
    bin5 = Queue.Queue()
    bin6 = Queue.Queue()
    bin7 = Queue.Queue()
    bin8 = Queue.Queue()
    bin9 = Queue.Queue()

    # Bins can be indexed by number:
    bins = [bin0, bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8, bin9]

    largestnum = 0
    biggestplace = 0

    # Queue numlist into mainbin and find the largest number
    for num in numlist:
        mainbin.enqueue(num)
        if num > largestnum:
            largestnum = num

    # Find the order of magnitude of the largest number
    biggestplace = len(str(largestnum))

    print("Main Bin: " + str(mainbin))

    # Sort once for each place of the biggest number
    for i in range(biggestplace):
        # Sort each number into a bin
        for j in range(mainbin.size()):
            # Grab each number in mainbin in order
            current = str(mainbin.dequeue())

            # Check order of magnitude of current number, then bin or return to mainbin
            if (len(current) - 1) >= i:
                # Get digit in i'th location using reverse indexing, then bin the number appropriately
                tobin = current[-1 - i]
                bins[int(tobin)].enqueue(current)
            else:
                mainbin.enqueue(current)
            print(current)

        # Return binned numbers to mainbin in sorted order
        for bin in bins:
            if bin.size() > 0:
                for k in range(bin.size()):
                    mainbin.enqueue(bin.dequeue())

        print(mainbin)

# radixSort([3,4,10, 500, 200, 222222])
# radixSort([14, 9, 37, 5, 2019, 10, 6])
radixSort([4, 3, 5, 80, 2, 6, 46, 1113, 3492352068464654684639, 2394209, 34444])