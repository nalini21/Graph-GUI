from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QMainWindow, QApplication, QGridLayout, QLabel
from PyQt5.QtGui import QPainter, QBrush, QPen
import sys
import os


file  = "mygraph_uifile.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(file)

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        canvas = QtGui.QPixmap(2000,2000)
        self.label.setPixmap(canvas)
        
        self.node=self.edge=self.delete=self.clicked=self.movenode=0
        self.yellow_=self.red_=self.white_=self.green_=self.blue_=0
        self._yellow=self._red=self._white=self._green=self._blue=0
        
        self.Add_node.clicked.connect(self.add_node)
        self.AddEdge.clicked.connect(self.add_edge)
        self.DelNode.clicked.connect(self.delete_node)
        self.move.clicked.connect(self.move_node)
        self.exitB.clicked.connect(self.exitt)
        
        self.redB.clicked.connect(self.red_n)
        self.greenB.clicked.connect(self.green_n)
        self.blueB.clicked.connect(self.blue_n)
        self.yellowB.clicked.connect(self.yellow_n)
        self.whiteB.clicked.connect(self.white_n)
        
        self.redE.clicked.connect(self.red_e)
        self.greenE.clicked.connect(self.green_e)
        self.blueE.clicked.connect(self.blue_e)
        self.yellowE.clicked.connect(self.yellow_e)
        self.whiteE.clicked.connect(self.white_e)
        self.initUI()
     
    def add_node(self):
        if self.node==0:
            self.node=1
            self.edge=0
            self.delete=0
            self.movenode=0
            self.update()
            
    def add_edge(self):
        if self.edge==0:
            self.edge=1
            self.node=0
            self.delete=0
            self.movenode=0
            self.update()
                     
    def move_node(self):
        if self.movenode==0:
            self.movenode=1
            self.delete=0
            self.node=0
            self.edge=0
            self.update()
            
    def delete_node(self):
        if self.delete==0:
            self.delete=1
            self.node=0
            self.edge=0
            self.movenode=0
            self.update()
            
    def exitt(self):
        sys.exit()
        
    def red_n(self):
        if self.red_==0:
            self.yellow_=0
            self.red_=1
            self.white_=0
            self.green_=0
            self.blue_=0
        
    def red_e(self):   
        if self._red==0:
            self._yellow=0
            self._red=1
            self._white=0
            self._green=0
            self._blue=0
            
    def yellow_n(self):
        if self.yellow_==0:
            self.yellow_=1
            self.red_=0
            self.white_=0
            self.green_=0
            self.blue_=0
        
    def yellow_e(self):   
        if self._yellow==0:
            self._yellow=1
            self._red=0
            self._white=0
            self._green=0
            self._blue=0
            
    def green_n(self):
        if self.green_==0:
            self.yellow_=0
            self.red_=0
            self.white_=0
            self.green_=1
            self.blue_=0
        
    def green_e(self):    
        if self._green==0:
            self._yellow=0
            self._red=0
            self._white=0
            self._green=1
            self._blue=0
            
    def blue_n(self):
        if self.blue_==0:
            self.yellow_=0
            self.red_=0
            self.white_=0
            self.green_=0
            self.blue_=1
        
    def blue_e(self):   
        if self._blue==0:
            self._yellow=0
            self._red=0
            self._white=0
            self._green=0
            self._blue=1
            
    def white_n(self):
        if self.white_==0:
            self.yellow_=0
            self.red_=0
            self.white_=1
            self.green_=0
            self.blue_=0
    
    def white_e(self):
        if self._white==0:
            self._yellow=0
            self._red=0
            self._white=1
            self._green=0
            self._blue=0
    
    def initUI(self):      
        self.x = 0
        self.y = 0
        self.vertex=[]
        self.edges=[]
        self.setMouseTracking(True) 
        self.show()    
    
    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()    
    
    def mouseReleaseEvent(self, event):
        if self.node==1:
            if self.x==event.x() and self.y==event.y():
                self.vertex.append([self.x,self.y])
                self.update()
        
        elif self.edge==1:
            if self.x!=event.x() and self.y!=event.y():
                ind1=-1
                ind2=-1
                for i in range(len(self.vertex)):
                    if self.x<self.vertex[i][0]+15 and self.x>self.vertex[i][0]-15 and self.y<self.vertex[i][1]+15 and self.y>self.vertex[i][1]-15:
                        ind1=i
                        
                    if event.x()<self.vertex[i][0]+15 and event.x()>self.vertex[i][0]-15 and event.y()<self.vertex[i][1]+15 and event.y()>self.vertex[i][1]-15:
                        ind2=i
                
                if ind1!=-1 and ind2!=-1:       
                    self.edges.append([self.vertex[ind1],self.vertex[ind2]])
                self.update()
            
        elif self.movenode==1:
            if self.x!=event.x() and self.y!=event.y():
                ind=-1
                for i in range(len(self.vertex)):
                    if self.x<self.vertex[i][0]+15 and self.x>self.vertex[i][0]-15 and self.y<self.vertex[i][1]+15 and self.y>self.vertex[i][1]-15:
                        ind=i
                        break
                arr=[]
                if ind!=-1:
                    for i in range(len(self.edges)):
                        if self.vertex[ind] in self.edges[i]:
                            self.edges[i].remove(self.vertex[ind])
                            self.edges[i].append([event.x(),event.y()])
                        
                    del self.vertex[ind]
                    self.vertex.append([event.x(),event.y()])
                    
                canvas = QtGui.QPixmap(2000,2000)
                self.label.setPixmap(canvas)
                self.update()
                
        elif self.delete==1:
            if self.x==event.x() and self.y==event.y():
                ind=-1
                for i in range(len(self.vertex)):
                    if self.x<self.vertex[i][0]+15 and self.x>self.vertex[i][0]-15 and self.y<self.vertex[i][1]+15 and self.y>self.vertex[i][1]-15:
                        ind=i
                        break
                arr=[]
                if ind!=-1:
                    for i in range(len(self.edges)):
                        if self.vertex[ind] not in self.edges[i]:
                            arr.append(self.edges[i])

                    self.edges=arr

                    arr=[]
                    for i in range(len(self.vertex)):
                        if i!=ind:
                            arr.append(self.vertex[i])
                    self.vertex=arr
                canvas = QtGui.QPixmap(2000,2000)
                self.label.setPixmap(canvas)
                self.update()
                    
    def paintEvent(self, event):
        q = QPainter(self.label.pixmap())
        if(self.green_==1):
            q.setPen(QPen(Qt.green, 8, Qt.SolidLine))
            q.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            self.update()
        elif(self.red_==1):
            q.setPen(QPen(Qt.red,  8, Qt.SolidLine))
            q.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            self.update()
        elif(self.yellow_==1):
            q.setPen(QPen(Qt.yellow,  8, Qt.SolidLine))
            q.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            self.update()
        elif(self.white_==1):
            q.setPen(QPen(Qt.white,  8, Qt.SolidLine))
            q.setBrush(QBrush(Qt.white, Qt.SolidPattern))
            self.update()
        elif(self.blue_==1):
            q.setPen(QPen(Qt.blue,  8, Qt.SolidLine))
            q.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            self.update()
        else:
            q.setPen(QPen(Qt.white,  8, Qt.SolidLine))
            q.setBrush(QBrush(Qt.white, Qt.SolidPattern))
            
        for pt in self.vertex:
            q.drawEllipse(QtCore.QPoint(pt[0]-38, pt[1]+500),7, 7)
        
        if(self._green==1):
            q.setPen(QPen(Qt.green, 5, Qt.SolidLine))
            q.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            self.update()
        elif(self._red==1):
            q.setPen(QPen(Qt.red, 5, Qt.SolidLine))
            q.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            self.update()
        elif(self._yellow==1):
            q.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
            q.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            self.update()
        elif(self._white==1):
            q.setPen(QPen(Qt.white, 5, Qt.SolidLine))
            q.setBrush(QBrush(Qt.white, Qt.SolidPattern))
            self.update()
        elif(self._blue==1):
            q.setPen(QPen(Qt.blue, 5, Qt.SolidLine))
            q.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            self.update()
        else:
            q.setPen(QPen(Qt.white, 5, Qt.SolidLine))
            q.setBrush(QBrush(Qt.white, Qt.SolidPattern))
            
        for i in range(len(self.edges)):
            q.drawLine(self.edges[i][0][0]-38,self.edges[i][0][1]+500,self.edges[i][1][0]-38,self.edges[i][1][1]+500)
            
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())