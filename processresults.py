#Inspired from https://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python

import xml.etree.ElementTree as ET
tree = ET.parse('./bin/junit/TESTS-TestSuites.xml')
root = tree.getroot()

for testcase in root.findall("./testsuite/testcase"):
    if testcase.findall("failure"):
        print "Test: ", testcase.attrib['name'], "Failed", testcase.findall("failure")[0].attrib['message']
    else:
        print "Test: ", testcase.attrib['name'], "Passed"