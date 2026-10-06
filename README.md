# SRE Service Monitor

A Python CLI for checking HTTP endpoints, TCP ports, and systemd units.
This project is being built as a DevOps/SRE scripting lab.

## Current status

The installable CLI scaffold is complete. Health checks are not implemented yet.

## Run

```bash
uv run sre-service-monitor --help
uv run sre-service-monitor --version
uv run sre-service-monitor
```

The current command logs to stderr and performs no health checks. It does not
change services or system configuration.

## Exit codes

- `0`: command completed
- `2`: invalid command-line arguments

## Development checks

```bash
uv run ruff check .
uv run mypy src
```
