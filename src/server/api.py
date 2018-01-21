from mimesis import Generic

from sanic import Blueprint, response
from sanic.exceptions import NotFound
from sanic.request import Request
from sanic.response import HTTPResponse

from simple_settings import settings


api = Blueprint('api', url_prefix='/api')


@api.route('/<resource>/<sub>')
async def handle_resource(request: Request,
                          resource: str, sub: str) -> HTTPResponse:
    """
    This route is a wrapper of :class:`mimesis.Generic`.
    It is used to serve different data over the REST API.

    Args:
        request: Sanic's request instance
        resource: first part of the url,
            name of mimesis's resource
        sub: subname of the mimesis's resource

    Returns:
        HTTPResponse: Sanic's response with json body,
            like: `{'data': 'some string'}`
    """
    language = request.args.get('lang', settings.SC_DEFAULT_LANGUAGE)

    g = Generic(language)

    try:
        obj = getattr(g, resource)
        obj = getattr(obj, sub)

    except AttributeError:
        # This means that one of the attributes
        # was not found, raise 404:
        raise NotFound('This resource does not exist')

    return response.json({'data': obj()})
