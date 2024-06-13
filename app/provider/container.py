from lagom import Container, Singleton
from ..clients.openai import OpenAIModule
from ..clients.playwright import PlaywrightModule


app_container = Container()

app_container[OpenAIModule] = Singleton(OpenAIModule)

app_container[PlaywrightModule] = Singleton(PlaywrightModule)
