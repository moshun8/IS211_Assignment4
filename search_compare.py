#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 4 Search Compare"""


import random
import time


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    end = time.time()
    timetaken = end - start
    return (found, timetaken)


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
    else:
        pos = pos + 1

    end = time.time()
    timetaken = end - start

    return (found, timetaken)


def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    timetaken = end - start

    return (found, timetaken)


def binary_search_recursive(a_list, item):
    start = time.time()
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                end = time.time()
                timetaken = end - start
                return (binary_search_recursive(a_list[:midpoint], item),
                    timetaken)
            else:
                end = time.time()
                timetaken = end - start
                return (binary_search_recursive(a_list[midpoint + 1], item),
                    timetaken)


def main():

    seqtime500 = 0.0
    seqtime1000 = 0.0
    seqtime10000 = 0.0

    orseqtime500 = 0.0
    orseqtime1000 = 0.0
    orseqtime10000 = 0.0

    biit_time500 = 0.0
    biit_time1000 = 0.0
    biit_time10000 = 0.0

    bire_time500 = 0.0
    bire_time1000 = 0.0
    bire_time10000 = 0.0

    for i in xrange(100):
        lst500 = [int(100*random.random()) for i in xrange(500)]
        lst1000 = [int(100*random.random()) for i in xrange(1000)]
        lst10000 = [int(100*random.random()) for i in xrange(10000)]

        seq500 = sequential_search(lst500, -1)
        seqtime500 += seq500[1]
        seqavg500 = seqtime500 / 100

        seq1000 = sequential_search(lst1000, -1)
        seqtime1000 += seq1000[1]
        seqavg1000 = seqtime1000 / 100

        seq10000 = sequential_search(lst10000, -1)
        seqtime10000 += seq10000[1]
        seqavg10000 = seqtime10000 / 100

        lst500.sort()
        lst1000.sort()
        lst10000.sort()

        orseq500 = ordered_sequential_search(lst500, -1)
        orseqtime500 += orseq500[1]
        orseqavg500 = orseqtime500 / 100

        orseq1000 = ordered_sequential_search(lst1000, -1)
        orseqtime1000 += orseq1000[1]
        orseqavg1000 = orseqtime1000 / 100

        orseq10000 = ordered_sequential_search(lst10000, -1)
        orseqtime10000 += orseq10000[1]
        orseqavg10000 = orseqtime10000 / 100

        biit500 = binary_search_iterative(lst500, -1)
        biit_time500 += biit500[1]
        biitavg500 = biit_time500 / 100

        biit1000 = binary_search_iterative(lst1000, -1)
        biit_time1000 += biit1000[1]
        biitavg1000 = biit_time1000 / 100

        biit10000 = binary_search_iterative(lst10000, -1)
        biit_time10000 += biit10000[1]
        biitavg10000 = biit_time10000 / 100

        bire500 = binary_search_recursive(lst500, -1)
        bire_time500 += bire500[1]
        bireavg500 = bire_time500 / 100

        bire1000 = binary_search_recursive(lst1000, -1)
        bire_time1000 += bire1000[1]
        bireavg1000 = bire_time1000 / 100

        bire10000 = binary_search_recursive(lst10000, -1)
        bire_time10000 += bire10000[1]
        bireavg10000 = bire_time10000 / 100

    print "Sequential Search took {:.7f}".format(seqavg500),
    print "seconds to run, on average over 500 items"
    print "Sequential Search took {:.7f}".format(seqavg1000),
    print "seconds to run, on average over 1,000 items"
    print "Sequential Search took {:.7f}".format(seqavg10000),
    print "seconds to run, on average over 10,000 items"

    print "Ordered Sequential Search took {:.7f}".format(orseqavg500),
    print "seconds to run, on average over 500 items"
    print "Ordered Sequential Search took {:.7f}".format(orseqavg1000),
    print "seconds to run, on average over 1,000 items"
    print "Ordered Sequential Search took {:.7f}".format(orseqavg10000),
    print "seconds to run, on average over 10,000 items"

    print "Binary Iterative Search took {:.7f}".format(biitavg500),
    print "seconds to run, on average over 500 items"
    print "Binary Iterative Search took {:.7f}".format(biitavg1000),
    print "seconds to run, on average over 1,000 items"
    print "Binary Iterative Search took {:.7f}".format(biitavg10000),
    print "seconds to run, on average over 10,000 items"

    print "Binary Recursive Search took {:.7f}".format(bireavg500),
    print "seconds to run, on average over 500 items"
    print "Binary Recursive Search took {:.7f}".format(bireavg1000),
    print "seconds to run, on average over 1,000 items"
    print "Binary Recursive Search took {:.7f}".format(bireavg10000),
    print "seconds to run, on average over 10,000 items"

if __name__ == "__main__":
    main()