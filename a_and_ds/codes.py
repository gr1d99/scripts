# linear search
def linearsearch():
    position = 0
    item = 3
    some_list = [1, 4, 6, 3, 6, 8, 2]
    # lets start from the beginning
    while position < len(some_list):
        if item == some_list[position]:
            print "Item found at position %s" % position
        position += 1


# binary search
def binarysearch():
    item = 7
    some_list = [2, 5, 7, 12, 14, 21, 28, 31, 36]
    sorted_list = sorted(some_list)
    half = len(sorted_list)/2
    # check if element is in half of the list

    def get_midpoint_item(l):
        
    midpoint_item = sorted_list[half]
    if item == midpoint_item:
        print 'at midpoint'

    elif item < midpoint_item:
        half = len(sorted_list[:midpoint_item])



#linearsearch()
binarysearch()
