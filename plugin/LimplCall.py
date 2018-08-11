#! /usr/bin/env python3

# Copyright (c) 2018, Dennis Hedback
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     1. Redistributions of source code must retain the above copyright
#        notice, this list of conditions and the following disclaimer.
#
#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in
#        the documentation and/or other materials provided with the
#        distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import vim
import os
import tempfile
import sys

USE_SYSTEM_MODULE = bool(int(vim.eval("g:__lets_implement_use_system_module")))
SCRIPT_DIR = vim.eval("s:dir")

if not USE_SYSTEM_MODULE:
    sys.path.insert(0, SCRIPT_DIR)

from lets_implement import implement


def main():
    error = False
    hpp_file = vim.eval("expand ('%:p')")
    cpp_file = ".".join(hpp_file.split(".")[:-1]) + ".cpp"
    try:
        implement(hpp_file, cpp_file)
    except RuntimeError as err:
        error = True
    else:
        vim.eval("LimplSmartOpen('" + cpp_file + "')")
        vim.command("edit!")
    finally:
        vim.command("redraw!")
        if error:
            # TODO: Would be nice to display Clang output here to indicate
            # where the problem is.
            print("LetsImplement: Parsing failed; "
                  "check your source for errors and try again.", file=sys.stderr)


if __name__ == "__main__":
    main()
