import base64, pathlib

HERE = pathlib.Path(__file__).resolve().parent
S = HERE / 'plates'

def img(n):
    return 'data:image/png;base64,' + base64.b64encode((S / n).read_bytes()).decode()

HTML = r"""<title>Honors Math, Period 3 — Day One: Circles</title>
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
  figcaption {
    font-family: var(--sans); font-size: .78rem; line-height: 1.6; color: var(--muted);
    margin-top: .8rem; display: grid; grid-template-columns: 5rem 1fr; gap: 0 1.2rem;
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
</style>

<div class="pad">

<header class="top">
  <p class="course">Honors Math &nbsp;·&nbsp; Period 3 &nbsp;·&nbsp; First Day</p>
  <h1>Circles, and the<br /><em>Half-Dot Problem</em></h1>
  <p class="standfirst">In which nothing is infinite, nobody uses a square root, and &pi; turns up anyway &mdash; by being counted.</p>
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

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Correct, and thank you for not being polite about it. Twelve dots is not a circle. So we have a problem, and here it is:</p></div></div>

  <div class="line"><div class="keybox"><span class="lbl">The trouble</span><p>Almost no dot is <em>exactly</em> ten from the middle. If we insist on &ldquo;exactly,&rdquo; our circles have twelve dots in them and enormous holes. A rule that strict doesn't draw &mdash; it just says no.</p></div></div>
</section>

<!-- 02 -->
<section>
  <h2><span class="n">02</span> How wrong are we willing to be?</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>So we loosen it, exactly one notch. New rule: <strong>for each column, take the dot nearest to ten away.</strong> Not the exact one. The nearest one.</p>
  </div></div>

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

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Half a dot.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Half a dot.</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Because if it were more than half, a different dot would be closer, and you'd have picked that one instead.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(to the room)</span> Say that back to yourselves tonight until it's boring. That is the entire argument.</p>
  </div></div>

  <div class="line"><div class="keybox"><span class="lbl">The answer to the objection</span><p>Our circle is never off by more than <span class="exact">half a dot</span>. Not on average &mdash; <em>ever</em>. Not at radius ten, not at radius ten thousand, not at radius the-size-of-the-county. The error doesn't grow, because &ldquo;nearest&rdquo; means what it says.</p></div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>Wait, it doesn't get worse when the circle gets bigger?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Not by a hair. Bigger circle, more dots, same half-dot. <span class="stage">(beat)</span> I checked it out to radius one hundred and ten this morning &mdash; worst dot on the whole ring was off by <span class="m">0.48</span>. It will still be under a half when you're my age.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Huh.</p></div></div>
</section>

<!-- 03 -->
<section>
  <h2><span class="n">03</span> Drawing it, without a single square root</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Now the good part. To find the nearest dot you'd think we need square roots &mdash; the square root of a hundred minus <span class="m">x</span> squared, every column, and most of those roots are horrible.</p>
    <p>We don't. Watch. Start at the top of the circle. Step one to the right. Ask one question: <em>am I still closer to the ring if I stay, or if I drop down one?</em> Answer it. Step again.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>How do you answer it without the square root?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>You keep a running number and add to it. When it goes negative you stay; when it doesn't, you drop. The amount you add is built out of the numbers you already have.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Copy this down. It is the entire circle, and I want you to notice what is <em>not</em> in it.</p>
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
    <p>No square root. No &pi;. No decimal point <em>anywhere</em> &mdash; every number in there is a whole number from start to finish. Adding, subtracting, doubling. That's the whole toolkit.</p>
    <p>And look at the loop condition: <span class="m">while x &lt;= y</span>. It stops at the diagonal. You only ever compute one eighth of the ring &mdash; the other seven eighths are mirror images, which is what that list of eight pairs is doing. You get them for free.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>That's how a computer draws a circle?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>That is <em>exactly</em> how a computer draws a circle. Every circle you have ever seen on a screen in your life was made this way. Nobody's graphics card has ever once taken a square root to draw a rim.</p>
  </div></div>

  <figure>
    <div class="plate"><img src="__P1__" alt="A circle of radius 110 drawn as blue lattice dots, visually smooth and round" /></div>
    <figcaption><span class="pn">Plate I</span><span class="pt">Radius 110. Six hundred and twenty-four dots, placed using nothing but addition and subtraction. No dot is more than half a step off the true ring &mdash; and that is a promise that holds at every radius, not a lucky outcome at this one.</span></figcaption>
  </figure>

  <div class="line"><div class="who p">Popovich</div><div class="says">
    <p>My grandfather laid out roads. County roads, before I was born. He had a steel chain and a notebook and he never took a square root in his life.</p>
  </div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Are the roads still there?</p></div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>I ride my bike on one.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Then your grandfather is the whole lesson and I'd like him to come talk to fourth period.</p>
  </div></div>
</section>

<!-- 04 -->
<section>
  <h2><span class="n">04</span> The dots that land perfectly</h2>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Back to Ralphie's twelve. Most dots on our ring are near-misses &mdash; off by a bit, under half. But some land <span class="exact">dead on</span>. Ralphie found six-eight-ten without knowing what he had. What did you have, Ralphie?</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;A three-four-five triangle. Doubled.</p></div></div>

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
    <div class="plate"><img src="__P2__" alt="Circle of radius 25 in blue dots with twenty gold dots marking the points that land exactly on the radius" /></div>
    <figcaption><span class="pn">Plate II</span><span class="pt">Radius 25. The blue dots are nearest-fits. The <span style="color:var(--gold);font-weight:600">gold</span> ones land perfectly &mdash; twenty of them, because 25 is a lucky radius that carries two different whole-number triangles. Sixty-five is luckier still, with four.</span></figcaption>
  </figure>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>Is there a radius where <em>all</em> of them land?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(pause)</span> No. And I want you to sit with why not, because the reason is good. You can always find a radius with <em>more</em> perfect dots &mdash; there's no ceiling. But the ring keeps getting longer as you grow it, and the perfect dots never keep up. You can have a thousand of them. You can't have all of them.</p>
  </div></div>
</section>

<!-- 05 -->
<section>
  <h2><span class="n">05</span> How much room is inside</h2>

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
    <figcaption><span class="pn">Plate III</span><span class="pt">Radius 10. Three hundred and seventeen dots. You can count them by hand in about four minutes, and two students in every class always do.</span></figcaption>
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

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>So here is what &pi; is, and I'd like you to hear it as a piece of good news rather than a disappointment.</p>
    <p>&pi; is not a mysterious endless decimal that somebody handed down and you have to take on faith. <strong>&pi; is the answer to a counting question.</strong> How many dots fit in a circle, compared to the square of its radius. That's it. That's the whole thing.</p>
    <p>And you can get as many digits of it as you are ever going to need by counting dots on a big enough sheet of graph paper. Nothing endless is required to do that. Just a bigger sheet.</p>
  </div></div>
</section>

<!-- 06 -->
<section>
  <h2><span class="n">06</span> The bell</h2>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>How many digits <em>do</em> you need?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>Wonderful question, and the answer is smaller than anyone expects. The people who fly spacecraft to other planets use about <span class="exact">fifteen</span>.</p>
  </div></div>

  <div class="line"><div class="who">Ralphie</div><div class="says"><p>Fifteen? That's it?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p>That's it. And if you wanted to draw a circle around the entire observable universe and have it come out right to within the width of a single hydrogen atom &mdash; the whole universe, one atom &mdash; you'd need about <span class="exact">thirty-eight</span>.</p>
  </div></div>

  <div class="line"><div class="beat">(Nobody says anything for a second.)</div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>So the rest of them are for what?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says">
    <p><span class="stage">(smiling)</span> Curiosity. Which is a perfectly good reason and I don't want to hear it slandered. But no bridge has ever needed the fortieth digit, and no bridge ever will.</p>
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
    <p>Half a dot. You got there in about nine seconds, and it took me until my second year of teaching to understand why that one sentence settles the whole argument.</p>
  </div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p>It's not that hard. If it were farther, you'd pick the other one.</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>I know. That's what I'm telling you.</p></div></div>

  <div class="line"><div class="beat">(He thinks about that on the way to the door.)</div></div>

  <div class="line"><div class="who p">Popovich</div><div class="says"><p><span class="stage">(from the hall)</span> &hellip;Does my grandfather actually have to come in?</p></div></div>

  <div class="line"><div class="who f">Mrs. Feeney</div><div class="says"><p>Ask him. Fourth period. Tell him to bring the chain.</p></div></div>
</section>

<footer class="colo">
  <h3>Checked before printing</h3>
  <p>Every number here was computed rather than remembered: the twelve dots at radius 5, 10 and 13; the twenty at radius 25 and thirty-six at 65; the worst-case error of 0.48 of a step at radius 110; the dot counts 317 / 31,417 / 3,141,549 / 314,159,053 and the &pi; digits they yield; and the integer-only drawing rule, verified to place its dots in the same spots as the square-root method at every radius tested.</p>
  <p>The thirty-eight digits: circumference of the observable universe (radius ~46 billion light years) to a precision of one hydrogen-atom radius needs 38 significant figures. Fifteen digits is the working precision NASA JPL reports using for interplanetary navigation.</p>
</footer>

</div>
"""

HTML = HTML.replace('__P1__', img('p1_circle.png')).replace('__P2__', img('p2_exact.png')).replace('__P3__', img('p3_count.png'))
out = HERE / 'day-one-circles.html'
out.write_text(HTML)
print('wrote', out, f'{out.stat().st_size/1024:.0f} KB')
