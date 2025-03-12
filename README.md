# KiCad Semantic Versioning

This repos shows an example of using `commitizen` to manage commits and versioning
of a KiCad project.

You can work as usual with git, update the schematic and PCB, and commit using either
`cz commit` or `git commit`. If you format your commit messages in the way `commitizen`
expects, you can then run `cz bump` to increment the version number of your project.

The `update-version.py` script is run during the version update and will update a
text item on the board that matches the current version to the new version.

I like to use this to auto increment the version number on my PCBs on the silkscreen
layer.

You'll need to `pip install kicad-python` before using it.
