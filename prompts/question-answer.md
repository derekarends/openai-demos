# Question Answer

The idea here is to have ChatGPT come up with questions to ask given a document and then answer those questions based on another document. 

```
You are a hiring manager who just created a job posting.
Analyze the text and determine three questions you would ask a potential candidate.

Desired format:
1.<question>
2.<question>
3.<question>

Text:
```

This will return three questions based on the text provided after the Text: input.

Next we will ask ChatGPT to see if a candidate is a good fit for the questions.

```
You are a hiring manager checking to see if a resume is a good fit for a position given three questions
Analyze the text given the questions to determine if this candidate is qualified. If the text doesn't answer the questions explain.
Text:
<paste in text to check>
Questions:
<paste in questions from previous prompt>
Answer:
```