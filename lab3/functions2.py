def func1(n):
    global movies
    if movies[n]["imdb"] > 5.5:
        return True
    else:
        return False 

def func2():
    global movies
    l = []
    for x in movies:
        if x["imdb"] > 5.5:
            l.append(x["name"])
    return l

def func3(t):
    global movies
    l = []
    for x in movies:
        if x["category"] == t:
            l.append(x["name"])
    return l

def func4(P):
    global movies
    sum = 0
    cnt = 0
    for x in P:
        sum += movies[x]["imdb"]
        cnt += 1
    return sum / cnt

def func5(C):
    global movies
    sum = 0
    cnt = len(C)
    for x in C:
        sum += movies[x]["imdb"]
    return sum / cnt

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print("Single movie, IMDB above 5.5")
s = input()
for x in range(len(movies)):
    if movies[x]["name"] == s:
        n = x
        break
b = func1(n)
print(b)

print("Sublist, IMDB above 5.5")
l = func2()
print(l)

print("Category")
t = input()
q = func3(t)
print(q)

print("Average IDMB of a list of movies")
p = input()
P = []
while p != "stop":
    for x in range(len(movies)):
        if movies[x]["name"] == p:
            m = x
            break
    P.append(m)
    p = input()
a = func4(P)
print(a)

print("Average IDMB of a category")
c = input()
C = []
for x in (range(len(movies))):
    if movies[x]["category"] == c:
        C.append(x)
i = func5(C)
print(i)