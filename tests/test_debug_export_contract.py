import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class DebugExportContractTests(unittest.TestCase):
    def test_project_export_contract_is_present(self):
        export_h = (ROOT / "src" / "Debug" / "DKDebugExport.h").read_text(encoding="utf-8")
        export_m = (ROOT / "src" / "Debug" / "DKDebugExport.m").read_text(encoding="utf-8")
        inspector = (ROOT / "src" / "Debug" / "DKDebugInspector.m").read_text(encoding="utf-8")
        class_dump_h = (ROOT / "src" / "FLEX" / "DKClassDump.h").read_text(encoding="utf-8")
        class_dump_m = (ROOT / "src" / "FLEX" / "DKClassDump.m").read_text(encoding="utf-8")

        self.assertIn("DKDebugExportModeProject", export_h)
        self.assertIn("DKClassDumpRuntimeInventory", class_dump_h)
        self.assertIn("DKClassDumpRuntimeInventory", class_dump_m)
        self.assertIn('project/classes/index.json', export_m)
        self.assertIn('dykiller.debug-project.v1', export_m)
        self.assertIn('导出项目 zip', inspector)
        self.assertIn('DKDebugExportModeProject', inspector)


if __name__ == "__main__":
    unittest.main()