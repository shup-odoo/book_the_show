from odoo import fields, models, api


class MovieGenres(models.Model):
    _name = "movie.genres"
    _description = "Movie Genres"
    # _order = "sequence"

    name = fields.Char('Name', required=True)
    color = fields.Integer(string='Color')