def print_pattern(n):
    first_num = 1
    
    for i in range(n):
        row = []
        current = first_num
        

        for j in range(n):
            row.append(str(current))
            current += (2 if i % 2 == 1 else 1)
        
        if i % 2 == 0:
            first_num = row[-1] if j == n-1 else row[j]
            first_num = int(first_num) + 2
        else:
            first_num = row[-1] if j == n-1 else row[j]
            first_num = int(first_num) + 1
            
        print(" ".join(row))


n = int(input())
print_pattern(n)