from typing import Annotated
from fastapi import APIRouter
from fastapi import HTTPException, Query
from app.dependencies import SessionDep
from app import models, schemas

router = APIRouter()


@router.post("/heroes/")
def create_hero(hero: schemas.Hero, session: SessionDep) -> schemas.Hero:
    new_hero = models.Hero(**hero.model_dump())
    session.add(new_hero)
    session.commit()
    session.refresh(new_hero)
    return new_hero


@router.get("/heroes/")
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[schemas.Hero]:
    return session.query(models.Hero).offset(offset).limit(limit).all()



@router.get("/heroes/{hero_id}")
def read_hero(hero_id: int, session: SessionDep) -> schemas.Hero:
    hero = session.query(models.Hero).filter(models.Hero.id == hero_id).first()

    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@router.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    hero = session.query(models.Hero).filter(models.Hero.id == hero_id).first()
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}

