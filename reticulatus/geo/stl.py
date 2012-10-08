""" This is blatantly stolen from https://github.com/sconklin/stlutils
Big thanks to https://github.com/sconklin for licensing this as GPLv3
so that I can use it in this project.
"""
import struct

class STL():
    """
    This class encapsulates reading, modifying, and writing .stl files
    in both binary and ascii formats
    """

    debug         = False
    _facets      = []
    _isBinary    = None
    _outIsBinary = None
    _fileComment = ''
    _readFD      = None
    _writeFD     = None
    _header      = None
    _length      = None


    @property
    def facets(self):
        return self._facets

    ## __init__
    #
    def __init__(self, infile = None, outfile = None):
        if infile != None:
            self._readFD = open (infile, "rb")
        if outfile != None:
            self._writeFD = open (outfile, "wb")
        return

    ## setInputFile
    #
    def setInputFile(self, infile):
        """
        Closes any open input file and open the one requested
        Resets any meta information associated with the input
        """
        assert infile is not None
        if self._readFD is not None:
            self._readFD.close()
        self._readFD = open (infile, "rb")

    ## setOutputType
    #
    def setOutputType(self, otype):
        """
        Set the type of file that will be written. Valid types are:
        "binary" and "ascii"
        """
        if otype not in ["binary", "ascii"]:
            raise ValueError("Valid output file types are 'ascii' and 'binary'")
        if otype == "ascii":
            self.outIsBinary = False
        else:
            self.outIsBinary = True

    ## setOutputFile
    #
    def setOutputFile(self, infile):
        """
        Flushes and closes the output file and open the one requested
        Resets any meta information associated with the output
        """
        if self._writeFD != None:
            self._writeFD.close()
            self._writeFD = None

        self.__writedf = open(infile, "wb")

        return

    ## __unpack_float
    #
    def __unpack_float(self, count):
        """
        Unpack the requested number of floating point values from
        the input descriptor and return them in an array
        """
        data = self._readFD.read(count*4)
        formatstr = "<%df" % count
        out = struct.unpack(formatstr, data)
        #print "OUT IS", out
        return out


    ## __unpack_attribute
    #
    def __unpack_attribute(self):
        """
        Unpack a 16 bit attribute from the input descriptor and return it
        """
        attr = self._readFD.read(2)
        return struct.unpack("<H", attr)[0]

    ## __binary_read_triangle
    #
    def __binary_read_triangle(self):
        """
        Read the Normal, three vertices, and 2 packing bytes for a triangle in
        binary stl format, from the input descriptor.
        Return arrays for each of these items.
        """
        n = self.__unpack_float(3)
        p1 = self.__unpack_float(3)
        p2 = self.__unpack_float(3)
        p3 = self.__unpack_float(3)
        b = self.__unpack_attribute()

        if self.debug:
            print "Read binary Triangle:"
            print "  Normal: %f %f %f" % (n[0], n[1], n[2])
            print "  P1:     %5.5f %5.5f %5.5f" % (p1[0], p1[1], p1[2])
            print "  P2:     %5.5f %5.5f %5.5f" % (p2[0], p2[1], p2[2])
            print "  P3:     %5.5f %5.5f %5.5f" % (p3[0], p3[1], p3[2])
            print "  Attr:   0x%X" % b

        return (n, p1, p2, p3, b)

    ## __read_vertex
    #
    def __read_vertex(self):
        """
        Read a 'vertex' line from an ascii input and return the result
        as a list of three points.
        Raise an exception for unexpected input or EOF.
        """
        lparts = self._readFD.readline().strip().split()
        #print "FOUND LPARTS", lparts
        if lparts[0] != 'vertex':
            raise ValueError(
                    'Found unexpected line <%s> when expecting vertex' %
                    lparts)
        return [float(lparts[1]), float(lparts[2]), float(lparts[3])]

    ## __ascii_read_triangle
    #
    def __ascii_read_triangle(self):
        """
        Read the Normal, three vertices, and 2 packing bytes for a triangle in
        ascii stl format, from the input descriptor.
        Return arrays for each of these items.
        Exception is raised for end of file.
        """
        # ascii data looks like this for a triangle:
        #
        # facet normal ni nj nk
        # outer loop
        # vertex v1x v1y v1z
        # vertex v2x v2y v2z
        # vertex v3x v3y v3z
        # endloop
        # endfacet
        #

        # we're expecting a facet line
        line = self._readFD.readline().strip()
        lparts = line.split()
        if lparts[0] == 'endsolid':
            # Same as end of file for our purposes
            raise EOFError
        if (lparts[0] != 'facet') or (lparts[1] != 'normal'):
            raise ValueError(
                    'Found unexpected line <%s> when expecting facet' % line)
        n = [float(lparts[2]), float(lparts[3]), float(lparts[4])]

        # "outer loop"
        if self._readFD.readline().strip() != 'outer loop':
            raise ValueError(
                    'Found unexpected line <%s> when expecting outer loop' %
                    line)

        # Now the three vertices
        p1 = self.__read_vertex()
        p2 = self.__read_vertex()
        p3 = self.__read_vertex()

        # "endloop"
        if self._readFD.readline().strip() != 'endloop':
            raise ValueError(
                    'Found unexpected line <%s> when expecting endloop' %
                    line)

        # "endfacet"
        if self._readFD.readline().strip() != 'endfacet':
            raise ValueError(
                    'Found unexpected line <%s> when expecting endfacet' %
                    line)

        # ascii has no attibute
        b = 0

        if self.debug:
            print "Read ascii Triangle:"
            print "  Normal: %f %f %f" % (n[0], n[1], n[2])
            print "  P1:     %f %f %f" % (p1[0], p1[1], p1[2])
            print "  P2:     %f %f %f" % (p2[0], p2[1], p2[2])
            print "  P3:     %f %f %f" % (p3[0], p3[1], p3[2])
            print "  Attr:   0x%X" % b

        return (n, p1, p2, p3, b)

    ## __determine_input_type()
    #
    def __determine_input_type(self):
        """What type of file is this?"""
        binflag = False
        pos = self._readFD.tell()
        if self.debug: print "My post at start is ",pos

        # Try to determine whether this is in binary or ascii format
        self._readFD.seek(0)

        # If the first line doesn't start with "solid " it is binary
        tststr = "solid "
        solidtest = self._readFD.read(len(tststr))
        if solidtest != tststr:
            binflag = True

        # It could still be binary, as first 80 bytes is comment in a binary
        # file each facet is 50 bytes, read one and test it to see if it's
        # all ascii
        self._readFD.seek(80)
        facet = self._readFD.read(50)
        if not all(ord(c) < 128 for c in facet):
            binflag = True

        self._isBinary = binflag

        # if binary, gather some more information depending on type
        if self._isBinary:
            self._readFD.seek(0)
            self._header =  self._readFD.read(80)
            tlen = self._readFD.read(4)
            self._length = struct.unpack("<I", tlen)[0]

        self._readFD.seek(pos)
        if self.debug: print "Now at", self._readFD.tell()
        return

    ## header
    #
    def header(self):
        """
        Return the header if the input file is binary, otherwise return None
        """
        if self._isBinary == None:
            # figure out whether it's binary or ascii
            self.__determine_input_type()

        if self._isBinary:
            if self.debug: print "Header is ",len(self._header), "bytes"
            return self._header
        else:
            return None

    ## length
    #
    def length(self):
        """
        return the number of triangles in the input file, only valid for binary unless we've read the data
        """
        if self._isBinary == None:
            # figure out whether it's binary or ascii
            self.__determine_input_type()

        if self._isBinary:
            return self._length
        else:
            return None

    ## type
    #
    def type(self):
        """
        Return the input file type - "ascii", "binary" or None (if not known)
        """
        if self._isBinary == None:
            # figure out whether it's binary or ascii
            self.__determine_input_type()

        if self._isBinary == None:
            return None
        elif self._isBinary:
            return "binary"
        else:
            return "ascii"

    ## read
    #
    def read(self):
        """
        Reads the input file into an internal representation.
        Raises an exception on error
        """
        if self._isBinary == None:
            # figure out whether it's binary or ascii
            self.__determine_input_type()

        if self._isBinary == None:
            raise ValueError(
                    "Unable to determine file type, is this an stl file?")
        elif self._isBinary:
            self._facets = []
            # Read all the binary vertices
            self._readFD.seek(80+4) #We need to skip header, AND the size uint32
            for i in range(self._length):
                facet = {}

                (n, p1, p2, p3, b) =  self.__binary_read_triangle()
                facet['n'] = n
                facet['p'] = [p1, p2, p3]
                facet['a'] = b
                self._facets.append(facet)
        else:
            self._facets = []
            # read all the ascii vertices
            self._readFD.seek(0)
            line = self._readFD.readline().strip()
            if not line.startswith('solid'):
                raise ValueError(
                        'Found unexpected line <%s> when expecting solid' %
                        line)
            try:
                while True:
                    facet = dict()
                    (n, p1, p2, p3, b) =  self.__ascii_read_triangle()
                    facet['n'] = n
                    facet['p'] = [p1, p2, p3]
                    facet['a'] = b
                    #print "Found facet: ", facet
                    self._facets.append(facet)
            except EOFError:
                pass
        return

    ## addFacet
    #
    def addFacet(self, p, n=None, a=0):
        """
        Add a facet to the internal list. Normal defaults to all zeros. Attribute defaults to zero
        """
        n = n or [0.0,0.0,0.0]
        self._facets.append([n, p, a])
        return

    ## addFace
    #
    def addFace(self, pointlist, n=None, a=0):
        """
        Add a four point face to the internal list. Normal defaults to all zeros. Attribute defaults to zero
        Addition follows a right hand rule, assigning facets from points 1,2,3 then 1,3,4
        """
        n = n or [0.0,0.0,0.0]
        self.addFacet([pointlist[0], pointlist[1], pointlist[2]])
        self.addFacet([pointlist[0], pointlist[2], pointlist[3]])

        return

    ## dump
    #
    def dump(self):
        """
        Dumps the internal tringle list
        """
        for facet in self._facets:
            n  = facet['n']
            p1 = facet['p'][0]
            p2 = facet['p'][1]
            p3 = facet['p'][2]
            a  = facet['a']
            print "Facet:"
            print "  Normal: %f %f %f" % (n[0], n[1], n[2])
            print "  P1:     %f %f %f" % (p1[0], p1[1], p1[2])
            print "  P2:     %f %f %f" % (p2[0], p2[1], p2[2])
            print "  P3:     %f %f %f" % (p3[0], p3[1], p3[2])
            print "  Attr:   0x%X" % a





