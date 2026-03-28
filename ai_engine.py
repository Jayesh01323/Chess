def minimax(depth, maximizingPlayer):
    # Base case: return the score of the board if we reach the maximum depth or if the game is over
    if depth == 0 or game_over():
        return evaluate_board()

    if maximizingPlayer:
        maxEval = float('-inf')
        for move in generate_moves():
            make_move(move)
            eval = minimax(depth - 1, False)
            undo_move(move)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for move in generate_moves():
            make_move(move)
            eval = minimax(depth - 1, True)
            undo_move(move)
            minEval = min(minEval, eval)
        return minEval


def best_move():
    best_move = None
    best_value = float('-inf')
    for move in generate_moves():
        make_move(move)
        move_value = minimax(3, False)  # Adjust depth as needed
        undo_move(move)
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move

# Example usage
# move = best_move()
# make_move(move)