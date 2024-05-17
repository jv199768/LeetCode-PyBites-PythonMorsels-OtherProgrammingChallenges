    var chessBoard = "";
    var size = 8;

    for (var lineCounter = 1; lineCounter < size; lineCounter++) { 

        if (lineCounter%2 === 0) {

//if lineCounter is an even number
        for (var charCounter = 1; charCounter < size; charCounter++) {
            var evenOdd = (charCounter%2 === 0);
            switch (evenOdd) {
                case true:
                    (chessBoard += "#");
                    break;
                case false:
                    (chessBoard += " ");
                    break;
                }
            }                   
        }
    else { //if lineCounter is an odd number
        for (var charCounter = 1; charCounter < size; charCounter++) {
            var evenOdd = (charCounter%2 === 0);
            switch (evenOdd) {
                case true:
                    (chessBoard += " ");
                    break;
                case false:
                    (chessBoard += "#");
                    break;
            }
            }                       
        }   
    chessBoard += "\n";
    }
    console.log(chessBoard);
