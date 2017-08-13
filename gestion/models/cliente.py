 #-*- coding: utf-8 -*- 
from odoo import models, fields 

class cliente(models.Model):
    _name = "cliente.cliente"
    
    name = fields.Char("Producto", required=True)
    proveedor = fields.Char("Proveedor", required=True)
    precio = fields.Float("Precio", required=True)
    fecha_hora = fields.Datetime("Fecha de Creacion", required=True)
    foto = fields.Binary("Foto")

