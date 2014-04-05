fiboValuePre = 0
fiboValueNext = 1

sumValue = 0
fiboValueNextNext = 0

while fiboValueNextNext <= 4000000 :
    fiboValueNextNext = fiboValuePre+fiboValueNext
    if fiboValueNextNext%2==0 :
        sumValue += fiboValueNextNext 
    fiboValuePre = fiboValueNext
    fiboValueNext = fiboValueNextNext


print(str(sumValue))
