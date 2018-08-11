# vim-LetsImplement

Create C/C++ definition stubs from header files.

![](tty.gif)

## Can I haz auto implement?

Yes you can! vim-LetsImplement parses your header files and appends definition stubs to a C/C++ file.

## Install

### Dependencies

* vim compiled with python3 support
* [castxml](https://github.com/CastXML/CastXML)
* [pygccxml](https://github.com/gccxml/pygccxml)

### Instructions

1. Run `vim --version` and look for `+python3` to verify that your vim installation was compiled with support for python3.
2. On many Linux systems, `castxml` should be obtainable through your package manager, either from official or unofficial repositories. If not, the more readily available package `gccxml` *could* work instead. On Mac OSX, homebrew is your friend.
3. `pygccxml` is most easily obtainable through pip: `pip install pygccxml`
4. Install vim-LetsImplement using Vundle or Pathogen. Alternatively, manually install by copying everything under `vim-LetsImplement/plugin/` to `~/.vim/plugin`

## Usage and configuration

vim-LetsImplement comes with the command `:LetsImplement`. By default, this
command will: Parse the contents of the current buffer, extract all
implementable declarations and append definitions to a corresponding
C/C++-file. Its behaviour may be configured in your `.vimrc` (default
values shown below):

```
" Whether to auto jump to the window containing the implementation file
let g:lets_implement_auto_jump=1
" Whether to auto open the implementation file
let g:lets_implement_auto_open=1
" Vim command used to open the implementation file
let g:lets_implement_open_command="belowright split"
```

## Planned features

* Only implement declaration under cursor
* Only implement declarations in selection
* Different brace styles
* Arbitrary filenames
* Preservation of modifier order

## Known issues

* Backend writes to standard output/standard error which may or may not make your vim session fubar
* Backend issues warnings on C++17 features

## Copying

See file `LICENSE`.
