"""Restaurant rating lister."""

import sys

filename = sys.argv

restaurant_scores = open(sys.argv[1])

restaurant_ratings = {}

new_restaurant = raw_input("Name a restaurant you want to rate: ")

while True:
    new_rating = raw_input("Give this restaurant a rating between 1-5: ")
    try:
        if int(new_rating) in range(1, 6):

            restaurant_ratings[new_restaurant] = new_rating
            break
        else:
            print "Try again we need a number between 1-5."

    except:
        print "Try again we need a number between 1-5."

for line in restaurant_scores:
            line = line.rstrip()
            items = line.split(':')
            restaurant_ratings[items[0]] = items[1]

for restaurant, rating in sorted(restaurant_ratings.items()):
    print "{} has a rating of {}.".format(restaurant, rating)
