from datetime import datetime
from typing import List, TypeVar

from app.models import CharityProject, Donation

TargetType = TypeVar("TargetType", CharityProject, Donation)
SourceType = TypeVar("SourceType", CharityProject, Donation)


def investing(
    target: TargetType, sources: List[SourceType]
) -> List[SourceType]:
    updated_sources = []
    for source in sources:
        source_to_close = source.full_amount - source.invested_amount
        target_to_close = target.full_amount - target.invested_amount
        distributable_amount = min(source_to_close, target_to_close)
        source.invested_amount += distributable_amount
        target.invested_amount += distributable_amount
        if source.invested_amount == source.full_amount:
            source.fully_invested = True
            source.close_date = datetime.now()
        updated_sources.append(source)

    if target.invested_amount == target.full_amount:
        target.fully_invested = True

    return updated_sources
