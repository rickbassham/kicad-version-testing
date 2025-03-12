from os import environ
import kipy

pre_version = environ.get("CZ_PRE_CURRENT_VERSION")
new_version = environ.get("CZ_PRE_NEW_VERSION")

if not pre_version or not new_version:
    raise Exception(
        "Please set the environment variables: CZ_PRE_CURRENT_VERSION and CZ_PRE_NEW_VERSION"
    )

client = kipy.KiCad()

board = client.get_board()

texts = board.get_text()

items_to_update = []

for text in texts:
    if text.value.find(pre_version) != -1:
        text.value = text.value.replace(pre_version, new_version)
        items_to_update.append(text)

board.update_items(items_to_update)
board.save()
