"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [(1,2,3)],
            "answer": 1
        },
        {
            "input": [(1,2, (3,))],
            "answer": 2
        },
        {
            "input": [(1,2,(3,(4,)))],
            "answer": 3
        },
        {
            "input": [()],
            "answer": 1
        },
        {
            "input": [((),)],
            "answer": 2
        },
        {
            "input": [(((),),)],
            "answer": 3
        },
        {
            "input": [(1,(2,),(3,))],
            "answer": 2
        },
        {
            "input": [(1,((),),(3,))],
            "answer": 3
        },
        
    ],
    "Extra": [
        {
            "input": [(6, 3)],
            "answer": 1
        },
        {
            "input": [(6, 7)],
            "answer": 1
        },
        {
            "input": [(1,2,3)],
            "answer": 1
        },
        {
            "input": [(5, 2, (3,))],
            "answer": 2
        },
        {
            "input": [(1,2,((3,),(4,)))],
            "answer": 3
        },
        {
            "input": [((),())],
            "answer": 2
        },
        {
            "input": [(((),(),()))],
            "answer": 3
        },
        {
            "input": [((1,),(5,),(3,))],
            "answer": 2
        },
        {
            "input": [(1, (2,), (2, (3,)))],
            "answer": 3
        }
    ]
}
