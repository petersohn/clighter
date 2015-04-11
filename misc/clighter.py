import vim
import string
import clighter_helper
import clang_service
import highlighting


def on_filetype():
    if clighter_helper.is_vim_buffer_allowed(vim.current.buffer):
        clang_service.ClangService().register([vim.current.buffer.name])
    else:
        clang_service.ClangService().unregister([vim.current.buffer.name])

    clang_service.ClangService().switch(vim.current.buffer.name)
    highlighting.clear_all()


def register_allowed_buffers():
    tobe_reg = set()
    for buf in vim.buffers:
        if clighter_helper.is_vim_buffer_allowed(buf):
            tobe_reg.add(buf.name)

    clang_service.ClangService().register(tobe_reg)


def clang_switch_to_current():
    clang_service.ClangService().switch(vim.current.buffer.name)

    if not vim.current.window.vars.get('clighter_hl'):
        vim.current.window.vars['clighter_hl'] = [
            -1, [], []]  # [hl_tick, syntax_range, symbol_range]
    else:
        vim.current.window.vars['clighter_hl'][0] = -1


def update_buffer_if_allow():
    if clighter_helper.is_vim_buffer_allowed(vim.current.buffer):
        clang_service.ClangService().update_buffers(
            [(vim.current.buffer.name,
              '\n'.join(vim.current.buffer),
              string.atoi(vim.eval('b:changedtick')))])


def get_vim_cursor_info():
    cc = clang_service.ClangService().get_cc(vim.current.buffer.name)
    if not cc:
        return None

    tu = cc.current_tu
    if not tu:
        return None

    vim_cursor = clighter_helper.get_vim_cursor(tu, tu.get_file(cc.name))

    if vim_cursor:
        return vim_cursor.kind, vim_cursor.type.kind
    else:
        return None


def show_information():
    print "Enable clighter: %s" % ('Enable' if vim.eval('s:clighter_enabled') == '1' else 'Disable')
    print "Current context: %s" % (clang_service.ClangService().current_cc.name if clang_service.ClangService().current_cc else '')
    print "Highlight occurrences: %s" % ('On' if vim.eval('g:ClighterOccurrences') == '1' else 'Off')
    print "Compilation database: %s" % ((clang_service.ClangService().compilation_database.file_path) if clang_service.ClangService().compilation_database else None)
    print "Compile args: %s" % (' '.join(clang_service.ClangService().current_cc.compile_args) if clang_service.ClangService().current_cc and clang_service.ClangService().current_cc.compile_args else '')
    print 'Cursor info:', get_vim_cursor_info()
