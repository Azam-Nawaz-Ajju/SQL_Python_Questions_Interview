# Questions:

# Q1: List all restaurants in a specific locality.
# Q2: Show the name and city of restaurants with a rating lower than 3.
# Q4: Display restaurants that have an average cost for two less than $50.
# Q5: Find restaurants with more than 100 votes.
# Q6: List the names of restaurants offering both table booking and online delivery.
# Q7: Show the cuisines offered by restaurants in 'Paris'.
# Q10: List all restaurants with 'Cafe' in their cuisine type.
# Q14: Display the average rating of 'Chinese' cuisine restaurants.
# Q15: Find the most common price range for restaurants in 'London'.
# Q19: Calculate the percentage of restaurants delivering now in each city.
# Q39: Calculate the percentage of restaurants in each locality with a rating above 4.5.

import pandas as pd
df = pd.read_csv(r'/home/nineleaps/Downloads/NineLeaps/Zomato_Dataset.csv')
locality = input("Enter locality name: ").strip()
result = df[df["Locality"].str.lower() == locality.lower()]
print(f"\nRestaurants in {locality}:")
print(result[["RestaurantID", "RestaurantName", "Address", "Cuisines", "Rating"]])
print("\nTotal restaurants found:", result.shape[0])
