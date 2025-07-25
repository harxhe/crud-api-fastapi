from models import Item
from sqlalchemy.orm import Session
from schemas import ItemCreate

def create_item(db:Session,item:ItemCreate):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item 

def get_items(db: Session):
    return db.query(Item).all()

def get_item(db: Session,item_id:int):
    return db.query(Item).filter(Item.id==item_id).first()

def update_item(db: Session, item_id: int, updated_data: ItemCreate):

    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        item.name = updated_data.name
        item.description = updated_data.description
        db.commit()
        db.refresh(item)
    return item


def delete_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item
