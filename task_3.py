def my_fun(n_1, n_2, n_3):
    my_list = [n_1, n_2, n_3]
    try:
     my_list.remove(min(my_list))
     return sum(my_list)
    except TypeError:
        return "enter only number"
print(my_fun(20, 15, 5))


