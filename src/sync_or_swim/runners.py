"""Contains this project's clack runners."""

from __future__ import annotations

from typing import List

from clack.types import ClackRunner
from logrus import Logger
import metaman

from clack.types import ClackRunner

from .config import PullConfig, PushConfig


RUNNERS: List[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)

logger = Logger(__name__)


@runner
def run_pull(cfg: PullConfig) -> int:
    """Runner for the 'pull' subcommand."""
    del cfg
    return 0


@runner
def run_push(cfg: PushConfig) -> int:
    """Runner for the 'push' subcommand."""
    del cfg
    return 0
