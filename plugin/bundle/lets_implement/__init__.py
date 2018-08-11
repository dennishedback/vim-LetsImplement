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

import os
import sys
import re
import pygccxml

__VERSION__ = (0, 1, 1)


def make_config():
    generator_path, generator_name = pygccxml.utils.find_xml_generator()
    return pygccxml.parser.xml_generator_configuration_t(
        xml_generator_path=generator_path,
        xml_generator=generator_name
    )


def parse(file_, xml_generator_config):
    decls = pygccxml.parser.parse(
        [file_], xml_generator_config)
    return pygccxml.declarations.get_global_namespace(decls)


def is_implementable(decl):
    from pygccxml.declarations import member_function_t, constructor_t, \
        destructor_t, free_function_t, member_operator_t, free_operator_t
    return ((((isinstance(decl, member_function_t)
               or isinstance(decl, constructor_t)
               or isinstance(decl, destructor_t)
               or isinstance(decl, member_operator_t))
              and not decl.virtuality == "pure virtual")
             or (isinstance(decl, free_operator_t)
                 or isinstance(decl, free_function_t)))
            and not decl.is_artificial)


def find_declarations(namespace, file_=None):
    criteria = pygccxml.declarations.declaration_matcher(
        header_file=file_)
    return pygccxml.declarations.matcher.find(criteria, namespace)


def create_cpp(cpp_file, hpp_file):
    hpp_path = hpp_file.split(os.sep)
    cpp_path = cpp_file.split(os.sep)
    hpp_rel_dir = os.path.relpath(os.sep.join(
        hpp_path[:-1]), os.sep.join(cpp_path[:-1]))
    hpp_rel_name = ""
    if hpp_rel_dir == ".":
        hpp_rel_name = hpp_path[-1]
    else:
        hpp_rel_name = hpp_rel_dir + os.sep + hpp_path[-1]
    with open(cpp_file, "w") as f:
        f.write("#include \"" + hpp_rel_name + "\"\n")
        f.write("\n")


def declstr(decl):
    return "".join(str(decl).split("[")[:-1]).strip()


def implement(hpp_file, cpp_file):
    hpp_file = os.path.abspath(hpp_file)
    cpp_file = os.path.abspath(cpp_file)

    if not os.path.isfile(cpp_file):
        create_cpp(cpp_file, hpp_file)

    config = make_config()
    hpp_global_namespace = parse(hpp_file, config)

    hpp_declarations = [decl for decl in find_declarations(
        hpp_global_namespace, hpp_file) if is_implementable(decl)]

    with open(cpp_file, "r") as f:
        cpp_buf = "".join(f.read().split())
    with open(cpp_file, "a") as f:
        for hpp_decl in hpp_declarations:
            hpp_declstr = declstr(hpp_decl)
            hpp_mangled_declstr = "".join(hpp_declstr.split())
            # FIXME: Very crude way of determining if the hpp
            # declaration is already implemented
            if cpp_buf.find(hpp_mangled_declstr) == -1:
                f.write(hpp_declstr)
                f.write(" {\n\n}\n\n")
