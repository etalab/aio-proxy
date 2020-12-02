from aiohttp import web


ESCAPED_CHARS = "!@#$\'\""
OUTPUT_URL = 'http://annuaire-entreprises.dataeng.etalab.studio/rpc/get_unite_legale'

routes = web.RouteTableDef()


def sanatize_param(param):
    param = param.translate({ord(c): None for c in ESCAPED_CHARS})
    param = ' & '.join(param.split())
    return param.lower()


@routes.get('/search')
async def search_endpoint(request):
    json_body = {
        'search': sanatize_param(request.rel_url.query['q']),
        'page_ask': request.rel_url.query['page'],
        'per_page_ask': request.rel_url.query['per_page']
    }

    async with request.app['http_session'] as session:
        async with session.post(OUTPUT_URL, json=json_body) as resp:
            res_status = resp.status
            res = await resp.json()

    return web.json_response(res, status=res_status)
