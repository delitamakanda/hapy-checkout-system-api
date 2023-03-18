import logging
from sqlalchemy.orm import Session
from app.db.session import engine
from app import crud, schemas
from app.db import base # noqa: F401
from app.channel_data import CHANNEL_DATA
from app.db.base_class import Base

logger = logging.getLogger(__name__)

FIRT_SUPERUSER = "admin@hapyapi.com"

def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(bind=engine)
    if FIRT_SUPERUSER:
        user = crud.user.get_by_email(db, email=FIRT_SUPERUSER)
        if not user:
            user_in = schemas.UserCreate(email=FIRT_SUPERUSER, full_name="admin", is_superuser=True)
            user = crud.user.create(db, obj_in=user_in) # noqa: F841
        else:
            logger.warning(f"User {FIRT_SUPERUSER} already exists")
        
        if not user.channels:
            pass
            # for channel in CHANNEL_DATA:
            #     channel_in = schemas.ChannelCreate(
            #         id = channel["id"],
            #         submitter_id = user.id,
            #     )
            #     crud.channel.create(db, obj_in=channel_in)
    else:
        logger.warning(f"User {FIRT_SUPERUSER} does not exist")