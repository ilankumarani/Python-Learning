# Python Roadmap (Slow & Steady) — 2 hours/day (Java/Spring Boot friendly)

Use this as a **daily checklist**. Tick items as you finish them.

## How to use (daily rhythm — 2 hours)
- **25 min**: read/notes (write 5 bullets)
- **75 min**: coding (hands-on)
- **20 min**: review (refactor/tests) + **git commit**

## Weekly rhythm (repeat every week)
- **Mon:** core concepts + tiny exercises  
- **Tue:** go deeper + edge cases  
- **Wed:** patterns + refactor  
- **Thu:** apply to a small module  
- **Fri:** tests + typing + cleanup  
- **Sat:** mini-project feature (visible output)  
- **Sun:** review + README + recap questions  

---

# Week 1 — Setup + workflow + basics

## Monday
- [ ] Install Python 3.12+
- [ ] Set up `uv` (or `python -m venv .venv`) and activate venv
- [ ] Configure VS Code (Python extension, interpreter selection)
- [ ] Learn how to run: `python file.py` and `python -m package`
- [ ] Create `hello_cli.py` that prints args + Python version
- [ ] Create Git repo + first commit

## Tuesday
- [ ] Create project layout (suggested):
  - [ ] `src/`
  - [ ] `tests/`
  - [ ] `README.md`
  - [ ] `.gitignore`
- [ ] Create package `app/` with `__init__.py`
- [ ] Add `__main__.py` so you can run `python -m app`
- [ ] Replace prints with `logging` (basic config)
- [ ] Commit

## Wednesday
- [ ] Learn VS Code debugging (breakpoints, step over/into, variables view)
- [ ] Write + debug 10 tiny snippets:
  - [ ] string slicing
  - [ ] dict access
  - [ ] loop with `enumerate`
  - [ ] function calls + stack trace understanding
  - [ ] basic exception raise/catch
- [ ] Write 5 bullet notes: “what debugger showed me”
- [ ] Commit

## Thursday
- [ ] Learn `pathlib.Path` basics
- [ ] Read a `.txt` file and compute:
  - [ ] line count
  - [ ] word count
  - [ ] top 10 words
- [ ] Handle file-not-found (nice error message, no crash)
- [ ] Commit

## Friday
- [ ] Install + configure:
  - [ ] `ruff`
  - [ ] `black`
  - [ ] `pytest`
- [ ] Run `ruff` and fix issues
- [ ] Run `black` and format code
- [ ] Write at least 2 pytest tests for your file stats functions
- [ ] Commit

## Saturday (Mini-project)
- [ ] Build **Text Stats CLI**
  - [ ] Input: file path
  - [ ] Output: JSON stats (counts + top words)
  - [ ] Add `--top N` option
  - [ ] Add logging for success/failure
- [ ] Commit

## Sunday (Review)
- [ ] Write/expand README with:
  - [ ] setup
  - [ ] how to run
  - [ ] sample output
- [ ] Refactor: simplify names, remove duplication
- [ ] Write a short “Week 1 recap” section (10 bullet points)
- [ ] Tag release `v0.1` (optional)

---

# Week 2 — Data types + control flow (deep)

## Monday
- [ ] Learn: numbers, booleans, `None`, comparisons, truthy/falsy
- [ ] Code 15 exercises:
  - [ ] even/odd
  - [ ] range checks
  - [ ] safe division (handle zero)
- [ ] Commit

## Tuesday
- [ ] Learn strings deeply (split/join, strip, replace, startswith/endswith)
- [ ] Build `normalize_text(s)`:
  - [ ] trim
  - [ ] lower
  - [ ] collapse multiple spaces
- [ ] Add 6 tests for `normalize_text`
- [ ] Commit

## Wednesday
- [ ] Learn clean `if/elif` patterns + guard clauses
- [ ] Refactor earlier code using guard clauses (reduce nesting)
- [ ] Add 3 “bad input” tests (empty string, None handling strategy, etc.)
- [ ] Commit

## Thursday
- [ ] Learn: loops + `range`, `enumerate`, `zip`
- [ ] Rewrite 10 exercises using `enumerate`/`zip` (no index loops)
- [ ] Add 5 tests
- [ ] Commit

## Friday
- [ ] Learn safe parsing patterns (control flow + exceptions lightly)
- [ ] Implement:
  - [ ] `parse_int(s) -> int | None`
  - [ ] `parse_float(s) -> float | None`
  - [ ] `parse_date(s) -> date | None` (basic, choose 1 format)
- [ ] Parametrized tests for all parsing functions
- [ ] Commit

## Saturday (Mini-project)
- [ ] Build **CSV Cleaner**
  - [ ] Read CSV
  - [ ] Clean/normalize 2–3 columns (trim, case, missing values)
  - [ ] Output cleaned CSV
  - [ ] Warn on invalid rows (do not crash)
- [ ] Commit

## Sunday (Review)
- [ ] Make a “control flow cheat sheet” (guard clauses, loops, truthiness)
- [ ] 1-hour no-notes challenge: implement a mini cleaner again from scratch
- [ ] Note weak points for Week 3
- [ ] Commit

---

# Week 3 — Collections mastery (list/dict/set)

## Monday (Lists)
- [ ] Learn: list operations, slicing, copying vs aliasing
- [ ] Code 20 list exercises
- [ ] Write 5 tests for list utilities
- [ ] Commit

## Tuesday (Dicts)
- [ ] Learn dict patterns: `.get`, `.setdefault`, `collections.Counter`
- [ ] Build:
  - [ ] frequency counter
  - [ ] group-by function (e.g., group words by first letter)
- [ ] Tests for both
- [ ] Commit

## Wednesday (Sets)
- [ ] Learn: union/intersection/difference
- [ ] Build:
  - [ ] dedupe function
  - [ ] “unique users” calculator from list of ids
- [ ] Tests + basic performance note (set membership O(1) idea)
- [ ] Commit

## Thursday (Sorting)
- [ ] Learn: `sorted` vs `.sort`, `key=` functions, multi-key sort
- [ ] Sort list of dicts by:
  - [ ] primary key
  - [ ] secondary key
- [ ] Tests for sort behavior
- [ ] Commit

## Friday (Comprehensions)
- [ ] Learn readability rules for comprehensions
- [ ] Refactor 5 loops → comprehensions (only when clearer)
- [ ] Ensure tests still pass
- [ ] Commit

## Saturday (Mini-project)
- [ ] Build **Log Analyzer v2**
  - [ ] Input: plain text log lines
  - [ ] Output: counts by level/user/action
  - [ ] Support filtering (e.g., `--level ERROR`)
  - [ ] (Stretch) Support JSON logs
- [ ] Commit

## Sunday (Review)
- [ ] Create a “collections cookbook” markdown file with examples
- [ ] 30-min speed recap: implement 5 patterns from memory
- [ ] Clean up repo structure
- [ ] Commit

---

# Week 4 — Functions + design (engineer mindset)

## Monday (Function basics)
- [ ] Learn: signatures, docstrings, return types
- [ ] Write 5 utility functions with docstrings
- [ ] Add tests for each
- [ ] Commit

## Tuesday (`*args/**kwargs`)
- [ ] Learn: `*args`, `**kwargs`, keyword-only args
- [ ] Build a config function with keyword-only parameters
- [ ] Add tests for “wrong usage” (TypeError expected)
- [ ] Commit

## Wednesday (Scope + purity)
- [ ] Learn: scope rules, pure vs impure functions
- [ ] Refactor one module to be mostly pure functions
- [ ] “Dependency injection” style: pass dependencies as arguments
- [ ] Commit

## Thursday (Composition)
- [ ] Learn composing functions into pipelines
- [ ] Create a small package module with clear API
- [ ] Add `__init__.py` exports for clean imports
- [ ] Commit

## Friday (Testing deeper)
- [ ] Add 20+ tests (edge cases + parametrization)
- [ ] Add one property-like test idea (not required to use hypothesis)
- [ ] Run coverage and push to ~80%+ for this module
- [ ] Commit

## Saturday (Mini-project)
- [ ] Build **Mini ETL**
  - [ ] read data (CSV/JSON)
  - [ ] transform (normalize + compute derived fields)
  - [ ] write output (CSV/JSON)
  - [ ] add `--dry-run`
  - [ ] add logging
- [ ] Commit

## Sunday (Review)
- [ ] Write: “Functions patterns I learned” (like Java service methods)
- [ ] Cleanup + tag release `v0.2` (optional)
- [ ] Plan Week 5 by listing what felt hard
- [ ] Commit

---

# Weeks 5–24 (high-level checklist — detailed daily plans can be added next)
> When you’re ready, tell me “generate daily plan for Week 5–8” and I’ll extend this README with the same level of detail.

## Week 5: Exceptions + debugging mindset
- [ ] Build robust error handling + custom exceptions
- [ ] Tracebacks, defensive parsing, failure modes

## Week 6: Modules/packages + standard library deep dive
- [ ] pathlib/datetime/json/csv/collections/itertools deeper usage

## Week 7: OOP in Python (vs Java)
- [ ] classes, composition, dunder methods, properties

## Week 8: Dataclasses + patterns
- [ ] dataclass patterns, immutability, value objects

## Week 9: Iterators/generators + context managers
- [ ] streaming pipelines, resource safety

## Week 10: Typing (slow + practical)
- [ ] Optional/Union/generics/Protocols (practical usage)

## Week 11: Testing (advanced)
- [ ] fixtures, mocking, integration tests

## Week 12: Tooling + logging + config + template repo
- [ ] pre-commit, ruff/black, logging strategy, settings

## Weeks 13–16: HTTP + async + threads/process + packaging
- [ ] build a reliable API client + async fetcher + CLI tool

## Weeks 17–22: Backend (FastAPI + DB + Auth + Docker)
- [ ] FastAPI CRUD
- [ ] Postgres + SQLAlchemy + Alembic
- [ ] JWT auth + RBAC
- [ ] Docker + production readiness

## Weeks 23–24: Capstone project (portfolio)
- [ ] Build + test + document + dockerize + polish

---

## Notes (your personal learning log)
- **Week 1 notes:**  
- **Week 2 notes:**  
- **Week 3 notes:**  
- **Week 4 notes:**  
