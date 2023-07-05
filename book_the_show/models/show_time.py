import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _


class ShowTime(models.Model):
    _name = "movie.show.time"
    _description = "Movie Show Timing"
    # _order = "sequence"

    st_movie_name = fields.Many2one('book.the.show', string="Select Movie")
    st_start_time = fields.Float(string='Time')
    st_screen_number = fields.Integer(string="Screen Number")
    st_screen_type = fields.Many2one('screen.types', string='Screen Type')
    st_language = fields.Many2one('movie.language', string='Movie Languages')

