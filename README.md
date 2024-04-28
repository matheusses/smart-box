https://github.com/Iazzetta/hexagonal-fastapi-sentry-sqlalchemy
https://chat.openai.com/share/170ec1c9-8b9a-4ca1-aa78-0fc99184a8ce

hexagonal_project/
│
├── app/                                   # Application root
│   ├── domain/                            # Core business logic
│   │   ├── __init__.py                    # Makes domain a Python package
│   │   ├── models.py                      # Domain models (business entities)
│   │   └── services.py                    # Domain services (business logic)
│   │
│   ├── use_cases/                         # Application use cases
│   │   ├── __init__.py                    # Makes use_cases a Python package
│   │   ├── create_user_use_case.py        # Use case for creating a user
│   │   └── delete_user_use_case.py        # Use case for deleting a user
│   │
│   ├── ports/                             # Ports (interfaces for the domain to interact with adapters)
│   │   ├── __init__.py                    # Makes ports a Python package
│   │   ├── repository_port.py             # Abstract repository interface
│   │   └── api_port.py                    # Abstract API interface
│   │
│   ├── adapters/                          # Adapters implement interfaces defined by ports
│   │   ├── __init__.py                    # Makes adapters a Python package
│   │   ├── orm_adapter.py                 # Adapter for ORM (implements repository_port)
│   │   ├── api_adapter.py                 # Adapter for external API (implements api_port)
│   │   └── cli_adapter.py                 # CLI adapter for command line interfacing
│   │
│   ├── entrypoints/                       # Application entry points (another form of adapter)
│   │   ├── __init__.py                    # Makes entrypoints a Python package
│   │   ├── api/                           # REST API as an entrypoint
│   │   │   ├── __init__.py
│   │   │   ├── main.py                    # FastAPI entry point
│   │   │   └── routers/                   # API routers
│   │   │       ├── __init__.py
│   │   │       ├── user_router.py
│   │   │       └── post_router.py
│   │   └── cli/                           # CLI as an entrypoint
│   │       ├── __init__.py
│   │       └── manage.py                  # Command line management tools
│   │
│   ├── infrastructure/                    # Infrastructure implementations (specific adapters)
│   │   ├── __init__.py                    # Makes infrastructure a Python package
│   │   ├── database/                      # Database interactions
│   │   │   ├── __init__.py
│   │   │   ├── models.py                  # ORM models
│   │   │   └── repository.py              # Repository implementations (adapts to repository_port)
│   │   ├── queue/                         # Queue system interactions
│   │   │   ├── __init__.py
│   │   │   └── message_broker.py          # Message broker configurations (could be an adapter)
│   │   └── cache/                         # Cache system
│   │       ├── __init__.py
│   │       └── redis_adapter.py           # Redis adapter
│   │
├── tests/                                 # Test suite
│   ├── domain/
│   ├── use_cases/
│   ├── entrypoints/
│   ├── infrastructure/
│   └── conftest.py                        # Pytest fixtures and test configurations
│
├── logs/                                  # Log directory
│   ├── app.log
│   └── error.log
│
├── README.md                              # Project overview and setup instructions
├── requirements.txt                       # Python dependencies
└── .gitignore                             # Specifies intentionally untracked files to ignore
