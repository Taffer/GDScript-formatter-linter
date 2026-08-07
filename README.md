# GDScript-formatter-linter

A [Sublime Text](https://www.sublimetext.com) linter using
[GDQuest](https://www.gdquest.com)'s
[GDScript-formatter](https://github.com/GDQuest/GDScript-formatter).

You must
[install GDScript-formatter](https://github.com/GDQuest/GDScript-formatter#installing-and-running-the-formatter)
before you can successfully use this linter.

## Settings

To tweak settings, add a `gdscriptformatterlinter` section to your user
`SublimeLinter.sublime-settings`file. For example:

```py
    "gdscriptformatterlinter" : {
        "args": [
            "--max-line-length",
            "132",
        ]
    },
```

Note that the `--pretty` argument will prevent the plugin from operating
properly.

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
