def solve(numheads, numlegs):
    r = (numlegs-2*numheads)/2
    ch = numheads - r
    print("chickens:", format(ch,".0f"), "\nrabbits:", format(r,".0f"))
h = 35
l = 94
solve(h,l)