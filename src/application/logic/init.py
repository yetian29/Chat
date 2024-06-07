from src.application.logic.commands.chat import (
    CreateChatCommand,
    CreateChatCommandHandler,
)
from src.application.logic.mediator import Mediator
from src.infrastructure.repositories.chat import BaseChatRespository


def init_mediator(mediator: Mediator, chat_repository: BaseChatRespository):
    mediator.push_command(
        CreateChatCommand, CreateChatCommandHandler(chat_repository=chat_repository)
    )
