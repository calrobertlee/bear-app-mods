# bear-app-mods
This is my first repository ever on any platform! Hello world!

I was inspired by this [Reddit post](https://www.reddit.com/r/bearapp/comments/fd7teq/how_i_do_bidirectional_linking_in_bear_ala_roam/) and decided to find a way to quicken the process.

This shorcut works with Espanso, a free text expander that is installed with Homebrew in the terminal.

This shortcut uses Python to find and replace spaces in the string in the clipboard, as Bear's URL scheme requires spaces to be replaced with "%20"

By typing the trigger text `:blink` in Bear it will auto-generate a footer with a soft reference link and date.

Currently, the script returns an extra newline in the outputted text — you must manually delete that new line, I haven't found a workaroud.  Here's a [gif](https://gfycat.com/freeskinnyfairybluebird) of what this looks like.

Message me if you have any questions!
