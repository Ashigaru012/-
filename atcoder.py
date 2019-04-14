t,n = map(int,input().split()) #tは区間、nは個数
for i in range(n):
    m = list(map(int,input().split()))
ans = sum(m[0:t])
tmp = ans
for i in range(n-t): #m[t+i]がout of rangeにならないため範囲をn-tにする
    tmp += m[t+i] #tmpに区間の末尾を足す
    tmp -= m[i]  #tmpに区間の先頭の一つ前を引く
    if ans < tmp:
        ans = tmp
print(tmp)

#しゃくとり法は前の最後の値の尻尾を切って、前の先頭の次の値を頭にするやり方