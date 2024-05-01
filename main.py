def sort_algo(number_list):
    n = len(number_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]


while True:
    input_str = input("Please enter numbers separated by spaces: ")

    if input_str == "stop":
        break

    number_list_inp = [int(x) for x in input_str.split()]

    sort_algo(number_list_inp)

    print("The list is sorted like this:", number_list_inp)




