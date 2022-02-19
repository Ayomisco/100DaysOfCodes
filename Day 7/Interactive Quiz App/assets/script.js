var questions = [
{
    question: "What does HTML stand for?",
    choices: [" Hyperlinks and Text Markup Language", " Hyper Text Markup Language", " Hyper Text Markup Language", " Hyper Text Multi Language"],
    correctAnswer: 2
}, {
    question: "The correct sequence of HTML tags for starting a webpage is",
    choices: ["Head, Title, HTML, body", "HTML, Body, Title, Head", "HTML, Head, Title, Body", "HTML, Head, Title, Body"],
    correctAnswer: 3
}, {
        question: "How many heading tags are there in HTML5?",
    choices: ["2", "3", "6", "5"],
    correctAnswer: 2
}, {
        question: "Which of the following attributes is used to add link to any element?",
        choices: ["link", "ref", "href", "newref"],
    correctAnswer: 2
}, {
        question: "What is the difference between an opening tag and a closing tag?",
        choices: ["Opening tag has a / in front", "Closing tag has a / in front", "Difference is not visible", "here is no difference"],
    correctAnswer: 1
}, {
        question: "Where is the meta tag only found?",
        choices: ["The home page", "The last page", "The second page", "billy"],
    correctAnswer: 0

}, {
        question: "What is an element that does not have a closing tag called?",
        choices: ["Tag", "Empty element", "Closed element", "Single Element"],
    correctAnswer: 1
}, {
        question: " What should values always be enclosed in?",
        choices: ["Quotation marks", "Commas", "Curly Bracket", "Parenthesis"],
    correctAnswer: 0
}, {
        question: "What is always a welcome page, and explains the purpose or topic of the site?",
        choices: ["Page 4", "Homepage", "Middle Page", "Table of contents"],
    correctAnswer: 1

}, {
        question: "What does View Source do?",
        choices: ["Nothing", "Brings up a note pad with the HTML code already used for the site.", "Close Site", "Opens a new website."],
    correctAnswer: 1

}, {
        question: "Which of the following attribute is used to provide a unique name to an element?",
        choices: ["class", "None of the above", "id", "type"],
    correctAnswer: 2

}, {
        question: "What are the types of unordered or bulleted list in HTML?",
        choices: ["disc, square, triangle", "polygon, triangle, circle", "disc, circle, square", "All of the above"],
    correctAnswer: 3
}, {
        question: "Which of the following HTML attribute is used to define inline styles?",
        choices: ["style", "type", "class", "None of the above"],
    correctAnswer: 0

}, {
        question: " An HTML program is saved by using the ____ extension.",
        choices: [".ht", ".hml", ".html", "None of the above"],
    correctAnswer: 2

}, {
        question: "A program in HTML can be rendered and read by -",
        choices: ["Web browser", "Server", "Interpreter", "None of the above"],
    correctAnswer: 0

}, {
        question: "Which is the correct way to comment out something in HTML?",
        choices: ["Using ## and #", "Using <!-- and -->", "Using </-- and -/->", "Using <!-- and -!>"],
    correctAnswer: 1

}
];

var currentQuestion = 0;
var correctAnswers = 0;
var quizOver = false;

// .ready check and ensure that the page is loader before executing
$(document).ready(function () {

    // Display the first question
    displayCurrentQuestion();
    $(this).find(".quizMessage").hide();

    // On clicking next, display the next question
    $(this).find(".nextButton").on("click", function () {
        if (!quizOver) {

            value = $("input[type='radio']:checked").val();

            if (value == undefined) {
                $(document).find(".quizMessage").text("Please select an answer");
                $(document).find(".quizMessage").show();
            } else {
                // TODO: Remove any message -> not sure if this is efficient to call this each time....
                $(document).find(".quizMessage").hide();

                if (value == questions[currentQuestion].correctAnswer) {
                    correctAnswers++;
                }

                currentQuestion++; // Since we have already displayed the first question on DOM ready
                if (currentQuestion < questions.length) {
                    displayCurrentQuestion();
                } else {
                    displayScore();
                    //                    $(document).find(".nextButton").toggle();
                    //                    $(document).find(".playAgainButton").toggle();
                    // Change the text in the next button to ask if user wants to play again
                    $(document).find(".nextButton").text("Play Again?");
                    quizOver = true;
                }
            }
        } else { // quiz is over and clicked the next button (which now displays 'Play Again?'
            quizOver = false;
            $(document).find(".nextButton").text("Next Question");
            resetQuiz();
            displayCurrentQuestion();
            hideScore();
        }
    });

});

// This displays the current question AND the choices
function displayCurrentQuestion() {

    console.log("In display current Question");

    var question = questions[currentQuestion].question;
    var questionClass = $(document).find(".quizContainer > .question");
    var choiceList = $(document).find(".quizContainer > .choiceList");
    var numChoices = questions[currentQuestion].choices.length;

    // Set the questionClass text to the current question
    $(questionClass).text(question);

    // Remove all current <li> elements (if any)
    $(choiceList).find("li").remove();

    var choice;
    for (i = 0; i < numChoices; i++) {
        choice = questions[currentQuestion].choices[i];
        $('<li><input type="radio" value=' + i + ' name="dynradio" />' + choice + '</li>').appendTo(choiceList);
    }
}

function resetQuiz() {
    currentQuestion = 0;
    correctAnswers = 0;
    hideScore();
}

function displayScore() {
    $(document).find(".quizContainer > .result").text("You scored: " + correctAnswers + " out of: " + questions.length);
    $(document).find(".quizContainer > .result").show();
}

function hideScore() {
    $(document).find(".result").hide();
}