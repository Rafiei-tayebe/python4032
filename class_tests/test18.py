age = float(input())
w = float(input())
h = float(input())
skin_color = input()
hair_color = input()
glasses = input()
mask = input()

count = 0
if mask == "Nadare" :
    print("Qaribas")
else:
    if 15 <= age <= 45: count+=1
    if 60 <= w <= 120: count+=1
    if (180 <= h <= 200) or (150 <= h <= 160): count+=1
    if skin_color == "Sand" or skin_color == "Bronze" :
        count += 1
    if hair_color == "Black" or hair_color == "Brown":
        count += 1
    if glasses == "Nadare" : count+=1 
    
    if count == 6:
        print("Ashnas")
    elif count >= 1:
        print("Shayad")
    else:
        print("Qaribas")
    
        

