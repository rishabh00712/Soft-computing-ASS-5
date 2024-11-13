import csv


with open("dataset.csv", 'w', newline='') as file:
    writer = csv.writer(file)


    data = [
        ["a", "b", "c", "d", "e", "f", "g", "y"],
    ]
    
    valid = [
        ['1','1','1','1','1','1','0'],# - 0
        ['0','1','1','0','0','0','0'],# - 1
        ['1','1','0','1','1','0','1'],# - 2
        ['1','1','1','1','0','0','1'],# - 3
        ['0','1','1','0','0','1','1'],# - 4
        ['1','0','1','1','0','1','1'],# - 5
        ['0','0','1','1','1','1','1'],# - 6
        ['1','1','1','0','0','0','0'],# - 7
        ['1','1','1','1','1','1','1'],# - 8
        ['1','1','1','0','0','1','1'] # - 9
    ]

    def get_lists():
        for i in range(0,128):
            lst = []
            x = i
            
            while x:
                lst.append(str(x % 2))
                x = x // 2  
            
            lst += ['0'] * (7 - len(lst))
            
            lst.reverse()
            lst.append(str(1 if lst in valid else 0))  
            
            data.append(lst)
    
    get_lists()
    writer.writerows(data)
    
print("CSV file 'dataset.csv' created successfully!")