# # Question1
# #Implement a python code that finds the probability of selection of 2 from Marvel and 3 from DC teams
# import mysql.connector
# from math import comb
# def get_team_counts():
#     # Connect to the database
#     con = mysql.connector.connect(
#         host="localhost",
#         user = "root",
#         password = "Rk3@7530",
#         database = "gladiator",
#     )
#     cur = con.cursor() 
#     # Get the count of players in Marvel team
#     cur.execute("SELECT COUNT(*) FROM marvel")  
#     marvel_count = cur.fetchone()[0]
#     # Get the count of players in DC team
#     cur.execute("SELECT COUNT(*) FROM dc")
#     dc_count = cur.fetchone()[0]
#     # Close the connection
#     con.close() 
#     return marvel_count, dc_count

# def calculate_probability(marvel_count, dc_count, select_marvel=2, select_dc=3):
#     # Calculate the total number of ways to select players from Marvel and DC teams
#     total_ways_marvel = comb(marvel_count, select_marvel)
#     total_ways_dc = comb(dc_count, select_dc)
    
#     # Calculate the total number of ways to select players from both teams
#     total_ways = total_ways_marvel * total_ways_dc
    
#     # Calculate the probability
#     probability = total_ways / (comb(marvel_count + dc_count, select_marvel + select_dc))
    
#     return probability

# if __name__ == "__main__":
#     marvel_count, dc_count = get_team_counts()
#     probability = calculate_probability(marvel_count, dc_count)
#     print(f"The probability of selecting 2 from Marvel and 3 from DC teams is: {probability:.4f}")  

# This code connects to a MySQL database to retrieve the number of players in the Marvel and DC teams,
# calculates the probability of selecting 2 players from Marvel and 3 players from DC teams,    
# and prints the result. The `comb` function from the `math` module is used to calculate combinations.
# Make sure to have the `mysql-connector-python` package installed to run this code.
# You can install it using pip:
# pip install mysql-connector-python
# Note: Ensure that the database and tables are set up as per the previous code snippets.
# The database connection details (host, user, password) should match your MySQL setup. 
# The code assumes that the Marvel and DC teams have been populated with player data as shown in the previous examples.
# The `comb` function is used to calculate combinations, which is essential for calculating probabilities in this context.
# The `get_team_counts` function retrieves the number of players in each team from the database.

# ## Question2
# #List all those stars who are heavier than SpiderMan and taller than Henery.
# # import mysql.connector
# def get_heavy_tall_stars():
#     import mysql.connector
#     # Connect to the database
#     con = mysql.connector.connect(
#         host="localhost",
#         user = "root",
#         password = "Rk3@7530",
#         database = "gladiator",
#     )
#     cur = con.cursor()  
#     # Get SpiderMan's weight and Henery's height
#     cur.execute("SELECT weight FROM marvel WHERE name = 'SpiderMan'")
#     spiderman_weight = cur.fetchone()[0]
#     cur.execute("SELECT height FROM dc WHERE name = 'Henery'")
#     henery_height = cur.fetchone()[0]
#     # Query to find stars heavier than SpiderMan and taller than Henery
#     print(f"SpiderMan's weight: {spiderman_weight}, Henery's height: {henery_height}")
#     query = """
#         SELECT name, weight, height FROM marvel
#         WHERE weight > %s AND height > %s
#         UNION
#         SELECT name, weight, height FROM dc
#         WHERE weight > %s AND height > %s
# """ 
#     cur.execute(query, (spiderman_weight, henery_height, spiderman_weight, henery_height))
#     results = cur.fetchall()
#     # Close the connection
#     con.close() 
#     return results
# def display_heavy_tall_stars(stars):
#     print(f"{'Name':<20} {'Weight':<8} {'Height':<8}")
#     print("-" * 36)
#     for star in stars:
#         print(f"{star[0]:<20} {star[1]:<8} {star[2]:<8}")  
# if __name__ == "__main__":
#     heavy_tall_stars = get_heavy_tall_stars()
#     if heavy_tall_stars:
#         display_heavy_tall_stars(heavy_tall_stars)
#     else:
#         print("No stars found that match the criteria.")    
# # This code connects to a MySQL database to retrieve the names, heights, and weights of stars who are heavier than SpiderMan and taller than Henery.
# # It uses a SQL query with a UNION to combine results from both Marvel and DC teams.
# # The `get_heavy_tall_stars` function retrieves the necessary data from the database,
# # and the `display_heavy_tall_stars` function formats and prints the results.
# # Make sure to have the `mysql-connector-python` package installed to run this code.


# ## Question3
# """List all those stars who have played more than 100 games and are heavier than
# Captain America"""
# import mysql.connector
# def get_heavy_stars():
#     # Connect to the database
#     con = mysql.connector.connect(
#         host="localhost",
#         user=   "root",
#         password="Rk3@7530",    
#         database="gladiator",
#     )   
#     cur = con.cursor()
#     # Get Captain America's weight
#     cur.execute("SELECT weight FROM marvel WHERE name = 'Captain America'")
#     captain_weight = cur.fetchone()[0]
#     print(f"Captain America's weight: {captain_weight}")
#     # Query to find stars heavier than Captain America and have played more than 100 games
#     query = """ 
#         SELECT name, weight, games_played FROM marvel
#         WHERE weight > %s AND games_played > 100
#         UNION
#         SELECT name, weight, games_played FROM dc
#         WHERE weight > %s AND games_played > 100
#     """
#     cur.execute(query, (captain_weight, captain_weight))
#     results = cur.fetchall()
#     # Close the connection
#     con.close()
#     return results  


# def display_heavy_stars(stars):
#     print(f"{'Name':<20} {'Weight':<8} {'Games Played':<12}")
#     print("-" * 40)
#     for star in stars:
#         print(f"{star[0]:<20} {star[1]:<8} {star[2]:<12}")  

# if __name__ == "__main__":
#         heavy_stars = get_heavy_stars()
#         if heavy_stars:
#             display_heavy_stars(heavy_stars)
#         else:
#             print("No stars found that match the criteria.")

    
# # This code connects to a MySQL database to retrieve the names, weights, and games played of stars who are heavier than Captain America and have played more than 100 games.
# # It uses a SQL query with a UNION to combine results from both Marvel and DC teams.    

    
##Question4
"""For the given dataset representing stars from the Marvel and DC teams, 
if a metaverse is to be formed where the summation of the stats (height, weight, and games played)
of any star is greater than 350 units, then display the names of all the stars meeting this criterion."""

import mysql.connector
def get_metaverse_stars():
    # Connect to the database
    con = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "Rk3@7530",
        database = "gladiator",
    )
    cur = con.cursor()
    # Query to find stars whose summation of stats (height, weight, games played) is greater than 350
    query = """
        SELECT name, height, weight, games_played FROM marvel
        WHERE (height + weight + games_played) > 350
        UNION
        SELECT name, height, weight, games_played FROM dc
        WHERE (height + weight + games_played) > 350
    """
    cur.execute(query)
    results = cur.fetchall()
    # Close the connection
    con.close()
    return results  
def display_metaverse_stars(stars):
    print(f"{'Name':<20} {'Height':<8} {'Weight':<8} {'Games Played':<12}")
    print("-" * 48)
    for star in stars:
        print(f"{star[0]:<20} {star[1]:<8} {star[2]:<8} {star[3]:<12}") 

if __name__ == "__main__":
    metaverse_stars = get_metaverse_stars()
    if metaverse_stars:
        display_metaverse_stars(metaverse_stars)
    else:
        print("No stars found that meet the metaverse criteria.")   

# This code connects to a MySQL database to retrieve the names, heights, weights, and games played of stars whose summation of stats is greater than 350.
# It uses a SQL query with a UNION to combine results from both Marvel and DC teams.

