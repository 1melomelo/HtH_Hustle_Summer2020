full_name = "Melo Yellow"
nickname = "Melo"
age = 99
has_used_python = True

hobbies = [
    "dancing", "traveling", "eating good food",
    "volunteering", "watching movies", "hanging out with dogs"
]

fav_things = {
    "movie": "Get Out",
    "food": "steak",
    "hobby": hobbies[0],
    "show/anime": "Killing Eve",
    "number": 33
}

print(
    f"Hello world! My name is {full_name}, but many of my friends call me {nickname}. I am {age} years old."
)
print()
print(f"Has Python Experience: {has_used_python}")
print()

for key in fav_things.keys():
    print(f"My favorite {key} is {fav_things[key]}.")

print()
print(f"Here are some of my other hobbies: {hobbies}")
print()

all_vars = dict(vars())