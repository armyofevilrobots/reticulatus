# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reticulate_main.ui'
#
# Created: Thu Oct 25 21:48:45 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(925, 633)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QtCore.QSize(512, 384))
        main_window.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.object_tabs = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_tabs.sizePolicy().hasHeightForWidth())
        self.object_tabs.setSizePolicy(sizePolicy)
        self.object_tabs.setObjectName("object_tabs")
        self.object_3d = QtGui.QWidget()
        self.object_3d.setCursor(QtCore.Qt.CrossCursor)
        self.object_3d.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.object_3d.setObjectName("object_3d")
        self.object_3d_layout = QtGui.QHBoxLayout(self.object_3d)
        self.object_3d_layout.setObjectName("object_3d_layout")
        self.frame = QtGui.QFrame(self.object_3d)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.slider_container_layout = QtGui.QVBoxLayout(self.frame)
        self.slider_container_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.slider_container_layout.setObjectName("slider_container_layout")
        self.layer_slider = QtGui.QSlider(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_slider.sizePolicy().hasHeightForWidth())
        self.layer_slider.setSizePolicy(sizePolicy)
        self.layer_slider.setMaximumSize(QtCore.QSize(50, 16777215))
        self.layer_slider.setMinimum(0)
        self.layer_slider.setMaximum(9999)
        self.layer_slider.setProperty("value", 0)
        self.layer_slider.setOrientation(QtCore.Qt.Vertical)
        self.layer_slider.setInvertedAppearance(False)
        self.layer_slider.setObjectName("layer_slider")
        self.slider_container_layout.addWidget(self.layer_slider)
        self.layer_lcd = QtGui.QLCDNumber(self.frame)
        self.layer_lcd.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.layer_lcd.setFont(font)
        self.layer_lcd.setNumDigits(4)
        self.layer_lcd.setObjectName("layer_lcd")
        self.slider_container_layout.addWidget(self.layer_lcd)
        self.object_3d_layout.addWidget(self.frame)
        self.object_tabs.addTab(self.object_3d, "")
        self.gcode = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gcode.sizePolicy().hasHeightForWidth())
        self.gcode.setSizePolicy(sizePolicy)
        self.gcode.setObjectName("gcode")
        self.gcode_hlayout = QtGui.QHBoxLayout(self.gcode)
        self.gcode_hlayout.setObjectName("gcode_hlayout")
        self.gcode_editor = QtGui.QTextEdit(self.gcode)
        self.gcode_editor.setObjectName("gcode_editor")
        self.gcode_hlayout.addWidget(self.gcode_editor)
        self.object_tabs.addTab(self.gcode, "")
        self.horizontalLayout.addWidget(self.object_tabs)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_edit = QtGui.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_Settings = QtGui.QMenu(self.menubar)
        self.menu_Settings.setObjectName("menu_Settings")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menu_Windows = QtGui.QMenu(self.menubar)
        self.menu_Windows.setObjectName("menu_Windows")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main_window)
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.layers_dock = QtGui.QDockWidget(main_window)
        self.layers_dock.setMinimumSize(QtCore.QSize(120, 160))
        self.layers_dock.setMaximumSize(QtCore.QSize(1024, 1024))
        self.layers_dock.setObjectName("layers_dock")
        self.dock_contents = QtGui.QWidget()
        self.dock_contents.setObjectName("dock_contents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dock_contents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.dock_contents)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.layer_list_widget = QtGui.QListWidget(self.dock_contents)
        self.layer_list_widget.setObjectName("layer_list_widget")
        self.verticalLayout.addWidget(self.layer_list_widget)
        self.layers_dock.setWidget(self.dock_contents)
        main_window.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.layers_dock)
        self.tools_dock = QtGui.QDockWidget(main_window)
        self.tools_dock.setMinimumSize(QtCore.QSize(120, 160))
        self.tools_dock.setObjectName("tools_dock")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.tools_dock.setWidget(self.dockWidgetContents)
        main_window.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.tools_dock)
        self.action_file = QtGui.QAction(main_window)
        self.action_file.setObjectName("action_file")
        self.action_new = QtGui.QAction(main_window)
        self.action_new.setObjectName("action_new")
        self.action_open = QtGui.QAction(main_window)
        self.action_open.setObjectName("action_open")
        self.action_save = QtGui.QAction(main_window)
        self.action_save.setObjectName("action_save")
        self.action_quit = QtGui.QAction(main_window)
        self.action_quit.setObjectName("action_quit")
        self.action_print_settings = QtGui.QAction(main_window)
        self.action_print_settings.setObjectName("action_print_settings")
        self.action_slice_settings = QtGui.QAction(main_window)
        self.action_slice_settings.setObjectName("action_slice_settings")
        self.action_help = QtGui.QAction(main_window)
        self.action_help.setObjectName("action_help")
        self.action_about = QtGui.QAction(main_window)
        self.action_about.setObjectName("action_about")
        self.action_display_settings = QtGui.QAction(main_window)
        self.action_display_settings.setObjectName("action_display_settings")
        self.action_slice = QtGui.QAction(main_window)
        self.action_slice.setObjectName("action_slice")
        self.action_Layers = QtGui.QAction(main_window)
        self.action_Layers.setObjectName("action_Layers")
        self.action_Toolbox = QtGui.QAction(main_window)
        self.action_Toolbox.setObjectName("action_Toolbox")
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.menu_Settings.addAction(self.action_print_settings)
        self.menu_Settings.addAction(self.action_slice_settings)
        self.menu_Settings.addAction(self.action_display_settings)
        self.menu_Help.addAction(self.action_help)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_about)
        self.menuActions.addAction(self.action_slice)
        self.menu_Windows.addAction(self.action_Layers)
        self.menu_Windows.addAction(self.action_Toolbox)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.menubar.addAction(self.menu_Windows.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(main_window)
        self.object_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtGui.QApplication.translate("main_window", "Reticulatus", None, QtGui.QApplication.UnicodeUTF8))
        self.layer_slider.setToolTip(QtGui.QApplication.translate("main_window", "Layer clip plane", None, QtGui.QApplication.UnicodeUTF8))
        self.object_tabs.setTabText(self.object_tabs.indexOf(self.object_3d), QtGui.QApplication.translate("main_window", "3D Object", None, QtGui.QApplication.UnicodeUTF8))
        self.object_tabs.setTabText(self.object_tabs.indexOf(self.gcode), QtGui.QApplication.translate("main_window", "GCode", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("main_window", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_edit.setTitle(QtGui.QApplication.translate("main_window", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Settings.setTitle(QtGui.QApplication.translate("main_window", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("main_window", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuActions.setTitle(QtGui.QApplication.translate("main_window", "&Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Windows.setTitle(QtGui.QApplication.translate("main_window", "&Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("main_window", "Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.action_file.setText(QtGui.QApplication.translate("main_window", "&file", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new.setText(QtGui.QApplication.translate("main_window", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setText(QtGui.QApplication.translate("main_window", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save.setText(QtGui.QApplication.translate("main_window", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_quit.setText(QtGui.QApplication.translate("main_window", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_print_settings.setText(QtGui.QApplication.translate("main_window", "&Printer", None, QtGui.QApplication.UnicodeUTF8))
        self.action_slice_settings.setText(QtGui.QApplication.translate("main_window", "S&licing", None, QtGui.QApplication.UnicodeUTF8))
        self.action_help.setText(QtGui.QApplication.translate("main_window", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setText(QtGui.QApplication.translate("main_window", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_display_settings.setText(QtGui.QApplication.translate("main_window", "&Display", None, QtGui.QApplication.UnicodeUTF8))
        self.action_slice.setText(QtGui.QApplication.translate("main_window", "&Slice", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Layers.setText(QtGui.QApplication.translate("main_window", "&Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Toolbox.setText(QtGui.QApplication.translate("main_window", "&Toolbox", None, QtGui.QApplication.UnicodeUTF8))

