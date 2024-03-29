from typing import List

from crud import create_offer as create_offer_
from crud import get_offer_by_id as get_offer_by_id_
from crud import get_offers, get_offers_by_user_id, update_offer
from fastapi import Depends
from services.utils import get_db
from sqlalchemy.orm import Session

from database import OfferBase, OfferModel

from .. import app


@app.get('/offers', response_model=List[OfferModel])
def offers_list(show_all: bool = False, user_id: int = None, db: Session = Depends(get_db)):
    if user_id is not None:
        return get_offers_by_user_id(user_id, show_all, db)
    return get_offers(show_all, db)


@app.get('/offers/{id}', response_model=OfferModel)
def get_offer_by_id(id: int, db: Session = Depends(get_db)):
    return get_offer_by_id_(id, db)


@app.post('/offers')
def create_offer(offer: OfferBase, db: Session = Depends(get_db)):
    db_offer = create_offer_(db=db, offer=offer)
    return db_offer


@app.post('/offers/accept/{id}')
def create_offer(id: int, db: Session = Depends(get_db)):
    return update_offer(id, db)
