# def insert_element(ans,insert):
#     ans.append(insert)
#
#     i = len(ans)-1
#
#     while ans[i] > ans[(i-1)//2] and i > 0:
#         ans[i],ans[(i-1)//2] = ans[(i-1)//2],ans[i]
#         i = (i-1)//2
#
#     return ans
#
#
# heap = [50,55,53,52,54]
# ans = []
# for i in heap:
#     insert_element(ans,i)
# print(ans)