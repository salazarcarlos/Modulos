 #-*- coding: utf-8 -*- 

{ 
    'name': 'Gestion de Tienda', 
    'description': 'Ven y compra productos un precio comodo.', 
    'author': 'Alex Salazar',
    "website": "www.gestion.com", 
    'depends': ['base'], 
    "data": [
        "views/producto_categoria.xml",
	    "views/producto_catalogo.xml", 
	    "views/clientes.xml",
        "views/materiales.xml",
        "views/ventas.xml"
	    ],
    'application': True, 
}