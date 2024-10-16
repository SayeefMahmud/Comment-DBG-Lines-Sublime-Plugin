1. Paste the two files in the `User` folder of Sublime Text
2. In sublime, go to settings -> key bindings
3. Add these two bindings and save

    {
    "keys": ["ctrl+shift+c"],  // Change the hotkey if you want
    "command": "comment_cout_lines"
    },
    {
    "keys": ["super+shift+c"],  // Change the hotkey if you want
    "command": "revert_comments"
    }
4. Done, use ctrl+shift+c for commenting and cmd+shift+c for uncommenting
