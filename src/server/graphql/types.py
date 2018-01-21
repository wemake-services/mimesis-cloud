import inspect

from collections import OrderedDict
from functools import partial

import graphene

from graphene import Field, ObjectType, String
from graphene.types.objecttype import ObjectTypeMeta
from graphene.types.options import Options
from graphene.types.utils import merge
from graphene.utils.is_base_type import is_base_type
from mimesis import Generic


def get_fields(instance, callables=False):
    def filter_condition(field):
        return not field.startswith('_')

    fields = OrderedDict()
    for name in filter(filter_condition, dir(instance)):
        field = getattr(instance, name)
        is_callable = callable(field)
        if (not is_callable and not callables) or (is_callable and callables):
            fields[name] = field

    return fields


def resolve(name, obj, context, *_args, **_kwargs):
    method = getattr(obj, name)
    return method(**context) if callable(method) else method


def get_field_args(field):
    types = {
        str: graphene.String,
        bool: graphene.Boolean,
        int: graphene.Int,
        float: graphene.Float,
    }

    try:
        args = inspect.signature(field)
        result = {}
        for name, arg in args.parameters.items():
            if arg.default is not None:
                custom_type = types[type(arg.default)]
            else:
                custom_type = graphene.String

            result.update({name: custom_type()})
        return result
    except (KeyError, ValueError):
        return {}


def make_resolvable_fields(inner_fields):
    result = {}

    for name, field in inner_fields.items():
        result.update({
            name: Field(String, **get_field_args(field)),
            'resolve_{}'.format(name): partial(resolve, name),
        })
    return result


def convert_fields_to_graph(fields):
    for name, field in fields.items():
        inner_fields = get_fields(field, callables=True)
        inner_fields = make_resolvable_fields(inner_fields)

        field_class = type(name.capitalize(), (ObjectType, ), inner_fields)
        fields[name] = Field(field_class)

    return fields


def resolve_callable(attname, default_value, root, args, context, info):
    method = getattr(root, attname, default_value)
    return method() if callable(method) else method


class GenericTypeMeta(ObjectTypeMeta):
    @staticmethod
    def __new__(cls, name, bases, attrs):
        # Also ensure initialization is only performed for subclasses of
        # DjangoObjectType
        if not is_base_type(bases, GenericTypeMeta):
            return type.__new__(cls, name, bases, attrs)

        defaults = dict(
            name=name,
            description=attrs.pop('__doc__', None),
            interfaces=[],
            default_resolver=resolve_callable,
        )

        options = Options(
            attrs.pop('Meta', None),
            **defaults,
        )
        cls = ObjectTypeMeta.__new__(
            cls, name, bases, dict(attrs, _meta=options))

        instance = Generic('en')
        options.generic_fields = convert_fields_to_graph(
            get_fields(instance),
        )

        options.fields = merge(
            options.interface_fields,
            options.generic_fields,
            options.base_fields,
            options.local_fields,
        )

        return cls


class MimesisType(ObjectType, metaclass=GenericTypeMeta):
    pass
