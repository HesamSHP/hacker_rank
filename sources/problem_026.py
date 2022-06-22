from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if (str(data).count("\n") >= 1):
            print(">>> Multi-line Comment", str(data), sep="\n")
        else:
            print(">>> Single-line Comment", str(data), sep="\n")

    def handle_data(self, data):
        if (str(data).count("\n") >= 1):
            pass
        else:
            print(">>> Data", data, sep="\n")

if (__name__ == "__main__"):
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()