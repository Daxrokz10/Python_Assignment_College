mov=()
n=int(input("Enter the number of favorite movies: "))
while n>0:
    movie=input("Enter your favorite movie: ")
    mov=mov+(movie,)
    n-=1
print(mov)    