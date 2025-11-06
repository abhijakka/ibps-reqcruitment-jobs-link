import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import warnings
import urllib3

# Suppress SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_ibps_jobs():
    # URL of IBPS recruitment page
    url = "https://www.ibps.in/index.php/recruitment/"
    print(f"Fetching job listings from: {url}")
    
    try:
        # Send HTTP request with SSL verification disabled (use with caution)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Lists to store job information
        jobs = []
        
        # Find job listings using the specified class names
        job_entries = soup.find_all('div', class_='detail-first-heading')
        print(f"Found {len(job_entries)} job entries")
        
        for entry in job_entries:
            try:
                # Get job title from detail-first-heading # Title of job
                title = entry.text.strip()
                print(f"Processing job: {title}")
                
                # Get job details from the next detail-second-heading # Details of job
                details_div = entry.find_next('div', class_='detail-second-heading')
                job_details = details_div.text.strip() if details_div else "No details available"
                
                # Get post date from detail-heading # Date of job start and end
                date_div = entry.find_next('div', class_='detail-heading')
                post_date = date_div.text.strip() if date_div else datetime.now().strftime("%Y-%m-%d")
                
                post_date1 = post_date[0:10]
                end_date = post_date[10:]

                # Get link (assuming it's in a parent or nearby element) # Link of job
                link_tag = entry.find_parent('a') or entry.find_next('a')
                link = link_tag['href'] if link_tag and link_tag.get('href') else ''
                if link and not link.startswith('http'):
                    link = 'https://www.ibps.in' + link
                
                # Location is typically Pan India for IBPS positions # Location of job
                location = "Pan India"
                
                # Append job details to list
                jobs.append({
                    'Job Title': title,
                    'Job Details': job_details,
                    'Location': location,
                    'Post Date': post_date1,
                    'End Date': end_date,
                    'Link': link
                })
                
            except AttributeError as e:
                print(f"Error extracting job details: {e}")
                continue
        
        if not jobs:
            print("No jobs found on the page")
            return None
            
        # Convert to DataFrame
        df = pd.DataFrame(jobs)
        
        # Save to CSV
        filename = f'ibps_jobs_{datetime.now().strftime("%Y%m%d")}.csv'
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Successfully saved {len(jobs)} jobs to {filename}")
        
        return df
        
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    print("Starting IBPS job scraping...")
    jobs_df = scrape_ibps_jobs()
    if jobs_df is not None and not jobs_df.empty:
        print("\nSample of scraped jobs:")
        print(jobs_df.head())
    else:
        print("No jobs were found or an error occurred.")
