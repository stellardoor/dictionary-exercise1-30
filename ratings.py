"""Restaurant rating lister."""


def restaurant_rating(file):
    restaurant_scores = open(file)
    restaurant_rating = {}

    for line in restaurant_scores:
        line = line.rstrip()
        scores = line.split(":")
        # for score in scores:
        restaurant_rating[scores[0]] = scores[1]
    restaurant_result = sorted(restaurant_rating.items())
        # print(restaurant_result)
    # final_scores = { }
    for item in restaurant_result:
        print(f"{item[0]} is rated {item[1]}.")
    # for item in final_scores:
    #     print(f"{item} is rated {final_scores[item]}.")

# sys.argv is a list of everything typed into the terminal
restaurant_rating(sys.argv[1]) 
