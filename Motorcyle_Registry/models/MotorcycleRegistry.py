from odoo import models, fields

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"

    registry_number = fields.Char(string="registry num", required=True)
    vin = fields.Char(string="vin #", required=True)
    first_name = fields.Char(string='first name', required=True)
    last_name = fields.Char(string='last name', required=True)
    picture = fields.Image("Image of Bike", max_width=1920, max_height=1920)
    current_milage = fields.Float('current mileage')
    license_plate = fields.Char(string="license_plate")
    certificate_title = fields.Binary(string="certificate_title")
    register_date = fields.Date(index=True)