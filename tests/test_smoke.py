"""Minimal no-network smoke tests for vision_executor."""

import subprocess
import sys
import unittest
import unittest.mock
from pathlib import Path


class TestHelp(unittest.TestCase):
    """Tests that --help exits 0 and documents core flags."""

    def test_help_exits_zero(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "scripts.vision_executor", "--help"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )
        self.assertEqual(result.returncode, 0)

    def test_help_contains_core_flags(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "scripts.vision_executor", "--help"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )
        output = result.stdout + result.stderr
        self.assertIn("--image", output)
        self.assertIn("--prompt", output)
        self.assertIn("--model", output)


class TestMissingApiKey(unittest.TestCase):
    """Tests that missing GOOGLE_API_KEY exits nonzero with a clear message."""

    def test_missing_key_exits_nonzero(self) -> None:
        from scripts.vision_executor import run_vision_sandbox

        with unittest.mock.patch.dict("os.environ", {}, clear=True):
            # Ensure GOOGLE_API_KEY is absent
            import os

            os.environ.pop("GOOGLE_API_KEY", None)
            with self.assertRaises(SystemExit) as ctx:
                run_vision_sandbox("/definitely/missing.png", "prompt")
            self.assertNotEqual(ctx.exception.code, 0)

    def test_missing_key_prints_env_var_name(self) -> None:
        import contextlib
        import io

        from scripts.vision_executor import run_vision_sandbox

        stderr_buf = io.StringIO()
        with unittest.mock.patch.dict("os.environ", {}, clear=True):
            import os

            os.environ.pop("GOOGLE_API_KEY", None)
            with contextlib.redirect_stderr(stderr_buf):
                with self.assertRaises(SystemExit):
                    run_vision_sandbox("/definitely/missing.png", "prompt")
        self.assertIn("GOOGLE_API_KEY", stderr_buf.getvalue())


class TestMissingImageFile(unittest.TestCase):
    """Tests that a missing image file exits nonzero when GOOGLE_API_KEY is set."""

    def test_missing_image_exits_nonzero(self) -> None:
        from scripts.vision_executor import run_vision_sandbox

        with unittest.mock.patch.dict("os.environ", {"GOOGLE_API_KEY": "fake-key"}):
            with self.assertRaises(SystemExit) as ctx:
                run_vision_sandbox("/definitely/missing.png", "prompt")
            self.assertNotEqual(ctx.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
