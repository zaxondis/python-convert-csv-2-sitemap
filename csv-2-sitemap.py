from itertools import islice
from lxml import etree, objectify
import csv
import sys
import glob

def main():
        increment = 0
        #path to files goes here
        path = "D:\\Extracts\\PhotoURIs\\*.csv"
        #use glob to iterate thorough the same kind of file in a directory, in this case: *.csv
        for filen in glob.glob(path):
                reader = csv.reader(open(filen, 'r'), delimiter=",")
                increment = increment + 1
                #name the files URI_ and an incremental number depending on how many there are
                smf = "PhotoItemIDsFromML_" + str(increment) + ".xml"
                #sitemap namespace declaration
                NSMAP = {None : "http://www.sitemaps.org/schemas/sitemap/0.9"}
                #root node of the sitemap
                urlset = etree.Element("{http://www.sitemaps.org/schemas/sitemap/0.9}urlset", nsmap=NSMAP)
                for row in reader:
                        #ignore lines in the file that begin with uribase (all my files have one of these rows)
                        if row[0].startswith('uribase'):
                                ()
                        else:
                                url = etree.SubElement(urlset, "{http://www.sitemaps.org/schemas/sitemap/0.9}url")
                                loc = etree.SubElement(url, "{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
                                #write each GUID to a <loc> element in the sitemap
                                loc.text = row[0]

                #create the XML file
                xml = etree.tostring(urlset, pretty_print=True, xml_declaration=True)
                et = etree.ElementTree(urlset)
                et.write(smf, pretty_print=True, xml_declaration=True, encoding="UTF-8")

if __name__ == "__main__":
    main()
