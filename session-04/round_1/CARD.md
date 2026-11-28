# Round 1

**What you see.** The study report stops with an error and a long stack trace.

```
python session-04/round_1/study_report.py
```

**Your task.** This is the third stack trace tonight, and you read this one on your own. Then fix the report with your assistant.

1. Read the trace from the bottom, and fill in the first three notes below.
2. Paste the whole trace and the code of `study_report.py` to your assistant.
3. Before you change anything, ask yourself: does its diagnosis explain this exact error message?
4. Apply the smallest fix, and run the report again.

**Done when** this prints PASS:

```
python session-04/round_1/check.py
```

## My notes

- The error type (the first word of the last line):ValueError
- The message (the rest of the last line):unconverted data remains
- The last line of the trace that is in my own file (file name and line number):study_report.py, line 23
- The assistant's diagnosis, in one sentence:
- Which words in the error message does that diagnosis explain?
- Did the assistant finish the job, or send me to check something?

## Hints

Try for three minutes before you open one.

<details>
<summary>Hint 1</summary>

The last line of the trace says `ValueError`, and then a message with some characters in it. Where have you seen those characters? Open `study_log.json`.

</details>

<details>
<summary>Hint 2</summary>

Most of the trace is inside Python's own files. Look for the last line that names `study_report.py`. That line is where your code asked for something Python could not do.

</details>

<details>
<summary>Hint 3</summary>

The times in the log include seconds. `TIME_FORMAT` near the top of `study_report.py` does not. Add `:%S` to the end of the format.

</details>
