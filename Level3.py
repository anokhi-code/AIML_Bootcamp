# #Question1
# """In the Marvel and DC teams, the players are randomly selected for a special tournament
# where the selection criteria include:
# The player must be above 180 cm in height.
# The player must have played more than 50 games. 
# If one player is randomly chosen from each team, what is the probability that both selected players 
# meet the selection criteria for the tournament?"""

# import mysql.connector

# # Connect to your database
# con = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Rk3@7530",
#     database="gladiator"
# )
# cur = con.cursor()

# # Marvel team
# cur.execute("SELECT COUNT(*) FROM marvel")
# total_marvel = cur.fetchone()[0]

# cur.execute("SELECT COUNT(*) FROM marvel WHERE height > 180 AND games_played > 50")
# qualified_marvel = cur.fetchone()[0]

# # DC team
# cur.execute("SELECT COUNT(*) FROM dc")
# total_dc = cur.fetchone()[0]

# cur.execute("SELECT COUNT(*) FROM dc WHERE height > 180 AND games_played > 50")
# qualified_dc = cur.fetchone()[0]

# # Calculate probabilities
# prob_marvel = qualified_marvel / total_marvel if total_marvel else 0
# prob_dc = qualified_dc / total_dc if total_dc else 0
# prob_both = prob_marvel * prob_dc

# print(f"Marvel: {qualified_marvel}/{total_marvel} meet criteria")
# print(f"DC: {qualified_dc}/{total_dc} meet criteria")
# print(f"Probability both selected players meet criteria: {prob_both:.2f}")

# cur.close()
# con.close()

""""Consider that a team is formed by selecting one player from the Marvel team and two players from the DC team for an upcoming championship. The selection criteria include:
● At least one player selected should have a weight below 80 kg.
● The combined weight of the team should not exceed 250 kg.
What is the probability of forming such a team, given that the selection is made randomly from the Marvel and DC teams?"""

import mysql.connector

# Connect to your database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rk3@7530",
    database="gladiator"
)
cur = con.cursor()
# Marvel team
cur.execute("SELECT COUNT(*) FROM marvel")
total_marvel = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM marvel WHERE weight < 80")
qualified_marvel = cur.fetchone()[0]
# DC team
cur.execute("SELECT COUNT(*) FROM dc")
total_dc = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM dc WHERE weight < 80")
qualified_dc = cur.fetchone()[0]
# Calculate probabilities
prob_marvel = qualified_marvel / total_marvel if total_marvel else 0
prob_dc = qualified_dc / total_dc if total_dc else 0
# Probability of selecting one Marvel player and two DC players
prob_team = prob_marvel * (prob_dc ** 2)
print(f"Marvel: {qualified_marvel}/{total_marvel} meet criteria")
print(f"DC: {qualified_dc}/{total_dc} meet criteria")
print(f"Probability of forming a team with at least one player below 80 kg and total weight <= 250 kg: {prob_team:.2f}")
cur.close()
con.close()
# Note: The above code assumes that the database and tables are already set up as per the previous code snippet.