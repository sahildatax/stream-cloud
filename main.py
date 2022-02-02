import api
import os
from aiohttp import web
import aiohttp_jinja2
import jinja2

server = api.Client()
hostx = os.getcwd()

@aiohttp_jinja2.template('stream.html')
def streamx(request):
    id1 = request.match_info.get("id1", "")
    id2 = request.match_info.get("id2", "")
    id3 = request.match_info.get("id3", "")
    id4 = request.match_info.get("id4", "")
    id5 = request.match_info.get("id5", "")
    id6 = request.match_info.get("id6", "")
    link = f'https://{id1}/{id2}/{id3}/{id4}/{id5}/{id6}'
    if link.endswith("////"):
      link = link[:-4]
    if link.endswith("//"):
      link = link[:-2]
    if link.endswith("/"):
      link = link[:-1]
    if link.endswith("///"):
      link = link[:-3]
    if link.endswith("/////"):
      link = link[:-5]
    return {'linkx' : link}

async def main():
    app = web.Application()
    aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(hostx + '/views'))
    app.add_routes(
        [
            web.get('/', server.hello),
            web.get('/favicon.ico', server.hello),
            web.get('/{id}', server.Downloader),
            web.get('/{id}/{name}', server.Downloader),web.get('/stream/{id1}', streamx),
            web.get('/stream/{id1}/{id2}', streamx),
            web.get('/stream/{id1}/{id2}/{id3}', streamx),
            web.get('/stream/{id1}/{id2}/{id3}/{id4}', streamx),
            web.get('/stream/{id1}/{id2}/{id3}/{id4}/{id5}', streamx),
            web.get('/stream/{id1}/{id2}/{id3}/{id4}/{id5}/{id6}', streamx)
        ]
    )
    return app

if __name__ == "__main__":
    web.run_app(main())
