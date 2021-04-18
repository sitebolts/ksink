#Sanitize HTML output
#Example: htmlspecialchars('I love the <b> tag') == 'I love the &lt;b&gt; tag'
def htmlspecialchars(text):
    return text.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")
