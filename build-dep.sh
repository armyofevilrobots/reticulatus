#!/bin/bash
# Fixup and build the dependencies.

(   \
    git submodule update --init && \
    cd deps/cgal-bindings && \
    mkdir -p build/cgal-local && \
    cd build/cgal-local && \
    cmake -DCGAL_DIR=/usr/lib/CGAL -DBUILD_PYTHON=ON -DBUILD_JAVA=OFF ../../ && \
    make -j 4 && \
    cd ../../../../ 
) || (echo "Failed to build."; exit 99)

echo "Copy the deps/cgal-bindings/build/cgal-local/build-python/CGAL folder"
echo "into your PYTHONPATH, ie, if this is a virtualenv, to:"
echo "lib/python2.X/site-packages/ . We STRONGLY recommend you use a virtual"
echo "env for development."





