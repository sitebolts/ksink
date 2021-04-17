from bs4 import BeautifulSoup, Comment, SoupStrainer

#Remove all attributes from every tag (including children) in the given soup
#TODO: Remove some of the unnecessary code in the last line
def recursively_remove_attributes(soup):    
    for tag in soup.recursiveChildGenerator():
        if hasattr(tag, 'attrs'):
            tag.attrs = {key:value for key, value in tag.attrs.items()
                        if False}


def bs4_inner_html(bs4_element):
    if (bs4_element == None):
        return None
    else:
        return bs4_element.decode_contents(formatter="html")
