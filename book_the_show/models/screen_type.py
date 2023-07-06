from odoo import fields, models, api


class ScreenType(models.Model):
    _name = "screen.types"
    _description = "Movie Screen Types"
    # _order = "sequence"

    name = fields.Char('Name', required=True)
    # screen_id = fields.One2many("movie.show.time", "st_language")

