# iPhone Price Analyzer

A Python-based desktop application using PyQt5 that scrapes OLX listings for iPhones, cleans and analyzes pricing data with Pandas, and displays key statistics (average, minimum, maximum, median) for each model in a user-friendly GUI.

* **Data Scraping** - Live data fetched directly from OLX using **requests**
* **Data Analysis** – Processed with **Pandas** for clear and structured model-based price statistics.
* **Data Cleaning** – Filters out irrelevant listings (cases, chargers, accessories, etc.).
* **User Interface** – Desktop GUI (**PyQt5**) allows user to input location and instantly view results.


## Getting Started

No database setup is required. All results are computed in-memory and displayed directly in the app.

1. Clone the Repository

2. Create and Activate a Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```
3. Install Dependencies
``` python
pip install -r requirements.txt
```
4. Run the Application
``` python
python main.py
```
5. How to Use
* Enter a location (e.g. polska, mazowieckie) in the input field.
* Click the "Analyze" button.
* The app will scrape OLX for iPhone listings, clean and filter the data, and display price statistics by model.

## Authors

kacperpszky  

## Version History

* 0.1
    * Initial Release – GUI, scraper, analyzer, and cleaner complete
