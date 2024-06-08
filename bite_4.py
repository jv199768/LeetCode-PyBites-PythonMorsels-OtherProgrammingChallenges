import os
import urllib.request
import re
from collections import Counter

# prep
temp_file = os.path.join("feed")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/feed",
    temp_file
)

with open(temp_file) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags():
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tags = re.findall("<category>(.*?)</category>", content)
    return Counter(tags).most_common(10)
