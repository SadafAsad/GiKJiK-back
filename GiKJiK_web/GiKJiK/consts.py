class QuizConsts:
    MULTIPLE_CHOICE = '0'
    SHORT_ANSWER = '1'
    BOTH = '2'

    types = (
        (MULTIPLE_CHOICE, "Multiple Choice"),
        (SHORT_ANSWER, "Short Answer"),
        (BOTH, "Both")
    )

    NOT_OVERDUE = '0'
    OVERDUE = '1'

    states = (
        (NOT_OVERDUE, "Not Overdue"),
        (OVERDUE, "Overdue")
    )

class AnswerConsts:
    MULTIPLE_CHOICE = '0'
    SHORT_ANSWER = '1'

    types = (
        (MULTIPLE_CHOICE, "Multiple Choice"),
        (SHORT_ANSWER, "Short Answer")
    )

    CORRECT = '0'
    WRONG = '1'
    NOT_ANSWERED = '2'

    states = (
        (CORRECT, "Correct"),
        (WRONG, "Wrong"),
        (NOT_ANSWERED, "Not Answered")
    )

class ClassConsts:
    ONLINE = '0'
    OFFLINE = '1'

    states = (
        (ONLINE, "Online"),
        (OFFLINE, "Offline")
    )
