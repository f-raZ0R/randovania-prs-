import dataclasses
from pathlib import Path

from randovania.exporter.game_exporter import GameExporter, GameExportParams
from randovania.lib import status_update_lib


@dataclasses.dataclass(frozen=True)
class BlankGameExportParams(GameExportParams):
    input_path: Path
    output_path: Path


class BlankGameExporter(GameExporter):
    _busy: bool = False

    @property
    def is_busy(self) -> bool:
        """
        Checks if the exporter is busy right now
        """
        return self._busy

    @property
    def export_can_be_aborted(self) -> bool:
        """
        Checks if export_game can be aborted
        """
        return False

    def _do_export_game(self, patch_data: dict, export_params: GameExportParams,
                        progress_update: status_update_lib.ProgressUpdateCallable):
        assert isinstance(export_params, BlankGameExportParams)
        raise RuntimeError("Needs to be implemented")
