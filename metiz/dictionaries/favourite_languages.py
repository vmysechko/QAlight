from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

for name, language in favourite_languages.items():
    print(name.title() + "`s favourite language is " +
          language.title() + ".")

print("\n")

favourite_languages_01 = {}

favourite_languages_01['sarah'] = ['pascal', 'java']
favourite_languages_01['edward'] = ['go']
favourite_languages_01['phil'] = ['fortran', 'python']
favourite_languages_01['jen'] = ['c++']

for name, languages in sorted(favourite_languages_01.items()):
    print("\n" + name.title() + "`s favourite language are: ")
    for language in languages:
        print("\t" + language.title())

print("\n")

for name in sorted(favourite_languages_01.keys()):
    print(name.title() + ".")