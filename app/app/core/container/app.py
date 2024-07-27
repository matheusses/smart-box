from uuid import uuid4

from app.core.settings import Settings
from app.infrastructure.db.repositories.box_repository import BoxPostgresRepository
from app.service.create_box import BoxService
from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine


class Container(containers.DeclarativeContainer):
    """In case we need to use a dependency injection, we can follow the example below.

    For more information, see the `Dependency Injector Providers
    <https://python-dependency-injector.ets-labs.org/providers.html>` documentation

    Example:
    -------
        from dependency_injector import containers, providers

        url_repository = providers.Factory(UrlRepository, db=db)

        url_service = providers.Factory(
            UrlService,
            url_repository=url_repository,
            short_code_length=config.get("short_code_length"),
            short_code_retries=config.get("short_code_retries"),
        )

    """
    wiring_config = containers.WiringConfiguration(
        packages=[
            "app.entrypoint.api.v1",
        ]
    )

    config = providers.Configuration()
    settings = Settings()
    config.from_dict(settings.model_dump())

    db = providers.Singleton(
        create_async_engine,
        settings.db,
        isolation_level="AUTOCOMMIT",
        pool_size=config.get("db_max_pool_size"),
        max_overflow=config.get("db_overflow_size"),
    )

    box_repository = providers.Factory(
        BoxPostgresRepository,
        db=db
    )

    box_service = providers.Factory(
        BoxService,
        box_repository=box_repository
    )

