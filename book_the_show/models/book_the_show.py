import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class BookTheShow(models.Model):
    _name = "book.the.show"
    _description = "book the show"
    # _order = "sequence"

    mv_name = fields.Char('Movie Name ', required=True)
    mv_description = fields.Text('Description', required=True)
    mv_release_date = fields.Date('Release Date', required=True)
    mv_duration = fields.Float(string='Time')
    mv_rating = fields.Float(string="Movie Rating")
    mv_screen_type_ids = fields.Many2many('screen.types', string='Screen Type')
    mv_language_ids = fields.Many2many('movie.language', string='Movie Languages')
    mv_genres_ids = fields.Many2many('movie.genres', string='Movie Genres')
    mv_select_movie = fields.One2many('movie.show.time', 'st_movie_name')
