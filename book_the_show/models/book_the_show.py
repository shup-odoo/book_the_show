import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class BookTheShow(models.Model):
    _name = "book.the.show"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "book the show"
    _rec_name = "mv_name"
    # _order = "sequence"

    mv_name = fields.Char('Movie Name ', required=True, tracking=True)
    mv_description = fields.Text('Description', required=True)
    mv_release_date = fields.Date('Release Date', tracking=True)
    mv_duration = fields.Float(string='Time')
    mv_rating = fields.Float(string="Movie Rating")
    mv_screen_type_ids = fields.Many2many('screen.types', string='Screen Type')
    mv_language_ids = fields.Many2many('movie.language', string='Movie Languages')
    mv_genres_ids = fields.Many2many('movie.genres', string='Movie Genres')
    mv_movie_show = fields.One2many('movie.show.time', 'st_movie_name')
    mv_image = fields.Binary(string="Movie Image", store=True, tracking=True)
    mv_select_movie = fields.One2many('movie.show.time', 'st_movie_name')
    status = fields.Selection(string="state",
                              selection=[('coming_soon', 'Coming_Soon'), ('new', 'New'),
                                         ('just_released', ' Just_Released'), ('old', 'Old'),
                                         ('flop', 'Flop'), ('released_on_platform', 'Released_On_Platform')],
                              copy=False, default='new',
                              tracking=True)

    _sql_constraints = [
        ('check_movie_rating', 'CHECK(mv_rating <= 10)', 'The Movie Rating should be less then 10'),
        ('mv_name_unique', 'UNIQUE(mv_name)', 'The Movie name should be unique')]

    @api.ondelete(at_uninstall=False)
    def ondelete_movie(self):
        if self.mv_status not in ('flop', 'released_on_platform'):
            raise UserError("Only flop and released on platform movies can be deleted")
