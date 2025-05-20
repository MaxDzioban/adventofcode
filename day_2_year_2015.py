# part 1
paper=0
with open("day_2_year_2015.txt", "r", encoding="utf-8") as file:
    for line in file:
        l, w, h = line.split("x")
        l = int(l)
        w= int(w)
        h = int(h)
        paper += 2*l*w + 2*w*h + 2*h*l
        paper += min(l*w, w*h , h*l)
print(paper)

#part 2
ribbon=0
with open("day_2_year_2015.txt", "r", encoding="utf-8") as file:
    for line in file:
        l, w, h = line.split("x")
        l = int(l)
        w= int(w)
        h = int(h)
        ribbon +=min(2*(l+w), 2*(w+h) , 2*(h+l))
        ribbon+= l*w*h
print(ribbon)