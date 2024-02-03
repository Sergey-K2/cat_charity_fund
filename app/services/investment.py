from datetime import datetime
from typing import List, TypeVar

from app.models import CharityProject, Donation

TargetType = TypeVar("TargetType", CharityProject, Donation)
SourceType = TypeVar("SourceType", CharityProject, Donation)


def investing(
    target: TargetType, sources: List[SourceType]
) -> List[SourceType]:
    target.invested_amount = (
        0 if target.invested_amount is None else target.invested_amount
    )
    new_sources = []
    for source in sources:
        if target.fully_invested:
            break
        donation = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )
        for obj in (target, source):
            obj.invested_amount += donation
            if obj.full_amount == obj.invested_amount:
                obj.fully_invested = 1
                obj.close_date = datetime.utcnow()
        new_sources.append(source)
    return new_sources