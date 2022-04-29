programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.", 
}

# Retreiving items from dictionary.
#print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
#print (programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
#programming_dictionary = {}
#print (programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)


# Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# Nesting List in Dictionary


travel_log = {
  "France": ["Paris", "Marseille", "Rennes", "Dijon", "Lille", "Lyon"],
  "Germany":["Berlin", "Hamburg", "Stutgart", "Hannover", "Dortmund", "Schalke"],         ## KEY (Word) : VALUE (List)
}


# Nesting Dictionary in Dictionary
travel_log = {
  "France": {
    "cities_visited":["Paris", "Marseille", "Rennes", "Dijon", "Lille", "Lyon"], 
    "total_visits": 10,
  },
                          ## DICTIONARY = { KEY (Word) : VALUE (Dictionary{}) }
  "Germany": {
    "cities_visited":["Berlin", "Hamburg", "Stutgart", "Hannover", "Dortmund", "Schalke"],
    "total_visits": 10,
  },
  
}


# Nesting Dictionary in a List
travel_log = [
  {
    "Country": "France",
    "cities_visited":["Paris", "Marseille", "Rennes", "Dijon", "Lille", "Lyon"],     
  
    "total_visits": 10,
  },
                      ##   LIST = [ Dictionary{key: value} , Ditionary{key: value} ]
  {
    "Country": "Germany",
    "cities_visited":["Berlin", "Hamburg", "Stutgart", "Hannover", "Dortmund", "Schalke"],
    "total_visits": 10,
  },
  
]
