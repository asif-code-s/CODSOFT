const cells = document.querySelectorAll('.cell');
const statusDisplay = document.getElementById('status');
const resetButton = document.getElementById('reset-button');
const playerXScore = document.getElementById('player-x-score');
const playerOScore = document.getElementById('player-o-score');
const drawScore = document.getElementById('draw-score');

let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = 'X';
let isGameActive = true;
let scores = { X: 0, O: 0, Draw: 0 };

const winningConditions = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
];

cells.forEach(cell => {
  cell.addEventListener('click', handleCellClick);
});

function handleCellClick(e) {
  const clickedCell = e.target;
  const index = parseInt(clickedCell.getAttribute('data-index'));
  if (board[index] !== "" || !isGameActive) return;

  board[index] = currentPlayer;
  clickedCell.textContent = 'X';

  if (checkWinner(board, 'X')) {
    statusDisplay.textContent = `You win! 🎉`;
    scores.X++;
    updateScoreboard();
    isGameActive = false;
    return;
  }

  if (isDraw()) {
    statusDisplay.textContent = "It's a draw 🤝";
    scores.Draw++;
    updateScoreboard();
    isGameActive = false;
    return;
  }

  currentPlayer = 'O';
  statusDisplay.textContent = `Zera-AI is thinking... 🤖`;

  setTimeout(() => {
    aiMove();

    if (checkWinner(board, 'O')) {
      statusDisplay.textContent = "Zera-AI wins! 🤖";
      scores.O++;
      updateScoreboard();
      isGameActive = false;
      return;
    }

    if (isDraw()) {
      statusDisplay.textContent = "It's a draw 🤝";
      scores.Draw++;
      updateScoreboard();
      isGameActive = false;
      return;
    }

    currentPlayer = 'X';
    statusDisplay.textContent = "Your turn! 🙋‍♂️";
  }, 500);
}

function aiMove() {
  let bestScore = -Infinity;
  let move;

  for (let i = 0; i < board.length; i++) {
    if (board[i] === "") {
      board[i] = 'O';
      let score = minimax(board, 0, false);
      board[i] = "";
      if (score > bestScore) {
        bestScore = score;
        move = i;
      }
    }
  }

  board[move] = 'O';
  cells[move].textContent = 'O';
}

function minimax(newBoard, depth, isMaximizing) {
  if (checkWinner(newBoard, 'O')) return 10 - depth;
  if (checkWinner(newBoard, 'X')) return depth - 10;
  if (isDraw()) return 0;

  if (isMaximizing) {
    let bestScore = -Infinity;
    for (let i = 0; i < newBoard.length; i++) {
      if (newBoard[i] === "") {
        newBoard[i] = 'O';
        let score = minimax(newBoard, depth + 1, false);
        newBoard[i] = "";
        bestScore = Math.max(score, bestScore);
      }
    }
    return bestScore;
  } else {
    let bestScore = Infinity;
    for (let i = 0; i < newBoard.length; i++) {
      if (newBoard[i] === "") {
        newBoard[i] = 'X';
        let score = minimax(newBoard, depth + 1, true);
        newBoard[i] = "";
        bestScore = Math.min(score, bestScore);
      }
    }
    return bestScore;
  }
}

function checkWinner(b, player) {
  return winningConditions.some(condition => {
    return condition.every(index => b[index] === player);
  });
}

function isDraw() {
  return board.every(cell => cell !== "");
}

function updateScoreboard() {
  playerXScore.textContent = `Human : ${scores.X}`;
  playerOScore.textContent = `Zera-AI : ${scores.O}`;
  drawScore.textContent = `Draws: ${scores.Draw}`;
}

resetButton.addEventListener('click', () => {
  board = ["", "", "", "", "", "", "", "", ""];
  currentPlayer = 'X';
  isGameActive = true;
  cells.forEach(cell => cell.textContent = "");
  statusDisplay.textContent = `Your turn! 🙋‍♂️`;
});

statusDisplay.textContent = `Your turn! 🙋‍♂️`;
