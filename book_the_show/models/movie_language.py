from odoo import fields, models, api


class MovieLanguage(models.Model):
    _name = "movie.language"
    _description = "Movie Languages"
    # _order = "sequence"

    name = fields.Char('Name', required=True)
    # language = fields.One2many("movie.show.time", "st_screen_type")
