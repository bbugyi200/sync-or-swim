"""Contains this project's clack runners."""

from __future__ import annotations

from typing import List, Optional

from clack.types import ClackRunner
from eris import ErisError, ErisResult, Err, Ok
from fabric import Connection
from logrus import Logger
import metaman

from . import APP_NAME
from .config import Config, PullConfig, PushConfig
from .types import Host


RUNNERS: List[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)

logger = Logger(__name__)


@runner
def run_pull(cfg: PullConfig) -> int:
    """Runner for the 'pull' subcommand."""
    if not (host := _logging_host_from_config(cfg)):
        return 1

    c = _connection_from_host(host)
    for target in cfg.targets:
        local = target.paths["local"]
        for host_name, remote in target.paths.items():
            if host_name == cfg.remote_target_name:
                logger.info(
                    "Fetching file from remote host.",
                    host=host,
                    name=target.name,
                    local=local,
                    remote=remote,
                )
                c.get(remote, local=local)
                break
        else:
            logger.info(
                "Skipping target since it is not configured for this host.",
                host=host,
                local_path=local,
            )
    return 0


@runner
def run_push(cfg: PushConfig) -> int:
    """Runner for the 'push' subcommand."""
    if not (host := _logging_host_from_config(cfg)):
        return 1
    return 0


def _connection_from_host(host: Host) -> Connection:
    c = Connection(host.address, user=host.user, port=host.port)
    return c


def _logging_host_from_config(cfg: Config) -> Optional[Host]:
    host_result = _host_from_config(cfg)
    if isinstance(host_result, Err):
        e = host_result.err()
        logger.error(
            "An error occurred while attempting to fetch the desired host from"
            " configureation.",
            error=e.to_json(),
            all_hosts=cfg.hosts,
            target_name=cfg.remote_target_name,
        )
        return None
    host = host_result.ok()
    return host


def _host_from_config(cfg: Config) -> ErisResult[Host]:
    host_container = [h for h in cfg.hosts if h.name == cfg.remote_target_name]
    if not host_container:
        error = ErisError(
            "Given target name was not found in 'hosts' values of"
            f" {APP_NAME}/config.yml."
        )
        return Err(error)

    host = host_container[0]
    return Ok(host)
