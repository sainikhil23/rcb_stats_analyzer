from rcb_stats.analyzer import load_match_data, win_loss_ratio, top_rum_scorer

def test_win_loss_ratio():
    data = load_match_data('data/rcb_2024.json')
    wins, losses = win_loss_ratio(data)
    assert wins == 1
    assert losses == 1

def test_top_run_scorer():
    data = load_match_data('data/rcb_2024.json')
    assert top_rum_scorer(data) == "Virat Kohli"
