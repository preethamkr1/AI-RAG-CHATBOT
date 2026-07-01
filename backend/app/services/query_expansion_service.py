def expand_query(question: str):

    expansion_dictionary = {
        "dbms": "Database Management Systems",
        "ml": "Machine Learning",
        "iot": "Internet of Things",
        "cn": "Computer Networks",
        "atcd": "Automata Theory and Compiler Design",
        "python": "Python Programming",
        "lab": "Laboratory practical internal marks",
        "cgpa": "Cumulative Grade Point Average",
        "sgpa": "Semester Grade Point Average"
    }

    expanded_question = question

    lower_question = question.lower()

    for key, value in expansion_dictionary.items():

        if key in lower_question:
            expanded_question += f" {value}"

    return expanded_question