import logging
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db import base # noqa: F401
from app.channel_data import CHANNEL_DATA
from app.core.config import settings

logger = logging.getLogger(__name__)


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    if settings.FIRST_SUPERUSER:
        user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
        if not user:
            user_in = schemas.UserCreate(email=settings.FIRST_SUPERUSER, full_name="initial admin", is_superuser=True, password=settings.FIRST_SUPERUSER_PASSWORD)
            user = crud.user.create(db, obj_in=user_in) # noqa: F841
        else:
            logger.warning(f"User {settings.FIRST_SUPERUSER} already exists")
        
        if not user.channels:
            pass
            # for channel in CHANNEL_DATA:
            #     channel_in = schemas.ChannelCreate(
            #         id = channel["id"],
            #         submitter_id = user.id,
            #     )
            #     crud.channel.create(db, obj_in=channel_in)
    else:
        logger.warning(f"User {settings.FIRST_SUPERUSER} does not exist")