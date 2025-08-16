# fedora_installer/config.py
"""
Centralized configuration for the Fedora setup script.
"""

import os
from pathlib import Path

LOG_FILE: Path = Path("fedora_setup.log")
STATE_FILE: Path = Path("/var/tmp/fedora_installer.state")
SUDO_USER: str = os.environ.get("SUDO_USER", os.getlogin())
USER_HOME: Path = Path.home().joinpath("..", SUDO_USER).resolve()
DOTFILES_DIR: Path = USER_HOME / ".hyprdots"
TEMP_BUILD_DIR: Path = Path("/tmp/fedora_installer_builds")

RPMFUSION_FREE_URL = "https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm"
RPMFUSION_NONFREE_URL = "https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm"
