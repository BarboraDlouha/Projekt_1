# separator 
print(67 * "-")

# Header
print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Dlouha
email: Barbora-Dlouha@seznam.cz
""")
# separator
print(67 * "-")

# Input data entry from the user (username, password)
username = input("Enter your username: ")
password = input("Enter your password: ")

# separator
print(67 * "-")

# Creating a user database
login_data = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
    }

# Creating a database of texts for analysis
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# User verification
if username in login_data and login_data[username] == password:
    print(f"Welcome to the application, {username}! We have three texts for analysis.")

    # separator
    print(67 * "-")

    # Text selection
    text_number = [1, 2, 3]
    text_selection = (input("Please, enter the number of the selected text (1 - 3): "))

    # separator
    print(67 * "-")

    # Verifying if the value is a number from the selected range
    if not text_selection.isdigit():
        print("The selected value is not a number.")
    elif not int(text_selection) in text_number:
        print("The selected value is out of the specified range.")
    else:
        selected_text = TEXTS[int(text_selection)-1]
        
        # deleting punctuation from the elected text
        import string
        mapping_table = str.maketrans("","", string.punctuation)
        clean_text = selected_text.translate(mapping_table)
        words = clean_text.split()

        # Counting words in the text
        words_count = len(words)
        print(f"There are {words_count} words in the selected text.")

        # Counting titlecase words in the text
        titlecase_word = [word for word in words if word[0].isupper()]
        titlecase_words_count = len(titlecase_word)
        print(f"There are {titlecase_words_count} titlecase words in the selected text.")

        # Counting uppercase words in the text
        uppercase_word = [word for word in words if word.isupper() and word.isalpha()]
        uppercase_words_count = len(uppercase_word)
        print(f"There are {uppercase_words_count} uppercase words in the selected text.")

        # Counting lowercase words in the text
        lowercase_word = [word for word in words if word.islower() and word.isalpha()]
        lowercase_words_count = len(lowercase_word)
        print(f"There are {lowercase_words_count} lowercase words in the selected text.")

        # Counting numbers in the text
        number = [int(word) for word in words if word.isdigit()]
        numbers_count = len(number)
        print(f"There are {numbers_count} numeric strings in the selected text.")

        # Sum of numbers in the text
        numbers_sum = sum(number)
        print(f"The sum of all the numbers in the text is {numbers_sum}.")
        
        # separator
        print(67 * "-")

        # Counting words in the text by length
        from collections import Counter
        word_length = [len(word) for word in words]
        word_lenght_count = Counter(word_length)
        print(f"{"LEN":>5}| {"OCCURENCES":<18}| {"NR.":<5}")
        print(30 * "-")
        for lenght, count in sorted(word_lenght_count.items()):
            print(f"{lenght:>5}| {count * "*":<18}| {count:<5}")
        print(67 * "-")

else:    
    print("Unregistered user, terminating the program...")