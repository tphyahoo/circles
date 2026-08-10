# A Finite Route Through School Mathematics

**Draft table of contents.** Seventh grade through single-variable calculus, with a
gesture beyond. Set against the traditional sequence so the divergences are visible.

Nothing here is new mathematics. Sources are credited per volume; the point is the
*order*, not the content.

## At a glance

| | | | |
|---|---|---|---|
| **I** | 7th | Counting Things | tables and the gaps between them — `Δ` and `Σ`, before either has a name |
| **II** | 8th | The Lattice Plane | the county's land: quadrance, circles, π by counting, Pick's rule |
| **III** | 9th | Turning | rotation without angles; polynomials turn out to be difference tables |
| **IV** | 10th | Growth | doubling, `e`, discrete logs, generating functions, recurrences |
| **V** | 11th | Calculus, Finitely | `h` gets smaller and never reaches zero |
| **VI** | 12th | Where the Finite Route Ends | the sums that do not stop, and the length you cannot count |

*Optional:* **an excursion into other finite worlds** — circles drawn over a prime.
Nothing depends on it, which is why it is not a year.

**What it is for.** Computation as the substrate the rest is done with — the way
arithmetic is the substrate now. The graduate specialises afterward and arrives able to
say what a procedure does before running it.

**How a chapter opens.** A do-now on the board before anybody sits down, answerable with
only what earlier chapters gave. Then the day's question is *elicited*, in the students'
words, out of the trouble the do-now has just caused. The needs come from outside the
room: a boundary set, a curve staked, a parcel taxed, a ledger closed.

**How it knows things.** By computing them, and saying so. Every answer arrives with a
receipt — a number and how wrong it can be. Proof is kept where it is short, because it
is cheaper than checking, not because it is holier.

**Where it stands.** Volumes I and II are specified chapter by chapter — do-now, what
goes wrong, elicited aim — with every number in them checked by `docs/verify_vol1.py`
and `docs/verify_vol2.py`. **19 of 58 chapters.** III through VI are titles and
glosses. One lesson has actually been written, from II.6, and it predates the entry it
now sits under.

---

### A standing debt

The nearest existing book is **Graham, Knuth & Patashnik, *Concrete Mathematics* (1989)**,
and this outline should say so on its first page rather than in a footnote. Volumes I,
III, IV and VI are all walking through territory it mapped: the difference operator,
falling factorials, telescoping, summation by parts, generating functions, recurrences.
Read it before writing a word of this.

It also supplies this project's best evidence. *Concrete Mathematics* exists because
Stanford computer science students who had completed calculus could not handle sums and
recurrences, and needed six hundred pages of remediation to get there. That is a
measurement, taken in our world, of the gap this book proposes to close from the other
side — and it is a stronger argument for the book than any claim about whether infinity
is real.

How complete the overlap is, is worth stating plainly rather than gesturing at.
*Concrete Mathematics* covers §2.6 *Finite and Infinite Calculus* — `Δ`, `Σ`, falling
factorials, summation by parts — plus generating functions, recurrences, hypergeometric
summation, and in the second edition the Gosper–Zeilberger mechanical summation
algorithm. That is essentially the whole difference-calculus spine of Volumes I, III, IV
and V, done thoroughly, decades ago.

What it does not do is *stop*. §2.7 is infinite sums; chapter 9 is asymptotics. It uses
finite methods without inhabiting a finite world, and nothing in it arrives with a
receipt. It is the toolkit, not the stance.

And it contains almost no geometry — so the lattice strand here, quadrance and spread
and Pick and the Gauss circle problem, is the part of this book that is genuinely not
borrowed. Which is worth noticing, since it is also the part that produced the
surveying spine and the do-nows that work best.

The difference between the two projects is audience and order. *Concrete Mathematics* is
for people who already have the calculus and need the discrete half; this is for people
who have neither, taking the discrete half first.

---

## What it is for

The substrate is **computation**. Not as a career and not as a subject beside the
others, but as the tool the rest of it is done with — the way arithmetic is the
substrate now.

A graduate specialises afterward, into statistics or physics or algebraic geometry
or building software, and arrives at any of them able to say what a procedure does
before running it, in notation that cannot be read two ways. Very few people in our
world get that at all; the ones who do get it at thirty, at work, badly.

**The claim is not that this is easier.** Nobody knows whether it is, and this
document should not pretend to. The claim is that it is a different vantage, and that
the vantage buys something specific: a student who can implement what a spreadsheet does has taken that much magic out of the world and got a tool back —
the kind of thing that hangs in a garage, which you are allowed to open, and which
turns out to have nothing in it you could not have built.

That is also the honest reason for the formal notation. Not rigour, and not
professional practice. A thing you can read is a thing you can open.

The trade is real and should be stated rather than discovered. **They do not come
out knowing the physics and statistics an honors student here does.** Our sequence
surveys everything and delivers mastery of nothing in particular; this one picks one
thing and delivers it. A reader who wants the survey should buy the survey.

The standing debt above is also the best evidence for the trade. *Concrete
Mathematics* is six hundred pages of remediation, sold to people who already have
the degree, for precisely the gap this proposes to close from the other side.

**What this is not.** It is not "teach kids to code," which every school system has
now attempted, and which produces students who can write a hundred lines of
JavaScript and cannot say what any of it does. The distinction is
computation-as-mathematics against coding-as-vocation, and it is worth restating
because the failure mode is one short hop away: the moment the subject becomes the
apparatus — how to specify, how to make it fast, what a tool is *for* — the
mathematics has stopped moving. Legibility is the whole of what the formal notation
is here to buy. Nothing beyond that is in scope.

A spreadsheet and not a calculator, deliberately. A spreadsheet is a table, the gaps
between its entries, and running totals — which is Volume I, exactly. A calculator is a
different promise: it has a square-root key this book declines, and does sine and
logarithm by methods the book replaces rather than builds. **Floating point is out of
scope on the same grounds as fast algorithms** — it is an answer to *how shall we store
this*, which is engineering. Students may use it freely; the mathematics never asks for
it, because I.2 settles that a fraction is a pair of whole numbers and never a decimal.

---

## How sure, and how you know

The book discovers things by computing them and then says so, rather than working
empirically and dressing the result in deductive clothes afterward. That is the
**Babylonian** habit, as against the Greek one, and it is not a philosophical position
the book argues for — it is just what actually happens when anybody does mathematics,
and this book declines to hide it.

Three consequences, and they are the whole of the epistemology.

**Every answer arrives with a receipt.** Not certainty — a number, and how wrong it can
be. The drawing is never off by more than half a unit. `e` to n places leaves under
`1/(n·n!)`. Counting dots gives π and tells you it overshot by under three. An answer
without a receipt is not finished.

**A proof is a compression of a check, not a higher grade of knowledge.** It is kept
wherever it is short, because it is cheaper — not because it is holier. This is
measurable rather than arguable: model-checking the circle specification clears radius
55 in seconds and was abandoned at radius 89 after **thirty-one minutes**, because the
work grows like `R⁴`. The two-line parity argument settles every radius and costs
nothing, because it never runs.

**And a check is only as good as the case somebody thought to try.** One constant
altered in the fast circle algorithm — 6 into 4, invisible to reading — breaks 114 of
the 118 radii from 3 to 120 and *survives* at 3, 5, 7 and 10, which are exactly the
radii small enough to fit on a board.

There are a great many books that teach mathematics as proof. One that does not is
unlikely to damage anybody's roads.

---

## How this differs, structurally

Four differences do all the work. Everything else follows from them.

**1. Organized by operation, not by object.** The traditional sequence is a tour of
kinds of thing — integers, then linear functions, then quadratics, then polynomials,
then exponentials, then trigonometric functions. This one is a tour of three verbs:
**count**, **difference**, **sum**. The objects arrive as answers to questions about
the verbs. Quadratics aren't a unit; they're *what has a constant second difference*.

**2. Calculus starts in seventh grade.** The difference operator `Δ` is subtracting
adjacent entries in a table. A twelve-year-old can do it on day one. So Volume I
contains the Fundamental Theorem of Calculus — as telescoping, which is a one-line
proof. The traditional sequence defers the same idea by five years because it insists
on limits first.

**3. Sequences are the primary object; functions are secondary.** A function is a table
of values. Traditional books treat sequences as a late Algebra II sidebar, which is
backwards: the table is the thing you can actually hold.

**4. The hard part moves to the end, and shrinks.** Limits and convergence traditionally
gate everything, arriving early and blocking the door. Here they arrive last and only
matter for the cases where refinement genuinely fails — because everything before them
*terminated*.

Two consequences worth flagging: square roots and `π` are late and derived rather than
early and given, and induction — the finitist's proof engine — does the heavy lifting
from Volume I onward instead of appearing once in Algebra II.

What is *unchanged*: order of operations, solving equations, fractions, coordinates,
factoring. The elementary layer is already finite. Nobody needs saving from it.

---

## How a chapter opens

*Piloted on Volume I below. If it holds up there it should be carried through; if it
does not, that is worth knowing before any more of this is written.*

Every chapter opens with a **do now** — a task on the board before anyone sits down,
answerable with only what earlier chapters gave them, needing no instruction and no
teacher. They work it cold. Then the **aim** is not announced but *elicited*: the class
names the day's question out of the trouble the do now has just put them in, and it goes
up in their words and stays up until it is settled.

Two rules, and the second is the harder one.

**A do now may only use what has already been taught.** So a chapter that cannot
produce one is in the wrong place, which makes this a test of the ordering rather than
a decoration on it.

**The need comes from outside the room.** Somebody wants something and cannot have it
yet — not *here is an interesting question*, which is a teacher wanting something and
pretending it is the world. This is Douglas Downing's method in the Carmorra books
(*Calculus the Easy Way*, and *Algebra* in the same setting), where nothing is ever
taught: the kingdom needs something built or measured or predicted, and the mathematics
is what it takes to get it. The difference here is that Downing wraps a conventional
course in a fiction, and this reorders the course itself, so it cannot lean on the
charm the way he can. The need has to be real.

### Where the needs come from

Volume I draws almost all of them from **the county** — its roads, its records, its
land, its money. That was not planned. It is what turned up when each chapter was asked
who wants this, and it is the same county whose roads Popovich's grandfather laid out
with a chain, which suggests the setting was already there and had not been noticed.

Whether that becomes a standing world with recurring people, the way Carmorra is, or
stays a source of jobs that happens to repeat, is a live decision and should be made on
purpose. Galileo appears in chapter five because a real man with a real ramp beats any
invented need, and the two chapters where the county has to be reached for — one and
four — are the weakest openings in the volume, which is worth watching for.

### Two habits, and one rule

Neither habit is a topic, and that is the point — a topic can take over a lesson and a
line at the end of an exercise cannot.

**"…and say how far you checked."** Attached to answers. It is what makes the receipt a
routine rather than a sermon, and it is the whole of the book's rigour policy.

**"…now write it down so it runs without you."** Attached to procedures. It is what
makes a graduate somebody who has *built* things rather than watched them being built,
and it is the only thing that cashes the *implement* half of the claim above. The
implementations are already in the book; what has been missing is that the class watches
somebody else type them.

And the rule, which governs the formal notation wherever it appears:

> **A specification may be shown. It may not be discussed.**

Written on a board, printed on a page, attached to an answer, it costs what it costs and
stops. Turned into a scene — two people talking about why one would write such a thing —
it grows without limit, every time, and the mathematics stops moving while it does. That
is not a guess; it is the one failure this project has had repeatedly, and it has never
once arrived any other way.

The failure mode to watch: nine consecutive ambushes is a lot of ambushes. Some
chapters should be allowed to open with *here is a tool, now use it*, and the method
gets tiring precisely when it is applied without exception.

---

## Volume I — Seventh Grade: Counting Things

*Traditional: ratios and proportions · negative numbers · expressions and equations ·
area, surface area, volume · sampling and probability*

**1. Numbers You Can Point At**
- *Do now:* The county pays a bounty on fence posts. A man arrives with a cartload and
  says there's *about four hundred*. What do you write in the book?
- *What happens:* Nobody will write *about four hundred*, because the book is what he
  gets paid from. So somebody has to count them, and the number that goes in the book
  is a different kind of thing from the number he said — one of them was got by doing
  something, and the other was got by looking.
- *Aim:* **What's wrong with "about"?**

**2. Exact Fractions** — why a fraction is a pair of whole numbers, and never a decimal
- *Do now:* Three brothers inherit a strip a hundred links long, share and share alike.
  Write each brother's share in the deed.
- *What happens:* `33.33` links each, and three of those is `99.99`. A hundredth of a
  link has gone missing and the deed has to say who got it. Write it as the pair
  `100/3` instead and three of them is exactly a hundred, with nothing left over and
  nobody to argue with.
- *Aim:* **Who gets the leftover?**

**3. Tables, and the Gaps Between Their Entries** — `Δ` introduced
- *Do now:* The county has recorded the same figure for six years running:
  `2, 5, 10, 17, 26, 37`. The board meets Thursday and wants next year's.
- *What happens:* Staring at it does not work. The ones who get it subtract each entry
  from the next and get `3, 5, 7, 9, 11`, which anybody can carry on — so the answer is
  50. They did not solve the puzzle. They made a second table and solved that.
- *Aim:* **Why does subtracting help?**

**4. When the Gap Never Changes** — linear, discovered rather than defined
- *Do now:* Four men's pay records, four different arrangements, none of them written
  down anywhere. Which of these men can you tell me next month's figure for?
- *What happens:* Two piles form, and nobody was told there would be two. The
  predictable pile all turn out to be *so much each month, starting from somewhere* —
  which is the definition of a straight line, arrived at from the far side and without
  the word.
- *Aim:* **What have the ones we can predict got in common?**

**5. When the Gap's Gap Never Changes** — quadratics, before the quadratic formula
- *Do now:* Galileo had a ramp, a ball, and a water clock, and no calculus, because
  nobody had any. Here is what he wrote down: `0, 1, 4, 9, 16, 25`. Take the gaps. Then
  take the gaps of those.
- *What happens:* Gaps `1, 3, 5, 7, 9` — the odd numbers, which is the thing he
  published in 1638 and is remembered for. Gaps of gaps: `2, 2, 2, 2`. Constant, one
  floor down. That constant is the acceleration, though nobody says the word yet.
- *Aim:* **The gaps keep changing but their gaps don't. What kind of thing is that?**
- *Why it is here:* the one chapter where no invented need would be better than the
  real one. A man rolled a ball down a plank and wrote the numbers in a column, and the
  column is a difference table. Everything this book does, he did first, with a pen.

**6. Pascal's Triangle Is a Machine**
- *Do now:* The county is laid out in mile squares. A man has to get from the
  courthouse to a farm three miles east and three north, along the roads, never
  doubling back — and he is paid by the route, so the clerk needs to know how many
  there are. Draw them.
- *What happens:* Twenty, and drawing all twenty is miserable. — *Then, once they are
  done and pleased with themselves:* now the farm ten east and ten north. That is
  **184,756**, which at ten seconds a route is three weeks of drawing without sleeping.
  The method is not slow. It is finished as a method. Somebody writes the count at each
  crossroads instead — 121 additions, and it fits in the lesson.
- *Aim:* **Nobody can draw a hundred and eighty thousand of anything. What else is
  there?**
- *Why it is here:* the first place in the book where a way of getting an answer runs
  out rather than merely being tiresome. Drawing routes doubles every time a row is
  added; the table of crossroads grows like `n²`. A twelve-year-old can feel that
  difference with no notation at all, and does not need telling which of the two won.

**7. Sums That Collapse** — `Σ` as the undoing of `Δ`; the Fundamental Theorem, unnamed
- *Do now:* A year of the county ledger: the twelve monthly changes, and nothing else.
  What is the balance in December? The clerk added all twelve and it took him an hour.
  The treasurer looked at two numbers and had it in four seconds.
- *What happens:* On the table `1, 4, 9, 16, 25, 36, 49, 64` the gaps are
  `3, 5, 7, 9, 11, 13, 15`, which add to 63 — and the table runs from 1 to 64.
  Everything in the middle cancelled, and nobody arranged for it to.
- *Aim:* **Why is the total of the changes just the last one take away the first?**

**8. Dots in a Box** — area by counting
- *Do now:* A triangular parcel, staked at every chain, six chains along the road and
  four back. The assessor taxes by the acre. (a) What is its area? (b) How many stakes
  are inside it? Count them.
- *What happens:* The formula says twelve square chains, which is an acre and a fifth.
  The count says seven. Both are done correctly, by people who agree about everything
  else. Twelve stakes sit on the boundary, which is exactly the discrepancy, and nobody
  has yet said what a boundary stake is half of.
- *Aim:* **The formula says twelve and I count seven. Which one do we tax him on?**

**9. Two Rules, One Table** — a procedure is not its answer
- *Do now:* Two clerks were given the same column to fill in. One added two to the line
  above, all the way down. The other worked out each line from its own line number and
  never looked up. The columns came out identical: `1, 3, 5, 7, 9, 11`.
- *What happens:* Both are right and both produced this column, but they are not the
  same instructions. Ask for the hundredth line: the first clerk must grind out the
  ninety-nine before it; the second answers directly. Pascal's crossroads, three
  chapters ago, was the first kind and has no known second kind. The collapsing ledger
  of chapter seven turned a first kind into a second, which is why the treasurer beat
  the clerk.
- *Aim:* **We did different work and got the same column. Did we do the same thing?**
- *Why it is here:* the answer is *no, and yes*, and holding both halves at once is the
  whole of what it means to think about a procedure rather than an answer. Every later
  volume leans on it. When a faster method is deferred with *it gets the same dots*,
  this is the chapter that makes the sentence mean something. Picked up again in V.6,
  recurrences and closed forms.

> *Credits:* Boole (1860) and Jordan (1939) for the difference calculus; Graham, Knuth
> & Patashnik, *Concrete Mathematics* ch. 2, for the modern treatment.

---

## Volume II — Eighth Grade: The Lattice Plane

*Traditional: linear equations · introduction to functions · the Pythagorean theorem ·
transformations and similarity · exponents and scientific notation · systems ·
volume of cones and spheres*

The county again, and now its land. Every need in this volume is somebody's job:
setting a boundary, settling which farm is nearer, filling in a deed, laying out a
bend, taxing a parcel. It is also where a chain stops being a length and becomes an
instrument — a hundred links, counted, and nothing in between them.

> **The old chapters 5 and 6 have become 5, 6 and 7.** Writing the do-nows is what
> forced it. Chapter 5 hands you the spots that land *exactly* on the curve; old
> chapter 6 handed you a fast way to run along one. Neither of them opens on the
> question in the middle — you have to set a stake where no exact spot exists, so how
> wrong may you be? — and that question carries the half-link bound and the proof that
> the rule never gets stuck. A chapter that cannot produce a do-now is in the wrong
> place; here it was a do-now that could not find a chapter.

**1. The Grid Has No Gaps in It**
- *Do now:* A boundary has to be set exactly halfway along a run of seven links. Two
  brothers are watching. Put the stake in.
- *What happens:* Three and a half links, and the chain has no half links. You can
  re-mark the whole chain in half-links, and then the next man wants a quarter, and the
  one after him wants an eighth. Or you say the spot is not there to be marked.
- *Aim:* **Is there a place there or isn't there?**

**2. Quadrance** — squared distance, so no square root ever appears
- *Do now:* Two farms both claim to be nearer the new schoolhouse, and the one that is
  gets the road. One is thirty links east and forty north; the other ten east and
  forty-eight north. There is standing water between, so neither can be chained
  directly. Settle it.
- *What happens:* Squares added: **2,500** against **2,404**. The second is nearer, and
  it is nearer by less than a link — far too close to settle by eye, and nobody had to
  say how far either of them was. One of the two distances is exactly 50; the other is
  a number that does not exist and never had to.
- *Aim:* **Can we say which is nearer without saying how far?**

**3. Pythagoras Without a Square Root**
- *Do now:* Two deeds want a diagonal. One field is 60 links by 80, the other 50 by 50.
  Write both diagonals into the deeds.
- *What happens:* The first squares to **10,000** and comes out at exactly 100, and the
  clerk is happy. The second squares to **5,000** and there is no whole number of links
  that does it — it falls between 70 and 71. Same question, same working, two entirely
  different kinds of answer, and the deed can only be written for one of them.
- *Aim:* **Why did one come out and the other didn't?**

**4. Which Numbers Are Hypotenuses?** — sums of two squares
- *Do now:* The surveyor wants a list he can keep in his pocket: every pair of whole
  legs, twenty links or under, whose diagonal is also whole. Make him the list.
- *What happens:* Seven pairs out of two hundred and ten. `3 4 5`, `5 12 13`, `6 8 10`,
  `8 15 17`, `9 12 15`, `12 16 20`, `15 20 25`. Enormous gaps between them, and no
  pattern anybody can see by staring — which means the list is worth carrying, and also
  that something is deciding which numbers get in.
- *Aim:* **Which ones work, and can you tell without trying?**

**5. A Circle Is a Set of Dots** — the exact ones, and how few there are
- *Do now:* The peg is set. The curve runs ten chains out from it, all the way round.
  Put a stake at every spot exactly ten chains from the peg. Do not measure anything.
- *What happens:* Twelve. Four on the axes and eight from the `6-8-10` of two chapters
  ago, and that is the lot, on the whole county. Twelve stakes is not a road.
- *Aim:* **Twelve stakes isn't a curve. So what is?**

**6. Drawing One** — the nearest rule, and how wrong it is allowed to be
- *Do now:* A curve a thousand links out from the peg. You have to set the stake at
  station 100 and there is no whole-link spot on the curve anywhere near it. Set it
  anyway, and be ready to say in front of the county why you put it there.
- *What happens:* 995 links up misses the curve by **25**; 994 misses by 1,964 and 996
  by 2,016. So 995, and it is not close. But *nearest* is a rule about the other
  candidates, not about the curve, and somebody is going to ask how far off the road
  actually is.
- *Aim:* **How wrong am I allowed to be?**
- *Why it is here:* the half-link bound lives in this chapter, and so does the proof
  that the rule never comes to a tie — the two things that make *nearest* a rule you can
  hand to somebody else rather than a judgement you have to be present for. Half a link
  is four inches, on a curve thirteen hundred feet across.

**7. Drawing One Fast** — the midpoint algorithm
- *Do now:* You are in the field. The book is back at the courthouse, it is going dark,
  and you have just set station 300. Where does 301 go?
- *What happens:* The rule from last chapter wants `301²` and then a search, by hand,
  in the dark, and then the same again for 302. There has to be a way of getting the
  next stake out of the one you just set, and there is: it is all additions, and the
  numbers stay small.
- *Aim:* **Can I get the next stake from the one I just set?**
- *Why it is here:* the fast way, kept in its own chapter and after the slow one on
  purpose. It gets the same stakes — which is I.9's *two rules, one table*, arriving
  where it matters.

**8. Counting Your Way to π** — the Gauss circle problem
- *Do now:* A round parcel, ten chains from peg to edge, staked at every chain. The
  assessor taxes by the acre and has no formula for a round thing that he is willing to
  trust. Count the stakes inside it.
- *What happens:* **317**. And 317 square chains is thirty-one and a bit acres, which
  is the area, near enough to argue about but not near enough to fight over — the true
  figure is 314.16, so counting overshot by under three. Divide the count by the square
  of the radius and you get 3.17, and nobody said the word π.
- *Aim:* **Can you get the area of a round thing just by counting?**

**9. Pick's Theorem** — the area of any lattice polygon, by counting its dots
- *Do now:* A five-cornered parcel, not one corner square, staked at every chain. The
  assessor wants the acreage and will not accept a rule he cannot check himself.
- *What happens:* 29 stakes inside, 14 on the boundary. Half the boundary ones, plus
  all the inside ones, less one: 35 square chains, three and a half acres — and it is
  exact, not near. The boundary stakes counting half is the same half that made the
  triangle in Volume I come out at twelve when the counting said seven.
- *Aim:* **Is there one rule that works for any shape at all?**
- *Why it is here:* it settles I.8, which was left open a year earlier with *which one
  do we tax him on?* That is the longest arc in the book so far, and it should be
  allowed to be that long.

**10. Spread** — turning, measured without trigonometry
- *Do now:* Two roads meet at a bend. The county must record the bend in the book well
  enough that a different man with a different chain can lay it out again next year.
  There is no protractor in the county. Write it down.
- *What happens:* What you have is two directions, each of them so far along and so far
  up — pairs of whole numbers. Whatever *amount of turn* is, it has to be got out of
  those four numbers, because they are all that was measured.
- *Aim:* **How do you write down a bend?**

> *Credits:* Wildberger, *Divine Proportions* (2005), for quadrance and spread.
>
> The circle-drawing algorithm in chapter 7 is the **midpoint circle algorithm**
> (`d = 3 − 2r`). Read the primary source before crediting it: Bresenham's *A Linear
> Algorithm for Incremental Digital Display of Circular Arcs*, CACM 20(2), Feb 1977,
> 100–106, uses a **different** decision variable — evaluated at the diagonal
> neighbour, initialised `2 − 2R`. The two agree on output but are not the same
> procedure, so the near-universal name "Bresenham's circle algorithm" for the `3 − 2r`
> form is a misattribution. (And the famous 1965 IBM Systems Journal paper draws lines,
> not circles.) Also: Gauss for the circle problem; Fermat and Jacobi for two squares;
> Pick (1899).

---

## Volume III — Ninth Grade: Turning

*Traditional Algebra I: linear, quadratic and exponential functions · factoring ·
polynomials · radicals · systems of equations*

1. Turning Without Angles
2. The Rotation Rule — `(a,b) ⋆ (u,v) = (au − bv, av + bu)`
3. You Cannot Get Off the Circle — closure, and why it's a group
4. Exact Turns — Pythagorean triples as rotations that land perfectly
5. Every Exact Turn There Is — the rational parametrization
   `((1−t²)/(1+t²), 2t/(1+t²))`, which emits the triples of Volume II on demand
6. The Spread Laws — the rational replacements for the sine and cosine rules
7. Spread Polynomials — multiple turns are *polynomials* in a single turn, so
   `cos nθ` is algebra rather than analysis (Chebyshev's polynomials, in disguise)
8. Polynomials Are Difference Tables
9. The Right Kind of Power — falling factorials, and the return of `Δx⁽ⁿ⁾ = n·x⁽ⁿ⁻¹⁾`
10. Newton's Series — every polynomial rebuilt from its differences at zero, in
    finitely many terms, exactly

> *Chapter 7 is the book's hinge.* The familiar power rule visibly **fails** on ordinary
> powers (`Δx² ≠ 2x`), and then comes back perfect on the right basis. Break it, then
> fix it.

> *Credits:* Chapters 6–8 are *Concrete Mathematics* ch. 2 and 5, reordered for a reader
> who has not met calculus. The falling-factorial notation and its treatment are theirs.
> Wildberger (2005) for chapters 1–5.

---

## Volume IV — Tenth Grade: Growth

*Traditional Algebra II / Precalculus: polynomial and rational functions · exponentials
and logarithms · sequences and series · trigonometric functions · conics · matrices ·
vectors*

1. Counting Them All at Once — induction, arriving as a labour-saving device rather
   than a proof engine: a check you do not have to run because you already ran the
   general one
2. Doubling — `Δ2ˣ = 2ˣ`, so **2** is this world's `e`
3. Every Other Base — `Δbˣ = (b − 1)bˣ`, and why 2 is the only fixed point
4. Letters in the Wrong Envelopes — `n` letters, `n` envelopes, nobody gets their own.
   Count the ways; `n!/Dₙ` marches to **e**. The same trick that gave us π, on a
   different pile of things to count
5. e, to as Many Digits as You Ask For — partial sums of `1/k!` are exact fractions
   and the leftover is smaller than `1/(n·n!)`, so every answer arrives with a receipt
6. Undoing Growth — discrete logarithms
7. Summation by Parts
8. Generating Functions — power series with no convergence question, because nothing
   is ever evaluated
9. Recurrences and Closed Forms
10. Tables With Two Indices — matrices as bookkeeping
11. Conics on a Lattice

> *Credits:* Chapters 7–9 are *Concrete Mathematics* ch. 7 and 8 — generating functions
> and recurrences — at a slower pace. Chapter 8 is the one place this book gets something
> for free that the continuous route pays dearly for: a generating function is never
> evaluated, so convergence never arises.

---

## Volume V — Eleventh Grade: Calculus, Finitely

*Traditional AP Calculus AB/BC: limits and continuity · derivatives and applications ·
integrals · the Fundamental Theorem · series · parametric and polar (BC)*

1. The Tolerance Game — you name the error you'll accept, I hand you the `N`. A
   procedure, introduced as a game, not a mystery
2. Refining the Grid — `h` gets smaller; it never "reaches" zero
3. The Difference Quotient
4. When Refinement Settles Down, and When It Doesn't
5. Sums Become Integrals
6. The Fundamental Theorem, Twice — the telescoping version you proved in Volume I,
   and the continuous shadow it casts
7. Taylor From Newton — the series that used to stop, and what breaks when it doesn't
8. Where We Must Borrow — the intermediate value theorem fails constructively; here is
   the weaker true thing, and here is what it costs

> *Credits:* Bishop, *Foundations of Constructive Analysis* (1967), for chapters 4 and
> 8; Weihrauch, *Computable Analysis* (2000), for the tolerance game.

---

## Coda — A Gesture at More Variables

Not a course. Four chapters to show the machinery keeps working.

1. Grids in Three Dimensions
2. Partial Differences
3. Volume by Counting — double sums
4. Green's Theorem Is Bookkeeping — the discrete version, where it's an accounting
   identity rather than a theorem

> Note on scope: AP Calculus BC is still **single-variable** — its extra material is
> series, parametric and polar. Genuinely multivariable work is post-AP. This coda is
> a flourish, and should be labelled as one.

---

## Volume VI — Twelfth Grade: Where the Finite Route Ends

**This is where the book pays for its method.** Three drafts got it wrong in three
different ways, and the errors are worth keeping because each one was a plausible
mistake about what the volume is.

The first called it an appendix, on the assumption that a finite reader needs only new
notation. False: seven of the ten chapters below are mathematics this book has not done
at all.

The second gave it the right size and left it outside the grades, so a reader who
followed the sequence met it in whatever time was left over.

The third — this one — gave it the year and then justified the year by the examination,
which made it **the only volume in the book whose customer is an institution.**
Everywhere else somebody wants something: a boundary set, a curve staked, a parcel
taxed, a ledger closed. *The College Board wants it* is not a need, and a do-now cannot
be written from one.

What it is actually for: **the finite route does not reach everywhere, and this is where
it stops.** A sum that does not terminate. A difference quotient that never settles, no
matter how far you refine. And a length you cannot get by counting — because a chain
measures chords and has never once measured an arc, which is why radian measure exists
and why it is the one place in this book where the continuum is unavoidable rather than
merely conventional.

That job — saying out loud what the approach cannot do — used to belong to the old
Volume IV, whose note read *"this is where the book earns trust; a curriculum that only
shows its wins is the thing we're replacing."* When that volume became an excursion the
job was left vacant, and this volume had been doing it anyway without being told.

The notation of the examination comes along for free, because it is the notation the
mathematics is written in. But it is a by-product, and it is not the reason.

### What comes free — the same idea, renamed

| This book | The usual notation |
|---|---|
| `Δf` | `f′` |
| `Σ` | `∫` |
| telescoping | the Fundamental Theorem |
| finite sums | Riemann sums |
| summation by parts | integration by parts |
| difference equations | Euler's method, slope fields |
| the tolerance game | `ε`–`N` |
| quadrance `Q` | `d²` |
| spread `s` | `sin²θ` |

On this half the reader arrives **ahead** of a traditional student. Riemann sums and
Euler's method are what they have been doing since Volume I.

### What must be relearned — same concept, different shape

1. The Power Rule Again — `Δx⁽ⁿ⁾ = n·x⁽ⁿ⁻¹⁾` becomes `d/dx xⁿ = n·xⁿ⁻¹`; the basis
   changes back
2. The Product Rule Loses Its Shift — discretely it is `Δf·g(x+1) + f·Δg`, which is
   *not* symmetric; continuously the shift vanishes and it is
3. Quotients, and Why They Were Ugly Before

### What is genuinely missing — new machinery

An earlier draft listed `e` and the trigonometric functions here. That was wrong, and
the mistake is instructive enough to keep in the book. **The objects are all reachable
finitely.** `e` is a counting problem about envelopes; sine and cosine are the rational
parametrization of the circle, the spread polynomials, and the rotation group, all of
them exact. What needs the limit is not the objects but the *differential relationships
between them*.

4. The Chain Rule — there is no clean general discrete analogue, so this is built from
   scratch. It is also the most-used tool on the exam.
5. Radians, and Why the Angle Had to Change — `d/dx sin x = cos x` is false in degrees
   and true in radians, and radian measure is defined by arc length. This is the one
   place the continuum is genuinely unavoidable, and it is worth dwelling on
6. Why the Natural Base Moved — it was 2 for `Δ`, it is `e` for `d/dx`. Same question,
   different operator, different answer
7. Logarithms of the Continuous Kind
8. Limits of Functions — one-sided, at infinity, L'Hôpital
9. **Series That Do Not Stop** — the longest chapter in the book, and the only really
   large gap. Everything until now terminated. Convergence tests, radius of
   convergence, and why Newton's series became Taylor's problem
10. Continuity and the Intermediate Value Theorem — the classical statement, the
    constructive one from VI.8, and an honest account of the difference

> **Honest accounting.** A reader finishing Volume VI arrives already owning `π`, `e`,
> sine and cosine as *objects*, with the structural half of calculus unusually solid.
> What they lack is the differential calculus of those objects, and convergence.
> Chapter 9 is the real work; the rest is smaller than it looks.

---

## An excursion — Other Finite Worlds

*Optional. Nothing later depends on it, which is exactly why it is here rather than in
the sequence.*

This was Volume IV, a required tenth-grade year, and it is where this whole project
started: circles drawn over a prime instead of over a lattice. It came out of the
sequence for three reasons, none of them about its quality.

Nothing needs it. Volumes IV, V and VI refer to induction, modular arithmetic,
equidistribution and finite fields exactly **zero** times between them. It is a
cul-de-sac — a beautiful one, and a whole year is a great deal to spend in one.

Its first two chapters were the book's only Greek chapters. *Induction — the only proof
engine we need* and *Why Collapsing Sums Always Collapse* exist to prove things the book
has been using contentedly since Volume I. That is the rigour-for-its-own-sake the rest
of this document declines.

And it was the one volume with no customer. Every other opens on somebody who wants
something: a boundary set, a curve staked, a parcel taxed, a balance predicted. Nobody
anywhere wants the remainder of something modulo seven, and a do-now cannot be written
for a need that does not exist.

1. Clock Arithmetic
2. Circles on a Clock — `p − 1` points, or `p + 1`, and why `−1` decides
3. Why That Circle Doesn't Look Like a Circle — equidistribution, honestly
4. Two Finite Worlds — a quotient is not an approximation
5. Quadrance and Spread Over Any Field — the same formulas, on a clock

> Chapter 4 is the one worth rescuing whatever happens to the rest. Reduction modulo a
> prime is a *quotient*, not an approximation — `ℤ/p` has no order and no metric, so a
> circle there is not a coarse circle, it is a different object wearing the same
> equation. Getting that wrong is what started this project, and the correction is
> worth more than the excursion around it.

*Credits:* Gauss; Fermat and Jacobi for two squares; Wildberger (2005) for quadrance and
spread over a general field.

---

## Probably not going to need this

Good ideas, parked. Kept so they do not have to be worked out twice.

**A named setting.** The county that supplies the Volume I and II do-nows could be
named, and *Finney County* was the candidate — it carries four things at once:
**finite**; **Mrs. Feeney**, who already teaches the one lesson that exists; a **real
county in western Kansas** laid out on the Public Land Survey grid, townships six miles
square and roads running on section lines, so the lattice is the actual place; and
**Hal Finney**, who spent a career in finite fields. Not needed yet and possibly never.
If a setting does get invented it should be more fantastical than a plain American
county — closer to Downing's Carmorra — while keeping the survey feel the do-nows have
grown on their own.

The candidate for that is **Finney County, in the land of Lamportia**, and the nesting
is what makes it work: a made-up country containing an entirely ordinary county gets
both halves, since the mathematics still happens at a courthouse with a chain while the
map it sits on can be as silly as it likes. The joke is also the right one for this book
— a magical mystical land named for the man whose whole position is that you should say
exactly what a thing is before building it. TLA+ is his, and is already the notation in
the one lesson that exists; so is LaTeX, which the book would be set in; and IV.3 is
*Clock Arithmetic*, which is an accident.

Mrs. Feeney keeps her spelling in the meantime; nothing turns on it.

**A dedication.** To Hal Finney (1956–2014), who worked in finite fields. Volumes IV
and V teach the mathematics his work rested on: clock arithmetic, counting the points on
a curve over a prime, and the discrete logarithm. Named for that and nothing else —
everything he built has an argument attached to it, and this book is not carrying any of
them. Anyone who knows, knows. Only if the book is finished.

**A chapter on checking versus proving.** The material is unusually good and verified:
one constant changed in the fast circle algorithm, invisible to reading, breaking 114 of
118 radii and surviving at exactly the four small enough to fit on a board; against a
two-line parity argument that settles all of them. Deferred, for two reasons. It depends
on the fast algorithm, which is the chapter this project has been least willing to
commit to — a bad foundation. And it cashes nothing: the two exercise habits deliver the
promise, and this would deliver a philosophical point. The distinction already lands for
free in II.6, in two lines, in a chapter that exists for other reasons. Numbers are on
record in `site/CircleCheck.tla`; the prose there is not itself checked by anything, so
it will rot if the specification moves again.

**Whether anything ever gets specified, or run.** *Program*, *specification*, *code*
and *implement* appear **zero** times across all seven volumes' chapter listings. What
the book does have is the idea underneath — I.9's *two rules, one table*, I.6's *the
method is finished as a method*, II.7's *it gets the same stakes* — without ever asking
a student to write down what a procedure should do before doing it. The one written
lesson does the whole thing already: a blueprint in TLA+, a program that obeys it, and a
figure that is that program's output. Two questions, both open: whether this becomes a
strand or is merely named where it already happens; and — a correctness matter rather
than an idea — that *What it is for* currently promises a graduate who can "implement
what a spreadsheet does" and "say what a procedure does before running
it", neither of which any chapter delivers.

---

## Known weak joints

Stated up front so a prototype can attack them first.

- **The excursion is untested as an excursion.** It was written as a required year and
  has been demoted to an optional one. Nobody has checked that it still reads as
  optional — whether it stands alone without the tenth-grade scaffolding around it, or
  whether pulling it out of the sequence left dangling references in its own chapters.
- **Chapter II.10 and the whole spread strand.** Reviewers of *Divine Proportions*
  granted its coherence but questioned whether quadrance and spread are actually
  *easier* for ordinary students. That objection lands on a claim this book does not
  make — see *What it is for*. What has to be tested is narrower and harder: not
  whether spread is easier than sine, but whether a student who has **only** ever had
  spread can do ninth-grade work with it. If the strand cannot carry Volume III on its
  own, the sequence breaks here first, which is why this is still the first chapter to
  write and test rather than the last.
- **Radian measure** is the single genuinely unavoidable appeal to the continuum. Every
  other apparent obstacle turned out to be reachable by counting or by algebra; this one
  did not. `π` and `e` as *numbers* are fine — they are procedures with error
  certificates. It is `d/dx sin x = cos x`, which needs arc length, that has no finite
  route.
- **Convergence.** The one large gap, and the whole of VI.9. Everything in Volumes I–VI
  terminates, which is the book's chief pleasure and also why its reader meets an
  infinite series for the first time in the last hundred pages.
- **Volume VI carries two jobs and may not survive both.** It is where the method's
  boundary gets drawn honestly — convergence, arc length, the chain rule — and it is
  also, incidentally, where a reader picks up the notation the examination is written
  in. Those coincide, which is lucky rather than designed. If they ever pull apart, the
  boundary is the one that matters and the notation is the one that will get demanded.
  The whole book funnels through this volume, so nothing upstream saves it if it fails.
