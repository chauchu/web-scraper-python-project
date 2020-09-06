import requests
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup
import tldextract

# initialize the set of links (unique links)
same_host = set()
same_domain = set()
different_domain = set()

total_urls_visited = 0


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
    urls = set()
    # domain name of the URL without the protocol
    domain_name = tldextract.extract(url).domain + '.' + tldextract.extract(url).suffix
    host_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        href1 = tldextract.extract(href)
        try:
            if not is_valid(href):
                # not a valid URL
                continue
            if href in same_host:
                # already in the set
                continue
            if domain_name != (href1.domain + '.' + href1.suffix):
                # different domain
                if href not in different_domain:
                    different_domain.add(href)
                continue
            if host_name != parsed_href.netloc:
                # same domain
                if href not in same_domain:
                    same_domain.add(href)
                continue
            urls.add(href)
            same_host.add(href)
        except:
            break
    return urls


def crawl(url, max_urls=50):
    """
    Crawls a web page and extracts all links.
    params:
        max_urls (int): number of max urls to crawl, default is 30.
    """
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Link Extractor Tool with Python")
    parser.add_argument("url", help="The URL to extract links from.")
    parser.add_argument("-m", "--max-urls", help="Number of max URLs to crawl, default is 30.", default=30, type=int)

    args = parser.parse_args()
    url = args.url
    max_urls = args.max_urls
    crawl(url, max_urls)
    extract = tldextract.extract(url)

    #print the output: TLD, Domain, Hostname, Path, Links
    print('TLD: ' + extract.suffix)
    if extract.subdomain == '':
        print('Domain: ' + urlparse(url).netloc)
    else:
        print('Domain: ' + extract.domain + '.' + extract.suffix)
    print('Hostname: ' + urlparse(url).netloc)
    print('Path: ' + urlparse(url).path)
    print('LINKS:')
    print('\t' + "Same hostname: ")
    for link in same_host:
        print('\t\t' + link)
    print('\n')
    print('\t' + "Same domain: ")
    for link in same_domain:
        print('\t\t' + link)
    print('\n')
    print('\t' + "Different domain: ")
    for link in different_domain:
        print('\t\t' + link)

    #print("[+] Total:", len(same_host) + len(same_domain) + len(different_domain))




