######## Lab 1 ########

import requests
url = "https://reqres.in/api/users"

response = requests.get(url)
if 199 < response.status_code <300 :
    print("Request was successful")
    # print(response.headers)
    data = response.json()
    users = data["data"]
    print(type(users))
    path = input('please enter the file name or path ')
    with open(path,'w+') as file:
        for user in users: # iteration on a list of dic [{},{},{}.....{}]
            # print(user)
            file.write(f'{"*"*20} {user["id"]} {"*"*20} \n')
            for k,v in user.items() : # iteration over a dict items [key.value),(),]
                if k == "id":
                    continue
                file.write(f"{v} \n",)
    print("all the data in the file go check for yourself",path)
else:
        print(f"Request was not successful status code {response.status_code}")


######## Lab 2 ########
import requests
import csv
import sys

def fetch_random_users(count=10):
    """
    Fetch random user data from the randomuser.me API
    
    Args:
        count (int): Number of random users to fetch
    
    Returns:
        dict: JSON response from the API or None if request failed
    """
    url = f"https://randomuser.me/api/?results={count}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_users_to_csv(users_data, filename="random_users.csv"):
    """
    Save user data to a CSV file
    
    Args:
        users_data (dict): The API response containing user data
        filename (str): The name of the CSV file to create
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Define CSV headers
            fieldnames = ['First Name', 'Last Name', 'Email', 'Gender', 'Country', 'Age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write headers
            writer.writeheader()
            
            # Write user data rows
            for user in users_data['results']:
                writer.writerow({
                    'First Name': user['name']['first'],
                    'Last Name': user['name']['last'],
                    'Email': user['email'],
                    'Gender': user['gender'],
                    'Country': user['location']['country'],
                    'Age': user['dob']['age']
                })
        
        print(f"Successfully saved {len(users_data['results'])} users to {filename}")
        return True
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
        return False

def main():
    # Get user count from command line argument or use default
    try:
        if len(sys.argv) > 1:
            count = int(sys.argv[1])
            if count < 1:
                raise ValueError("Number of users must be at least 1")
        else:
            count = 10  # Default
    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Using default value of 10 users")
        count = 10
    
    print(f"Fetching {count} random users...")
    
    # Fetch data from API
    users_data = fetch_random_users(count)
    
    # If data was successfully fetched, save it to a CSV file
    if users_data:
        save_users_to_csv(users_data)
    else:
        print("Failed to fetch random user data.")

if __name__ == "__main__":
    main()


######## Lab 3 ########
import requests
import csv

def fetch_population_data():
    """
    Fetch US population data from the datausa.io API
    
    Returns:
        dict: JSON response from the API or None if request failed
    """
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def calculate_percentage_change(current, previous):
    """
    Calculate percentage change between two values
    
    Args:
        current (float): Current value
        previous (float): Previous value
    
    Returns:
        float: Percentage change
    """
    if previous == 0:
        return 0  # Avoid division by zero
    return ((current - previous) / previous) * 100

def process_population_data(pop_data):
    """
    Process population data and calculate year-over-year changes
    
    Args:
        pop_data (dict): The API response containing population data
    
    Returns:
        list: Processed data with years, population, and percentage changes
    """
    # Sort data by year (ascending)
    sorted_data = sorted(pop_data['data'], key=lambda x: x['Year'])
    
    # Process data to calculate year-over-year percentage changes
    processed_data = []
    
    for i, year_data in enumerate(sorted_data):
        year = year_data['Year']
        population = year_data['Population']
        
        if i > 0:
            # Calculate percentage change from previous year
            prev_population = sorted_data[i-1]['Population']
            pct_change = calculate_percentage_change(population, prev_population)
        else:
            # No previous year for the first entry
            pct_change = None
        
        processed_data.append({
            'Year': year,
            'Population': population,
            'Percentage Change': pct_change
        })
    
    return processed_data

def save_to_csv(data, filename="us_population.csv"):
    """
    Save population data to a CSV file
    
    Args:
        data (list): Processed population data
        filename (str): The name of the CSV file to create
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w', newline='') as csvfile:
            # Define CSV headers
            fieldnames = ['Year', 'Population', 'Percentage Change']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write headers
            writer.writeheader()
            
            # Write data rows
            for row in data:
                writer.writerow(row)
        
        print(f"Successfully saved population data to {filename}")
        return True
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
        return False

def create_summary_file(data, filename="population_summary.txt"):
    """
    Create a summary file with population statistics
    
    Args:
        data (list): Processed population data
        filename (str): The name of the summary file to create
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Get first and last year data
        first_year_data = data[0]
        last_year_data = data[-1]
        
        # Calculate total population change
        total_pct_change = calculate_percentage_change(
            last_year_data['Population'], 
            first_year_data['Population']
        )
        
        with open(filename, 'w') as file:
            file.write("US POPULATION DATA SUMMARY\n")
            file.write("==========================\n\n")
            
            # Write time period
            file.write(f"Period: {first_year_data['Year']} to {last_year_data['Year']}\n\n")
            
            # Write first year data
            file.write(f"First year ({first_year_data['Year']}):\n")
            file.write(f"  Population: {first_year_data['Population']:,}\n\n")
            
            # Write last year data
            file.write(f"Last year ({last_year_data['Year']}):\n")
            file.write(f"  Population: {last_year_data['Population']:,}\n\n")
            
            # Write total change
            file.write("Total change over the entire period:\n")
            file.write(f"  Absolute change: {last_year_data['Population'] - first_year_data['Population']:,}\n")
            file.write(f"  Percentage change: {total_pct_change:.2f}%\n")
        
        print(f"Successfully created summary file: {filename}")
        return True
    except Exception as e:
        print(f"Error creating summary file: {e}")
        return False

def main():
    # Fetch data from API
    pop_data = fetch_population_data()
    
    if not pop_data:
        print("Failed to fetch population data.")
        return
    
    # Process the data
    processed_data = process_population_data(pop_data)
    
    # Save data to CSV
    save_to_csv(processed_data)
    
    # Create summary file
    create_summary_file(processed_data)

if __name__ == "__main__":
    main()

######## challenge 1 ########
import requests
import csv
import json
import datetime
import os
from collections import Counter

# Create a logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)
os.makedirs('raw_data', exist_ok=True)

# Initialize the log file
def init_log_file(filename="logs/api_requests.log"):
    """Create or clear the log file"""
    with open(filename, 'w') as log_file:
        log_file.write("API REQUEST LOG\n")
        log_file.write("==============\n\n")
    return filename

# Log an API request
def log_request(api_name, status, message, log_filename="logs/api_requests.log"):
    """Log an API request with timestamp, status, and message"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_filename, 'a') as log_file:
        log_file.write(f"[{timestamp}] {api_name}: {status} - {message}\n")

# Fetch data from an API
def fetch_api_data(api_name, url):
    """
    Fetch data from an API and log the request
    
    Args:
        api_name (str): Name of the API for logging
        url (str): URL to fetch data from
    
    Returns:
        dict: JSON response from the API or None if request failed
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Log success
        log_request(api_name, "SUCCESS", f"Retrieved {len(json.dumps(data))} bytes of data")
        
        # Save raw data
        with open(f"raw_data/{api_name.lower().replace(' ', '_')}_raw.txt", 'w') as file:
            json.dump(data, file, indent=2)
        
        return data
    except requests.exceptions.RequestException as e:
        # Log failure
        log_request(api_name, "FAILURE", str(e))
        return None

# Function to fetch data from all three APIs
def fetch_all_apis():
    """
    Fetch data from all three APIs
    
    Returns:
        dict: Dictionary containing data from all three APIs
    """
    apis = {
        "ReqRes Users": "https://reqres.in/api/users",
        "Random Users": "https://randomuser.me/api/?results=5",
        "US Population": "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    }
    
    results = {}
    
    for api_name, url in apis.items():
        print(f"Fetching data from {api_name}...")
        data = fetch_api_data(api_name, url)
        results[api_name] = data
    
    return results

# Process ReqRes users data
def process_reqres_data(data):
    """
    Process ReqRes users data
    
    Args:
        data (dict): ReqRes API response
    
    Returns:
        dict: Processed data with user count and first/last user info
    """
    if not data:
        return {
            "user_count": 0,
            "first_user": None,
            "last_user": None
        }
    
    users = data.get('data', [])
    
    return {
        "user_count": len(users),
        "first_user": users[0] if users else None,
        "last_user": users[-1] if users else None
    }

# Process Random users data
def process_random_users(data):
    """
    Process Random users data
    
    Args:
        data (dict): Random Users API response
    
    Returns:
        dict: Processed data with country and gender counts
    """
    if not data:
        return {
            "users": [],
            "countries": Counter(),
            "genders": Counter()
        }
    
    users = data.get('results', [])
    
    countries = Counter()
    genders = Counter()
    
    for user in users:
        countries[user['location']['country']] += 1
        genders[user['gender']] += 1
    
    return {
        "users": users,
        "countries": countries,
        "genders": genders
    }

# Process US Population data
def process_population_data(data):
    """
    Process US Population data
    
    Args:
        data (dict): US Population API response
    
    Returns:
        dict: Processed data with most recent year and population
    """
    if not data:
        return {
            "most_recent_year": None,
            "most_recent_population": None,
            "years": []
        }
    
    # Sort data by year (descending)
    years_data = sorted(data.get('data', []), key=lambda x: x['Year'], reverse=True)
    
    if not years_data:
        return {
            "most_recent_year": None,
            "most_recent_population": None,
            "years": []
        }
    
    # Get most recent year's data
    most_recent = years_data[0]
    
    return {
        "most_recent_year": most_recent['Year'],
        "most_recent_population": most_recent['Population'],
        "years": years_data
    }

# Create the summary CSV file
def create_summary_csv(api_data, filename="summary.csv"):
    """
    Create a summary CSV file with data from all three APIs
    
    Args:
        api_data (dict): Dictionary containing data from all three APIs
        filename (str): The name of the CSV file to create
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Process data from each API
        reqres_processed = process_reqres_data(api_data.get("ReqRes Users"))
        random_users_processed = process_random_users(api_data.get("Random Users"))
        population_processed = process_population_data(api_data.get("US Population"))
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            writer.writerow(["API Data Summary"])
            writer.writerow(["Generated on", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
            writer.writerow([])
            
            # ReqRes Users section
            writer.writerow(["REQRES USERS"])
            writer.writerow(["Total Users", reqres_processed["user_count"]])
            
            if reqres_processed["first_user"]:
                first_user = reqres_processed["first_user"]
                writer.writerow(["First User", f"{first_user['first_name']} {first_user['last_name']} ({first_user['email']})"])
            
            if reqres_processed["last_user"]:
                last_user = reqres_processed["last_user"]
                writer.writerow(["Last User", f"{last_user['first_name']} {last_user['last_name']} ({last_user['email']})"])
            
            writer.writerow([])
            
            # Random Users section
            writer.writerow(["RANDOM USERS"])
            writer.writerow(["Countries"])
            for country, count in random_users_processed["countries"].items():
                writer.writerow(["", country, count])
            
            writer.writerow(["Genders"])
            for gender, count in random_users_processed["genders"].items():
                writer.writerow(["", gender.capitalize(), count])
            
            writer.writerow([])
            
            # US Population section
            writer.writerow(["US POPULATION"])
            if population_processed["most_recent_year"]:
                writer.writerow(["Most Recent Year", population_processed["most_recent_year"]])
                writer.writerow(["Population", f"{population_processed['most_recent_population']:,}"])
            else:
                writer.writerow(["Data", "Not available"])
        
        print(f"Successfully created summary file: {filename}")
        return True
    except Exception as e:
        print(f"Error creating summary file: {e}")
        log_request("Summary CSV", "FAILURE", f"Error creating summary: {e}")
        return False

def main():
    # Initialize log file
    log_filename = init_log_file()
    print(f"Initialized log file: {log_filename}")
    
    # Fetch data from all APIs
    api_data = fetch_all_apis()
    
    # Create summary CSV
    create_summary_csv(api_data)
    
    print("Data processing complete!")

if __name__ == "__main__":
    main()


######## challenge 2 ########
import requests
import csv
import json
import concurrent.futures
import argparse
import os
import statistics
from collections import Counter
import re
import time

# Create directories for our data
os.makedirs('cache', exist_ok=True)
os.makedirs('csv_output', exist_ok=True)
os.makedirs('raw_json', exist_ok=True)

def parse_args():
    """
    Parse command-line arguments
    
    Returns:
        Namespace: The parsed arguments
    """
    parser = argparse.ArgumentParser(description='Fetch and compare random user data by nationality')
    parser.add_argument(
        'nationalities', 
        nargs='*', 
        default=['us', 'gb', 'fr'],
        help='List of nationalities to fetch (default: us gb fr)'
    )
    parser.add_argument(
        '--count', 
        type=int, 
        default=20,
        help='Number of users to fetch per nationality (default: 20)'
    )
    parser.add_argument(
        '--save-json', 
        action='store_true',
        help='Save raw JSON responses'
    )
    parser.add_argument(
        '--no-cache', 
        action='store_true',
        help='Disable caching (always fetch new data)'
    )
    
    return parser.parse_args()

def get_cache_path(nationality, count):
    """
    Get the path to a cached response
    
    Args:
        nationality (str): The nationality code
        count (int): The number of users
    
    Returns:
        str: The cache file path
    """
    return f"cache/{nationality}_{count}.json"

def load_from_cache(nationality, count):
    """
    Load data from cache if available
    
    Args:
        nationality (str): The nationality code
        count (int): The number of users
    
    Returns:
        dict: The cached data or None if not available
    """
    cache_path = get_cache_path(nationality, count)
    
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading cache: {e}")
    
    return None

def save_to_cache(nationality, count, data):
    """
    Save data to cache
    
    Args:
        nationality (str): The nationality code
        count (int): The number of users
        data (dict): The data to cache
    """
    cache_path = get_cache_path(nationality, count)
    
    try:
        with open(cache_path, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error saving to cache: {e}")

def fetch_users(nationality, count, no_cache=False):
    """
    Fetch random users for a specific nationality
    
    Args:
        nationality (str): The nationality code
        count (int): The number of users to fetch
        no_cache (bool): Whether to bypass cache
    
    Returns:
        dict: The API response or None if request failed
    """
    # Check cache first (unless no_cache is True)
    if not no_cache:
        cached_data = load_from_cache(nationality, count)
        if cached_data:
            print(f"Loading {nationality} data from cache...")
            return cached_data
    
    url = f"https://randomuser.me/api/?nat={nationality}&results={count}"
    print(f"Fetching {count} users with nationality {nationality}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Save to cache for future use
        if not no_cache:
            save_to_cache(nationality, count, data)
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {nationality} data: {e}")
        return None

def save_raw_json(data, nationality, count):
    """
    Save raw JSON response
    
    Args:
        data (dict): The API response
        nationality (str): The nationality code
        count (int): The number of users
    """
    if not data:
        return
    
    filename = f"raw_json/{nationality}_{count}.json"
    
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving raw JSON: {e}")

def create_csv_for_nationality(data, nationality):
    """
    Create a CSV file for a specific nationality
    
    Args:
        data (dict): The API response
        nationality (str): The nationality code
    
    Returns:
        list: The processed user data
    """
    if not data or 'results' not in data:
        print(f"No data available for {nationality}")
        return []
    
    users = data['results']
    filename = f"csv_output/{nationality}_users.csv"
    
    processed_users = []
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Gender', 'Age', 'Email', 'Nationality']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for user in users:
                full_name = f"{user['name']['first']} {user['name']['last']}"
                processed_user = {
                    'Name': full_name,
                    'Gender': user['gender'],
                    'Age': user['dob']['age'],
                    'Email': user['email'],
                    'Nationality': nationality.upper()
                }
                
                writer.writerow(processed_user)
                processed_users.append(processed_user)
        
        print(f"Created CSV for {nationality} with {len(users)} users")
    except Exception as e:
        print(f"Error creating CSV for {nationality}: {e}")
    
    return processed_users

def create_master_csv(all_users):
    """
    Create a master CSV with all users
    
    Args:
        all_users (list): List of all processed users
    """
    if not all_users:
        print("No users available for master CSV")
        return
    
    filename = "csv_output/master_users.csv"
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Gender', 'Age', 'Email', 'Nationality']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for user in all_users:
                writer.writerow(user)
        
        print(f"Created master CSV with {len(all_users)} users")
    except Exception as e:
        print(f"Error creating master CSV: {e}")

def extract_email_domain(email):
    """
    Extract domain from email address
    
    Args:
        email (str): Email address
    
    Returns:
        str: Domain part of the email
    """
    match = re.search(r'@([^@]+)$', email)
    if match:
        return match.group(1)
    return "unknown"

def main():
    """
    Main function to run the nationality comparison
    """
    # Parse command-line arguments
    args = parse_args()
    
    nationalities = args.nationalities
    count = args.count
    save_json = args.save_json
    no_cache = args.no_cache
    
    print(f"Comparing data for nationalities: {', '.join(nationalities)}")
    print(f"Users per nationality: {count}")
    
    # Fetch user data for each nationality concurrently
    all_users = []
    users_by_nationality = {}
    
    # Using concurrent.futures to make parallel API requests
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Create a mapping of futures to nationalities
        future_to_nat = {
            executor.submit(fetch_users, nat, count, no_cache): nat
            for nat in nationalities
        }
        
        # Process the results as they complete
        for future in concurrent.futures.as_completed(future_to_nat):
            nat = future_to_nat[future]
            try:
                data = future.result()
                
                # Save raw JSON if requested
                if save_json and data:
                    save_raw_json(data, nat, count)
                
                # Create CSV for this nationality
                processed_users = create_csv_for_nationality(data, nat)
                users_by_nationality[nat] = processed_users
                all_users.extend(processed_users)
            except Exception as e:
                print(f"Error processing {nat}: {e}")
    
    # Create the master CSV with all users
    create_master_csv(all_users)
    
    # Create the comparison analysis file
    create_comparison_file(users_by_nationality)
    
    print("\nProcessing complete!")


def create_comparison_file(users_by_nationality):
    """
    Create a comparison file analyzing differences between nationalities
    
    Args:
        users_by_nationality (dict): Dictionary mapping nationalities to user lists
    """
    if not users_by_nationality:
        print("No data available for comparison")
        return
    
    filename = "comparison.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("NATIONALITY COMPARISON ANALYSIS\n")
            f.write("==============================\n\n")
            
            # Gender distribution
            f.write("GENDER DISTRIBUTION\n")
            f.write("-----------------\n")
            
            for nat, users in users_by_nationality.items():
                if not users:
                    f.write(f"{nat.upper()}: No data available\n")
                    continue
                
                gender_counts = Counter(user['Gender'] for user in users)
                total = len(users)
                
                f.write(f"{nat.upper()} (Total: {total}):\n")
                for gender, count in gender_counts.items():
                    percentage = (count / total) * 100
                    f.write(f"  {gender.capitalize()}: {count} ({percentage:.1f}%)\n")
                f.write("\n")
            
            # Age statistics
            f.write("\nAGE STATISTICS\n")
            f.write("-------------\n")
            
            for nat, users in users_by_nationality.items():
                if not users:
                    f.write(f"{nat.upper()}: No data available\n")
                    continue
                
                ages = [user['Age'] for user in users]
                
                f.write(f"{nat.upper()}:\n")
                f.write(f"  Minimum Age: {min(ages)}\n")
                f.write(f"  Maximum Age: {max(ages)}\n")
                f.write(f"  Average Age: {statistics.mean(ages):.1f}\n")
                f.write(f"  Median Age: {statistics.median(ages)}\n")
                if len(ages) > 1:
                    f.write(f"  Standard Deviation: {statistics.stdev(ages):.2f}\n")
                f.write("\n")
            
            # Email domain frequency
            f.write("\nEMAIL DOMAIN FREQUENCY\n")
            f.write("---------------------\n")
            
            for nat, users in users_by_nationality.items():
                if not users:
                    f.write(f"{nat.upper()}: No data available\n")
                    continue
                
                domains = [extract_email_domain(user['Email']) for user in users]
                domain_counts = Counter(domains)
                
                f.write(f"{nat.upper()} top domains:\n")
                for domain, count in domain_counts.most_common(5):
                    percentage = (count / len(users)) * 100
                    f.write(f"  {domain}: {count} ({percentage:.1f}%)\n")
                f.write("\n")
        
        print(f"Created comparison file: {filename}")
    except Exception as e:
        print(f"Error creating comparison file: {e}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")