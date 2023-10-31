from enum import Enum


class ConversationFormats(Enum):
    GIVE_A_LESSON = """
Please provide a lesson on the specified topic.
Structure the lesson into chapters and sections.
Start with a table of contents and check if I am ready to proceed.
After each section, check if I have questions or if I'm ready for the next section.
    """

    WRITE_CODE = """
Write code based on the specifications I provide.
Ensure each component comes with unit tests.
If this is the beginning of a project, provide a project skeleton.
If there are queries about the specifications, ask them concisely.
Do not deliver code if there's any ambiguity about the specifications.
    """

    REVIEW_CODE = """
Conduct a code review and highlight areas for improvement.
Hold the review to the standards of an exemplary professional software engineer.
Provide feedback using the following tags based on issue severity:
    - [BUG] for bugs
    - [STYLE] for style issues
    - [REFACTOR] for refactoring suggestions
    - [OPTIMIZE] for optimization suggestions
    - [QUESTION] for questions
    - [COMPLIMENT] for compliments
    - [SUGGESTION] for general suggestions
    - [PRAISE] for praise
    - [CONCERN] for concerns
    - [CRITICISM] for criticisms
    """




