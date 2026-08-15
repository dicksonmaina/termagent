import importlib

import pytest

from termagent.cli import build_parser


def test_imports():
    cli = importlib.import_module("termagent.cli")
    assert hasattr(cli, "build_parser")
    assert hasattr(cli, "main")


def test_parser_defaults():
    p = build_parser()
    args = p.parse_args([])
    assert args.prompt == []
    assert args.model is None
    assert args.base_url is None
    assert args.api_key is None
    assert args.auto_approve is False
    assert args.config is False
    assert args.max_turns is None
    assert args.session is None


def test_parser_prompt():
    p = build_parser()
    args = p.parse_args(["hello", "world"])
    assert args.prompt == ["hello", "world"]


def test_parser_model_flag():
    p = build_parser()
    args = p.parse_args(["-m", "gpt-4"])
    assert args.model == "gpt-4"


def test_parser_base_url_flag():
    p = build_parser()
    args = p.parse_args(["-b", "https://example.com"])
    assert args.base_url == "https://example.com"


def test_parser_api_key_flag():
    p = build_parser()
    args = p.parse_args(["-k", "secret"])
    assert args.api_key == "secret"


def test_parser_auto_approve_flag():
    p = build_parser()
    args = p.parse_args(["-a"])
    assert args.auto_approve is True


def test_parser_config_flag():
    p = build_parser()
    args = p.parse_args(["--config"])
    assert args.config is True


def test_parser_max_turns():
    p = build_parser()
    args = p.parse_args(["--max-turns", "10"])
    assert args.max_turns == 10
