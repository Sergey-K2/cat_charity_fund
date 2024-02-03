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
    updated_sources = []
    for source in sources:
        if target.fully_invested:
            break
        donation = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )
        for object in (target, source):
            object.invested_amount += donation
            if object.full_amount == object.invested_amount:
                object.fully_invested = 1
                object.close_date = datetime.utcnow()
        updated_sources.append(source)
    return updated_sources
