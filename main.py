import uvicorn
from fastapi import FastAPI, BackgroundTasks
from functions import get_players_guerribro, get_all_players_with_guilds, get_all_players

app = FastAPI(title='Tibia - Guerribra')

@app.get('/')
def index():
    return get_all_players()

@app.get('/guerribro')
def index():
    return get_players_guerribro()

@app.get('/with_guilds')
def index():
    return get_all_players_with_guilds()

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)