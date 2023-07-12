from xml.etree import ElementTree

xml = input()
root = ElementTree.fromstring(xml)

weights = {'red': 0, 'green': 0, 'blue': 0}

def get_weights(element, level=1):
    weights[element.attrib['color']] += level
    for child in element:
        get_weights(child, level+1)

get_weights(root)

r, g, b = (
    weights['red'],
    weights['green'],
    weights['blue'],
)

print(r, g, b)