import sys

sizeList = int(sys.argv[1])

html = "<ul>\n"
i = 0

while i < sizeList:
    i += 1
    # uso de \t para tabular y \n para salto de linea
    html += "\t<li>Elemento {}</li>\n".format(i)

html += "</ul>"
print(html)