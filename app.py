from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

def check_winner(board):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]
    if "" not in board:
        return "draw"
    return None

def ai_move(board):
    empty = [i for i, val in enumerate(board) if val == ""]
    return random.choice(empty)

@app.route('/')
def index():
    session.setdefault("player", "X")
    session.setdefault("score", {"X": 0, "O": 0, "draw": 0})
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    board = data['board']
    turn = data['turn']

    board[data['index']] = turn
    winner = check_winner(board)

    if not winner and data['mode'] == 'ai' and turn == 'X':
        ai_index = ai_move(board)
        board[ai_index] = 'O'
        winner = check_winner(board)

    if winner:
        session['score'][winner] += 1

    return jsonify(board=board, winner=winner, score=session['score'])

@app.route('/reset', methods=['POST'])
def reset():
    session['score'] = {"X": 0, "O": 0, "draw": 0}
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

