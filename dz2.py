i = 1
ls_res = []
sum_res = 0
sum_q = 0
while i < 1000:
    res = i**3
    ls_res.append(res)
    sum_q = 0
    for q in str(res):
        sum_q = sum_q + int(q)
    if sum_q % 7 == 0:
        sum_res = sum_res + res
    i = i + 2
# for s in ls_res:
#     sum_q = 0
#         ls_res1.append(sum_q)
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