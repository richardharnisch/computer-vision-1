"""Small constructors for the original practice questions."""


def mc(topic, stem, correct, distractors, explanation, source):
    return dict(kind="mc", topic=topic, stem=stem, correct=correct,
                distractors=distractors, explanation=explanation, source=source)


def num(topic, stem, answer, explanation, source, integer=False):
    return dict(kind="num", topic=topic, stem=stem, answer=answer,
                explanation=explanation, source=source, integer=integer)
