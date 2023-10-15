# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attribute in attrs:
            print(f"-> {attribute[0]} > {attribute[1]}")

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attribute in attrs:
            print(f"-> {attribute[0]} > {attribute[1]}")

n = int(input())


html_code = []

for _ in range(n):
    html_code.append(input())

html = "\n".join(html_code)

parser = MyHTMLParser()
parser.feed(html)
