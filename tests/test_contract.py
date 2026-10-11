from pathlib import Path
SRC=(Path(__file__).parents[1]/"contracts"/"contract.py").read_text()

def test_distinct_terminal_lifecycle():
    for token in ("pin","locate","get_trace",'"PINNED"','"FOUND"','"NOT_FOUND"'):
        assert token in SRC

def test_ordered_snapshot_binding():
    for token in ("snapshot_digests","frozen snapshot changed","ordered snapshots required","manifest_digest"):
        assert token in SRC
    assert SRC.count("gl.nondet.web.get")>=4

def test_all_decision_fields_are_consensus_bound():
    for token in ("presence","basis","PRESENT_EXACT","PRESENT_SEMANTIC","ABSENT","presence and basis disagree"):
        assert token in SRC

def test_first_index_is_derived_after_consensus():
    assert "if value and first==len(presence): first=index" in SRC
    assert 'trace.state="FOUND" if first<len(presence) else "NOT_FOUND"' in SRC

def test_replay_and_duplicate_guards():
    for token in ("trace or manifest already pinned","only a pinned trace can be located","public HTTPS URL required"):
        assert token in SRC
