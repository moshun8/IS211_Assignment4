#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 4 Sort Compare"""


import time
import random


def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end = time.time()
    timetaken = end - start
    return timetaken


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    timetaken = end - start
    return timetaken


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    timetaken = end - start
    return timetaken


def main():

    intime500 = 0.0
    intime1000 = 0.0
    intime10000 = 0.0

    shelltime500 = 0.0
    shelltime1000 = 0.0
    shelltime10000 = 0.0

    pytime500 = 0.0
    pytime1000 = 0.0
    pytime10000 = 0.0

    for i in xrange(100):
        lst500 = [int(100*random.random()) for i in xrange(500)]
        lst1000 = [int(100*random.random()) for i in xrange(1000)]
        lst10000 = [int(100*random.random()) for i in xrange(10000)]
        
        in500 = insertion_sort(lst500)
        intime500 += in500
        inavg500 = intime500 / 100

        in1000 = insertion_sort(lst1000)
        intime1000 += in1000
        inavg1000 = intime1000 / 100

        in10000 = insertion_sort(lst10000)
        intime10000 += in10000
        inavg10000 = intime10000 / 100

        shell500 = shell_sort(lst500)
        shelltime500 += shell500
        shellavg500 = shelltime500 / 100

        shell1000 = shell_sort(lst1000)
        shelltime1000 += shell1000
        shellavg1000 = shelltime1000 / 100

        shell10000 = shell_sort(lst10000)
        shelltime10000 += shell10000
        shellavg10000 = shelltime10000 / 100

        py500 = python_sort(lst500)
        pytime500 += py500
        pyavg500 = pytime500 / 100

        py1000 = python_sort(lst1000)
        pytime1000 += py1000
        pyavg1000 = pytime1000 / 100

        py10000 = python_sort(lst10000)
        pytime10000 += py10000
        pyavg10000 = pytime10000 / 100

    print "Insertion Sort took {:.7f}".format(inavg500),
    print "seconds to run, on average over 500 times"
    print "Insertion Sort took {:.7f}".format(inavg1000),
    print "seconds to run, on average over 1,000 times"
    print "Insertion Sort took {:.7f}".format(inavg10000),
    print "seconds to run, on average over 10,000 times"

    print "Shell Sort took {:.7f}".format(shellavg500),
    print "seconds to run, on average over 500 times"
    print "Shell Sort took {:.7f}".format(shellavg1000),
    print "seconds to run, on average over 1,000 times"
    print "Shell Sort took {:.7f}".format(shellavg10000),
    print "seconds to run, on average over 10,000 times"

    print "Python Sort took {:.7f}".format(pyavg500),
    print "seconds to run, on average over 500 times"
    print "Python Sort took {:.7f}".format(pyavg1000),
    print "seconds to run, on average over 1,000 times"
    print "Python Sort took {:.7f}".format(pyavg10000),
    print "seconds to run, on average over 10,000 times"


if __name__ == "__main__":
    main()