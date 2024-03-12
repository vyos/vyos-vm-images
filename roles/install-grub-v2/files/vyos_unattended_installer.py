#!/usr/bin/env python3
#
# Copyright (C) 2023 VyOS maintainers and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from importlib import util
from os import environ
from sys import exit

spec = util.spec_from_file_location(
    "vinstall", "/usr/libexec/vyos/op_mode/image_installer.py"
)
vinstall = util.module_from_spec(spec)
spec.loader.exec_module(vinstall)

if __name__ == "__main__":
    # read configuration variables
    vyos_version = environ["vyos_version"]
    console_type = "tty" if environ["console_type"] == "kvm" else "ttyS"
    install_target = environ["install_target"]

    # install GRUB configuration files
    vinstall.setup_grub("/boot")
    vinstall.grub.version_add(vyos_version, "/boot")
    vinstall.grub.set_default(vyos_version, "/boot")
    vinstall.grub.set_console_type(console_type, "/boot")

    # install GRUB
    vinstall.grub.install(install_target, "/boot/boot", "/boot/efi")

    # sort inodes (to make GRUB read config files in alphabetical order)
    vinstall.grub.sort_inodes(f"/boot/{vinstall.grub.GRUB_DIR_VYOS}")
    vinstall.grub.sort_inodes(f"/boot/{vinstall.grub.GRUB_DIR_VYOS_VERS}")

    exit()
