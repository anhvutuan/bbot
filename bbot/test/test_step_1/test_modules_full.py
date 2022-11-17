import shutil
import logging
from omegaconf import OmegaConf

from ..bbot_fixtures import *  # noqa: F401
from ..modules_test_classes import *

log = logging.getLogger(f"bbot.test")


def test_gowitness(bbot_config, bbot_scanner, bbot_httpserver):
    x = Gowitness(bbot_config, bbot_scanner, bbot_httpserver)
    x.run()


def test_otx(bbot_config, bbot_scanner, bbot_httpserver):
    x = Otx(bbot_config, bbot_scanner, bbot_httpserver)
    x.run()


def test_anubisdb(bbot_config, bbot_scanner, bbot_httpserver):
    x = Anubisdb(bbot_config, bbot_scanner, bbot_httpserver)
    x.run()


def test_httpx(bbot_config, bbot_scanner, bbot_httpserver):
    x = Httpx(bbot_config, bbot_scanner, bbot_httpserver)
    x.run()


def test_aspnet_viewstate(bbot_config, bbot_scanner, bbot_httpserver):
    x = Aspnet_viewstate(bbot_config, bbot_scanner, bbot_httpserver)
    x.run()
