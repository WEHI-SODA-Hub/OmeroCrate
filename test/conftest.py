from pathlib import Path
from git import Repo
import pytest

@pytest.fixture
def ca_imaging() -> Path:
    out = Path(__file__).parent / "ca-imaging"
    if not out.exists():
        Repo.clone_from("https://github.com/SFB-ELAINE/Ca-imaging-RO-Crate", out)
    return out

@pytest.fixture
def ca_imaging_1021(ca_imaging: Path) -> Path:
    return ca_imaging / "ro-crate_1021"
