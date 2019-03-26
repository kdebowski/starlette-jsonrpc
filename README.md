# starlette-jsonrpc

[![Build Status](https://travis-ci.com/kdebowski/starlette-jsonrpc.svg?token=JXg8SCx8Y9Ybz183mTgo&branch=master)](https://travis-ci.com/kdebowski/starlette-jsonrpc)
[![codecov](https://codecov.io/gh/kdebowski/starlette-jsonrpc/branch/master/graph/badge.svg?token=3DkWshhv8x)](https://codecov.io/gh/kdebowski/starlette-jsonrpc)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Examples

Code:
```python
import uvicorn
from starlette.applications import Starlette

from starlette_jsonrpc import dispatcher
from starlette_jsonrpc.endpoint import JSONRPCEndpoint


app = Starlette()


@dispatcher.add_method
async def subtract(params):
    return {"result": params["x"] - params["y"]}


@dispatcher.add_method(name="SubtractMethod")
async def seconds_subtract(params):
    return {"result": params["x"] - params["y"]}
    
    
@dispatcher.add_method
async def subtract_positional(x, y):
    return {"result": x - y}


app.mount("/api", JSONRPCEndpoint)

if __name__ == "__main__":
    uvicorn.run(app)
```

Example of requests:

```json
{
  "jsonrpc": "2.0",
  "method": "subtract",
  "params": {"x": 42, "y": 23},
  "id": "1"
}
```

```json
{
  "jsonrpc": "2.0",
  "method": "SubtractMethod",
  "params": {"x": 42, "y": 23},
  "id": "1"
}
```

```json
{
    "jsonrpc": "2.0",
    "method": "subtract_positional",
    "params": [42, 23],
    "id": "1",
}
```

Example of response:

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": {"result": 19}
}
```

## Contributing

Thank you for your interest in contributing. Everyone is welcome to take part in developting this package. Please fFollow contributing guide in [CONTRIBUTING.md](https://github.com/kdebowski/starlette-jsonrpc/blob/master/CONTRIBUTING.md).

## Support

If you like this project and find it useful and want to say "Thank you", please consider to [buy me a coffee](https://buymeacoff.ee/zRWISPHo0) ;)

## todo:
* add namespaces
* add guide how to install package
* push package to pypi repository
* add type annotations