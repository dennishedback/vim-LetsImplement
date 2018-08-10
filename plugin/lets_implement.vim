" Copyright (c) 2018, Dennis Hedback
" All rights reserved.
"
" Redistribution and use in source and binary forms, with or without
" modification, are permitted provided that the following conditions
" are met:
"
"     1. Redistributions of source code must retain the above copyright
"        notice, this list of conditions and the following disclaimer.
"
"     2. Redistributions in binary form must reproduce the above copyright
"        notice, this list of conditions and the following disclaimer in
"        the documentation and/or other materials provided with the
"        distribution.
"
" THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
" 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
" LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
" A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
" HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
" SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
" LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
" DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
" THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
" (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
" OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

if !has("python3")
    finish
endif

"if exists("g:__lets_implement_plugin_loaded")
"    finish
"endif

" https://stackoverflow.com/questions/6639863/vim-split-unless-open
function! LimplSmartOpen(file)
    let buffer_num=bufnr(expand(a:file))
    let window_num=bufwinnr(buffer_num)
    if window_num != -1 && g:lets_implement_auto_jump
        " Jump to existing window
        exe window_num . "wincmd w"
    elseif window_num == -1 && g:lets_implement_auto_open
        " Open file in new window
        exe g:lets_implement_open_command . a:file
    endif
endfunction

let s:script = expand("<sfile>:p:h") . "/LimplCall.py"

function! LimplCall()
    exe "py3file " . s:script
endfunction

command! LetsImplement call LimplCall()

let g:__lets_implement_plugin_loaded=1
let g:lets_implement_auto_jump=1
let g:lets_implement_auto_open=1
let g:lets_implement_open_command="belowright split"
