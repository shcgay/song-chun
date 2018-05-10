def get_num(num):
    if num == 1:
        return 1
    else:
        return num*get_num(num-1)
get_num(5)

