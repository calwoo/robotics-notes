# AGENTS.md

## Purpose

Maintain study notes for Princeton University's public **ROB 345/549: Introduction to Robotics** course:

- Course page: <https://irom-lab.princeton.edu/intro-to-robotics/>
- Instructor: Anirudha Majumdar
- Current public offering represented here: Fall 2026

This directory is a study companion, not a mirror of the course site. Summarize the public materials in original language; do not reproduce full transcripts, slide decks, assignments, or solutions.

## Source of truth

Before adding or updating notes, inspect the course page's **Course materials** table. Treat it as authoritative for:

- lecture numbering and titles;
- the order of topics;
- links to videos, slides, assignments, and projects; and
- which lectures have actually been released publicly.

Use sources in this priority order:

1. The lecture's official slides and video linked by the course page.
2. The course page and syllabus information exposed there.
3. The course's listed reference texts.
4. Other primary or authoritative sources, only when they materially clarify a point.

Do not infer that an unreleased lecture has occurred merely because it appears in the planned syllabus. Record a lecture as available only when the course page provides public lecture material.

## Directory layout

```text
princeton-intro-robotics/
├── AGENTS.md
├── README.md
├── hardware-buying-guide.md
├── assignments/
│   ├── README.md
│   └── assignment-01/
│       ├── Assignment1.pdf
│       ├── Lab1.ipynb
│       ├── README.md
│       ├── UV_SETUP.md
│       └── env-mae345.yml
└── notes/
    ├── README.md
    ├── assets/
    │   ├── lecture-01/
    │   └── lecture-02/
    ├── lecture-01-intro-to-robotics.md
    └── lecture-02-discrete-motion-planning.md
```

Add future notes as:

```text
notes/lecture-NN-short-kebab-case-title.md
```

Use the lecture number and title shown on the course page. Keep one lecture per file.

## Required note structure

Each lecture note should contain, in this order:

1. Title
2. Metadata block with topic, instructor, course, source links, and access date
3. Lecture at a glance
4. Learning objectives
5. Detailed summary organized by concept
6. Important definitions and notation
7. Algorithms, derivations, or worked examples, when applicable
8. Assumptions, limitations, and common pitfalls
9. Connections to the rest of the course
10. Review questions
11. Compact takeaway

Use equations where they improve precision. Define symbols immediately and keep notation consistent with the lecture. Prefer small tables for exact comparisons.

## Source discipline

- Link the official course page, lecture video, and slide deck at the top of every note.
- Preserve useful citations when transforming or extending existing notes.
- Paraphrase sources. Short labels, equations, and algorithm names may be retained where necessary.
- When adding a slide screenshot, use a selected explanatory figure rather than copying a full deck, and caption it with the slide/PDF page number and the official source link.
- Attribute statements that are specific to the lecture with wording such as "the lecture frames..." or "the slides assume...".
- Label material not explicit in the lecture as **Supplemental clarification**, **Derived observation**, or **Open question**.
- Distinguish the lecture's simplified model from a claim about real robots.
- If slides and video appear to disagree, record the discrepancy rather than silently choosing one.
- Include an `Accessed` date because the public course site may change during the semester.

## Mathematical and algorithmic standards

- State the domain and meaning of each variable.
- State assumptions before conclusions.
- For algorithms, describe the data structure, selection rule, update rule, termination condition, path reconstruction method, and guarantee.
- Do not claim optimality or completeness without stating the conditions under which it holds.
- For configuration spaces, distinguish physical/workspace coordinates from configurations.
- For planning, distinguish geometric feasibility from dynamic feasibility.
- When discussing A*, distinguish admissibility from consistency and explain whether closed nodes may be reopened.

## Updating the course notes

When new public lectures appear:

1. Re-check the course page and capture the official title and links.
2. Read the slides and, where available, review the video for explanations not visible in extracted slide text.
3. Add one note file using the required structure.
4. Add the lecture to `notes/README.md` and the progress table in the root `README.md`.
5. Check links, headings, equations, and filenames.
6. Review the diff for accidental changes outside this directory.

If an existing lecture is revised, update its access date and add a short note under its sources only when the change materially affects the summary.

## Course-work boundaries

- Notes may explain concepts and analyze released course material.
- Do not generate answers for graded assignments unless the user explicitly requests help that is permitted under the current course policy.
- Never present a generated solution as the student's own work.
- The Lecture 1 slides describe a restricted generative-AI policy for enrolled students. Re-check the current syllabus or Canvas policy before helping with assessed work, since policies can change.

## Definition of done

A lecture note is complete when it:

- accurately follows the released lecture;
- is understandable without opening the slides;
- includes all central definitions, equations, algorithms, and examples;
- separates sourced content from added explanation;
- links its primary sources;
- identifies important assumptions and failure modes; and
- is indexed in both README files.
