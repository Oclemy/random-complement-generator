import random
from sanic import Sanic
from sanic.response import json

app = Sanic("RandomComplimentGenerator")

compliments = [
    "You are absolutely wonderful!",
    "Your smile brightens everyone's day.",
    "You have an amazing sense of humor.",
    "You are incredibly kind and thoughtful.",
    "You make the world a better place just by being in it.",
    "You are stronger than you think.",
    "Your creativity knows no bounds.",
    "You have a heart of gold.",
    "You inspire everyone around you.",
    "You are one of a kind!",
    "You bring out the best in others.",
    "Your positivity is contagious.",
    "You have an incredible work ethic.",
    "You are a joy to be around.",
    "The world is lucky to have you in it.",
]


@app.get("/")
async def index(request):
    return json({
        "message": "Welcome to the Random Compliment Generator!",
        "hint": "Visit /compliment to receive a compliment."
    })


@app.get("/compliment")
async def get_compliment(request):
    compliment = random.choice(compliments)
    return json({"compliment": compliment})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
