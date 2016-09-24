from __future__ import unicode_literals, print_function

from django.core.management.base import BaseCommand, CommandError
from swx_generator import utils

try:
    from django.core.management.base import make_option
except ImportError:
    pass


class Command(BaseCommand):
    help = """
    Create a model:\n
        python manage.py generate <app_name> --model=<model_name>\n
    Create a view:\n
        python manage.py generate <app_name> --view=<view_name>
    """

    def __init__(self, *args, **kwargs):
        if hasattr(self, 'option_list'):
            self.option_list = BaseCommand.option_list + (
                make_option(
                    '--model',
                    dest='model',
                    help='specify the django model name',
                    metavar='MODEL',
                    default=None
                ),
                make_option(
                    '--view',
                    dest='view',
                    help='specify the django view file name',
                    metavar='VIEW',
                    default=None
                ),
            )
        super(Command, self).__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            'args',
            metavar='APPNAME',
            nargs='*',
            help='specify app name',
        )
        parser.add_argument(
            '--model',
            dest='model',
            help='specify the django model name',
            metavar='MODEL',
            default=None
        )
        parser.add_argument(
            '--view',
            dest='view',
            help='specify the django view file name',
            metavar='VIEW',
            default=None
        )

    @staticmethod
    def __validate_input(*args, **kwargs):
        if len(args) == 0:
            raise CommandError('A app name must be passed as first argument.')
        if kwargs['model'] is None and kwargs['view'] is None:
            raise CommandError('A view or model must be specified.')

    def handle(self, *args, **kwargs):
        self.__validate_input(*args, **kwargs)

        if kwargs['model'] is not None:
            utils.create_model(args[0], kwargs['model'])
            if kwargs['verbosity'] > 0:
                self.stdout.write(
                    '\x1b[6;30;42m{0}\x1b[0m'.format(
                        'Model %s created with success.' % kwargs['model']
                    )
                )

        if kwargs['view'] is not None:
            utils.create_view(args[0], kwargs['view'])
            if kwargs['verbosity'] > 0:
                self.stdout.write(
                    '\x1b[6;30;42m{0}\x1b[0m'.format(
                        'View %s created with success.' % kwargs['view']
                    )
                )
