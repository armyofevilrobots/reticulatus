"""Test STL"""
from reticulatus.geo.stl import STL
from reticulatus.worker import Worker, IncompleteWork
import os
import unittest
import time



class TestWorker(unittest.TestCase):
    """Test the worker"""

    def test_worker_simple(self):
        """Does a deferred return, and correctly?"""
        worker = Worker(4)
        def func(a, b):
            time.sleep(0.3)
            return (a*b)
        deferred = worker.defer(func, 3, 2)
        print "Deferred is", deferred
        self.assertEquals(worker.get_result(deferred), IncompleteWork)
        self.assertEquals(worker.get_result(deferred, True), 6)
        self.assertEquals(len(worker.workers), 0)


    def test_multiple_workers(self):
        """Test if multiple workers work in parallel and give
        correct results"""
        worker = Worker(4)
        def func(a, b):
            time.sleep(0.3)
            return (a*b)
        start = time.time()
        defs = list()
        for i in range(4):
            defs.append(worker.defer(func, 3, 2))
            print "Got a deferred", defs[-1]
        for i in range(4):
            self.assertEquals(worker.get_result(defs[i], True), 6)
        assert time.time()-start < .5

    def test_map_functional(self):
        """Test if the functional process map works."""
        worker = Worker(4)
        def func(x):
            time.sleep(1)
            return (x*x)
        now = time.time()
        results = worker.map(func, range(10))
        print "Results are", results
        for index in xrange(len(results)):
            self.assertEquals(results[index], index*index)
        assert time.time()-now < 8














