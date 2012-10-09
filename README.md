    __________        __  .__             .__          __                 
    \______   \ _____/  |_|__| ____  __ __|  | _____ _/  |_ __ __  ______ 
     |       _// __ \   __\  |/ ___\|  |  \  | \__  \\   __\  |  \/  ___/ 
     |    |   \  ___/|  | |  \  \___|  |  /  |__/ __ \|  | |  |  /\___ \  
     |____|_  /\___  >__| |__|\___  >____/|____(____  /__| |____//____  > 
            \/     \/             \/                \/                \/  
     _____   _______ _  _  ___  _  _   ___ ___ ___ ___    _   ___      
    | _ \ \ / /_   _| || |/ _ \| \| | | _ \ __| _ \ _ \  /_\ | _ \     
    |  _/\ V /  | | | __ | (_) | .` | |   / _||  _/   / / _ \|  _/      
    |_|   |_|   |_| |_||_|\___/|_|\_| |_|_\___|_| |_|_\/_/ \_\_|       
      ___  ___ ___  ___  ___   __  __   _   _  _  ___ _    ___ ___      
     / __|/ __/ _ \|   \| __| |  \/  | /_\ | \| |/ __| |  | __| _ \     
    | (_ | (_| (_) | |) | _|  | |\/| |/ _ \| .` | (_ | |__| _||   /     
     \___|\___\___/|___/|___| |_|  |_/_/ \_\_|\_|\___|____|___|_|_\     

============================================
Reticulatus : A Python Reprap G-Code mangler
============================================

This is a project that will (soon) provide fast 3d object skeining.
The goal of this project is to provide a minimal set of reusable
slicing tools that are very robust, fast, and repeatable.

While there are other great projects out there, including skeinforge
and Slic3r, neither of them meets my need to be able to fine tune
toolpaths and fill strategies, and/or are written in languages that
are far enough outside of my expertise to be productive. I also spent
a fair bit of time researching various methods of slicing and skeining
so that I could get the most bang with the least effort. Productivity
through pathological laziness!

Currently working:
 - STL parsing (thanks https://github.com/sconklin!)
 - Conversion of STL to CGAL polymesh
 - CGAL polymesh to layered planar perimeters
 - Planar perimeter inset based on tool width
 - Multiple perimeters
 - GUI interface: http://youtu.be/4cn2QE-PHxA?hd=1

Coming soon:
 - Cross hatched infill
 - Full 3d LIVE PREVIEW of printable objects and layers
 - Realtime slicing
 - Full multiprocessor support (via multiprocessing) for both
   slicing and perimeters/infills.
 - Selective density perimeters

Longer term:
 - Shallow dome perimeter gap filling
 - Smooth transitions between layers (ramping)
 - Structural ribbing on interial walls
 - Optimized (voronoi/delaunay) infill on perimeter only objects
 - High speed optimized exterior sacrificial support
 - Corner velocity optimization via virtual G64
 - Post processing existing gcode

 ===========
 Building...
 ===========

 This slicer/optimizer requires the CGAL bindings for Python, which are a bit
 of a PITA to install correctly. In order to do so, you need to pull the 
 git repo in the .gitmodule (it should happen automagically), then go into
 the deps/cgal-bindings folder, then issue:
 git checkout e77c16bd5a65 #For example on Ubuntu 12.04
 to get the appropriate git version. Once this is done, you can build the
 python bindings.

 These swig bindings are used to generate fast planar slices of the 3d
 stl models.
