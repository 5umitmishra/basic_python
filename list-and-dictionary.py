# list and dictionary

# nesting

captails = {
    "france": "paris",
    "germany": "burlin"
}

# nesting a list in dictionary
# below we add lists in a dictionary

travel_log = {
    "india": ["delhi", "kolkata", "odisha" ],
    "delhi": ["lal kila", "sarojni", "india gate" ]
}



# nesting dictionary in dictionary

travel_log = [
     {
         "country": "india",
         "state_viseted": ["delhi", "kolkata", "odisha"],
         "total_visited": 9},

     {
         "state": "delhi",
         "place_viseted": ["lal kila", "sarojni", "india gate" ],
         "total_viseted" : 12}

]

print(travel_log)
