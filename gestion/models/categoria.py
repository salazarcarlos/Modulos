 #-*- coding: utf-8 -*- 

from odoo import models, fields, api

class ProductoCategoria(models.Model): 
    _name = 'producto.categoria' 

    name = fields.Char('Nombre', required=True)
    cantidad = fields.Float(string="Cantidad", required=True)
    precio = fields.Float(string="Precio", required=True) 
    fecha = fields.Date(string="Fecha de Creacion", required=True)
    is_done = fields.Boolean('Efectivo')
    visa = fields.Boolean('Visa') 


    @api.multi 
    def do_toggle_done(self):
        self.is_done = True

    @api.multi 
    def do_clear_done(self):
        self.is_done = False

    @api.multi 
    def pago_visa(self):
        self.visa = True

    @api.multi 
    def no_pago_visa(self):
        self.visa = False



class ProductoCatalogo(models.Model): 
    _name = 'producto.catalogo' 

    name = fields.Char(strging="Nombre", required=True)
    precio = fields.Float(string="Precio", required=True)
    cantidad = fields.Float(strgin="Cantidad", required=True)
    fecha = fields.Date(string="Fecha de Creacion", required=True)

    categoria = fields.Many2one('producto.categoria', string='Categoria')












        
    
