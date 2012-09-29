# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reticulate_main.ui'
#
# Created: Sat Sep 29 09:36:32 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 560)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(512, 384))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../albino_reticulated_python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
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
        self.object_3d_hlayout = QtGui.QHBoxLayout(self.object_3d)
        self.object_3d_hlayout.setObjectName("object_3d_hlayout")
        self.gl_widget = QtGui.QWidget(self.object_3d)
        self.gl_widget.setObjectName("gl_widget")
        self.object_3d_hlayout.addWidget(self.gl_widget)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menu_Settings = QtGui.QMenu(self.menubar)
        self.menu_Settings.setObjectName("menu_Settings")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dock_widget = QtGui.QDockWidget(MainWindow)
        self.dock_widget.setMinimumSize(QtCore.QSize(150, 300))
        self.dock_widget.setMaximumSize(QtCore.QSize(1024, 1024))
        self.dock_widget.setObjectName("dock_widget")
        self.dock_contents = QtGui.QWidget()
        self.dock_contents.setObjectName("dock_contents")
        self.dock_hlayout = QtGui.QHBoxLayout(self.dock_contents)
        self.dock_hlayout.setObjectName("dock_hlayout")
        self.tool_box = QtGui.QToolBox(self.dock_contents)
        self.tool_box.setObjectName("tool_box")
        self.layers = QtGui.QWidget()
        self.layers.setGeometry(QtCore.QRect(0, 0, 264, 413))
        self.layers.setObjectName("layers")
        self.verticalLayout = QtGui.QVBoxLayout(self.layers)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layer_list_widget = QtGui.QListWidget(self.layers)
        self.layer_list_widget.setObjectName("layer_list_widget")
        self.verticalLayout.addWidget(self.layer_list_widget)
        self.tool_box.addItem(self.layers, "")
        self.tools = QtGui.QWidget()
        self.tools.setGeometry(QtCore.QRect(0, 0, 264, 413))
        self.tools.setObjectName("tools")
        self.gridLayout_2 = QtGui.QGridLayout(self.tools)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tool_box.addItem(self.tools, "")
        self.dock_hlayout.addWidget(self.tool_box)
        self.dock_widget.setWidget(self.dock_contents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_widget)
        self.action_file = QtGui.QAction(MainWindow)
        self.action_file.setObjectName("action_file")
        self.action_New = QtGui.QAction(MainWindow)
        self.action_New.setObjectName("action_New")
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Printer = QtGui.QAction(MainWindow)
        self.action_Printer.setObjectName("action_Printer")
        self.actionS_licing = QtGui.QAction(MainWindow)
        self.actionS_licing.setObjectName("actionS_licing")
        self.action_Help = QtGui.QAction(MainWindow)
        self.action_Help.setObjectName("action_Help")
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_toolbox = QtGui.QAction(MainWindow)
        self.action_toolbox.setObjectName("action_toolbox")
        self.menuFile.addAction(self.action_New)
        self.menuFile.addAction(self.action_Open)
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Quit)
        self.menu_Settings.addAction(self.action_Printer)
        self.menu_Settings.addAction(self.actionS_licing)
        self.menu_Help.addAction(self.action_Help)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_About)
        self.menu_View.addAction(self.action_toolbox)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.object_tabs.setCurrentIndex(1)
        self.tool_box.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.object_tabs.setTabText(self.object_tabs.indexOf(self.object_3d), QtGui.QApplication.translate("MainWindow", "3D Object", None, QtGui.QApplication.UnicodeUTF8))
        self.object_tabs.setTabText(self.object_tabs.indexOf(self.gcode), QtGui.QApplication.translate("MainWindow", "GCode", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Settings.setTitle(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.tool_box.setItemText(self.tool_box.indexOf(self.layers), QtGui.QApplication.translate("MainWindow", "Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.tool_box.setItemText(self.tool_box.indexOf(self.tools), QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.action_file.setText(QtGui.QApplication.translate("MainWindow", "&file", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Printer.setText(QtGui.QApplication.translate("MainWindow", "&Printer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionS_licing.setText(QtGui.QApplication.translate("MainWindow", "S&licing", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Help.setText(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_toolbox.setText(QtGui.QApplication.translate("MainWindow", "&Toolbox", None, QtGui.QApplication.UnicodeUTF8))

