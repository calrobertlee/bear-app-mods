# bear-app-mods
This is my first repository ever on any platform! Hello world!

I was inspired by this [Reddit post](https://www.reddit.com/r/bearapp/comments/fd7teq/how_i_do_bidirectional_linking_in_bear_ala_roam/) and decided to find a way to quicken the process.

This shorcut works with [Espanso](https://github.com/federico-terzi/espanso), a free text expander that is installed with Homebrew in the terminal.

This shortcut uses Python to find and replace spaces in the string in the clipboard, as Bear's URL scheme requires spaces to be replaced with "%20". Currently this does NOT allow for punctiuations in the clipboard text, I am adding this soon.

By typing the trigger text `:bf` in Bear it will auto-generate a footer with a soft reference link and date.

By typing the trigger test `:bd` in a brand new Bear note, it will auto-generate a Daily Note with a footer

Message me with any requests!
