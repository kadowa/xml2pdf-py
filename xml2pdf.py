#!/usr/bin/python

import sys, getopt, logging
from weasyprint import HTML, CSS
from lxml import etree

def usage():
	sys.stderr.write("./xml2pdf.py --xml <xml-file> --xsl <xsl-file> -o <pdf-output> [--css <stylesheet>]")

options, rest = getopt.getopt(sys.argv[1:], "o:", ["xml=", "xsl=", "output=","css="])

out_fn = None
xml_fn = None
xsl_fn = None
css_fn = None

for opt, arg in options:
	if opt in ("-o", "--output"):
		out_fn = arg
	elif opt == "--xml":
		xml_fn = arg
	elif opt == "--xsl":
		xsl_fn = arg
	elif opt == "--css":
		css_fn = arg
	else:
		sys.stderr.write("Unknown option %s"%opt)

if not (out_fn and xml_fn and xsl_fn):
	usage()

xsl = etree.parse(xsl_fn)
transformer = etree.XSLT(xsl)

xml = etree.parse(xml_fn)

logging.info
html = transformer(xml)

if css_fn:
	css = [CSS(css_fn)]
else:
	css = None

HTML(tree=html).write_pdf(out_fn, css)
