from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from datetime import datetime
import psycopg2
global str

class Ventana_Emergente_No_Inventario(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana_Emergente_No_Inventario, self).__init__(parent)

        self.setFixedSize(400,200)
        self.setWindowTitle("Error")
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(u"background-color:rgb(177, 114, 182)")
        
        label = QLabel("No hay productos suficientes",self)
        label.setGeometry(30,50 , 350, 40)
        label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        label.setStyleSheet(u"color:rgb(255, 255, 255)")

        boton_cerrar = QPushButton("Cerrar", self)
        boton_cerrar.setGeometry(QRect(150, 100, 100, 31))
        boton_cerrar.setFont(font)
        boton_cerrar.clicked.connect(lambda: self.close())

        

class Menu_Principal(QMainWindow):
    def __init__(self, parent=None):
        super(Menu_Principal, self).__init__(parent)
        self.setFixedSize(1920,1040)
        self.setWindowTitle("CONSTRUCTORA CASTRO")
        logo = QtGui.QIcon()
        logo.addFile('logo.png', QtCore.QSize(48,48))
        self.setWindowIcon(QIcon(logo))
        self.setWindowFlag(Qt.FramelessWindowHint) #METODO PARAQUITAR BOTONES DE ARRIBA
        self.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.frame_superior = QFrame(self)
        self.frame_superior.setGeometry(QRect(0, 0, 1920, 51))
        self.frame_superior.setStyleSheet(u"background-color:rgb(215, 181, 216)")

        self.frame_izquierdo = QFrame(self)
        self.frame_izquierdo.setGeometry(QRect(0, 50, 281, 990))
        self.frame_izquierdo.setMaximumSize(QSize(0, 16777215))
        self.frame_izquierdo.setStyleSheet(u"background-color:rgb(177, 114, 182)")
        self.frame_izquierdo.setFrameShape(QFrame.StyledPanel)
        self.frame_izquierdo.setFrameShadow(QFrame.Raised)

        self.boton_cerrar = QPushButton(self.frame_superior)
        self.boton_cerrar.setGeometry(QRect(1870, 10, 41, 31))
        self.boton_cerrar.setIcon(QIcon("x.png"))
        self.boton_cerrar.setIconSize(QSize(32, 32))
        self.boton_cerrar.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);}")
        self.boton_cerrar.clicked.connect(lambda: self.close())

        self.boton_minimizar = QPushButton(self.frame_superior)
        self.boton_minimizar.setGeometry(QRect(1820, 10, 41, 31))
        self.boton_minimizar.setIcon(QIcon("minimize.png"))
        self.boton_minimizar.setIconSize(QSize(32, 32))
        self.boton_minimizar.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);}")
        self.boton_minimizar.clicked.connect(self.minimizar)

        self.boton_sacar_menu = QPushButton(self.frame_superior)
        self.boton_sacar_menu.setGeometry(QRect(10, 10, 41, 31))
        self.boton_sacar_menu.setIcon(QIcon("menu.png"))
        self.boton_sacar_menu.setIconSize(QSize(32, 32))
        self.boton_sacar_menu.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);}")
        self.boton_sacar_menu.clicked.connect(lambda: self.moverderecha())

        self.label_menu = QLabel("MENU",self.frame_superior)
        self.label_menu.setGeometry(QRect(60, 10, 71, 31))
        self.label_menu.setStyleSheet(u"color:rgb(0, 0, 0)")
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_menu.setFont(font)

        self.click = QShortcut(QKeySequence('Return'), self)
        
        self.toolBox = QToolBox(self.frame_izquierdo)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(0, 0, 281, 721))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.toolBox.setFont(font1)

        self.compras = QWidget()
        self.compras.setGeometry(QRect(0, 0, 281, 392))
        self.compras.setStyleSheet(u"background-color:rgb(152, 68, 158)")
        icon1 = QIcon()
        icon1.addFile(u"carrito-de-compras (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.compras, icon1, u" COMPRAS")

        self.ventas = QWidget()
        self.ventas.setGeometry(QRect(0, 0, 281, 392))
        self.ventas.setStyleSheet(u"background-color:rgb(152, 68, 158)")
        icon2 = QIcon()
        icon2.addFile(u"ventas (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.ventas, icon2, u" VENTAS")
        
        self.inventario = QWidget()
        self.inventario.setGeometry(QRect(0, 0, 281, 392))
        self.inventario.setStyleSheet(u"background-color:rgb(152, 68, 158)")
        icon3 = QIcon()
        icon3.addFile(u"inventario-disponible (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.inventario, icon3, u" INVENTARIO")

        self.clientes = QWidget()
        self.clientes.setGeometry(QRect(0, 0, 281, 392))
        self.clientes.setStyleSheet(u"background-color:rgb(152, 68, 158)")
        icon4 = QIcon()
        icon4.addFile(u"cliente (1).png", QSize(), QIcon.Normal, QIcon.Off)        
        self.toolBox.addItem(self.clientes, icon4, u" CLIENTES")

        self.proveedores = QWidget()
        self.proveedores.setGeometry(QRect(0, 0, 281, 392))
        self.proveedores.setStyleSheet(u"background-color:rgb(152, 68, 158)")
        icon5 = QIcon()
        icon5.addFile(u"administracion.png", QSize(), QIcon.Normal, QIcon.Off)  
        self.toolBox.addItem(self.proveedores, icon5, u" PROVEEDORES")

        self.trabajadores = QWidget()
        self.trabajadores.setGeometry(QRect(0, 0, 281, 392))
        self.trabajadores.setStyleSheet(u"background-color:rgb(152, 68, 158)")
        icon6 = QIcon()
        icon6.addFile(u"cientifico-de-la-computacion.png", QSize(), QIcon.Normal, QIcon.Off)  
        self.toolBox.addItem(self.trabajadores, icon6, u" TRABAJADORES")

        self.proyectos = QWidget()
        self.proyectos.setGeometry(QRect(0, 0, 281, 392))
        self.proyectos.setStyleSheet(u"background-color:rgb(152, 68, 158)")
        icon7 = QIcon()
        icon7.addFile(u"gerente-de-proyecto.png", QSize(), QIcon.Normal, QIcon.Off)  
        self.toolBox.addItem(self.proyectos, icon7,u" PROYECTOS")

        self.hacer_compra = QPushButton("  HACER COMPRA",self.compras)
        self.hacer_compra.setGeometry(QRect(10, 20, 250, 41))
        font1 = QFont()
        font1.setFamily(u"Arial Narrow")
        font1.setPointSize(12)
        self.hacer_compra.setFont(font1)
        self.hacer_compra.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon = QIcon()
        icon.addFile(u"hacercompra.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hacer_compra.setIcon(icon)
        self.hacer_compra.setIconSize(QSize(32, 32))

        self.mostrar_compras = QPushButton("  MOSTRAR COMPRAS",self.compras)
        self.mostrar_compras.setGeometry(QRect(10, 80, 250, 41))
        self.mostrar_compras.setFont(font1)
        self.mostrar_compras.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"mostrarcompras.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mostrar_compras.setIcon(icon1)
        self.mostrar_compras.setIconSize(QSize(32, 32))

        self.buscar_compra = QPushButton("  BUSCAR COMPRA",self.compras)
        self.buscar_compra.setGeometry(QRect(10, 140, 250, 41))
        self.buscar_compra.setFont(font1)
        self.buscar_compra.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"buscar_compra.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_compra.setIcon(icon2)
        self.buscar_compra.setIconSize(QSize(32, 32))

        self.agregar_venta = QPushButton("  HACER VENTA",self.ventas)
        self.agregar_venta.setGeometry(QRect(10, 20, 250, 41))
        self.agregar_venta.setFont(font1)
        self.agregar_venta.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"hacerventa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_venta.setIcon(icon4)
        self.agregar_venta.setIconSize(QSize(32, 32))

        self.mostrar_venta = QPushButton("  MOSTRAR VENTAS",self.ventas)
        self.mostrar_venta.setGeometry(QRect(10, 80, 250, 41))
        self.mostrar_venta.setFont(font1)
        self.mostrar_venta.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"mostrarventa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mostrar_venta.setIcon(icon5)
        self.mostrar_venta.setIconSize(QSize(32, 32))

        self.buscar_venta = QPushButton("  BUSCAR VENTA",self.ventas)
        self.buscar_venta.setGeometry(QRect(10, 140, 250, 41))
        self.buscar_venta.setFont(font1)
        self.buscar_venta.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"buscarventa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_venta.setIcon(icon6)
        self.buscar_venta.setIconSize(QSize(32, 32))

        self.agregar_producto = QPushButton("  AGREGAR PRODUCTO",self.inventario)
        self.agregar_producto.setGeometry(QRect(10, 20, 250, 41))
        self.agregar_producto.setFont(font1)
        self.agregar_producto.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"agregarproducto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_producto.setIcon(icon7)
        self.agregar_producto.setIconSize(QSize(32, 32))

        self.modificar_producto = QPushButton("  MODIFICAR PRODUCTO",self.inventario)
        self.modificar_producto.setGeometry(QRect(10, 80, 250, 41))
        self.modificar_producto.setFont(font1)
        self.modificar_producto.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"modificarproducto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modificar_producto.setIcon(icon8)
        self.modificar_producto.setIconSize(QSize(32, 32))

        self.buscar_producto = QPushButton("  BUSCAR PRODUCTO",self.inventario)
        self.buscar_producto.setGeometry(QRect(10, 140, 250, 41))
        self.buscar_producto.setFont(font1)
        self.buscar_producto.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"buscar_producto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_producto.setIcon(icon9)
        self.buscar_producto.setIconSize(QSize(32, 32))

        self.mostrar_producto = QPushButton("  MOSTRAR PRODUCTOS",self.inventario)
        self.mostrar_producto.setGeometry(QRect(10, 200, 250, 41))
        self.mostrar_producto.setFont(font1)
        self.mostrar_producto.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"mostrar_producto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mostrar_producto.setIcon(icon10)
        self.mostrar_producto.setIconSize(QSize(32, 32))

        self.agregar_cliente = QPushButton("  AGREGAR CLIENTE",self.clientes)
        self.agregar_cliente.setGeometry(QRect(10, 20, 250, 41))
        self.agregar_cliente.setFont(font1)
        self.agregar_cliente.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"agregarcliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_cliente.setIcon(icon11)
        self.agregar_cliente.setIconSize(QSize(32, 32))

        self.modificar_cliente = QPushButton("  MODIFICAR CLIENTE",self.clientes)
        self.modificar_cliente.setGeometry(QRect(10, 80, 250, 41))
        self.modificar_cliente.setFont(font1)
        self.modificar_cliente.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u"modificarcliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modificar_cliente.setIcon(icon12)
        self.modificar_cliente.setIconSize(QSize(32, 32))

        self.buscar_cliente = QPushButton("  BUSCAR CLIENTE",self.clientes)
        self.buscar_cliente.setObjectName(u"buscar_cliente")
        self.buscar_cliente.setGeometry(QRect(10, 140, 250, 41))
        self.buscar_cliente.setFont(font1)
        self.buscar_cliente.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u"mostrarcliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_cliente.setIcon(icon13)
        self.buscar_cliente.setIconSize(QSize(32, 32))

        self.mostrar_cliente = QPushButton("  MOSTRAR CLIENTES",self.clientes)
        self.mostrar_cliente.setObjectName(u"mostrar_cliente")
        self.mostrar_cliente.setGeometry(QRect(10, 200, 250, 41))
        self.mostrar_cliente.setFont(font1)
        self.mostrar_cliente.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u"buscarcliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mostrar_cliente.setIcon(icon14)
        self.mostrar_cliente.setIconSize(QSize(32, 32))

        self.agregar_proveedor = QPushButton("  AGREGAR PROVEEDOR",self.proveedores)
        self.agregar_proveedor.setGeometry(QRect(10, 20, 250, 41))
        self.agregar_proveedor.setFont(font1)
        self.agregar_proveedor.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u"agregarproveedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_proveedor.setIcon(icon15)
        self.agregar_proveedor.setIconSize(QSize(32, 32))

        self.modificar_proveedor = QPushButton("  MODIFICAR PROVEEDOR",self.proveedores)
        self.modificar_proveedor.setGeometry(QRect(10, 80, 250, 41))
        self.modificar_proveedor.setFont(font1)
        self.modificar_proveedor.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon16 = QIcon()
        icon16.addFile(u"modificarproveedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modificar_proveedor.setIcon(icon16)
        self.modificar_proveedor.setIconSize(QSize(32, 32))

        self.mostrar_proveedor = QPushButton("  MOSTRAR PROVEEDORES",self.proveedores)
        self.mostrar_proveedor.setGeometry(QRect(10, 200, 250, 41))
        self.mostrar_proveedor.setFont(font1)
        self.mostrar_proveedor.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon17 = QIcon()
        icon17.addFile(u"mostrarproveedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mostrar_proveedor.setIcon(icon17)
        self.mostrar_proveedor.setIconSize(QSize(32, 32))

        self.buscar_proveedor = QPushButton("  BUSCAR PROVEEDOR", self.proveedores)
        self.buscar_proveedor.setGeometry(QRect(10, 140, 250, 41))
        self.buscar_proveedor.setFont(font1)
        self.buscar_proveedor.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon18 = QIcon()
        icon18.addFile(u"buscarproveedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_proveedor.setIcon(icon18)
        self.buscar_proveedor.setIconSize(QSize(32, 32))

        self.agregar_trabajador = QPushButton("  AGREGAR TRABAJADOR",self.trabajadores)
        self.agregar_trabajador.setGeometry(QRect(10, 20, 250, 41))
        self.agregar_trabajador.setFont(font1)
        self.agregar_trabajador.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon19 = QIcon()
        icon19.addFile(u"agregartrabajador.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_trabajador.setIcon(icon19)
        self.agregar_trabajador.setIconSize(QSize(32, 32))

        self.modificar_trabajador = QPushButton("  MODIFICAR TRABAJADOR",self.trabajadores)
        self.modificar_trabajador.setGeometry(QRect(10, 80, 250, 41))
        self.modificar_trabajador.setFont(font1)
        self.modificar_trabajador.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon20 = QIcon()
        icon20.addFile(u"modificartrabajador.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modificar_trabajador.setIcon(icon20)
        self.modificar_trabajador.setIconSize(QSize(32, 32))

        self.buscar_trabajador = QPushButton("  BUSCAR TRABAJADOR",self.trabajadores)
        self.buscar_trabajador.setGeometry(QRect(10, 140, 250, 41))
        self.buscar_trabajador.setFont(font1)
        self.buscar_trabajador.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon21 = QIcon()
        icon21.addFile(u"buscartrabajador.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_trabajador.setIcon(icon21)
        self.buscar_trabajador.setIconSize(QSize(32, 32))

        self.mostrar_trabajador = QPushButton("  MOSTRAR TRABAJADORES",self.trabajadores)
        self.mostrar_trabajador.setGeometry(QRect(10, 200, 250, 41))
        self.mostrar_trabajador.setFont(font1)
        self.mostrar_trabajador.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon22 = QIcon()
        icon22.addFile(u"mostrartrabajador.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mostrar_trabajador.setIcon(icon22)
        self.mostrar_trabajador.setIconSize(QSize(32, 32))

        self.busca_proyecto = QPushButton("  BUSCAR PROYECTO",self.proyectos)
        self.busca_proyecto.setGeometry(QRect(10, 140, 250, 41))
        self.busca_proyecto.setFont(font1)
        self.busca_proyecto.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon23 = QIcon()
        icon23.addFile(u"buscarproyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.busca_proyecto.setIcon(icon23)
        self.busca_proyecto.setIconSize(QSize(32, 32))

        self.modificar_proyecto = QPushButton("  MODIFICAR PROYECTO",self.proyectos)
        self.modificar_proyecto.setGeometry(QRect(10, 80, 250, 41))
        self.modificar_proyecto.setFont(font1)
        self.modificar_proyecto.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
        "border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon24 = QIcon()
        icon24.addFile(u"modificarproyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modificar_proyecto.setIcon(icon24)
        self.modificar_proyecto.setIconSize(QSize(32, 32))

        self.agregar_proyecto = QPushButton("  AGREGAR PROYECTO",self.proyectos)
        self.agregar_proyecto.setObjectName(u"agregar_proyecto")
        self.agregar_proyecto.setGeometry(QRect(10, 20, 250, 41))
        self.agregar_proyecto.setFont(font1)
        self.agregar_proyecto.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon25 = QIcon()
        icon25.addFile(u"agregarproyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_proyecto.setIcon(icon25)
        self.agregar_proyecto.setIconSize(QSize(32, 32))

        self.mostrar_proyectos = QPushButton("  MOSTRAR PROYECTOS",self.proyectos)
        self.mostrar_proyectos.setGeometry(QRect(10, 200, 250, 41))
        self.mostrar_proyectos.setFont(font1)
        self.mostrar_proyectos.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"")
        icon26 = QIcon()
        icon26.addFile(u"mostrarproyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mostrar_proyectos.setIcon(icon26)
        self.mostrar_proyectos.setIconSize(QSize(32, 32))
#####IVA####
        self.agregar_iva = QPushButton(self.frame_superior)
        self.agregar_iva.setGeometry(QRect(130, 5, 40, 41))
        self.agregar_iva.setFont(font1)
        self.agregar_iva.setStyleSheet(u"QPushButton:hover{background-color:rgb(255, 255, 255);border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;}\n"
"QPushButton{background-color:rgb(129, 34, 141); \n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px;}\n"
"")
        icon26 = QIcon()
        icon26.addFile(u"iva.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_iva.setIcon(icon26)
        self.agregar_iva.setIconSize(QSize(32, 32))


############################################################################################################################################
#################################################################################STACKED WIDGET#############################################
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setGeometry(QRect(281, 50, 1639, 990))
        self.stackedWidget.setStyleSheet(u"background:rgb(111, 32, 164)")

        self.page = QWidget()
        self.page.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.logo = QLabel(self.page)
        self.logo.setGeometry(QRect(0, 0, 1639 , 1100))
        self.logo.setPixmap(QPixmap(u"logo.png"))
        self.stackedWidget.addWidget(self.page)

##############################################INVENTARIO########################################################################################################
######AGREGAR PRODUCTO####################
        self.pagina_agregar_producto = QWidget()
        self.fecha = QLabel("Fecha:",self.pagina_agregar_producto)
        self.fecha.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha.setGeometry(QRect(1340, 40, 70, 30))
        self.stackedWidget.addWidget(self.pagina_agregar_producto)
        self.fecha.setFont(font)

        self.ahora = datetime.now()
        self.fecha_resul = self.ahora.strftime(("%d/%m/%Y"))

        self.fecha_datos = QLabel(self.pagina_agregar_producto)
        self.fecha_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_datos.setGeometry(QRect(1420, 40, 114, 30))
        self.fecha_datos.setFont(font)
        self.fecha_datos.setText(self.fecha_resul)

        self.codigo_producto = QLabel("Codigo de Producto:",self.pagina_agregar_producto)
        self.codigo_producto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_producto.setGeometry(QRect(40, 80, 215, 30))
        self.codigo_producto.setFont(font)

        self.codigo_producto_datos = QLabel(self.pagina_agregar_producto)
        self.codigo_producto_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_producto_datos.setGeometry(QRect(260, 80, 100, 30))
        self.codigo_producto_datos.setFont(font)
        self.codigo_producto_datos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.nombre_producto = QLabel("Nombre de Producto:",self.pagina_agregar_producto)
        self.nombre_producto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.nombre_producto.setGeometry(QRect(40, 120, 225, 30))
        self.nombre_producto.setFont(font)

        self.nombre_producto_datos = QLineEdit(self.pagina_agregar_producto)
        self.nombre_producto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.nombre_producto_datos.setGeometry(QRect(270, 120, 500, 30))
        self.nombre_producto_datos.setFont(font)

        self.marca_producto = QLabel("Marca de Producto:",self.pagina_agregar_producto)
        self.marca_producto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.marca_producto.setGeometry(QRect(40, 160, 210, 30))
        self.marca_producto.setFont(font)

        self.marca_producto_datos = QLineEdit(self.pagina_agregar_producto)
        self.marca_producto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.marca_producto_datos.setGeometry(QRect(255, 160, 300, 30))
        self.marca_producto_datos.setFont(font)

        self.tipo_producto = QLabel("Tipo de Producto:",self.pagina_agregar_producto)
        self.tipo_producto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.tipo_producto.setGeometry(QRect(40, 200, 210, 30))
        self.tipo_producto.setFont(font)

        self.comboBox_tipo_producto_datos = QComboBox(self.pagina_agregar_producto)
        self.comboBox_tipo_producto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.comboBox_tipo_producto_datos.addItem("Maquinaria")
        self.comboBox_tipo_producto_datos.addItem("Herramienta")
        self.comboBox_tipo_producto_datos.addItem("Arena")
        self.comboBox_tipo_producto_datos.addItem("Estructural")
        self.comboBox_tipo_producto_datos.addItem("Envolvente")
        self.comboBox_tipo_producto_datos.addItem("Carpinteria")
        self.comboBox_tipo_producto_datos.addItem("Acabado")
        self.comboBox_tipo_producto_datos.setGeometry(QRect(255, 200, 150, 30))
        self.comboBox_tipo_producto_datos.setFont(font)

        self.precio_producto = QLabel("Precio de Producto:",self.pagina_agregar_producto)
        self.precio_producto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.precio_producto.setGeometry(QRect(40, 240, 210, 30))
        self.precio_producto.setFont(font)

        self.precio_producto_datos = QLineEdit(self.pagina_agregar_producto)
        self.precio_producto_datos.setPlaceholderText("45")
        self.precio_producto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.precio_producto_datos.setGeometry(QRect(255, 240, 100, 30))
        self.precio_producto_datos.setFont(font)

        self.boton_añadir_producto = QPushButton("Añadir Producto", self.pagina_agregar_producto)
        self.boton_añadir_producto.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_añadir_producto.setGeometry(QRect(40, 280, 120, 30))
        self.boton_añadir_producto.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_añadir_producto.setIcon(icon27)
        self.boton_añadir_producto.setIconSize(QSize(18, 18))

        self.tabla_agregar_inventario = QTableWidget(self.pagina_agregar_producto)
        if (self.tabla_agregar_inventario.columnCount() < 7):
            self.tabla_agregar_inventario.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("NOMBRE")
        self.tabla_agregar_inventario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("CODIGO PRODUCTO")
        self.tabla_agregar_inventario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_agregar_inventario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("MARCA")
        self.tabla_agregar_inventario.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("TIPO")
        self.tabla_agregar_inventario.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("CANTIDAD")
        self.tabla_agregar_inventario.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("PRECIO")
        self.tabla_agregar_inventario.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_agregar_inventario.setColumnWidth(0,214)
        self.tabla_agregar_inventario.setColumnWidth(1,214)
        self.tabla_agregar_inventario.setColumnWidth(2,214)
        self.tabla_agregar_inventario.setColumnWidth(3,214)
        self.tabla_agregar_inventario.setColumnWidth(4,214)
        self.tabla_agregar_inventario.setColumnWidth(5,214)
        self.tabla_agregar_inventario.setColumnWidth(6,214)

        self.tabla_agregar_inventario.setGeometry(QRect(40, 370, 1500, 200))
        self.tabla_agregar_inventario.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")
#########MODIFICAR PRODUCTO##########################################     
        self.pagina_modificar_producto = QWidget()
        self.stackedWidget.addWidget(self.pagina_modificar_producto)

        self.label_codigo_modificar_producto = QLabel("Codigo de producto a cambiar:",self.pagina_modificar_producto)
        self.label_codigo_modificar_producto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_producto.setGeometry(QRect(40, 330, 325, 30))
        self.label_codigo_modificar_producto.setFont(font)

        self.label_codigo_modificar_producto_datos = QLineEdit(self.pagina_modificar_producto)
        self.label_codigo_modificar_producto_datos.setPlaceholderText("1")
        self.label_codigo_modificar_producto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_producto_datos.setGeometry(QRect(370, 330, 350, 30))
        self.label_codigo_modificar_producto_datos.setFont(font)

        self.label_codigo_modificar_producto_informacion = QLabel(self.pagina_modificar_producto)
        self.label_codigo_modificar_producto_informacion.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_producto_informacion.setGeometry(QRect(725, 330, 700, 30))
        self.label_codigo_modificar_producto_informacion.setFont(font)

        self.label_modificar_producto = QLabel("Campo de producto a cambiar:",self.pagina_modificar_producto)
        self.label_modificar_producto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_modificar_producto.setGeometry(QRect(40, 370, 325, 30))
        self.label_modificar_producto.setFont(font)

        self.modificar_producto_datos = QLineEdit(self.pagina_modificar_producto)
        self.modificar_producto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.modificar_producto_datos.setGeometry(QRect(370, 370, 350, 30))
        self.modificar_producto_datos.setFont(font)

        self.comboBox_label_modificar_producto = QComboBox(self.pagina_modificar_producto)
        self.comboBox_label_modificar_producto.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.comboBox_label_modificar_producto.addItem("Nombre")
        self.comboBox_label_modificar_producto.addItem("Marca")
        self.comboBox_label_modificar_producto.addItem("Tipo")
        self.comboBox_label_modificar_producto.addItem("Cantidad")
        self.comboBox_label_modificar_producto.addItem("Precio")
        self.comboBox_label_modificar_producto.setGeometry(QRect(730, 370, 150, 30))
        self.comboBox_label_modificar_producto.setFont(font)

        self.boton_modificar_producto = QPushButton("Modificar Producto", self.pagina_modificar_producto)
        self.boton_modificar_producto.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_modificar_producto.setGeometry(QRect(885, 370, 160, 30))
        self.boton_modificar_producto.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_modificar_producto.setIcon(icon27)
        self.boton_modificar_producto.setIconSize(QSize(18, 18))

        self.tabla_modificar_inventario = QTableWidget(self.pagina_modificar_producto)
        if (self.tabla_modificar_inventario.columnCount() < 7):
            self.tabla_modificar_inventario.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("NOMBRE")
        self.tabla_modificar_inventario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("CODIGO PRODUCTO")
        self.tabla_modificar_inventario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_modificar_inventario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("MARCA")
        self.tabla_modificar_inventario.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("TIPO")
        self.tabla_modificar_inventario.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("CANTIDAD")
        self.tabla_modificar_inventario.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("PRECIO")
        self.tabla_modificar_inventario.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_modificar_inventario.setColumnWidth(0,214)
        self.tabla_modificar_inventario.setColumnWidth(1,214)
        self.tabla_modificar_inventario.setColumnWidth(2,214)
        self.tabla_modificar_inventario.setColumnWidth(3,214)
        self.tabla_modificar_inventario.setColumnWidth(4,214)
        self.tabla_modificar_inventario.setColumnWidth(5,214)
        self.tabla_modificar_inventario.setColumnWidth(6,214)

        self.tabla_modificar_inventario.setGeometry(QRect(40, 410, 1500, 200))
        self.tabla_modificar_inventario.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

####BUSCAR PRODUCTO##################
        self.pagina_buscar_producto = QWidget()
        self.stackedWidget.addWidget(self.pagina_buscar_producto)
        self.label_buscar_producto = QLabel("Codigo de producto a buscar:",self.pagina_buscar_producto)
        self.label_buscar_producto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_buscar_producto.setGeometry(QRect(40, 370, 325, 30))
        self.label_buscar_producto.setFont(font)

        self.buscar_producto_datos = QLineEdit(self.pagina_buscar_producto)
        self.buscar_producto_datos.setPlaceholderText("1")
        self.buscar_producto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.buscar_producto_datos.setGeometry(QRect(370, 370, 350, 30))
        self.buscar_producto_datos.setFont(font)

        self.boton_buscar_producto = QPushButton("Buscar Producto", self.pagina_buscar_producto)
        self.boton_buscar_producto.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_buscar_producto.setGeometry(QRect(725, 370, 160, 30))
        self.boton_buscar_producto.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_buscar_producto.setIcon(icon27)
        self.boton_buscar_producto.setIconSize(QSize(18, 18))

        self.tabla_buscar_inventario = QTableWidget(self.pagina_buscar_producto)
        if (self.tabla_buscar_inventario.columnCount() < 7):
            self.tabla_buscar_inventario.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("NOMBRE")
        self.tabla_buscar_inventario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("CODIGO PRODUCTO")
        self.tabla_buscar_inventario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_buscar_inventario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("MARCA")
        self.tabla_buscar_inventario.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("TIPO")
        self.tabla_buscar_inventario.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("CANTIDAD")
        self.tabla_buscar_inventario.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("PRECIO")
        self.tabla_buscar_inventario.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_buscar_inventario.setColumnWidth(0,214)
        self.tabla_buscar_inventario.setColumnWidth(1,214)
        self.tabla_buscar_inventario.setColumnWidth(2,214)
        self.tabla_buscar_inventario.setColumnWidth(3,214)
        self.tabla_buscar_inventario.setColumnWidth(4,214)
        self.tabla_buscar_inventario.setColumnWidth(5,214)
        self.tabla_buscar_inventario.setColumnWidth(6,214)

        self.tabla_buscar_inventario.setGeometry(QRect(40, 410, 1500, 400))
        self.tabla_buscar_inventario.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

#############MOSTRAR PRODUCTOS################
        self.pagina_mostrar_producto = QWidget()
        self.stackedWidget.addWidget(self.pagina_mostrar_producto)

        self.tabla_mostrar_inventario = QTableWidget(self.pagina_mostrar_producto)
        if (self.tabla_mostrar_inventario.columnCount() < 7):
            self.tabla_mostrar_inventario.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO PRODUCTO")
        self.tabla_mostrar_inventario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_mostrar_inventario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_mostrar_inventario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("MARCA")
        self.tabla_mostrar_inventario.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("TIPO")
        self.tabla_mostrar_inventario.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("CANTIDAD")
        self.tabla_mostrar_inventario.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("PRECIO")
        self.tabla_mostrar_inventario.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_mostrar_inventario.setColumnWidth(0,214)
        self.tabla_mostrar_inventario.setColumnWidth(1,214)
        self.tabla_mostrar_inventario.setColumnWidth(2,214)
        self.tabla_mostrar_inventario.setColumnWidth(3,214)
        self.tabla_mostrar_inventario.setColumnWidth(4,214)
        self.tabla_mostrar_inventario.setColumnWidth(5,214)
        self.tabla_mostrar_inventario.setColumnWidth(6,214)

        self.tabla_mostrar_inventario.setGeometry(QRect(40, 110, 1500, 700))
        self.tabla_mostrar_inventario.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

############################# CLIENTE ###############################################################################
###### AGREGAR CLIENTE ###################
        self.pagina_agregar_cliente = QWidget()
        self.fecha = QLabel("Fecha:",self.pagina_agregar_cliente)
        self.fecha.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha.setGeometry(QRect(1340, 40, 70, 30))
        self.stackedWidget.addWidget(self.pagina_agregar_cliente)
        self.fecha.setFont(font)

        self.ahora = datetime.now()
        self.fecha_resul = self.ahora.strftime(("%d/%m/%Y"))

        self.fecha_datos = QLabel(self.pagina_agregar_cliente)
        self.fecha_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_datos.setGeometry(QRect(1420, 40, 114, 30))
        self.fecha_datos.setFont(font)
        self.fecha_datos.setText(self.fecha_resul)

        self.codigo_cliente = QLabel("Codigo de Cliente:",self.pagina_agregar_cliente)
        self.codigo_cliente.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_cliente.setGeometry(QRect(40, 80, 200, 30))
        self.codigo_cliente.setFont(font)

        self.codigo_cliente_datos = QLabel(self.pagina_agregar_cliente)
        self.codigo_cliente_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_cliente_datos.setGeometry(QRect(245, 80, 100, 30))
        self.codigo_cliente_datos.setFont(font)
        self.codigo_cliente_datos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.nombre_cliente = QLabel("Nombre de Cliente:",self.pagina_agregar_cliente)
        self.nombre_cliente.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.nombre_cliente.setGeometry(QRect(40, 120, 210, 30))
        self.nombre_cliente.setFont(font)

        self.nombre_cliente_datos = QLineEdit(self.pagina_agregar_cliente)
        self.nombre_cliente_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.nombre_cliente_datos.setGeometry(QRect(255, 120, 500, 30))
        self.nombre_cliente_datos.setFont(font)

        self.rfc_cliente = QLabel("RFC:",self.pagina_agregar_cliente)
        self.rfc_cliente.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.rfc_cliente.setGeometry(QRect(40, 160, 60, 30))
        self.rfc_cliente.setFont(font)

        self.rfc_cliente_datos = QLineEdit(self.pagina_agregar_cliente)
        self.rfc_cliente_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.rfc_cliente_datos.setGeometry(QRect(105, 160, 180, 30))
        self.rfc_cliente_datos.setFont(font)

        self.email_cliente = QLabel("Email:",self.pagina_agregar_cliente)
        self.email_cliente.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.email_cliente.setGeometry(QRect(40, 200, 70, 30))
        self.email_cliente.setFont(font)

        self.email_cliente_datos = QLineEdit(self.pagina_agregar_cliente)
        self.email_cliente_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.email_cliente_datos.setGeometry(QRect(115, 200, 400, 30))
        self.email_cliente_datos.setFont(font)

        self.telefono_cliente = QLabel("Telefono:",self.pagina_agregar_cliente)
        self.telefono_cliente.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.telefono_cliente.setGeometry(QRect(40, 240, 100, 30))
        self.telefono_cliente.setFont(font)

        self.telefono_cliente_datos = QLineEdit(self.pagina_agregar_cliente)
        self.telefono_cliente_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.telefono_cliente_datos.setGeometry(QRect(145, 240, 200, 30))
        self.telefono_cliente_datos.setFont(font)

        self.direccion_cliente = QLabel("Direccion:",self.pagina_agregar_cliente)
        self.direccion_cliente.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.direccion_cliente.setGeometry(QRect(40, 280, 110, 30))
        self.direccion_cliente.setFont(font)

        self.direccion_cliente_datos = QLineEdit(self.pagina_agregar_cliente)
        self.direccion_cliente_datos.setPlaceholderText("Calle, Colonia, Ciudad Estado")
        self.direccion_cliente_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.direccion_cliente_datos.setGeometry(QRect(155, 280, 750, 30))
        self.direccion_cliente_datos.setFont(font)

        self.boton_añadir_cliente = QPushButton("Añadir Cliente", self.pagina_agregar_cliente)
        self.boton_añadir_cliente.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_añadir_cliente.setGeometry(QRect(40, 320, 120, 30))
        self.boton_añadir_cliente.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_añadir_cliente.setIcon(icon27)
        self.boton_añadir_cliente.setIconSize(QSize(18, 18))

        self.tabla_agregar_cliente = QTableWidget(self.pagina_agregar_cliente)
        if (self.tabla_agregar_cliente.columnCount() < 7):
            self.tabla_agregar_cliente.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO CLIENTE")
        self.tabla_agregar_cliente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_agregar_cliente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_agregar_cliente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_agregar_cliente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_agregar_cliente.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_agregar_cliente.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_agregar_cliente.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_agregar_cliente.setColumnWidth(0,100)
        self.tabla_agregar_cliente.setColumnWidth(1,250)
        self.tabla_agregar_cliente.setColumnWidth(2,100)
        self.tabla_agregar_cliente.setColumnWidth(3,100)
        self.tabla_agregar_cliente.setColumnWidth(4,250)
        self.tabla_agregar_cliente.setColumnWidth(5,150)
        self.tabla_agregar_cliente.setColumnWidth(6,548)

        self.tabla_agregar_cliente.setGeometry(QRect(40, 410, 1500, 200))
        self.tabla_agregar_cliente.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")
###### MODIFICAR CLIENTE ########
        self.pagina_modificar_cliente = QWidget()
        self.stackedWidget.addWidget(self.pagina_modificar_cliente)

        self.label_codigo_modificar_cliente = QLabel("Codigo de cliente a cambiar:",self.pagina_modificar_cliente)
        self.label_codigo_modificar_cliente.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_cliente.setGeometry(QRect(40, 330, 325, 30))
        self.label_codigo_modificar_cliente.setFont(font)

        self.label_codigo_modificar_cliente_datos = QLineEdit(self.pagina_modificar_cliente)
        self.label_codigo_modificar_cliente_datos.setPlaceholderText("1")
        self.label_codigo_modificar_cliente_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_cliente_datos.setGeometry(QRect(370, 330, 350, 30))
        self.label_codigo_modificar_cliente_datos.setFont(font)

        self.label_codigo_modificar_cliente_informacion = QLabel(self.pagina_modificar_cliente)
        self.label_codigo_modificar_cliente_informacion.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_cliente_informacion.setGeometry(QRect(725, 330, 700, 30))
        self.label_codigo_modificar_cliente_informacion.setFont(font)

        self.label_modificar_cliente = QLabel("Campo de cliente a cambiar:",self.pagina_modificar_cliente)
        self.label_modificar_cliente.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_modificar_cliente.setGeometry(QRect(40, 370, 325, 30))
        self.label_modificar_cliente.setFont(font)

        self.modificar_cliente_datos = QLineEdit(self.pagina_modificar_cliente)
        self.modificar_cliente_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.modificar_cliente_datos.setGeometry(QRect(370, 370, 350, 30))
        self.modificar_cliente_datos.setFont(font)

        self.comboBox_label_modificar_cliente = QComboBox(self.pagina_modificar_cliente)
        self.comboBox_label_modificar_cliente.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.comboBox_label_modificar_cliente.addItem("RFC")
        self.comboBox_label_modificar_cliente.addItem("Nombre")
        self.comboBox_label_modificar_cliente.addItem("Email")
        self.comboBox_label_modificar_cliente.addItem("Telefono")
        self.comboBox_label_modificar_cliente.addItem("Direccion")
        self.comboBox_label_modificar_cliente.setGeometry(QRect(730, 370, 150, 30))
        self.comboBox_label_modificar_cliente.setFont(font)

        self.boton_modificar_cliente = QPushButton("Modificar Cliente", self.pagina_modificar_cliente)
        self.boton_modificar_cliente.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_modificar_cliente.setGeometry(QRect(885, 370, 160, 30))
        self.boton_modificar_cliente.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_modificar_cliente.setIcon(icon27)
        self.boton_modificar_cliente.setIconSize(QSize(18, 18))

        self.tabla_modificar_cliente = QTableWidget(self.pagina_modificar_cliente)
        if (self.tabla_modificar_cliente.columnCount() < 7):
            self.tabla_modificar_cliente.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO CLIENTE")
        self.tabla_modificar_cliente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_modificar_cliente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_modificar_cliente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_modificar_cliente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_modificar_cliente.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_modificar_cliente.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_modificar_cliente.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_modificar_cliente.setColumnWidth(0,100)
        self.tabla_modificar_cliente.setColumnWidth(1,250)
        self.tabla_modificar_cliente.setColumnWidth(2,100)
        self.tabla_modificar_cliente.setColumnWidth(3,100)
        self.tabla_modificar_cliente.setColumnWidth(4,250)
        self.tabla_modificar_cliente.setColumnWidth(5,150)
        self.tabla_modificar_cliente.setColumnWidth(6,548)

        self.tabla_modificar_cliente.setGeometry(QRect(40, 410, 1500, 200))
        self.tabla_modificar_cliente.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

####BUSCAR CLIENTE##################
        self.pagina_buscar_cliente = QWidget()
        self.stackedWidget.addWidget(self.pagina_buscar_cliente)
        self.label_buscar_cliente = QLabel("Codigo de cliente a buscar:",self.pagina_buscar_cliente)
        self.label_buscar_cliente.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_buscar_cliente.setGeometry(QRect(40, 370, 325, 30))
        self.label_buscar_cliente.setFont(font)

        self.buscar_cliente_datos = QLineEdit(self.pagina_buscar_cliente)
        self.buscar_cliente_datos.setPlaceholderText("1")
        self.buscar_cliente_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.buscar_cliente_datos.setGeometry(QRect(370, 370, 350, 30))
        self.buscar_cliente_datos.setFont(font)

        self.boton_buscar_cliente = QPushButton("Buscar Cliente", self.pagina_buscar_cliente)
        self.boton_buscar_cliente.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_buscar_cliente.setGeometry(QRect(725, 370, 160, 30))
        self.boton_buscar_cliente.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_buscar_cliente.setIcon(icon27)
        self.boton_buscar_cliente.setIconSize(QSize(18, 18))

        self.tabla_buscar_cliente = QTableWidget(self.pagina_buscar_cliente)
        if (self.tabla_buscar_cliente.columnCount() < 7):
            self.tabla_buscar_cliente.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO CLIENTE")
        self.tabla_buscar_cliente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_buscar_cliente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_buscar_cliente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_buscar_cliente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_buscar_cliente.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_buscar_cliente.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_buscar_cliente.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_buscar_cliente.setColumnWidth(0,100)
        self.tabla_buscar_cliente.setColumnWidth(1,250)
        self.tabla_buscar_cliente.setColumnWidth(2,100)
        self.tabla_buscar_cliente.setColumnWidth(3,100)
        self.tabla_buscar_cliente.setColumnWidth(4,250)
        self.tabla_buscar_cliente.setColumnWidth(5,150)
        self.tabla_buscar_cliente.setColumnWidth(6,548)

        self.tabla_buscar_cliente.setGeometry(QRect(40, 410, 1500, 400))
        self.tabla_buscar_cliente.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")
        
#############MOSTRAR CLIENTES################
        self.pagina_mostrar_cliente = QWidget()
        self.stackedWidget.addWidget(self.pagina_mostrar_cliente)

        self.tabla_mostrar_cliente = QTableWidget(self.pagina_mostrar_cliente)
        if (self.tabla_mostrar_cliente.columnCount() < 7):
            self.tabla_mostrar_cliente.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO CLIENTE")
        self.tabla_mostrar_cliente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_mostrar_cliente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_mostrar_cliente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_mostrar_cliente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_mostrar_cliente.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_mostrar_cliente.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_mostrar_cliente.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_mostrar_cliente.setColumnWidth(0,100)
        self.tabla_mostrar_cliente.setColumnWidth(1,250)
        self.tabla_mostrar_cliente.setColumnWidth(2,100)
        self.tabla_mostrar_cliente.setColumnWidth(3,100)
        self.tabla_mostrar_cliente.setColumnWidth(4,250)
        self.tabla_mostrar_cliente.setColumnWidth(5,150)
        self.tabla_mostrar_cliente.setColumnWidth(6,548)

        self.tabla_mostrar_cliente.setGeometry(QRect(40, 110, 1500, 700))
        self.tabla_mostrar_cliente.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")
############################# PROVEEDOR ###############################################################################
###### AGREGAR PROVEEDOR ###################
        self.pagina_agregar_proveedor = QWidget()
        self.fecha = QLabel("Fecha:",self.pagina_agregar_proveedor)
        self.fecha.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha.setGeometry(QRect(1340, 40, 70, 30))
        self.stackedWidget.addWidget(self.pagina_agregar_proveedor)
        self.fecha.setFont(font)

        self.ahora = datetime.now()
        self.fecha_resul = self.ahora.strftime(("%d/%m/%Y"))

        self.fecha_datos = QLabel(self.pagina_agregar_proveedor)
        self.fecha_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_datos.setGeometry(QRect(1420, 40, 114, 30))
        self.fecha_datos.setFont(font)
        self.fecha_datos.setText(self.fecha_resul)

        self.codigo_proveedor = QLabel("Codigo de Proveedor:",self.pagina_agregar_proveedor)
        self.codigo_proveedor.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_proveedor.setGeometry(QRect(40, 80, 230, 30))
        self.codigo_proveedor.setFont(font)

        self.codigo_proveedor_datos = QLabel(self.pagina_agregar_proveedor)
        self.codigo_proveedor_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_proveedor_datos.setGeometry(QRect(275, 80, 100, 30))
        self.codigo_proveedor_datos.setFont(font)
        self.codigo_proveedor_datos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.nombre_proveedor = QLabel("Nombre de Proveedor:",self.pagina_agregar_proveedor)
        self.nombre_proveedor.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.nombre_proveedor.setGeometry(QRect(40, 120, 240, 30))
        self.nombre_proveedor.setFont(font)

        self.nombre_proveedor_datos = QLineEdit(self.pagina_agregar_proveedor)
        self.nombre_proveedor_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.nombre_proveedor_datos.setGeometry(QRect(285, 120, 500, 30))
        self.nombre_proveedor_datos.setFont(font)

        self.rfc_proveedor = QLabel("RFC:",self.pagina_agregar_proveedor)
        self.rfc_proveedor.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.rfc_proveedor.setGeometry(QRect(40, 160, 60, 30))
        self.rfc_proveedor.setFont(font)

        self.rfc_proveedor_datos = QLineEdit(self.pagina_agregar_proveedor)
        self.rfc_proveedor_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.rfc_proveedor_datos.setGeometry(QRect(105, 160, 180, 30))
        self.rfc_proveedor_datos.setFont(font)

        self.email_proveedor = QLabel("Email:",self.pagina_agregar_proveedor)
        self.email_proveedor.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.email_proveedor.setGeometry(QRect(40, 200, 70, 30))
        self.email_proveedor.setFont(font)

        self.email_proveedor_datos = QLineEdit(self.pagina_agregar_proveedor)
        self.email_proveedor_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.email_proveedor_datos.setGeometry(QRect(115, 200, 400, 30))
        self.email_proveedor_datos.setFont(font)

        self.telefono_proveedor = QLabel("Telefono:",self.pagina_agregar_proveedor)
        self.telefono_proveedor.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.telefono_proveedor.setGeometry(QRect(40, 240, 100, 30))
        self.telefono_proveedor.setFont(font)

        self.telefono_proveedor_datos = QLineEdit(self.pagina_agregar_proveedor)
        self.telefono_proveedor_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.telefono_proveedor_datos.setGeometry(QRect(145, 240, 200, 30))
        self.telefono_proveedor_datos.setFont(font)

        self.direccion_proveedor = QLabel("Direccion:",self.pagina_agregar_proveedor)
        self.direccion_proveedor.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.direccion_proveedor.setGeometry(QRect(40, 280, 110, 30))
        self.direccion_proveedor.setFont(font)

        self.direccion_proveedor_datos = QLineEdit(self.pagina_agregar_proveedor)
        self.direccion_proveedor_datos.setPlaceholderText("Calle, Colonia, Ciudad Estado")
        self.direccion_proveedor_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.direccion_proveedor_datos.setGeometry(QRect(155, 280, 750, 30))
        self.direccion_proveedor_datos.setFont(font)

        self.boton_añadir_proveedor = QPushButton("Añadir Proveedor", self.pagina_agregar_proveedor)
        self.boton_añadir_proveedor.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_añadir_proveedor.setGeometry(QRect(40, 320, 140, 30))
        self.boton_añadir_proveedor.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_añadir_proveedor.setIcon(icon27)
        self.boton_añadir_proveedor.setIconSize(QSize(18, 18))

        self.tabla_agregar_proveedor = QTableWidget(self.pagina_agregar_proveedor)
        if (self.tabla_agregar_proveedor.columnCount() < 7):
            self.tabla_agregar_proveedor.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO PROVEEDOR")
        self.tabla_agregar_proveedor.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_agregar_proveedor.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_agregar_proveedor.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_agregar_proveedor.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_agregar_proveedor.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_agregar_proveedor.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_agregar_proveedor.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_agregar_proveedor.setColumnWidth(0,140)
        self.tabla_agregar_proveedor.setColumnWidth(1,250)
        self.tabla_agregar_proveedor.setColumnWidth(2,100)
        self.tabla_agregar_proveedor.setColumnWidth(3,100)
        self.tabla_agregar_proveedor.setColumnWidth(4,250)
        self.tabla_agregar_proveedor.setColumnWidth(5,150)
        self.tabla_agregar_proveedor.setColumnWidth(6,508)

        self.tabla_agregar_proveedor.setGeometry(QRect(40, 410, 1500, 200))
        self.tabla_agregar_proveedor.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

###### MODIFICAR PROVEEDOR ########
        self.pagina_modificar_proveedor = QWidget()
        self.stackedWidget.addWidget(self.pagina_modificar_proveedor)

        self.label_codigo_modificar_proveedor = QLabel("Codigo de proveedor a cambiar:",self.pagina_modificar_proveedor)
        self.label_codigo_modificar_proveedor.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_proveedor.setGeometry(QRect(40, 330, 335, 30))
        self.label_codigo_modificar_proveedor.setFont(font)

        self.label_codigo_modificar_proveedor_datos = QLineEdit(self.pagina_modificar_proveedor)
        self.label_codigo_modificar_proveedor_datos.setPlaceholderText("1")
        self.label_codigo_modificar_proveedor_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_proveedor_datos.setGeometry(QRect(375, 330, 350, 30))
        self.label_codigo_modificar_proveedor_datos.setFont(font)

        self.label_codigo_modificar_proveedor_informacion = QLabel(self.pagina_modificar_proveedor)
        self.label_codigo_modificar_proveedor_informacion.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_proveedor_informacion.setGeometry(QRect(730, 330, 700, 30))
        self.label_codigo_modificar_proveedor_informacion.setFont(font)

        self.label_modificar_proveedor = QLabel("Campo de proveedor a cambiar:",self.pagina_modificar_proveedor)
        self.label_modificar_proveedor.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_modificar_proveedor.setGeometry(QRect(40, 370, 335, 30))
        self.label_modificar_proveedor.setFont(font)

        self.modificar_proveedor_datos = QLineEdit(self.pagina_modificar_proveedor)
        self.modificar_proveedor_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.modificar_proveedor_datos.setGeometry(QRect(380, 370, 350, 30))
        self.modificar_proveedor_datos.setFont(font)

        self.comboBox_label_modificar_proveedor = QComboBox(self.pagina_modificar_proveedor)
        self.comboBox_label_modificar_proveedor.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.comboBox_label_modificar_proveedor.addItem("RFC")
        self.comboBox_label_modificar_proveedor.addItem("Nombre")
        self.comboBox_label_modificar_proveedor.addItem("Email")
        self.comboBox_label_modificar_proveedor.addItem("Telefono")
        self.comboBox_label_modificar_proveedor.addItem("Direccion")
        self.comboBox_label_modificar_proveedor.setGeometry(QRect(730, 370, 150, 30))
        self.comboBox_label_modificar_proveedor.setFont(font)

        self.boton_modificar_proveedor = QPushButton("Modificar Proveedor", self.pagina_modificar_proveedor)
        self.boton_modificar_proveedor.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_modificar_proveedor.setGeometry(QRect(885, 370, 180, 30))
        self.boton_modificar_proveedor.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_modificar_proveedor.setIcon(icon27)
        self.boton_modificar_proveedor.setIconSize(QSize(18, 18))

        self.tabla_modificar_proveedor = QTableWidget(self.pagina_modificar_proveedor)
        if (self.tabla_modificar_proveedor.columnCount() < 7):
            self.tabla_modificar_proveedor.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO PROVEEDOR")
        self.tabla_modificar_proveedor.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_modificar_proveedor.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_modificar_proveedor.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_modificar_proveedor.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_modificar_proveedor.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_modificar_proveedor.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_modificar_proveedor.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_modificar_proveedor.setColumnWidth(0,100)
        self.tabla_modificar_proveedor.setColumnWidth(1,250)
        self.tabla_modificar_proveedor.setColumnWidth(2,100)
        self.tabla_modificar_proveedor.setColumnWidth(3,100)
        self.tabla_modificar_proveedor.setColumnWidth(4,250)
        self.tabla_modificar_proveedor.setColumnWidth(5,150)
        self.tabla_modificar_proveedor.setColumnWidth(6,548)

        self.tabla_modificar_proveedor.setGeometry(QRect(40, 410, 1500, 200))
        self.tabla_modificar_proveedor.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

####BUSCAR PROVEEDOR##################
        self.pagina_buscar_proveedor = QWidget()
        self.stackedWidget.addWidget(self.pagina_buscar_proveedor)
        self.label_buscar_proveedor = QLabel("Codigo de proveedor a buscar:",self.pagina_buscar_proveedor)
        self.label_buscar_proveedor.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_buscar_proveedor.setGeometry(QRect(40, 370, 325, 30))
        self.label_buscar_proveedor.setFont(font)

        self.buscar_proveedor_datos = QLineEdit(self.pagina_buscar_proveedor)
        self.buscar_proveedor_datos.setPlaceholderText("1")
        self.buscar_proveedor_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.buscar_proveedor_datos.setGeometry(QRect(370, 370, 350, 30))
        self.buscar_proveedor_datos.setFont(font)

        self.boton_buscar_proveedor = QPushButton("Buscar Proveedor", self.pagina_buscar_proveedor)
        self.boton_buscar_proveedor.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_buscar_proveedor.setGeometry(QRect(725, 370, 160, 30))
        self.boton_buscar_proveedor.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_buscar_proveedor.setIcon(icon27)
        self.boton_buscar_proveedor.setIconSize(QSize(18, 18))

        self.tabla_buscar_proveedor = QTableWidget(self.pagina_buscar_proveedor)
        if (self.tabla_buscar_proveedor.columnCount() < 7):
            self.tabla_buscar_proveedor.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO PROVEEDOR")
        self.tabla_buscar_proveedor.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_buscar_proveedor.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_buscar_proveedor.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_buscar_proveedor.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_buscar_proveedor.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_buscar_proveedor.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_buscar_proveedor.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_buscar_proveedor.setColumnWidth(0,100)
        self.tabla_buscar_proveedor.setColumnWidth(1,250)
        self.tabla_buscar_proveedor.setColumnWidth(2,100)
        self.tabla_buscar_proveedor.setColumnWidth(3,100)
        self.tabla_buscar_proveedor.setColumnWidth(4,250)
        self.tabla_buscar_proveedor.setColumnWidth(5,150)
        self.tabla_buscar_proveedor.setColumnWidth(6,548)

        self.tabla_buscar_proveedor.setGeometry(QRect(40, 410, 1500, 400))
        self.tabla_buscar_proveedor.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")
        
#############MOSTRAR PROVEEDOR################
        self.pagina_mostrar_proveedor = QWidget()
        self.stackedWidget.addWidget(self.pagina_mostrar_proveedor)

        self.tabla_mostrar_proveedor = QTableWidget(self.pagina_mostrar_proveedor)
        if (self.tabla_mostrar_proveedor.columnCount() < 7):
            self.tabla_mostrar_proveedor.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO PROVEEDOR")
        self.tabla_mostrar_proveedor.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_mostrar_proveedor.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_mostrar_proveedor.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_mostrar_proveedor.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_mostrar_proveedor.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_mostrar_proveedor.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_mostrar_proveedor.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_mostrar_proveedor.setColumnWidth(0,100)
        self.tabla_mostrar_proveedor.setColumnWidth(1,250)
        self.tabla_mostrar_proveedor.setColumnWidth(2,100)
        self.tabla_mostrar_proveedor.setColumnWidth(3,100)
        self.tabla_mostrar_proveedor.setColumnWidth(4,250)
        self.tabla_mostrar_proveedor.setColumnWidth(5,150)
        self.tabla_mostrar_proveedor.setColumnWidth(6,548)

        self.tabla_mostrar_proveedor.setGeometry(QRect(40, 110, 1500, 700))
        self.tabla_mostrar_proveedor.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")
############################# TRABAJADOR ###############################################################################
###### AGREGAR TRABAJADOR ###################
        self.pagina_agregar_trabajador = QWidget()
        self.stackedWidget.addWidget(self.pagina_agregar_trabajador)

        self.fecha_arribaiz = QLabel("Fecha:",self.pagina_agregar_trabajador)
        self.fecha_arribaiz.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha_arribaiz.setGeometry(QRect(1340, 40, 70, 30))
        self.fecha_arribaiz.setFont(font)

        self.ahora = datetime.now()
        self.fecha_arribaiz = self.ahora.strftime(("%d/%m/%Y"))

        self.fecha_arribaiz_datos = QLabel(self.pagina_agregar_trabajador)
        self.fecha_arribaiz_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_arribaiz_datos.setGeometry(QRect(1420, 40, 114, 30))
        self.fecha_arribaiz_datos.setFont(font)
        self.fecha_arribaiz_datos.setText(self.fecha_resul)     

        self.fecha_datos = QLabel(self.pagina_agregar_trabajador)
        self.fecha_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_datos.setGeometry(QRect(235, 120, 125, 30))
        self.fecha_datos.setFont(font)
        self.fecha_datos.setText(self.fecha_resul)     
        

        self.fecha = QLabel("Fecha de Ingreso:",self.pagina_agregar_trabajador)
        self.fecha.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha.setGeometry(QRect(40, 120, 190, 30))

        self.fecha.setFont(font)

        self.codigo_trabajador = QLabel("Codigo de Trabajador:",self.pagina_agregar_trabajador)
        self.codigo_trabajador.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_trabajador.setGeometry(QRect(40, 80, 230, 30))
        self.codigo_trabajador.setFont(font)

        self.codigo_trabajador_datos = QLabel(self.pagina_agregar_trabajador)
        self.codigo_trabajador_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_trabajador_datos.setGeometry(QRect(275, 80, 100, 30))
        self.codigo_trabajador_datos.setFont(font)
        self.codigo_trabajador_datos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.nombre_trabajador = QLabel("Nombre del Trabajador:",self.pagina_agregar_trabajador)
        self.nombre_trabajador.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.nombre_trabajador.setGeometry(QRect(40, 160, 250, 30))
        self.nombre_trabajador.setFont(font)

        self.nombre_trabajador_datos = QLineEdit(self.pagina_agregar_trabajador)
        self.nombre_trabajador_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.nombre_trabajador_datos.setGeometry(QRect(295, 160, 500, 30))
        self.nombre_trabajador_datos.setFont(font)

        self.rfc_trabajador = QLabel("RFC:",self.pagina_agregar_trabajador)
        self.rfc_trabajador.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.rfc_trabajador.setGeometry(QRect(40, 200, 60, 30))
        self.rfc_trabajador.setFont(font)

        self.rfc_trabajador_datos = QLineEdit(self.pagina_agregar_trabajador)
        self.rfc_trabajador_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.rfc_trabajador_datos.setGeometry(QRect(105, 200, 180, 30))
        self.rfc_trabajador_datos.setFont(font)

        self.email_trabajador = QLabel("Email:",self.pagina_agregar_trabajador)
        self.email_trabajador.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.email_trabajador.setGeometry(QRect(40, 240, 70, 30))
        self.email_trabajador.setFont(font)

        self.email_trabajador_datos = QLineEdit(self.pagina_agregar_trabajador)
        self.email_trabajador_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.email_trabajador_datos.setGeometry(QRect(115, 240, 400, 30))
        self.email_trabajador_datos.setFont(font)

        self.telefono_trabajador = QLabel("Telefono:",self.pagina_agregar_trabajador)
        self.telefono_trabajador.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.telefono_trabajador.setGeometry(QRect(40, 280, 100, 30))
        self.telefono_trabajador.setFont(font)

        self.telefono_trabajador_datos = QLineEdit(self.pagina_agregar_trabajador)
        self.telefono_trabajador_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.telefono_trabajador_datos.setGeometry(QRect(145, 280, 200, 30))
        self.telefono_trabajador_datos.setFont(font)

        self.direccion_trabajador = QLabel("Direccion:",self.pagina_agregar_trabajador)
        self.direccion_trabajador.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.direccion_trabajador.setGeometry(QRect(40, 320, 110, 30))
        self.direccion_trabajador.setFont(font)

        self.direccion_trabajador_datos = QLineEdit(self.pagina_agregar_trabajador)
        self.direccion_trabajador_datos.setPlaceholderText("Calle, Colonia, Ciudad Estado")
        self.direccion_trabajador_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.direccion_trabajador_datos.setGeometry(QRect(155, 320, 750, 30))
        self.direccion_trabajador_datos.setFont(font)

        self.departamento_trabajador = QLabel("Departamento:",self.pagina_agregar_trabajador)
        self.departamento_trabajador.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.departamento_trabajador.setGeometry(QRect(40, 360, 160, 30))
        self.departamento_trabajador.setFont(font)

        self.comboBox_departamento_trabajador_datos = QComboBox(self.pagina_agregar_trabajador)
        self.comboBox_departamento_trabajador_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.comboBox_departamento_trabajador_datos.addItem("Computo")
        self.comboBox_departamento_trabajador_datos.addItem("Construccion")
        self.comboBox_departamento_trabajador_datos.addItem("Servicio al cliente")
        self.comboBox_departamento_trabajador_datos.addItem("Administracion")
        self.comboBox_departamento_trabajador_datos.setGeometry(QRect(205, 360, 300, 30))
        self.comboBox_departamento_trabajador_datos.setFont(font)      

        self.boton_añadir_trabajador = QPushButton("Añadir Trabajador", self.pagina_agregar_trabajador)
        self.boton_añadir_trabajador.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_añadir_trabajador.setGeometry(QRect(40, 400, 140, 30))
        self.boton_añadir_trabajador.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_añadir_trabajador.setIcon(icon27)
        self.boton_añadir_trabajador.setIconSize(QSize(18, 18))

        self.tabla_agregar_trabajador = QTableWidget(self.pagina_agregar_trabajador)
        if (self.tabla_agregar_trabajador.columnCount() < 8):
            self.tabla_agregar_trabajador.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem("CODIGO TRABAJADOR")
        self.tabla_agregar_trabajador.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_agregar_trabajador.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_agregar_trabajador.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA INGRESO")
        self.tabla_agregar_trabajador.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_agregar_trabajador.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_agregar_trabajador.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_agregar_trabajador.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem6 = QTableWidgetItem("DEPARTAMENTO")
        self.tabla_agregar_trabajador.setHorizontalHeaderItem(7, __qtablewidgetitem6)
        self.tabla_agregar_trabajador.setColumnWidth(0,140)
        self.tabla_agregar_trabajador.setColumnWidth(1,250)
        self.tabla_agregar_trabajador.setColumnWidth(2,100)
        self.tabla_agregar_trabajador.setColumnWidth(3,100)
        self.tabla_agregar_trabajador.setColumnWidth(4,250)
        self.tabla_agregar_trabajador.setColumnWidth(5,150)
        self.tabla_agregar_trabajador.setColumnWidth(7,150)
        self.tabla_agregar_trabajador.setColumnWidth(6,358)

        self.tabla_agregar_trabajador.setGeometry(QRect(40, 450, 1500, 200))
        self.tabla_agregar_trabajador.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

###### MODIFICAR TRABAJADOR ################################
        self.pagina_modificar_trabajador = QWidget()
        self.stackedWidget.addWidget(self.pagina_modificar_trabajador)

        self.label_codigo_modificar_trabajador = QLabel("Codigo de trabajador a cambiar:",self.pagina_modificar_trabajador)
        self.label_codigo_modificar_trabajador.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_trabajador.setGeometry(QRect(40, 330, 335, 30))
        self.label_codigo_modificar_trabajador.setFont(font)

        self.label_codigo_modificar_trabajador_datos = QLineEdit(self.pagina_modificar_trabajador)
        self.label_codigo_modificar_trabajador_datos.setPlaceholderText("1")
        self.label_codigo_modificar_trabajador_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_trabajador_datos.setGeometry(QRect(375, 330, 350, 30))
        self.label_codigo_modificar_trabajador_datos.setFont(font)

        self.label_codigo_modificar_trabajador_informacion = QLabel(self.pagina_modificar_trabajador)
        self.label_codigo_modificar_trabajador_informacion.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_trabajador_informacion.setGeometry(QRect(730, 330, 700, 30))
        self.label_codigo_modificar_trabajador_informacion.setFont(font)

        self.label_modificar_trabajador = QLabel("Campo de trabajador a cambiar:",self.pagina_modificar_trabajador)
        self.label_modificar_trabajador.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_modificar_trabajador.setGeometry(QRect(40, 370, 335, 30))
        self.label_modificar_trabajador.setFont(font)

        self.modificar_trabajador_datos = QLineEdit(self.pagina_modificar_trabajador)
        self.modificar_trabajador_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.modificar_trabajador_datos.setGeometry(QRect(380, 370, 350, 30))
        self.modificar_trabajador_datos.setFont(font)

        self.comboBox_label_modificar_trabajador = QComboBox(self.pagina_modificar_trabajador)
        self.comboBox_label_modificar_trabajador.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.comboBox_label_modificar_trabajador.addItem("RFC")
        self.comboBox_label_modificar_trabajador.addItem("Nombre")
        self.comboBox_label_modificar_trabajador.addItem("Email")
        self.comboBox_label_modificar_trabajador.addItem("Telefono")
        self.comboBox_label_modificar_trabajador.addItem("Direccion")
        self.comboBox_label_modificar_trabajador.addItem("Departamento")
        self.comboBox_label_modificar_trabajador.setGeometry(QRect(730, 370, 180, 30))
        self.comboBox_label_modificar_trabajador.setFont(font)

        self.boton_modificar_trabajador = QPushButton("Modificar Trabajador", self.pagina_modificar_trabajador)
        self.boton_modificar_trabajador.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_modificar_trabajador.setGeometry(QRect(915, 370, 180, 30))
        self.boton_modificar_trabajador.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_modificar_trabajador.setIcon(icon27)
        self.boton_modificar_trabajador.setIconSize(QSize(18, 18))

        self.tabla_modificar_trabajador = QTableWidget(self.pagina_modificar_trabajador)
        if (self.tabla_modificar_trabajador.columnCount() < 8):
            self.tabla_modificar_trabajador.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem("CODIGO TRABAJADOR")
        self.tabla_modificar_trabajador.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_modificar_trabajador.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_modificar_trabajador.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_modificar_trabajador.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_modificar_trabajador.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_modificar_trabajador.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_modificar_trabajador.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem6 = QTableWidgetItem("DEPARTAMENTO")
        self.tabla_modificar_trabajador.setHorizontalHeaderItem(7, __qtablewidgetitem6)
        self.tabla_modificar_trabajador.setColumnWidth(0,140)
        self.tabla_modificar_trabajador.setColumnWidth(1,250)
        self.tabla_modificar_trabajador.setColumnWidth(2,100)
        self.tabla_modificar_trabajador.setColumnWidth(3,100)
        self.tabla_modificar_trabajador.setColumnWidth(4,250)
        self.tabla_modificar_trabajador.setColumnWidth(5,150)
        self.tabla_modificar_trabajador.setColumnWidth(7,150)
        self.tabla_modificar_trabajador.setColumnWidth(6,358)

        self.tabla_modificar_trabajador.setGeometry(QRect(40, 410, 1500, 200))
        self.tabla_modificar_trabajador.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

####BUSCAR TRABAJADOR##################
        self.pagina_buscar_trabajador = QWidget()
        self.stackedWidget.addWidget(self.pagina_buscar_trabajador)
        self.label_buscar_trabajador = QLabel("Codigo de trabajador a buscar:",self.pagina_buscar_trabajador)
        self.label_buscar_trabajador.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_buscar_trabajador.setGeometry(QRect(40, 370, 325, 30))
        self.label_buscar_trabajador.setFont(font)

        self.buscar_trabajador_datos = QLineEdit(self.pagina_buscar_trabajador)
        self.buscar_trabajador_datos.setPlaceholderText("1")
        self.buscar_trabajador_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.buscar_trabajador_datos.setGeometry(QRect(370, 370, 350, 30))
        self.buscar_trabajador_datos.setFont(font)

        self.boton_buscar_trabajador = QPushButton("Buscar Trabajador", self.pagina_buscar_trabajador)
        self.boton_buscar_trabajador.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_buscar_trabajador.setGeometry(QRect(725, 370, 160, 30))
        self.boton_buscar_trabajador.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_buscar_trabajador.setIcon(icon27)
        self.boton_buscar_trabajador.setIconSize(QSize(18, 18))

        self.tabla_buscar_trabajador = QTableWidget(self.pagina_buscar_trabajador)
        if (self.tabla_buscar_trabajador.columnCount() < 8):
            self.tabla_buscar_trabajador.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem("CODIGO TRABAJADOR")
        self.tabla_buscar_trabajador.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_buscar_trabajador.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_buscar_trabajador.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_buscar_trabajador.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_buscar_trabajador.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_buscar_trabajador.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_buscar_trabajador.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem6 = QTableWidgetItem("DEPARTAMENTO")
        self.tabla_buscar_trabajador.setHorizontalHeaderItem(7, __qtablewidgetitem6)
        self.tabla_buscar_trabajador.setColumnWidth(0,140)
        self.tabla_buscar_trabajador.setColumnWidth(1,250)
        self.tabla_buscar_trabajador.setColumnWidth(2,100)
        self.tabla_buscar_trabajador.setColumnWidth(3,100)
        self.tabla_buscar_trabajador.setColumnWidth(4,250)
        self.tabla_buscar_trabajador.setColumnWidth(5,150)
        self.tabla_buscar_trabajador.setColumnWidth(7,150)
        self.tabla_buscar_trabajador.setColumnWidth(6,358)

        self.tabla_buscar_trabajador.setGeometry(QRect(40, 410, 1500, 400))
        self.tabla_buscar_trabajador.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")
        
#############MOSTRAR TRABAJADOR################
        self.pagina_mostrar_trabajador = QWidget()
        self.stackedWidget.addWidget(self.pagina_mostrar_trabajador)

        self.tabla_mostrar_trabajador = QTableWidget(self.pagina_mostrar_trabajador)
        if (self.tabla_mostrar_trabajador.columnCount() < 8):
            self.tabla_mostrar_trabajador.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem("CODIGO TRABAJADOR")
        self.tabla_mostrar_trabajador.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_mostrar_trabajador.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("RFC")
        self.tabla_mostrar_trabajador.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA REGISTRO")
        self.tabla_mostrar_trabajador.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("EMAIL")
        self.tabla_mostrar_trabajador.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TELEFONO")
        self.tabla_mostrar_trabajador.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_mostrar_trabajador.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem6 = QTableWidgetItem("DEPARTAMENTO")
        self.tabla_mostrar_trabajador.setHorizontalHeaderItem(7, __qtablewidgetitem6)
        self.tabla_mostrar_trabajador.setColumnWidth(0,140)
        self.tabla_mostrar_trabajador.setColumnWidth(1,250)
        self.tabla_mostrar_trabajador.setColumnWidth(2,100)
        self.tabla_mostrar_trabajador.setColumnWidth(3,100)
        self.tabla_mostrar_trabajador.setColumnWidth(4,250)
        self.tabla_mostrar_trabajador.setColumnWidth(5,150)
        self.tabla_mostrar_trabajador.setColumnWidth(7,150)
        self.tabla_mostrar_trabajador.setColumnWidth(6,358)

        self.tabla_mostrar_trabajador.setGeometry(QRect(40, 110, 1500, 700))
        self.tabla_mostrar_trabajador.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

###### AGREGAR PROYECTO ###################
        self.pagina_agregar_proyecto = QWidget()
        self.stackedWidget.addWidget(self.pagina_agregar_proyecto)

        self.fecha_arribaiz = QLabel("Fecha:",self.pagina_agregar_proyecto)
        self.fecha_arribaiz.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha_arribaiz.setGeometry(QRect(1340, 40, 70, 30))
        self.fecha_arribaiz.setFont(font)

        self.ahora = datetime.now()
        self.fecha_arribaiz = self.ahora.strftime(("%d/%m/%Y"))

        self.fecha_arribaiz_datos = QLabel(self.pagina_agregar_proyecto)
        self.fecha_arribaiz_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_arribaiz_datos.setGeometry(QRect(1420, 40, 114, 30))
        self.fecha_arribaiz_datos.setFont(font)
        self.fecha_arribaiz_datos.setText(self.fecha_resul)            

        self.codigo_proyecto = QLabel("Codigo de Proyecto:",self.pagina_agregar_proyecto)
        self.codigo_proyecto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_proyecto.setGeometry(QRect(40, 80, 230, 30))
        self.codigo_proyecto.setFont(font)

        self.codigo_proyecto_datos = QLabel(self.pagina_agregar_proyecto)
        self.codigo_proyecto_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_proyecto_datos.setGeometry(QRect(275, 80, 100, 30))
        self.codigo_proyecto_datos.setFont(font)
        self.codigo_proyecto_datos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fecha_inicio_proyecto = QLabel("Fecha Inicio:",self.pagina_agregar_proyecto)
        self.fecha_inicio_proyecto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha_inicio_proyecto.setGeometry(QRect(40, 120, 140, 30))
        self.fecha_inicio_proyecto.setFont(font)

        self.fecha_inicio_proyecto_datos = QLineEdit(self.pagina_agregar_proyecto)
        self.fecha_inicio_proyecto_datos.setPlaceholderText("dd/mm/aaaa")
        self.fecha_inicio_proyecto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha_inicio_proyecto_datos.setGeometry(QRect(185, 120, 130, 30))
        self.fecha_inicio_proyecto_datos.setFont(font)

        self.fecha_termino_proyecto = QLabel("Fecha Termino:",self.pagina_agregar_proyecto)
        self.fecha_termino_proyecto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha_termino_proyecto.setGeometry(QRect(40, 160, 170, 30))
        self.fecha_termino_proyecto.setFont(font)

        self.fecha_termino_proyecto_datos = QLineEdit(self.pagina_agregar_proyecto)
        self.fecha_termino_proyecto_datos.setPlaceholderText("dd/mm/aaaa")
        self.fecha_termino_proyecto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha_termino_proyecto_datos.setGeometry(QRect(215, 160, 130, 30))
        self.fecha_termino_proyecto_datos.setFont(font)

        self.presupuesto_proyecto = QLabel("Presupuesto:",self.pagina_agregar_proyecto)
        self.presupuesto_proyecto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.presupuesto_proyecto.setGeometry(QRect(40, 200, 140, 30))
        self.presupuesto_proyecto.setFont(font)

        self.presupuesto_proyecto_datos = QLineEdit(self.pagina_agregar_proyecto)
        self.presupuesto_proyecto_datos.setPlaceholderText("30000000")
        self.presupuesto_proyecto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.presupuesto_proyecto_datos.setGeometry(QRect(185, 200, 400, 30))
        self.presupuesto_proyecto_datos.setFont(font)

        self.codigo_cliente_proyecto = QLabel("Cliente:",self.pagina_agregar_proyecto)
        self.codigo_cliente_proyecto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_cliente_proyecto.setGeometry(QRect(40, 240, 90, 30))
        self.codigo_cliente_proyecto.setFont(font)

        self.codigo_cliente_proyecto_datos = QLineEdit(self.pagina_agregar_proyecto)
        self.presupuesto_proyecto_datos.setPlaceholderText("1")
        self.codigo_cliente_proyecto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_cliente_proyecto_datos.setGeometry(QRect(135, 240, 200, 30))
        self.codigo_cliente_proyecto_datos.setFont(font)

        self.codigo_cliente_proyecto_informacion = QLabel(self.pagina_agregar_proyecto)
        self.codigo_cliente_proyecto_informacion.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_cliente_proyecto_informacion.setGeometry(QRect(340, 240, 500, 30))
        self.codigo_cliente_proyecto_informacion.setFont(font)

        self.nombre_proyecto = QLabel("Direccion:",self.pagina_agregar_proyecto)
        self.nombre_proyecto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.nombre_proyecto.setGeometry(QRect(40, 280, 110, 30))
        self.nombre_proyecto.setFont(font)

        self.direccion_proyecto_datos = QLineEdit(self.pagina_agregar_proyecto)
        self.direccion_proyecto_datos.setPlaceholderText("Calle, Colonia, Ciudad Estado")
        self.direccion_proyecto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.direccion_proyecto_datos.setGeometry(QRect(155, 280, 750, 30))
        self.direccion_proyecto_datos.setFont(font)

        self.domicilio_proyecto = QLabel("Nombre:",self.pagina_agregar_proyecto)
        self.domicilio_proyecto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.domicilio_proyecto.setGeometry(QRect(40, 320, 90, 30))
        self.domicilio_proyecto.setFont(font)

        self.nombre_proyecto_datos = QLineEdit(self.pagina_agregar_proyecto)
        self.nombre_proyecto_datos.setPlaceholderText("La Gran Plaza")
        self.nombre_proyecto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.nombre_proyecto_datos.setGeometry(QRect(135, 320, 350, 30))
        self.nombre_proyecto_datos.setFont(font)

        self.boton_añadir_proyecto = QPushButton("Añadir Proyecto", self.pagina_agregar_proyecto)
        self.boton_añadir_proyecto.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_añadir_proyecto.setGeometry(QRect(40, 360, 140, 30))
        self.boton_añadir_proyecto.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_añadir_proyecto.setIcon(icon27)
        self.boton_añadir_proyecto.setIconSize(QSize(18, 18))

        self.tabla_agregar_proyecto = QTableWidget(self.pagina_agregar_proyecto)
        if (self.tabla_agregar_proyecto.columnCount() < 7):
            self.tabla_agregar_proyecto.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO PROYECTO")
        self.tabla_agregar_proyecto.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_agregar_proyecto.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("FECHA INICIO")
        self.tabla_agregar_proyecto.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA TERMINO")
        self.tabla_agregar_proyecto.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("PRESUPUESTO")
        self.tabla_agregar_proyecto.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("CLIENTE")
        self.tabla_agregar_proyecto.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_agregar_proyecto.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_agregar_proyecto.setColumnWidth(0,140)
        self.tabla_agregar_proyecto.setColumnWidth(1,150)
        self.tabla_agregar_proyecto.setColumnWidth(2,133)
        self.tabla_agregar_proyecto.setColumnWidth(3,133)
        self.tabla_agregar_proyecto.setColumnWidth(4,134)
        self.tabla_agregar_proyecto.setColumnWidth(5,340)
        self.tabla_agregar_proyecto.setColumnWidth(6,468)

        self.tabla_agregar_proyecto.setGeometry(QRect(40, 450, 1500, 200))
        self.tabla_agregar_proyecto.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

###### MODIFICAR PROYECTO ################################
        self.pagina_modificar_proyecto = QWidget()
        self.stackedWidget.addWidget(self.pagina_modificar_proyecto)

        self.label_codigo_modificar_proyecto = QLabel("Codigo de proyecto a cambiar:",self.pagina_modificar_proyecto)
        self.label_codigo_modificar_proyecto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_proyecto.setGeometry(QRect(40, 330, 335, 30))
        self.label_codigo_modificar_proyecto.setFont(font)

        self.label_codigo_modificar_proyecto_datos = QLineEdit(self.pagina_modificar_proyecto)
        self.label_codigo_modificar_proyecto_datos.setPlaceholderText("1")
        self.label_codigo_modificar_proyecto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_proyecto_datos.setGeometry(QRect(375, 330, 350, 30))
        self.label_codigo_modificar_proyecto_datos.setFont(font)

        self.label_codigo_modificar_proyecto_informacion = QLabel(self.pagina_modificar_proyecto)
        self.label_codigo_modificar_proyecto_informacion.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_codigo_modificar_proyecto_informacion.setGeometry(QRect(730, 330, 700, 30))
        self.label_codigo_modificar_proyecto_informacion.setFont(font)

        self.label_modificar_proyecto = QLabel("Campo de proyecto a cambiar:",self.pagina_modificar_proyecto)
        self.label_modificar_proyecto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_modificar_proyecto.setGeometry(QRect(40, 370, 335, 30))
        self.label_modificar_proyecto.setFont(font)

        self.modificar_proyecto_datos = QLineEdit(self.pagina_modificar_proyecto)
        self.modificar_proyecto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.modificar_proyecto_datos.setGeometry(QRect(380, 370, 350, 30))
        self.modificar_proyecto_datos.setFont(font)

        self.comboBox_label_modificar_proyecto = QComboBox(self.pagina_modificar_proyecto)
        self.comboBox_label_modificar_proyecto.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.comboBox_label_modificar_proyecto.addItem("Fecha Inicio")
        self.comboBox_label_modificar_proyecto.addItem("Fecha Termino")
        self.comboBox_label_modificar_proyecto.addItem("Presupuesto")
        self.comboBox_label_modificar_proyecto.addItem("Codigo Cliente")
        self.comboBox_label_modificar_proyecto.addItem("Nombre")
        self.comboBox_label_modificar_proyecto.addItem("Domicilio")
        self.comboBox_label_modificar_proyecto.setGeometry(QRect(730, 370, 180, 30))
        self.comboBox_label_modificar_proyecto.setFont(font)

        self.boton_modificar_proyecto = QPushButton("Modificar Proyecto", self.pagina_modificar_proyecto)
        self.boton_modificar_proyecto.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_modificar_proyecto.setGeometry(QRect(915, 370, 180, 30))
        self.boton_modificar_proyecto.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_modificar_proyecto.setIcon(icon27)
        self.boton_modificar_proyecto.setIconSize(QSize(18, 18))

        self.tabla_modificar_proyecto = QTableWidget(self.pagina_modificar_proyecto)
        if (self.tabla_modificar_proyecto.columnCount() < 7):
            self.tabla_modificar_proyecto.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO PROYECTO")
        self.tabla_modificar_proyecto.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_modificar_proyecto.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("FECHA INICIO")
        self.tabla_modificar_proyecto.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA TERMINO")
        self.tabla_modificar_proyecto.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("PRESUPUESTO")
        self.tabla_modificar_proyecto.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("CLIENTE")
        self.tabla_modificar_proyecto.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_modificar_proyecto.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_modificar_proyecto.setColumnWidth(0,140)
        self.tabla_modificar_proyecto.setColumnWidth(1,150)
        self.tabla_modificar_proyecto.setColumnWidth(2,133)
        self.tabla_modificar_proyecto.setColumnWidth(3,133)
        self.tabla_modificar_proyecto.setColumnWidth(4,134)
        self.tabla_modificar_proyecto.setColumnWidth(5,340)
        self.tabla_modificar_proyecto.setColumnWidth(6,468)

        self.tabla_modificar_proyecto.setGeometry(QRect(40, 410, 1500, 200))
        self.tabla_modificar_proyecto.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

####BUSCAR PROYECTO##################
        self.pagina_buscar_proyecto = QWidget()
        self.stackedWidget.addWidget(self.pagina_buscar_proyecto)
        self.label_buscar_proyecto = QLabel("Codigo de proyecto a buscar:",self.pagina_buscar_proyecto)
        self.label_buscar_proyecto.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_buscar_proyecto.setGeometry(QRect(40, 370, 325, 30))
        self.label_buscar_proyecto.setFont(font)

        self.buscar_proyecto_datos = QLineEdit(self.pagina_buscar_proyecto)
        self.buscar_proyecto_datos.setPlaceholderText("1")
        self.buscar_proyecto_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.buscar_proyecto_datos.setGeometry(QRect(370, 370, 350, 30))
        self.buscar_proyecto_datos.setFont(font)

        self.boton_buscar_proyecto = QPushButton("Buscar Proyecto", self.pagina_buscar_proyecto)
        self.boton_buscar_proyecto.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_buscar_proyecto.setGeometry(QRect(725, 370, 160, 30))
        self.boton_buscar_proyecto.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_buscar_proyecto.setIcon(icon27)
        self.boton_buscar_proyecto.setIconSize(QSize(18, 18))

        self.tabla_buscar_proyecto = QTableWidget(self.pagina_buscar_proyecto)
        if (self.tabla_buscar_proyecto.columnCount() < 7):
            self.tabla_buscar_proyecto.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("CODIGO PROYECTO")
        self.tabla_buscar_proyecto.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_buscar_proyecto.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("FECHA INICIO")
        self.tabla_buscar_proyecto.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA TERMINO")
        self.tabla_buscar_proyecto.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("PRESUPUESTO")
        self.tabla_buscar_proyecto.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("CLIENTE")
        self.tabla_buscar_proyecto.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_buscar_proyecto.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_buscar_proyecto.setColumnWidth(0,140)
        self.tabla_buscar_proyecto.setColumnWidth(1,150)
        self.tabla_buscar_proyecto.setColumnWidth(2,133)
        self.tabla_buscar_proyecto.setColumnWidth(3,133)
        self.tabla_buscar_proyecto.setColumnWidth(4,134)
        self.tabla_buscar_proyecto.setColumnWidth(5,340)
        self.tabla_buscar_proyecto.setColumnWidth(6,468)

        self.tabla_buscar_proyecto.setGeometry(QRect(40, 410, 1500, 400))
        self.tabla_buscar_proyecto.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")
        
#############MOSTRAR PROYECTO################
        self.pagina_mostrar_proyecto = QWidget()
        self.stackedWidget.addWidget(self.pagina_mostrar_proyecto)

        self.tabla_mostrar_proyecto2 = QTableWidget(self.pagina_mostrar_proyecto)
        if (self.tabla_mostrar_proyecto2.columnCount() < 7):
            self.tabla_mostrar_proyecto2.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem("PROYECTO")
        self.tabla_mostrar_proyecto2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("NOMBRE")
        self.tabla_mostrar_proyecto2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("FECHA INICIO")
        self.tabla_mostrar_proyecto2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("FECHA TERMINO")
        self.tabla_mostrar_proyecto2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("PRESUPUESTO")
        self.tabla_mostrar_proyecto2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("CLIENTE")
        self.tabla_mostrar_proyecto2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("DIRECCION")
        self.tabla_mostrar_proyecto2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_mostrar_proyecto2.setColumnWidth(0,140)
        self.tabla_mostrar_proyecto2.setColumnWidth(1,150)
        self.tabla_mostrar_proyecto2.setColumnWidth(2,133)
        self.tabla_mostrar_proyecto2.setColumnWidth(3,133)
        self.tabla_mostrar_proyecto2.setColumnWidth(4,134)
        self.tabla_mostrar_proyecto2.setColumnWidth(5,340)
        self.tabla_mostrar_proyecto2.setColumnWidth(6,468)

        self.tabla_mostrar_proyecto2.setGeometry(QRect(40, 110, 1500, 700))
        self.tabla_mostrar_proyecto2.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

###### AGREGAR IVA ###################
        self.pagina_agregar_iva = QWidget()
        self.stackedWidget.addWidget(self.pagina_agregar_iva)

        self.fecha_arribaiz = QLabel("Fecha:",self.pagina_agregar_iva)
        self.fecha_arribaiz.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha_arribaiz.setGeometry(QRect(1340, 40, 70, 30))
        self.fecha_arribaiz.setFont(font)

        self.ahora = datetime.now()
        self.fecha_arribaiz = self.ahora.strftime(("%d/%m/%Y"))

        self.fecha_arribaiz_datos = QLabel(self.pagina_agregar_iva)
        self.fecha_arribaiz_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_arribaiz_datos.setGeometry(QRect(1420, 40, 114, 30))
        self.fecha_arribaiz_datos.setFont(font)
        self.fecha_arribaiz_datos.setText(self.fecha_resul)            

        self.porcentaje_iva = QLabel("Porcentaje:",self.pagina_agregar_iva)
        self.porcentaje_iva.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.porcentaje_iva.setGeometry(QRect(40, 280, 140, 30))
        self.porcentaje_iva.setFont(font)

        self.porcentaje_iva_datos = QLineEdit(self.pagina_agregar_iva)
        self.porcentaje_iva_datos.setPlaceholderText("16")
        self.porcentaje_iva_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.porcentaje_iva_datos.setGeometry(QRect(185, 280, 130, 30))
        self.porcentaje_iva_datos.setFont(font)

        self.fecha_termino_iva = QLabel("Fecha Inicio:",self.pagina_agregar_iva)
        self.fecha_termino_iva.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha_termino_iva.setGeometry(QRect(40, 320, 170, 30))
        self.fecha_termino_iva.setFont(font)

        self.fecha_arribaiz_datos2 = QLabel(self.pagina_agregar_iva)
        self.fecha_arribaiz_datos2.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_arribaiz_datos2.setGeometry(QRect(215, 320, 134, 30))
        self.fecha_arribaiz_datos2.setFont(font)
        self.fecha_arribaiz_datos2.setText(self.fecha_resul)    

        self.boton_añadir_iva = QPushButton("Añadir IVA", self.pagina_agregar_iva)
        self.boton_añadir_iva.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_añadir_iva.setGeometry(QRect(40, 360, 140, 30))
        self.boton_añadir_iva.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_añadir_iva.setIcon(icon27)
        self.boton_añadir_iva.setIconSize(QSize(18, 18))

        self.tabla_agregar_iva = QTableWidget(self.pagina_agregar_iva)
        if (self.tabla_agregar_iva.columnCount() < 3):
            self.tabla_agregar_iva.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem("CODIGO IVA")
        self.tabla_agregar_iva.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("PORCENTAJE")
        self.tabla_agregar_iva.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("FECHA")
        self.tabla_agregar_iva.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabla_agregar_iva.setColumnWidth(0,80)
        self.tabla_agregar_iva.setColumnWidth(1,100)
        self.tabla_agregar_iva.setColumnWidth(2,100)

        self.tabla_agregar_iva.setGeometry(QRect(40, 400, 282, 200))
        self.tabla_agregar_iva.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")        

        self.boton_mostrar_iva = QPushButton("Mostrar IVA", self.pagina_agregar_iva)
        self.boton_mostrar_iva.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_mostrar_iva.setGeometry(QRect(570, 360, 140, 30))
        self.boton_mostrar_iva.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_mostrar_iva.setIcon(icon27)
        self.boton_mostrar_iva.setIconSize(QSize(18, 18))

        self.tabla_mostrar_iva = QTableWidget(self.pagina_agregar_iva)
        if (self.tabla_mostrar_iva.columnCount() < 3):
            self.tabla_mostrar_iva.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem("CODIGO IVA")
        self.tabla_mostrar_iva.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("PORCENTAJE")
        self.tabla_mostrar_iva.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("FECHA")
        self.tabla_mostrar_iva.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabla_mostrar_iva.setColumnWidth(0,80)
        self.tabla_mostrar_iva.setColumnWidth(1,100)
        self.tabla_mostrar_iva.setColumnWidth(2,100)

        self.tabla_mostrar_iva.setGeometry(QRect(500, 400, 282, 200))
        self.tabla_mostrar_iva.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")   

##############################################VENTA########################################################################################################
######AGREGAR VENTA####################
        self.pagina_agregar_venta = QWidget()
        self.fecha = QLabel("Fecha:",self.pagina_agregar_venta)
        self.fecha.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha.setGeometry(QRect(1340, 40, 70, 30))
        self.stackedWidget.addWidget(self.pagina_agregar_venta)
        self.fecha.setFont(font)
        
        self.contador_agregar_venta = 1

        self.ahora = datetime.now()
        self.fecha_resul = self.ahora.strftime(("%d/%m/%Y"))

        self.fecha_datos = QLabel(self.pagina_agregar_venta)
        self.fecha_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_datos.setGeometry(QRect(1420, 40, 114, 30))
        self.fecha_datos.setFont(font)
        self.fecha_datos.setText(self.fecha_resul)

        self.codigo_venta = QLabel("Folio Venta:",self.pagina_agregar_venta)
        self.codigo_venta.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_venta.setGeometry(QRect(40, 120, 130, 30))
        self.codigo_venta.setFont(font)

        self.codigo_venta_datos = QLabel(self.pagina_agregar_venta)
        self.codigo_venta_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_venta_datos.setGeometry(QRect(175, 120, 100, 30))
        self.codigo_venta_datos.setFont(font)
        self.codigo_venta_datos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.cliente_venta = QLabel("Codigo Cliente:",self.pagina_agregar_venta)
        self.cliente_venta.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.cliente_venta.setGeometry(QRect(40, 160, 165, 30))
        self.cliente_venta.setFont(font)

        self.cliente_venta_datos = QLineEdit(self.pagina_agregar_venta)
        self.cliente_venta_datos.setPlaceholderText("1")
        self.cliente_venta_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.cliente_venta_datos.setGeometry(QRect(210, 160, 70, 30))
        self.cliente_venta_datos.setFont(font)

        self.cliente_venta_resultado = QLabel(self.pagina_agregar_venta)
        self.cliente_venta_resultado.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.cliente_venta_resultado.setGeometry(QRect(285, 160, 700, 30))
        self.cliente_venta_resultado.setFont(font)

        self.empleado_venta = QLabel("Codigo Empleado:",self.pagina_agregar_venta)
        self.empleado_venta.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.empleado_venta.setGeometry(QRect(40, 200, 200, 30))
        self.empleado_venta.setFont(font)

        self.empleado_venta_datos = QLineEdit(self.pagina_agregar_venta)
        self.empleado_venta_datos.setPlaceholderText("1")
        self.empleado_venta_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.empleado_venta_datos.setGeometry(QRect(245, 200, 70, 30))
        self.empleado_venta_datos.setFont(font)

        self.empleado_venta_resultado = QLabel(self.pagina_agregar_venta)
        self.empleado_venta_resultado.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.empleado_venta_resultado.setGeometry(QRect(320, 200, 700, 30))
        self.empleado_venta_resultado.setFont(font)

        self.codigo_producto_venta = QLabel("Codigo Producto:",self.pagina_agregar_venta)
        self.codigo_producto_venta.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_producto_venta.setGeometry(QRect(40, 240, 190, 30))
        self.codigo_producto_venta.setFont(font)

        self.codigo_producto_venta_datos = QLineEdit(self.pagina_agregar_venta)
        self.codigo_producto_venta_datos.setPlaceholderText("1")
        self.codigo_producto_venta_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_producto_venta_datos.setGeometry(QRect(235, 240, 70, 30))
        self.codigo_producto_venta_datos.setFont(font)

        self.codigo_producto_venta_resultados = QLabel(self.pagina_agregar_venta)
        self.codigo_producto_venta_resultados.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_producto_venta_resultados.setGeometry(QRect(310, 240, 700, 30))
        self.codigo_producto_venta_resultados.setFont(font)

        self.cantidad_venta = QLabel("Cantidad:",self.pagina_agregar_venta)
        self.cantidad_venta.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.cantidad_venta.setGeometry(QRect(40, 280, 110, 30))
        self.cantidad_venta.setFont(font)

        self.cantidad_venta_datos = QLineEdit(self.pagina_agregar_venta)
        self.cantidad_venta_datos.setPlaceholderText("15")
        self.cantidad_venta_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.cantidad_venta_datos.setGeometry(QRect(155, 280, 100, 30))
        self.cantidad_venta_datos.setFont(font)

        self.inventario_venta = QLabel("Inventario:",self.pagina_agregar_venta)
        self.inventario_venta.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.inventario_venta.setGeometry(QRect(280, 280, 120, 30))
        self.inventario_venta.setFont(font)

        self.inventario_venta_resultados = QLabel(self.pagina_agregar_venta)
        self.inventario_venta_resultados.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.inventario_venta_resultados.setGeometry(QRect(405, 280, 100, 30))
        self.inventario_venta_resultados.setFont(font)

        self.boton_añadir_producto_venta = QPushButton("Añadir Producto", self.pagina_agregar_venta)
        self.boton_añadir_producto_venta.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_añadir_producto_venta.setGeometry(QRect(40, 320, 120, 30))
        self.boton_añadir_producto_venta.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_añadir_producto_venta.setIcon(icon27)
        self.boton_añadir_producto_venta.setIconSize(QSize(18, 18))

        self.boton_añadir_total_venta = QPushButton("Terminar Venta", self.pagina_agregar_venta)
        self.boton_añadir_total_venta.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_añadir_total_venta.setGeometry(QRect(1050, 770, 0, 30))
        self.boton_añadir_total_venta.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_añadir_total_venta.setIcon(icon27)
        self.boton_añadir_total_venta.setIconSize(QSize(18, 18))

        self.tabla_agregar_productos_venta = QTableWidget(self.pagina_agregar_venta)
        if (self.tabla_agregar_productos_venta.columnCount() < 5):
            self.tabla_agregar_productos_venta.setColumnCount(5)
        __qtablewidgetitem1 = QTableWidgetItem("PRODUCTO")
        self.tabla_agregar_productos_venta.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("CANTIDAD")
        self.tabla_agregar_productos_venta.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("TIPO")
        self.tabla_agregar_productos_venta.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("PRECIO UNITARIO")
        self.tabla_agregar_productos_venta.setHorizontalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TOTAL PRODUCTO")
        self.tabla_agregar_productos_venta.setHorizontalHeaderItem(4, __qtablewidgetitem5)
        self.tabla_agregar_productos_venta.setColumnWidth(0,314)
        self.tabla_agregar_productos_venta.setColumnWidth(1,200)
        self.tabla_agregar_productos_venta.setColumnWidth(2,214)
        self.tabla_agregar_productos_venta.setColumnWidth(3,200)
        self.tabla_agregar_productos_venta.setColumnWidth(4,200)

        self.tabla_agregar_productos_venta.setGeometry(QRect(40, 360, 1130, 400))
        self.tabla_agregar_productos_venta.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

        self.iva_venta = QLabel("IVA:",self.pagina_agregar_venta)
        self.iva_venta.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.iva_venta.setGeometry(QRect(40, 770, 50, 30))
        self.iva_venta.setFont(font)

        self.iva_venta_datos = QLabel(self.pagina_agregar_venta)
        self.iva_venta_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.iva_venta_datos.setGeometry(QRect(95, 770, 170, 30))
        self.iva_venta_datos.setFont(font)

        self.subtotal_venta = QLabel("SUBTOTAL:",self.pagina_agregar_venta)
        self.subtotal_venta.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.subtotal_venta.setGeometry(QRect(40, 810, 130, 30))
        self.subtotal_venta.setFont(font)

        self.subtotal_venta_datos = QLabel(self.pagina_agregar_venta)
        self.subtotal_venta_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.subtotal_venta_datos.setGeometry(QRect(175, 810, 170, 30))
        self.subtotal_venta_datos.setFont(font)

        self.total_venta = QLabel("TOTAL:",self.pagina_agregar_venta)
        self.total_venta.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.total_venta.setGeometry(QRect(40, 850, 80, 30))
        self.total_venta.setFont(font)

        self.total_venta_datos = QLabel(self.pagina_agregar_venta)
        self.total_venta_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.total_venta_datos.setGeometry(QRect(125, 850, 170, 30))
        self.total_venta_datos.setFont(font)
###### BUSCAR VENTA####################

        self.pagina_buscar_venta = QWidget()
        self.stackedWidget.addWidget(self.pagina_buscar_venta)
        self.label_buscar_venta = QLabel("Folio a buscar:",self.pagina_buscar_venta)
        self.label_buscar_venta.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_buscar_venta.setGeometry(QRect(40, 160, 165, 30))
        self.label_buscar_venta.setFont(font)

        self.buscar_venta_datos = QLineEdit(self.pagina_buscar_venta)
        self.buscar_venta_datos.setPlaceholderText("1")
        self.buscar_venta_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.buscar_venta_datos.setGeometry(QRect(210, 160, 350, 30))
        self.buscar_venta_datos.setFont(font)

        self.boton_buscar_venta = QPushButton("Buscar Venta", self.pagina_buscar_venta)
        self.boton_buscar_venta.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_buscar_venta.setGeometry(QRect(565, 160, 160, 30))
        self.boton_buscar_venta.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_buscar_venta.setIcon(icon27)
        self.boton_buscar_venta.setIconSize(QSize(18, 18))

        self.codigo_venta_buscar = QLabel("Folio Venta:",self.pagina_buscar_venta)
        self.codigo_venta_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_venta_buscar.setGeometry(QRect(40, 210, 130, 30))
        self.codigo_venta_buscar.setFont(font)

        self.codigo_venta_buscar_datos = QLabel(self.pagina_buscar_venta)
        self.codigo_venta_buscar_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_venta_buscar_datos.setGeometry(QRect(175, 210, 100, 30))
        self.codigo_venta_buscar_datos.setFont(font)
        self.codigo_venta_buscar_datos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)


        self.cliente_venta_buscar = QLabel("Nombre Cliente:",self.pagina_buscar_venta)
        self.cliente_venta_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.cliente_venta_buscar.setGeometry(QRect(40, 250, 170, 30))
        self.cliente_venta_buscar.setFont(font)
        
        self.cliente_venta_buscar_resultado = QLabel(self.pagina_buscar_venta)
        self.cliente_venta_buscar_resultado.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.cliente_venta_buscar_resultado.setGeometry(QRect(215, 250, 700, 30))
        self.cliente_venta_buscar_resultado.setFont(font)

        self.trabajador_venta_buscar = QLabel("Nombre Trabajador:",self.pagina_buscar_venta)
        self.trabajador_venta_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.trabajador_venta_buscar.setGeometry(QRect(40, 290, 210, 30))
        self.trabajador_venta_buscar.setFont(font)
        
        self.trabajador_venta_buscar_resultado = QLabel(self.pagina_buscar_venta)
        self.trabajador_venta_buscar_resultado.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.trabajador_venta_buscar_resultado.setGeometry(QRect(255, 290, 700, 30))
        self.trabajador_venta_buscar_resultado.setFont(font)

        self.fecha_venta_buscar = QLabel("Fecha:",self.pagina_buscar_venta)
        self.fecha_venta_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha_venta_buscar.setGeometry(QRect(40, 330, 70, 30))
        self.fecha_venta_buscar.setFont(font)
        
        self.fecha_venta_buscar_resultado = QLabel(self.pagina_buscar_venta)
        self.fecha_venta_buscar_resultado.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_venta_buscar_resultado.setGeometry(QRect(115, 330, 140, 30))
        self.fecha_venta_buscar_resultado.setFont(font)

        self.tabla_buscar_productos_venta = QTableWidget(self.pagina_buscar_venta)
        if (self.tabla_buscar_productos_venta.columnCount() < 5):
            self.tabla_buscar_productos_venta.setColumnCount(5)
        __qtablewidgetitem1 = QTableWidgetItem("PRODUCTO")
        self.tabla_buscar_productos_venta.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("CANTIDAD")
        self.tabla_buscar_productos_venta.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("TIPO")
        self.tabla_buscar_productos_venta.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("PRECIO UNITARIO")
        self.tabla_buscar_productos_venta.setHorizontalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("SUBTOTAL")
        self.tabla_buscar_productos_venta.setHorizontalHeaderItem(4, __qtablewidgetitem5)
        self.tabla_buscar_productos_venta.setColumnWidth(0,314)
        self.tabla_buscar_productos_venta.setColumnWidth(1,200)
        self.tabla_buscar_productos_venta.setColumnWidth(2,214)
        self.tabla_buscar_productos_venta.setColumnWidth(3,200)
        self.tabla_buscar_productos_venta.setColumnWidth(4,200)

        self.tabla_buscar_productos_venta.setGeometry(QRect(40, 410, 1130, 400))
        self.tabla_buscar_productos_venta.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

        self.iva_venta_buscar = QLabel("IVA:",self.pagina_buscar_venta)
        self.iva_venta_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.iva_venta_buscar.setGeometry(QRect(40, 820, 50, 30))
        self.iva_venta_buscar.setFont(font)

        self.iva_venta_buscar_datos = QLabel(self.pagina_buscar_venta)
        self.iva_venta_buscar_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.iva_venta_buscar_datos.setGeometry(QRect(95, 820, 170, 30))
        self.iva_venta_buscar_datos.setFont(font)

        self.subtotal_venta_buscar = QLabel("SUBTOTAL:",self.pagina_buscar_venta)
        self.subtotal_venta_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.subtotal_venta_buscar.setGeometry(QRect(40, 860, 130, 30))
        self.subtotal_venta_buscar.setFont(font)

        self.subtotal_venta_buscar_datos = QLabel(self.pagina_buscar_venta)
        self.subtotal_venta_buscar_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.subtotal_venta_buscar_datos.setGeometry(QRect(175, 860, 170, 30))
        self.subtotal_venta_buscar_datos.setFont(font)

        self.total_venta_buscar = QLabel("TOTAL:",self.pagina_buscar_venta)
        self.total_venta_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.total_venta_buscar.setGeometry(QRect(40, 900, 80, 30))
        self.total_venta_buscar.setFont(font)

        self.total_venta_buscar_datos = QLabel(self.pagina_buscar_venta)
        self.total_venta_buscar_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.total_venta_buscar_datos.setGeometry(QRect(125, 900, 170, 30))
        self.total_venta_buscar_datos.setFont(font)
########## MOSTRAR VENTA###########
        self.pagina_mostrar_venta = QWidget()
        self.stackedWidget.addWidget(self.pagina_mostrar_venta)

        self.tabla_mostrar_venta = QTableWidget(self.pagina_mostrar_venta)
        if (self.tabla_mostrar_venta.columnCount() < 9):
            self.tabla_mostrar_venta.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem("FOLIO")
        self.tabla_mostrar_venta.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("FECHA")
        self.tabla_mostrar_venta.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("CLIENTE")
        self.tabla_mostrar_venta.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("EMPLEADO")
        self.tabla_mostrar_venta.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("PRODUCTO")
        self.tabla_mostrar_venta.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("CANTIDAD")
        self.tabla_mostrar_venta.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("TIPO")
        self.tabla_mostrar_venta.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem("PRECIO")
        self.tabla_mostrar_venta.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem("SUBTOTAL")
        self.tabla_mostrar_venta.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tabla_mostrar_venta.setColumnWidth(0,50)
        self.tabla_mostrar_venta.setColumnWidth(1,100)
        self.tabla_mostrar_venta.setColumnWidth(2,300)
        self.tabla_mostrar_venta.setColumnWidth(3,300)
        self.tabla_mostrar_venta.setColumnWidth(4,150)
        self.tabla_mostrar_venta.setColumnWidth(5,100)
        self.tabla_mostrar_venta.setColumnWidth(6,150)
        self.tabla_mostrar_venta.setColumnWidth(7,150)
        self.tabla_mostrar_venta.setColumnWidth(8,198)

        self.tabla_mostrar_venta.setGeometry(QRect(40, 110, 1500, 700))
        self.tabla_mostrar_venta.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")
##################################### COMPRAS #####################################################################################
######AGREGAR COMPRA####################
        self.pagina_agregar_compra = QWidget()
        self.fecha = QLabel("Fecha:",self.pagina_agregar_compra)
        self.fecha.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha.setGeometry(QRect(1340, 40, 70, 30))
        self.stackedWidget.addWidget(self.pagina_agregar_compra)
        self.fecha.setFont(font)

        self.ahora = datetime.now()
        self.fecha_resul = self.ahora.strftime(("%d/%m/%Y"))

        self.contador_agregar_compra = 1

        self.fecha_datos = QLabel(self.pagina_agregar_compra)
        self.fecha_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_datos.setGeometry(QRect(1420, 40, 114, 30))
        self.fecha_datos.setFont(font)
        self.fecha_datos.setText(self.fecha_resul)

        self.codigo_compra = QLabel("Codigo de compra:",self.pagina_agregar_compra)
        self.codigo_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_compra.setGeometry(QRect(40, 120, 200, 30))
        self.codigo_compra.setFont(font)

        self.codigo_compra_datos = QLabel(self.pagina_agregar_compra)
        self.codigo_compra_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_compra_datos.setGeometry(QRect(245, 120, 100, 30))
        self.codigo_compra_datos.setFont(font)
        self.codigo_compra_datos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.proveedor_compra = QLabel("Codigo Proveedor:",self.pagina_agregar_compra)
        self.proveedor_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.proveedor_compra.setGeometry(QRect(40, 160, 205, 30))
        self.proveedor_compra.setFont(font)

        self.proveedor_compra_datos = QLineEdit(self.pagina_agregar_compra)
        self.proveedor_compra_datos.setPlaceholderText("1")
        self.proveedor_compra_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.proveedor_compra_datos.setGeometry(QRect(250, 160, 70, 30))
        self.proveedor_compra_datos.setFont(font)

        self.proveedor_compra_resultado = QLabel(self.pagina_agregar_compra)
        self.proveedor_compra_resultado.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.proveedor_compra_resultado.setGeometry(QRect(325, 160, 700, 30))
        self.proveedor_compra_resultado.setFont(font)

        self.empleado_compra = QLabel("Codigo Empleado:",self.pagina_agregar_compra)
        self.empleado_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.empleado_compra.setGeometry(QRect(40, 200, 200, 30))
        self.empleado_compra.setFont(font)

        self.empleado_compra_datos = QLineEdit(self.pagina_agregar_compra)
        self.empleado_compra_datos.setPlaceholderText("1")
        self.empleado_compra_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.empleado_compra_datos.setGeometry(QRect(245, 200, 70, 30))
        self.empleado_compra_datos.setFont(font)

        self.empleado_compra_resultado = QLabel(self.pagina_agregar_compra)
        self.empleado_compra_resultado.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.empleado_compra_resultado.setGeometry(QRect(320, 200, 700, 30))
        self.empleado_compra_resultado.setFont(font)

        self.codigo_producto_compra = QLabel("Codigo Producto:",self.pagina_agregar_compra)
        self.codigo_producto_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_producto_compra.setGeometry(QRect(40, 240, 190, 30))
        self.codigo_producto_compra.setFont(font)

        self.codigo_producto_compra_datos = QLineEdit(self.pagina_agregar_compra)
        self.codigo_producto_compra_datos.setPlaceholderText("1")
        self.codigo_producto_compra_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_producto_compra_datos.setGeometry(QRect(235, 240, 70, 30))
        self.codigo_producto_compra_datos.setFont(font)

        self.codigo_producto_compra_resultados = QLabel(self.pagina_agregar_compra)
        self.codigo_producto_compra_resultados.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_producto_compra_resultados.setGeometry(QRect(310, 240, 700, 30))
        self.codigo_producto_compra_resultados.setFont(font)

        self.cantidad_compra = QLabel("Cantidad:",self.pagina_agregar_compra)
        self.cantidad_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.cantidad_compra.setGeometry(QRect(40, 280, 110, 30))
        self.cantidad_compra.setFont(font)

        self.cantidad_compra_datos = QLineEdit(self.pagina_agregar_compra)
        self.cantidad_compra_datos.setPlaceholderText("15")
        self.cantidad_compra_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.cantidad_compra_datos.setGeometry(QRect(155, 280, 100, 30))
        self.cantidad_compra_datos.setFont(font)

        self.inventario_compra = QLabel("Inventario:",self.pagina_agregar_compra)
        self.inventario_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.inventario_compra.setGeometry(QRect(280, 280, 120, 30))
        self.inventario_compra.setFont(font)

        self.inventario_compra_resultados = QLabel(self.pagina_agregar_compra)
        self.inventario_compra_resultados.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.inventario_compra_resultados.setGeometry(QRect(405, 280, 100, 30))
        self.inventario_compra_resultados.setFont(font)

        self.boton_añadir_producto_compra = QPushButton("Añadir Producto", self.pagina_agregar_compra)
        self.boton_añadir_producto_compra.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_añadir_producto_compra.setGeometry(QRect(40, 320, 120, 30))
        self.boton_añadir_producto_compra.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_añadir_producto_compra.setIcon(icon27)
        self.boton_añadir_producto_compra.setIconSize(QSize(18, 18))

        self.boton_añadir_total_compra = QPushButton("Terminar Compra", self.pagina_agregar_compra)
        self.boton_añadir_total_compra.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_añadir_total_compra.setGeometry(QRect(1050, 770, 0, 30))
        self.boton_añadir_total_compra.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_añadir_total_compra.setIcon(icon27)
        self.boton_añadir_total_compra.setIconSize(QSize(18, 18))

        self.tabla_agregar_productos_compra = QTableWidget(self.pagina_agregar_compra)
        if (self.tabla_agregar_productos_compra.columnCount() < 5):
            self.tabla_agregar_productos_compra.setColumnCount(5)
        __qtablewidgetitem1 = QTableWidgetItem("PRODUCTO")
        self.tabla_agregar_productos_compra.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("CANTIDAD")
        self.tabla_agregar_productos_compra.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("TIPO")
        self.tabla_agregar_productos_compra.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("PRECIO UNITARIO")
        self.tabla_agregar_productos_compra.setHorizontalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("TOTAL PRODUCTO")
        self.tabla_agregar_productos_compra.setHorizontalHeaderItem(4, __qtablewidgetitem5)
        self.tabla_agregar_productos_compra.setColumnWidth(0,314)
        self.tabla_agregar_productos_compra.setColumnWidth(1,200)
        self.tabla_agregar_productos_compra.setColumnWidth(2,214)
        self.tabla_agregar_productos_compra.setColumnWidth(3,200)
        self.tabla_agregar_productos_compra.setColumnWidth(4,200)

        self.tabla_agregar_productos_compra.setGeometry(QRect(40, 360, 1130, 400))
        self.tabla_agregar_productos_compra.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

        self.iva_compra = QLabel("IVA:",self.pagina_agregar_compra)
        self.iva_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.iva_compra.setGeometry(QRect(40, 770, 50, 30))
        self.iva_compra.setFont(font)

        self.iva_compra_datos = QLabel(self.pagina_agregar_compra)
        self.iva_compra_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.iva_compra_datos.setGeometry(QRect(95, 770, 170, 30))
        self.iva_compra_datos.setFont(font)

        self.subtotal_compra = QLabel("SUBTOTAL:",self.pagina_agregar_compra)
        self.subtotal_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.subtotal_compra.setGeometry(QRect(40, 810, 130, 30))
        self.subtotal_compra.setFont(font)

        self.subtotal_compra_datos = QLabel(self.pagina_agregar_compra)
        self.subtotal_compra_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.subtotal_compra_datos.setGeometry(QRect(175, 810, 170, 30))
        self.subtotal_compra_datos.setFont(font)

        self.total_compra = QLabel("TOTAL:",self.pagina_agregar_compra)
        self.total_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.total_compra.setGeometry(QRect(40, 850, 80, 30))
        self.total_compra.setFont(font)

        self.total_compra_datos = QLabel(self.pagina_agregar_compra)
        self.total_compra_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.total_compra_datos.setGeometry(QRect(125, 850, 170, 30))
        self.total_compra_datos.setFont(font)

###### BUSCAR COMPRA####################
        self.pagina_buscar_compra = QWidget()
        self.stackedWidget.addWidget(self.pagina_buscar_compra)
        self.label_buscar_compra = QLabel("Folio a buscar:",self.pagina_buscar_compra)
        self.label_buscar_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.label_buscar_compra.setGeometry(QRect(40, 160, 165, 30))
        self.label_buscar_compra.setFont(font)

        self.buscar_compra_datos = QLineEdit(self.pagina_buscar_compra)
        self.buscar_compra_datos.setPlaceholderText("1")
        self.buscar_compra_datos.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.buscar_compra_datos.setGeometry(QRect(210, 160, 350, 30))
        self.buscar_compra_datos.setFont(font)

        self.boton_buscar_compra = QPushButton("Buscar Compra", self.pagina_buscar_compra)
        self.boton_buscar_compra.setStyleSheet(u"background-color:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.boton_buscar_compra.setGeometry(QRect(565, 160, 160, 30))
        self.boton_buscar_compra.setFont(font1)
        icon27 = QIcon()
        icon27.addFile(u"cheque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_buscar_compra.setIcon(icon27)
        self.boton_buscar_compra.setIconSize(QSize(18, 18))

        self.codigo_venta_compra = QLabel("Folio Compra:",self.pagina_buscar_compra)
        self.codigo_venta_compra.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.codigo_venta_compra.setGeometry(QRect(40, 210, 130, 30))
        self.codigo_venta_compra.setFont(font)

        self.codigo_compra_buscar_datos = QLabel(self.pagina_buscar_compra)
        self.codigo_compra_buscar_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.codigo_compra_buscar_datos.setGeometry(QRect(175, 210, 100, 30))
        self.codigo_compra_buscar_datos.setFont(font)
        self.codigo_compra_buscar_datos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)


        self.cliente_compra_buscar = QLabel("Nombre Proveedor:",self.pagina_buscar_compra)
        self.cliente_compra_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.cliente_compra_buscar.setGeometry(QRect(40, 250, 210, 30))
        self.cliente_compra_buscar.setFont(font)
        
        self.cliente_compra_buscar_resultado = QLabel(self.pagina_buscar_compra)
        self.cliente_compra_buscar_resultado.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.cliente_compra_buscar_resultado.setGeometry(QRect(255, 250, 700, 30))
        self.cliente_compra_buscar_resultado.setFont(font)

        self.trabajador_compra_buscar = QLabel("Nombre Trabajador:",self.pagina_buscar_compra)
        self.trabajador_compra_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.trabajador_compra_buscar.setGeometry(QRect(40, 290, 210, 30))
        self.trabajador_compra_buscar.setFont(font)
        
        self.trabajador_compra_buscar_resultado = QLabel(self.pagina_buscar_compra)
        self.trabajador_compra_buscar_resultado.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.trabajador_compra_buscar_resultado.setGeometry(QRect(255, 290, 700, 30))
        self.trabajador_compra_buscar_resultado.setFont(font)

        self.fecha_compra_buscar = QLabel("Fecha:",self.pagina_buscar_compra)
        self.fecha_compra_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.fecha_compra_buscar.setGeometry(QRect(40, 330, 70, 30))
        self.fecha_compra_buscar.setFont(font)
        
        self.fecha_compra_buscar_resultado = QLabel(self.pagina_buscar_compra)
        self.fecha_compra_buscar_resultado.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.fecha_compra_buscar_resultado.setGeometry(QRect(115, 330, 140, 30))
        self.fecha_compra_buscar_resultado.setFont(font)

        self.tabla_buscar_productos_compra = QTableWidget(self.pagina_buscar_compra)
        if (self.tabla_buscar_productos_compra.columnCount() < 5):
            self.tabla_buscar_productos_compra.setColumnCount(5)
        __qtablewidgetitem1 = QTableWidgetItem("PRODUCTO")
        self.tabla_buscar_productos_compra.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("CANTIDAD")
        self.tabla_buscar_productos_compra.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("TIPO")
        self.tabla_buscar_productos_compra.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("PRECIO UNITARIO")
        self.tabla_buscar_productos_compra.setHorizontalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("SUBTOTAL")
        self.tabla_buscar_productos_compra.setHorizontalHeaderItem(4, __qtablewidgetitem5)
        self.tabla_buscar_productos_compra.setColumnWidth(0,314)
        self.tabla_buscar_productos_compra.setColumnWidth(1,200)
        self.tabla_buscar_productos_compra.setColumnWidth(2,214)
        self.tabla_buscar_productos_compra.setColumnWidth(3,200)
        self.tabla_buscar_productos_compra.setColumnWidth(4,200)

        self.tabla_buscar_productos_compra.setGeometry(QRect(40, 410, 1130, 400))
        self.tabla_buscar_productos_compra.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

        self.iva_compra_buscar = QLabel("IVA:",self.pagina_buscar_compra)
        self.iva_compra_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.iva_compra_buscar.setGeometry(QRect(40, 820, 50, 30))
        self.iva_compra_buscar.setFont(font)

        self.iva_compra_buscar_datos = QLabel(self.pagina_buscar_compra)
        self.iva_compra_buscar_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.iva_compra_buscar_datos.setGeometry(QRect(95, 820, 170, 30))
        self.iva_compra_buscar_datos.setFont(font)

        self.subtotal_compra_buscar = QLabel("SUBTOTAL:",self.pagina_buscar_compra)
        self.subtotal_compra_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.subtotal_compra_buscar.setGeometry(QRect(40, 860, 130, 30))
        self.subtotal_compra_buscar.setFont(font)

        self.subtotal_compra_buscar_datos = QLabel(self.pagina_buscar_compra)
        self.subtotal_compra_buscar_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.subtotal_compra_buscar_datos.setGeometry(QRect(175, 860, 170, 30))
        self.subtotal_compra_buscar_datos.setFont(font)

        self.total_compra_buscar = QLabel("TOTAL:",self.pagina_buscar_compra)
        self.total_compra_buscar.setStyleSheet(u"background:rgb(99, 30, 96); color:rgb(255,255,255)")
        self.total_compra_buscar.setGeometry(QRect(40, 900, 80, 30))
        self.total_compra_buscar.setFont(font)

        self.total_compra_buscar_datos = QLabel(self.pagina_buscar_compra)
        self.total_compra_buscar_datos.setStyleSheet(u"background:rgb(77, 0, 75); color:rgb(255,255,255)")
        self.total_compra_buscar_datos.setGeometry(QRect(125, 900, 170, 30))
        self.total_compra_buscar_datos.setFont(font)

########## MOSTRAR COMPRA###########
        self.pagina_mostrar_compra = QWidget()
        self.stackedWidget.addWidget(self.pagina_mostrar_compra)

        self.tabla_mostrar_compra = QTableWidget(self.pagina_mostrar_compra)
        if (self.tabla_mostrar_compra.columnCount() < 9):
            self.tabla_mostrar_compra.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem("FOLIO")
        self.tabla_mostrar_compra.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem("FECHA")
        self.tabla_mostrar_compra.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem("PROVEEDOR")
        self.tabla_mostrar_compra.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem("EMPLEADO")
        self.tabla_mostrar_compra.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem("PRODUCTO")
        self.tabla_mostrar_compra.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem("CANTIDAD")
        self.tabla_mostrar_compra.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem("TIPO")
        self.tabla_mostrar_compra.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem("PRECIO")
        self.tabla_mostrar_compra.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem("SUBTOTAL")
        self.tabla_mostrar_compra.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tabla_mostrar_compra.setColumnWidth(0,50)
        self.tabla_mostrar_compra.setColumnWidth(1,100)
        self.tabla_mostrar_compra.setColumnWidth(2,300)
        self.tabla_mostrar_compra.setColumnWidth(3,300)
        self.tabla_mostrar_compra.setColumnWidth(4,150)
        self.tabla_mostrar_compra.setColumnWidth(5,100)
        self.tabla_mostrar_compra.setColumnWidth(6,150)
        self.tabla_mostrar_compra.setColumnWidth(7,150)
        self.tabla_mostrar_compra.setColumnWidth(8,198)

        self.tabla_mostrar_compra.setGeometry(QRect(40, 110, 1500, 700))
        self.tabla_mostrar_compra.setStyleSheet(u"background-color:rgb(255, 255, 255);color:rgb(0,0,0);")

#############METODOS VENTANAS######################################################################################################
        self.boton_sacar_menu.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
####### INVENTARIO ##############
        self.agregar_producto.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_agregar_producto))
        self.agregar_producto.clicked.connect(self.extraer_serial_producto)
        self.agregar_producto.clicked.connect(self.metodo_limpiar_contador)
        self.modificar_producto.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_modificar_producto))
        self.modificar_producto.clicked.connect(self.modificar_producto_contador)
        self.buscar_producto.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_buscar_producto))
        self.buscar_producto.clicked.connect(self.metodo_limpiar_contador)
        self.mostrar_producto.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_mostrar_producto))  
        self.mostrar_producto.clicked.connect(self.metodo_limpiar_contador)     
####### CLIENTE #################
        self.agregar_cliente.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_agregar_cliente))
        self.agregar_cliente.clicked.connect(self.extraer_serial_cliente)
        self.agregar_cliente.clicked.connect(self.metodo_limpiar_contador)
        self.modificar_cliente.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_modificar_cliente))
        self.modificar_cliente.clicked.connect(self.modificar_cliente_contador)
        self.buscar_cliente.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_buscar_cliente))
        self.buscar_cliente.clicked.connect(self.metodo_limpiar_contador)
        self.mostrar_cliente.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_mostrar_cliente))
        self.mostrar_cliente.clicked.connect(self.metodo_limpiar_contador)
####### PROVEEDOR ##############
        self.agregar_proveedor.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_agregar_proveedor))
        self.agregar_proveedor.clicked.connect(self.extraer_serial_proveedor)
        self.agregar_proveedor.clicked.connect(self.metodo_limpiar_contador)
        self.modificar_proveedor.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_modificar_proveedor))
        self.modificar_proveedor.clicked.connect(self.modificar_proveedor_contador)
        self.buscar_proveedor.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_buscar_proveedor))
        self.buscar_proveedor.clicked.connect(self.metodo_limpiar_contador)
        self.mostrar_proveedor.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_mostrar_proveedor))
        self.mostrar_proveedor.clicked.connect(self.metodo_limpiar_contador)
####### TRABAJADOR #################
        self.agregar_trabajador.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_agregar_trabajador))
        self.agregar_trabajador.clicked.connect(self.extraer_serial_trabajador)
        self.agregar_trabajador.clicked.connect(self.metodo_limpiar_contador)
        self.modificar_trabajador.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_modificar_trabajador))
        self.modificar_trabajador.clicked.connect(self.modificar_trabajador_contador)
        self.buscar_trabajador.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_buscar_trabajador))
        self.buscar_trabajador.clicked.connect(self.metodo_limpiar_contador)
        self.mostrar_trabajador.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_mostrar_trabajador))
        self.mostrar_trabajador.clicked.connect(self.metodo_limpiar_contador)
####### PROYECTO #################
        self.agregar_proyecto.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_agregar_proyecto))
        self.agregar_proyecto.clicked.connect(self.extraer_serial_proyecto)
        self.agregar_proyecto.clicked.connect(self.agregar_proyecto_contador)
        self.modificar_proyecto.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_modificar_proyecto))
        self.modificar_proyecto.clicked.connect(self.modificar_proyecto_contador)
        self.busca_proyecto.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_buscar_proyecto))
        self.busca_proyecto.clicked.connect(self.metodo_limpiar_contador)
        self.mostrar_proyectos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_mostrar_proyecto))
        self.mostrar_proyectos.clicked.connect(self.metodo_limpiar_contador)
####### IVA #################
        self.agregar_iva.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_agregar_iva))
        self.agregar_iva.clicked.connect(self.metodo_limpiar_contador)
        self.agregar_iva.clicked.connect(lambda: self.moverderecha())
####### VENTA #################
        self.agregar_venta.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_agregar_venta))
        self.agregar_venta.clicked.connect(self.extraer_serial_venta)
        self.agregar_venta.clicked.connect(self.agregar_venta_contador)
        self.buscar_venta.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_buscar_venta))
        self.buscar_venta.clicked.connect(self.metodo_limpiar_contador)
        self.mostrar_venta.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_mostrar_venta))
        self.mostrar_venta.clicked.connect(self.metodo_limpiar_contador)
####### COMPRA #################
        self.hacer_compra.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_agregar_compra))
        self.hacer_compra.clicked.connect(self.extraer_serial_compra)
        self.hacer_compra.clicked.connect(self.agregar_compra_contador)
        self.buscar_compra.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_buscar_compra))
        self.buscar_compra.clicked.connect(self.metodo_limpiar_contador)
        self.mostrar_compras.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_mostrar_compra))
        self.mostrar_compras.clicked.connect(self.metodo_limpiar_contador)

#########################################METODO BASE DE DATOS########################################################
#######AÑADIR INVENTARIO#################
        self.mostrar_producto.clicked.connect(self.mostrar_inventario_metodo) 
        self.boton_modificar_producto.clicked.connect(self.modificar_inventario_metodo)

        self.click.activated.connect(self.funcion_click) 

        self.boton_buscar_producto.clicked.connect(self.buscar_inventario_metodo)
        self.boton_añadir_producto.clicked.connect(self.agregar_inventario_metodo)
#######AÑADIR CLIENTE#################
        self.boton_añadir_cliente.clicked.connect(self.agregar_cliente_metodo)
        self.boton_modificar_cliente.clicked.connect(self.modificar_cliente_metodo)
        self.mostrar_cliente.clicked.connect(self.mostrar_cliente_metodo) 
        self.boton_buscar_cliente.clicked.connect(self.buscar_cliente_metodo)
#######AÑADIR PROVEEDOR##############
        self.boton_añadir_proveedor.clicked.connect(self.agregar_proveedor_metodo)
        self.boton_modificar_proveedor.clicked.connect(self.modificar_proveedor_metodo)
        self.boton_buscar_proveedor.clicked.connect(self.buscar_proveedor_metodo)
        self.mostrar_proveedor.clicked.connect(self.mostrar_proveedor_metodo) 
#########AÑADIR TRABAJADOR###########
        self.boton_añadir_trabajador.clicked.connect(self.agregar_trabajador_metodo) 
        self.boton_modificar_trabajador.clicked.connect(self.modificar_trabajador_metodo)
        self.boton_buscar_trabajador.clicked.connect(self.buscar_trabajador_metodo)
        self.mostrar_trabajador.clicked.connect(self.mostrar_trabajador_metodo) 
#########AÑADIR PROYECTO###########
        self.boton_añadir_proyecto.clicked.connect(self.agregar_proyecto_metodo)
        self.boton_modificar_proyecto.clicked.connect(self.modificar_proyecto_metodo)
        self.boton_buscar_proyecto.clicked.connect(self.buscar_proyecto_metodo)
        self.mostrar_proyectos.clicked.connect(self.mostrar_proyecto_metodo)  
#########AÑADIR IVA###################
        self.boton_añadir_iva.clicked.connect(self.agregar_iva_metodo)
        self.boton_mostrar_iva.clicked.connect(self.mostrar_iva_metodo)
########AÑADIR VENTA##############
        self.boton_añadir_producto_venta.clicked.connect(self.agregar_venta_metodo)
        self.boton_añadir_total_venta.clicked.connect(self.terminar_venta_metodo)
        self.boton_buscar_venta.clicked.connect(self.buscar_venta_metodo)
        self.mostrar_venta.clicked.connect(self.mostrar_venta_metodo)
#########AÑADIR COMPRA###########
        self.boton_añadir_producto_compra.clicked.connect(self.agregar_compra_metodo)
        self.boton_añadir_total_compra.clicked.connect(self.terminar_compra_metodo)
        self.boton_buscar_compra.clicked.connect(self.buscar_compra_metodo)
        self.mostrar_compras.clicked.connect(self.mostrar_compra_metodo)
##########CONTADOR#########
#######INVENTARIO############
    def metodo_limpiar_contador(self):
            self.contador = ""
    def modificar_producto_contador(self):
            self.contador = "modificar_producto"  
#######CLIENTE############
    def modificar_cliente_contador(self):
            self.contador = "modificar_cliente"  
#######PROVEEDOR############
    def modificar_proveedor_contador(self):
            self.contador = "modificar_proveedor"
#######TRABAJADOR############
    def modificar_trabajador_contador(self):
            self.contador = "modificar_trabajador"   
#######PROYECTO############
    def modificar_proyecto_contador(self):
            self.contador = "modificar_proyecto"  
    def agregar_proyecto_contador(self):
            self.contador = "agregar_proyecto"  
##########VENTA############  
    def agregar_venta_contador(self):
            self.contador = "agregar_venta"    
########COMPRA#############
    def agregar_compra_contador(self):
            self.contador = "agregar_compra"                                 
#############EXTRAER SERIAL############
    def extraer_serial_producto(self):
            conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
            cursor= conn.cursor()
            query= '''SELECT max(codigo_inventario)+1 FROM inventario '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            if respstring == "[(None,)]":
                respstringnew = "1"
                self.codigo_producto_datos.setText(respstringnew)
            else:
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")
                self.codigo_producto_datos.setText(respstring3)
    def extraer_serial_cliente(self):
            conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
            cursor= conn.cursor()
            query= '''SELECT max(codigo_cliente)+1 FROM cliente '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            if respstring == "[(None,)]":
                respstringnew = "1"
                self.codigo_cliente_datos.setText(respstringnew)
            else:
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")
                self.codigo_cliente_datos.setText(respstring3)

    def extraer_serial_proveedor(self):
            conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
            cursor= conn.cursor()
            query= '''SELECT max(codigo_proveedor)+1 FROM proveedor '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            if respstring == "[(None,)]":
                respstringnew = "1"
                self.codigo_proveedor_datos.setText(respstringnew)
            else:
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")
                self.codigo_proveedor_datos.setText(respstring3)

    def extraer_serial_trabajador(self):
            conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
            cursor= conn.cursor()
            query= '''SELECT max(codigo_trabajador)+1 FROM trabajador '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            if respstring == "[(None,)]":
                respstringnew = "1"
                self.codigo_trabajador_datos.setText(respstringnew)
            else:
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")
                self.codigo_trabajador_datos.setText(respstring3)

    def extraer_serial_proyecto(self):
            conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
            cursor= conn.cursor()
            query= '''SELECT max(codigo_proyecto)+1 FROM proyecto '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            if respstring == "[(None,)]":
                respstringnew = "1"
                self.codigo_proyecto_datos.setText(respstringnew)
            else:
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")
                self.codigo_proyecto_datos.setText(respstring3)

    def extraer_serial_venta(self):
            conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
            cursor= conn.cursor()
            query= '''SELECT max(codigo_venta)+1 FROM venta '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            if respstring == "[(None,)]":
                respstringnew = "1"
                self.codigo_venta_datos.setText(respstringnew)
                
            else:
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")
                self.codigo_venta_datos.setText(respstring3)

    def extraer_serial_compra(self):
            conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
            cursor= conn.cursor()
            query= '''SELECT max(codigo_compra)+1 FROM compra '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            if respstring == "[(None,)]":
                respstringnew = "1"
                self.codigo_compra_datos.setText(respstringnew)
                
            else:
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")
                self.codigo_compra_datos.setText(respstring3)


##############METODOS############################
    def moverderecha(self):
        if True:
            width = self.frame_izquierdo.width()
            normal = 0
            if width == 0:
                extender = 281
            else:
                extender = normal
            self.animation = QPropertyAnimation(self.frame_izquierdo, b"minimumWidth")
            self.animation.setDuration(800)
            self.animation.setStartValue(width)
            self.animation.setEndValue(extender)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def minimizar(self):
        self.showMinimized()

    def error_inventario(self):
        otraventana=Ventana_Emergente_No_Inventario(self)
        otraventana.show()
#########################METODOS BASE DE DATOS IMPLEMENTACION##############
################INVENTARIO ##############################
    def agregar_inventario_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''INSERT INTO inventario(nombre_inventario, marca_inventario, tipo_inventario, precio_inventario) VALUES (%s,%s,%s,%s)'''
        nombre_producto_agregar = self.nombre_producto_datos.text()
        marca_producto_agregar = self.marca_producto_datos.text()
        tipo_producto_agregar = self.comboBox_tipo_producto_datos.currentText()
        precio_producto_agregar = self.precio_producto_datos.text()
        cursor.execute(query,(nombre_producto_agregar,marca_producto_agregar,tipo_producto_agregar,precio_producto_agregar))
        query= '''SELECT * FROM inventario order by codigo_inventario desc limit 1'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_agregar_inventario.setRowCount(len(registros))
        for row in registros:
            self.tabla_agregar_inventario.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_agregar_inventario.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_agregar_inventario.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_agregar_inventario.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_agregar_inventario.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_agregar_inventario.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_agregar_inventario.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        self.nombre_producto_datos.setText("")
        self.marca_producto_datos.setText("")
        self.precio_producto_datos.setText("")
        query= '''SELECT max(codigo_inventario)+1 FROM inventario '''
        cursor.execute(query)
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("[(","")
        respstring3 = respstring2.replace(",)]","")
        self.codigo_producto_datos.setText(respstring3)
        conn.commit()
        conn.close()

    def modificar_inventario_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        opc = self.comboBox_label_modificar_producto.currentText()

        self.codigo_producto_modificar = self.label_codigo_modificar_producto_datos.text()
        nombre_producto_modificar = self.modificar_producto_datos.text()
        if opc == 'Nombre':
                query= '''update inventario set nombre_inventario = %s where codigo_inventario = %s'''
        elif opc == 'Marca':
                query= '''update inventario set marca_inventario = %s where codigo_inventario = %s'''
        elif opc == 'Tipo':
                query= '''update inventario set tipo_inventario = %s where codigo_inventario = %s'''
        elif opc == 'Cantidad':
                query= '''update inventario set cantidad_inventario = %s where codigo_inventario = %s'''
        elif opc == 'Precio':
                query= '''update inventario set precio_inventario = %s where codigo_inventario = %s'''
        cursor.execute(query,(nombre_producto_modificar,self.codigo_producto_modificar))
        query= '''SELECT * FROM inventario where codigo_inventario = %s'''
        cursor.execute(query,(self.codigo_producto_modificar,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_modificar_inventario.setRowCount(len(registros))
        for row in registros:
            self.tabla_modificar_inventario.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_modificar_inventario.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_modificar_inventario.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_modificar_inventario.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_modificar_inventario.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_modificar_inventario.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_modificar_inventario.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

    def funcion_click(self):

        if self.contador == "modificar_producto":
            var1=self.label_codigo_modificar_producto_datos.text()
            if len(var1) > 0:
                conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
                cursor= conn.cursor()
                click_modificar_inventario_respuesta= self.label_codigo_modificar_producto_datos.text()
                query= '''select nombre_inventario from inventario where codigo_inventario = %s'''
                cursor.execute(query,(click_modificar_inventario_respuesta,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.label_codigo_modificar_producto_informacion.setText(nuevaresqstring3)

        elif self.contador == "modificar_cliente":
            var1=self.label_codigo_modificar_cliente_datos.text()
            if len(var1) > 0:
                conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
                cursor= conn.cursor()
                click_modificar_cliente_respuesta= self.label_codigo_modificar_cliente_datos.text()
                query= '''select nombre_cliente from cliente where codigo_cliente = %s'''
                cursor.execute(query,(click_modificar_cliente_respuesta,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.label_codigo_modificar_cliente_informacion.setText(nuevaresqstring3)

        elif self.contador == "modificar_proveedor":
            var1=self.label_codigo_modificar_proveedor_datos.text()
            if len(var1) > 0:
                conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
                cursor= conn.cursor()
                click_modificar_proveedor_respuesta= self.label_codigo_modificar_proveedor_datos.text()
                query= '''select nombre_proveedor from proveedor where codigo_proveedor = %s'''
                cursor.execute(query,(click_modificar_proveedor_respuesta,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.label_codigo_modificar_proveedor_informacion.setText(nuevaresqstring3)

        elif self.contador == "modificar_trabajador":
            var1=self.label_codigo_modificar_trabajador_datos.text()
            if len(var1) > 0:
                conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
                cursor= conn.cursor()
                click_modificar_trabajador_respuesta= self.label_codigo_modificar_trabajador_datos.text()
                query= '''select nombre_trabajador from trabajador where codigo_trabajador = %s'''
                cursor.execute(query,(click_modificar_trabajador_respuesta,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.label_codigo_modificar_trabajador_informacion.setText(nuevaresqstring3)

        elif self.contador == "agregar_proyecto":
            var1=self.codigo_cliente_proyecto_datos.text()
            if len(var1) > 0:
                conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
                cursor= conn.cursor()
                click_agregar_proyecto_respuesta= self.codigo_cliente_proyecto_datos.text()
                query= '''select nombre_cliente from cliente where codigo_cliente = %s'''
                cursor.execute(query,(click_agregar_proyecto_respuesta,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.codigo_cliente_proyecto_informacion.setText(nuevaresqstring3)

        elif self.contador == "modificar_proyecto":
            var1=self.label_codigo_modificar_proyecto_datos.text()
            if len(var1) > 0:
                conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
                cursor= conn.cursor()
                click_modificar_proyecto_respuesta= self.label_codigo_modificar_proyecto_datos.text()
                query= '''select nombre_proyecto from proyecto where codigo_proyecto = %s'''
                cursor.execute(query,(click_modificar_proyecto_respuesta,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.label_codigo_modificar_proyecto_informacion.setText(nuevaresqstring3)

        elif self.contador == "agregar_venta":
            conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
            cursor= conn.cursor()
            var1=self.cliente_venta_datos.text()
            var2=self.empleado_venta_datos.text()
            var3=self.codigo_producto_venta_datos.text()
            if len(var1) > 0:
                click_agregar_venta_respuesta_cliente= self.cliente_venta_datos.text()
                query= '''select nombre_cliente from cliente where codigo_cliente = %s'''
                cursor.execute(query,(click_agregar_venta_respuesta_cliente,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.cliente_venta_resultado.setText(nuevaresqstring3)
            if len(var2) > 0:
                click_agregar_venta_respuesta_empleado= self.empleado_venta_datos.text()
                query= '''select nombre_trabajador from trabajador where codigo_trabajador = %s'''
                cursor.execute(query,(click_agregar_venta_respuesta_empleado,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.empleado_venta_resultado.setText(nuevaresqstring3)
            if len(var3) > 0:
                click_agregar_venta_respuesta_producto= self.codigo_producto_venta_datos.text()
                query= '''select nombre_inventario from inventario where codigo_inventario = %s'''
                cursor.execute(query,(click_agregar_venta_respuesta_producto,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.codigo_producto_venta_resultados.setText(nuevaresqstring3)

                query= '''select cantidad_inventario from inventario where codigo_inventario = %s'''
                cursor.execute(query,(click_agregar_venta_respuesta_producto,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[(","")
                nuevaresqstring2 = nuevaresqstring.replace(",)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                if nuevaresqstring2!="[]":
                    self.inventario_venta_existente = int(nuevaresqstring2)
                self.inventario_venta_resultados.setText(nuevaresqstring3)

        elif self.contador == "agregar_compra":
            conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
            cursor= conn.cursor()
            var1=self.proveedor_compra_datos.text()
            var2=self.empleado_compra_datos.text()
            var3=self.codigo_producto_compra_datos.text()
            if len(var1) > 0:
                click_agregar_compra_respuesta_proveedor= self.proveedor_compra_datos.text()
                query= '''select nombre_proveedor from proveedor where codigo_proveedor = %s'''
                cursor.execute(query,(click_agregar_compra_respuesta_proveedor,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.proveedor_compra_resultado.setText(nuevaresqstring3)
            if len(var2) > 0:
                click_agregar_compra_respuesta_empleado= self.empleado_compra_datos.text()
                query= '''select nombre_trabajador from trabajador where codigo_trabajador = %s'''
                cursor.execute(query,(click_agregar_compra_respuesta_empleado,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.empleado_compra_resultado.setText(nuevaresqstring3)
            if len(var3) > 0:
                click_agregar_compra_respuesta_producto= self.codigo_producto_compra_datos.text()
                query= '''select nombre_inventario from inventario where codigo_inventario = %s'''
                cursor.execute(query,(click_agregar_compra_respuesta_producto,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[('","")
                nuevaresqstring2 = nuevaresqstring.replace("',)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.codigo_producto_compra_resultados.setText(nuevaresqstring3)

                query= '''select cantidad_inventario from inventario where codigo_inventario = %s'''
                cursor.execute(query,(click_agregar_compra_respuesta_producto,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[(","")
                nuevaresqstring2 = nuevaresqstring.replace(",)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                if nuevaresqstring2!="[]":
                    self.inventario_compra_existente = int(nuevaresqstring2)
                self.inventario_compra_resultados.setText(nuevaresqstring3)

                
    def mostrar_inventario_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''SELECT codigo_inventario, nombre_inventario, fecha_inventario, marca_inventario, tipo_inventario, cantidad_inventario, precio_inventario FROM inventario order by codigo_inventario asc'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_mostrar_inventario.setRowCount(len(registros))
        for row in registros:
            self.tabla_mostrar_inventario.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_mostrar_inventario.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_mostrar_inventario.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_mostrar_inventario.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_mostrar_inventario.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_mostrar_inventario.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_mostrar_inventario.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

    def buscar_inventario_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        codigo = self.buscar_producto_datos.text()
        query= '''SELECT * FROM inventario where codigo_inventario = %s'''
        cursor.execute(query,(codigo,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_buscar_inventario.setRowCount(len(registros))
        for row in registros:
            self.tabla_buscar_inventario.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_buscar_inventario.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_buscar_inventario.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_buscar_inventario.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_buscar_inventario.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_buscar_inventario.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_buscar_inventario.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

##########################CLIENTES##########################
    def agregar_cliente_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''INSERT INTO cliente(nombre_cliente, rfc_cliente, email_cliente, telefono_cliente, direccion_cliente) VALUES (%s,%s,%s,%s,%s)'''
        nombre_cliente_agregar = self.nombre_cliente_datos.text()
        rfc_cliente_agregar = self.rfc_cliente_datos.text()
        email_cliente_agregar = self.email_cliente_datos.text()
        telefono_cliente_agregar = self.telefono_cliente_datos.text()
        direccion_cliente_agregar = self.direccion_cliente_datos.text()
        cursor.execute(query,(nombre_cliente_agregar,rfc_cliente_agregar,email_cliente_agregar,telefono_cliente_agregar,direccion_cliente_agregar))
        query= '''SELECT * FROM cliente order by codigo_cliente desc limit 1'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_agregar_cliente.setRowCount(len(registros))
        for row in registros:
            self.tabla_agregar_cliente.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_agregar_cliente.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_agregar_cliente.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_agregar_cliente.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_agregar_cliente.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_agregar_cliente.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_agregar_cliente.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        self.nombre_cliente_datos.setText("")
        self.rfc_cliente_datos.setText("")
        self.email_cliente_datos.setText("")
        self.telefono_cliente_datos.setText("")
        self.direccion_cliente_datos.setText("")
        query= '''SELECT max(codigo_cliente)+1 FROM cliente '''
        cursor.execute(query)
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("[(","")
        respstring3 = respstring2.replace(",)]","")
        self.codigo_cliente_datos.setText(respstring3)
        conn.commit()
        conn.close()

    def modificar_cliente_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        opc = self.comboBox_label_modificar_cliente.currentText()
        self.codigo_cliente_modificar = self.label_codigo_modificar_cliente_datos.text()
        nombre_cliente_modificar = self.modificar_cliente_datos.text()
        if opc == 'RFC':
                query= '''update cliente set rfc_cliente = %s where codigo_cliente = %s'''
        elif opc == 'Nombre':
                query= '''update cliente set nombre_cliente = %s where codigo_cliente = %s'''
        elif opc == 'Email':
                query= '''update cliente set email_cliente = %s where codigo_cliente = %s'''
        elif opc == 'Telefono':
                query= '''update cliente set telefono_cliente = %s where codigo_cliente = %s'''
        elif opc == 'Direccion':
                query= '''update cliente set direccion_cliente = %s where codigo_cliente = %s'''
        cursor.execute(query,(nombre_cliente_modificar,self.codigo_cliente_modificar))
        query= '''SELECT * FROM cliente where codigo_cliente = %s'''
        cursor.execute(query,(self.codigo_cliente_modificar,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_modificar_cliente.setRowCount(len(registros))
        for row in registros:
            self.tabla_modificar_cliente.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_modificar_cliente.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_modificar_cliente.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_modificar_cliente.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_modificar_cliente.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_modificar_cliente.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_modificar_cliente.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

    def mostrar_cliente_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''SELECT * FROM cliente order by codigo_cliente asc'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_mostrar_cliente.setRowCount(len(registros))
        for row in registros:
            self.tabla_mostrar_cliente.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_mostrar_cliente.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_mostrar_cliente.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_mostrar_cliente.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_mostrar_cliente.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_mostrar_cliente.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_mostrar_cliente.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

    def buscar_cliente_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        codigo = self.buscar_cliente_datos.text()
        query= '''SELECT * FROM cliente where codigo_cliente = %s'''
        cursor.execute(query,(codigo,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_buscar_cliente.setRowCount(len(registros))
        for row in registros:
            self.tabla_buscar_cliente.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_buscar_cliente.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_buscar_cliente.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_buscar_cliente.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_buscar_cliente.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_buscar_cliente.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_buscar_cliente.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

##########################PROVEEDOR##########################
    def agregar_proveedor_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''INSERT INTO proveedor(nombre_proveedor, rfc_proveedor, email_proveedor, telefono_proveedor, direccion_proveedor) VALUES (%s,%s,%s,%s,%s)'''
        nombre_proveedor_agregar = self.nombre_proveedor_datos.text()
        rfc_proveedor_agregar = self.rfc_proveedor_datos.text()
        email_proveedor_agregar = self.email_proveedor_datos.text()
        telefono_proveedor_agregar = self.telefono_proveedor_datos.text()
        direccion_proveedor_agregar = self.direccion_proveedor_datos.text()
        cursor.execute(query,(nombre_proveedor_agregar,rfc_proveedor_agregar,email_proveedor_agregar,telefono_proveedor_agregar,direccion_proveedor_agregar))
        query= '''SELECT * FROM proveedor order by codigo_proveedor desc limit 1'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_agregar_proveedor.setRowCount(len(registros))
        for row in registros:
            self.tabla_agregar_proveedor.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_agregar_proveedor.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_agregar_proveedor.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_agregar_proveedor.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_agregar_proveedor.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_agregar_proveedor.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_agregar_proveedor.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        self.nombre_proveedor_datos.setText("")
        self.rfc_proveedor_datos.setText("")
        self.email_proveedor_datos.setText("")
        self.telefono_proveedor_datos.setText("")
        self.direccion_proveedor_datos.setText("")
        query= '''SELECT max(codigo_proveedor)+1 FROM proveedor '''
        cursor.execute(query)
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("[(","")
        respstring3 = respstring2.replace(",)]","")
        self.codigo_proveedor_datos.setText(respstring3)
        conn.commit()
        conn.close()
    
    def modificar_proveedor_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        opc = self.comboBox_label_modificar_proveedor.currentText()
        self.codigo_proveedor_modificar = self.label_codigo_modificar_proveedor_datos.text()
        nombre_proveedor_modificar = self.modificar_proveedor_datos.text()
        if opc == 'RFC':
                query= '''update proveedor set rfc_proveedor = %s where codigo_proveedor = %s'''
        elif opc == 'Nombre':
                query= '''update proveedor set nombre_proveedor = %s where codigo_proveedor = %s'''
        elif opc == 'Email':
                query= '''update proveedor set email_proveedor = %s where codigo_proveedor = %s'''
        elif opc == 'Telefono':
                query= '''update proveedor set telefono_proveedor = %s where codigo_proveedor = %s'''
        elif opc == 'Direccion':
                query= '''update proveedor set direccion_proveedor = %s where codigo_proveedor = %s'''
        cursor.execute(query,(nombre_proveedor_modificar,self.codigo_proveedor_modificar))
        query= '''SELECT * FROM proveedor where codigo_proveedor = %s'''
        cursor.execute(query,(self.codigo_proveedor_modificar,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_modificar_proveedor.setRowCount(len(registros))
        for row in registros:
            self.tabla_modificar_proveedor.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_modificar_proveedor.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_modificar_proveedor.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_modificar_proveedor.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_modificar_proveedor.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_modificar_proveedor.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_modificar_proveedor.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

    def buscar_proveedor_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        codigo = self.buscar_proveedor_datos.text()
        query= '''SELECT * FROM proveedor where codigo_proveedor = %s'''
        cursor.execute(query,(codigo,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_buscar_proveedor.setRowCount(len(registros))
        for row in registros:
            self.tabla_buscar_proveedor.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_buscar_proveedor.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_buscar_proveedor.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_buscar_proveedor.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_buscar_proveedor.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_buscar_proveedor.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_buscar_proveedor.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

    def mostrar_proveedor_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''SELECT * FROM proveedor order by codigo_proveedor asc'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_mostrar_proveedor.setRowCount(len(registros))
        for row in registros:
            self.tabla_mostrar_proveedor.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_mostrar_proveedor.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_mostrar_proveedor.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_mostrar_proveedor.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_mostrar_proveedor.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_mostrar_proveedor.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_mostrar_proveedor.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

##################TRABAJADOR#######################
    def agregar_trabajador_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''INSERT INTO trabajador(nombre_trabajador, rfc_trabajador, email_trabajador, telefono_trabajador, direccion_trabajador, departamento_trabajador) VALUES (%s,%s,%s,%s,%s,%s)'''
        nombre_trabajador_agregar = self.nombre_trabajador_datos.text()
        rfc_trabajador_agregar = self.rfc_trabajador_datos.text()
        email_trabajador_agregar = self.email_trabajador_datos.text()
        telefono_trabajador_agregar = self.telefono_trabajador_datos.text()
        direccion_trabajador_agregar = self.direccion_trabajador_datos.text()
        departamento_trabajador_agregar = self.comboBox_departamento_trabajador_datos.currentText()
        cursor.execute(query,(nombre_trabajador_agregar,rfc_trabajador_agregar,email_trabajador_agregar,telefono_trabajador_agregar,direccion_trabajador_agregar, departamento_trabajador_agregar))
        query= '''SELECT * FROM trabajador order by codigo_trabajador desc limit 1'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_agregar_trabajador.setRowCount(len(registros))
        for row in registros:
            self.tabla_agregar_trabajador.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_agregar_trabajador.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_agregar_trabajador.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_agregar_trabajador.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_agregar_trabajador.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_agregar_trabajador.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_agregar_trabajador.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            self.tabla_agregar_trabajador.setItem(contador,7,QtWidgets.QTableWidgetItem(str(row[7])))
            contador += 1
        self.nombre_trabajador_datos.setText("")
        self.rfc_trabajador_datos.setText("")
        self.email_trabajador_datos.setText("")
        self.telefono_trabajador_datos.setText("")
        self.direccion_trabajador_datos.setText("")
        query= '''SELECT max(codigo_trabajador)+1 FROM trabajador '''
        cursor.execute(query)
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("[(","")
        respstring3 = respstring2.replace(",)]","")
        self.codigo_trabajador_datos.setText(respstring3)
        conn.commit()
        conn.close()

    def modificar_trabajador_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        opc = self.comboBox_label_modificar_trabajador.currentText()
        self.codigo_trabajador_modificar = self.label_codigo_modificar_trabajador_datos.text()
        nombre_trabajador_modificar = self.modificar_trabajador_datos.text()
        if opc == 'RFC':
                query= '''update trabajador set rfc_trabajador = %s where codigo_trabajador = %s'''
        elif opc == 'Nombre':
                query= '''update trabajador set nombre_trabajador = %s where codigo_trabajador = %s'''
        elif opc == 'Email':
                query= '''update trabajador set email_trabajador = %s where codigo_trabajador = %s'''
        elif opc == 'Telefono':
                query= '''update trabajador set telefono_trabajador = %s where codigo_trabajador = %s'''
        elif opc == 'Direccion':
                query= '''update trabajador set direccion_trabajador = %s where codigo_trabajador = %s'''
        elif opc == 'Departamento':
                query= '''update trabajador set departamento_trabajador = %s where codigo_trabajador = %s'''
        cursor.execute(query,(nombre_trabajador_modificar,self.codigo_trabajador_modificar))
        query= '''SELECT * FROM trabajador where codigo_trabajador = %s'''
        cursor.execute(query,(self.codigo_trabajador_modificar,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_modificar_trabajador.setRowCount(len(registros))
        for row in registros:
            self.tabla_modificar_trabajador.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_modificar_trabajador.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_modificar_trabajador.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_modificar_trabajador.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_modificar_trabajador.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_modificar_trabajador.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_modificar_trabajador.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            self.tabla_modificar_trabajador.setItem(contador,7,QtWidgets.QTableWidgetItem(str(row[7])))
            contador += 1
        conn.commit()
        conn.close()

    def buscar_trabajador_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        codigo = self.buscar_trabajador_datos.text()
        query= '''SELECT * FROM trabajador where codigo_trabajador = %s'''
        cursor.execute(query,(codigo,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_buscar_trabajador.setRowCount(len(registros))
        for row in registros:
            self.tabla_buscar_trabajador.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_buscar_trabajador.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_buscar_trabajador.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_buscar_trabajador.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_buscar_trabajador.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_buscar_trabajador.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_buscar_trabajador.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            self.tabla_buscar_trabajador.setItem(contador,7,QtWidgets.QTableWidgetItem(str(row[7])))
            contador += 1
        conn.commit()
        conn.close()

    def mostrar_trabajador_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''SELECT * FROM trabajador order by codigo_trabajador asc'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_mostrar_trabajador.setRowCount(len(registros))
        for row in registros:
            self.tabla_mostrar_trabajador.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_mostrar_trabajador.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_mostrar_trabajador.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_mostrar_trabajador.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_mostrar_trabajador.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_mostrar_trabajador.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_mostrar_trabajador.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            self.tabla_mostrar_trabajador.setItem(contador,7,QtWidgets.QTableWidgetItem(str(row[7])))
            contador += 1
        conn.commit()
        conn.close()

##################PROYECTOS#######################
    def agregar_proyecto_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''INSERT INTO proyecto( direccion_proyecto,fecha_inicio_proyecto, fecha_termino_proyecto, presupuesto_proyecto, cliente_proyecto,nombre_proyecto) VALUES (%s,%s,%s,%s,%s,%s)'''
        fecha_inicio_proyecto_agregar = self.fecha_inicio_proyecto_datos.text()
        fecha_termino_proyecto_agregar = self.fecha_termino_proyecto_datos.text()
        presupuesto_proyecto_agregar = self.presupuesto_proyecto_datos.text()
        cliente_proyecto_agregar = self.codigo_cliente_proyecto_datos.text()
        direccion_proyecto_agregar = self.direccion_proyecto_datos.text()
        nombre_proyecto_agregar = self.nombre_proyecto_datos.text()
        cursor.execute(query,(direccion_proyecto_agregar,fecha_inicio_proyecto_agregar,fecha_termino_proyecto_agregar,presupuesto_proyecto_agregar,cliente_proyecto_agregar,nombre_proyecto_agregar))
        query= '''SELECT codigo_proyecto, nombre_proyecto, fecha_inicio_proyecto, fecha_termino_proyecto, presupuesto_proyecto,(select nombre_cliente from cliente where codigo_cliente=cliente_proyecto), direccion_proyecto FROM proyecto order by codigo_proyecto desc limit 1'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_agregar_proyecto.setRowCount(len(registros))
        for row in registros:
            self.tabla_agregar_proyecto.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_agregar_proyecto.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_agregar_proyecto.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_agregar_proyecto.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_agregar_proyecto.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_agregar_proyecto.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_agregar_proyecto.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        self.fecha_inicio_proyecto_datos.setText("")
        self.fecha_termino_proyecto_datos.setText("")
        self.presupuesto_proyecto_datos.setText("")
        self.codigo_cliente_proyecto_datos.setText("")
        self.direccion_proyecto_datos.setText("")
        self.nombre_proyecto_datos.setText("")
        query= '''SELECT max(codigo_proyecto)+1 FROM proyecto '''
        cursor.execute(query)
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("[(","")
        respstring3 = respstring2.replace(",)]","")
        self.codigo_proyecto_datos.setText(respstring3)
        conn.commit()
        conn.close()

    def modificar_proyecto_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        opc = self.comboBox_label_modificar_proyecto.currentText()
        self.codigo_proyecto_modificar = self.label_codigo_modificar_proyecto_datos.text()
        nombre_proyecto_modificar = self.modificar_proyecto_datos.text()
        if opc == 'Fecha Inicio':
                query= '''update proyecto set fecha_inicio_proyecto = %s where codigo_proyecto = %s'''
        elif opc == 'Fecha Termino':
                query= '''update proyecto set fecha_termino_proyecto = %s where codigo_proyecto = %s'''
        elif opc == 'Presupuesto':
                query= '''update proyecto set presupuesto_proyecto = %s where codigo_proyecto = %s'''
        elif opc == 'Codigo Cliente':
                query= '''update proyecto set cliente_proyecto = %s where codigo_proyecto = %s'''
        elif opc == 'Nombre':
                query= '''update proyecto set nombre_proyecto = %s where codigo_proyecto = %s'''
        elif opc == 'Domicilio':
                query= '''update proyecto set direccion_proyecto = %s where codigo_proyecto = %s'''
        cursor.execute(query,(nombre_proyecto_modificar,self.codigo_proyecto_modificar))
        query= '''SELECT codigo_proyecto, nombre_proyecto, fecha_inicio_proyecto, fecha_termino_proyecto, presupuesto_proyecto,(select nombre_cliente as "Cliente" from cliente where codigo_cliente = cliente_proyecto),direccion_proyecto FROM proyecto where codigo_proyecto = %s'''
        cursor.execute(query,(self.codigo_proyecto_modificar,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_modificar_proyecto.setRowCount(len(registros))
        for row in registros:
            self.tabla_modificar_proyecto.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_modificar_proyecto.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_modificar_proyecto.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_modificar_proyecto.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_modificar_proyecto.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_modificar_proyecto.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_modificar_proyecto.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

    def buscar_proyecto_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        codigo = self.buscar_proyecto_datos.text()
        query= '''SELECT codigo_proyecto, nombre_proyecto, fecha_inicio_proyecto, fecha_termino_proyecto, presupuesto_proyecto,(select nombre_cliente as "Cliente" from cliente where codigo_cliente = cliente_proyecto),direccion_proyecto FROM proyecto where codigo_proyecto = %s'''
        cursor.execute(query,(codigo,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_buscar_proyecto.setRowCount(len(registros))
        for row in registros:
            self.tabla_buscar_proyecto.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_buscar_proyecto.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_buscar_proyecto.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_buscar_proyecto.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_buscar_proyecto.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_buscar_proyecto.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_buscar_proyecto.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

    def mostrar_proyecto_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''SELECT codigo_proyecto, nombre_proyecto, fecha_inicio_proyecto, fecha_termino_proyecto, presupuesto_proyecto,(select nombre_cliente as "Cliente" from cliente where codigo_cliente = cliente_proyecto),direccion_proyecto FROM proyecto'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_mostrar_proyecto2.setRowCount(len(registros))
        for row in registros:
            self.tabla_mostrar_proyecto2.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_mostrar_proyecto2.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_mostrar_proyecto2.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_mostrar_proyecto2.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_mostrar_proyecto2.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_mostrar_proyecto2.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_mostrar_proyecto2.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            contador += 1
        conn.commit()
        conn.close()

#####################IVA##########################
    def agregar_iva_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''INSERT INTO iva(porcentaje_iva,fecha_iva) VALUES (%s,%s)'''
        porcentaje_iva_agregar = self.porcentaje_iva_datos.text()
        fecha_iva_agregar = self.fecha_datos.text()
        cursor.execute(query,(porcentaje_iva_agregar,fecha_iva_agregar))
        query= '''SELECT * FROM iva order by codigo_iva desc limit 1'''
        cursor.execute(query,(porcentaje_iva_agregar,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_agregar_iva.setRowCount(len(registros))
        for row in registros:
            self.tabla_agregar_iva.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_agregar_iva.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_agregar_iva.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            contador += 1
        conn.commit()
        conn.close()

    def mostrar_iva_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''SELECT * FROM iva'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_mostrar_iva.setRowCount(len(registros))
        for row in registros:
            self.tabla_mostrar_iva.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_mostrar_iva.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_mostrar_iva.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            contador += 1
        conn.commit()
        conn.close()
                   
#################VENTAS#########################
    def agregar_venta_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        if self.contador_agregar_venta == 1:
            query= '''INSERT INTO venta(cliente_venta, empleado_venta) VALUES (%s,%s)'''
            cliente_venta_agregar = self.cliente_venta_datos.text()
            empleado_venta_agregar = self.empleado_venta_datos.text()
            cursor.execute(query,(cliente_venta_agregar,empleado_venta_agregar))
            
            query='''SELECT max(codigo_venta) FROM venta '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("[(","")
            respstring3 = respstring2.replace(",)]","")
            producto_venta_agregar = self.codigo_producto_venta_datos.text()
            cantidad_venta_agregar = self.cantidad_venta_datos.text()
            cantidad_venta_agregar_int = int(cantidad_venta_agregar)
            
            query= '''select cantidad_inventario from inventario where codigo_inventario = %s'''
            cursor.execute(query,(producto_venta_agregar,))
            resq = cursor.fetchall()
            resqstring = str(resq)
            nuevaresqstring = resqstring.replace("[(","")
            nuevaresqstring2 = nuevaresqstring.replace(",)]","")
            espacio = " "
            nuevaresqstring3 = espacio + nuevaresqstring2 
            if nuevaresqstring2!="[]":
                inventario_venta_existente = int(nuevaresqstring2)
            self.inventario_venta_resultados.setText(nuevaresqstring3)

            query= '''insert into descripcion_venta(codigo_venta_descripcion, codigo_producto_descripcion_venta ,cantidad_venta) values(%s,%s,%s)'''

            if cantidad_venta_agregar_int <= inventario_venta_existente:
                cursor.execute(query,(respstring3,producto_venta_agregar,cantidad_venta_agregar,))
                query= '''select (select nombre_inventario as "Producto" from inventario where codigo_inventario = codigo_producto_descripcion_venta), cantidad_venta, (select tipo_inventario as "Tipo" from inventario where codigo_inventario = codigo_producto_descripcion_venta), (select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_venta), cantidad_venta*(select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_venta) as "Subtotal" from descripcion_venta where codigo_venta_descripcion = %s'''
                cursor.execute(query,(respstring3,))
                registros= cursor.fetchall()
                contador = 0
                self.tabla_agregar_productos_venta.setRowCount(len(registros))
                for row in registros:
                    self.tabla_agregar_productos_venta.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tabla_agregar_productos_venta.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tabla_agregar_productos_venta.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tabla_agregar_productos_venta.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tabla_agregar_productos_venta.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
                    contador += 1
                query='''select sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta)) from descripcion_venta where codigo_venta_descripcion=%s'''
                cursor.execute(query,(respstring3,))
                resp= cursor.fetchall()
                respstring = str(resp)
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")
                self.total_venta_datos.setText(respstring3)
            
                query='''SELECT max(codigo_venta) FROM venta '''
                cursor.execute(query)
                resp= cursor.fetchall()
                respstring = str(resp)
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")

                query='''select sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100) from descripcion_venta where codigo_venta_descripcion=%s'''
                cursor.execute(query,(respstring3,))
                resp= cursor.fetchall()
                respstring = str(resp)
                respstring2 = respstring.replace("Decimal('","")
                respstring3 = respstring2.replace(",)","")
                respstring4 = respstring3.replace("[(","")
                respstring5 = respstring4.replace("')]","")
                respstring6 = respstring5.replace("000000000000000000","")
                self.iva_venta_datos.setText(respstring6)

                query='''SELECT max(codigo_venta) FROM venta '''
                cursor.execute(query)
                resp= cursor.fetchall()
                respstring = str(resp)
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")

                query='''select ((sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100)) - sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta)))*-1 from descripcion_venta where codigo_venta_descripcion=%s'''
                cursor.execute(query,(respstring3,))
                resp= cursor.fetchall()
                respstring = str(resp)
                respstring2 = respstring.replace("Decimal('","")
                respstring3 = respstring2.replace(",)","")
                respstring4 = respstring3.replace("[(","")
                respstring5 = respstring4.replace("')]","")
                respstring6 = respstring5.replace("000000000000000000","")
                self.subtotal_venta_datos.setText(respstring6)

                query='''update inventario set cantidad_inventario= cantidad_inventario - %s where codigo_inventario = %s'''
                cursor.execute(query,(cantidad_venta_agregar,producto_venta_agregar))
                query = '''select cantidad_inventario from inventario where codigo_inventario = %s'''
                cursor.execute(query,(producto_venta_agregar,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[(","")
                nuevaresqstring2 = nuevaresqstring.replace(",)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.inventario_venta_resultados.setText(nuevaresqstring3)

                conn.commit()
                conn.close()
                self.contador_agregar_venta = 0

                self.boton_añadir_total_venta.setGeometry(QRect(1050, 770, 120, 30))
            else:
                otraventana=Ventana_Emergente_No_Inventario(self)
                otraventana.show()


        elif self.contador_agregar_venta==0:
            query='''SELECT max(codigo_venta) FROM venta '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("[(","")
            codigo = respstring2.replace(",)]","")
            if codigo == "[(None,)]":
                codigo = "1"
                
            producto_venta_agregar = self.codigo_producto_venta_datos.text()
            cantidad_venta_agregar = self.cantidad_venta_datos.text()
            cantidad_venta_agregar_int = int(cantidad_venta_agregar)

            query= '''select cantidad_inventario from inventario where codigo_inventario = %s'''
            cursor.execute(query,(producto_venta_agregar,))
            resq = cursor.fetchall()
            resqstring = str(resq)
            nuevaresqstring = resqstring.replace("[(","")
            nuevaresqstring2 = nuevaresqstring.replace(",)]","")
            espacio = " "
            nuevaresqstring3 = espacio + nuevaresqstring2 
            if nuevaresqstring2!="[]":
                inventario_venta_existente = int(nuevaresqstring2)
            self.inventario_venta_resultados.setText(nuevaresqstring3)


            if cantidad_venta_agregar_int <= inventario_venta_existente:
                query='''select count(*) from descripcion_venta where codigo_venta_descripcion=%s and codigo_producto_descripcion_venta=%s'''
                cursor.execute(query,(codigo,producto_venta_agregar))
                resp= cursor.fetchall()
                respstring = str(resp)
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")
                respint = int(respstring3)

                if respint >= 1:
                    query="update descripcion_venta set cantidad_venta =cantidad_venta+%s where codigo_venta_descripcion=%s and codigo_producto_descripcion_venta=%s"
                    cursor.execute(query,(cantidad_venta_agregar,codigo,producto_venta_agregar))

                else:
                    query= '''insert into descripcion_venta(codigo_venta_descripcion, codigo_producto_descripcion_venta ,cantidad_venta) values(%s,%s,%s)'''
                    cursor.execute(query,(codigo,producto_venta_agregar,cantidad_venta_agregar))

                query='''update inventario set cantidad_inventario= cantidad_inventario - %s where codigo_inventario = %s'''
                cursor.execute(query,(cantidad_venta_agregar,producto_venta_agregar))
                query = '''select cantidad_inventario from inventario where codigo_inventario = %s'''
                cursor.execute(query,(producto_venta_agregar,))
                resq = cursor.fetchall()
                resqstring = str(resq)
                nuevaresqstring = resqstring.replace("[(","")
                nuevaresqstring2 = nuevaresqstring.replace(",)]","")
                espacio = " "
                nuevaresqstring3 = espacio + nuevaresqstring2 
                self.inventario_venta_resultados.setText(nuevaresqstring3)
                query= '''select (select nombre_inventario as "Producto" from inventario where codigo_inventario = codigo_producto_descripcion_venta), cantidad_venta, (select tipo_inventario as "Tipo" from inventario where codigo_inventario = codigo_producto_descripcion_venta), (select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_venta), cantidad_venta*(select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_venta) as "Subtotal" from descripcion_venta where codigo_venta_descripcion = %s'''
                cursor.execute(query,(codigo,))
                registros= cursor.fetchall()
                contador = 0
                self.tabla_agregar_productos_venta.setRowCount(len(registros))
                for row in registros:
                    self.tabla_agregar_productos_venta.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tabla_agregar_productos_venta.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tabla_agregar_productos_venta.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tabla_agregar_productos_venta.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tabla_agregar_productos_venta.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
                    contador += 1
                query='''select sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta)) from descripcion_venta where codigo_venta_descripcion=%s'''
                cursor.execute(query,(codigo,))
                resp= cursor.fetchall()
                totalventa = str(resp)
                totalventa2 = totalventa.replace("[(","")
                totalventa3 = totalventa2.replace(",)]","")
                self.total_venta_datos.setText(totalventa3)

                query='''SELECT max(codigo_venta) FROM venta '''
                cursor.execute(query)
                resp= cursor.fetchall()
                respstring = str(resp)
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")

                query='''select sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100) from descripcion_venta where codigo_venta_descripcion=%s'''
                cursor.execute(query,(respstring3,))
                resp= cursor.fetchall()
                respstring = str(resp)
                respstring2 = respstring.replace("Decimal('","")
                respstring3 = respstring2.replace(",)","")
                respstring4 = respstring3.replace("[(","")
                respstring5 = respstring4.replace("')]","")
                respstring6 = respstring5.replace("000000000000000000","")
                self.iva_venta_datos.setText(respstring6)

                query='''SELECT max(codigo_venta) FROM venta '''
                cursor.execute(query)
                resp= cursor.fetchall()
                respstring = str(resp)
                respstring2 = respstring.replace("[(","")
                respstring3 = respstring2.replace(",)]","")

                query='''select ((sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100)) - sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta)))*-1 from descripcion_venta where codigo_venta_descripcion=%s'''
                cursor.execute(query,(respstring3,))
                resp= cursor.fetchall()
                respstring = str(resp)
                respstring2 = respstring.replace("Decimal('","")
                respstring3 = respstring2.replace(",)","")
                respstring4 = respstring3.replace("[(","")
                respstring5 = respstring4.replace("')]","")
                respstring6 = respstring5.replace("000000000000000000","")
                self.subtotal_venta_datos.setText(respstring6)

                conn.commit()
                conn.close()
            else:
                otraventana=Ventana_Emergente_No_Inventario(self)
                otraventana.show()

    def terminar_venta_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        self.cliente_venta_datos.setText("")
        self.empleado_venta_datos.setText("")
        self.codigo_producto_venta_datos.setText("")
        self.cliente_venta_resultado.setText("")
        self.empleado_venta_resultado.setText("")
        self.codigo_producto_venta_resultados.setText("")
        self.cantidad_venta_datos.setText("")
        self.total_venta_datos.setText("")
        self.subtotal_venta_datos.setText("")
        self.iva_venta_datos.setText("")
        self.inventario_venta_resultados.setText("")
        query= '''SELECT max(codigo_venta)+1 FROM venta '''
        cursor.execute(query)
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("[(","")
        respstring3 = respstring2.replace(",)]","")
        self.codigo_venta_datos.setText(respstring3)
        self.contador_agregar_venta = 1
        query= '''select (select nombre_inventario as "Producto" from inventario where codigo_inventario = codigo_producto_descripcion_venta), cantidad_venta, (select tipo_inventario as "Tipo" from inventario where codigo_inventario = codigo_producto_descripcion_venta), (select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_venta), cantidad_venta*(select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_venta) as "Subtotal" from descripcion_venta where codigo_venta_descripcion > 1000000'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_agregar_productos_venta.setRowCount(len(registros))
        for row in registros:
            self.tabla_agregar_productos_venta.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_agregar_productos_venta.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_agregar_productos_venta.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_agregar_productos_venta.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_agregar_productos_venta.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            contador += 1
        conn.commit()
        conn.close()

    def buscar_venta_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        codigo = self.buscar_venta_datos.text()
        self.codigo_venta_buscar_datos.setText(codigo)
        query='''select (select nombre_cliente from cliente where codigo_cliente = cliente_venta) from venta where codigo_venta=%s'''
        cursor.execute(query,(codigo,))
        resq = cursor.fetchall()
        resqstring = str(resq)
        nuevaresqstring = resqstring.replace("[('","")
        nuevaresqstring2 = nuevaresqstring.replace("',)]","")
        espacio = " "
        nuevaresqstring3 = espacio + nuevaresqstring2 
        self.cliente_venta_buscar_resultado.setText(nuevaresqstring3)

        query='''select (select nombre_trabajador from trabajador where codigo_trabajador = empleado_venta) from venta where codigo_venta=%s'''
        cursor.execute(query,(codigo,))
        resq = cursor.fetchall()
        resqstring = str(resq)
        nuevaresqstring = resqstring.replace("[('","")
        nuevaresqstring2 = nuevaresqstring.replace("',)]","")
        espacio = " "
        nuevaresqstring3 = espacio + nuevaresqstring2 
        self.trabajador_venta_buscar_resultado.setText(nuevaresqstring3)

        query='''select fecha_venta from venta where codigo_venta=%s'''
        cursor.execute(query,(codigo,))
        resq = cursor.fetchall()
        resqstring = str(resq)
        nuevaresqstring = resqstring.replace("[(datetime.date(","")
        nuevaresqstring2 = nuevaresqstring.replace(", ","/")
        nuevaresqstring3 = nuevaresqstring2.replace("),)]","")
        espacio = " "
        nuevaresqstring4 = espacio + nuevaresqstring3 
        self.fecha_venta_buscar_resultado.setText(nuevaresqstring4)

        query= '''select(select nombre_inventario as "Producto" from inventario where codigo_inventario = codigo_producto_descripcion_venta), cantidad_venta,(select tipo_inventario as "Tipo" from inventario where codigo_inventario = codigo_producto_descripcion_venta), (select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta), (select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta)*cantidad_venta from descripcion_venta where codigo_venta_descripcion=%s'''
        cursor.execute(query,(codigo,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_buscar_productos_venta.setRowCount(len(registros))
        for row in registros:
            self.tabla_buscar_productos_venta.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_buscar_productos_venta.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_buscar_productos_venta.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_buscar_productos_venta.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_buscar_productos_venta.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            contador += 1

        query='''select sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta)) from descripcion_venta where codigo_venta_descripcion=%s'''
        cursor.execute(query,(codigo,))
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("[(","")
        respstring3 = respstring2.replace(",)]","")
        self.total_venta_buscar_datos.setText(respstring3)

        query='''select sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100) from descripcion_venta where codigo_venta_descripcion=%s'''
        cursor.execute(query,(codigo,))
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("Decimal('","")
        respstring3 = respstring2.replace(",)","")
        respstring4 = respstring3.replace("[(","")
        respstring5 = respstring4.replace("')]","")
        respstring6 = respstring5.replace("000000000000000000","")
        self.iva_venta_buscar_datos.setText(respstring6)

        query='''select ((sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100)) - sum(cantidad_venta*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta)))*-1 from descripcion_venta where codigo_venta_descripcion=%s'''
        cursor.execute(query,(codigo,))
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("Decimal('","")
        respstring3 = respstring2.replace(",)","")
        respstring4 = respstring3.replace("[(","")
        respstring5 = respstring4.replace("')]","")
        respstring6 = respstring5.replace("000000000000000000","")
        self.subtotal_venta_buscar_datos.setText(respstring6)

        conn.commit()
        conn.close()            

    def mostrar_venta_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query='''select codigo_venta,fecha_venta,(select nombre_cliente from cliente where codigo_cliente = cliente_venta), (select nombre_trabajador from trabajador where codigo_trabajador = empleado_venta), (select nombre_inventario as "Producto" from inventario where codigo_inventario = codigo_producto_descripcion_venta), cantidad_venta, (select tipo_inventario as "Tipo" from inventario where codigo_inventario = codigo_producto_descripcion_venta), (select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta), (select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_venta)*cantidad_venta from venta as v inner join descripcion_venta as dv on v.codigo_venta=dv.codigo_venta_descripcion order by codigo_venta asc '''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_mostrar_venta.setRowCount(len(registros))
        for row in registros:
            self.tabla_mostrar_venta.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_mostrar_venta.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_mostrar_venta.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_mostrar_venta.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_mostrar_venta.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_mostrar_venta.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_mostrar_venta.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            self.tabla_mostrar_venta.setItem(contador,7,QtWidgets.QTableWidgetItem(str(row[7])))
            self.tabla_mostrar_venta.setItem(contador,8,QtWidgets.QTableWidgetItem(str(row[8])))
            contador += 1
        conn.commit()
        conn.close()   

###################COMPRAS#######################
    def agregar_compra_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        if self.contador_agregar_venta == 1:
            query= '''INSERT INTO compra(proveedor_compra, empleado_compra) VALUES (%s,%s)'''
            proveedor_compra_agregar = self.proveedor_compra_datos.text()
            empleado_compra_agregar = self.empleado_compra_datos.text()
            cursor.execute(query,(proveedor_compra_agregar,empleado_compra_agregar))
            
            query='''SELECT max(codigo_compra) FROM compra '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("[(","")
            respstring3 = respstring2.replace(",)]","")
            producto_compra_agregar = self.codigo_producto_compra_datos.text()
            cantidad_compra_agregar = self.cantidad_compra_datos.text()
            
            query= '''select cantidad_inventario from inventario where codigo_inventario = %s'''
            cursor.execute(query,(producto_compra_agregar,))
            resq = cursor.fetchall()
            resqstring = str(resq)
            nuevaresqstring = resqstring.replace("[(","")
            nuevaresqstring2 = nuevaresqstring.replace(",)]","")
            espacio = " "
            nuevaresqstring3 = espacio + nuevaresqstring2 
            self.inventario_compra_resultados.setText(nuevaresqstring3)

            query= '''insert into descripcion_compra(codigo_compra_descripcion, codigo_producto_descripcion_compra ,cantidad_compra) values(%s,%s,%s)'''
            cursor.execute(query,(respstring3,producto_compra_agregar,cantidad_compra_agregar,))
            query= '''select (select nombre_inventario as "Producto" from inventario where codigo_inventario = codigo_producto_descripcion_compra), cantidad_compra, (select tipo_inventario as "Tipo" from inventario where codigo_inventario = codigo_producto_descripcion_compra), (select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_compra), cantidad_compra*(select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_compra) as "Subtotal" from descripcion_compra where codigo_compra_descripcion = %s'''
            cursor.execute(query,(respstring3,))
            registros= cursor.fetchall()
            contador = 0
            self.tabla_agregar_productos_compra.setRowCount(len(registros))
            for row in registros:
                self.tabla_agregar_productos_compra.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabla_agregar_productos_compra.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabla_agregar_productos_compra.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
                self.tabla_agregar_productos_compra.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
                self.tabla_agregar_productos_compra.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
                contador += 1
            query='''select sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra)) from descripcion_compra where codigo_compra_descripcion=%s'''
            cursor.execute(query,(respstring3,))
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("[(","")
            respstring3 = respstring2.replace(",)]","")
            self.total_compra_datos.setText(respstring3)
            
            query='''SELECT max(codigo_compra) FROM compra '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("[(","")
            respstring3 = respstring2.replace(",)]","")

            query='''select sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100) from descripcion_compra where codigo_compra_descripcion=%s'''
            cursor.execute(query,(respstring3,))
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("Decimal('","")
            respstring3 = respstring2.replace(",)","")
            respstring4 = respstring3.replace("[(","")
            respstring5 = respstring4.replace("')]","")
            respstring6 = respstring5.replace("000000000000000000","")
            self.iva_compra_datos.setText(respstring6)

            query='''SELECT max(codigo_compra) FROM compra '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("[(","")
            respstring3 = respstring2.replace(",)]","")

            query='''select ((sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100)) - sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra)))*-1 from descripcion_compra where codigo_compra_descripcion=%s'''
            cursor.execute(query,(respstring3,))
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("Decimal('","")
            respstring3 = respstring2.replace(",)","")
            respstring4 = respstring3.replace("[(","")
            respstring5 = respstring4.replace("')]","")
            respstring6 = respstring5.replace("000000000000000000","")
            self.subtotal_compra_datos.setText(respstring6)

            query='''update inventario set cantidad_inventario= cantidad_inventario + %s where codigo_inventario = %s'''
            cursor.execute(query,(cantidad_compra_agregar,producto_compra_agregar))
            query = '''select cantidad_inventario from inventario where codigo_inventario = %s'''
            cursor.execute(query,(producto_compra_agregar,))
            resq = cursor.fetchall()
            resqstring = str(resq)
            nuevaresqstring = resqstring.replace("[(","")
            nuevaresqstring2 = nuevaresqstring.replace(",)]","")
            espacio = " "
            nuevaresqstring3 = espacio + nuevaresqstring2 
            self.inventario_compra_resultados.setText(nuevaresqstring3)

            conn.commit()
            conn.close()
            self.contador_agregar_venta = 0

            self.boton_añadir_total_compra.setGeometry(QRect(1050, 770, 140, 30))



        elif self.contador_agregar_venta==0:
            query='''SELECT max(codigo_compra) FROM compra '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("[(","")
            codigo = respstring2.replace(",)]","")

            producto_compra_agregar = self.codigo_producto_compra_datos.text()
            cantidad_compra_agregar = self.cantidad_compra_datos.text()

            query= '''select cantidad_inventario from inventario where codigo_inventario = %s'''
            cursor.execute(query,(producto_compra_agregar,))
            resq = cursor.fetchall()
            resqstring = str(resq)
            nuevaresqstring = resqstring.replace("[(","")
            nuevaresqstring2 = nuevaresqstring.replace(",)]","")
            espacio = " "
            nuevaresqstring3 = espacio + nuevaresqstring2 
            self.inventario_compra_resultados.setText(nuevaresqstring3)

            query='''select count(*) from descripcion_compra where codigo_compra_descripcion=%s and codigo_producto_descripcion_compra=%s'''
            cursor.execute(query,(codigo,producto_compra_agregar))
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("[(","")
            respstring3 = respstring2.replace(",)]","")
            respint = int(respstring3)

            if respint >= 1:
                query="update descripcion_compra set cantidad_compra =cantidad_compra+%s where codigo_compra_descripcion=%s and codigo_producto_descripcion_compra=%s"
                cursor.execute(query,(cantidad_compra_agregar,codigo,producto_compra_agregar))

            else:
                query= '''insert into descripcion_compra(codigo_compra_descripcion, codigo_producto_descripcion_compra ,cantidad_compra) values(%s,%s,%s)'''
                cursor.execute(query,(codigo,producto_compra_agregar,cantidad_compra_agregar))

            query='''update inventario set cantidad_inventario= cantidad_inventario + %s where codigo_inventario = %s'''
            cursor.execute(query,(cantidad_compra_agregar,producto_compra_agregar))
            query = '''select cantidad_inventario from inventario where codigo_inventario = %s'''
            cursor.execute(query,(producto_compra_agregar,))
            resq = cursor.fetchall()
            resqstring = str(resq)
            nuevaresqstring = resqstring.replace("[(","")
            nuevaresqstring2 = nuevaresqstring.replace(",)]","")
            espacio = " "
            nuevaresqstring3 = espacio + nuevaresqstring2 
            self.inventario_compra_resultados.setText(nuevaresqstring3)
            query= '''select (select nombre_inventario as "Producto" from inventario where codigo_inventario = codigo_producto_descripcion_compra), cantidad_compra, (select tipo_inventario as "Tipo" from inventario where codigo_inventario = codigo_producto_descripcion_compra), (select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_compra), cantidad_compra*(select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_compra) as "Subtotal" from descripcion_compra where codigo_compra_descripcion = %s'''
            cursor.execute(query,(codigo,))
            registros= cursor.fetchall()
            contador = 0
            self.tabla_agregar_productos_compra.setRowCount(len(registros))
            for row in registros:
                self.tabla_agregar_productos_compra.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabla_agregar_productos_compra.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabla_agregar_productos_compra.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
                self.tabla_agregar_productos_compra.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
                self.tabla_agregar_productos_compra.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
                contador += 1
            query='''select sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra)) from descripcion_compra where codigo_compra_descripcion=%s'''
            cursor.execute(query,(codigo,))
            resp= cursor.fetchall()
            totalventa = str(resp)
            totalventa2 = totalventa.replace("[(","")
            totalventa3 = totalventa2.replace(",)]","")
            self.total_compra_datos.setText(totalventa3)

            query='''SELECT max(codigo_compra) FROM compra '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("[(","")
            respstring3 = respstring2.replace(",)]","")

            query='''select sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100) from descripcion_compra where codigo_compra_descripcion=%s'''
            cursor.execute(query,(respstring3,))
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("Decimal('","")
            respstring3 = respstring2.replace(",)","")
            respstring4 = respstring3.replace("[(","")
            respstring5 = respstring4.replace("')]","")
            respstring6 = respstring5.replace("000000000000000000","")
            self.iva_compra_datos.setText(respstring6)

            query='''SELECT max(codigo_compra) FROM compra '''
            cursor.execute(query)
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("[(","")
            respstring3 = respstring2.replace(",)]","")

            query='''select ((sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100)) - sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra)))*-1 from descripcion_compra where codigo_compra_descripcion=%s'''
            cursor.execute(query,(respstring3,))
            resp= cursor.fetchall()
            respstring = str(resp)
            respstring2 = respstring.replace("Decimal('","")
            respstring3 = respstring2.replace(",)","")
            respstring4 = respstring3.replace("[(","")
            respstring5 = respstring4.replace("')]","")
            respstring6 = respstring5.replace("000000000000000000","")
            self.subtotal_compra_datos.setText(respstring6)

            conn.commit()
            conn.close()

    def terminar_compra_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        self.proveedor_compra_datos.setText("")
        self.empleado_compra_datos.setText("")
        self.codigo_producto_compra_datos.setText("")
        self.proveedor_compra_resultado.setText("")
        self.empleado_compra_resultado.setText("")
        self.codigo_producto_compra_resultados.setText("")
        self.cantidad_compra_datos.setText("")
        self.total_compra_datos.setText("")
        self.subtotal_compra_datos.setText("")
        self.iva_compra_datos.setText("")
        self.inventario_compra_resultados.setText("")
        query= '''SELECT max(codigo_compra)+1 FROM compra '''
        cursor.execute(query)
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("[(","")
        respstring3 = respstring2.replace(",)]","")
        self.codigo_compra_datos.setText(respstring3)
        self.contador_agregar_compra = 1
        query= '''select (select nombre_inventario as "Producto" from inventario where codigo_inventario = codigo_producto_descripcion_compra), cantidad_compra, (select tipo_inventario as "Tipo" from inventario where codigo_inventario = codigo_producto_descripcion_compra), (select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_compra), cantidad_compra*(select precio_inventario as "Precio" from inventario where codigo_inventario = codigo_producto_descripcion_compra) as "Subtotal" from descripcion_compra where codigo_compra_descripcion > 1000000'''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_agregar_productos_compra.setRowCount(len(registros))
        for row in registros:
            self.tabla_agregar_productos_compra.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_agregar_productos_compra.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_agregar_productos_compra.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_agregar_productos_compra.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_agregar_productos_compra.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            contador += 1
        conn.commit()
        conn.close()

    def buscar_compra_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        codigo = self.buscar_compra_datos.text()
        self.codigo_compra_buscar_datos.setText(codigo)
        query='''select (select nombre_proveedor from proveedor where codigo_proveedor = proveedor_compra) from compra where codigo_compra=%s'''
        cursor.execute(query,(codigo,))
        resq = cursor.fetchall()
        resqstring = str(resq)
        nuevaresqstring = resqstring.replace("[('","")
        nuevaresqstring2 = nuevaresqstring.replace("',)]","")
        espacio = " "
        nuevaresqstring3 = espacio + nuevaresqstring2 
        self.cliente_compra_buscar_resultado.setText(nuevaresqstring3)

        query='''select (select nombre_trabajador from trabajador where codigo_trabajador = empleado_compra) from compra where codigo_compra=%s'''
        cursor.execute(query,(codigo,))
        resq = cursor.fetchall()
        resqstring = str(resq)
        nuevaresqstring = resqstring.replace("[('","")
        nuevaresqstring2 = nuevaresqstring.replace("',)]","")
        espacio = " "
        nuevaresqstring3 = espacio + nuevaresqstring2 
        self.trabajador_compra_buscar_resultado.setText(nuevaresqstring3)

        query='''select fecha_compra from compra where codigo_compra=%s'''
        cursor.execute(query,(codigo,))
        resq = cursor.fetchall()
        resqstring = str(resq)
        nuevaresqstring = resqstring.replace("[(datetime.date(","")
        nuevaresqstring2 = nuevaresqstring.replace(", ","/")
        nuevaresqstring3 = nuevaresqstring2.replace("),)]","")
        espacio = " "
        nuevaresqstring4 = espacio + nuevaresqstring3 
        self.fecha_compra_buscar_resultado.setText(nuevaresqstring4)

        query= '''select(select nombre_inventario as "Producto" from inventario where codigo_inventario = codigo_producto_descripcion_compra), cantidad_compra,(select tipo_inventario as "Tipo" from inventario where codigo_inventario = codigo_producto_descripcion_compra), (select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra), (select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra)*cantidad_compra from descripcion_compra where codigo_compra_descripcion=%s'''
        cursor.execute(query,(codigo,))
        registros= cursor.fetchall()
        contador = 0
        self.tabla_buscar_productos_compra.setRowCount(len(registros))
        for row in registros:
            self.tabla_buscar_productos_compra.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_buscar_productos_compra.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_buscar_productos_compra.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_buscar_productos_compra.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_buscar_productos_compra.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            contador += 1

        query='''select sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra)) from descripcion_compra where codigo_compra_descripcion=%s'''
        cursor.execute(query,(codigo,))
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("[(","")
        respstring3 = respstring2.replace(",)]","")
        self.total_compra_buscar_datos.setText(respstring3)

        query='''select sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100) from descripcion_compra where codigo_compra_descripcion=%s'''
        cursor.execute(query,(codigo,))
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("Decimal('","")
        respstring3 = respstring2.replace(",)","")
        respstring4 = respstring3.replace("[(","")
        respstring5 = respstring4.replace("')]","")
        respstring6 = respstring5.replace("000000000000000000","")
        self.iva_compra_buscar_datos.setText(respstring6)

        query='''select ((sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra))*((select porcentaje_iva from iva order by fecha_iva desc limit 1)/100)) - sum(cantidad_compra*(select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra)))*-1 from descripcion_compra where codigo_compra_descripcion=%s'''
        cursor.execute(query,(codigo,))
        resp= cursor.fetchall()
        respstring = str(resp)
        respstring2 = respstring.replace("Decimal('","")
        respstring3 = respstring2.replace(",)","")
        respstring4 = respstring3.replace("[(","")
        respstring5 = respstring4.replace("')]","")
        respstring6 = respstring5.replace("000000000000000000","")
        self.subtotal_compra_buscar_datos.setText(respstring6)

        conn.commit()
        conn.close()           

    def mostrar_compra_metodo(self):
        conn = psycopg2.connect(dbname="zamora", user="postgres", password="219748227", host="localhost", port="5432")
        cursor= conn.cursor()
        query='''select codigo_compra,fecha_compra,(select nombre_proveedor from proveedor where codigo_proveedor = proveedor_compra), (select nombre_trabajador from trabajador where codigo_trabajador = empleado_compra), (select nombre_inventario as "Producto" from inventario where codigo_inventario = codigo_producto_descripcion_compra), cantidad_compra, (select tipo_inventario as "Tipo" from inventario where codigo_inventario = codigo_producto_descripcion_compra), (select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra), (select precio_inventario as "Precio Unitario" from inventario where codigo_inventario = codigo_producto_descripcion_compra)*cantidad_compra from compra as v inner join descripcion_compra as dv on v.codigo_compra=dv.codigo_compra_descripcion order by codigo_compra asc '''
        cursor.execute(query)
        registros= cursor.fetchall()
        contador = 0
        self.tabla_mostrar_compra.setRowCount(len(registros))
        for row in registros:
            self.tabla_mostrar_compra.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_mostrar_compra.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabla_mostrar_compra.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabla_mostrar_compra.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_mostrar_compra.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_mostrar_compra.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.tabla_mostrar_compra.setItem(contador,6,QtWidgets.QTableWidgetItem(str(row[6])))
            self.tabla_mostrar_compra.setItem(contador,7,QtWidgets.QTableWidgetItem(str(row[7])))
            self.tabla_mostrar_compra.setItem(contador,8,QtWidgets.QTableWidgetItem(str(row[8])))
            contador += 1
        conn.commit()
        conn.close()   
if __name__ == '__main__':
    app = QApplication([])
    window = Menu_Principal()
    window.show()
    app.exec_()