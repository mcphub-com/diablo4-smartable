import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/SmartableAI/api/diablo4-smartable'

mcp = FastMCP('diablo4-smartable')

@mcp.tool()
def get_topics() -> dict: 
    '''Get Diablo 4 topics.'''
    url = 'https://diablo4-smartable.p.rapidapi.com/topics/'
    headers = {'x-rapidapi-host': 'diablo4-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_newsletters() -> dict: 
    '''Get Diablo 4 newsletters.'''
    url = 'https://diablo4-smartable.p.rapidapi.com/newsletters/'
    headers = {'x-rapidapi-host': 'diablo4-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_sponsorships() -> dict: 
    '''Get Diablo 4 sponsorships.'''
    url = 'https://diablo4-smartable.p.rapidapi.com/sponsorships/today/'
    headers = {'x-rapidapi-host': 'diablo4-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_games(page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get Diablo 4 gameplays.'''
    url = 'https://diablo4-smartable.p.rapidapi.com/games/page/1'
    headers = {'x-rapidapi-host': 'diablo4-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_games_by_topic(topic: Annotated[str, Field(description='')],
                       page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get Diablo 4 gameplays by topic.'''
    url = 'https://diablo4-smartable.p.rapidapi.com/games/druid/page/1/'
    headers = {'x-rapidapi-host': 'diablo4-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'topic': topic,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_communities(page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get Diablo 4 communities'''
    url = 'https://diablo4-smartable.p.rapidapi.com/communities/page/1/'
    headers = {'x-rapidapi-host': 'diablo4-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_people(page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get Diablo 4 influencers and top players.'''
    url = 'https://diablo4-smartable.p.rapidapi.com/people/page/1/'
    headers = {'x-rapidapi-host': 'diablo4-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
