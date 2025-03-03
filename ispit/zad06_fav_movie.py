'''
Favorite Movie
It's Friday night and you're wondering which movie to watch. You decide to write a program that will make the choice for you. Until the command "STOP" is received, you will receive titles of your favorite movies. The best movie for you will be the one with the highest score. The score is calculated as the sum of the ASCII values of the characters in the movie title. (There will be no case of two movies with equal scores).
    • For each lowercase letter in the title, its value should be reduced by twice the length of the movie title.
    • For each uppercase letter in the title, its value should be reduced by the length of the movie title.
You will receive a maximum of 7 movie titles.
Input
Read lines from the console until you receive the command "STOP" or until the limit of 7 movies is reached.
    • Movie title  – a string; length [1… 100]
'''
# Moje resenje:
movie_name = ""
count_movies = 0
max_char = 0
best_movie = ""
while True:
  movie_name = input()
  if movie_name == "STOP":
    break
  elif count_movies == 7:
    print("The limit is reached.")
    break
  title_length = len(movie_name)
  char_sum = 0
  for i in range(title_length):
    if movie_name[i] == ' ':
       char_sum += ord(movie_name[i])
    elif movie_name[i].isupper():
      char_sum += ord(movie_name[i]) - title_length
    else:
      char_sum += ord(movie_name[i]) - (title_length * 2)
  if char_sum > max_char:
    max_char = char_sum
    best_movie = movie_name

  count_movies += 1

print(f"The best movie for you is {best_movie} with {max_char} ASCII sum.")

# chat gpt resenje:
def calculate_score(title: str) -> int:
    length = len(title)
    score = 0

    for char in title:
        ascii_value = ord(char)
        if 'A' <= char <= 'Z':  # Uppercase letters
            ascii_value -= length
        elif 'a' <= char <= 'z':  # Lowercase letters
            ascii_value -= (2 * length)
        score += ascii_value
    
    return score

# Initialize variables
best_movie = ""
best_score = float('-inf')
count = 0

while count < 7:  # Limit of 7 movies
    movie_title = input("Enter movie title (or 'STOP' to finish): ")
    if movie_title == "STOP":
        break

    count += 1
    current_score = calculate_score(movie_title)

    if current_score > best_score:
        best_movie = movie_title
        best_score = current_score

# Display the best movie
print(f"The best movie for you is {best_movie} with a score of {best_score}.")

# Enter movie title (or 'STOP' to finish): Titanic
# Enter movie title (or 'STOP' to finish): Inception
# Enter movie title (or 'STOP' to finish): Avatar
# Enter movie title (or 'STOP' to finish): STOP