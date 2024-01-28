from datetime import datetime
from typing import List, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


async def investing(
    object: Union[CharityProject, Donation],
    session: AsyncSession
) -> Union[CharityProject, Donation]:
    model = (
        CharityProject if isinstance(object, Donation) else Donation
    )
    not_invested_objects = await get_objects_without_investments(
        model, session
    )

    if not_invested_objects:
        available_amount = object.full_amount
        for element in not_invested_objects:
            need_amount = element.full_amount - element.invested_amount
            investment = (
                need_amount
                if need_amount < available_amount
                else available_amount
            )
            available_amount -= investment
            element.invested_amount += investment
            object.invested_amount += investment

            if element.full_amount == element.invested_amount:
                await close_invested_object(element)

            if not available_amount:
                await close_invested_object(object)
                break
        await session.commit()
    return object


async def close_invested_object(
        object: Union[CharityProject, Donation],
) -> None:
    object.fully_invested = True
    object.close_date = datetime.now()


async def get_objects_without_investments(
    model: Union[CharityProject, Donation], session: AsyncSession
) -> List[Union[CharityProject, Donation]]:
    objects = await session.execute(
        select(model)
        .where(model.fully_invested == False) # noqa
        .order_by(model.create_date)
    )
    return objects.scalars().all()
