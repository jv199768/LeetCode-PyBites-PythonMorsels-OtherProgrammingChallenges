'''Bite 133. Convert an Amazon URL into an affiliation link
Can you help PyBites automate their Amazon affiliation link creation?

Complete the generate_affiliation_link(url) function below which should convert the following links:

https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art
https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1
https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234
https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X
https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/
'''
def generate_affiliation_link(url, path, query):
    u = urlparse(url)
    print(u._replace(path=path, query=query).geturl())
