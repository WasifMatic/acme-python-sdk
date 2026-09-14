<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Swagger Petstore - OpenAPI 3.0 (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Swagger Petstore - OpenAPI 3.0 |
| Root package | `swagger_petstore_open_api_3_0` |
| Distribution name | `cliV1` |
| Requires | Python 3.10 or later |
| API spec version | `1.0.26` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from swagger_petstore_open_api_3_0 import SwaggerPetstoreOpenApi30Client

client = SwaggerPetstoreOpenApi30Client(petstore_auth="YOUR_API_KEY", api_key="YOUR_API_KEY")

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with SwaggerPetstoreOpenApi30Client(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run

from swagger_petstore_open_api_3_0 import AsyncSwaggerPetstoreOpenApi30Client


async def main() -> None:
    client = AsyncSwaggerPetstoreOpenApi30Client(petstore_auth="YOUR_API_KEY", api_key="YOUR_API_KEY")
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncSwaggerPetstoreOpenApi30Client(...) as client:` closes the pool on exit.

`AsyncClient` (`swagger_petstore_open_api_3_0/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `SwaggerPetstoreOpenApi30Client` and `AsyncSwaggerPetstoreOpenApi30Client` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.pet_api`). Every constructor argument is optional and keyword-only. Sources: `swagger_petstore_open_api_3_0/client.py`, `swagger_petstore_open_api_3_0/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `server_config` | `ServerConfigOrDict \| None` | `ServerConfigOrDict \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `petstore_auth` | `str \| None` | `str \| None` | `None` |
| `api_key` | `str \| None` | `str \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `ServerConfigOrDict` | `swagger_petstore_open_api_3_0.server` | keys as the Servers & auth tables read |
| `HttpClient` | `swagger_petstore_open_api_3_0.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()` |
| `AsyncHttpClient` | `swagger_petstore_open_api_3_0.core` | protocol — `async send(request: HttpRequest) -> HttpResponse` · `async aclose()` |

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.response`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `swagger_petstore_open_api_3_0/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`swagger_petstore_open_api_3_0/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse`.

Core runtime types (`swagger_petstore_open_api_3_0/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `swagger_petstore_open_api_3_0/errors/` or `RawError` | `error: E` · `status_code: int` · `response: HttpResponse` | `swagger_petstore_open_api_3_0/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `response: HttpResponse` (on both) | `swagger_petstore_open_api_3_0/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse` | `swagger_petstore_open_api_3_0/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
from swagger_petstore_open_api_3_0.core import ApiError, RawError

try:
    response = client.pet_api.add_pet(name, photo_urls)
except ApiError as e:
    # Case A — typed error: e.error is AddPetErrorBody
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **19 operations**, **15 are Case A (typed)** and **4 are Case B (raw)**.

---

## Operations — by controller (3 pages, 19 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every *generated* type it names, with the module that declares it. A runtime type — a file alias, a date/time or byte converter — is not listed there.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout or extra headers; every signature ends with it | here (`swagger_petstore_open_api_3_0/core/request_options.py`) |
| **Each operation names its own server** — this SDK declares several, so every block carries a **Server** bullet with the server's key in `server_config=` | its block |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.pet_api` | 8 | [map/operations/pet_api.md](map/operations/pet_api.md) |
| `client.store` | 4 | [map/operations/store.md](map/operations/store.md) |
| `client.user_api` | 7 | [map/operations/user_api.md](map/operations/user_api.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `swagger_petstore_open_api_3_0/models/` declares one type plus its input companion, and every module under `swagger_petstore_open_api_3_0/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`ApiResponse` ↔ `api_response.py`; an error alias drops its `Body` suffix: `AddPetErrorBody` ↔ `add_pet_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 6 | `swagger_petstore_open_api_3_0/models/` |
| Enums (`Enum` over `str`) — Python member names + wire values | 2 | `swagger_petstore_open_api_3_0/models/enums/` |
| Error aliases (one per Case A operation) | 15 | `swagger_petstore_open_api_3_0/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`type_` ↔ `"type"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model and enum also has an **input companion**, exported beside it from the same package (`ApiResponse` ↔ `ApiResponseDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`OrderStatus` ↔ `OrderStatusOrStr`) and additionally accepts a wire value this SDK version does not know.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `swagger_petstore_open_api_3_0` |
| Operation controllers | `swagger_petstore_open_api_3_0.apis` |
| Models | `swagger_petstore_open_api_3_0.models` |
| Enums | `swagger_petstore_open_api_3_0.models.enums` |
| Error aliases | `swagger_petstore_open_api_3_0.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `swagger_petstore_open_api_3_0.core` |

---

## Servers & auth

**API key (header `Authorization`).** Pass `petstore_auth="<api_key>"`; sent as the `Authorization` request header.

**API key (header `api_key`).** Pass `api_key="<api_key>"`; sent as the `api_key` request header.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**One environment.** The spec declares a single environment, so no `environment` keyword exists and there is nothing to select.

**2 servers.** Base-URL templates and override points (`swagger_petstore_open_api_3_0/server/server_config.py`):

| Server | Base URL | Override point |
| --- | --- | --- |
| `default` | `https://petstore3.swagger.io/api/v3` | `{"default": {"base_url": …}}` |
| `auth_server` | `https://petstore3.swagger.io/oauth` | `{"auth_server": {"base_url": …}}` |

Override any of these by passing `server_config=` a dict nested exactly as the columns above read — `{"default": {"base_url": …}}` — with each row's variables sitting beside its `base_url`.

