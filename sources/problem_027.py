from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    # def parse_starttag(self, i):
    #     print(i)
    def handle_starttag(self, tag, attrs):
        print(tag)
        for item in attrs:
            print("->", item[0], ">", item[1])

if (__name__== '__main__'):
    parser = MyHTMLParser()
    n = int(input())
    result = []
    for i in range(n):
        script = input()
        result.append(parser.feed(script))