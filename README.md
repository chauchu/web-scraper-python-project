# web-scraper-python-project
This is an exercise to practice scraping a website using beautifulsoap4

Exercise requirements:
Given a URL, you need to generate the following:
1.) The Top Level Domain (TLD) of this URL.
2.) The domain of this URL.
3.) The hostname of this URL.
4.) The path of this URL.
5.) All the links (both statically clickable & statically unclickable but dynamically generated) found on the page this URL points to, arranged in the following:
    a.) Links that belong to the same hostname.
    b.) Links that belong to the same domain, but different hostname.
    c.) Links that belong to a different domain.

Eg:

INPUT: yourscript.py http://test.testdomain.org/xyz

OUTPUT:
    TLD: org
    DOMAIN: testdomain.org
    HOSTNAME: test.testdomain.org
    PATH: /xyz
    LINKS:
        Same hostname:
            http://test.testdomain.org/abc
            http://test.testdomain.org/ddff
        Same domain:
            http://test3.testdomain.org/
            http://x.testdomain.org/abc
        Different domain:
            http://ddfgc.com/abc
