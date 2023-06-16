from odoo import api, models, fields
from odoo.exceptions import ValidationError
import re

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "motorcycle registry"
    registry_number = fields.Char(string="Registry Number", default="MRN0000",
                                    copy=False, required=True, readonly=True)
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000'))==('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')

        print(vals_list)
        return super().create(vals_list)


    vin = fields.Char(string="vin #", required=True)
    first_name = fields.Char(string='first name', required=True)
    last_name = fields.Char(string='last name', required=True)
    picture = fields.Image("Image of Bike", max_width=1920, max_height=1920)
    current_milage = fields.Float('current mileage')
    license_plate = fields.Char(string="license_plate")
    certificate_title = fields.Binary(string="certificate_title")
    register_date = fields.Date(index=True)
    owner_id = fields.Many2one(comodel_name="res.partner", string="Owner", ondelete='restrict')

    @api.constrains('vin')
    def _check_vin(self):
        for reg in self:
            if not (re.fullmatch("^[A-Z]{4}[0-9]{2}[0-9A-Z]{2}[0-9]{6}$",reg.vin)):
                raise ValidationError("""the vin number should follow the following pattern 
                                      Make - 2 Capital Letters 
                                      Model - 2 Capital Letters Year - 2 Digits 
                                      Battery Capacity - 2 Capital Letters or Numbers 
                                      Serial Number - 6 Digits""")
    
    @api.constrains('license_plate')
    def _check_license_plate(self):
        for reg in self:
            if not (re.fullmatch("^[A-Z]{1,4}[0-9]{1,3}[A-Z]{0,2}$",reg.license_plate)):
                raise ValidationError("""the license plate should follow the following pattern 
                                      1 - 4 Capital Letters
                                      1 - 3 Digits
                                      Optional 2 Capital Letters""")
                
    
