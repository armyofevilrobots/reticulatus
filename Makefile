


all: reticulate

reticulate: reticulatus/gui/reticulate_main.py
	(cd reticulatus/gui && pyside-uic reticulate_main.ui -o reticulate_main.py)

