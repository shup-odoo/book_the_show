{
    'name': 'Book The Show',
    'version': '1.0',
    'summary': 'Movie Booking System ',
    'desciption': """BookTheShow is an Odoo module which is a  ticketing booking  platform that allows users to book tickets for movies""",
    'category': 'Movie',
    'depends': ['base_setup', 'product'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'views/movie_genres_view.xml',
        'views/movie_language_view.xml',
        'views/screen_type_view.xml',
        'views/show_time_view.xml',
        'views/ticket_booking_view.xml',
        'views/book_the_show_view.xml'
    ],
    'demo': [
        'demo/screen_type_movie_genres_demo.xml',
        'demo/movie_language_demo.xml',
        # 'demo/book_the_show_demo.xml',
    ]
}
