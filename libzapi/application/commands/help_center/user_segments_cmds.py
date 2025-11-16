"""User Segments Commands"""

from dataclasses import dataclass
from typing import Optional, Literal


@dataclass(frozen=True, slots=True)
class BaseUserSegmentCmd:
    name: str
    user_type: Literal["signed_in_users", "staff"]
    tags: Optional[list[str]] = None
    or_tags: Optional[list[str]] = None
    added_user_ids: Optional[list[int]] = None
    groups_ids: Optional[list[int]] = None
    organization_ids: Optional[list[int]] = None

    def __post_init__(self):
        if self.user_type not in ("signed_in_users", "staff"):
            raise ValueError("user_type must be 'signed_in_users' or 'staff'")


@dataclass(frozen=True, slots=True)
class CreateUserSegmentCmd(BaseUserSegmentCmd): ...


@dataclass(frozen=True, slots=True)
class UpdateUserSegmentCmd(BaseUserSegmentCmd): ...
