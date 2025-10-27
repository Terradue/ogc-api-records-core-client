"""A client library for accessing OGC API - Records - Part 1: Core"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
