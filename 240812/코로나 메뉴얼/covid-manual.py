symptomA, tempA = input().split()
symptomB, tempB = input().split()
symptomC, tempC = input().split()

tempA = float(tempA)
tempB = float(tempB)
tempC = float(tempC)

count_A = 0

if symptomA == "Y" and tempA >= 37:
    count_A += 1
if symptomB == "Y" and tempB >= 37:
    count_A += 1
if symptomC == "Y" and tempC >= 37:
    count_A += 1

# 위급상황인지 판단
if count_A >= 2:
    print("E")
else:
    print("N")