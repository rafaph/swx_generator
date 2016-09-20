from django.core.management.base import CommandError
from django.template import Template, Context
from django.utils.text import camel_case_to_spaces
from django.conf import settings
from os import path, mkdir
from shutil import copyfile

BASE_DIR = path.dirname(path.dirname(__file__))


def __camel_case_to_snake_case(value):
    return camel_case_to_spaces(value).replace(' ', '_')


def create_model(app_name, model_name):
    models_path = path.join(
        settings.BASE_DIR,
        app_name,
        'models'
    )
    init_path = path.join(models_path, '__init__.py')
    if not path.isdir(models_path):
        mkdir(models_path)

    model_name_snake_case = __camel_case_to_snake_case(model_name)
    model_file_name = '%s.py' % model_name_snake_case
    model_path = path.join(
        models_path,
        model_file_name
    )

    if path.isfile(model_path):
        raise CommandError(
            'The model file "%s" already exists' % model_file_name
        )

    model_template_path = path.join(
        BASE_DIR,
        'swx_generator',
        'tpls',
        'python',
        'model.pytpl'
    )

    with open(model_template_path, 'r') as f:
        model_template_string = f.read()

    template = Template(model_template_string)
    template_rendered = template.render(Context({
        'class_name': model_name
    }))

    with open(model_path, 'w') as f:
        f.write(template_rendered)

    with open(init_path, 'a') as f:
        f.write(
            'from .{0} import {1}\n'.format(
                model_name_snake_case,
                model_name
            )
        )


def create_view(app_name, view_name):
    views_path = path.join(
        settings.BASE_DIR,
        app_name,
        'views'
    )

    if not path.isdir(views_path):
        mkdir(
            views_path
        )
        with open(path.join(views_path, '__init__.py'), 'w') as f:
            f.write('')

    view_name_snake_case = __camel_case_to_snake_case(view_name)
    view_file_name = '%s.py' % view_name_snake_case
    view_path = path.join(
        views_path,
        view_file_name
    )

    if path.isfile(view_path):
        raise CommandError(
            'The view file "%s" already exists' % view_file_name
        )

    view_template_path = path.join(
        BASE_DIR,
        'swx_generator',
        'tpls',
        'python',
        'view.pytpl'
    )

    copyfile(
        src=view_template_path,
        dst=view_path
    )
