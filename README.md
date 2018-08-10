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
2. On many Linux systems, `castxml` should be obtainable through your package manager, either from official or unofficial repositories. On Mac OSX, homebrew should be able to accomplish the same thing. If not, `gccxml` *should* work instead.
3. `pygccxml` is most easily obtainable through pip: `pip install pygccxml`
4. Install vim-LetsImplement using Vundle or Pathogen. Alternatively, manually install by copying everything under `vim-LetsImplement/plugin/` to `~/.vim/plugin`

## Usage and configuration

vim-LetsImplement comes with the command `:LetsImplement`. When run, it will:

1. Parse the contents of the current buffer and extract all implementable declarations.
2. Look for a corresponding C/C++-file on *the same path* as the file in the current buffer. If no such file is found, it will create this file instead, and add an `#include`-directive.
3. Create definition stubs of all methods not yet implemented. **NOTE:** vim-LetsImplement will never overwrite the contents of the C/C++-file, only append to it.
4. If the implementation file is already open in some buffer, then vim will focus on that window. If not, the file will be opened automatically by vim-LetsImplement.

The following options are available for use in your `.vimrc` (default values shown below):

```
let g:lets_implement_auto_jump=1                      " Whether to auto focus on the implementation file
let g:lets_implement_auto_open=1                      " Whether to auto open the implementation file
let g:lets_implement_open_command="belowright split"  " Command used to open the implementation file
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
