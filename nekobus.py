#!/usr/bin/python
import urllib2
import requests
from bs4 import BeautifulSoup
import urlparse
from optparse import OptionParser
parser = OptionParser()

parser.add_option(
	"-t", "--target",
	action="store",
	default="None",
	type="string",
	dest="target_url",
	help="target url"
)

#parser.add_option(
#	"-p", "--print_html",
#	action="store_true",
#	default=False,
#	dest="ph",
#	help="print target html"
#)

parser.add_option(
	"-o", "--output",
	action="store",
	dest="output",
	help="--output [html,form,link]"
)

(options, args) = parser.parse_args()
if options.target_url == 'None':
	print "[*]please set target url!"
	exit()

def get_html(url):
	r = requests.get(url)
	html = urllib2.urlopen(url).read()
	return html

def print_html():
	print get_html(options.target_url)

def print_link():
	soup = BeautifulSoup(get_html(options.target_url))
	for link in soup.find_all('a'):
		print(link.get('href'))

def print_header(url):
	html = urllib2.urlopen(url)
	html.info().heders
        
def print_form_tag():
	soup = BeautifulSoup(get_html(options.target_url))
	for inp in soup.find_all('form'):
    		print(str(inp.get('action')) + " " + str(inp.get('method')))

def make_model():
	soup = BeautifulSoup(get_html(options.target_url))
	for inp in soup.find_all():
                print inp.get_text().replace("\n","").replace(" ","")

if options.output == "html":
	print_html()
elif options.output == "link":
	print_link()
elif options.output == "form":	
	print_form_tag()
elif options.output == "make":
        make_model()
else:
	print "[*]please set [form,link,html]"


