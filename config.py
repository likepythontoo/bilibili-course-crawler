# Configuration settings for the Bilibili Course Crawler

# Course types to scrape
COURSE_TYPES = [
    'Live',  # Live courses
    'Recorded',  # Recorded courses
]

# Request parameters
REQUEST_PARAMS = {
    'page_size': 20,  # Number of results per page
    'sort_by': 'popularity',  # Sort by popularity or date
}

# Output settings
OUTPUT_SETTINGS = {
    'output_format': 'json',  # Output format can be json or csv
    'output_directory': 'output/',  # Directory where output files will be saved
}
