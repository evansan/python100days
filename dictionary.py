favorite_languages = {
      'jen': 'python',
      'sarah': 'c',
      'edward': 'rust',
      'phil': 'python',
      }

language = favorite_languages['sarah'].title() 
print(f"Sarah's favorite language is {language}.")


alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('dd', 'blue')
print(point_value)

person = {'age': 21, 'name': 'alex', 'gender': 'male'}
print (person['age'])

user_0 = {
                 'username': 'efermi',
                 'first': 'enrico',
                 'last': 'fermi',
                 }
for key, value in user_0.items():
            print(f"\nKey: {key}")
            print(f"Value: {value}")
print (user_0)

exit = ""
while exit == "yes":
      print("🥳")
      exit = input("Exit?: ")
