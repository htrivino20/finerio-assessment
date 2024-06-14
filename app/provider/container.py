from lagom import Container, Singleton
from app.clients.openai import OpenAIModule
from app.clients.playwright import PlaywrightModule
from app.shared.utils import Utils

app_container = Container()

app_container[OpenAIModule] = Singleton(OpenAIModule)
app_container[PlaywrightModule] = Singleton(PlaywrightModule)
app_container[Utils] = Singleton(Utils)
