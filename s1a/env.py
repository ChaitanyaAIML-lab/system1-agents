# coding: utf-8
"""The environment surface every tool-front agent adapts: reset, observe, enumerate candidates, step, done, score."""

from __future__ import annotations

from typing import Any, Protocol


class Env(Protocol):
    async def reset(self) -> None: ...
    async def observe(self) -> dict[str, Any]: ...  # a ``progress`` key, when present, is what the stall check compares
    async def candidates(self) -> dict[str, str]: ...  # key to one-line description; empty once the episode is done
    async def step(self, key: str) -> None: ...
    @property
    def done(self) -> bool: ...
    @property
    def score(self) -> float: ...
