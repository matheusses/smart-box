"""Create Box

Revision ID: 66f23c16a002
Revises: 
Create Date: 2024-07-05 01:19:11.005521

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66f23c16a002'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
            -- Create Address table
            CREATE TABLE address (
                id SERIAL PRIMARY KEY,
                street VARCHAR(255) NOT NULL,
                city VARCHAR(100) NOT NULL,
                state VARCHAR(100) NOT NULL,
                zip_code VARCHAR(20) NOT NULL
            );

            -- Create Box table
            CREATE TABLE box (
                id SERIAL PRIMARY KEY,
                external_id BIGINT UNIQUE NOT NULL,
                name VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                address_id INTEGER REFERENCES address(id)
            );
        """

    )


def downgrade() -> None:
    op.execute(
        """
            -- Drop Box table
            DROP TABLE IF EXISTS box;

            -- Drop Address table
            DROP TABLE IF EXISTS address;

        """
    )
