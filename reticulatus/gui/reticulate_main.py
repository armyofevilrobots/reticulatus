# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reticulate_main.ui'
#
# Created: Tue Oct  2 20:57:20 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(512, 384)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QtCore.QSize(512, 384))
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
        self.object_3d.setObjectName("object_3d")
        self.object_3d_layout = QtGui.QGridLayout(self.object_3d)
        self.object_3d_layout.setObjectName("object_3d_layout")
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_edit = QtGui.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_Settings = QtGui.QMenu(self.menubar)
        self.menu_Settings.setObjectName("menu_Settings")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
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
        self.action_print = QtGui.QAction(main_window)
        self.action_print.setObjectName("action_print")
        self.action_slice = QtGui.QAction(main_window)
        self.action_slice.setObjectName("action_slice")
        self.action_help = QtGui.QAction(main_window)
        self.action_help.setObjectName("action_help")
        self.action_about = QtGui.QAction(main_window)
        self.action_about.setObjectName("action_about")
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.menu_Settings.addAction(self.action_print)
        self.menu_Settings.addAction(self.action_slice)
        self.menu_Help.addAction(self.action_help)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_about)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(main_window)
        self.object_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtGui.QApplication.translate("main_window", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.object_tabs.setTabText(self.object_tabs.indexOf(self.object_3d), QtGui.QApplication.translate("main_window", "3D Object", None, QtGui.QApplication.UnicodeUTF8))
        self.object_tabs.setTabText(self.object_tabs.indexOf(self.gcode), QtGui.QApplication.translate("main_window", "GCode", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("main_window", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_edit.setTitle(QtGui.QApplication.translate("main_window", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Settings.setTitle(QtGui.QApplication.translate("main_window", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("main_window", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("main_window", "Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.action_file.setText(QtGui.QApplication.translate("main_window", "&file", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new.setText(QtGui.QApplication.translate("main_window", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setText(QtGui.QApplication.translate("main_window", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save.setText(QtGui.QApplication.translate("main_window", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_quit.setText(QtGui.QApplication.translate("main_window", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_print.setText(QtGui.QApplication.translate("main_window", "&Printer", None, QtGui.QApplication.UnicodeUTF8))
        self.action_slice.setText(QtGui.QApplication.translate("main_window", "S&licing", None, QtGui.QApplication.UnicodeUTF8))
        self.action_help.setText(QtGui.QApplication.translate("main_window", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setText(QtGui.QApplication.translate("main_window", "&About", None, QtGui.QApplication.UnicodeUTF8))

