#!/usr/bin/python3

import unittest
import xlsGenerate

#TEST xlsGenerate
class SimpleTestCase(unittest.TestCase):

    def testCreateXls1(self):
        try:
            array = [('test1', 'test2', 'test3'), ('test11', 'test22', 'test33')]
            xlsGenerate.scrapXls(array,"unittest", "unitest1.xls")
            
        except Exception :
            fail("expected a ValueError")
        else :
            pass

    def testCreateXls2(self):
        try:
            array = [('test1', 'test2', 'test3'), ('test11', 'test22', 'test33','test44'),('test111','test222')]
            xlsGenerate.scrapXls(array,"unittest", "unitest2.xls")
            
        except Exception :
            fail("expected a ValueError")
        else :
            pass

    def testCreateXls3(self):
        try:
            array = [('test1',), ('test11',),('test111',)]
            xlsGenerate.scrapXls(array,"unittest", "unitest3.xls")
            
        except Exception :
            fail("expected a ValueError")
        else :
            pass

if __name__ == '__main__':
    unittest.main()
