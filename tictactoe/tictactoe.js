const X_class = 'x';
const Y_class = 'y';
const WINNING_COMBINATIONS = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
];
const cellElements = document.querySelectorAll('[data-cell]');
const board = document.getElementById('board');
const restartButton = document.getElementById('restartButton');
const statusMessage = document.getElementById('statusMessage');
let oturn;  

startGame();
restartButton.addEventListener('click', startGame);
function startGame() {
    oturn = false;
    cellElements.forEach(cell => {
        cell.classList.remove(X_class);
        cell.classList.remove(O_class);
        cell.removeEventListener('click', handleClick);
        cell.addEventListener('click', handleClick, {once: true});
    });
    setBoardHoverClass(); {
        statusMessage.textContent = "Player X's turn";
    }
    function handleClick(e) {
        const cell = e.target;
        const currentClass = oturn?
        O_class : X_class;
        placeMark(cell, currentClass);
        if (checkWin(currentClass)) {
            endgame(false);
        } else if (isDraw()) {
            endgame(true);
        } else {
            swapTurns();
            setBoardHoverClass();
            statusMessage.textContent = 'Player ${oturn ? "O" : "X" WINS!!!';
        }
    }
    function isDraw() {
        return [...cellElements].every(cell => {
            return
            cell.classList.contains(X_class) || cell.classList.contains(O_class);
        });
    }
    function placeMark(cell, currentClass)
    {
        cell.classList.add(currentClass);
    }
    function swapTurns()
    {
        oturn = !oturn;
    }
    function setBoardHoverClass()
    {
        board.classList.remove(X_class);
        board.classList.remove(O_class);
        if (oturn) 
        {
            board.classList.add(O_class);
        }
        else
        {
            board.classList.add(X_class);
        }
    }
    function checkWin(currentClass)
    {
        WINNING_COMBINATIONS.some(combination =>
            {
                return combination.every(indec =>
                    {
                        return
                        classElements[index].classList.contains(currentClass);
                    });
            });
    }
}