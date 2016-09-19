from django.core.management.base import CommandError
from django.template import Template, Context
from django.utils.text import camel_case_to_spaces
from django.conf import settings
from os import path, mkdir

BASE_DIR = path.dirname(path.dirname(__file__))


def camel_case_to_snake_case(value):
    return camel_case_to_spaces(value).replace(' ', '_')


def create_model(app_name, model_name):
    models_path = path.join(
        settings.BASE_DIR,
        app_name,
        'models'
    )

    if not path.isdir(models_path):
        mkdir(models_path)
        with open(path.join(models_path, '__init__.py'), 'wb') as f:
            f.write('')

    model_file_name = '%s.py' % camel_case_to_snake_case(model_name)
    model_path = path.join(
        models_path,
        model_file_name
    )

    if path.isfile(model_path):
        raise CommandError('The model file %r already exists' % model_file_name)

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
