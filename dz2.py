i = 1
ls_res = []
sum_res = 0
sum_q = 0
# def sum_numb (number):
#     sum_number = 0
#     for i in str(number):
#         sum_number = sum_number + int(i)
#     return sum_number
while i < 1000:
    res = i**3
    ls_res.append(res)
    sum_q = 0
    for q in str(res):
        sum_q = sum_q + int(q)
    #sum_q = sum_numb(res)
    if sum_q % 7 == 0:
        sum_res = sum_res + res
    i = i + 2
print(ls_res)
print(sum_res)
for numb in ls_res:
    res = numb + 17
    sum_q = 0
    for q in str(res):
        sum_q = sum_q + int(q)
    if sum_q % 7 == 0:
        sum_res = sum_res + res
print(sum_res)