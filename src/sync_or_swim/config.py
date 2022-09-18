"""Contains this project's clack.Config classes."""

from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Sequence

import clack
from pydantic import BaseModel


Command = Literal["pull", "push"]


class Host(BaseModel):
    """Represents an element of the 'hosts' config file field."""

    name: str
    address: str
    port: Optional[int] = None
    user: Optional[str] = None


class Target(BaseModel):
    """Represents an element of the 'targets' config file field."""

    name: str
    paths: Dict[str, str]


class Config(clack.Config):
    """Shared clack configuration class."""

    command: Command

    # ----- CONFIG
    hosts: List[Host]
    targets: List[Target] 


class PullConfig(Config):
    """Config for the 'pull' subcommand."""

    command: Literal["pull"]


class PushConfig(Config):
    """Config for the 'push' subcommand."""

    command: Literal["push"]


def clack_parser(argv: Sequence[str]) -> dict[str, Any]:
    """Parser we pass to the `main_factory()` `parser` kwarg."""
    parser = clack.Parser(
        description="Sync data files across all of your machines."
    )
    new_command = clack.new_command_factory(parser)

    new_command("pull", help="Pull files from another machine.")
    new_command("push", help="Push files to another machine.")

    args = parser.parse_args(argv[1:])
    kwargs = clack.filter_cli_args(args)

    return kwargs
