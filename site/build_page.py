import base64, pathlib

HERE = pathlib.Path(__file__).resolve().parent
SCRATCH = HERE / 'plates'

def img(name):
    b = (SCRATCH / f'web_{name}.png').read_bytes()
    return 'data:image/png;base64,' + base64.b64encode(b).decode()

HTML = r"""<title>Honors Algebra, Period 3 — Day One: Circles</title>
<style>
  :root {
    --paper:      #E9EAE3;
    --paper-2:    #DFE1D8;
    --ink:        #191B18;
    --state:      #1F4E96;
    --correction: #A3392B;
    --muted:      #6E7269;
    --rule:       #C3C6BA;
    --plate-bg:   #0D1117;
    --serif: Charter, "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
    --mono: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --paper:      #14171A;
      --paper-2:    #1B1F23;
      --ink:        #DDE1DC;
      --state:      #6FA8FF;
      --correction: #E0705C;
      --muted:      #868C84;
      --rule:       #2C3238;
    }
  }
  :root[data-theme="dark"] {
    --paper:#14171A; --paper-2:#1B1F23; --ink:#DDE1DC;
    --state:#6FA8FF; --correction:#E0705C; --muted:#868C84; --rule:#2C3238;
  }
  :root[data-theme="light"] {
    --paper:#E9EAE3; --paper-2:#DFE1D8; --ink:#191B18;
    --state:#1F4E96; --correction:#A3392B; --muted:#6E7269; --rule:#C3C6BA;
  }

  body {
    background: var(--paper);
    color: var(--ink);
    font-family: var(--serif);
    font-size: 17px;
    line-height: 1.62;
    margin: 0;
    padding: 0 1.5rem 6rem;
    -webkit-font-smoothing: antialiased;
  }
  .sheet { max-width: 62rem; margin: 0 auto; }

  /* ---------- masthead ---------- */
  .masthead {
    border-bottom: 2.5px solid var(--ink);
    padding: 3.5rem 0 1rem;
    margin-bottom: .5rem;
  }
  .ministry {
    font-family: var(--mono);
    font-size: .68rem;
    letter-spacing: .22em;
    text-transform: uppercase;
    color: var(--state);
    margin: 0 0 1.6rem;
  }
  .masthead h1 {
    font-family: var(--serif);
    font-weight: 600;
    font-size: clamp(2rem, 5.5vw, 3.1rem);
    line-height: 1.08;
    letter-spacing: -.015em;
    text-wrap: balance;
    margin: 0 0 1.1rem;
  }
  .masthead h1 em { font-style: italic; color: var(--state); }
  .docmeta {
    display: flex; flex-wrap: wrap; gap: .5rem 2.2rem;
    font-family: var(--mono); font-size: .7rem;
    letter-spacing: .1em; text-transform: uppercase;
    color: var(--muted); padding-bottom: .4rem;
  }

  /* ---------- cast ---------- */
  .cast {
    border-bottom: 1px solid var(--rule);
    padding: 2.2rem 0 2rem; margin-bottom: 3rem;
    display: grid; gap: 1.1rem;
  }
  .cast-row { display: grid; grid-template-columns: 9.5rem 1fr; gap: 0 2rem; }
  .cast-name {
    font-family: var(--mono); font-size: .72rem; letter-spacing: .13em;
    text-transform: uppercase; color: var(--state); padding-top: .28em;
  }
  .cast-desc { font-size: .95rem; color: var(--ink); max-width: 46rem; }

  /* ---------- sections ---------- */
  section { margin: 0 0 3.4rem; }
  h2 {
    font-family: var(--mono);
    font-size: .74rem; letter-spacing: .19em; text-transform: uppercase;
    color: var(--ink); font-weight: 600;
    margin: 0 0 1.9rem; padding-bottom: .7rem;
    border-bottom: 1px solid var(--rule);
    display: flex; gap: 1.2rem; align-items: baseline;
  }
  h2 .sec-no { color: var(--state); font-variant-numeric: tabular-nums; }

  /* ---------- dialogue ---------- */
  .line {
    display: grid; grid-template-columns: 9.5rem 1fr; gap: 0 2rem;
    margin-bottom: 1.15rem;
  }
  .who {
    font-family: var(--mono); font-size: .72rem; letter-spacing: .13em;
    text-transform: uppercase; color: var(--state);
    padding-top: .35em; text-align: left;
  }
  .who.pop  { color: var(--correction); }
  .who.feen { color: var(--ink); }
  .says { max-width: 40rem; }
  .says p { margin: 0 0 .85rem; }
  .says p:last-child { margin-bottom: 0; }
  .stage { color: var(--muted); font-style: italic; }
  .beat {
    grid-column: 2; color: var(--muted); font-style: italic;
    font-size: .93rem; margin: 1.4rem 0 1.5rem; max-width: 40rem;
  }

  /* ---------- margin note (Popovich's pen) ---------- */
  .marginal {
    grid-column: 2; max-width: 27rem;
    margin: 1.5rem 0 1.7rem;
    padding: .85rem 1.1rem;
    border-left: 2px solid var(--correction);
    color: var(--correction);
    font-family: var(--mono); font-size: .76rem; line-height: 1.55;
    transform: rotate(-.35deg);
    background: color-mix(in srgb, var(--correction) 6%, transparent);
  }
  .marginal b {
    display: block; font-weight: 600; letter-spacing: .1em;
    text-transform: uppercase; font-size: .66rem; margin-bottom: .35rem;
    opacity: .8;
  }

  /* ---------- math + tables ---------- */
  .eq {
    grid-column: 2; font-family: var(--mono); font-size: .93rem;
    background: var(--paper-2); border-left: 2px solid var(--state);
    padding: .95rem 1.2rem; margin: 1.3rem 0; max-width: 40rem;
    overflow-x: auto;
  }
  .tablewrap { grid-column: 2; overflow-x: auto; margin: 1.5rem 0 1.8rem; max-width: 44rem; }
  table { border-collapse: collapse; font-family: var(--mono); font-size: .78rem; width: 100%; }
  th, td {
    text-align: left; padding: .5rem .95rem .5rem 0;
    border-bottom: 1px solid var(--rule); font-variant-numeric: tabular-nums;
    white-space: nowrap;
  }
  th {
    font-size: .65rem; letter-spacing: .13em; text-transform: uppercase;
    color: var(--muted); font-weight: 600; border-bottom: 1.5px solid var(--ink);
  }
  td.hi { color: var(--state); font-weight: 600; }

  /* ---------- plates ---------- */
  figure { margin: 2.6rem 0; }
  .plate {
    background: var(--plate-bg);
    border: 1px solid var(--rule);
    padding: .7rem;
    display: grid; gap: .7rem;
  }
  .plate.two { grid-template-columns: repeat(2, 1fr); }
  .plate.strip { grid-template-columns: repeat(4, 1fr); }
  .plate img { width: 100%; height: auto; display: block; }
  figcaption {
    font-family: var(--mono); font-size: .7rem; line-height: 1.6;
    color: var(--muted); margin-top: .8rem;
    display: grid; grid-template-columns: 5.5rem 1fr; gap: 0 1.2rem;
  }
  figcaption .plateno {
    letter-spacing: .13em; text-transform: uppercase; color: var(--state);
  }
  figcaption .platetxt { max-width: 40rem; }

  /* ---------- homework ---------- */
  .homework {
    border: 1.5px solid var(--ink); padding: 1.8rem 2rem; margin: 2.4rem 0;
    background: var(--paper-2);
  }
  .homework h3 {
    font-family: var(--mono); font-size: .7rem; letter-spacing: .18em;
    text-transform: uppercase; margin: 0 0 1.3rem; color: var(--state);
  }
  .homework ol { margin: 0; padding-left: 1.3rem; display: grid; gap: .95rem; }
  .homework li { max-width: 40rem; padding-left: .3rem; }
  .homework .unsolved { color: var(--correction); font-style: italic; }

  /* ---------- colophon ---------- */
  .colophon {
    border-top: 2.5px solid var(--ink); margin-top: 4.5rem; padding-top: 1.6rem;
    font-family: var(--mono); font-size: .72rem; line-height: 1.75; color: var(--muted);
  }
  .colophon h3 {
    font-size: .68rem; letter-spacing: .18em; text-transform: uppercase;
    color: var(--ink); margin: 0 0 1rem;
  }
  .colophon p { max-width: 44rem; margin: 0 0 .9rem; }
  .colophon .flag { color: var(--correction); }

  @media (max-width: 760px) {
    body { font-size: 16px; padding: 0 1.1rem 4rem; }
    .line, .cast-row { grid-template-columns: 1fr; gap: .2rem; }
    .who, .cast-name { padding-top: 0; margin-bottom: .1rem; }
    .beat, .marginal, .eq, .tablewrap { grid-column: 1; }
    figcaption { grid-template-columns: 1fr; gap: .3rem; }
    .plate.strip { grid-template-columns: repeat(2, 1fr); }
  }
  @media (prefers-reduced-motion: reduce) {
    * { animation: none !important; transition: none !important; }
  }
</style>

<div class="sheet">

  <header class="masthead">
    <p class="ministry">Ministry of Constructible Mathematics &nbsp;·&nbsp; Approved Curriculum</p>
    <h1>Honors Algebra, Period 3<br /><em>Day One: Circles</em></h1>
    <div class="docmeta">
      <span>Form 8-H / Rev. 19</span>
      <span>Instructor: M. Feeney</span>
      <span>Transcript, unabridged</span>
    </div>
  </header>

  <div class="cast">
    <div class="cast-row">
      <div class="cast-name">Mrs. Feeney</div>
      <div class="cast-desc">Nineteen years teaching the Ultimate Ceiling curriculum. Believes most of it.</div>
    </div>
    <div class="cast-row">
      <div class="cast-name">Ralphie</div>
      <div class="cast-desc">Front row. Has read ahead, and is confident about it.</div>
    </div>
    <div class="cast-row">
      <div class="cast-name">Popovich</div>
      <div class="cast-desc">Back row. His grandfather wrote forty pages about something called <span style="font-family:var(--mono)">&#8477;</span> and was invited to spend eleven years thinking it over in a facility near the mountains.</div>
    </div>
    <div class="cast-row">
      <div class="cast-name">Note</div>
      <div class="cast-desc" style="color:var(--muted)">All arithmetic in this transcript has been checked. Ralphie's has not.</div>
    </div>
  </div>

  <!-- ============ 01 ============ -->
  <section>
    <h2><span class="sec-no">01</span> The definition, and a wrong answer</h2>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>Hello, students! Welcome to Honors Algebra. Settle in, find a seat &mdash; Popovich, an actual seat, thank you.</p>
        <p>Today: circles. Everyone has drawn a circle. Today you learn what a circle <em>is</em>, which is a different thing and a better one. On our grid, a circle is every pair <span style="font-family:var(--mono)">(x, y)</span> satisfying:</p>
      </div>
    </div>

    <div class="line"><div></div><div class="eq" style="grid-column:auto">x&sup2; + y&sup2; &equiv; c &nbsp;&nbsp;(mod p)</div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>That's the whole definition. Now &mdash; the question I want from you is not &ldquo;what does it look like.&rdquo; It's <em>how many points, and what holds them together?</em> Both have exact answers.</p>
      </div>
    </div>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says">
        <p>Mrs. Feeney! Mrs. Feeney. Should we start with how the circle <em>disappears</em> if you pick a bad prime? Like 19? Because 19 leaves a remainder of 3 when you divide by 4, so the circle collapses entirely &mdash;</p>
      </div>
    </div>

    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>No, Ralphie.</p></div></div>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says"><p>&mdash; and that's why we only use good primes like 17, because &mdash; sorry. No?</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p>No. Where did you read that?</p></div>
    </div>

    <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;A tutoring service.</p></div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>Get your money back. Let's count. Everyone take <span style="font-family:var(--mono)">c = 4</span>. Count the points on the 17-clock, then the 19-clock. Popovich, you may use your tablet, I know you were going to anyway.</p>
      </div>
    </div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says"><p><span class="stage">(not looking up)</span> Sixteen and twenty.</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>Sixteen and twenty. Ralphie, 19 is the prime you said had <em>no</em> circle. It has four more points than 17 does. Here is the actual law, and I want it in your notes:</p>
      </div>
    </div>

    <div class="line"><div></div>
      <div class="tablewrap" style="grid-column:auto">
        <table>
          <thead><tr><th>Clock</th><th>Points, c &ne; 0</th><th>At c = 4</th></tr></thead>
          <tbody>
            <tr><td>p &equiv; 1 (mod 4)</td><td class="hi">p &minus; 1</td><td>p=17 &rarr; 16&nbsp;&nbsp;·&nbsp;&nbsp;p=101 &rarr; 100</td></tr>
            <tr><td>p &equiv; 3 (mod 4)</td><td class="hi">p + 1</td><td>p=19 &rarr; 20&nbsp;&nbsp;·&nbsp;&nbsp;p=103 &rarr; 104</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="line"><div class="who">Ralphie</div><div class="says"><p>So the bad primes are&hellip; better?</p></div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>There are no bad primes. There's a law, and it goes one way for half of them and the other way for the rest. That's not a defect, Ralphie, that's the <em>whole subject.</em></p>
      </div>
    </div>
  </section>

  <!-- ============ 02 ============ -->
  <section>
    <h2><span class="sec-no">02</span> Where it really does collapse</h2>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>Now &mdash; Ralphie wasn't hallucinating entirely. Something does collapse. He just had it pinned to the wrong knob. Set <span style="font-family:var(--mono)">c = 0</span>. Radius zero.</p>
      </div>
    </div>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says"><p><span class="stage">(fast)</span> One point! The origin! Zero squared plus zero squared &mdash;</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p>On the 19-clock, yes. Exactly one lonely point. On the 17-clock?</p></div>
    </div>

    <div class="line"><div class="who pop">Popovich</div><div class="says"><p>Thirty-three.</p></div></div>

    <div class="line"><div class="who">Ralphie</div><div class="says"><p><em>Thirty-three?</em> For radius <strong>zero</strong>?</p></div></div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says"><p>It's two lines. They cross at the origin. <span style="font-family:var(--mono)">2p &minus; 1</span>, you're double-counting where they meet.</p></div>
    </div>

    <figure>
      <div class="plate two">
        <img src="__IMG_17_0__" alt="Circle plot for x squared plus y squared congruent to 0 mod 17, showing 33 points forming two crossed lines" />
        <img src="__IMG_19_0__" alt="Circle plot for x squared plus y squared congruent to 0 mod 19, showing a single point at the origin" />
      </div>
      <figcaption>
        <span class="plateno">Plate I</span>
        <span class="platetxt">Radius zero on two clocks. Left, the 17-clock: thirty-three points forming two crossed lines through the origin. Right, the 19-clock: one point, alone. This is where <span style="color:var(--state)">p mod 4</span> earns its reputation &mdash; not on c = 4.</span>
      </figcaption>
    </figure>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p><span class="stage">(delighted)</span> Two lines, crossing at the origin. A circle of radius zero that is secretly a large <span style="font-family:var(--mono)">X</span>. Popovich, that is correct and you clearly did it before I asked the question.</p>
      </div>
    </div>

    <div class="line"><div class="who pop">Popovich</div><div class="says"><p>I got bored.</p></div></div>

    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>Get bored more.</p></div></div>
  </section>

  <!-- ============ 03 ============ -->
  <section>
    <h2><span class="sec-no">03</span> The good part</h2>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>Now I'll tell you <em>why</em> the count works, and this is the part I have been looking forward to since August.</p>
        <p>Last unit you learned that on some clocks there is a real, honest number that squares to <span style="font-family:var(--mono)">&minus;1</span>. On the 17-clock, what is it?</p>
      </div>
    </div>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says"><p>Four! Four squared is sixteen, and sixteen is <span style="font-family:var(--mono)">&minus;1</span> on a 17-clock.</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p>Good. Now watch. With that number in hand:</p></div>
    </div>

    <div class="line"><div></div><div class="eq" style="grid-column:auto">x&sup2; + y&sup2;  =  (x + 4y)(x &minus; 4y)      <span style="color:var(--muted)">— on the 17-clock</span></div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p>Check it at every one of the 289 grid points if you like. It holds at all of them.</p></div>
    </div>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says"><p>That's just&hellip; difference of squares. That's from <em>seventh grade.</em></p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>It is exactly difference of squares. Seventh grade comes back for you. Now substitute <span style="font-family:var(--mono)">u = x + 4y</span> and <span style="font-family:var(--mono)">v = x &minus; 4y</span>, and the circle equation becomes:</p>
      </div>
    </div>

    <div class="line"><div></div><div class="eq" style="grid-column:auto">u &middot; v = c</div></div>

    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>Count <em>that</em>. How many ways?</p></div></div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says"><p><span class="stage">(sitting up slightly)</span> Pick <span style="font-family:var(--mono)">u</span> to be anything nonzero, <span style="font-family:var(--mono)">v</span> is forced. Sixteen choices. Sixteen points.</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p><span style="font-family:var(--mono)">p &minus; 1</span>. And you didn't memorize it, you <em>derived</em> it in one line.</p></div>
    </div>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says"><p>So the square roots of <span style="font-family:var(--mono)">&minus;1</span> and the circle count are &mdash;</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>The same fact. They were never two lessons. The factoring works exactly when <span style="font-family:var(--mono)">&minus;1</span> is a square, and that is exactly when <span style="font-family:var(--mono)">p &equiv; 1 (mod 4)</span>. Gold star, Ralphie, that's the sentence I wanted.</p>
      </div>
    </div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says">
        <p>So what happens on 19, where your <span style="font-family:var(--mono)">i</span> doesn't exist? Because you still got twenty points. You said so. The circle didn't care that the number was missing.</p>
      </div>
    </div>

    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>Then we build it.</p></div></div>

    <div class="line"><div class="who pop">Popovich</div><div class="says"><p>You <em>build</em> it.</p></div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>We adjoin <span style="font-family:var(--mono)">i</span>. We declare a new symbol whose square is <span style="font-family:var(--mono)">&minus;1</span>, we attach it to the 19-clock, and we obtain a perfectly good field of 361 numbers. In it, <span style="font-family:var(--mono)">x&sup2; + y&sup2;</span> is the norm of <span style="font-family:var(--mono)">x + iy</span>. The norm map lands <span style="font-family:var(--mono)">(p&sup2; &minus; 1)/(p &minus; 1) = p + 1</span> numbers on every target. Twenty points. Same as we counted.</p>
      </div>
    </div>

    <div class="line"><div class="who pop">Popovich</div><div class="says"><p>Mrs. Feeney.</p></div></div>
    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>Yes, Popovich.</p></div></div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says">
        <p>You took a field where a square root was missing, and you invented a new number to fill the hole, and you got a field twice as big where every rotation lives.</p>
      </div>
    </div>

    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>&hellip;Yes.</p></div></div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says"><p>My grandfather went to the mountains for eleven years for writing down that exact sentence.</p></div>
    </div>

    <div class="line"><div class="beat">(The room gets quiet. Ralphie looks at his desk.)</div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p><span class="stage">(after a moment, putting down the marker)</span> Your grandfather was a better mathematician than the people who sent him there.</p>
        <p>I'm not going to stand here and tell you this is different. It isn't. <span style="font-family:var(--mono)">F<sub>p</sub>[i]</span> is the finite mirror of the thing his forty pages were about. Every argument I just made is an argument he'd recognize. The difference between what we do and what he did is that ours stops &mdash; the mirror has <span style="font-family:var(--mono)">p&sup2;</span> numbers in it and you can count them &mdash; and his didn't. That is a real difference. It is not the difference the textbook claims, which is that we never needed the idea at all.</p>
        <p>We need the idea. We use it in the second week. The chapter heading that says otherwise is wrong, and you may write that in the margin.</p>
      </div>
    </div>

    <div class="line">
      <div class="marginal">
        <b>Margin, p. 41 — in pen</b>
        Ch. 1 heading is wrong. We do need i. For half of all primes you must build it, and what you get is a scale model of the thing they sent Grandfather away for. She said to write this down. — P.
      </div>
    </div>

    <div class="line"><div class="who pop">Popovich</div><div class="says"><p><span class="stage">(a beat)</span> &hellip;I'll write it in the margin.</p></div></div>
    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>Do. In pen.</p></div></div>
  </section>

  <!-- ============ 04 ============ -->
  <section>
    <h2><span class="sec-no">04</span> The circle is a rotation group. Actually.</h2>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>Recover, everyone, because the next part is the best thing you'll see this year. Take two points on the circle <span style="font-family:var(--mono)">x&sup2; + y&sup2; = 1</span> and multiply them like this:</p>
      </div>
    </div>

    <div class="line"><div></div><div class="eq" style="grid-column:auto">(a, b) &#8902; (u, v)  =  (au &minus; bv,  av + bu)</div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p>Try it. Take any two points on the circle, combine them, see where you land.</p></div>
    </div>

    <div class="line"><div class="who">Ralphie</div><div class="says"><p>&hellip;I landed back on the circle.</p></div></div>
    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>Try again.</p></div></div>
    <div class="line"><div class="who">Ralphie</div><div class="says"><p>Still on the circle. <span class="stage">(pause)</span> Mrs. Feeney, I can't get off the circle.</p></div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>You can't get off the circle. It's closed. The circle is a <strong>group</strong>. And it's better than that. Popovich &mdash; take the 17-clock, take the point <span style="font-family:var(--mono)">(4, 6)</span>, and keep multiplying it by itself. Tell me what you see.</p>
      </div>
    </div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says"><p><span class="stage">(a minute of tapping)</span> It hits every point on the circle. All sixteen. Then it comes back to <span style="font-family:var(--mono)">(1, 0)</span> and starts over.</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>Every point, exactly once, then home. That is a <strong>generator</strong>. There is a smallest rotation on our finite circle &mdash; one sixteenth of the way around &mdash; and every rotation is a repeat of it.</p>
      </div>
    </div>

    <div class="line"><div></div>
      <div class="tablewrap" style="grid-column:auto">
        <table>
          <thead><tr><th>Clock</th><th>Circle size</th><th>A generator</th></tr></thead>
          <tbody>
            <tr><td>7</td><td>8</td><td class="hi">(2, 2)</td></tr>
            <tr><td>17</td><td>16</td><td class="hi">(4, 6)</td></tr>
            <tr><td>19</td><td>20</td><td class="hi">(3, 7)</td></tr>
            <tr><td>29</td><td>28</td><td class="hi">(5, 11)</td></tr>
            <tr><td>103</td><td>104</td><td class="hi">(2, 10)</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says"><p>So <em>this</em> is how the engineers rotate things! Not the swap-and-flip trick you showed us for 90 degrees!</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p>The swap-and-flip <em>is</em> this. It's this one specific element. I showed you a single brick and called it architecture. Here's the building.</p></div>
    </div>

    <div class="line"><div class="who pop">Popovich</div><div class="says"><p>Does the generator go around in order?</p></div></div>
    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>Say more.</p></div></div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says"><p>When you keep multiplying &mdash; does the point walk around the picture like a clock hand? Neighbor to neighbor?</p></div>
    </div>

    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p><span class="stage">(pause)</span> No. It jumps all over the picture.</p></div></div>
    <div class="line"><div class="who pop">Popovich</div><div class="says"><p>Then in what sense is it a rotation?</p></div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>In the sense that it generates the group. Not in the sense that it moves a little bit at a time &mdash; that would require knowing what &ldquo;a little bit&rdquo; means, and we're about to discuss why we don't. Popovich, that question is your homework, and I mean that as a compliment. Nobody has asked me that in four years.</p>
      </div>
    </div>

    <figure>
      <div class="plate two">
        <img src="__IMG_17_7__" alt="Circle plot mod 17 with radius squared 7, all sixteen points lying on a single ring" />
        <img src="__IMG_29_3__" alt="Circle plot mod 29 with radius squared 3, twenty-four of twenty-eight points forming a clear ring" />
      </div>
      <figcaption>
        <span class="plateno">Plate II</span>
        <span class="platetxt">The two best circles in the curriculum. Left, the 17-clock at c = 7: every one of its sixteen points sits on one ring &mdash; mathematically perfect, visually sparse. Right, the 29-clock at c = 3: twenty-four of twenty-eight points on a single ring, and the only plot in the course that reads as a circle at a glance.</span>
      </figcaption>
    </figure>
  </section>

  <!-- ============ 05 ============ -->
  <section>
    <h2><span class="sec-no">05</span> What we don't have</h2>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>Which brings us to the uncomfortable slide. Some of what a circle means in the old texts, we simply do not have. Not &ldquo;cleverly avoid.&rdquo; Do not have.</p>
        <p><strong>No distance.</strong> Our clock has no ordering. You cannot ask whether one point is farther out than another. &ldquo;Radius squared&rdquo; is a label on an equation, not a length.</p>
        <p><strong>No angle. No arc. No pi.</strong> Not a triumph over pi. There is no arc to measure, so there is nothing for pi to be the ratio <em>of</em>.</p>
        <p><strong>No betweenness.</strong> No point lies between two others. Our circle is not a curve. It never was.</p>
      </div>
    </div>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says"><p>But the textbook says the absence of pi is why our bridges don't have rounding errors &mdash;</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>The textbook is selling something. If you delete the concept of length, of course you have no errors in measuring length. You also have no bridges.</p>
        <p>What survives is the count, the group, the symmetry, the factoring. That is a great deal! It is simply algebra rather than geometry, and I would rather you knew which one you were holding.</p>
      </div>
    </div>
  </section>

  <!-- ============ 06 ============ -->
  <section>
    <h2><span class="sec-no">06</span> The pictures, which are the least interesting part</h2>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says"><p><span class="stage">(rallying)</span> But when you scale up to ten thousand ticks, the points get so dense that they blur into a smooth ring! That's the Human Threshold!</p></div>
    </div>

    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>Popovich, plot the 65537-clock.</p></div></div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says"><p><span class="stage">(after a moment, turning the tablet around)</span> It's dust. It's a grey rectangle of dust.</p></div>
    </div>

    <figure>
      <div class="plate strip">
        <img src="__IMG_29_3__" alt="Modular circle at p equals 29, a clear ring" />
        <img src="__IMG_109_92__" alt="Modular circle at p equals 109, ring visible through scatter" />
        <img src="__IMG_257_4__" alt="Modular circle at p equals 257, mostly scatter with a small central ring" />
        <img src="__IMG_65537_4__" alt="Modular circle at p equals 65537, uniform dust with no visible ring" />
      </div>
      <figcaption>
        <span class="plateno">Plate III</span>
        <span class="platetxt">The dissolve: 29, 109, 257, 65537. The curriculum promises that around ten thousand ticks the points blur into a smooth unbroken ring. They do the opposite. Roughly <span style="color:var(--state)">p</span> points scattered over <span style="color:var(--state)">p&sup2;</span> cells means density falls as the clock grows. Structure lives at <em>small</em> primes.</span>
      </figcaption>
    </figure>

    <div class="line"><div class="who">Ralphie</div><div class="says"><p>That can't be right &mdash;</p></div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>It's right. And it's backwards from what you were told, so hear it clearly: <strong>the points spread out evenly.</strong> Big primes don't sharpen into a ring. They dissolve. The beautiful pictures are at <em>small</em> primes.</p>
      </div>
    </div>

    <div class="line"><div></div>
      <div class="tablewrap" style="grid-column:auto">
        <table>
          <thead><tr><th>Clock, c</th><th>On one ring</th><th>Reading</th></tr></thead>
          <tbody>
            <tr><td>17, 7</td><td class="hi">100%</td><td>perfect, but sparse</td></tr>
            <tr><td>29, 3</td><td class="hi">86%</td><td>24 of 28 &mdash; looks like a circle</td></tr>
            <tr><td>53, 49</td><td>62%</td><td>noise creeping in</td></tr>
            <tr><td>109, 92</td><td>44%</td><td>rim visible through scatter</td></tr>
            <tr><td>65537, 4</td><td>&mdash;</td><td>dust</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says"><p>Why does <em>any</em> of it ring up, then? If they're spread evenly.</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p><span class="stage">(genuinely pleased)</span> Because sometimes there's no wraparound. If <span style="font-family:var(--mono)">x&sup2; + y&sup2;</span> equals <span style="font-family:var(--mono)">c + kp</span> as an <em>honest whole number</em> &mdash; no clock involved &mdash; those points sit on a real circle of real integers. Our modular circle is a stack of ordinary integer circles, and one dominates when <span style="font-family:var(--mono)">c + kp</span> happens to be a number with many ways of being written as a sum of two squares.</p>
        <p>For the 29-clock at <span style="font-family:var(--mono)">c = 3</span>, that number is <span style="font-family:var(--mono)">650 = 2 &middot; 5&sup2; &middot; 13</span>. It has twenty-four such ways. Twenty-four points, one ring.</p>
      </div>
    </div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says"><p>So the nicest thing our finite grid does is accidentally show us a picture of ordinary integers.</p></div>
    </div>

    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p><span class="stage">(long pause)</span> Yes.</p></div></div>
    <div class="line"><div class="who pop">Popovich</div><div class="says"><p>Huh.</p></div></div>
  </section>

  <!-- ============ 07 ============ -->
  <section>
    <h2><span class="sec-no">07</span> The bell</h2>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p>Two minutes. Ralphie, you had your hand up for six of them.</p></div>
    </div>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says">
        <p>I just wanted to say &mdash; on the first slide you said the reason we do all this is that no fraction squares to 2. And that our clocks find the exact number that does.</p>
      </div>
    </div>

    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>I did say that.</p></div></div>

    <div class="line">
      <div class="who">Ralphie</div>
      <div class="says">
        <p>So I checked, because I wanted to have it ready for you. And on the 5-clock there's no square root of 2. There isn't one on the 13-clock either. Or the 29-clock. Those are three of the four clocks in the chapter.</p>
      </div>
    </div>

    <div class="line"><div class="beat">(Popovich starts laughing.)</div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p><span class="stage">(setting down the marker)</span> Ralphie. That is the best question anyone has asked today, and you asked it by accident while trying to agree with me.</p>
        <p>You're right. <span style="font-family:var(--mono)">&radic;2</span> exists on a clock exactly when <span style="font-family:var(--mono)">p &equiv; &plusmn;1 (mod 8)</span>.</p>
      </div>
    </div>

    <div class="line"><div></div>
      <div class="tablewrap" style="grid-column:auto">
        <table>
          <thead><tr><th>Clock</th><th>5</th><th>7</th><th>13</th><th>17</th><th>23</th><th>29</th><th>31</th><th>41</th></tr></thead>
          <tbody>
            <tr><td>&radic;2 exists?</td><td>no</td><td class="hi">yes</td><td>no</td><td class="hi">yes</td><td class="hi">yes</td><td>no</td><td class="hi">yes</td><td class="hi">yes</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>It is <em>not</em> there on 5, 13, or 29. The example the entire curriculum opens with does not work on most of the clocks the curriculum teaches.</p>
      </div>
    </div>

    <div class="line"><div class="who">Ralphie</div><div class="says"><p>So what do we do on the 13-clock?</p></div></div>
    <div class="line"><div class="who feen">Mrs. Feeney</div><div class="says"><p>We extend the field.</p></div></div>
    <div class="line"><div class="who pop">Popovich</div><div class="says"><p><span class="stage">(still laughing)</span> You build it again.</p></div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p>We build it again. Yes. That is the second thing you may write in the margin.</p></div>
    </div>

    <div class="line">
      <div class="marginal">
        <b>Margin, p. 4 — in pen</b>
        Opening example doesn't work on 3 of the 4 clocks in this book. Fix is: build the bigger field. Same fix as p. 41. It is always the same fix. — P.
      </div>
    </div>

    <div class="line"><div class="beat">(bell)</div></div>

    <div class="homework">
      <h3>Homework — the whole assignment</h3>
      <ol>
        <li>Count the points for <span style="font-family:var(--mono)">c = 0</span> on the 17-clock and the 19-clock. Explain the thirty-three.</li>
        <li>Find a generator for the 13-clock circle. Any generator.</li>
        <li><span class="unsolved">Popovich's question.</span> When you step a generator around the circle, the point hops all over the picture instead of walking neighbor to neighbor. Why? I don't want a paragraph. I want one honest sentence about what &ldquo;neighbor&rdquo; would even mean here.</li>
      </ol>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says">
        <p>Nobody has turned in a good answer to number three since I started assigning it. I'd like that to change this year.</p>
        <p>Popovich &mdash; a moment.</p>
      </div>
    </div>

    <div class="line">
      <div class="who pop">Popovich</div>
      <div class="says"><p><span class="stage">(gathering his bag)</span> I know, I know, the seat &mdash;</p></div>
    </div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p>No. Your grandfather's forty pages. Are they somewhere I could read them?</p></div>
    </div>

    <div class="line"><div class="beat">(Popovich stops in the doorway.)</div></div>

    <div class="line"><div class="who pop">Popovich</div><div class="says"><p>&hellip;I'd have to ask my mother.</p></div></div>

    <div class="line">
      <div class="who feen">Mrs. Feeney</div>
      <div class="says"><p>Ask her. Chapter 4 is about extensions, and I've never had anything good to hand the students who get that far.</p></div>
    </div>
  </section>

  <footer class="colophon">
    <h3>For the teacher's edition</h3>
    <p>Verified by computation for this transcript: point counts <span style="color:var(--state)">p &#8723; 1</span>; the c = 0 split (33 against 1); the factorization <span style="color:var(--state)">x&sup2; + y&sup2; = (x + iy)(x &minus; iy)</span> at all p&sup2; grid points for p = 13, 17, 29; closure and cyclicity of the group law <span style="color:var(--state)">(a,b) &#8902; (u,v) = (au &minus; bv, av + bu)</span> with the generators tabled above; ring fractions from an exhaustive search over every residue of every prime below 600; <span style="color:var(--state)">&radic;2</span> existing exactly when p &equiv; &plusmn;1 (mod 8).</p>
    <p class="flag">Ralphie's errors are quoted from a real lesson transcript. Every one of them was presented there as fact.</p>
    <p>All plates produced by <span style="color:var(--state)">circles.py</span>. Plate III at reduced resolution; the dust is the point.</p>
  </footer>

</div>
"""

for key in ['17_0', '19_0', '17_7', '29_3', '109_92', '257_4', '65537_4']:
    HTML = HTML.replace(f'__IMG_{key}__', img(key))

out = HERE / 'day-one-circles-v1-ministry.html'
out.write_text(HTML)
print('wrote', out, f'{out.stat().st_size/1024:.0f} KB')
