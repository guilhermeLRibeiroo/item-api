from alembic import command

from src.database.migrations.config import alembic_cfg


def revision():
    message = input("Revision Name:")
    command.revision(alembic_cfg, autogenerate=True, message=message)


def upgrade():
    print("Start Migration")
    command.upgrade(alembic_cfg, "head")
    print("End Migration")
