const board = document.getElementById('board')
const squares = document.getElementsByClassName('square')
const players = ['X', 'O']
let currentPlayer = players[0]
const winningMessageElement = document.getElementById('winningMessage')
const winningMessageText = document.getElementById('winningMessageText')

const winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

for(let i = 0; i < squares.length; i++){
    squares[i].addEventListener('click', () => {
        if(squares[i].textContent !== ''){
            return
        }
        squares[i].textContent = currentPlayer
        if(currentPlayer === 'X') {
            squares[i].classList.add('blue')
        } else {
            squares[i].classList.add('green')
        }
        
        if(checkWin(currentPlayer)) {
            showWinningMessage(`${currentPlayer} wins!`)
            return
        }
        if(checkTie()) {
            showWinningMessage('Game is tied!')
            return
        }
        currentPlayer = (currentPlayer === players[0]) ? players[1] : players[0] 
        if(currentPlayer === 'O') {
            computerMove() // AI makes a move
        }
    })   
}

function checkWin(currentPlayer) {
    for(let i = 0; i < winning_combinations.length; i++){
        const [a, b, c] = winning_combinations[i]
        if(squares[a].textContent === currentPlayer && squares[b].textContent === currentPlayer && squares[c].textContent === currentPlayer){
            return true
        }
    }
    return false
}

function checkTie(){
    for(let i = 0; i < squares.length; i++) {
        if(squares[i].textContent === '') {
            return false;
        }
    }
    return true
}

function showWinningMessage(message) {
    winningMessageText.textContent = message
    winningMessageElement.classList.add('show')
}

function restartGame() {
    for(let i = 0; i < squares.length; i++) {
        squares[i].textContent = ""
        squares[i].classList.remove('blue', 'green')
    }
    winningMessageElement.classList.remove('show')
    currentPlayer = players[0]
}

function computerMove() {
    // Simple AI: Choose a random empty square
    let availableSquares = []
    for(let i = 0; i < squares.length; i++) {
        if(squares[i].textContent === '') {
            availableSquares.push(squares[i])
        }
    }
    if (availableSquares.length > 0) {
        const randomSquare = availableSquares[Math.floor(Math.random() * availableSquares.length)]
        randomSquare.textContent = 'O'
        randomSquare.classList.add('green')
        if(checkWin('O')) {
            showWinningMessage('O wins!')
        } else if(checkTie()) {
            showWinningMessage('Game is tied!')
        } else {
            currentPlayer = 'X'
        }
    }
}
