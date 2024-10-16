1. Paste the two files in the `User` folder of Sublime Text
2. In sublime, go to settings -> key bindings
3. Add these two bindings and save

    { "keys": ["ctrl+shift+c"], "command": "comment_dbg_lines" }, // Change the hotkey if you want
   
    { "keys": ["super+shift+c"], "command": "revert_comments" } // Change the hotkey if you want
5. Done, use ctrl+shift+c for commenting and cmd+shift+c for uncommenting
