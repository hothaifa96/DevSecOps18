# Python API Request Labs

## Lab 1: Basic API Request and Text File Saving (Easy)
**Requirements:**
1. Make a GET request to https://reqres.in/api/users
2. Extract the user data from the JSON response
3. Save the following information for each user to a text file:
   - User ID
   - First name and last name
   - Email
   - Avatar URL
4. Format the text file with clear separators between users
5. Print a confirmation message when the file is successfully saved

## Lab 2: Random User Data to CSV (Easy)
**Requirements:**
1. Make a GET request to https://randomuser.me/api/?results=10 to fetch 10 random users
2. Extract the user data from the JSON response
3. Create a CSV file with the following columns:
   - First name
   - Last name
   - Email
   - Gender
   - Country
   - Age
4. Write the data for all 10 users to the CSV file
5. Implement error handling for the API request
6. Add a feature to let the user specify how many random users to fetch

## Lab 3: US Population Data Analysis (Medium)
**Requirements:**
1. Fetch US population data from https://datausa.io/api/data?drilldowns=Nation&measures=Population
2. Extract the yearly population figures from the JSON response
3. Create a CSV file with columns for Year and Population
4. Calculate the year-over-year percentage change in population
5. Add this percentage change as a third column in the CSV
6. Create a separate summary text file that includes:
   - The earliest and latest years in the dataset
   - The population values for those years
   - The total population change over the entire period (as a percentage)

## Challenge 1: Multi-API Data Aggregation (Hard)
**Requirements:**
1. Create a script that fetches data from all three APIs:
   - https://reqres.in/api/users
   - https://randomuser.me/api/?results=5
   - https://datausa.io/api/data?drilldowns=Nation&measures=Population
2. For each API, save the raw data to separate text files (with appropriate formatting)
3. Extract relevant information from each API response
4. Create a single "summary.csv" file that includes:
   - A section for ReqRes users (user count and first/last user info)
   - A section for random users (listing countries and gender counts)
   - A section for US population (most recent year and population)
5. Add timestamps to track when each API was accessed
6. Implement comprehensive error handling for all API requests
7. Create a log file that records success/failure for each API request

## Challenge 2: API Data Comparison Challenge 
**Requirements:**
1. Create a script that can:
   - Fetch data from the Random User API for different "nationalities" (e.g., US, GB, FR)
   - Request 20 users from each nationality
   - Make these requests run concurrently to save time
2. Parse the JSON responses for each nationality
3. Create a CSV file for each nationality with consistent columns (name, gender, age, email)
4. Create a "master" CSV file that combines all users from all nationalities
5. Create a "comparison.txt" file that analyzes the differences between nationalities:
   - Gender distribution
   - Age statistics (min, max, average)
   - Email domain frequencies
6. Implement robust error handling that allows partial success (if one API request fails, others continue)
7. Add a caching mechanism to save responses locally and avoid unnecessary API requests
8. Include a command-line interface to specify which nationalities to fetch
9. Add an option to save raw JSON responses alongside the processed CSVs

