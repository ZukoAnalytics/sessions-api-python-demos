# Zuko Sessions API Demos

A series of demo scripts, showing how to consume the [Zuko Sessions API][api-docs], using Python.

## Setup

You will need the following:

### API key

You will need an _API key_ from the Zuko app to be able to run these scripts. This authenticates you with our API and allows us to authorise your access to a given form.

If you don't have an API key, please reach out to your account manager, who will be able to get one setup for you.

Note: This is different to the [_form UUID_](#form-uuid).

Store this as an environment variable:

```bash
export ZUKO_API_KEY=abc123abc123
```

### Form UUID

You will also need to know the _form UUID_ for a form which you are currently tracking in Zuko.

Note: This is different to the [_API key_](#api-key).

### Python

These scripts assume:

* Python 3 is installed.
* The `requests` library is installed.

## Demos

### Fetching sessions

This demo script will retrieve all of the sessions for a given form, for a given time range and return a message informing you of how many sessions were retrieved.

Note: Remember to replace the example form UUID with your form UUID.

```bash
./fetch_sessions_demo.py --form-uuid 4ef0392b-dd54-42b6-ba68-4ec10f74e3de --start-time 2023-03-01T00:00:00Z --end-time 2023-04-01T00:00:00Z
```

### Fetching total view, starter, completion and abandonment (VSCA) counts

This demo script will retrieve all of the sessions for a given form, for a given time range and return a message informing you of how views, starters, completions and abandons there were for a given form and time range.

This recreates the top-level stats that are shown in the Zuko application for your form.

```bash
./fetch_vsca_demo.py --form-uuid 4ef0392b-dd54-42b6-ba68-4ec10f74e3de --start-time 2023-03-01T00:00:00Z --end-time 2023-04-01T00:00:00Z
```

### Handling rate limiting

This demo script shows how you can handle rate limiting when retrieving sessions from the API.

```bash
./handle_rate_limit_demo.py --form-uuid 4ef0392b-dd54-42b6-ba68-4ec10f74e3de --start-time 2023-03-01T00:00:00Z --end-time 2023-04-01T00:00:00Z
```

[api-docs]: https://docs.zuko.io/knowledge-base/sessions-api
