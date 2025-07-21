let currentPlayer = "X";
let board = ["", "", "", "", "", "", "", "", ""];
let gameOver = false;

const statusText = document.getElementById("status");
const cells = document.querySelectorAll(".cell");

cells.forEach(cell => {
    cell.addEventListener("click", () => {
        const index = cell.getAttribute("data-index");

        if (board[index] === "" && !gameOver) {
            board[index] = currentPlayer;
            cell.textContent = currentPlayer;

            if (checkWinner()) {
                statusText.textContent = `🎉 Player ${currentPlayer} wins!`;
                gameOver = true;
            } else if (board.every(cell => cell !== "")) {
                statusText.textContent = "🤝 It's a draw!";
                gameOver = true;
            } else {
                currentPlayer = currentPlayer === "X" ? "O" : "X";
                statusText.textContent = `Player ${currentPlayer}'s turn`;
            }
        }
    });
});

function checkWinner() {
    const winPatterns = [
        [0,1,2], [3,4,5], [6,7,8], // rows
        [0,3,6], [1,4,7], [2,5,8], // cols
        [0,4,8], [2,4,6]           // diagonals
    ];

    return winPatterns.some(pattern => {
        const [a, b, c] = pattern;
        return board[a] && board[a] === board[b] && board[a] === board[c];
    });
}

function resetGame() {
    currentPlayer = "X";
    board = ["", "", "", "", "", "", "", "", ""];
    gameOver = false;
    cells.forEach(cell => cell.textContent = "");
    statusText.textContent = "Player X's turn";
}

