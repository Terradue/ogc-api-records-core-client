# Keycloak OIDC API Client

This is a (work in Progress) collection of client-side APIs to simplify the interaction with Keycloak via Python.

## Installation

```
pip install ogc-api-records-core-client
```

## APIs Usage

### Init

```python
from ogc_api_records_core_client import Client

my_keycloak_base_url = "https://iam.acme.com"

client: Client = Client(base_url=my_keycloak_base_url)
```

### Get the User Code

```python
import webbrowser

from ogc_api_records_core_client.api.default.generate_user_code import sync as generate_user_code
from ogc_api_records_core_client.models.user_code_request import UserCodeRequest
from ogc_api_records_core_client.models.user_code_response import UserCodeResponse

client_id: str = "my-client-id"
default_realm: str = "my-realm"

with Client(base_url=my_keycloak_base_url) as keykoack_client:
    user_code_response: UserCodeResponse | Error | None = generate_user_code(
        realm=default_realm,
        client=keykoack_client,
        body=UserCodeRequest(client_id=client_id, scope="my-scope my-other-scope"),
    )

    if isinstance(user_code_response, UserCodeResponse):
        webbrowser.open(user_code_response.verification_uri_complete)
```

### Obtain a device token

```python
import loguru
import time

from ogc_api_records_core_client.api.default.request_token import sync as request_token
from ogc_api_records_core_client.models.request_token import RequestToken
from ogc_api_records_core_client.models.request_token_response import RequestTokenResponse

request_token_response: RequestTokenResponse | Error | None = None

if not request_token_response and isinstance(user_code_response, UserCodeResponse):
    start_time = time.time()

    with Client(base_url=my_keycloak_base_url) as keykoack_client:
        while time.time() - start_time < user_code_response.expires_in:
            request_token_response = request_token(
                realm=default_realm,
                client=keykoack_client,
                body=RequestToken(
                    client_id=client_id,
                    grant_type="urn:ietf:params:oauth:grant-type:device_code",
                    device_code=user_code_response.device_code,
                ),
            )

            if isinstance(request_token_response, RequestTokenResponse):
                logger.success("Found it!")
                break
            else:
                logger.debug(f"User hasn't confirmed yet, sleeping for {user_code_response.interval} seconds")
                time.sleep(user_code_response.interval)
```

### Access to a protected resource

| :warning: WARNING                                                   |
|:--------------------------------------------------------------------|
| This is a simple use case and it is not covered by this client APIs |

```python
import httpx

my_resource_url = "https://acme.com/my/protected/resource.bak"

http_client: Client = httpx.Client()

response: Response = http_client.get(
    url=resource_url,
    headers={
        "Authorization": f"{request_token_response.token_type} {request_token_response.access_token}"
    },
    follow_redirects=True,
)

with open("resource.bak", "wb") as download_file:
    for chunk in response.iter_bytes(chunk_size=8192):
        download_file.write(chunk)
```
