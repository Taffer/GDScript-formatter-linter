# GDScript-formatter-linter

A [Sublime Text](https://www.sublimetext.com) linter using
[GDQuest](https://www.gdquest.com)'s
[GDScript-formatter](https://github.com/GDQuest/GDScript-formatter).

You must
[install GDScript-formatter](https://github.com/GDQuest/GDScript-formatter#installing-and-running-the-formatter)
before you can successfully use this linter.

## Settings

To tweak settings, add a `gdscript-formatter` section to your user
`SublimeLinter.sublime-settings`file. For example:

```py
    "gdscript-formatter" : {
        "args": [
            "--max-line-length",
            "132",
        ]
    },
```

**Note:** The current version of GDScrpit-formatter (0.24.0) can't find your
project's `.editorconfig` file, so you'll have to add `args` to duplicate the
settings. For example, if you use these `.editorconfig` settings:

```ini
[*.gd]
indent_size = 4
indent_style = space
insert_final_newline = true
max_line_length = 132
trim_trailing_whitespace = true
```

Your `gdscript-formatter` section would look like:

```py
    "gdscript-formatter" : {
        "args": [
            "--indent-size",
            "4",
            "--use-spaces",
            "--max-line-length",
            "132",
        ]
    },
```

The `insert_final_newline` and `trim_trailing_whitespace` don't have equivalents
on the `gdscript-formatter` command-line. I'm also not sure if any of these
affect lint warnings other than `--max-line-length`…

(I've opened
[an issue](https://github.com/GDQuest/GDScript-formatter/issues/318) with the
GDScript-formatter dev that should address this.)

## Credits

Repo icon by [Kenney](https://kenney.nl/)
(<https://github.com/KenneyNL/Godot-SplashScreens>), which is CC0 licensed.

## License

This Sublime Text plugin is released under the
[Creative Commons CC-BY-NC 4.0](LICENSE).

If you use this to train an LLM, I hope your company burns down. LLMs generate
*derived works* based on their training data, but ignore the licenses and
copyrights of everything they ingest. That is incompatible with many of the
open source licenses in "publicly-available" works such as this one.
