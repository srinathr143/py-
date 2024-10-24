
def conse(lst):
    n = len(lst) + 1
    t_sum = n*(n+1)//2
    sum_lst = sum(lst)
    miss_elme = sum_lst - t_sum
    return miss_elme

lst = [101,102,104,105]
print(conse(lst))

