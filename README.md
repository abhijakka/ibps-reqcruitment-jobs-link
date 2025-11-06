# ibps-reqcruitment-jobs-link
✅ IBPS Job Scraper (Python)  This project is a Python-based web scraper that extracts public job notifications from the IBPS (Institute of Banking Personnel Selection) official website.  The script scrapes the Recruitment section of the IBPS portal, collects all visible job postings, and saves them into a CSV file for later analysis.

📌 Features

✅ Scrapes Job Title
✅ Scrapes Job Details / Description
✅ Extracts Post Date and End Date
✅ Extracts Direct Link to the Notification
✅ Adds Location (Pan India) by default
✅ Saves all results into a timestamped CSV
✅ Uses BeautifulSoup for scraping
✅ Handles SSL warnings safely
✅ Lightweight and simple to run

🗂 Example Output (CSV Columns)

Job Title

Job Details

Location

Post Date

End Date

Link

🛠 Technologies Used

Python 3

Requests

BeautifulSoup (bs4)

Pandas

Datetime

📥 Installation

Clone the repository:

git clone https://github.com/yourusername/ibps-job-scraper.git
cd ibps-job-scraper


Install dependencies:

pip install -r requirements.txt

▶️ How to Run

Just run:

python scrape_ibps_jobs.py


If successful, it will generate:

ibps_jobs_YYYYMMDD.csv


Example:

ibps_jobs_20251106.csv

📄 Script Explanation

The script:

Requests the HTML from IBPS → Recruitment Page

Parses job blocks using:

.detail-first-heading

.detail-second-heading

.detail-heading

Extracts:

Title

Description

Start/End Dates

Notification Link

Stores data in a DataFrame

Saves to a CSV file

⚠️ Important Notes

IBPS often changes their HTML layout, so scraping may require updates.

Always follow IBPS’s Terms of Use when scraping data.

✅ Future Enhancements (Optional)

Add automatic scheduling (e.g., cron job)

Add Telegram/Email alerts

Add filtering of exams (PO, Clerk, SO, RRB)

Add progress bar using tqdm

Export to Excel

📬 Contact

If you want help improving the script, feel free to open an issue or ask!
