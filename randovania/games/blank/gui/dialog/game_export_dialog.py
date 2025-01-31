import dataclasses
from pathlib import Path

from randovania.games.blank.exporter.game_exporter import BlankGameExportParams
from randovania.games.blank.exporter.options import BlankPerGameOptions
from randovania.games.game import RandovaniaGame
from randovania.gui.dialog.game_export_dialog import GameExportDialog, spoiler_path_for


class BlankGameExportDialog(GameExportDialog):
    """A window for asking the user for what is needed to export this specific game.

    The provided implementation assumes you need an ISO/ROM file, and produces a new ISO/ROM file."""

    @classmethod
    def game_enum(cls):
        return RandovaniaGame.BLANK

    @property
    def input_file(self) -> Path:
        raise NotImplementedError("This method hasn't been implemented yet")

    @property
    def output_file(self) -> Path:
        raise NotImplementedError("This method hasn't been implemented yet")

    @property
    def auto_save_spoiler(self) -> bool:
        raise NotImplementedError("This method hasn't been implemented yet")

    def update_per_game_options(self, per_game: BlankPerGameOptions) -> BlankPerGameOptions:
        return dataclasses.replace(
            per_game,
            input_path=self.input_file,
            output_path=self.output_file,
        )

    def get_game_export_params(self) -> BlankGameExportParams:
        """Creates the GameExportParams for this specific game,
        based on the data provided by the user in this window."""

        spoiler_output = spoiler_path_for(self.auto_save_spoiler, self.output_file)

        return BlankGameExportParams(
            spoiler_output=spoiler_output,
            input_path=self.input_file,
            output_path=self.output_file,
        )
