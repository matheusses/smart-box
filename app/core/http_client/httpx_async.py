import httpx

__all__ = ["init_async_client"]


async def init_async_client():
    """Initialize the async client to allow re-utilization."""

    client = httpx.AsyncClient()

    yield client

    await client.aclose()
