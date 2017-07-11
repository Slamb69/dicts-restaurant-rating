"""Restaurant rating lister."""

import sys

filename = sys.argv

restaurant_scores = open(sys.argv[1])

restaurant_ratings = {}

for line in restaurant_scores:
    line = line.rstrip()
    items = line.split(':')
    restaurant_ratings[items[0]] = items[1]

# print restaurant_ratings
for restaurant, rating in sorted(restaurant_ratings.items()):
    print "{} has a rating of {}.".format(restaurant, rating)

# ordered_retaurants_rated = sorted(restaurant_ratings)

#print ordered_retaurants_rated