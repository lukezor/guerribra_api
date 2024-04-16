import uvicorn
from fastapi import FastAPI, BackgroundTasks
from functions import get_players_guerribro, get_all_players_with_guilds, update_online_time

app = FastAPI(title='Tibia - Guerribra')

@app.get('/')
def index():
    return update_online_time()

@app.get('/guerribro')
def index():
    return get_players_guerribro()

@app.get('/with_guilds')
def index():
    return get_all_players_with_guilds()

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)