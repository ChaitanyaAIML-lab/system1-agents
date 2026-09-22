# coding: utf-8
"""a decision model by slot name, from the environment."""

from __future__ import annotations

from s1a.decision_models.base import DecisionModel
from s1a.decision_models.baselines import RandomModel, Rule, RuleModel
from s1a.decision_models.cua import CuaS1Model
from s1a.decision_models.jev import JevModel
from s1a.decision_models.laya import LayaModel

DECISION_MODEL_SLOTS = (
    "jev",
    "laya",
    "cua",
    "random",
    "rule",
)  # the slots a decision model fills; ``llm`` is not a decision model


def build_model(slot: str, *, seed: int = 0, rule: tuple[str, Rule] | None = None) -> DecisionModel:
    """``jev``, ``laya`` and ``cua`` from the environment, ``random`` from the seed, ``rule`` from the agent's baseline."""
    match slot:
        case "jev":
            return JevModel.from_env()
        case "laya":
            return LayaModel.from_env()  # the laya import happens inside
        case "cua":
            return CuaS1Model.from_env()  # the cua_s1 import happens inside
        case "random":
            return RandomModel(seed)
        case "rule":
            if rule is None:
                raise RuntimeError("this agent has no rule baseline")
            return RuleModel(*rule)
        case _:
            raise ValueError(f"unknown decision-model slot {slot!r}; one of {DECISION_MODEL_SLOTS}")
