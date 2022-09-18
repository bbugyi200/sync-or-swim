"""Custom types used by greatday."""

from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel


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
