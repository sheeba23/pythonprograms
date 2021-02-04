"""W.A.P to find different aggregates(min, max, average/mean and median) value in existing list of numbers.
[5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]
Note:- Program should have implementation of function and
don't use inbuilt function to calculate specific aggregates."""

static_list = [5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]


def find_aggregates() -> tuple:
    """
    This function is used to find aggregates such as:
    mean/average
    median
    maximum
    minimum
    """
    total = 0
    mean_avg = 0
    current_num = 0
    present_num = 0
    sorted_list = sorted(static_list)
    list_length = len(sorted_list)
    num = list_length // 2
    if list_length % 2 == 0:
        middle_num = (sorted_list[num] + sorted_list[num - 1]) / 2
    else:
        middle_num = sorted_list[num]
    for num in static_list:
        total = total + num
        mean_avg = total / len(static_list)
        current_num = sorted_list[0]
        present_num = sorted_list[-1]
        if num < current_num:
            current_num = num
        elif num > present_num:
            present_num = num
    return mean_avg, middle_num, current_num, present_num


if __name__ == '__main__':
    mean_avg, middle_num, current_num, present_num = find_aggregates()
    print("Median of  list is: ", mean_avg)
    print("Mean or average of list is: ", middle_num)
    print("Minimum number from list is: ", current_num)
    print("Maximum number from list is: ", present_num)
