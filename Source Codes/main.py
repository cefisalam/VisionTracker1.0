# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoTracker.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

# Import Essential Libraries
from fbs_runtime.application_context import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import numpy as np
import cv2 as cv
from os.path import isfile
from centroidtracker import CentroidTracker
from trackableobject import TrackableObject
import dlib

# Start of GUI initialization
class Ui_VideoTracker(object):
    def setupUi(self, VideoTracker):
        VideoTracker.setObjectName("VideoTracker")
        VideoTracker.resize(504, 426)
        self.label = QtWidgets.QLabel(VideoTracker)
        self.label.setGeometry(QtCore.QRect(50, 10, 401, 41))
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.toolBox = QtWidgets.QToolBox(VideoTracker)
        self.toolBox.setGeometry(QtCore.QRect(30, 70, 451, 341))
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBox.setObjectName("toolBox")
        self.SVTTools = QtWidgets.QWidget()
        self.SVTTools.setGeometry(QtCore.QRect(0, 0, 451, 279))
        self.SVTTools.setObjectName("SVTTools")
        self.MovingObjects = QtWidgets.QGroupBox(self.SVTTools)
        self.MovingObjects.setGeometry(QtCore.QRect(10, 10, 181, 251))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.MovingObjects.setPalette(palette)
        self.MovingObjects.setObjectName("MovingObjects")
        self.verticalLayoutWidget_34 = QtWidgets.QWidget(self.MovingObjects)
        self.verticalLayoutWidget_34.setGeometry(QtCore.QRect(10, 70, 164, 171))
        self.verticalLayoutWidget_34.setObjectName("verticalLayoutWidget_34")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_34)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.MOG = QtWidgets.QRadioButton(self.verticalLayoutWidget_34)
        self.MOG.setChecked(True)
        self.MOG.setObjectName("MOG")
        self.verticalLayout_34.addWidget(self.MOG)
        self.MOG_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_34)
        self.MOG_2.setObjectName("MOG_2")
        self.verticalLayout_34.addWidget(self.MOG_2)
        self.Bayesian = QtWidgets.QRadioButton(self.verticalLayoutWidget_34)
        self.Bayesian.setObjectName("Bayesian")
        self.verticalLayout_34.addWidget(self.Bayesian)
        self.LoadVideoMO = QtWidgets.QPushButton(self.verticalLayoutWidget_34)
        self.LoadVideoMO.setObjectName("LoadVideoMO")
        self.verticalLayout_34.addWidget(self.LoadVideoMO)
        self.CaptureMO = QtWidgets.QPushButton(self.verticalLayoutWidget_34)
        self.CaptureMO.setObjectName("CaptureMO")
        self.verticalLayout_34.addWidget(self.CaptureMO)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.MovingObjects)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 161, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.ThresholdEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ThresholdEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ThresholdEdit.setObjectName("ThresholdEdit")
        self.horizontalLayout_2.addWidget(self.ThresholdEdit)
        self.ObjectsofInterest = QtWidgets.QGroupBox(self.SVTTools)
        self.ObjectsofInterest.setGeometry(QtCore.QRect(240, 0, 181, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.ObjectsofInterest.setPalette(palette)
        self.ObjectsofInterest.setObjectName("ObjectsofInterest")
        self.verticalLayoutWidget_35 = QtWidgets.QWidget(self.ObjectsofInterest)
        self.verticalLayoutWidget_35.setGeometry(QtCore.QRect(10, 20, 161, 91))
        self.verticalLayoutWidget_35.setObjectName("verticalLayoutWidget_35")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_35)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.LoadVideoOOI = QtWidgets.QPushButton(self.verticalLayoutWidget_35)
        self.LoadVideoOOI.setObjectName("LoadVideoOOI")
        self.verticalLayout_35.addWidget(self.LoadVideoOOI)
        self.CaptureOOI = QtWidgets.QPushButton(self.verticalLayoutWidget_35)
        self.CaptureOOI.setObjectName("CaptureOOI")
        self.verticalLayout_35.addWidget(self.CaptureOOI)
        self.OpticalFlow = QtWidgets.QGroupBox(self.SVTTools)
        self.OpticalFlow.setGeometry(QtCore.QRect(240, 120, 181, 151))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.OpticalFlow.setPalette(palette)
        self.OpticalFlow.setObjectName("OpticalFlow")
        self.verticalLayoutWidget_36 = QtWidgets.QWidget(self.OpticalFlow)
        self.verticalLayoutWidget_36.setGeometry(QtCore.QRect(10, 60, 161, 91))
        self.verticalLayoutWidget_36.setObjectName("verticalLayoutWidget_36")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_36)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.LoadVideoOP = QtWidgets.QPushButton(self.verticalLayoutWidget_36)
        self.LoadVideoOP.setObjectName("LoadVideoOP")
        self.verticalLayout_36.addWidget(self.LoadVideoOP)
        self.CaptureOP = QtWidgets.QPushButton(self.verticalLayoutWidget_36)
        self.CaptureOP.setObjectName("CaptureOP")
        self.verticalLayout_36.addWidget(self.CaptureOP)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.OpticalFlow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.WinSizeEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.WinSizeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.WinSizeEdit.setObjectName("WinSizeEdit")
        self.horizontalLayout_3.addWidget(self.WinSizeEdit)
        self.toolBox.addItem(self.SVTTools, "")
        self.AVTTools = QtWidgets.QWidget()
        self.AVTTools.setGeometry(QtCore.QRect(0, 0, 451, 279))
        self.AVTTools.setObjectName("AVTTools")
        self.Objects = QtWidgets.QGroupBox(self.AVTTools)
        self.Objects.setGeometry(QtCore.QRect(0, 10, 221, 241))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Objects.setPalette(palette)
        self.Objects.setObjectName("Objects")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.Objects)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 30, 199, 201))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.DogsButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.DogsButton.setObjectName("DogsButton")
        self.gridLayout_5.addWidget(self.DogsButton, 2, 0, 1, 1)
        self.BusesButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.BusesButton.setObjectName("BusesButton")
        self.gridLayout_5.addWidget(self.BusesButton, 3, 0, 1, 1)
        self.TrainsButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.TrainsButton.setObjectName("TrainsButton")
        self.gridLayout_5.addWidget(self.TrainsButton, 3, 1, 1, 1)
        self.BikesButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.BikesButton.setObjectName("BikesButton")
        self.gridLayout_5.addWidget(self.BikesButton, 1, 1, 1, 1)
        self.BottlesButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.BottlesButton.setObjectName("BottlesButton")
        self.gridLayout_5.addWidget(self.BottlesButton, 1, 0, 1, 1)
        self.PersonsButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.PersonsButton.setChecked(True)
        self.PersonsButton.setObjectName("PersonsButton")
        self.gridLayout_5.addWidget(self.PersonsButton, 0, 0, 1, 1)
        self.CarsButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.CarsButton.setObjectName("CarsButton")
        self.gridLayout_5.addWidget(self.CarsButton, 0, 1, 1, 1)
        self.CatsButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.CatsButton.setObjectName("CatsButton")
        self.gridLayout_5.addWidget(self.CatsButton, 2, 1, 1, 1)
        self.BoatsButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.BoatsButton.setObjectName("BoatsButton")
        self.gridLayout_5.addWidget(self.BoatsButton, 4, 0, 1, 1)
        self.BicyclesButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.BicyclesButton.setObjectName("BicyclesButton")
        self.gridLayout_5.addWidget(self.BicyclesButton, 4, 1, 1, 1)
        self.Tracker = QtWidgets.QGroupBox(self.AVTTools)
        self.Tracker.setGeometry(QtCore.QRect(250, 10, 201, 241))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Tracker.setPalette(palette)
        self.Tracker.setObjectName("Tracker")
        self.verticalLayoutWidget_40 = QtWidgets.QWidget(self.Tracker)
        self.verticalLayoutWidget_40.setGeometry(QtCore.QRect(10, 20, 183, 221))
        self.verticalLayoutWidget_40.setObjectName("verticalLayoutWidget_40")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_40)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.LoadModelWeightsOTD = QtWidgets.QPushButton(self.verticalLayoutWidget_40)
        self.LoadModelWeightsOTD.setObjectName("LoadModelWeightsOTD")
        self.verticalLayout_40.addWidget(self.LoadModelWeightsOTD)
        self.LoadModelLabelsOTD = QtWidgets.QPushButton(self.verticalLayoutWidget_40)
        self.LoadModelLabelsOTD.setObjectName("LoadModelLabelsOTD")
        self.verticalLayout_40.addWidget(self.LoadModelLabelsOTD)
        self.LoadVideoOTD = QtWidgets.QPushButton(self.verticalLayoutWidget_40)
        self.LoadVideoOTD.setObjectName("LoadVideoOTD")
        self.verticalLayout_40.addWidget(self.LoadVideoOTD)
        self.CaptureOTD = QtWidgets.QPushButton(self.verticalLayoutWidget_40)
        self.CaptureOTD.setObjectName("CaptureOTD")
        self.verticalLayout_40.addWidget(self.CaptureOTD)
        self.TrackOTD = QtWidgets.QPushButton(self.verticalLayoutWidget_40)
        self.TrackOTD.setObjectName("TrackOTD")
        self.verticalLayout_40.addWidget(self.TrackOTD)
        self.toolBox.addItem(self.AVTTools, "")

        self.retranslateUi(VideoTracker)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VideoTracker)

    def retranslateUi(self, VideoTracker):
        _translate = QtCore.QCoreApplication.translate
        VideoTracker.setWindowTitle(_translate("VideoTracker", "Dialog"))
        self.label.setText(_translate("VideoTracker", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#75507b;\">Object Tracking in Video Sequence</span></p></body></html>"))
        self.MovingObjects.setTitle(_translate("VideoTracker", "Background Subtraction"))
        self.MOG.setText(_translate("VideoTracker", "Mixture of Gaussian"))
        self.MOG_2.setText(_translate("VideoTracker", "Adaptive MOG"))
        self.Bayesian.setText(_translate("VideoTracker", "Bayesian Estimation"))
        self.LoadVideoMO.setText(_translate("VideoTracker", "Load Video"))
        self.CaptureMO.setText(_translate("VideoTracker", "Capture Video"))
        self.label_6.setText(_translate("VideoTracker", "  Threshold "))
        self.ThresholdEdit.setText(_translate("VideoTracker", "500"))
        self.ObjectsofInterest.setTitle(_translate("VideoTracker", "Object Tracking"))
        self.LoadVideoOOI.setText(_translate("VideoTracker", "Load Video"))
        self.CaptureOOI.setText(_translate("VideoTracker", "Capture Video"))
        self.OpticalFlow.setTitle(_translate("VideoTracker", "Optical Flow"))
        self.LoadVideoOP.setText(_translate("VideoTracker", "Load Video"))
        self.CaptureOP.setText(_translate("VideoTracker", "Capture Video"))
        self.label_7.setText(_translate("VideoTracker", "      Win Size    "))
        self.WinSizeEdit.setText(_translate("VideoTracker", "15"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.SVTTools), _translate("VideoTracker", "Object Detection N Tracking"))
        self.Objects.setTitle(_translate("VideoTracker", "Objects"))
        self.DogsButton.setText(_translate("VideoTracker", "Dogs"))
        self.BusesButton.setText(_translate("VideoTracker", "Buses"))
        self.TrainsButton.setText(_translate("VideoTracker", "Trains"))
        self.BikesButton.setText(_translate("VideoTracker", "Motor Bikes"))
        self.BottlesButton.setText(_translate("VideoTracker", "Bottles"))
        self.PersonsButton.setText(_translate("VideoTracker", "Persons"))
        self.CarsButton.setText(_translate("VideoTracker", "Cars"))
        self.CatsButton.setText(_translate("VideoTracker", "Cats"))
        self.BoatsButton.setText(_translate("VideoTracker", "Boats"))
        self.BicyclesButton.setText(_translate("VideoTracker", "Bicycles"))
        self.Tracker.setTitle(_translate("VideoTracker", "Tracker"))
        self.LoadModelWeightsOTD.setText(_translate("VideoTracker", "Load Pre-trained Weights"))
        self.LoadModelLabelsOTD.setText(_translate("VideoTracker", "Load Pre-trained Labels"))
        self.LoadVideoOTD.setText(_translate("VideoTracker", "Load Video"))
        self.CaptureOTD.setText(_translate("VideoTracker", "Capture Video"))
        self.TrackOTD.setText(_translate("VideoTracker", "Track"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.AVTTools), _translate("VideoTracker", "Directional Tracking"))
# End of GUI initialization

        # Connect All Push Buttons to the corresponding functions
        self.LoadVideoMO.clicked.connect(self.on_LoadVideoMO_clicked)
        self.CaptureMO.clicked.connect(self.on_CaptureMO_clicked)
        self.LoadVideoOOI.clicked.connect(self.on_LoadVideoOOI_clicked)
        self.CaptureOOI.clicked.connect(self.on_CaptureOOI_clicked)
        self.LoadVideoOP.clicked.connect(self.on_LoadVideoOP_clicked)
        self.CaptureOP.clicked.connect(self.on_CaptureOP_clicked)
        self.LoadModelWeightsOTD.clicked.connect(self.on_LoadModelWeightsOTD_clicked)
        self.LoadModelLabelsOTD.clicked.connect(self.on_LoadModelLabelsOTD_clicked)
        self.LoadModelLabelsOTD.setEnabled(False)
        self.LoadVideoOTD.clicked.connect(self.on_LoadVideoOTD_clicked)
        self.LoadVideoOTD.setEnabled(False)
        self.CaptureOTD.clicked.connect(self.on_CaptureOTD_clicked)
        self.CaptureOTD.setEnabled(False)
        self.TrackOTD.clicked.connect(self.on_TrackOTD_clicked)
        self.TrackOTD.setEnabled(False)

# Define Functions
    def on_LoadVideoMO_clicked(self):
        # Background Subtraction (Adopted from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_video/py_bg_subtraction/py_bg_subtraction.html#py-background-subtraction)
        # Load a Video with File Picker (Found on https://doc.qt.io/qt-5/qfiledialog.html)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        LoadfileName, _ = QFileDialog.getOpenFileName(VideoTracker,"Select a Video","","Video Files (*.avi *.flv *.wmv *.mp4)", options=options)
        # Get the Size Threshold of Moving Object
        Thres = int(self.ThresholdEdit.text())
        # Intialize OpenCV Background Subtractors
        if self.MOG.isChecked() == True:
            subtractor = cv.bgsegm.createBackgroundSubtractorMOG()
        elif self.MOG_2.isChecked() == True:
            subtractor = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=100, detectShadows=True)
        elif self.Bayesian.isChecked() == True:
            subtractor = cv.bgsegm.createBackgroundSubtractorGMG()
        if isfile(LoadfileName):
            # Save the Video (If asked by the User)
            msgBox = QMessageBox()
            msgBox.setText("Video Loaded!!!")
            msgBox.setInformativeText("Do you want to save the Video after Tracking?")
            msgBox.setStyleSheet("QLabel{min-width:400 px; font-size: 16px;}")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()
            if ret == QMessageBox.Save:
                # Save was Clicked
                fileName, _ = QFileDialog.getSaveFileName(VideoTracker,"Save Output")
                # Show the Message
                msgBox = QMessageBox()
                msgBox.setText("Attention!")
                msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
                msgBox.setInformativeText("Press 'q' to Save Video after Tracking.")
                msgBox.exec_()
                writeOutput = True
            elif ret == QMessageBox.Discard:
                # Show the Message
                msgBox = QMessageBox()
                msgBox.setText("Attention!")
                msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
                msgBox.setInformativeText("Press 'q' to Quit Video after Tracking.")
                msgBox.exec_()
                writeOutput = False
            # Initialize Capture
            cap = cv.VideoCapture(LoadfileName)
            ret,frame = cap.read()
            # Get the Size of Frame
            (H,W,_) = frame.shape
            if writeOutput == True:
                # Define the Codec and Create VideoWriter object
                fourcc = cv.VideoWriter_fourcc(*"MJPG")
                out = cv.VideoWriter(fileName, fourcc, 30, (W, H),True)
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                # Apply Background Subtraction to each Frame
                mask = subtractor.apply(frame)
                im2, contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
                # Draw Bounding Boxes over the Objects which is notPresent in Background
                for pic,contour in enumerate(contours):
                    area = cv.contourArea(contour)
                    if (area >Thres):
                        x,y,w,h = cv.boundingRect(contour)
                        img = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                # Write and Show Output
                if writeOutput == True:
                    out.write(frame)
                cv.imshow("Output",frame)
                if cv.waitKey(30) == ord('q'):
                    break
            # Release everything if Job is Finished
            cap.release()
            if writeOutput == True:
                out.release()
            cv.destroyAllWindows()
        else:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Attention!")
            msgBox.setInformativeText("No Video Loaded!!!")
            msgBox.exec_()

    def on_CaptureMO_clicked(self):
        # Get the Size Threshold of Moving Object
        Thres = int(self.ThresholdEdit.text())
        # Intialize OpenCV Background Subtractors
        if self.MOG.isChecked() == True:
            subtractor = cv.bgsegm.createBackgroundSubtractorMOG()
        elif self.MOG_2.isChecked() == True:
            subtractor = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=100, detectShadows=True)
        elif self.Bayesian.isChecked() == True:
            subtractor = cv.bgsegm.createBackgroundSubtractorGMG()
        # Save the Video (If asked by the User)
        msgBox = QMessageBox()
        msgBox.setText("Do you want to save the Video after Tracking?")
        msgBox.setStyleSheet("QLabel{min-width:500 px; font-size: 16px;}")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()
        if ret == QMessageBox.Save:
            # Save was Clicked
            fileName, _ = QFileDialog.getSaveFileName(VideoTracker,"Save Output")
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setText("Attention!")
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setInformativeText("Press 'q' to Save Video after Tracking.")
            msgBox.exec_()
            writeOutput = True
        elif ret == QMessageBox.Discard:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setText("Attention!")
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setInformativeText("Press 'q' to Quit Video after Tracking.")
            msgBox.exec_()
            writeOutput = False
        # Initialize Capture
        cap = cv.VideoCapture(0)
        ret,frame = cap.read()
        # Get the Size of Frame
        (H,W,_) = frame.shape
        if writeOutput == True:
            # Define the Codec and Create VideoWriter object
            fourcc = cv.VideoWriter_fourcc(*"MJPG")
            out = cv.VideoWriter(fileName, fourcc, 30, (W, H),True)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            # Apply Background Subtraction to each Frame
            mask = subtractor.apply(frame)
            im2, contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
            # Draw Bounding Boxes over the Objects which is notPresent in Background
            for pic,contour in enumerate(contours):
                area = cv.contourArea(contour)
                if (area >Thres):
                    x,y,w,h = cv.boundingRect(contour)
                    img = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            # Write and Show Output
            if writeOutput == True:
                out.write(frame)
            cv.imshow("Output",frame)
            if cv.waitKey(30) == ord('q'):
                break
        # Release everything if Job is Finished
        cap.release()
        if writeOutput == True:
            out.release()
        cv.destroyAllWindows()

    def on_LoadVideoOOI_clicked(self):
        # Simple Object Tracking (Adopted from https://docs.opencv.org/3.4.2/d2/dff/classcv_1_1TrackerKCF.html)
        # Load a Video with File Picker
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        LoadfileName, _ = QFileDialog.getOpenFileName(VideoTracker,"Select a Video","","Video Files (*.avi *.flv *.wmv *.mp4)", options=options)
        # Create OpenCV Object Tracker
        tracker = cv.TrackerKCF_create()
        if isfile(LoadfileName):
            # Save the Video (If asked by the User)
            msgBox = QMessageBox()
            msgBox.setText("Video Loaded!!!")
            msgBox.setInformativeText("Do you want to save the Video after Tracking?")
            msgBox.setStyleSheet("QLabel{min-width:400 px; font-size: 16px;}")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()
            if ret == QMessageBox.Save:
                # Save was Clicked
                fileName, _ = QFileDialog.getSaveFileName(VideoTracker,"Save Output")
                # Show the Message
                msgBox = QMessageBox()
                msgBox.setText("Press 'f' to freeze Frame. Drag to Select a ROI and then press ENTER button!")
                msgBox.setStyleSheet("QLabel{min-width:500 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px}")
                msgBox.setInformativeText("Press 'q' to Quit Video after Tracking.")
                msgBox.exec_()
                writeOutput = True
            elif ret == QMessageBox.Discard:
                # Show the Message
                msgBox = QMessageBox()
                msgBox.setText("Press 'f' to freeze Frame. Drag to Select a ROI and then press ENTER button!")
                msgBox.setStyleSheet("QLabel{min-width:500 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px}")
                msgBox.setInformativeText("Press 'q' to Quit Video after Tracking.")
                msgBox.exec_()
                writeOutput = False
            # Initialize Capture
            cap = cv.VideoCapture(LoadfileName)
            ret,frame = cap.read()
            # Get the Size of Frame
            (H,W,_) = frame.shape
            if writeOutput == True:
                # Define the Codec and Create VideoWriter object
                fourcc = cv.VideoWriter_fourcc(*"MJPG")
                out = cv.VideoWriter(fileName, fourcc, 30, (W, H),True)
            init = None
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                # Check to ee if We are Currently Tracking an Object
                if init is not None:
                    # Grab the New Bounding Box Coordinates of the Object
                    (success, box) = tracker.update(frame)
                    # Check to See if the Tracking was a Success
                    if success:
                        (x, y, w, h) = [int(v) for v in box]
                        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Write and Show Output
                if writeOutput == True:
                    out.write(frame)
                cv.imshow("Output",frame)
                key = cv.waitKey(50) & 0xFF
                # If the 'f' key is selected, Freeze the Frame to "Select" a Bounding Box to Track
                if key == ord("f"):
                    # Select the Bounding Box of the Object to Track
                    init = cv.selectROI("Output", frame, fromCenter=False, showCrosshair=True)
                    # Start OpenCV Object Tracker using the Bounding Box Coordinates
                    tracker.init(frame, init)
                # If the 'q' key is selected, Break
                elif key == ord("q"):
                    break
            # Release everything if Job is Finished
            cap.release()
            if writeOutput == True:
                out.release()
            cv.destroyAllWindows()
        else:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Attention!")
            msgBox.setInformativeText("No Video Loaded!!!")
            msgBox.exec_()

    def on_CaptureOOI_clicked(self):
        tracker = cv.TrackerKCF_create()
        # Save the Video (If asked by the User)
        msgBox = QMessageBox()
        msgBox.setText("Do you want to save the Video after Tracking?")
        msgBox.setStyleSheet("QLabel{min-width:400 px; font-size: 16px;}")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()
        if ret == QMessageBox.Save:
            # Save was Clicked
            fileName, _ = QFileDialog.getSaveFileName(VideoTracker,"Save Output")
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setText("Press 'f' to freeze Frame. Drag to Select a ROI and then press ENTER button!")
            msgBox.setStyleSheet("QLabel{min-width:500 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px}")
            msgBox.setInformativeText("Press 'q' to Quit Video after Tracking.")
            msgBox.exec_()
            writeOutput = True
        elif ret == QMessageBox.Discard:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setText("Press 'f' to freeze Frame. Drag to Select a ROI and then press ENTER button!")
            msgBox.setStyleSheet("QLabel{min-width:500 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px}")
            msgBox.setInformativeText("Press 'q' to Quit Video after Tracking.")
            msgBox.exec_()
            writeOutput = False
        # Initialize Capture
        cap = cv.VideoCapture(0)
        ret,frame = cap.read()
        # Get the Size of Frame
        (H,W,_) = frame.shape
        if writeOutput == True:
            # Define the Codec and Create VideoWriter object
            fourcc = cv.VideoWriter_fourcc(*"MJPG")
            out = cv.VideoWriter(fileName, fourcc, 30, (W, H),True)
        init = None
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            # Check to ee if We are Currently Tracking an Object
            if init is not None:
                # Grab the New Bounding Box Coordinates of the Object
                (success, box) = tracker.update(frame)
                # Check to See if the Tracking was a Success
                if success:
                    (x, y, w, h) = [int(v) for v in box]
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Write and Show Output
            if writeOutput == True:
                out.write(frame)
            cv.imshow("Output",frame)
            key = cv.waitKey(50) & 0xFF
            # If the 'f' key is selected, Freeze the Frame to "Select" a Bounding Box to Track
            if key == ord("f"):
                # Select the Bounding Box of the Object to Track
                init = cv.selectROI("Output", frame, fromCenter=False, showCrosshair=True)
                # Start OpenCV Object Tracker using the Bounding Box Coordinates
                tracker.init(frame, init)
            # If the 'q' key is selected, Break
            elif key == ord("q"):
                break
        # Release everything if Job is Finished
        cap.release()
        if writeOutput == True:
            out.release()
        cv.destroyAllWindows()

    def on_LoadVideoOP_clicked(self):
        # Optical Flow (Adopted from https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html)
        # Load a Video with File Picker
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        LoadfileName, _ = QFileDialog.getOpenFileName(VideoTracker,"Select a Video","","Video Files (*.avi *.flv *.wmv *.mp4)", options=options)
        # Get the Window Size
        k = int(self.WinSizeEdit.text())
        # Parameters for ShiTomasi Corner Detection
        feature_params = dict( maxCorners = 100,
                               qualityLevel = 0.3,
                               minDistance = 7,
                               blockSize = 7 )
        # Parameters for Lucas Kanade Optical Flow
        lk_params = dict( winSize  = (k,k),
                          maxLevel = 2,
                          criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
        # Create Some Random Colors
        color = np.random.randint(0,255,(100,3))
        if isfile(LoadfileName):
            # Save the Video (If asked by the User)
            msgBox = QMessageBox()
            msgBox.setText("Do you want to save the Video after Tracking?")
            msgBox.setStyleSheet("QLabel{min-width:500 px; font-size: 16px;}")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()
            if ret == QMessageBox.Save:
                # Save was Clicked
                fileName, _ = QFileDialog.getSaveFileName(VideoTracker,"Save Output")
                # Show the Message
                msgBox = QMessageBox()
                msgBox.setText("Attention!")
                msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
                msgBox.setInformativeText("Press 'q' to Save Video after Tracking.")
                msgBox.exec_()
                writeOutput = True
            elif ret == QMessageBox.Discard:
                # Show the Message
                msgBox = QMessageBox()
                msgBox.setText("Attention!")
                msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
                msgBox.setInformativeText("Press 'q' to Quit Video after Tracking.")
                msgBox.exec_()
                writeOutput = False
            # Initialize Capture
            cap = cv.VideoCapture(LoadfileName)
            ret,frame = cap.read()
            # Get the Size of Frame
            (H,W,_) = frame.shape
            if writeOutput == True:
                # Define the Codec and Create VideoWriter object
                fourcc = cv.VideoWriter_fourcc(*"MJPG")
                out = cv.VideoWriter(fileName, fourcc, 30, (W, H),True)
            # Take First Frame and Find Features
            ret, old_frame = cap.read()
            old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
            p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
            # Create a Mask Image for Drawing Purposes
            mask = np.zeros_like(old_frame)
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                # Calculate Optical Flow
                p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
                # Select Good Points
                good_new = p1[st==1]
                good_old = p0[st==1]
                # Draw the Tracks (Trajectories)
                for i,(new,old) in enumerate(zip(good_new,good_old)):
                    a,b = new.ravel()
                    c,d = old.ravel()
                    mask = cv.line(mask, (a,b),(c,d), color[i].tolist(), 2)
                    frame = cv.circle(frame,(a,b),5,color[i].tolist(),-1)
                img = cv.add(frame,mask)
                # Write and Show Output
                if writeOutput == True:
                    out.write(img)
                cv.imshow("Output",img)
                if cv.waitKey(30) == ord('q'):
                    break
            # Now Update the Previous Frame and Previous Points
            old_gray = frame_gray.copy()
            p0 = good_new.reshape(-1,1,2)
            # Release everything if Job is Finished
            cap.release()
            if writeOutput == True:
                out.release()
            cv.destroyAllWindows()
        else:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Attention!")
            msgBox.setInformativeText("No Video Loaded!!!")
            msgBox.exec_()

    def on_CaptureOP_clicked(self):
        # Get the Window Size
        k = int(self.WinSizeEdit.text())
        # Parameters for ShiTomasi Corner Detection
        feature_params = dict( maxCorners = 100,
                               qualityLevel = 0.3,
                               minDistance = 7,
                               blockSize = 7 )
        # Parameters for Lucas Kanade Optical Flow
        lk_params = dict( winSize  = (k,k),
                          maxLevel = 2,
                          criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
        # Create Some Random Colors
        color = np.random.randint(0,255,(100,3))
        # Save the Video (If asked by the User)
        msgBox = QMessageBox()
        msgBox.setText("Do you want to save the Video after Tracking?")
        msgBox.setStyleSheet("QLabel{min-width:400 px; font-size: 16px;}")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()
        if ret == QMessageBox.Save:
            # Save was Clicked
            fileName, _ = QFileDialog.getSaveFileName(VideoTracker,"Save Output")
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setText("Attention!")
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setInformativeText("Press 'q' to Save Video after Tracking.")
            msgBox.exec_()
            writeOutput = True
        elif ret == QMessageBox.Discard:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setText("Attention!")
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setInformativeText("Press 'q' to Quit Video after Tracking.")
            msgBox.exec_()
            writeOutput = False
        # Initialize Capture
        cap = cv.VideoCapture(0)
        ret,frame = cap.read()
        # Get the Size of Frame
        (H,W,_) = frame.shape
        if writeOutput == True:
            # Define the Codec and Create VideoWriter object
            fourcc = cv.VideoWriter_fourcc(*"MJPG")
            out = cv.VideoWriter(fileName, fourcc, 30, (W, H),True)
        # Take First Frame and Find Features
        ret, old_frame = cap.read()
        old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
        p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
        # Create a Mask Image for Drawing Purposes
        mask = np.zeros_like(old_frame)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            # Calculate Optical Flow
            p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
            # Select Good Points
            good_new = p1[st==1]
            good_old = p0[st==1]
            # Draw the Tracks (Trajectories)
            for i,(new,old) in enumerate(zip(good_new,good_old)):
                a,b = new.ravel()
                c,d = old.ravel()
                mask = cv.line(mask, (a,b),(c,d), color[i].tolist(), 2)
                frame = cv.circle(frame,(a,b),5,color[i].tolist(),-1)
            img = cv.add(frame,mask)
            # Write and Show Output
            if writeOutput == True:
                out.write(img)
            cv.imshow("Output",img)
            if cv.waitKey(30) == ord('q'):
                break
            # Now Update the Previous Frame and Previous Points
            old_gray = frame_gray.copy()
            p0 = good_new.reshape(-1,1,2)
        # Release everything if Job is Finished
        cap.release()
        if writeOutput == True:
            out.release()
        cv.destroyAllWindows()

    def on_LoadModelWeightsOTD_clicked(self):
        # Load Model Weights with File Picker
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        LoadfileName, _ = QFileDialog.getOpenFileName(VideoTracker,"Select Model Weights","","Model Weights (*.caffemodel)", options=options)
        if isfile(LoadfileName):
            global modelWeights
            modelWeights = LoadfileName
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Model Weights Loaded!")
            msgBox.exec_()
            self.LoadModelLabelsOTD.setEnabled(True)
        else:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Attention!")
            msgBox.setInformativeText("No Model Weights Loaded!!!")
            msgBox.exec_()

    def on_LoadModelLabelsOTD_clicked(self):
        # Load Model Labels with File Picker
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        LoadfileName, _ = QFileDialog.getOpenFileName(VideoTracker,"Select Model Labels","","Model Labels (*.prototxt)", options=options)
        if isfile(LoadfileName):
            global modelLabels
            modelLabels = LoadfileName
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Model Labels Loaded!")
            msgBox.exec_()
            self.LoadVideoOTD.setEnabled(True)
            self.CaptureOTD.setEnabled(True)

        else:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Attention!")
            msgBox.setInformativeText("No Model Labels Loaded!!!")
            msgBox.exec_()

    def on_LoadVideoOTD_clicked(self):
        # Load a Video with File Picker
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        LoadfileName, _ = QFileDialog.getOpenFileName(VideoTracker,"Select a Video","","Video Files (*.avi *.flv *.wmv *.mp4)", options=options)
        if isfile(LoadfileName):
            global videoInput
            videoInput = LoadfileName
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Video Loaded!")
            msgBox.setInformativeText("Click 'Track' to Start Streaming!!!")
            msgBox.exec_()
            self.TrackOTD.setEnabled(True)
        else:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Attention!")
            msgBox.setInformativeText("No Video Loaded!!!")
            msgBox.exec_()

    def on_CaptureOTD_clicked(self):
        global videoInput
        videoInput = 0 # 0 for Internal Camera (1 for External Camera)
        # Show the Message
        msgBox = QMessageBox()
        msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
        msgBox.setText("Camera initialized!")
        msgBox.setInformativeText("Click 'Track' to Start Capture!!!")
        msgBox.exec_()
        self.TrackOTD.setEnabled(True)

    def on_TrackOTD_clicked(self):
        # Region based Directional Tracking (Adopted from https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/)
        confidence = 0.4
        # Initialize the list of Class Labels that MobileNet SSD was Trained to Detect
        CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
                   "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                   "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                   "sofa", "train", "tvmonitor"]
        # Read the Caffe NN Model
        net = cv.dnn.readNetFromCaffe(modelLabels, modelWeights)
        # Select the Object to Track
        if self.PersonsButton.isChecked() == True:
            obj = "person"
        elif self.CarsButton.isChecked() == True:
            obj = "car"
        elif self.BottlesButton.isChecked() == True:
            obj = "bottle"
        elif self.BikesButton.isChecked() == True:
            obj = "motorbike"
        elif self.DogsButton.isChecked() == True:
            obj = "dog"
        elif self.CatsButton.isChecked() == True:
            obj = "cat"
        elif self.BusesButton.isChecked() == True:
            obj = "bus"
        elif self.TrainsButton.isChecked() == True:
            obj = "train"
        elif self.BoatsButton.isChecked() == True:
            obj = "boat"
        elif self.BicyclesButton.isChecked() == True:
            obj = "bicycle"
        # Save the Video (If asked by the User)
        msgBox = QMessageBox()
        msgBox.setText("Video Loaded!!!")
        msgBox.setInformativeText("Do you want to save the Video after Tracking?")
        msgBox.setStyleSheet("QLabel{min-width:400 px; font-size: 16px;}")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()
        if ret == QMessageBox.Save:
            # Save was Clicked
            fileName, _ = QFileDialog.getSaveFileName(VideoTracker,"Save Output")
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setText("Click on the Frame (twice) and Select two distinct Points to draw Reference Line!!!")
            msgBox.setStyleSheet("QLabel{min-width:500 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setInformativeText("Press 'd' to Deselect the Points to change the Reference Line\nPress 'q' to Save Video after Tracking")
            msgBox.exec_()
            writeOutput = True
        else:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setText("Click on the Frame (twice) and Select two distinct Points to draw Reference Line!!!")
            msgBox.setStyleSheet("QLabel{min-width:500 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setInformativeText("Press 'd' to Deselect the Points to change the Reference Line\nPress 'q' to Quit Video after Tracking")
            msgBox.exec_()
            writeOutput = False
        # Initialize Capture
        cap = cv.VideoCapture(videoInput)
        # Get the Size of Frame
        ret,frame = cap.read()
        (H,W,_) = frame.shape
        # Initialize the Coordinates to Draw the Reference Line (to distinguish between two Regions)
        points = []
        x1 = 0
        y1 = H//2
        x2 = W
        y2 = H//2
        X1 = 0
        Y1 = 0
        X2 = 0
        Y2 = 0
        # Function to Select Points in a Frame using Mouse Clicks
        def mouseDrawing(event, x, y, flags, params):
            if event == cv.EVENT_LBUTTONDOWN:
                points.append((x, y))
        # Define the Codec and Create VideoWriter object
        writer = None
        if writeOutput == True:
            fourcc = cv.VideoWriter_fourcc(*"MJPG")
            writer = cv.VideoWriter(fileName, fourcc, 30,(W, H), True)
        # Instantiate our Centroid Tracker, then Initialize a List to Store each of the 'dlib Correlation Trackers', followed by a Dictionary to Map each Unique Object ID to a TrackableObject
        ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
        trackers = []
        trackableObjects = {}
        # Initialize the total number of frames processed thus far, along with the total number of objects that have moved either up or down
        totalFrames = 0
        skipFrames = 20
        totalDown = 0
        totalUp = 0
        # Loop over all Frames from the Video Stream
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv.namedWindow("Frame")
            cv.setMouseCallback("Frame", mouseDrawing)
            if len(points) >= 2:
                pointsArray = np.array(points)
                X1 = pointsArray[0,0]
                Y1 = pointsArray[0,1]
                X2 = pointsArray[1,0]
                Y2 = pointsArray[1,1]
                # Draw a Line to Distinguish between two Regions (We have Implemented it by Defining the Line using Slope 'M' and Intercept 'C')
                # Note: This is Our Own Implementation using the Equation of Line
                if X1 == X2:
                    X2 = X2 + 1
                M = (Y2 - Y1) // (X2 - X1)
                C = Y1 - (M * X1)
                Bline1 = Y1 - W//H*X1
                Bline2 = Y1 + W//H*X1 -W
                if Y1 == Y2:
                    x1 = 0
                    y1 = C
                    x2 = W
                    y2 = C
                elif X1 < X2 and Y1 < Y2 and Bline1 <= 0:
                    x1 = 0
                    y1 = C
                    x2 = (W-C)//M
                    y2 = W
                elif X1 < X2 and Y1 < Y2 and Bline1 >= 0:
                    x1 = C
                    y1 = 0
                    x2 = H
                    y2 = M*H+C
                elif X1 > X2 and Y1 > Y2 and Bline1 >= 0:
                    x1 = H
                    y1 = M*H+C
                    x2 = C
                    y2 = 0
                elif X1 > X2 and Y1 > Y2 and Bline1 <= 0:
                    x1 = (W-C)//M
                    y1 = W
                    x2 = 0
                    y2 = C
                elif X1 > X2 and Y1 < Y2 and Bline2 <= 0:
                    x1 = -C//M
                    y1 = 0
                    x2 = 0
                    y2 = C
                elif X1 > X2 and Y1 < Y2 and Bline2 >= 0:
                    x1 = H
                    y1 = M*H+C
                    x2 = (W-C)//M
                    y2 = W
                elif X1 < X2 and Y1 > Y2 and Bline2 >= 0:
                    x1 = (W-C)//M
                    y1 = W
                    x2 = H
                    y2 = M*H+C
                elif X1 < X2 and Y1 > Y2 and Bline2 <= 0:
                    x1 = 0
                    y1 = C
                    x2 = -C//M
                    y2 = 0
            # If we are viewing a video and we did not grab a frame then we have reached the end of the video
            rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            # If the frame dimensions are empty, set them initialize the current status along with our list of bounding box rectangles returned by either (1) our object detector or (2) the correlation trackers
            rects = []
        	# Check to see if we should run a more computationally expensive object detection method to aid our tracker
            if totalFrames % skipFrames == 0:
        		# Set the status and initialize our new set of object trackers
                trackers = []
        		# Convert the frame to a blob and pass the blob through the network and obtain the detections
                blob = cv.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)
                net.setInput(blob)
                detections = net.forward()
        		# Loop over the detections
                for i in np.arange(0, detections.shape[2]):
                    # Extract the confidence (i.e., probability) associated with the prediction
                    detectedConfidence = detections[0, 0, i, 2]
        			# Filter out weak detections by requiring a minimum confidence
                    if detectedConfidence > confidence:
        				# Extract the index of the class label from the detections list
                        idx = int(detections[0, 0, i, 1])
        				# If the class label is not a person, ignore it
                        if CLASSES[idx] != obj:
                            continue
        				# Compute the (x, y)-coordinates of the bounding box for the object
                        box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                        (startX, startY, endX, endY) = box.astype("int")
        				# Construct a dlib rectangle object from the bounding box coordinates and then start the dlib correlation tracker
                        tracker = dlib.correlation_tracker()
                        rect = dlib.rectangle(startX, startY, endX, endY)
                        tracker.start_track(rgb, rect)
        				# Add the tracker to our list of trackers so we can utilize it during skip frames
                        trackers.append(tracker)
        	# Otherwise, we should utilize our object *trackers* rather than object *detectors* to obtain a higher frame processing throughput
            else:
        		# Loop over the trackers
                for tracker in trackers:
        			# Update the tracker and grab the updated position
                    tracker.update(rgb)
                    pos = tracker.get_position()
        			# Unpack the position object
                    newStartX = int(pos.left())
                    newStartY = int(pos.top())
                    newEndX = int(pos.right())
                    newEndY = int(pos.bottom())
        			# Add the bounding box coordinates to the rectangles list
                    rects.append((newStartX, newStartY, newEndX, newEndY))
        	# Draw a horizontal line in the center of the frame -- once an object crosses this line we will determine whether they were moving 'up' or 'down'
            cv.line(frame, (x1, y1), (x2, y2), (0, 0, 225), 2)
        	# Use the centroid tracker to associate the (1) old object centroids with (2) the newly computed object centroids
            objects = ct.update(rects)
        	# Loop over the tracked objects
            for (objectID, centroid) in objects.items():
        		# Check to see if a trackable object exists for the current object ID
                to = trackableObjects.get(objectID, None)
        		# If there is no existing trackable object, create one
                if to is None:
                    to = TrackableObject(objectID, centroid)
        		# Otherwise, there is a trackable object so we can utilize it to determine direction
                else:
        			# The difference between the y-coordinate of the *current* centroid and the mean of *previous* centroids will tell us in which direction the object is moving (negative for 'up' and positive for 'down')
                    y = [c[1] for c in to.centroids]
                    direction = centroid[1] - np.mean(y)
                    to.centroids.append(centroid)
                    m = (y2 - y1) // (x2 - x1)
                    c = y1 - m * x1
                    refLine = centroid[1] - m*centroid[0] - c
        			# Check to see if the object has been counted or not
                    if not to.counted:
        				# If the direction is negative (indicating the object is moving up) AND the centroid is above the center line, count the object
                        if  direction > 0 and refLine > 0:
                            totalUp += 1
                            to.counted = True
                        elif direction < 0 and refLine < 0:
                            totalDown += 1
                            to.counted = True
        		# Store the trackable object in our dictionary
                trackableObjects[objectID] = to
        		# Draw both the ID of the object and the centroid of the object on the output frame
                txt = "NO.{} {}".format(objectID+1, CLASSES[idx])
                cv.putText(frame, txt, (centroid[0]-10, centroid[1]-10), cv.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 1)
                cv.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
        	# Construct a tuple of information we will be displaying on the frame
            info = [("Region-1", totalUp),
                    ("Region-2", totalDown)]
        	# Loop over the info tuples and draw them on our frame
            for (i, (k, v)) in enumerate(info):
                text = "{}: {}".format(k, v)
                cv.putText(frame, text, (10, H - ((i * 20) + 20)), cv.FONT_HERSHEY_SIMPLEX, 0.4, (225, 0, 0), 2)
        	# Check to see if we should write the frame to disk
            if writeOutput is True:
                writer.write(frame)
        	# Show the output frame
            cv.imshow("Frame", frame)
            key = cv.waitKey(1) & 0xFF
            # If 'd' is pressed, Clear the Points
            if key == ord("d"):
                points = []
        	# If 'q' is pressed, break from the Loop
            if key == ord("q"):
                points = []
                break
        	# Increment the total number of frames processed thus far and then update the FPS counter
            totalFrames += 1
        # Show and Save Output
        if writeOutput is True:
            writer.release()
        cap.release()
        cv.destroyAllWindows()

# Run the File
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VideoTracker = QtWidgets.QDialog()
    ui = Ui_VideoTracker()
    ui.setupUi(VideoTracker)
    VideoTracker.show()
    sys.exit(app.exec_())
