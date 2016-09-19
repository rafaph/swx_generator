from __future__ import unicode_literals, print_function

from django.core.management.base import BaseCommand, make_option, CommandError

from swx_generator import utils


class Command(BaseCommand):
    help = """
    Create a model:\n
        python manage.py generate <app_name> --model=<model_name>\n
    Create a view:\n
        python manage.py generate <app_name> --view=<view_name>
    """
    option_list = BaseCommand.option_list + (
        make_option(
            "--model",
            dest="model",
            help="specify the django model name",
            metavar="MODEL",
            default=None
        ),
        make_option(
            "--view",
            dest="view",
            help="specify the django view file name",
            metavar="VIEW",
            default=None
        ),
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
            pass
