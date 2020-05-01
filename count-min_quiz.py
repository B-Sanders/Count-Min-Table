def hash1(x):
    z = (x%5)%4
    return z

def hash2(x):
    z = (x%7)%4
    return z

def hash3(x):
    z = (x%13)%4
    return z

def list_to_table(l, t):
    
    for n in l:
        a = hash1(n)
        t[0][a] += 1

        b = hash2(n)
        t[1][b] += 1

        c = hash3(n)
        t[2][c] += 1

def get_min(l, t):
    mins = {}
    for n in l:
        n_min = 0
        a = hash1(n)
        b = hash2(n)
        c = hash3(n)
        n_min = min(t[0][a], t[1][b], t[2][c])
        mins[n] = n_min
    return mins

def differences(dic, l):
    counts_l = {}
    diff_d = {}
    for num in l:
        if num in counts_l:
            counts_l[num] += 1
        else:
            counts_l[num] = 1
    for key in dic:
        if counts_l[key] < dic[key]:
            diff_d[key] = "Overestimate"
        else:
            diff_d[key] = "Exact"
    return diff_d
        
    
    
def main():
    l = [1, 35, 10, 17, 9, 14, 1, 35, 17, 35, 16, 9]
    count_l = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    list_to_table(l, count_l)
    countz = get_min(l, count_l)
    d = differences(countz, l)
    print(d)

main()

