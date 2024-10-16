import sublime
import sublime_plugin

class RevertCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            all_lines = self.view.lines(sublime.Region(0, self.view.size()))
            
            for line in reversed(all_lines):
                line_content = self.view.substr(line) 
                if line_content.startswith("// ") and line_content.endswith(" // 998244353"):
                    uncommented_line = line_content.replace("// ", "", 1).replace(" // 998244353", "")
                    self.view.replace(edit, line, uncommented_line)

