 #-*- coding: utf-8 -*- 
from odoo import models, fields 

class MaterialEspeciales(models.Model):
    _name = "material.especial"
    
    name = fields.Char("Nombre del Producto", required=True)
    cantidad = fields.Float("Cantidad", required=True)
    precio = fields.Float("Precio", required=True)
    fecha_hora = fields.Datetime("Fecha de Creacion", required=True)
    foto = fields.Binary("Foto")
