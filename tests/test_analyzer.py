import app.analyzer as analyzer
import pytest

def test_binary_not_found(monkeypatch):
    monkeypatch.setattr(analyzer, "ANALYZER_BINARY", "./tests/stubs/no-existe")
    with pytest.raises(FileNotFoundError):
        analyzer.run_analysis([])

def test_analysis_success(monkeypatch):
    monkeypatch.setattr(analyzer, "ANALYZER_BINARY", "./tests/stubs/fake-analyzer.sh")
    code, output = analyzer.run_analysis([])
    assert code == 0
    assert "simulacion exitosa" in output

def test_analysis_failure(monkeypatch):
    monkeypatch.setattr(analyzer, "ANALYZER_BINARY", "./tests/stubs/fake-analyzer.sh")
    code, output = analyzer.run_analysis(["--fail"])
    assert code == 1
    assert "simular fallo" in output
