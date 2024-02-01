#!/usr/bin/env python3

# SPDX-License-Identifier: CC0-1.0
#
# SPDX-FileContributor: Antonio Niño Díaz, 2024

from architectds import *

arm9 = Arm9Binary(
    sourcedirs=['source'],
    libs=['NE', 'nds9'],
    libdirs=['${BLOCKSDS}/libs/libnds', '${BLOCKSDSEXT}/nitro-engine']
)
arm9.add_grit(['assets/robot'])
arm9.add_nitro_engine_md5(['assets/robot'])
arm9.generate_elf()

nds = NdsRom(
    binaries=[arm9],
    game_title='NE: Animated model',
)
nds.generate_nds()

nds.run_command_line_arguments()
