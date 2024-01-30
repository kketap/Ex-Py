def mcd(m,n):
    rest = 0 
    while(0 < m):
        rest = m

        m = n % m
        n = rest
        return n
def mcm(n,m):
    if n > m    :
        greater = n
    else :
        greater = m
    while (greater % n !=0) or (greater % m  !=0) :
        greater += 1 
    return greater

print(mcd(12,36))
print(mcm(12,36))

