import sublime
import sublime_plugin

class CommentCoutLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            all_lines = self.view.lines(sublime.Region(0, self.view.size()))
            
            for line in reversed(all_lines):
                line_content = self.view.substr(line).strip() 
                if line_content.startswith("cerr") or line_content.startswith("dbg"):
                    now = self.view.substr(line)
                    marker = " // 998244353"
                    self.view.replace(edit, line, f'// {now}{marker}')
