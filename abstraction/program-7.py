# 7.	Create an abstract class Question with an abstract method evaluate_answer(). Derive:
# a)	MCQQuestion 
# b)	TrueFalseQuestion 
# c)	DescriptiveQuestion 
# Implement answer evaluation for each question type.

from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, prompt, max_marks):
        self.prompt = prompt
        self.max_marks = max_marks

    @abstractmethod
    def evaluate_answer(self, submitted_answer):
        pass


class MCQQuestion(Question):
    def __init__(self, prompt, options, correct_option, marks=1):
        super().__init__(prompt, marks)
        self.options = options
        self.correct_option = correct_option.strip().upper()

    def evaluate_answer(self, submitted_answer):
        is_correct = submitted_answer.strip().upper() == self.correct_option
        awarded = self.max_marks if is_correct else 0
        return awarded, f"{'Correct' if is_correct else 'Incorrect'} (Expected: {self.correct_option})"


class TrueFalseQuestion(Question):
    def __init__(self, prompt, correct_bool, marks=1):
        super().__init__(prompt, marks)
        self.correct_bool = correct_bool

    def evaluate_answer(self, submitted_answer):
        submitted_bool = str(submitted_answer).strip().lower() in ["true", "t", "1", "yes"]
        is_correct = submitted_bool == self.correct_bool
        awarded = self.max_marks if is_correct else 0
        return awarded, f"{'Correct' if is_correct else 'Incorrect'} (Expected: {self.correct_bool})"


class DescriptiveQuestion(Question):
    def __init__(self, prompt, key_phrases, marks=5):
        super().__init__(prompt, marks)
        self.key_phrases = [k.lower() for k in key_phrases]

    def evaluate_answer(self, submitted_answer):
        ans_lower = submitted_answer.lower()
        matched = [k for k in self.key_phrases if k in ans_lower]
        score_ratio = len(matched) / len(self.key_phrases) if self.key_phrases else 1.0
        awarded = round(score_ratio * self.max_marks, 1)
        return awarded, f"Matched {len(matched)}/{len(self.key_phrases)} key concepts."


q1 = MCQQuestion("What is the keyword to define a function in Python?\nA. func\nB. def\nC. define", ["A", "B", "C"], "B")
q2 = TrueFalseQuestion("Python strings are mutable.", False)
q3 = DescriptiveQuestion("Explain encapsulation in OOP.", ["data hiding", "private attributes", "methods"])

submissions = [
    (q1, "B"),
    (q2, "False"),
    (q3, "Encapsulation involves data hiding using private attributes and accessing them via public methods.")
]

print("Question Evaluation Results")
for q, ans in submissions:
    score, feedback = q.evaluate_answer(ans)
    print(f"Q: {q.prompt[:40]}...")
    print(f"Answer: {ans}")
    print(f"Score: {score}/{q.max_marks} | Feedback: {feedback}\n")
