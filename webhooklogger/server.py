from dataclasses import dataclass
from random import randint
from typing import Callable
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.routing import APIRoute

app = FastAPI()


class CustomRouteHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            req = await request.body()
            print("Request: " + req.decode())
            headers = request.headers
            print("Headers: " + str(headers))
            response: Response = await original_route_handler(request)
            print("Response: " + response.body.decode())
            return response

        return custom_route_handler


app.router.route_class = CustomRouteHandler


@dataclass
class Address:
    street: str
    city: str
    postcode: str
    number: str
    country: str

@dataclass
class WebhookPayload:
    amount: int
    item: str
    address: Address


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/webhook")
def read_root(payload: WebhookPayload):
    x = randint(0, 10)
    if 0 < x < 3:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    elif 3 <= x < 5:
        raise HTTPException(status_code=422, detail="Validation Error")

    return payload
