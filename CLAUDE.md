# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastMCP (Model Context Protocol) server project built with Python:
- `main.py`: FastMCP server with tools for hello, add_numbers, and get_info
- `test_client.py`: Test client for the MCP server
- `pyproject.toml`: UV project configuration
- PyCharm IDE configuration present in `.idea/` directory

## Development Environment

- **Python Version**: 3.13.5 (managed by uv)
- **Package Manager**: uv
- **Main Framework**: FastMCP 2.12.0
- **MCP SDK**: 1.13.1
- **IDE**: PyCharm (configuration files present in `.idea/`)

## Running the MCP Server

To run the FastMCP server:
```bash
uv run python main.py
```

To see server info and help:
```bash
uv run python main.py --help
```

To test the server with the test client:
```bash
uv run python test_client.py
```

## Available Tools

The MCP server provides these tools:
- `hello(name: str)`: Say hello to someone
- `add_numbers(a: int, b: int)`: Add two numbers together  
- `get_info()`: Get information about this MCP server

## Project Structure

This is a FastMCP server project with:
- MCP server implementation in `main.py`
- Test client in `test_client.py`
- UV-managed dependencies and virtual environment
- Standard PyCharm project structure

## Development Commands

- `uv add <package>`: Add a new dependency
- `uv run <command>`: Run commands in the virtual environment
- `uv sync`: Sync dependencies from lock file