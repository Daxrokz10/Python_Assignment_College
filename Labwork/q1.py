# WAP to take users favourite movies and store it in a list and print it at the end

num_movies = int(input("Enter number of movies: "))
movie_list = []

i = 1
while i <= num_movies:
    movie = input(f"Enter the name of movie {i}: ")
    movie_list.append(movie)
    i += 1

print("Your favorite movies are:", movie_list)

