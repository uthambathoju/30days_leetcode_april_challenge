from collections import defaultdict
def countElements(arr) -> int:
    cnt_vals = defaultdict(int)
    for ele in arr:
        inc_val = ele + 1
        if(inc_val in arr):
            cnt_vals[ele] += 1
        
    if cnt_vals:
        return sum(cnt_vals.values())
    else:
        return 0



#res = countElements([1,1,3,3,5,5,7,7])
res = countElements([1,1,2,2])
print(res)
