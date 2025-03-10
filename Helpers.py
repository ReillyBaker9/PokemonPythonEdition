def playerChoice(ask_text, max, fail_text="Invalid selection."):
    player_input = -1
    allowed_values = list(range(max))
    while player_input not in allowed_values:
        try:
            player_input = int(input(ask_text)) - 1
            if player_input in allowed_values:
                break
        except ValueError:
            player_input = -1
        print(fail_text)
    return player_input
