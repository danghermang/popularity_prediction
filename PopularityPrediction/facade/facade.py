#!/usr/bin/env python
# -*- coding: utf-8 -*-


from untitled2.facade import class_1,class_2,class_3

class TestRunner:
    def __init__(self):
        self.tc1 = class_1()
        self.tc2 = class_2()
        self.tc3 = class_3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def runAll(self):
        [i.run() for i in self.tests]



if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()

