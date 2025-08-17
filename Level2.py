# """Implement a python code to find following values and interpret why these are useful and in which scenarios:"""
# #1. Find Mean and Median of their respective heights, weights and Games played.
# import mysql.connector
# def calculate_mean_median():
#     # Connect to the database
#     con = mysql.connector.connect(
#         host="localhost",
#         user = "root",
#         password = "Rk3@7530",
#         database = "gladiator",
#     )
#     cur = con.cursor()
#     # Query to get heights, weights, and games played from both Marvel and DC
#     query = """
#         SELECT height, weight, games_played FROM marvel
#         UNION ALL
#         SELECT height, weight, games_played FROM dc
#     """ 
#     cur.execute(query)
#     results = cur.fetchall()
    
#     # Close the connection
#     con.close()
    
#     # Calculate mean and median for heights, weights, and games played
#     heights = [row[0] for row in results]
#     weights = [row[1] for row in results]
#     games_played = [row[2] for row in results]
    
#     def calculate_mean(data):
#         return sum(data) / len(data) if data else 0
    
#     def calculate_median(data):
#         sorted_data = sorted(data)
#         n = len(sorted_data)
#         mid = n // 2
#         if n % 2 == 0:
#             return (sorted_data[mid - 1] + sorted_data[mid]) / 2
#         else:
#             return sorted_data[mid]
    
#     mean_height = calculate_mean(heights)
#     median_height = calculate_median(heights)
    
#     mean_weight = calculate_mean(weights)
#     median_weight = calculate_median(weights)
    
#     mean_games_played = calculate_mean(games_played)
#     median_games_played = calculate_median(games_played)
    
#     return {
#         "mean_height": mean_height,
#         "median_height": median_height,
#         "mean_weight": mean_weight,
#         "median_weight": median_weight,
#         "mean_games_played": mean_games_played,
#         "median_games_played": median_games_played
#     }

# def display_statistics(stats):
#     print(f"{'Statistic':<20} {'Value':<10}")          
#     print("-" * 30)
#     print(f"{'Mean Height':<20} {stats['mean_height']:<10}")
#     print(f"{'Median Height':<20} {stats['median_height']:<10}")
#     print(f"{'Mean Weight':<20} {stats['mean_weight']:<10}")
#     print(f"{'Median Weight':<20} {stats['median_weight']:<10}")
#     print(f"{'Mean Games Played':<20} {stats['mean_games_played']:<10}")
#     print(f"{'Median Games Played':<20} {stats['median_games_played']:<10}")    

# if __name__ == "__main__":
#     stats = calculate_mean_median()
#     display_statistics(stats)
# # This code connects to a MySQL database to retrieve the heights, weights, and games played of stars from both Marvel and DC teams.
# # It calculates the mean and median for each of these attributes and displays the results.
# # The mean and median are useful for understanding the central tendency of the data, which can help in making comparisons between different groups or in identifying outliers.
# # Mean provides the average value, while median gives the middle value when the data is sorted, which is less affected by outliers.
# # This is particularly useful in scenarios where you want to analyze the performance or characteristics of different teams or individuals based on their physical attributes and game statistics.

# #2. Find Deviation and Standard deviation of height and weight.
# import mysql.connector
# def calculate_deviation_and_stddev():
#     # Connect to the database
#     con = mysql.connector.connect(
#         host="localhost",
#         user=   "root",
#         password="Rk3@7530",    
#         database="gladiator",
#     )
#     cur = con.cursor()  
#     # Query to get heights and weights from both Marvel and DC
#     query = """
#         SELECT height, weight FROM marvel
#         UNION ALL
#         SELECT height, weight FROM dc
#     """
#     cur.execute(query)
#     results = cur.fetchall()
#     # Close the connection
#     con.close()
#     # Calculate mean for heights and weights
#     heights = [row[0] for row in results]
#     weights = [row[1] for row in results]
#     def calculate_mean(data):
#         return sum(data) / len(data) if data else 0
#     mean_height = calculate_mean(heights)
#     mean_weight = calculate_mean(weights)   
    
#     def calculate_deviation(data, mean):
#         return [x - mean for x in data]
#     def calculate_stddev(data, mean):
#         deviations = calculate_deviation(data, mean)
#         variance = sum(d ** 2 for d in deviations) / len(data) if data else 0
#         return variance ** 0.5
#     # Calculate deviation and standard deviation for heights and weights
#     height_deviation = [round(x, 2) for x in calculate_deviation(heights, mean_height)]
#     weight_deviation = [round(x, 2) for x in calculate_deviation(weights, mean_weight)]
#     height_stddev = calculate_stddev(heights, mean_height)
#     weight_stddev = calculate_stddev(weights, mean_weight)
#     return {
#         "height_deviation": height_deviation,
#         "weight_deviation": weight_deviation,
#         "height_stddev": height_stddev,
#         "weight_stddev": weight_stddev
#     }   
# def display_deviation_and_stddev(stats):
#     print(f"{'Statistic':<20} {'Value':<10}")
#     print("-" * 30)
#     print(f"{'Height Deviation':<20} {stats['height_deviation']}")
#     print(f"{'Weight Deviation':<20} {stats['weight_deviation']}")
#     print(f"{'Height Std Dev':<20} {stats['height_stddev']:<10}")
#     print(f"{'Weight Std Dev':<20} {stats['weight_stddev']:<10}")

# if __name__ == "__main__":
#     stats = calculate_deviation_and_stddev()
#     display_deviation_and_stddev(stats) 

# This code connects to a MySQL database to retrieve the heights and weights of stars from both Marvel and DC teams.
# It calculates the deviation and standard deviation for each of these attributes and displays the results.
# The deviation shows how much each value differs from the mean, while the standard deviation provides a measure of the spread of the data.
# These statistics are useful for understanding the variability in the data, which can help in identifying trends

#3. 
"""Perform the necessary operation to find linear regression model of effect of 
weight on games played (take games played as y and weight as x)."""
import mysql.connector
def linear_regression_weight_games():
    # Connect to the database
    con = mysql.connector.connect(
        host="localhost",
        user=   "root",
        password="Rk3@7530",
        database="gladiator",
    )
    cur = con.cursor()
    # Query to get weights and games played from both Marvel and DC
    query = """
        SELECT weight, games_played FROM marvel
        UNION ALL
        SELECT weight, games_played FROM dc

    """
    cur.execute(query)  
    results = cur.fetchall()
    # Close the connection
    con.close()
    # Extract weights and games played
    weights = [row[0] for row in results]   
    games_played = [row[1] for row in results]
    # Calculate means
    mean_weight = sum(weights) / len(weights) if weights else 0
    mean_games_played = sum(games_played) / len(games_played) if games_played else 0
    # Calculate covariance and variance
    covariance = sum((weights[i] - mean_weight) * (games_played[i] - mean_games_played) for i in range(len(weights))) / len(weights) if weights else 0
    variance_weight = sum((weights[i] - mean_weight) ** 2 for i in range(len(weights))) / len(weights) if weights else 0
    # Calculate slope (m) and intercept (b) for the linear regression line  
    slope = covariance / variance_weight if variance_weight != 0 else 0
    intercept = mean_games_played - slope * mean_weight 
    return {
        "slope": slope,
        "intercept": intercept,
        "mean_weight": mean_weight,
        "mean_games_played": mean_games_played
    }   
def display_linear_regression(stats):
    print(f"{'Statistic':<20} {'Value':<10}")
    print("-" * 30)
    print(f"{'Slope (m)':<20} {stats['slope']:<10}")
    print(f"{'Intercept (b)':<20} {stats['intercept']:<10}")
    print(f"{'Mean Weight':<20} {stats['mean_weight']:<10}")
    print(f"{'Mean Games Played':<20} {stats['mean_games_played']:<10}")

if __name__ == "__main__":
    stats = linear_regression_weight_games()
    display_linear_regression(stats)
# This code connects to a MySQL database to retrieve the weights and games played of stars from both Marvel and DC teams.
# It calculates the slope and intercept for a linear regression model that predicts games played based on weight
# using the formula y = mx + b, where m is the slope and b is the intercept.
# The slope indicates how much the games played change for each unit increase in weight, while the intercept represents the expected games played when weight is zero.
# This model can be useful for understanding the relationship between weight and performance in terms of games played.  


