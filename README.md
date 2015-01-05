# Clighter: VIM plugin to improve c-family development environment based on Clang

## Intro

Clighter(C lighter) is a vim plugin that integrates libclang to improve
development environment for c-family programming. Clighter provides following
features currently:

* Syntax(semantic) highlighting
* Cursor word highlighting
* Experimental rename-refactoring function

![Clighter GIF demo](http://goo.gl/C7FYg8)

## Requirements

Clighter requires the following:

* Vim version 7.4 with python2.x enabled
* libclang with python binding(3.5 is recommended). Please reference
  http://llvm.org/apt/ to install
* Clighter has been tested under Linux

## Installation

* Vundle Install:
```vim
Bundle 'bbchung/clighter'
```
* Manuall Install

Untar the clighter.tar.gz to your vim path.

## Options

### g:clighter_autostart

Clighter will automatically start while g:clighter_autostart == `1`.

Default: `1`
```vim
let g:clighter_autostart = 1
```

### g:ClighterCompileArgs

Clighter will pass these args to libclang to parse the code. Notice that bad
options will cause clighter not working even crashing. For convenience, you
can use mksession to save this option.

Default: `["-Iinclude"]`
```vim
let g:ClighterCompileArgs = ["-Iinclude"]
```

### g:clighter_libclang_file

Clighter try to find libclang-3.5 in your system automatically. You must set
this option if clighter cannot find libclang or other version of libclang is
used.

Default: `''`
```vim
let g:clighter_libclang_file = '/usr/lib/libclang.so'
```

### g:clighter_rename_prompt_level

The prompt level of rename refactoring.

`0`: no prompt

`1`: prompt while do cross buffer renaming

`2`: prompt of each word that going to be replaced

Default: `1`
```vim
let g:clighter_rename_prompt_level = 1
```

### g:clighter_enable_cross_rename

`0`: disable

`1`: enable

Default: `1`
```vim
let g:clighter_enable_cross_rename = 1
```

### g:clighter_highlight_groups

Define the token type of syntax to be highlighted.

Default: `['clighterMacroInstantiation','clighterStructDecl','clighterClassDecl','clighterEnumDecl','clighterEnumConstantDecl','clighterTypeRef','clighterDeclRefExprEnum']`
```vim
let g:clighter_highlight_groups = ['clighterMacroInstantiation', 'clighterStructDecl', 'clighterClassDecl', 'clighterEnumDecl', 'clighterEnumConstantDecl', 'clighterTypeRef', 'clighterDeclRefExprEnum']
```

### g:clighter_cursor_hl_default

Enable cursor highlight by default.

Default: `1`
```vim
let g:clighter_cursor_hl_default = 1
```

## Commands and Functions

Clighter provides these commands and functions.

### ClighterEnable

Enable clighter plugin.

### ClighterDisable

Disable clighter plugin.

### ClighterToggleCursorHL

Toggle cursor highlighting.

### clighter#Rename()

* An experimental function to do rename refactoring.
* The scope is opened vim buffers.
* There is no one-step undo/redo method.
* Strongly recommend that backing up all files before calling this function.
* For convenience, you can add key mapping in your vimrc:
```vim
nmap <silent> <Leader>r :call clighter#Rename()<CR>
```

### clighter#SetCompileArgs()

Set clang compile args in runtime.

## Syntax Group

Clighter defines these syntax groups corresponded to libclang.

```vim
hi link clighterMacroInstantiation Constant
hi link clighterTypeRef Identifier
hi link clighterStructDecl Type
hi link clighterClassDecl Type
hi link clighterEnumDecl Type
hi link clighterEnumConstantDecl Identifier
hi link clighterDeclRefExprEnum Identifier
hi link clighterCursorSymbolRef IncSearch
hi link clighterFunctionDecl None
hi link clighterDeclRefExprCall None
hi link clighterMemberRefExpr None
hi link clighterNamespace None
```

You can customize these colors in your colorscheme, for example:
```vim
hi clighterTypeRef term=NONE cterm=NONE ctermbg=232 ctermfg=255 gui=NONE
hi clighterClassDecl term=NONE cterm=NONE ctermbg=255 ctermfg=232 gui=NONE
```

## FAQ

### The clighter plugin doesn't work.
Vim version 7.4 with python2.x is required, and make sure libclang(3.5 is
recommended) is installed correctly and set g:clighter_libclang_file if need.

### Why rename-refactoring function is an experimental function?
Even though libclang provides many useful informations, it's not enough to do
cross file rename-refactoring. Clighter needs to use its own way way to
'guess' what should be renamed. Clighter can't gurantee the result of
rename-factoring result is perfect.
