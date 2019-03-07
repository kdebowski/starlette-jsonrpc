import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse

from starlette_jsonrpc import dispatcher
from starlette_jsonrpc.endpoint import JSONRPCEndpoint

app = Starlette()


@app.route('/')
def index(request):
    return JSONResponse({'hello': 'world'})


@dispatcher.add_method
def substract(request):
    return {'test': 'method'}


app.mount('/api', JSONRPCEndpoint)


if __name__ == '__main__':
    uvicorn.run(app)
