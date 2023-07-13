from openerp import tools
from odoo import fields, models, api, _


class YourModelName(models.Model):
    _name = 'your.model.name'
    image = fields.Binary(string="Picture", required=True)
    image_name = fields.Char("Picture Name")

    @api.model
    def create(self, values):
        if 'image' in values:
            # resize uploaded image into 250 X 250
            resize_image = tools.image_resize_image(values['image'], size=(250, 250), avoid_if_small=True)
            values['image'] = resize_image
            return super(YourModelName, self).create(values)

    @api.multi
    def write(self, values):
        if 'image' in values:
            # resize uploaded image into 250 X 250
            resize_image = tools.image_resize_image(values['image'], size=(250, 250), avoid_if_small=True)
            values['image'] = resize_image
            return super(YourModelName, self).write(values)
