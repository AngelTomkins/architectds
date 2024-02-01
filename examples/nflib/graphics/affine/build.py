#!/usr/bin/env python3

# SPDX-License-Identifier: CC0-1.0
#
# SPDX-FileContributor: Antonio Niño Díaz, 2024

from architectds import *

nitrofs = NitroFS()
nitrofs.add_nflib_bg_affine(['assets/bgaffine'], 'bg')
nitrofs.add_nflib_bg_affine_shared_pal('assets/bgaffine_shared_pal_1', 'bg')
nitrofs.generate_image()

arm9 = Arm9Binary(
    sourcedirs=['source'],
    libs=['nds9', 'nflib'],
    libdirs=['${BLOCKSDS}/libs/libnds', '${BLOCKSDSEXT}/nflib']
)
arm9.generate_elf()

nds = NdsRom(
    binaries=[arm9, nitrofs],
    game_title='NFlib: Affine BGs',
)
nds.generate_nds()

nds.run_command_line_arguments()
