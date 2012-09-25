"""Sooper simple worker class"""

from multiprocessing import cpu_count
import os
import sys
import time
import select
import cPickle

class IncompleteWork:
    """Placeholder for incomplete work."""
    def __init__(self):
        pass
INCOMPLETEWORK = IncompleteWork()


class Worker:
    """Worker that forks of X processes, and each waits for work in the form
    of a process, and returns a cPickled result. This is used instead of
    Multiprocessing since we cannot actually pickle the INPUT data (hence
    forking after generating the input data), but the results are easily
    serializable.
    Strangely; not re-entrant. Don't generate work from separate threads."""
    def __init__(self, workers = None):
        self.worker_count = workers or cpu_count()
        self.workers = {}
        self.results = {}


    def map(self, func, iterable):
        """Like python's map, but using forked processes.
        Note; kinda memory hungry, not optimized to RETURN
        an iterable, just a list. We may change that if needed but:
        http://en.wikipedia.org/wiki/Program_optimization#When_to_optimize
        """
        if self.worker_count == 1:
            #Special case, just use this process
            return map(func, iterable)

        outdata = list()
        mypids = list()

        for param in iterable:
            if isinstance(param, tuple):
                mypids.append(self.defer(func, *param))
            else:
                mypids.append(self.defer(func, param))

        for pid in mypids:
            outdata.append(self.get_result(pid, True))
        return outdata




    def defer(self, func, *args, **kw):
        """Defer to a fork"""
        while len(self.workers) >= self.worker_count:
            #This sucks, but what-evs.
            for pid in self.workers.keys():
                if self.is_ready(pid):
                    self.results[pid] = self.get_result(pid)
            if len(self.workers) >= self.worker_count:
                time.sleep(0.01)

        rpipe, wpipe = os.pipe()
        newpid = os.fork()
        if newpid == 0:
            # This is the new thread!
            wfile = os.fdopen(wpipe, 'w')
            cPickle.dump(func(*args, **kw), wfile)
            wfile.close()
            #Mostly we close these for Nosetests
            sys.stderr.close()
            sys.stdout.close()
            sys.exit(0)
        else:
            self.workers[newpid] = rpipe
            return newpid


    def is_ready(self, pid):
        """Is the pid done?"""
        if pid in self.results:
            return True
        return select.select([self.workers[pid], ], [], [], 0.0)[0]

    def get_result(self, pid, blocking=False):
        """Get's the result for a pipe"""
        if blocking:
            while not self.is_ready(pid) and not self.results.has_key(pid):
                time.sleep(0.02)
        if self.results.has_key(pid):
            try:
                return self.results[pid]
            finally:
                del self.results[pid]
        elif self.is_ready(pid):
            try:
                return cPickle.load(os.fdopen(self.workers[pid]))
            finally:
                del self.workers[pid]
        else:
            return IncompleteWork








