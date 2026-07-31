import base64, pathlib

HERE = pathlib.Path(__file__).resolve().parent
S = HERE / 'plates'

def img(n):
    return 'data:image/png;base64,' + base64.b64encode((S / n).read_bytes()).decode()

DOC1 = r"""<title>Honors Math, Period 3 — Day One: Circles</title>
<style>
  :root {
    --pad:      #EDF0F2;
    --pad-2:    #E3E9ED;
    --rule:     #C9D6DE;
    --rule-fine:#DCE5EA;
    --ink:      #16222B;
    --blue:     #1D5C8F;
    --gold:     #9A6B12;
    --muted:    #667680;
    --plate:    #0D1117;
    --serif: Charter, "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
    --sans: system-ui, "Avenir Next", "Segoe UI", Helvetica, Arial, sans-serif;
    --mono: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --pad:#0F1419; --pad-2:#161C22; --rule:#232C34; --rule-fine:#1A2128;
      --ink:#DCE3E8; --blue:#6FA8FF; --gold:#E3B341; --muted:#7E8C96;
    }
  }
  :root[data-theme="dark"] {
    --pad:#0F1419; --pad-2:#161C22; --rule:#232C34; --rule-fine:#1A2128;
    --ink:#DCE3E8; --blue:#6FA8FF; --gold:#E3B341; --muted:#7E8C96;
  }
  :root[data-theme="light"] {
    --pad:#EDF0F2; --pad-2:#E3E9ED; --rule:#C9D6DE; --rule-fine:#DCE5EA;
    --ink:#16222B; --blue:#1D5C8F; --gold:#9A6B12; --muted:#667680;
  }

  body {
    margin: 0;
    padding: 0 1.5rem 6rem;
    background-color: var(--pad);
    background-image:
      repeating-linear-gradient(to right,  var(--rule-fine) 0 1px, transparent 1px 28px),
      repeating-linear-gradient(to bottom, var(--rule-fine) 0 1px, transparent 1px 28px);
    color: var(--ink);
    font-family: var(--serif);
    font-size: 17px;
    line-height: 1.64;
    -webkit-font-smoothing: antialiased;
  }
  .pad {
    max-width: 60rem; margin: 0 auto;
    background: var(--pad);
    box-shadow: 0 0 0 1px var(--rule);
    padding: 0 clamp(1.2rem, 4vw, 3.5rem);
  }

  /* ---- header ---- */
  header.top { padding: 3.2rem 0 1.4rem; border-bottom: 3px double var(--rule); }
  .course {
    font-family: var(--sans); font-size: .72rem; font-weight: 600;
    letter-spacing: .16em; text-transform: uppercase; color: var(--blue);
    margin: 0 0 1.4rem;
  }
  header.top h1 {
    font-family: var(--serif); font-weight: 600;
    font-size: clamp(2.1rem, 6vw, 3.2rem); line-height: 1.06;
    letter-spacing: -.02em; margin: 0 0 1rem; text-wrap: balance;
  }
  header.top h1 em { font-style: italic; color: var(--blue); }
  .standfirst {
    font-size: 1.02rem; color: var(--muted); max-width: 38rem; margin: 0 0 .6rem;
  }

  /* ---- cast ---- */
  .cast { padding: 2rem 0 2.2rem; border-bottom: 1px solid var(--rule); margin-bottom: 3rem; display: grid; gap: 1rem; }
  .cast-row { display: grid; grid-template-columns: 9rem 1fr; gap: 0 2rem; }
  .cast-name {
    font-family: var(--sans); font-size: .74rem; font-weight: 600;
    letter-spacing: .1em; text-transform: uppercase; color: var(--blue); padding-top: .3em;
  }
  .cast-desc { font-size: .95rem; max-width: 44rem; }

  /* ---- sections ---- */
  section { margin: 0 0 3.6rem; }
  h2 {
    font-family: var(--sans); font-size: .76rem; font-weight: 700;
    letter-spacing: .15em; text-transform: uppercase; color: var(--ink);
    margin: 0 0 2rem; padding-bottom: .65rem; border-bottom: 1px solid var(--rule);
    display: flex; gap: 1.1rem; align-items: baseline;
  }
  h2 .n { color: var(--blue); font-family: var(--mono); font-variant-numeric: tabular-nums; }

  /* ---- dialogue ---- */
  .line { display: grid; grid-template-columns: 9rem 1fr; gap: 0 2rem; margin-bottom: 1.1rem; }
  .who {
    font-family: var(--sans); font-size: .74rem; font-weight: 600;
    letter-spacing: .1em; text-transform: uppercase; color: var(--blue); padding-top: .36em;
  }
  .who.f { color: var(--ink); }
  .who.p { color: var(--muted); }
  .who.n { color: var(--gold); }
  .says { max-width: 39rem; }
  .says p { margin: 0 0 .8rem; }
  .says p:last-child { margin-bottom: 0; }
  .stage { color: var(--muted); font-style: italic; }
  .beat { grid-column: 2; color: var(--muted); font-style: italic; font-size: .93rem; margin: 1.3rem 0 1.4rem; max-width: 39rem; }
  code, .m { font-family: var(--mono); font-size: .92em; }

  /* ---- emphasis: gold means it lands exactly ---- */
  .exact { color: var(--gold); font-weight: 600; }
  .keybox {
    grid-column: 2; max-width: 39rem; margin: 1.5rem 0 1.7rem;
    border-left: 3px solid var(--gold); padding: 1rem 1.3rem;
    background: color-mix(in srgb, var(--gold) 8%, transparent);
  }
  .keybox p { margin: 0; }
  .keybox .lbl {
    font-family: var(--sans); font-size: .66rem; font-weight: 700; letter-spacing: .13em;
    text-transform: uppercase; color: var(--gold); display: block; margin-bottom: .4rem;
  }

  /* ---- code on the board / on a screen ---- */
  .code { grid-column: 2; max-width: 39rem; margin: 1.4rem 0 1.7rem; }
  .code .attrib {
    display: block; font-family: var(--sans); font-size: .64rem; font-weight: 700;
    letter-spacing: .13em; text-transform: uppercase; color: var(--muted); margin-bottom: .45rem;
  }
  .code pre {
    margin: 0; background: var(--plate); border: 1px solid var(--rule);
    padding: 1rem 1.15rem; overflow-x: auto;
    font-family: var(--mono); font-size: .8rem; line-height: 1.62; color: #C9D1D9;
  }
  .code.spec pre {
    background: var(--pad-2); color: var(--ink);
    border: 1px solid var(--rule); border-left: 3px solid var(--gold);
  }
  .code.spec .kw { color: var(--correction, #A3392B); }
  .code.spec .cm { color: var(--muted); }
  .code .kw { color: #FF7B72; }
  .code .cm { color: #8B949E; font-style: italic; }
  .code .st { color: #79C0FF; }
  .out {
    grid-column: 2; max-width: 39rem; margin: -.9rem 0 1.7rem;
    font-family: var(--mono); font-size: .78rem; color: var(--muted);
    border-left: 2px solid var(--rule); padding: .5rem 0 .5rem 1rem;
  }

  .eq {
    grid-column: 2; font-family: var(--mono); font-size: .92rem;
    background: var(--pad-2); border-left: 3px solid var(--blue);
    padding: .9rem 1.2rem; margin: 1.2rem 0; max-width: 39rem; overflow-x: auto;
  }

  /* ---- tables ---- */
  .tablewrap { grid-column: 2; overflow-x: auto; margin: 1.5rem 0 1.7rem; max-width: 42rem; }
  table { border-collapse: collapse; width: 100%; font-family: var(--mono); font-size: .79rem; }
  th, td { text-align: left; padding: .5rem 1rem .5rem 0; border-bottom: 1px solid var(--rule); font-variant-numeric: tabular-nums; white-space: nowrap; }
  th { font-family: var(--sans); font-size: .64rem; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); font-weight: 700; border-bottom: 2px solid var(--ink); }
  td.g { color: var(--gold); font-weight: 600; }
  td.b { color: var(--blue); }

  /* ---- plates ---- */
  figure { margin: 2.5rem 0; }
  .plate { background: var(--plate); border: 1px solid var(--rule); padding: .7rem; }
  .plate img { width: 100%; height: auto; display: block; }
  /* the board is a whiteboard: it stays light whatever theme the reader is in */
  .boardshot { background: #F8F7F3; border: 1px solid var(--rule); padding: .5rem; }
  .boardshot img { width: 100%; height: auto; display: block; }
  figcaption .pn.hand { color: var(--gold); }
  figcaption {
    font-family: var(--sans); font-size: .78rem; line-height: 1.6; color: var(--muted);
    margin-top: .8rem; display: grid; grid-template-columns: 7.5rem 1fr; gap: 0 1.2rem;
  }
  figcaption .pn { font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: var(--blue); font-size: .68rem; padding-top: .12em; }
  figcaption .pt { max-width: 39rem; }

  /* ---- homework ---- */
  .hw { border: 2px solid var(--ink); background: var(--pad-2); padding: 1.7rem 1.9rem; margin: 2.3rem 0; }
  .hw h3 { font-family: var(--sans); font-size: .72rem; font-weight: 700; letter-spacing: .15em; text-transform: uppercase; color: var(--blue); margin: 0 0 1.2rem; }
  .hw ol { margin: 0; padding-left: 1.3rem; display: grid; gap: .9rem; }
  .hw li { max-width: 39rem; padding-left: .3rem; }

  footer.colo { border-top: 3px double var(--rule); margin-top: 4rem; padding: 1.5rem 0 3rem; font-family: var(--sans); font-size: .78rem; line-height: 1.7; color: var(--muted); }
  footer.colo h3 { font-size: .68rem; letter-spacing: .15em; text-transform: uppercase; color: var(--ink); margin: 0 0 .9rem; }
  footer.colo p { max-width: 42rem; margin: 0 0 .8rem; }

  @media (max-width: 760px) {
    body { font-size: 16px; padding: 0 .6rem 4rem; }
    .line, .cast-row { grid-template-columns: 1fr; gap: .15rem; }
    .who, .cast-name { padding-top: 0; margin-bottom: .05rem; }
    .beat, .keybox, .eq, .tablewrap { grid-column: 1; }
    figcaption { grid-template-columns: 1fr; gap: .3rem; }
  }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }

  .nextday {
    grid-column: 2; max-width: 39rem; margin: 2.4rem 0 0;
    border-top: 1px solid var(--rule); padding-top: 1.1rem;
    font-family: var(--sans); font-size: .9rem; color: var(--muted);
  }
  .nextday p { margin: 0 0 .35rem; }
  .nextday a { color: var(--blue); font-weight: 600; text-decoration: none; }
  .nextday a:hover, .nextday a:focus { text-decoration: underline; }
  .hw .unsolved { color: var(--gold); font-style: italic; font-weight: 600; }
</style>

<div class="pad">

<header class="top">
  <p class="course">Honors Math &nbsp;·&nbsp; Period 3 &nbsp;·&nbsp; First Day</p>
  <h1>Circles, and<br /><em>How Wrong We're Willing to Be</em></h1>
  <p class="standfirst">In which nothing is infinite, nothing is measured, and &pi; turns up anyway &mdash; by being counted.</p>
</header>

<div class="cast">
  <div class="cast-row"><div class="cast-name">Mrs. Feeney</div><div class="cast-desc">Nineteen years of eighth grade. Has never once written &ldquo;because I said so&rdquo; on a board.</div></div>
  <div class="cast-row"><div class="cast-name">Ralphie</div><div class="cast-desc">Front row. Answers before his hand is all the way up.</div></div>
  <div class="cast-row"><div class="cast-name">Popovich</div><div class="cast-desc">Back row, hood up. His grandfather laid out county roads with a steel chain.</div></div>
</div>

<!-- 01 -->
<section>
  <h2><span class="n">01</span> What a circle is, and the trouble with dots</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Good morning. Sit anywhere. Popovich, hood.</p>
    <p>Today: circles. Everybody in this room has drawn one. Today you find out what one <em>is</em>, and I promise that's a different thing.</p>
    <p>Somebody give me the definition. Not a drawing &mdash; the rule.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>All the points that are the same distance from the middle!</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Perfect. Say it again but slower, because there's a landmine in it.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>All the points&hellip; the same distance&hellip; from the middle.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(tapping the board, which is a grid of dots)</span> Here is our world. Dots. A dot at every whole-number spot, as far as you like in any direction. That's all we've got &mdash; there's nothing <em>between</em> two dots, because there's nothing there to be.</p>
    <p>Now. Put your finger on the middle dot and find me every dot exactly ten away.</p>
  </div></div>

  <figure>
    <div class="boardshot"><img src="__B1__" alt="A whiteboard printed with a lattice of faint dots, the centre dot circled in red marker and labelled the middle, with one unit measured between two adjacent dots" /></div>
    <figcaption><span class="pn hand">Fig. 1 &middot; board</span><span class="pt">The whole world, and the only thing in it. The lattice is printed on the board; everything else is marker.</span></figcaption>
  </figure>

  <div class="line"><div class="beat">(Scratching. A long pause. Ralphie's hand goes up, then down, then up.)</div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>Ten to the right. Ten up. Ten left, ten down. Um. And &mdash; six across and eight up! That's ten, because six squared plus eight squared is thirty-six plus sixty-four is a hundred.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Beautiful. Keep going.</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;Eight across and six up. <span class="stage">(pause)</span> That might be all of them.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>That's all of them. Twelve dots. Now &mdash; is that a circle?</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>No. That's twelve dots.</p></div></div>

  <figure>
    <div class="boardshot"><img src="__B2__" alt="Twelve blue dots marked on the lattice, all exactly ten steps from the centre, with a six-eight-ten right triangle drawn in red marker from the middle to one of them" /></div>
    <figcaption><span class="pn hand">Fig. 2 &middot; board</span><span class="pt">Every dot exactly ten away &mdash; and the one Ralphie found first, which is a 6-8-10 triangle whether he knew it or not.</span></figcaption>
  </figure>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Correct, and thank you for not being polite about it. Twelve dots is not a circle. So we have a problem, and here it is:</p></div></div>

  <div class="line"><div class="keybox"><span class="lbl">The trouble</span><p>Almost no dot is <em>exactly</em> ten from the middle. If we insist on &ldquo;exactly,&rdquo; our circles have twelve dots in them and enormous holes. A rule that strict doesn't draw &mdash; it just says no.</p></div></div>
</section>

<!-- 02 -->
<section>
  <h2><span class="n">02</span> How wrong are we willing to be?</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>So we loosen it, exactly one notch. New rule: <strong>for each column, take the dot nearest to ten away.</strong> Not the exact one. The nearest one.</p>
  </div></div>

  <figure>
    <div class="boardshot"><img src="__B4__" alt="Fifty-six blue dots on the lattice forming an unmistakable ring, with the true circle faintly dashed behind them" /></div>
    <figcaption><span class="pn hand">Fig. 3 &middot; board</span><span class="pt">Fifty-six dots. Nobody in the room disputes that this is a circle, which is what makes the next two minutes worth having.</span></figcaption>
  </figure>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>How do we know which one's nearest, though? Do we measure it?</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>With what, Ralphie. A piece of string?</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;I was going to say a ruler.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>You don't measure. Ten away means the squares add up to a hundred. So square the two dots that look close and see which total lands nearer a hundred.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Do the seventh column for me.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>Forty-nine and forty-nine is ninety-eight. Two short. Forty-nine and sixty-four is a hundred and thirteen. Thirteen over. So it's the lower one.</p>
  </div></div>

  <figure>
    <div class="boardshot"><img src="__B6__" alt="One column of the lattice with the ring crossing it, the two candidate dots labelled 49 plus 64 equals 113 and 49 plus 49 equals 98, and the nearer one circled" /></div>
    <figcaption><span class="pn hand">Fig. 4 &middot; board</span><span class="pt">No ruler and no string. Squaring turns &ldquo;which is nearer&rdquo; into arithmetic you can do in your head &mdash; and it never once asks what the distance actually <em>is</em>.</span></figcaption>
  </figure>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Notice what he did <em>not</em> do. He never worked out how far away either dot was. He only worked out which of them was <em>nearer</em>, and squaring is enough for that.</p>
    <p>This is going to keep happening all year, so learn to like it: the squared distance is easier than the distance, and most of the time the distance was never the thing you wanted.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>What if there are two dots equally near, though?</p>
  </div></div>

  <div class="line"><div class="beat">(Mrs. Feeney stops writing.)</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Say that again.</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>If the ring goes exactly down the middle between two dots. Then neither one is <em>the</em> nearest, and you never said what to do.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Then the rule does not tell you what to do, and a rule that does not tell you what to do is not a rule at all. That is a serious objection and I want it settled before we go on.</p>
    <p>So: can it happen? Write down what it would take.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>Both totals the same distance from a hundred. One under, one over, same gap.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Then what would the two of them have to add up to?</p>
  </div></div>

  <div class="line"><div class="beat">(Working. Somebody counts on their fingers, which Mrs. Feeney pretends not to see.)</div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;Two hundred?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Don't ask me, tell me. Why two hundred?</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>Because one of them is a hundred <em>take away</em> something, and the other one is a hundred <em>plus</em> the same something. So when you add them up the something cancels itself out and you're left with two hundreds.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Do it with a number so the back row can see it.</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>Say one's three under. That's ninety-seven. Then the other's three over, so that's a hundred and three. And ninety-seven and a hundred and three is two hundred.</p>
    <p>The three you took off the first one is the same three you put on the second. Moving it across doesn't change the pile.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(writing &ldquo;moving it across doesn't change the pile&rdquo; on the board)</span> That is the whole of it, and it works for any amount, not just three. Under by seven, over by seven &mdash; ninety-three and a hundred and seven. Two hundred. It cannot help itself.</p>
  </div></div>

  <figure>
    <div class="boardshot"><img src="__B10__" alt="Two columns drawn on the board, one topping out three below a dashed line marked a hundred and the other three above it, with an arrow showing the same three moving across" /></div>
    <figcaption><span class="pn hand">Fig. 5 &middot; board</span><span class="pt">Ralphie's reason, drawn. What one pile is short, the other is over by, and it is the same three. Zoomed to the tops, because at full height a difference of three is invisible &mdash; and the three is the entire point.</span></figcaption>
  </figure>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Exactly two hundred, and I want to be careful about what that sentence means, because it is not a statement about any dots we have actually looked at.</p>
    <p>Your column seven: ninety-eight and a hundred and thirteen. Add those.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>Two hundred and eleven.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Two hundred and eleven, so no tie in that column, obviously. Two hundred is not something the totals <em>do</em>. It is the thing they would have to do <em>if</em> there were a tie.</p>
    <p>So the question is now a completely different question, and a much easier one. Never mind circles. Is there any column anywhere, at any radius, where the two totals land on exactly twice the target?</p>
  </div></div>

  <div class="line"><div class="beat">(A long pause. Then Ralphie, who asked the question, gets there first.)</div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>They can't. They can't ever add up to an even number.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p><span class="stage">(carefully)</span> Why not.</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>Because the two dots are one apart. So it's <span class="m">y</span> squared plus <span class="m">y</span>-plus-one squared, and that's always odd &mdash; you can try it, it's always odd. And then twice <span class="m">x</span> squared on top, which is even.</p>
    <p>Odd plus even is odd. And twice the target is even. They're never the same number.</p>
  </div></div>

  <div class="line"><div class="beat">(Mrs. Feeney puts the cap on the marker.)</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Ralphie has just proved something. Not checked it &mdash; <em>proved</em> it. There is no radius, no column, and no dot anywhere in this room or outside it where that rule gets stuck, and he did it with odd and even.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>How close does it get?</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(delighted, checking)</span> On the ten-ring? Column three. The dots at nine and ten give ninety and a hundred and nine. That is <em>one hundred and ninety-nine</em>.</p>
    <p>One short. It gets as near as it is arithmetically possible to get and it still cannot arrive, because arriving would mean an odd number was even.</p>
  </div></div>

  <figure>
    <div class="boardshot"><img src="__B11__" alt="The board after the argument, showing column seven totalling 211, column three totalling 199 marked as the closest, a greyed-out tie needing 200, and the note that one side is always odd and the other always even" /></div>
    <figcaption><span class="pn hand">Fig. 6 &middot; board</span><span class="pt">What is left on the board when they finish. The greyed line is the tie &mdash; written down, never met. Two hundred is the only one of the three that never happens.</span></figcaption>
  </figure>

  <div class="line"><div class="keybox"><span class="lbl">The rule is never stuck</span><p>Two dots one apart give totals that always sum to an <span class="exact">odd</span> number. Twice the target is always <span class="exact">even</span>. So the two can never be equally near, at any radius, in any column &mdash; and &ldquo;take the nearest&rdquo; always names exactly one dot.</p><p>No search found this. It was settled by asking what a tie would require and noticing that the requirement is impossible.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p><span class="stage">(to Ralphie)</span> That was good.</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>I know.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>That's rounding.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>It is rounding.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>So it's not a circle. It's a picture of a circle. You just decided to be wrong and then drew it anyway.</p>
  </div></div>

  <div class="line"><div class="beat">(Mrs. Feeney puts the marker down. This is clearly her favourite moment of the year.)</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Popovich, that is the correct objection and I want the whole class to write it down. Here's what we do with it. We don't argue. We <em>measure</em> it.</p>
    <p>You say I'm wrong. Fine. <strong>How wrong?</strong></p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>&hellip;How would I know?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>You'd work it out. And it isn't hard, because I told you the rule: take the <em>nearest</em> dot. If a dot is the nearest one, how far off can it possibly be?</p>
  </div></div>

  <div class="line"><div class="beat">(Silence. Then, from the back:)</div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Half a unit.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Half a unit.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Because if it were more than half, a different dot would be closer, and you'd have picked that one instead.</p></div></div>

  <figure>
    <div class="boardshot"><img src="__B3__" alt="A curved arc drawn in marker passing between two lattice dots in the same column, with the gap above the ring and the gap below it braced together as one whole unit" /></div>
    <figcaption><span class="pn hand">Fig. 7 &middot; board</span><span class="pt">Popovich's argument, drawn. The ring passes between two dots one unit apart, so the two gaps make one unit between them &mdash; so whichever is shorter cannot be more than a half. Notice the board never says where the ring actually crosses: working that out would need a square root, and the argument does not need to know.</span></figcaption>
  </figure>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(to the room)</span> Say that back to yourselves tonight until it's boring. That is the entire argument.</p>
  </div></div>

  <div class="line"><div class="keybox"><span class="lbl">The answer to the objection</span><p>Our circle is never off by more than <span class="exact">half a unit</span>. Not on average &mdash; <em>ever</em>. Not at radius ten, not at radius ten thousand, not at radius the-size-of-the-county. The error doesn't grow, because &ldquo;nearest&rdquo; means what it says.</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>Wait, it doesn't get worse when the circle gets bigger?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Not by a hair. Bigger circle, more dots, same half unit. <span class="stage">(beat)</span> I ran it out to radius one hundred and ten before you came in this morning. It held the whole way, and I will show you how I know that before the bell.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Huh.</p></div></div>
</section>

<!-- 03 -->
<section>
  <h2><span class="n">03</span> Drawing it, without knowing how far</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Now the good part. To find the nearest dot you'd think we need to know how far away things are &mdash; how far, in every single column. And we have just agreed that mostly there is no such number.</p>
    <p>We don't. Watch. Start at the top of the circle. Step one to the right. Ask one question: <em>am I still closer to the ring if I stay, or if I drop down one?</em> Answer it. Step again.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>How do you answer it without knowing how far anything is?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>You keep a running number and add to it. When it goes negative you stay; when it doesn't, you drop. The amount you add is built out of the numbers you already have.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Before anybody writes a line of it &mdash; what has to be <em>true</em> of the answer? Not how you would get it. What would make it right.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;It should look like a circle?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Not good enough. Nobody can check &ldquo;looks like a circle.&rdquo; Give me something that could be checked by something with no eyes.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Nothing more than half a unit off the ring.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(writing)</span> That's it. And notice what it is &mdash; that's <em>your own sentence</em> from twenty minutes ago, and it has just become the definition.</p>
    <p>Now. &ldquo;Half a unit off the ring&rdquo; sounds like it needs to know how far the dot actually is. And most of these dots have no how-far. There is no whole number that squares to forty-eight, and there is no fraction either &mdash; the distance is simply not a thing you can write down.</p>
    <p>So do not ask for it. Square both sides and watch the question go away.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>There's a name for it, though. The number that isn't there. My grandfather had a word for it.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Did he.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>He called it a square r&mdash;</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Popovich.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>You're the one who said there's no number. I'm saying it has a name anyway.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>It has a name in books I am not handing you in the first week of term. That way lie paradoxes, and paradoxes are a spring problem.</p>
    <p>Don't be a rebel in my classroom. Not today, anyway.</p>
  </div></div>

  <div class="line"><div class="beat">(Popovich sits back. Not conceding &mdash; filing it.)</div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Not today.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Thank you. <span class="stage">(beat)</span> Ask me in April. I will tell you the whole thing and you will be sorry you asked.</p>
    <p>And for what it is worth &mdash; your grandfather knew the word too, and laid out eleven miles of road without ever once needing it. Hold on to that part.</p>
  </div></div>

  <div class="line"><div class="code spec">
    <span class="attrib">The blueprint</span>
<pre><span class="cm">\* squared distance. no square root lives in this file.</span>
Quadrance(p) == p[1]*p[1] + p[2]*p[2]

<span class="cm">\* "no more than half a unit off the ring", squared out</span>
<span class="cm">\* so that every number in it is a whole number:</span>
NearRing(p) == /\ (2*R - 1)^2 =&lt; 4 * Quadrance(p)
               /\ 4 * Quadrance(p) =&lt; (2*R + 1)^2

<span class="cm">\* and this is the circle. all of it.</span>
Circle == { p \in Dots : NearRing(p) }</pre>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Four lines, and I want you to notice what is <em>missing</em> from them. There is no first dot. There is no next dot. Nothing goes round the ring in any order, because nothing goes round the ring at all &mdash; it is a set, and a set does not have a beginning.</p>
    <p>Nobody draws a house out of bricks. You draw it on paper, and the paper is not made of brick. This is the paper.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>So where's the program?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>The program is somebody's <em>clever way of picking dots that satisfy this</em>. It is downstream. Copy it down, and notice that it agrees with nothing you just wrote &mdash; it has loops in it, and an order, and a running total, and none of those words appear above.</p>
  </div></div>

  <div class="line"><div class="code">
    <span class="attrib">On the board</span>
<pre><span class="kw">def</span> circle(r):
    x, y, d = 0, r, 3 - 2*r
    dots = []

    <span class="kw">while</span> x &lt;= y:
        <span class="cm"># one dot gives you eight, by mirroring</span>
        <span class="kw">for</span> a, b <span class="kw">in</span> [(x,y), (y,x), (-x,y), (-y,x),
                     (x,-y), (y,-x), (-x,-y), (-y,-x)]:
            dots.append((a, b))

        <span class="kw">if</span> d &lt; 0:
            d = d + 4*x + 6          <span class="cm"># stay on this row</span>
        <span class="kw">else</span>:
            d = d + 4*(x - y) + 10   <span class="cm"># drop down one</span>
            y = y - 1
        x = x + 1

    <span class="kw">return</span> dots</pre>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>No distances. No &pi;. No decimal point <em>anywhere</em> &mdash; every number in there is a whole number from start to finish. Adding, subtracting, doubling. That's the whole toolkit.</p>
    <p>And look at the loop condition: <span class="m">while x &lt;= y</span>. It stops at the diagonal. You only ever compute one eighth of the ring &mdash; the other seven eighths are mirror images, which is what that list of eight pairs is doing. You get them for free.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>What happens if that running number lands on nought? It says <span class="m">less than nought</span>, and then <span class="m">otherwise</span>. Nought falls into <em>otherwise</em>. Why should it?</p>
  </div></div>

  <div class="line"><div class="beat">(Mrs. Feeney looks at Ralphie rather than at Popovich.)</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Ralphie. Answer him.</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;Why me?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Because you already did, twenty minutes ago. That running number is odd every single time it is looked at &mdash; it is an even thing plus an odd thing minus an even thing. And nought is even.</p>
    <p>It never lands on nought. The <em>otherwise</em> never has to decide anything, because the case it would be deciding cannot happen.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>So the program is only unambiguous because of odd and even.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Yes &mdash; for <em>this</em> way of writing it. And I want to be careful here, because there is more than one way to write the same algorithm, and the other one does not get off so lightly.</p>
    <p>Write the running number a slightly different way and it <em>does</em> land on nought sometimes. Not often. And when it does, it is not a problem &mdash; it is telling you something.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Telling you what?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Ask me again after we have looked at which dots land perfectly. <span class="stage">(she writes &ldquo;nought&rdquo; in the corner of the board and boxes it)</span> That is a promise, not a dodge.</p>
  </div></div>

  <figure>
    <div class="boardshot"><img src="__B5__" alt="The lattice with one eighth of the plane shaded, the four fold lines dashed through the centre, and a single red dot inside the shaded wedge together with its seven mirror images" /></div>
    <figcaption><span class="pn hand">Fig. 8 &middot; board</span><span class="pt">The shaded wedge is the only part anyone computes. The four dashed lines are the folds; one dot in the wedge lands on eight when you unfold it.</span></figcaption>
  </figure>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>That's how a computer draws a circle?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>That is <em>exactly</em> how a computer draws a circle. Every circle you have ever seen on a screen in your life was made this way. Nobody's graphics card has ever once needed to know how far a pixel was to draw a rim.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>Can we see a big one? Bigger than the board.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(crossing to the projector, which has been off all morning)</span> We can, and we are going to have to start being careful about something. Everything up to now has been <em>mine</em> &mdash; my board, my marker, my arithmetic, and you have all been checking it as I went.</p>
    <p>This is a machine. It does not check itself, and it does not care whether I am right. Watch what it does anyway.</p>
    <p>Put up the one from this morning. Radius a hundred and ten.</p>
  </div></div>

  <figure>
    <div class="plate"><img src="__P1__" alt="A circle of radius 110 drawn as blue lattice dots, visually smooth and round" /></div>
    <figcaption><span class="pn">Fig. 9 &middot; screen</span><span class="pt">Radius 110. Six hundred and twenty-four dots, placed using nothing but addition and subtraction. No dot is more than half a unit off the true ring &mdash; and that is a promise that holds at every radius, not a lucky outcome at this one.</span></figcaption>
  </figure>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Six hundred and twenty-four dots. And I promised you this morning that not one of them would be more than half a unit off, however big we made it.</p>
    <p>So check me. Six hundred and twenty-four dots, Ralphie. Off you go with your ruler.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;That's not fair, that would take all week.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>You don't need a ruler. You wrote the rule down twenty minutes ago. Four times the squares, between two hundred and nineteen squared and two hundred and twenty-one squared.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(typing)</span> Four times the squares. Between <span class="m">47,961</span> and <span class="m">48,841</span>. Every dot.</p>
  </div></div>

  <div class="line"><div class="out">r = 110
lowest  4Q seen:  48,008
highest 4Q seen:  48,820
inside the band:  624 of 624</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Every one. And notice what we did <em>not</em> do &mdash; nobody worked out how far off any dot actually was. For most of them there is no such number to work out.</p>
    <p>We asked a smaller question. Not <em>how far</em>. Only <em>near enough or not</em>. Popovich's sentence, eleven times bigger than the board, and it still costs nothing to check.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>My grandfather laid out roads. County roads, before I was born. He had a steel chain and a notebook and he never once needed a number that wasn't there.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Are the roads still there?</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>I ride my bike on one.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Then your grandfather is the whole lesson and I'd like him to come talk to fourth period.</p>
  </div></div>
</section>

<!-- 04 -->
<section>
  <h2><span class="n">04</span> Checking it without reading it</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Now. I have two copies of that program on the board. They differ by exactly one number. One of them is right and one of them is wrong.</p>
    <p>Find the wrong one. By reading.</p>
  </div></div>

  <div class="line"><div class="beat">(Three minutes. Somebody guesses the 10. Somebody guesses the minus sign. Both wrong.)</div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>They look the same.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>They do look the same. So stop reading them. We are going to say what a <em>drawing</em> has to satisfy &mdash; not what it does, what it owes us &mdash; and then let the machine sort them out.</p>
  </div></div>

  <div class="line"><div class="code spec">
    <span class="attrib">What a drawing owes us</span>
<pre><span class="cm">\* it only drew dots that were allowed</span>
Sound(drawn)     == drawn \subseteq Circle

<span class="cm">\* it left no column empty</span>
Complete(drawn)  == \A x \in -R..R : \E p \in drawn : p[1] = x

<span class="cm">\* whatever it drew, it drew all eight mirrors of</span>
Symmetric(drawn) == \A p \in drawn : Mirrors(p) \subseteq drawn

Correct(drawn)   == Sound(drawn) /\ Complete(drawn) /\ Symmetric(drawn)</pre>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>Mine isn't in there.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Which one is yours?</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>The tie one. That there's never two dots equally near. We <em>proved</em> that and it's not written down anywhere.</p>
  </div></div>

  <div class="line"><div class="beat">(Mrs. Feeney reads her own three rules again, slowly.)</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>No, it is not, and that is a fair complaint. But before you write it in &mdash; look at where you would put it. Read the three you have and tell me what they are all about.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>They're all about the drawing. What it drew, what it left out, whether it mirrored properly.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>And Ralphie's?</p></div></div>

  <div class="line"><div class="beat">(Ralphie opens his mouth, then doesn't.)</div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>His isn't about the drawing at all. There's no program in it. It's about the dots.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>His is about whether the <em>question</em> means anything. The very first rule says the drawing may only use dots that are near enough &mdash; and the whole method for finding them was &ldquo;take the nearest one&rdquo;. If two could tie, there is no such thing as the nearest one, and that rule is asking for a dot that might not exist.</p>
    <p>So it does not go among the three. It goes <em>above</em> them.</p>
  </div></div>

  <div class="line"><div class="code spec">
    <span class="attrib">Added to the blueprint</span>
<pre><span class="cm">\* not about any drawing. about whether "the nearest"</span>
<span class="cm">\* names anything at all.</span>
NoTies == \A x \in -R..R : \A y \in -R..R :
            LET Q1 == x*x + y*y
                Q2 == x*x + (y+1)*(y+1)
            IN  Q1 + Q2 # 2*R*R</pre>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>And note the order we did that in. Ralphie did not write it down and then wonder whether it was true. He settled it with odd and even, at his desk, twenty minutes ago &mdash; and <em>then</em> we wrote it where a machine can keep checking it.</p>
    <p>That is the right way round, and it is the opposite of what most people do.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>Both fine. I checked them at thirteen.</p></div></div>

  <div class="line"><div class="out">R = 13
program A:  Correct
program B:  Correct</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>You checked them at thirteen. Check them at everything.</p>
  </div></div>

  <div class="line"><div class="out">R = 3 to 120
program A:  Correct at all 118
program B:  FAILS at 103 of 118 — always Sound; it drew a dot that was not allowed
            passes at 3, 4, 5, 6, 7, 9, 10, 11, 13, 17, 18, 19, 28, 31 …</div></div>

  <figure>
    <div class="plate"><img src="__S2__" alt="A strip of 118 bars, one per radius, red where the sabotaged program is caught and blue where it passes, with radius 13 marked in gold" /></div>
    <figcaption><span class="pn">Fig. 10 &middot; screen</span><span class="pt">One bar per radius from 3 to 120. Red is caught, blue passes. The gold marker is thirteen, sitting comfortably among the radii where the broken program looks perfect.</span></figcaption>
  </figure>

  <div class="line"><div class="beat">(Ralphie looks at the 13 in his own list of passing radii for a while.)</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>The <span class="m">6</span> in program B is a <span class="m">4</span>. None of you were ever going to see that by reading, and it did not matter, because you had written down what must be true.</p>

  <figure>
    <div class="plate"><img src="__S1__" alt="Two circles side by side at radius 8, the right-hand one with eight dots circled in red where they fall outside what the blueprint permits" /></div>
    <figcaption><span class="pn">Fig. 11 &middot; screen</span><span class="pt">Radius eight, where the sabotage does bite. Eight of program B&rsquo;s dots sit outside the permitted band &mdash; and they are not visibly out of place until something checks them.</span></figcaption>
  </figure>
    <p>But look at what nearly happened. The broken program is wrong at a hundred and three radii out of a hundred and eighteen, and it is <em>right at thirteen</em>, which is the number we have been using all morning. Ralphie tested it once and it told him everything was fine.</p>
  </div></div>

  <div class="line"><div class="keybox"><span class="lbl">Checking one case is not checking</span><p>A wrong program is not wrong everywhere. It is wrong <em>somewhere</em>, and it will be perfectly well behaved on the example you happen to try &mdash; especially if you picked that example because it was the one you understood.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>So we don't have to understand the program.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>You have to understand the <em>rules</em>. The program is somebody's clever trick for satisfying them. Tricks are cheap. Knowing what would make a trick correct is not.</p>
  </div></div>

  <div class="line"><div class="beat">(Ralphie has been typing this whole time and now looks alarmed.)</div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>Mrs. Feeney, I added a fourth rule and now the <em>good</em> program fails.</p>
  </div></div>

  <div class="line"><div class="code spec">
    <span class="attrib">Ralphie's fourth condition</span>
<pre><span class="cm">\* each column's dot sits at the whole-number part of</span>
<span class="cm">\* the square root. seems obvious enough.</span>
Tidy(drawn) == \A x \in -R..R :
                 &lt;&lt;x, WholePartOfSqrt(R*R - x*x)&gt;&gt; \in drawn</pre>
  </div></div>

  <div class="line"><div class="out">program A:  FAILS at R = 3 — Tidy is false</div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>So program A is broken after all? At <em>three</em>?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(very pleased, and hiding it badly)</span> Maybe. Or your rule is broken. Which is it?</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;How would I even tell?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>The same way we settle everything in here. Go count one by hand.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p><span class="stage">(already doing it)</span> Three is too cramped to see anything. Do thirteen.</p>
    <p>Column eleven. Thirteen squared is one sixty-nine. Take off a hundred and twenty-one and you want forty-eight.</p>
    <p>Six squared is thirty-six &mdash; that's twelve short. Seven squared is forty-nine &mdash; that's one over. So it's <em>seven</em>, and it isn't close.</p>
    <p>Your rule chops it down to six. It rounds the wrong way, and it has been rounding the wrong way since three.</p>
  </div></div>

  <div class="line"><div class="beat">(Ralphie stares at his screen for a second.)</div></div>

  <figure>
    <div class="boardshot"><img src="__B7__" alt="Column 11 of the radius 13 ring, showing 121 plus 49 equals 170 for the dot at 7 and 121 plus 36 equals 157 for the dot at 6, against a target of 169" /></div>
    <figcaption><span class="pn hand">Fig. 12 &middot; board</span><span class="pt">Popovich settling it by hand. The target is 169. The dot at 7 gives 170, one over; the dot at 6 gives 157, twelve under. Ralphie&rsquo;s rule demanded the 6.</span></figcaption>
  </figure>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>My rule was wrong. Not the program.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Your rule was wrong. And this is the part I want you to remember longer than anything else today.</p>
  </div></div>

  <div class="line"><div class="keybox"><span class="lbl">Rules are claims too</span><p>A rule that says what must be true is itself a thing that might be false. It can be wrong in exactly the confident, plausible-looking way a program can be wrong &mdash; and it will happily accuse a correct program of being broken.</p><p>So a rule has to answer to something outside itself: <span class="exact">a case you worked out by hand.</span> Thirteen and eleven and six point nine. That is why we counted three hundred and seventeen dots one at a time before we trusted anything.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>So we check the program with the rules, and the rules with the counting.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>All the way down. Yes.</p></div></div>
</section>


<!-- the bell -->
<section>
  <h2><span class="n">05</span> The bell</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Two minutes. Look at where we started.</p>
    <p>Ralphie found twelve dots this morning, and Popovich said &mdash; correctly &mdash; that twelve dots is not a circle.</p>
  </div></div>

  <div class="line"><div class="beat">(Nobody says anything. The board is covered.)</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>We have one now. We know it is never wrong by more than half a unit, and we know that at every size, for ever. We know the rule that finds it never gets stuck, and we know <em>that</em> because Ralphie proved it with odd and even, not because I told you.</p>
    <p>And we have three sentences that will catch a program lying to us &mdash; including one that lies extremely well at thirteen.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>We never did find out how far away anything was.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>No. <span class="stage">(gathering the markers)</span> And you stopped asking about half an hour ago.</p>
  </div></div>

  <div class="hw">
    <h3>Homework &mdash; the whole assignment</h3>
    <ol>
      <li>The ring at nineteen. Which dot sits in column six? Do not measure anything, and show me the two totals you compared.</li>
      <li>Ralphie's proof was about two dots <em>one</em> apart. Does it still work for dots <em>two</em> apart? If it does, say why in one line. If it doesn't, bring me a tie.</li>
      <li><span class="unsolved">The one I want most.</span> Our three rules are Sound, Complete and Symmetric. Find something that obeys all three and is <em>not</em> the circle we wanted. It exists. When you find it, write the fourth rule that would have stopped it.</li>
    </ol>
  </div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Number three is not a trick and it is not impossible. It is the thing that keeps me up at night, and one of you is going to find it on the bus.</p>
  </div></div>

  <div class="line"><div class="beat">(bell)</div></div>

  <div class="line"><div class="nextday">
    <p><strong>The next lesson</strong> is about which dots land <em>perfectly</em> &mdash; and about counting your way to &pi;.</p>
    <p><a href="counting.html">Go on to day three &rarr;</a></p>
  </div></div>
</section>

<footer class="colo">
  <h3>Checked before printing</h3>
  <p>Every number here was computed rather than remembered: the twelve dots at radius 5, 10 and 13; the twenty at radius 25 and thirty-six at 65; all 624 dots at radius 110 sitting inside the integer band, four times the squares between 219&sup2; and 221&sup2; &mdash; established without taking a square root; the dot counts 317 / 31,417 / 3,141,549 / 314,159,053 and the &pi; digits they yield; and the integer-only drawing rule, verified to place its dots in the same spots as the square-root method at every radius tested. Ralphie's parity argument is also carried in the specification as an invariant, <span style="font-family:var(--mono)">NoTies</span>, model-checked at eight radii &mdash; though the argument itself settles every radius at once.</p>
  <p>The same parity fact makes the drawing algorithm deterministic: its decision variable is odd at every step, so it never lands on nought and the <span style="font-family:var(--mono)">otherwise</span> branch never breaks a tie. Checked at every radius from 2 to 1999. That is a fact about the <em>midpoint</em> variant, which is what this lesson teaches.</p>
  <p>Bresenham's own 1977 algorithm is a different procedure &mdash; a decision variable evaluated at the diagonal neighbour, initialised <span style="font-family:var(--mono)">2 &minus; 2R</span> rather than <span style="font-family:var(--mono)">3 &minus; 2r</span>. His <em>does</em> land on zero, at 143 of the radii from 2 to 399, and he handles it explicitly as his &ldquo;case 5&rdquo;, proving the move stays forced. It is zero exactly when a lattice point sits perfectly on the ring &mdash; so the radii that trouble his algorithm are precisely the lucky ones. The two algorithms agree on their output at every radius tested to 200, but <span style="font-family:var(--mono)">3 &minus; 2r</span> is not his, and calling it &ldquo;Bresenham's circle algorithm&rdquo;, as almost everyone does, is a misattribution.</p>
  <p>Ralphie's homework, for anyone who wants it now: NASA JPL reports working to about fifteen digits for interplanetary navigation. Thirty-eight would draw a circle round the observable universe to within a hydrogen atom. Mrs. Feeney does not know either figure, and would rather he looked them up than took them from her &mdash; which is the only reason they are down here and not up there.</p>

  <h3 style="margin-top:2rem">Whose ideas these are</h3>
  <p><strong>The drawing algorithm</strong> is Bresenham's circle algorithm &mdash; J. E. Bresenham, &ldquo;A Linear Algorithm for Incremental Digital Display of Circular Arcs&rdquo;, <em>Communications of the ACM</em> 20(2), February 1977, 100&ndash;106. Not the better-known 1965 paper (&ldquo;Algorithm for computer control of a digital plotter&rdquo;, <em>IBM Systems Journal</em> 4(1), 25&ndash;30), which draws lines; the circle came twelve years afterwards. The variant used here is usually called the midpoint circle algorithm.</p>
  <p><strong>Counting dots to get &pi;</strong> is the Gauss circle problem. <strong>Which radii carry dots that land exactly</strong> is the theory of sums of two squares, from Fermat and Jacobi. <strong>Writing the blueprint before the program</strong>, and the observation that a specification is not written in the material the thing is built from, is Leslie Lamport &mdash; &ldquo;Thinking Above the Code&rdquo;, Microsoft Research Faculty Summit, 2014 &mdash; and the notation of the blueprint is his TLA+.</p>
  <p>None of the mathematics in this lesson is new. The only thing arranged here is the order.</p>
</footer>

</div>
"""

DOC2 = r"""<title>Honors Math, Period 3 — Day Three: Counting</title>
<style>
  :root {
    --pad:      #EDF0F2;
    --pad-2:    #E3E9ED;
    --rule:     #C9D6DE;
    --rule-fine:#DCE5EA;
    --ink:      #16222B;
    --blue:     #1D5C8F;
    --gold:     #9A6B12;
    --muted:    #667680;
    --plate:    #0D1117;
    --serif: Charter, "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
    --sans: system-ui, "Avenir Next", "Segoe UI", Helvetica, Arial, sans-serif;
    --mono: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --pad:#0F1419; --pad-2:#161C22; --rule:#232C34; --rule-fine:#1A2128;
      --ink:#DCE3E8; --blue:#6FA8FF; --gold:#E3B341; --muted:#7E8C96;
    }
  }
  :root[data-theme="dark"] {
    --pad:#0F1419; --pad-2:#161C22; --rule:#232C34; --rule-fine:#1A2128;
    --ink:#DCE3E8; --blue:#6FA8FF; --gold:#E3B341; --muted:#7E8C96;
  }
  :root[data-theme="light"] {
    --pad:#EDF0F2; --pad-2:#E3E9ED; --rule:#C9D6DE; --rule-fine:#DCE5EA;
    --ink:#16222B; --blue:#1D5C8F; --gold:#9A6B12; --muted:#667680;
  }

  body {
    margin: 0;
    padding: 0 1.5rem 6rem;
    background-color: var(--pad);
    background-image:
      repeating-linear-gradient(to right,  var(--rule-fine) 0 1px, transparent 1px 28px),
      repeating-linear-gradient(to bottom, var(--rule-fine) 0 1px, transparent 1px 28px);
    color: var(--ink);
    font-family: var(--serif);
    font-size: 17px;
    line-height: 1.64;
    -webkit-font-smoothing: antialiased;
  }
  .pad {
    max-width: 60rem; margin: 0 auto;
    background: var(--pad);
    box-shadow: 0 0 0 1px var(--rule);
    padding: 0 clamp(1.2rem, 4vw, 3.5rem);
  }

  /* ---- header ---- */
  header.top { padding: 3.2rem 0 1.4rem; border-bottom: 3px double var(--rule); }
  .course {
    font-family: var(--sans); font-size: .72rem; font-weight: 600;
    letter-spacing: .16em; text-transform: uppercase; color: var(--blue);
    margin: 0 0 1.4rem;
  }
  header.top h1 {
    font-family: var(--serif); font-weight: 600;
    font-size: clamp(2.1rem, 6vw, 3.2rem); line-height: 1.06;
    letter-spacing: -.02em; margin: 0 0 1rem; text-wrap: balance;
  }
  header.top h1 em { font-style: italic; color: var(--blue); }
  .standfirst {
    font-size: 1.02rem; color: var(--muted); max-width: 38rem; margin: 0 0 .6rem;
  }

  /* ---- cast ---- */
  .cast { padding: 2rem 0 2.2rem; border-bottom: 1px solid var(--rule); margin-bottom: 3rem; display: grid; gap: 1rem; }
  .cast-row { display: grid; grid-template-columns: 9rem 1fr; gap: 0 2rem; }
  .cast-name {
    font-family: var(--sans); font-size: .74rem; font-weight: 600;
    letter-spacing: .1em; text-transform: uppercase; color: var(--blue); padding-top: .3em;
  }
  .cast-desc { font-size: .95rem; max-width: 44rem; }

  /* ---- sections ---- */
  section { margin: 0 0 3.6rem; }
  h2 {
    font-family: var(--sans); font-size: .76rem; font-weight: 700;
    letter-spacing: .15em; text-transform: uppercase; color: var(--ink);
    margin: 0 0 2rem; padding-bottom: .65rem; border-bottom: 1px solid var(--rule);
    display: flex; gap: 1.1rem; align-items: baseline;
  }
  h2 .n { color: var(--blue); font-family: var(--mono); font-variant-numeric: tabular-nums; }

  /* ---- dialogue ---- */
  .line { display: grid; grid-template-columns: 9rem 1fr; gap: 0 2rem; margin-bottom: 1.1rem; }
  .who {
    font-family: var(--sans); font-size: .74rem; font-weight: 600;
    letter-spacing: .1em; text-transform: uppercase; color: var(--blue); padding-top: .36em;
  }
  .who.f { color: var(--ink); }
  .who.p { color: var(--muted); }
  .who.n { color: var(--gold); }
  .says { max-width: 39rem; }
  .says p { margin: 0 0 .8rem; }
  .says p:last-child { margin-bottom: 0; }
  .stage { color: var(--muted); font-style: italic; }
  .beat { grid-column: 2; color: var(--muted); font-style: italic; font-size: .93rem; margin: 1.3rem 0 1.4rem; max-width: 39rem; }
  code, .m { font-family: var(--mono); font-size: .92em; }

  /* ---- emphasis: gold means it lands exactly ---- */
  .exact { color: var(--gold); font-weight: 600; }
  .keybox {
    grid-column: 2; max-width: 39rem; margin: 1.5rem 0 1.7rem;
    border-left: 3px solid var(--gold); padding: 1rem 1.3rem;
    background: color-mix(in srgb, var(--gold) 8%, transparent);
  }
  .keybox p { margin: 0; }
  .keybox .lbl {
    font-family: var(--sans); font-size: .66rem; font-weight: 700; letter-spacing: .13em;
    text-transform: uppercase; color: var(--gold); display: block; margin-bottom: .4rem;
  }

  /* ---- code on the board / on a screen ---- */
  .code { grid-column: 2; max-width: 39rem; margin: 1.4rem 0 1.7rem; }
  .code .attrib {
    display: block; font-family: var(--sans); font-size: .64rem; font-weight: 700;
    letter-spacing: .13em; text-transform: uppercase; color: var(--muted); margin-bottom: .45rem;
  }
  .code pre {
    margin: 0; background: var(--plate); border: 1px solid var(--rule);
    padding: 1rem 1.15rem; overflow-x: auto;
    font-family: var(--mono); font-size: .8rem; line-height: 1.62; color: #C9D1D9;
  }
  .code.spec pre {
    background: var(--pad-2); color: var(--ink);
    border: 1px solid var(--rule); border-left: 3px solid var(--gold);
  }
  .code.spec .kw { color: var(--correction, #A3392B); }
  .code.spec .cm { color: var(--muted); }
  .code .kw { color: #FF7B72; }
  .code .cm { color: #8B949E; font-style: italic; }
  .code .st { color: #79C0FF; }
  .out {
    grid-column: 2; max-width: 39rem; margin: -.9rem 0 1.7rem;
    font-family: var(--mono); font-size: .78rem; color: var(--muted);
    border-left: 2px solid var(--rule); padding: .5rem 0 .5rem 1rem;
  }

  .eq {
    grid-column: 2; font-family: var(--mono); font-size: .92rem;
    background: var(--pad-2); border-left: 3px solid var(--blue);
    padding: .9rem 1.2rem; margin: 1.2rem 0; max-width: 39rem; overflow-x: auto;
  }

  /* ---- tables ---- */
  .tablewrap { grid-column: 2; overflow-x: auto; margin: 1.5rem 0 1.7rem; max-width: 42rem; }
  table { border-collapse: collapse; width: 100%; font-family: var(--mono); font-size: .79rem; }
  th, td { text-align: left; padding: .5rem 1rem .5rem 0; border-bottom: 1px solid var(--rule); font-variant-numeric: tabular-nums; white-space: nowrap; }
  th { font-family: var(--sans); font-size: .64rem; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); font-weight: 700; border-bottom: 2px solid var(--ink); }
  td.g { color: var(--gold); font-weight: 600; }
  td.b { color: var(--blue); }

  /* ---- plates ---- */
  figure { margin: 2.5rem 0; }
  .plate { background: var(--plate); border: 1px solid var(--rule); padding: .7rem; }
  .plate img { width: 100%; height: auto; display: block; }
  /* the board is a whiteboard: it stays light whatever theme the reader is in */
  .boardshot { background: #F8F7F3; border: 1px solid var(--rule); padding: .5rem; }
  .boardshot img { width: 100%; height: auto; display: block; }
  figcaption .pn.hand { color: var(--gold); }
  figcaption {
    font-family: var(--sans); font-size: .78rem; line-height: 1.6; color: var(--muted);
    margin-top: .8rem; display: grid; grid-template-columns: 7.5rem 1fr; gap: 0 1.2rem;
  }
  figcaption .pn { font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: var(--blue); font-size: .68rem; padding-top: .12em; }
  figcaption .pt { max-width: 39rem; }

  /* ---- homework ---- */
  .hw { border: 2px solid var(--ink); background: var(--pad-2); padding: 1.7rem 1.9rem; margin: 2.3rem 0; }
  .hw h3 { font-family: var(--sans); font-size: .72rem; font-weight: 700; letter-spacing: .15em; text-transform: uppercase; color: var(--blue); margin: 0 0 1.2rem; }
  .hw ol { margin: 0; padding-left: 1.3rem; display: grid; gap: .9rem; }
  .hw li { max-width: 39rem; padding-left: .3rem; }

  footer.colo { border-top: 3px double var(--rule); margin-top: 4rem; padding: 1.5rem 0 3rem; font-family: var(--sans); font-size: .78rem; line-height: 1.7; color: var(--muted); }
  footer.colo h3 { font-size: .68rem; letter-spacing: .15em; text-transform: uppercase; color: var(--ink); margin: 0 0 .9rem; }
  footer.colo p { max-width: 42rem; margin: 0 0 .8rem; }

  @media (max-width: 760px) {
    body { font-size: 16px; padding: 0 .6rem 4rem; }
    .line, .cast-row { grid-template-columns: 1fr; gap: .15rem; }
    .who, .cast-name { padding-top: 0; margin-bottom: .05rem; }
    .beat, .keybox, .eq, .tablewrap { grid-column: 1; }
    figcaption { grid-template-columns: 1fr; gap: .3rem; }
  }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }

  .nextday {
    grid-column: 2; max-width: 39rem; margin: 2.4rem 0 0;
    border-top: 1px solid var(--rule); padding-top: 1.1rem;
    font-family: var(--sans); font-size: .9rem; color: var(--muted);
  }
  .nextday p { margin: 0 0 .35rem; }
  .nextday a { color: var(--blue); font-weight: 600; text-decoration: none; }
  .nextday a:hover, .nextday a:focus { text-decoration: underline; }
  .hw .unsolved { color: var(--gold); font-style: italic; font-weight: 600; }
</style>

<div class="pad">

<header class="top">
  <p class="course">Honors Math &nbsp;·&nbsp; Period 3 &nbsp;·&nbsp; Day Three</p>
  <h1>What Lands Perfectly,<br /><em>and How Much Room Is Inside</em></h1>
  <p class="standfirst">In which some radii turn out to be luckier than others, a promise made on the first day is kept, and &pi; arrives by being counted.</p>
</header>

<div class="cast">
  <div class="cast-row"><div class="cast-name">Previously</div><div class="cast-desc">A circle is the dots nearest a given distance from the middle, and it is never wrong by more than half a unit. Nobody has measured anything. On day one Mrs. Feeney boxed the word <em>nought</em> in the corner of the board and promised to come back to it. <a href="index.html">&larr; days one and two</a></div></div>
  <div class="cast-row"><div class="cast-name">Mrs. Feeney</div><div class="cast-desc">Nineteen years of eighth grade. Has never once written &ldquo;because I said so&rdquo; on a board.</div></div>
  <div class="cast-row"><div class="cast-name">Ralphie</div><div class="cast-desc">Front row. Proved something yesterday and has not entirely got over it.</div></div>
  <div class="cast-row"><div class="cast-name">Popovich</div><div class="cast-desc">Back row, hood up. Still waiting on the nought.</div></div>
  <div class="cast-row"><div class="cast-name">Nell</div><div class="cast-desc">By the window. Has not said anything since Tuesday.</div></div>
</div>

<!-- 00 -->
<section>
  <h2><span class="n">01</span> Somebody found it on the bus</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Number three. Something that obeys all our rules and is not the circle. Who has it?</p>
  </div></div>

  <div class="line"><div class="beat">(Nothing.)</div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says">
    <p>I tried for an hour. Everything I drew broke one of them. If I left a column out it wasn't Complete, if I put a dot too far out it wasn't Sound &mdash;</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>That is the correct way to fail at it, and I mean that. Anybody else.</p>
  </div></div>

  <div class="line"><div class="beat">(A long pause. Then, from the window, without looking up:)</div></div>

  <div class="line"><div class="who n">Nell</div><div class="says"><p>Draw all of them.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>&hellip;Say that again.</p></div></div>

  <div class="line"><div class="who n">Nell</div><div class="says">
    <p>Every dot that's allowed. Don't choose. The first rule says which dots you're <em>allowed</em> to use, so use all of them.</p>
  </div></div>

  <div class="line"><div class="beat">(Mrs. Feeney puts down the register and goes to the board.)</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Sound. Every dot we drew is a dot we were allowed to draw &mdash; we only drew allowed ones, so yes.</p>
    <p>Complete. Is any column empty? We drew <em>everything</em>. No.</p>
    <p>Symmetric. We drew every allowed dot, and the mirror of an allowed dot is allowed. So yes.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>It passes.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>It passes. Now look at it.</p></div></div>

  <figure>
    <div class="plate"><img src="__S5__" alt="Two rings side by side at radius 25, the left one a thin circle of 140 dots and the right one 168 dots with the extra ones in red, making the rim visibly lumpy and several dots thick" /></div>
    <figcaption><span class="pn">Fig. 1 &middot; screen</span><span class="pt">Both obey Sound, Complete and Symmetric. The red dots break no rule anyone wrote down. At radius twenty-five the rim reaches five dots thick.</span></figcaption>
  </figure>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>That's not a circle. That's a stripe.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>It is a stripe, and it is a stripe that obeys every single thing we wrote down yesterday. So we did not write down what we meant.</p>
    <p>Popovich. What did you actually say, on the first day, when I asked how to pick a dot?</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Take the nearest one.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>And what does our first rule say?</p></div></div>

  <div class="line"><div class="beat">(Popovich reads it off the board twice before he answers.)</div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>&hellip;That it's near enough.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><em>Near enough.</em> You said <em>nearest</em> and we wrote down <em>near enough</em>, and those are not the same sentence. One of them picks a dot. The other one hands out permission slips.</p>
    <p>Nell's stripe walked straight through the gap between them.</p>
  </div></div>

  <div class="line"><div class="keybox"><span class="lbl">What a specification is for</span><p>Nobody made a mistake yesterday. Every rule we wrote is true, and the program we checked really does obey them. What we got wrong was <span class="exact">weaker than what we meant</span> &mdash; and you cannot see that by staring at it. You see it when something obeys the rules and is obviously wrong.</p><p>That is the whole job. Not catching a liar. Catching yourself.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>So. Fourth rule. Nell, it's yours, say it.</p></div></div>

  <div class="line"><div class="who n">Nell</div><div class="says">
    <p>For every column, keep the dot whose total is closest to the target. Not one that's close. The closest one.</p>
  </div></div>

  <div class="line"><div class="code spec">
    <span class="attrib">The fourth rule</span>
<pre><span class="cm">\* it did not merely use allowed dots. in each column it</span>
<span class="cm">\* used the BEST one. this is what we meant all along.</span>
Nearest(drawn) == \A x \in -R..R : \A y \in -R..R :
                    &lt;&lt;x, y&gt;&gt; \in drawn =&gt;
                      \A z \in -R..R :
                        Gap(x, y) =&lt; Gap(x, z)</pre>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>And it does the job. Add that rule and the stripe fails immediately &mdash; every red dot on that screen has a better dot sitting in its own column.</p>
    <p><span class="stage">(to Nell)</span> You have been in this room for two days without saying a word.</p>
  </div></div>

  <div class="line"><div class="who n">Nell</div><div class="says"><p>I was listening.</p></div></div>

  <div class="line"><div class="beat">(Ralphie looks like he wants to say something and, wisely, doesn't.)</div></div>
</section>

<!-- 05 -->
<section>
  <h2><span class="n">02</span> The dots that land perfectly</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Back to Ralphie's twelve. Most dots on our ring are near-misses &mdash; off by a bit, under half. But some land <span class="exact">dead on</span>. Ralphie found six-eight-ten without knowing what he had. What did you have, Ralphie?</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;A three-four-five triangle. Doubled.</p></div></div>

  <figure>
    <div class="boardshot"><img src="__B8__" alt="The radius 5 ring with its twelve exactly-landing dots marked, and a 3-4-5 triangle drawn from the centre to one of them" /></div>
    <figcaption><span class="pn hand">Fig. 2 &middot; board</span><span class="pt">Radius five, worked by hand. Twelve dots land perfectly, and eight of them are the same 3-4-5 triangle turned around.</span></figcaption>
  </figure>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Doubled. So the dots that land perfectly on a circle of radius <span class="m">r</span> are exactly the right triangles with whole-number sides and hypotenuse <span class="m">r</span>. Circles and triangles are the same question wearing different hats, and nobody tells you that until today.</p>
    <p>Here's the fun part: some radii are luckier than others.</p>
  </div></div>

  <div class="line"><div class="tablewrap"><table>
    <thead><tr><th>Radius</th><th>Dots landing exactly</th><th>Why</th></tr></thead>
    <tbody>
      <tr><td>5</td><td class="g">12</td><td>3-4-5, and the four axis dots</td></tr>
      <tr><td>10</td><td class="g">12</td><td>the same triangle, doubled</td></tr>
      <tr><td>13</td><td class="g">12</td><td>5-12-13</td></tr>
      <tr><td>25</td><td class="g">20</td><td>7-24-25 <em>and</em> 15-20-25</td></tr>
      <tr><td>65</td><td class="g">36</td><td>four different triangles at once</td></tr>
    </tbody>
  </table></div></div>

  <figure>
    <div class="plate"><img src="__S3__" alt="Three rings side by side at radii 5, 25 and 65, with the exactly-landing dots picked out in gold: twelve, twenty and thirty-six of them" /></div>
    <figcaption><span class="pn">Fig. 3 &middot; screen</span><span class="pt">Five, twenty-five, sixty-five. The gold dots land perfectly. A radius is lucky when it carries several whole-number triangles at once.</span></figcaption>
  </figure>

  <figure>
    <div class="plate"><img src="__P2__" alt="Circle of radius 25 in blue dots with twenty gold dots marking the points that land exactly on the radius" /></div>
    <figcaption><span class="pn">Fig. 4 &middot; screen</span><span class="pt">Radius 25. The blue dots are nearest-fits. The <span style="color:var(--gold);font-weight:600">gold</span> ones land perfectly &mdash; twenty of them, because 25 is a lucky radius that carries two different whole-number triangles. Sixty-five is luckier still, with four.</span></figcaption>
  </figure>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>You said you'd tell me what the nought means.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(going back to the boxed word)</span> The other way of writing the algorithm keeps a running number that asks &ldquo;is the <em>diagonal</em> dot outside the ring or inside it?&rdquo; And it lands on nought exactly when that dot is on the ring. Neither outside nor inside. <em>On</em> it.</p>
    <p>Which is to say: the running number hits nought precisely at the gold dots. At five. At ten. At fifteen, seventeen, twenty, twenty-five. The radii we have just been calling lucky are the radii where that program has to stop and think.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>So the awkward case and the nice case are the same case.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>The same case, seen from two sides. That happens a great deal and it never stops being worth noticing.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Is there a radius where <em>all</em> of them land?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(pause)</span> No. And I want you to sit with why not, because the reason is good. You can always find a radius with <em>more</em> perfect dots &mdash; there's no ceiling. But the ring keeps getting longer as you grow it, and the perfect dots never keep up. You can have a thousand of them. You can't have all of them.</p>
  </div></div>
</section>

<!-- 05 -->
<section>
  <h2><span class="n">03</span> How much room is inside</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Last thing today, and it's the one I'd keep if they made me throw the rest out.</p>
    <p>Forget the rim. How much <em>room</em> is inside a circle? In our world that question has an embarrassingly literal answer. Count the dots.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>Just&hellip; count them?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Just count them. Every dot whose distance from the middle is ten or less. Radius ten. Go.</p>
  </div></div>

  <figure>
    <div class="plate"><img src="__P3__" alt="A filled disk of 317 blue lattice dots at radius 10" /></div>
    <figcaption><span class="pn">Fig. 5 &middot; screen</span><span class="pt">Radius 10. Three hundred and seventeen dots. You can count them by hand in about four minutes, and two students in every class always do.</span></figcaption>
  </figure>

  <div class="line"><div class="beat">(Four minutes. Ralphie finishes first and is wrong. Popovich finishes second and isn't.)</div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Three hundred seventeen.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Three hundred seventeen. Now divide it by the radius squared. By a hundred.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Three point one seven.</p></div></div>

  <div class="line"><div class="beat">(Mrs. Feeney says nothing. She writes 3.17 on the board and lets it sit there.)</div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;That's &pi;.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>That's &pi;. You just counted dots on graph paper and &pi; fell out. Do a bigger one and it gets sharper.</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>Can I just write it? I don't want to count to thirty thousand.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Please. Nobody in the history of this room has ever wanted to count to thirty thousand.</p></div></div>

  <div class="line"><div class="code">
    <span class="attrib">Ralphie's laptop</span>
<pre><span class="kw">def</span> count_dots(r):
    n = 0
    <span class="kw">for</span> x <span class="kw">in</span> range(-r, r+1):
        <span class="kw">for</span> y <span class="kw">in</span> range(-r, r+1):
            <span class="kw">if</span> x*x + y*y &lt;= r*r:
                n = n + 1
    <span class="kw">return</span> n

<span class="kw">for</span> r <span class="kw">in</span> [10, 100, 1000]:
    print(r, count_dots(r), count_dots(r) / (r*r))</pre>
  </div></div>

  <div class="line"><div class="out">10 317 3.17
100 31417 3.1417
1000 3141549 3.141549</div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>Three point one four one five four nine. <span class="stage">(pause)</span> Can I do ten thousand?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Try it.</p></div></div>

  <div class="line"><div class="beat">(A minute goes by. Then another one.)</div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>It's&hellip; still going.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>You're checking every dot in the whole square. That's four hundred million of them and you're throwing most away.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>How else would you do it?</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>Take one column at a time. For a given <span class="m">x</span>, you already know how tall the column is &mdash; it's however far up you can go before you leave the circle. You don't have to <em>check</em> each dot in it. You can just say how many there are.</p>
  </div></div>

  <div class="line"><div class="code">
    <span class="attrib">Popovich, over his shoulder</span>
<pre><span class="kw">from</span> math <span class="kw">import</span> isqrt

<span class="kw">def</span> count_dots(r):
    n = 0
    <span class="kw">for</span> x <span class="kw">in</span> range(-r, r+1):
        <span class="cm"># the whole column at once, no inner loop</span>
        n = n + 2*isqrt(r*r - x*x) + 1
    <span class="kw">return</span> n</pre>
  </div></div>

  <figure>
    <div class="boardshot"><img src="__B9__" alt="The disk of dots at radius 10 with four columns picked out and their heights measured as 17, 21, 17 and 9" /></div>
    <figcaption><span class="pn hand">Fig. 6 &middot; board</span><span class="pt">What Popovich did instead. You never look at a dot: you measure how tall each column is and add the heights.</span></figcaption>
  </figure>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(reading it)</span> Popovich. <span class="m">isqrt</span>. That's the whole-number square root &mdash; it throws the decimal away.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>We don't need the decimal. You can't have two-thirds of a dot.</p></div></div>

  <div class="line"><div class="beat">(Mrs. Feeney looks at the ceiling for a second, the way people do when a lesson they have taught nineteen times gets improved by a fifteen-year-old.)</div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Ralphie. Run his.</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;It already printed.</p></div></div>

  <div class="line"><div class="tablewrap"><table>
    <thead><tr><th>Radius</th><th>Dots inside</th><th>Dots &divide; r&sup2;</th><th>Correct digits</th></tr></thead>
    <tbody>
      <tr><td>10</td><td>317</td><td class="b">3.17</td><td>2</td></tr>
      <tr><td>100</td><td>31,417</td><td class="b">3.1417</td><td>4</td></tr>
      <tr><td>1,000</td><td>3,141,549</td><td class="b">3.141549</td><td>5</td></tr>
      <tr><td>10,000</td><td>314,159,053</td><td class="b">3.14159053</td><td>6</td></tr>
      <tr><td>&nbsp;</td><td>&nbsp;</td><td class="g">3.14159265&hellip;</td><td>&pi;</td></tr>
    </tbody>
  </table></div></div>

  <figure>
    <div class="plate"><img src="__S4__" alt="A line chart of dots inside divided by radius squared, dropping from above 3.2 and settling onto a dashed line marked pi" /></div>
    <figcaption><span class="pn">Fig. 7 &middot; screen</span><span class="pt">The same table, drawn. It is not creeping towards &pi; by luck &mdash; counting dots is what &pi; <em>is</em>.</span></figcaption>
  </figure>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>So here is what &pi; is, and I'd like you to hear it as a piece of good news rather than a disappointment.</p>
    <p>&pi; is not a mysterious endless decimal that somebody handed down and you have to take on faith. <strong>&pi; is the answer to a counting question.</strong> How many dots fit in a circle, compared to the square of its radius. That's it. That's the whole thing.</p>
    <p>And you can get as many digits of it as you are ever going to need by counting dots on a big enough sheet of graph paper. Nothing endless is required to do that. Just a bigger sheet.</p>
  </div></div>
</section>

<!-- 06 -->
<section>
  <h2><span class="n">04</span> The bell</h2>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>How many digits <em>do</em> you need?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>How many did you get?</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;Six. At ten thousand.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Six, off a morning's counting. So make a guess. How many would you want before you'd let somebody build a bridge with it?</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;Twenty?</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Fewer. Nobody measures a bridge that well.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Popovich is closer, and I am not going to tell you the number because <em>I do not know it</em>. Not exactly. I know it is smaller than people expect, and I know I have never once needed more than a handful of them.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>You don't know?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>I have spent fifty minutes telling you not to believe a number because a grown-up said it. I am not going to spoil that in the last two.</p>
    <p><span class="stage">(writing it up)</span> Find out. Somebody flies things to other planets for a living and they will have written down what they use. Bring me the number and bring me where you got it.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>And if nobody's written it down?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Then that is a much more interesting Thursday than the one I had planned.</p>
  </div></div>

  <div class="line"><div class="beat">(bell)</div></div>

  <div class="hw">
    <h3>Homework — the whole assignment</h3>
    <ol>
      <li>Find all twelve dots exactly 13 from the middle. One of them is not a triangle you've met before. Which triangle is it?</li>
      <li>Count the dots inside a circle of radius 20. Divide by 400. Write down how close you got, and then write down one sentence about why it isn't closer.</li>
      <li>Radius 25 has twenty perfect dots and radius 24 has four. Both are perfectly ordinary numbers. Go find out what 25 has that 24 doesn't. <em>Hint: it isn't about the 25.</em> It's about 5.</li>
    </ol>
  </div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Popovich. Hang on a second.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p><span class="stage">(waiting)</span></p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Half a unit. You got there in about nine seconds, and it took me until my second year of teaching to understand why that one sentence settles the whole argument.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>It's not that hard. If it were farther, you'd pick the other one.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>I know. That's what I'm telling you.</p></div></div>

  <div class="line"><div class="beat">(He thinks about that on the way to the door.)</div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p><span class="stage">(from the hall)</span> &hellip;Does my grandfather actually have to come in?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Ask him. Fourth period. Tell him to bring the chain.</p></div></div>
</section>


  <div class="line"><div class="nextday">
    <p><a href="index.html">&larr; back to days one and two</a></p>
  </div></div>

<footer class="colo">
  <h3>Checked before printing</h3>
  <p>Every number here was computed rather than remembered: the twelve dots at radius 5, 10 and 13; the twenty at radius 25 and thirty-six at 65; all 624 dots at radius 110 sitting inside the integer band, four times the squares between 219&sup2; and 221&sup2; &mdash; established without taking a square root; the dot counts 317 / 31,417 / 3,141,549 / 314,159,053 and the &pi; digits they yield; and the integer-only drawing rule, verified to place its dots in the same spots as the square-root method at every radius tested. Ralphie's parity argument is also carried in the specification as an invariant, <span style="font-family:var(--mono)">NoTies</span>, model-checked at eight radii &mdash; though the argument itself settles every radius at once.</p>
  <p>The same parity fact makes the drawing algorithm deterministic: its decision variable is odd at every step, so it never lands on nought and the <span style="font-family:var(--mono)">otherwise</span> branch never breaks a tie. Checked at every radius from 2 to 1999. That is a fact about the <em>midpoint</em> variant, which is what this lesson teaches.</p>
  <p>Bresenham's own 1977 algorithm is a different procedure &mdash; a decision variable evaluated at the diagonal neighbour, initialised <span style="font-family:var(--mono)">2 &minus; 2R</span> rather than <span style="font-family:var(--mono)">3 &minus; 2r</span>. His <em>does</em> land on zero, at 143 of the radii from 2 to 399, and he handles it explicitly as his &ldquo;case 5&rdquo;, proving the move stays forced. It is zero exactly when a lattice point sits perfectly on the ring &mdash; so the radii that trouble his algorithm are precisely the lucky ones. The two algorithms agree on their output at every radius tested to 200, but <span style="font-family:var(--mono)">3 &minus; 2r</span> is not his, and calling it &ldquo;Bresenham's circle algorithm&rdquo;, as almost everyone does, is a misattribution.</p>
  <p>Ralphie's homework, for anyone who wants it now: NASA JPL reports working to about fifteen digits for interplanetary navigation. Thirty-eight would draw a circle round the observable universe to within a hydrogen atom. Mrs. Feeney does not know either figure, and would rather he looked them up than took them from her &mdash; which is the only reason they are down here and not up there.</p>

  <h3 style="margin-top:2rem">Whose ideas these are</h3>
  <p><strong>The drawing algorithm</strong> is Bresenham's circle algorithm &mdash; J. E. Bresenham, &ldquo;A Linear Algorithm for Incremental Digital Display of Circular Arcs&rdquo;, <em>Communications of the ACM</em> 20(2), February 1977, 100&ndash;106. Not the better-known 1965 paper (&ldquo;Algorithm for computer control of a digital plotter&rdquo;, <em>IBM Systems Journal</em> 4(1), 25&ndash;30), which draws lines; the circle came twelve years afterwards. The variant used here is usually called the midpoint circle algorithm.</p>
  <p><strong>Counting dots to get &pi;</strong> is the Gauss circle problem. <strong>Which radii carry dots that land exactly</strong> is the theory of sums of two squares, from Fermat and Jacobi. <strong>Writing the blueprint before the program</strong>, and the observation that a specification is not written in the material the thing is built from, is Leslie Lamport &mdash; &ldquo;Thinking Above the Code&rdquo;, Microsoft Research Faculty Summit, 2014 &mdash; and the notation of the blueprint is his TLA+.</p>
  <p>None of the mathematics in this lesson is new. The only thing arranged here is the order.</p>
</footer>

</div>
"""

for k, f in [('__P1__','p1_circle.png'), ('__P2__','p2_exact.png'), ('__P3__','p3_count.png'),
             ('__B1__','board_01_world.png'), ('__B2__','board_02_twelve.png'),
             ('__B3__','board_03_halfdot.png'), ('__B4__','board_04_nearest.png'),
             ('__B5__','board_05_mirrors.png'), ('__B6__','board_06_squares.png'), ('__B7__','board_07_badrule.png'),
             ('__B8__','board_08_lucky5.png'), ('__B9__','board_09_columns.png'),
             ('__S1__','s1_sabotage.png'), ('__S2__','s2_where_it_bites.png'),
             ('__S3__','s3_lucky.png'), ('__S4__','s4_counting_pi.png'), ('__B10__','board_10_pile.png'),
             ('__B11__','board_11_tiework.png'), ('__S5__','s5_the_band.png')]:
    DOC1 = DOC1.replace(k, img(f))
    DOC2 = DOC2.replace(k, img(f))
# Canonical output is docs/index.html, which is what GitHub Pages serves.
docs = HERE.parent / 'docs'
for name, doc in (('index.html', DOC1), ('counting.html', DOC2)):
    p = docs / name
    p.write_text(doc)
    print(f'wrote {p}  {p.stat().st_size/1024:.0f} KB')
