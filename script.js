(() => {
  const WA_NUMBER = "918618302179";

  /* ---------- Header & nav ---------- */
  const header = document.querySelector(".site-header");
  const nav = document.getElementById("primary-nav");
  const toggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelectorAll(".nav-link");

  const onScroll = () => {
    header && header.classList.toggle("is-scrolled", window.scrollY > 10);
    const y = window.scrollY + 140;
    let current = "top";
    document.querySelectorAll("main section[id]").forEach((s) => {
      if (s.offsetTop <= y) current = s.id;
    });
    if (window.scrollY < 80) current = "top";
    navLinks.forEach((l) => l.classList.toggle("is-active", l.getAttribute("href") === "#" + current));
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });
    navLinks.forEach((l) =>
      l.addEventListener("click", () => {
        toggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
      })
    );
  }

  /* ---------- Formatting ---------- */
  const inr = (v) => "₹" + Math.round(v).toLocaleString("en-IN");
  const short = (v) => {
    if (v >= 1e7) return "₹" + (v / 1e7).toFixed(2) + " Cr";
    if (v >= 1e5) return "₹" + (v / 1e5).toFixed(2) + " L";
    return inr(v);
  };

  /* ---------- Calculators ---------- */
  const sipFV = (p, rate, years) => {
    const i = rate / 1200;
    const m = years * 12;
    if (i === 0) return p * m;
    return p * ((Math.pow(1 + i, m) - 1) / i) * (1 + i);
  };
  const sipNeeded = (target, rate, years) => target / sipFV(1, rate, years);

  const CALCS = {
    sip: {
      fields: [
        { id: "amt", label: "Monthly SIP", min: 500, max: 200000, step: 500, value: 10000, fmt: inr },
        { id: "rate", label: "Expected return (p.a.)", min: 1, max: 20, step: 0.5, value: 12, fmt: (v) => v + "%" },
        { id: "yrs", label: "Time period", min: 1, max: 40, step: 1, value: 15, fmt: (v) => v + " yrs" },
      ],
      run: ({ amt, rate, yrs }) => {
        const fv = sipFV(amt, rate, yrs);
        const inv = amt * yrs * 12;
        return { main: ["Estimated value", fv], rows: [["Amount invested", inv], ["Estimated gains", fv - inv]], bar: [inv, fv - inv] };
      },
    },
    stepup: {
      fields: [
        { id: "amt", label: "Starting monthly SIP", min: 500, max: 200000, step: 500, value: 10000, fmt: inr },
        { id: "step", label: "Annual step-up", min: 0, max: 25, step: 1, value: 10, fmt: (v) => v + "%" },
        { id: "rate", label: "Expected return (p.a.)", min: 1, max: 20, step: 0.5, value: 12, fmt: (v) => v + "%" },
        { id: "yrs", label: "Time period", min: 1, max: 40, step: 1, value: 15, fmt: (v) => v + " yrs" },
      ],
      run: ({ amt, step, rate, yrs }) => {
        const i = rate / 1200;
        let fv = 0, inv = 0, p = amt;
        for (let m = 1; m <= yrs * 12; m++) {
          fv = (fv + p) * (1 + i);
          inv += p;
          if (m % 12 === 0) p *= 1 + step / 100;
        }
        const flat = sipFV(amt, rate, yrs);
        return { main: ["Estimated value", fv], rows: [["Amount invested", inv], ["Estimated gains", fv - inv], ["Extra vs flat SIP", fv - flat]], bar: [inv, fv - inv] };
      },
    },
    lumpsum: {
      fields: [
        { id: "amt", label: "One-time investment", min: 10000, max: 10000000, step: 10000, value: 500000, fmt: inr },
        { id: "rate", label: "Expected return (p.a.)", min: 1, max: 20, step: 0.5, value: 12, fmt: (v) => v + "%" },
        { id: "yrs", label: "Time period", min: 1, max: 40, step: 1, value: 10, fmt: (v) => v + " yrs" },
      ],
      run: ({ amt, rate, yrs }) => {
        const fv = amt * Math.pow(1 + rate / 100, yrs);
        return { main: ["Estimated value", fv], rows: [["Amount invested", amt], ["Estimated gains", fv - amt]], bar: [amt, fv - amt] };
      },
    },
    goal: {
      fields: [
        { id: "cost", label: "Goal cost today", min: 100000, max: 50000000, step: 50000, value: 2500000, fmt: inr },
        { id: "yrs", label: "Years to goal", min: 1, max: 30, step: 1, value: 12, fmt: (v) => v + " yrs" },
        { id: "inf", label: "Inflation", min: 0, max: 12, step: 0.5, value: 6, fmt: (v) => v + "%" },
        { id: "rate", label: "Expected return (p.a.)", min: 1, max: 20, step: 0.5, value: 12, fmt: (v) => v + "%" },
      ],
      run: ({ cost, yrs, inf, rate }) => {
        const future = cost * Math.pow(1 + inf / 100, yrs);
        const sip = sipNeeded(future, rate, yrs);
        const lump = future / Math.pow(1 + rate / 100, yrs);
        return { main: ["Monthly SIP needed", sip], rows: [["Goal cost in " + yrs + " yrs", future], ["OR one-time investment today", lump], ["Total SIP invested", sip * yrs * 12]] };
      },
    },
    retire: {
      fields: [
        { id: "age", label: "Current age", min: 18, max: 60, step: 1, value: 35, fmt: (v) => v + " yrs" },
        { id: "rage", label: "Retirement age", min: 40, max: 70, step: 1, value: 60, fmt: (v) => v + " yrs" },
        { id: "life", label: "Life expectancy", min: 70, max: 100, step: 1, value: 85, fmt: (v) => v + " yrs" },
        { id: "exp", label: "Monthly expenses today", min: 10000, max: 500000, step: 5000, value: 50000, fmt: inr },
        { id: "inf", label: "Inflation", min: 0, max: 12, step: 0.5, value: 6, fmt: (v) => v + "%" },
        { id: "pre", label: "Return before retirement", min: 1, max: 18, step: 0.5, value: 12, fmt: (v) => v + "%" },
        { id: "post", label: "Return after retirement", min: 1, max: 12, step: 0.5, value: 7, fmt: (v) => v + "%" },
      ],
      run: ({ age, rage, life, exp, inf, pre, post }) => {
        const yrsToRet = Math.max(rage - age, 1);
        const retYrs = Math.max(life - rage, 1);
        const monthlyAtRet = exp * Math.pow(1 + inf / 100, yrsToRet);
        const annual = monthlyAtRet * 12;
        const g = (1 + post / 100) / (1 + inf / 100) - 1;
        const corpus = Math.abs(g) < 1e-9 ? annual * retYrs : annual * ((1 - Math.pow(1 + g, -retYrs)) / g) * (1 + g);
        const sip = sipNeeded(corpus, pre, yrsToRet);
        return { main: ["Retirement corpus needed", corpus], rows: [["Monthly expenses at " + rage, monthlyAtRet], ["Monthly SIP needed from now", sip], ["Years to retirement", null, yrsToRet + " yrs"]] };
      },
    },
  };

  const form = document.getElementById("calc-form");
  const result = document.getElementById("calc-result");
  let active = "sip";

  const renderForm = () => {
    const c = CALCS[active];
    form.innerHTML = c.fields
      .map(
        (f) => `<div class="field">
          <label for="f-${f.id}">${f.label}<output id="o-${f.id}"></output></label>
          <input type="range" id="f-${f.id}" name="${f.id}" min="${f.min}" max="${f.max}" step="${f.step}" value="${f.value}" />
        </div>`
      )
      .join("");
    compute();
  };

  const compute = () => {
    const c = CALCS[active];
    const vals = {};
    c.fields.forEach((f) => {
      const v = Number(document.getElementById("f-" + f.id).value);
      vals[f.id] = v;
      document.getElementById("o-" + f.id).textContent = f.fmt(v);
    });
    const r = c.run(vals);
    let html = `<div class="res-row res-main"><span>${r.main[0]}</span><b>${inr(r.main[1])}</b>${r.main[1] >= 1e5 ? `<span>${short(r.main[1])}</span>` : ""}</div>`;
    if (r.bar) {
      const tot = r.bar[0] + r.bar[1];
      html += `<div class="bar"><i class="b1" style="width:${(r.bar[0] / tot) * 100}%"></i><i class="b2" style="width:${(r.bar[1] / tot) * 100}%"></i></div>
        <div class="bar-legend"><span><i class="dot dot-muted"></i>Invested</span><span><i class="dot dot-accent"></i>Gains</span></div>`;
    }
    r.rows.forEach(([k, v, txt]) => {
      html += `<div class="res-row"><span>${k}</span><b>${txt || inr(v)}</b></div>`;
    });
    html += `<a class="btn btn-accent" href="#contact">Plan This With Us</a>`;
    result.innerHTML = html;
  };

  if (form) {
    form.addEventListener("input", compute);
    document.querySelectorAll(".calc-tab").forEach((t) =>
      t.addEventListener("click", () => {
        document.querySelectorAll(".calc-tab").forEach((x) => x.classList.remove("is-active"));
        t.classList.add("is-active");
        active = t.dataset.calc;
        renderForm();
      })
    );
    renderForm();
  }

  /* ---------- Risk profiler ---------- */
  const QUESTIONS = [
    ["What is your age?", ["Above 60", "46 – 60", "31 – 45", "Below 30"]],
    ["When will you need most of this money?", ["Within 1 year", "1 – 3 years", "3 – 7 years", "More than 7 years"]],
    ["How stable is your income?", ["Irregular or none", "Somewhat stable", "Stable", "Very stable with growth"]],
    ["Your investments fall 20% in a month. You would…", ["Sell everything", "Sell some", "Hold and wait", "Invest more"]],
    ["What is your main goal?", ["Protect my capital", "Regular income", "Balanced growth", "Maximum long-term growth"]],
    ["How much investing experience do you have?", ["None", "Only FDs / savings", "Some mutual funds", "Equity & MFs for years"]],
  ];
  const PROFILES = [
    { max: 12, name: "Conservative", text: "You value stability. A debt-heavy portfolio with a small equity allocation (around 20–30%) may suit you better." },
    { max: 18, name: "Moderate", text: "You want growth with controlled swings. A balanced mix (around 40–60% equity) through hybrid and diversified funds may suit you." },
    { max: 24, name: "Aggressive", text: "You can ride out volatility for higher long-term growth. An equity-heavy portfolio (70%+) with a long horizon may suit you." },
  ];

  const qWrap = document.getElementById("quiz-questions");
  const quiz = document.getElementById("quiz");
  const quizResult = document.getElementById("quiz-result");
  if (qWrap && quiz) {
    qWrap.innerHTML = QUESTIONS.map(
      ([q, opts], qi) => `<fieldset class="q"><legend>${qi + 1}. ${q}</legend><div class="q-opts">
        ${opts.map((o, oi) => `<label><input type="radio" name="q${qi}" value="${oi + 1}" />${o}</label>`).join("")}
      </div></fieldset>`
    ).join("");

    quiz.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(quiz);
      let score = 0, answered = 0;
      QUESTIONS.forEach((_, i) => {
        const v = data.get("q" + i);
        if (v) { score += Number(v); answered++; }
      });
      if (answered < QUESTIONS.length) {
        quizResult.innerHTML = `<p class="quiz-error">Please answer all ${QUESTIONS.length} questions.</p>`;
        return;
      }
      const p = PROFILES.find((x) => score <= x.max);
      const msg = encodeURIComponent(`Hi Pritesh, I took the risk profiler on your website. My profile: ${p.name} (score ${score}/24). I'd like to discuss a suitable plan.`);
      quizResult.innerHTML = `<div class="result-box"><p class="eyebrow eyebrow-light">Your Risk Profile</p><h3>${p.name}</h3>
        <p>${p.text} This is an indicative self-assessment, not a recommendation.</p>
        <a class="btn btn-accent" href="https://wa.me/${WA_NUMBER}?text=${msg}" target="_blank" rel="noopener noreferrer">Discuss My Profile On WhatsApp</a></div>`;
    });
  }

  /* ---------- Contact form → WhatsApp ---------- */
  const cf = document.getElementById("contact-form");
  if (cf) {
    cf.addEventListener("submit", (e) => {
      e.preventDefault();
      const d = new FormData(cf);
      const text = `Hi Pritesh, I'd like to book a call.\nName: ${d.get("name")}\nPhone: ${d.get("phone")}\nCity/Country: ${d.get("city") || "-"}\nInterested in: ${d.get("interest")}`;
      const url = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(text)}`;
      let out = cf.querySelector(".cf-out");
      if (!out) { out = document.createElement("p"); out.className = "cf-out"; cf.appendChild(out); }
      out.innerHTML = `<a class="btn btn-primary" href="${url}" target="_blank" rel="noopener noreferrer">Open WhatsApp To Send →</a>`;
    });
  }
})();
