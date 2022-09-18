"""Contains this project's clack.Config classes."""

from __future__ import annotations

from typing import Any, Final, List, Literal, Sequence

import clack

from .types import Host, Target


Command = Literal["pull", "push"]


class Config(clack.Config):
    """Shared clack configuration class."""

    command: Command

    # ----- ARGUMENTS
    remote_target_name: str

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

    pull_parser = new_command("pull", help="Pull files from another machine.")
    push_parser = new_command("push", help="Push files to another machine.")
    for config_class, subparser in [
        (PullConfig, pull_parser),
        (PushConfig, push_parser),
    ]:
        push_or_pull: Final = "pull" if config_class is PullConfig else "push"
        to_or_from: Final = "from" if config_class is PullConfig else "to"
        subparser.add_argument(
            "remote_target_name",
            help=(
                "The name of the remote machine (which MUST be configured in"
                f" sync_or_swim/config.yml) that we will {push_or_pull} files"
                f" {to_or_from}."
            ),
        )

    args = parser.parse_args(argv[1:])
    kwargs = clack.filter_cli_args(args)

    return kwargs
