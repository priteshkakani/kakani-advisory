"""Static site generator for kakaniwealth.com.

Run:  python3 src/build.py   (from repo root)
Edits go in this file / src/home-main.html; generated HTML is committed for GitHub Pages.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "Kakani Wealth"
LEGAL = "Pritesh Kakani (trading as Kakani Financial Services)"
REG = "AMFI-Registered MFD · ARN-373766 · EUIN E717134 · APMI-Registered PMS Distributor · APRN10835"
PHONE = "+91 86183 02179"
WA = "https://wa.me/918618302179"
EMAIL = "priteshkakani@outlook.com"

SERVICES = [
    ("mutual-funds", "Mutual Funds"),
    ("sif", "Specialised Investment Funds (SIF)"),
    ("pms", "Portfolio Management Services"),
    ("aif", "Alternative Investment Funds"),
    ("bonds-fds", "Bonds & Fixed Deposits"),
]
CALCS = [
    ("sip", "SIP Calculator"),
    ("stepup", "Step-Up SIP Calculator"),
    ("lumpsum", "Lump Sum Calculator"),
    ("lumptarget", "Lump Sum Target Calculator"),
    ("goal", "Goal Planner"),
    ("education", "Children Education Planner"),
    ("retire", "Retirement Calculator"),
    ("swp", "SWP Calculator"),
]
CALC_SLUG = {"sip": "sip-calculator", "stepup": "step-up-sip-calculator", "lumpsum": "lumpsum-calculator",
             "lumptarget": "lumpsum-target-calculator", "goal": "goal-planner", "education": "children-education-planner",
             "retire": "retirement-calculator", "swp": "swp-calculator"}


def esc(t):
    return t.replace("&", "&amp;")


def header():
    svc = "".join(f'<a href="/services/{s}/">{esc(n)}</a>' for s, n in SERVICES) + '<a href="/#nri">NRI Desk</a>'
    calc = "".join(f'<a href="/calculators/{CALC_SLUG[c]}/">{n}</a>' for c, n in CALCS) + '<a href="/#risk-profiler">Risk Profiler</a>'
    return f"""    <div class="topbar">
      <div class="wrap topbar-inner">
        <div class="topbar-contact">
          <a href="tel:+918618302179">📞 {PHONE}</a>
          <a href="mailto:{EMAIL}">✉ {EMAIL}</a>
        </div>
        <p class="topbar-reg">{REG}</p>
      </div>
    </div>

    <header class="site-header" id="top">
      <div class="wrap header-inner">
        <a class="brand" href="/" aria-label="{SITE} home">
          <span class="brand-mark">K</span>
          <span class="brand-text">
            <span class="brand-name">{SITE}</span>
            <span class="brand-tag">AMFI-Registered Mutual Fund Distributor · ARN-373766</span>
          </span>
        </a>

        <nav class="nav" id="primary-nav" aria-label="Primary">
          <a href="/" class="nav-link">Home</a>
          <a href="/about/" class="nav-link">About</a>
          <a href="/investment-process/" class="nav-link">Our Process</a>
          <div class="nav-dd">
            <button class="nav-link dd-toggle" type="button" aria-expanded="false">Services <span class="caret">▾</span></button>
            <div class="dd-menu">{svc}</div>
          </div>
          <div class="nav-dd">
            <button class="nav-link dd-toggle" type="button" aria-expanded="false">Calculators <span class="caret">▾</span></button>
            <div class="dd-menu">{calc}</div>
          </div>
          <a href="/#faq" class="nav-link">FAQs</a>
          <a href="/#contact" class="nav-link">Contact</a>
        </nav>

        <a class="btn btn-accent header-cta" href="/#contact" data-interest="Portfolio consultation">Portfolio Consultation</a>

        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </header>
"""


def footer():
    svc = "".join(f'<a href="/services/{s}/">{esc(n)}</a>' for s, n in SERVICES)
    calc = "".join(f'<a href="/calculators/{CALC_SLUG[c]}/">{n}</a>' for c, n in CALCS[:6])
    return f"""
    <footer class="site-footer">
      <div class="wrap footer-grid footer-grid-5">
        <div>
          <a class="brand brand-light" href="/">
            <span class="brand-mark">K</span>
            <span class="brand-text">
              <span class="brand-name">{SITE}</span>
              <span class="brand-tag">{REG}</span>
            </span>
          </a>
          <p class="footer-about">Goal-based investing for resident and NRI families. Plan today, secure your tomorrow.</p>
        </div>
        <div>
          <h4>Quick Links</h4>
          <a href="/about/">About</a>
          <a href="/investment-process/">Our Investment Process</a>
          <a href="/about/#philosophy">Intellect &amp; Integrity</a>
          <a href="/#risk-profiler">Risk Profiler</a>
          <a href="/#faq">FAQs</a>
          <a href="/#disclosures">Disclosures</a>
          <a href="/#contact">Contact</a>
        </div>
        <div>
          <h4>Services</h4>
          {svc}
          <a href="/#nri">NRI Desk</a>
        </div>
        <div>
          <h4>Calculators</h4>
          {calc}
        </div>
        <div>
          <h4>Contact</h4>
          <p>108, Bhagirathi, Renavikar Nagar,<br />Savedi, Ahilyanagar – 414003</p>
          <a href="tel:+918618302179">{PHONE}</a>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
      </div>
      <div class="wrap footer-bottom">
        <p>© 2026 {SITE} · a brand of {LEGAL} · ARN-373766 · APRN10835. All rights reserved. Mutual Fund investments are subject to market risks, read all scheme related documents carefully.</p>
        <div class="footer-legal">
          <a href="https://www.amfiindia.com/" target="_blank" rel="noopener noreferrer">AMFI</a>
          <a href="https://www.amfiindia.com/locate-distributor" target="_blank" rel="noopener noreferrer">Verify ARN</a>
          <a href="https://scores.sebi.gov.in/" target="_blank" rel="noopener noreferrer">SEBI SCORES</a>
          <a href="https://smartodr.in/" target="_blank" rel="noopener noreferrer">SMART ODR</a>
          <a href="/#disclosures">Commission Disclosure</a>
          <a href="/#grievance">Grievance Redressal</a>
          <a href="/#privacy">Privacy Policy</a>
          <a href="/#terms">Terms of Use</a>
          <a href="https://investor.sebi.gov.in/pdf/investor-charter/mf_amc_amfi.pdf" target="_blank" rel="noopener noreferrer">Investor Charter</a>
        </div>
      </div>
    </footer>

    <a class="wa-float" href="{WA}" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
      <svg viewBox="0 0 24 24" width="28" height="28" fill="#fff" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2z"/></svg>
    </a>
"""


def page(title, desc, main, body_attr=""):
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <script>if(location.protocol==="http:"&&/kakaniwealth[.]com$/.test(location.hostname)){{location.replace("https://kakaniwealth.com"+location.pathname+location.search+location.hash)}}</script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <meta name="description" content="{desc}" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="/styles.css" />
  </head>
  <body{body_attr}>
{header()}
{main}
{footer()}
    <script src="/script.js"></script>
  </body>
</html>
"""


def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", rel)


def page_hero(eyebrow, h1, lede, crumbs):
    crumb = " / ".join(crumbs)
    return f"""      <section class="page-hero">
        <div class="wrap">
          <p class="crumbs"><a href="/">Home</a> / {crumb}</p>
          <p class="eyebrow eyebrow-light">{eyebrow}</p>
          <h1>{h1}</h1>
          <p class="hero-lede">{lede}</p>
          <div class="hero-actions">
            <a class="btn btn-accent" href="/#contact" data-interest="Portfolio consultation">Book A Portfolio Consultation</a>
            <a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener noreferrer">Chat On WhatsApp</a>
          </div>
        </div>
      </section>
"""


def cta_band(text="Have questions about whether this suits you?"):
    return f"""      <section class="closing">
        <div class="wrap closing-inner">
          <h2>{text}</h2>
          <a class="btn btn-accent" href="/#contact" data-interest="Portfolio consultation">Book A Portfolio Consultation</a>
        </div>
      </section>
"""


def disclaimer(extra=""):
    return f"""      <section class="regulatory">
        <div class="wrap">
          <p class="risk-line">Mutual Fund investments are subject to market risks, read all scheme related documents carefully.</p>
          <p>{SITE} is the brand name of {LEGAL}, an AMFI-Registered Mutual Fund Distributor, ARN-373766, EUIN E717134, and an APMI-Registered PMS Distributor, APRN10835. We are not a
          SEBI-Registered Investment Adviser. Any guidance provided is incidental to distribution. {extra} Past performance is not
          indicative of future returns, and returns are not guaranteed.</p>
        </div>
      </section>
"""


INTELLECT_INTEGRITY = """      <section class="section ii" id="philosophy">
        <div class="wrap">
          <div class="section-head center">
            <p class="eyebrow">Our Philosophy</p>
            <h2>Built on Intellect &amp; Integrity</h2>
            <p class="lede">Most of an investor's long-term success comes from behaviour: staying disciplined, diversified and invested. Our job is to make that easier, and to add careful thinking where it matters.</p>
          </div>
          <div class="ii-grid">
            <article class="ii-card">
              <div class="ii-head"><span class="ii-icon">🧠</span><h3>Intellect</h3></div>
              <ul>
                <li><b>Portfolio over products.</b> How your overall portfolio is built (allocation, diversification and goal mapping) matters more than picking any single scheme.</li>
                <li><b>Active monitoring, not "buy and forget".</b> Portfolios are reviewed and rebalanced as markets, schemes and your life change.</li>
                <li><b>Tracking as a discipline.</b> We use a structured, data-driven review process, shaped by an engineering background and 9+ years in the markets.</li>
                <li><b>Risk management first.</b> Protecting the downside comes before chasing returns: credit quality, concentration and liquidity are checked before anything else.</li>
              </ul>
            </article>
            <article class="ii-card ii-card-dark">
              <div class="ii-head"><span class="ii-icon">🤝</span><h3>Integrity</h3></div>
              <ul>
                <li><b>Client first.</b> Every suggestion has to serve your interest and suit your goals and risk profile.</li>
                <li><b>No sales targets.</b> We have no product-pushing incentives. If a product doesn't fit you, we won't suggest it.</li>
                <li><b>Skin in the game.</b> We only suggest products we understand and would be comfortable recommending to our own family.</li>
                <li><b>Full disclosure.</b> Commissions, costs, risks and direct-plan alternatives are always shared upfront.</li>
              </ul>
            </article>
          </div>
        </div>
      </section>
"""


# ---------------------------------------------------------------- Service pages
SVC = {
    "mutual-funds": dict(
        title="Mutual Funds",
        eyebrow="Service · Mutual Funds",
        lede="Professionally managed, SEBI-regulated pooled investments for every goal, from your first ₹100 SIP to a retirement income plan.",
        minimum="₹100 – ₹500 SIP / ₹1,000 – ₹5,000 lump sum (varies by scheme)",
        who="Every investor: salaried professionals, business owners, families, retirees and NRIs",
        horizon="From 1 day (liquid funds) to 7+ years (equity funds)",
        liquidity="High. Most open-ended schemes can be redeemed on any business day (exit loads may apply)",
        overview=[
            "A mutual fund pools money from many investors and invests it in equities, bonds, money-market instruments or gold, according to the objective stated in its Scheme Information Document. Each fund is managed by a SEBI-registered Asset Management Company (AMC), and investor money is held by an independent custodian and overseen by trustees.",
            "Mutual funds give you diversification, professional management and daily liquidity with very small ticket sizes. They are among the most transparent investment products in India: NAVs are published daily and portfolios monthly.",
        ],
        types=[
            ("Equity Funds", "Large, mid, small, flexi-cap, ELSS and sectoral funds for long-term growth."),
            ("Debt Funds", "Liquid, money-market, short-duration, corporate bond and gilt funds for stability and income."),
            ("Hybrid Funds", "Balanced advantage, aggressive and conservative hybrid, and multi-asset funds that mix asset classes."),
            ("Index Funds & ETFs", "Low-cost passive funds that track indices such as the Nifty 50 or Sensex."),
            ("Solution-Oriented", "Retirement and children's funds with a lock-in suited to long-term goals."),
            ("International / FoF", "Fund-of-funds giving exposure to global markets, within regulatory limits."),
        ],
        modes=[
            ("SIP", "Invest a fixed amount every month and benefit from rupee-cost averaging."),
            ("Lump Sum", "Invest a one-time amount, such as a bonus or the proceeds of a sale."),
            ("STP", "Park a lump sum in a debt fund and move it gradually into equity."),
            ("SWP", "Withdraw a fixed amount every month, which suits retirement income."),
        ],
        risks=["Market risk: equity NAVs move with stock prices.", "Interest-rate and credit risk in debt funds.",
               "Every scheme carries a SEBI riskometer from Low to Very High. Check it before investing.",
               "Exit loads and expense ratios vary by scheme."],
        how=["Understand your goals, time horizon and risk profile", "Shortlist suitable categories and schemes, with commission disclosure",
             "Complete KYC and set up SIPs online", "Review the portfolio at least twice a year and rebalance if needed"],
        extra="",
    ),
    "sif": dict(
        title="Specialised Investment Funds (SIF)",
        eyebrow="Service · SIF",
        lede="SEBI's new investment category, sitting between mutual funds and PMS, with more flexible strategies for investors putting in ₹10 lakh or more.",
        minimum="₹10 lakh per investor (PAN level, across the SIF strategies of an AMC)",
        who="Experienced investors seeking strategies beyond a regular mutual fund, without a PMS-sized ticket",
        horizon="Typically 3+ years, depending on the strategy",
        liquidity="Varies by strategy. Redemption may be daily, weekly or at other intervals, as stated in the strategy's offer document",
        overview=[
            "Specialised Investment Funds are a SEBI-regulated product category launched under the mutual fund framework. They are offered only by eligible AMCs, under a separate SIF brand, and are meant for investors who want differentiated strategies with the governance of a mutual fund.",
            "Unlike regular mutual funds, SIF strategies may take limited unhedged short positions through derivatives and follow long-short or more concentrated approaches, within the limits SEBI prescribes.",
        ],
        types=[
            ("Equity Long-Short", "Equity strategies that can take limited short positions to manage downside."),
            ("Equity Ex-Top 100 Long-Short", "Long-short strategies focused beyond the largest 100 stocks."),
            ("Sector Rotation Long-Short", "Rotation across sectors with limited short exposure."),
            ("Debt Long-Short", "Fixed-income strategies with interest-rate positioning."),
            ("Sectoral Debt Long-Short", "Debt strategies concentrated in chosen sectors."),
            ("Hybrid / Active Asset Allocator", "Multi-asset long-short strategies across equity, debt and other assets."),
        ],
        modes=[
            ("Lump Sum", "Invest the ₹10 lakh minimum, or more, in one go."),
            ("SIP / STP", "Where the strategy allows, after the minimum threshold is met."),
            ("Redemption", "As per the strategy's stated frequency and notice period."),
            ("Statements", "Reported through your CAS, like mutual funds."),
        ],
        risks=["Derivative and short-selling risk can amplify losses.", "Strategies are newer and have shorter track records.",
               "Liquidity may be restricted compared with open-ended mutual funds.", "Read each strategy's Investment Strategy Information Document carefully."],
        how=["Check eligibility and the ₹10 lakh threshold", "Compare available SIF strategies and their risk bands",
             "Explain redemption terms, costs and commission", "Complete the investment and track it with your mutual fund portfolio"],
        extra="SIFs carry higher risk than regular mutual funds, including derivative exposure.",
    ),
    "pms": dict(
        title="Portfolio Management Services (PMS)",
        eyebrow="Service · PMS",
        lede="Professionally managed, concentrated portfolios held in your own demat account, for investors with ₹50 lakh or more. Distributed by an APMI-Registered PMS Distributor (APRN10835).",
        minimum="₹50 lakh (SEBI minimum; in cash or securities)",
        who="HNIs and family offices comfortable with concentrated, higher-volatility portfolios",
        horizon="3 – 5+ years",
        liquidity="Moderate. Withdrawal is possible, subject to exit loads in the PMS agreement",
        overview=[
            "Portfolio Management Services are offered by SEBI-registered Portfolio Managers. Unlike a mutual fund, the securities are held directly in your own demat account, so you can see every stock and every transaction.",
            "PMS strategies are usually concentrated, often 15–30 stocks, and follow a defined investment approach such as growth, value, quality or small-cap. Fees may include a fixed management fee, a performance fee, or both, as set out in the PMS Disclosure Document.",
        ],
        types=[
            ("Discretionary", "The portfolio manager takes all investment decisions within the agreed strategy."),
            ("Non-Discretionary", "The portfolio manager suggests trades, which are executed only with your approval."),
            ("Advisory", "The manager only advises, and you execute the trades yourself."),
            ("Strategy Styles", "Large-cap, multi-cap, mid & small-cap, thematic, value and quality approaches."),
        ],
        modes=[
            ("Funding", "In cash, or by transferring existing stocks (subject to the manager's acceptance)."),
            ("Fees", "Fixed, performance-linked or hybrid, as disclosed upfront."),
            ("Reporting", "Regular statements, plus performance published on the APMI website."),
            ("Top-ups", "Additional investments as permitted by the agreement."),
        ],
        risks=["Concentrated portfolios can be more volatile than diversified funds.", "Fees and taxes on churn can affect net returns.",
               "Past performance of a strategy does not guarantee future results.", "Read the PMS Disclosure Document and agreement before investing."],
        how=["Confirm eligibility and suitability for a ₹50 lakh+ allocation", "Compare strategies, fees, track records (APMI data) and risk",
             "Explain the fee structure and our commission transparently", "Support onboarding and periodic review meetings with you"],
        extra="PMS is not a mutual fund product. It is offered by SEBI-registered portfolio managers and carries its own risks.",
    ),
    "aif": dict(
        title="Alternative Investment Funds (AIF)",
        eyebrow="Service · AIF",
        lede="Privately pooled funds investing in private equity, private credit, real estate, venture capital and hedge strategies, for investors with ₹1 crore or more.",
        minimum="₹1 crore (SEBI minimum for most investors)",
        who="HNIs, family offices and accredited investors with a long horizon and high risk appetite",
        horizon="Usually 3 – 10 years (closed-ended)",
        liquidity="Low. Most AIFs are closed-ended, with capital locked in for the fund's tenure",
        overview=[
            "Alternative Investment Funds are SEBI-registered, privately pooled investment vehicles. They give access to asset classes and strategies that aren't available through mutual funds, such as unlisted companies, structured private credit and long-short hedge strategies.",
            "AIFs are typically closed-ended, with capital drawn down over time as the manager deploys it, and returns distributed as investments are exited.",
        ],
        types=[
            ("Category I", "Venture capital, SME, social-impact and infrastructure funds."),
            ("Category II", "Private equity, private credit and real-estate funds. The largest category."),
            ("Category III", "Hedge-fund style strategies, including long-short and listed-equity funds that use leverage."),
        ],
        modes=[
            ("Commitment", "You commit capital, which is drawn down in tranches."),
            ("Distributions", "Paid out as underlying investments are exited."),
            ("Reporting", "Periodic NAV and portfolio reports from the manager."),
            ("Tenure", "Fixed fund life, sometimes with extensions."),
        ],
        risks=["Illiquidity: capital may be locked in for many years.", "Higher risk from unlisted, leveraged or concentrated exposures.",
               "Valuations are periodic and may be estimates.", "Read the Private Placement Memorandum (PPM) carefully."],
        how=["Assess suitability, liquidity needs and the ₹1 crore threshold", "Compare fund managers, strategy, track record and terms",
             "Walk you through the PPM, fees, drawdown schedule and commission", "Support documentation and track distributions"],
        extra="AIFs are not mutual fund products. They are illiquid, carry high risk and are suitable only for eligible investors.",
    ),
    "bonds-fds": dict(
        title="Bonds & Fixed Deposits",
        eyebrow="Service · Bonds & FDs",
        lede="Rated corporate fixed deposits and bonds for predictable income and the debt portion of your portfolio.",
        minimum="Corporate FDs from about ₹5,000 – ₹25,000; bonds from about ₹10,000 (varies by issue)",
        who="Conservative investors, retirees and anyone seeking regular interest income",
        horizon="12 months – 5+ years",
        liquidity="Varies. FDs allow premature withdrawal with a penalty, and listed bonds can be sold on the exchange subject to demand",
        overview=[
            "Corporate fixed deposits are offered by NBFCs and housing finance companies and are rated by credit-rating agencies such as CRISIL, ICRA and CARE. They often pay more than bank FDs, but they are not covered by DICGC deposit insurance.",
            "Bonds include corporate bonds, PSU bonds, government securities and tax-free bonds. Listed bonds are held in your demat account and pay interest (coupons) on a fixed schedule.",
        ],
        types=[
            ("Corporate FDs", "Fixed deposits from rated NBFCs and housing finance companies, with cumulative or payout options."),
            ("Corporate & PSU Bonds", "Rated, listed bonds held in demat form with fixed coupons."),
            ("Government Securities", "Central and state government bonds with sovereign backing."),
            ("Tax-Free Bonds", "Available in the secondary market from PSU issuers."),
        ],
        modes=[
            ("Interest Payout", "Monthly, quarterly, annual or cumulative options."),
            ("Laddering", "Spread maturities to balance liquidity and reinvestment risk."),
            ("Demat Holding", "Listed bonds held safely in your demat account."),
            ("Renewal", "Reminders before maturity to reinvest or redeem."),
        ],
        risks=["Credit risk: the issuer may delay or default. Check the rating.", "Interest-rate risk: bond prices fall when rates rise.",
               "Liquidity risk: some bonds trade thinly.", "Corporate FDs are not covered by DICGC insurance."],
        how=["Match tenure and payout options to your cash-flow needs", "Prefer highly rated issuers and diversify across them",
             "Explain ratings, risks and our commission transparently", "Track maturities and remind you before renewal"],
        extra="Bonds and fixed deposits are not mutual fund products and carry credit, interest-rate and liquidity risks.",
    ),
}


def service_page(slug):
    d = SVC[slug]
    cards = "".join(f'<article class="mini-card"><h3>{esc(t)}</h3><p>{p}</p></article>' for t, p in d["types"])
    modes = "".join(f'<article class="mode"><h4>{esc(t)}</h4><p>{p}</p></article>' for t, p in d["modes"])
    risks = "".join(f"<li>{r}</li>" for r in d["risks"])
    how = "".join(f"<li><span>{i+1:02d}</span>{h}</li>" for i, h in enumerate(d["how"]))
    ov = "".join(f'<p class="lede">{p}</p>' for p in d["overview"])
    others = "".join(f'<a class="other-link" href="/services/{s}/">{esc(n)} →</a>' for s, n in SERVICES if s != slug)
    main = f"""    <main>
{page_hero(d['eyebrow'], esc(d['title']), d['lede'], ['Services', esc(d['title'])])}
      <section class="section">
        <div class="wrap split split-top">
          <div>
            <p class="eyebrow">Overview</p>
            <h2>What is {esc(d['title'].split(' (')[0])}?</h2>
            {ov}
          </div>
          <aside class="facts-card">
            <h3>At a glance</h3>
            <dl>
              <dt>Minimum investment</dt><dd>{d['minimum']}</dd>
              <dt>Suitable for</dt><dd>{d['who']}</dd>
              <dt>Typical horizon</dt><dd>{d['horizon']}</dd>
              <dt>Liquidity</dt><dd>{d['liquidity']}</dd>
            </dl>
            <a class="btn btn-accent" href="/#contact">Enquire Now</a>
          </aside>
        </div>
      </section>

      <section class="section alt">
        <div class="wrap">
          <div class="section-head center">
            <p class="eyebrow">Options</p>
            <h2>Types &amp; strategies</h2>
          </div>
          <div class="mini-grid">{cards}</div>
        </div>
      </section>

      <section class="section">
        <div class="wrap">
          <div class="section-head center">
            <p class="eyebrow">How It Works</p>
            <h2>Ways to invest</h2>
          </div>
          <div class="mode-grid">{modes}</div>
        </div>
      </section>

      <section class="section process">
        <div class="wrap split split-top">
          <div>
            <p class="eyebrow eyebrow-light">Our Role</p>
            <h2>How we help</h2>
            <ol class="how-list">{how}</ol>
          </div>
          <div class="risk-card">
            <h3>Key risks to understand</h3>
            <ul>{risks}</ul>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="wrap">
          <div class="section-head center">
            <p class="eyebrow">Explore</p>
            <h2>Other services</h2>
          </div>
          <div class="other-grid">{others}</div>
        </div>
      </section>
{cta_band()}
{disclaimer(d['extra'])}
    </main>"""
    t = f"{d['title']} | {SITE} (ARN-373766)"
    write(f"services/{slug}/index.html", page(esc(t), esc(d["lede"]), main))


# ---------------------------------------------------------------- Calculator pages
CALC_INFO = {
    "sip": "Estimate what a fixed monthly SIP could grow to over time at an assumed rate of return.",
    "stepup": "See how raising your SIP every year (for example, with each increment) could change the outcome.",
    "lumpsum": "Estimate the future value of a one-time investment at an assumed rate of return.",
    "lumptarget": "Find the one-time amount you'd need to invest today to reach a target corpus.",
    "goal": "Work out the monthly SIP needed for any goal, such as a home, a car or a wedding, after adjusting for inflation.",
    "education": "Plan for your child's higher education by projecting future costs and the SIP needed to fund them.",
    "retire": "Estimate the corpus you'll need at retirement and the monthly SIP to build it.",
    "swp": "See how long a corpus could last with fixed monthly withdrawals at an assumed return.",
}


def calc_page(key):
    name = dict(CALCS)[key]
    others = "".join(f'<a class="other-link" href="/calculators/{CALC_SLUG[c]}/">{n} →</a>' for c, n in CALCS if c != key)
    main = f"""    <main>
      <section class="page-hero page-hero-sm">
        <div class="wrap">
          <p class="crumbs"><a href="/">Home</a> / Calculators / {name}</p>
          <h1>{name}</h1>
          <p class="hero-lede">{CALC_INFO[key]}</p>
        </div>
      </section>
      <section class="section calculators">
        <div class="wrap">
          <div class="calc-card">
            <form class="calc-form" id="calc-form" autocomplete="off"></form>
            <div class="calc-result" id="calc-result" aria-live="polite"></div>
          </div>
          <p class="disclaimer">Calculators are for illustration only. Assumed rates of return are not guaranteed and do not reflect any scheme's past or future performance.</p>
        </div>
      </section>
      <section class="section alt">
        <div class="wrap">
          <div class="section-head center"><p class="eyebrow">More Tools</p><h2>Other calculators</h2></div>
          <div class="other-grid">{others}</div>
        </div>
      </section>
{cta_band("Want a plan built around these numbers?")}
{disclaimer()}
    </main>"""
    write(f"calculators/{CALC_SLUG[key]}/index.html",
          page(f"{name} | {SITE}", CALC_INFO[key], main, f' data-calc="{key}"'))


# ---------------------------------------------------------------- About page
BIO_CARD = """<div class="founder-card founder-photo-card">
            <img class="founder-photo" src="/assets/pritesh-kakani.jpg" alt="Pritesh Kakani, founder of Kakani Wealth" width="768" height="1024" loading="lazy" />
            <h3>Pritesh Kakani</h3>
            <p class="founder-role">Founder · AMFI-Registered Mutual Fund Distributor</p>
            <ul class="founder-facts">
              <li><b>ARN</b><span>373766</span></li>
              <li><b>EUIN</b><span>E717134</span></li>
              <li><b>APRN (PMS)</b><span>APRN10835</span></li>
              <li><b>Education</b><span>B.Tech + M.Tech, IIT Kharagpur</span></li>
              <li><b>Certification</b><span>NISM Series V-A</span></li>
              <li><b>Market experience</b><span>9+ years, stocks &amp; commodities</span></li>
              <li><b>Base</b><span>Ahilyanagar, Maharashtra</span></li>
            </ul>
          </div>"""

BIO_TEXT = """<p class="lede">Pritesh Kakani is the founder of Kakani Wealth (registered business name: Kakani Financial Services) and an AMFI-Registered Mutual Fund Distributor (ARN-373766, EUIN E717134) and an APMI-Registered PMS Distributor (APRN10835). He holds a B.Tech and an M.Tech in Electronics from IIT Kharagpur (2014).</p>
            <p class="lede">Before moving into financial services, he spent a decade as a software engineer, rising to Senior Software Engineer at companies including UnitedHealth Group, Nutanix, Qolsys, Vedantu and e-Zest Solutions. Alongside his engineering career, he has spent 9+ years actively following and participating in Indian stock and commodity markets. That background shapes how he works: structured, data-driven and process-first.</p>
            <p class="lede">Today he helps resident and NRI families invest through mutual funds and other financial products, starting from their goals, their risk profile and their time horizon, with full transparency on costs and commissions. He is based in Ahilyanagar, Maharashtra, and works with clients across India and abroad.</p>"""


def about_page():
    main = f"""    <main>
      <section class="page-hero page-hero-sm">
        <div class="wrap">
          <p class="crumbs"><a href="/">Home</a> / About</p>
          <p class="eyebrow eyebrow-light">About Us</p>
          <h1>Meet the founder</h1>
          <p class="hero-lede">An IIT Kharagpur engineer bringing structure, data and transparency to family investing.</p>
        </div>
      </section>
      <section class="section about">
        <div class="wrap split split-top">
          {BIO_CARD}
          <div>
            <p class="eyebrow">Pritesh Kakani</p>
            <h2>Engineer by training. Distributor by choice.</h2>
            {BIO_TEXT}
            <div class="vm-grid">
              <div class="vm"><h4>Our Vision</h4><p>To be a trusted mutual fund distributor that makes a lasting, positive difference to the financial lives of the families we serve.</p></div>
              <div class="vm"><h4>Our Mission</h4><p>To give every investor a simple, transparent and disciplined investing experience, from the first SIP to retirement.</p></div>
            </div>
            <h3 class="sub-h">Our principles</h3>
            <ul class="checks">
              <li>Goals and risk profile first, product second</li>
              <li>Full disclosure of commissions, and of direct-plan alternatives</li>
              <li>No return guarantees, tips or hype</li>
              <li>Diversification across categories and fund houses</li>
              <li>Regular reviews and responsive service</li>
            </ul>
            <a class="btn btn-primary" href="/#contact" data-interest="Portfolio consultation">Book A Portfolio Consultation</a>
          </div>
        </div>
      </section>
{INTELLECT_INTEGRITY}
{cta_band("Let's start with a conversation.")}
{disclaimer()}
    </main>"""
    write("about/index.html", page(f"About Pritesh Kakani | {SITE}", "Pritesh Kakani — IIT Kharagpur engineer and AMFI-Registered Mutual Fund Distributor (ARN-373766).", main))


# ---------------------------------------------------------------- Home
def home():
    main = open(os.path.join(ROOT, "src/home-main.html")).read()
    # founder card with photo + short bio
    main = re.sub(r'<div class="founder-card">.*?</ul>\s*</div>', BIO_CARD, main, count=1, flags=re.S)
    main = re.sub(r'(<p class="eyebrow">About Us</p>\s*<h2>)How we work with every investor(</h2>)\s*<p class="lede">.*?</p>',
                  r'\1Meet Pritesh Kakani\2\n            ' + BIO_TEXT.split("\n")[0] + "\n            " + BIO_TEXT.split("\n")[1].strip(),
                  main, count=1, flags=re.S)
    main = main.replace('<a class="btn btn-primary" href="#contact">Book An Appointment</a>\n          </div>\n        </div>\n      </section>\n\n      <!-- Services -->',
                        '<a class="btn btn-primary" href="/about/">Read Full Profile</a>\n          </div>\n        </div>\n      </section>\n\n      <!-- Services -->', 1)
    main = main.replace("      <!-- Services -->", INTELLECT_INTEGRITY + "\n      <!-- Services -->", 1)
    # service cards -> links
    for s, n in SERVICES:
        main = main.replace(f"<h3>{esc(n)}</h3>", f'<h3><a href="/services/{s}/">{esc(n)}</a></h3>', 1)
    main = re.sub(r'(<article class="service">.*?<h3><a href="(/services/[^"]+)">.*?</p>)\s*</article>',
                  r'\1\n              <a class="text-link" href="\2">Read more →</a>\n            </article>', main, flags=re.S)
    # calculators: link to full pages
    main = main.replace('<p class="disclaimer">Calculators are for illustration only.',
                        '<div class="calc-links">' + "".join(f'<a href="/calculators/{CALC_SLUG[c]}/">{n}</a>' for c, n in CALCS) +
                        '</div>\n          <p class="disclaimer">Calculators are for illustration only.', 1)
    write("index.html", page(f"{SITE} | AMFI-Registered Mutual Fund Distributor (ARN-373766)",
                             "Kakani Wealth — Pritesh Kakani (Kakani Financial Services), AMFI-Registered Mutual Fund Distributor (ARN-373766, EUIN E717134), PMS Distributor (APRN10835), Ahilyanagar. Mutual funds, SIF, PMS, AIF, bonds and FDs for resident and NRI families.",
                             main))


# ---------------------------------------------------------------- Investment process page
def process_page():
    stages = [
        ("01", "Initial Meeting", "We discuss your goals, income, existing investments, time horizon and risk tolerance, complete a formal risk profile, and outline an initial strategy for each goal."),
        ("02", "Implementation", "Investments are matched to your risk profile and objectives. We share the suggested allocation and schemes with reasons, costs and commission, and execute only after your approval."),
        ("03", "Ongoing Support", "We monitor your portfolio continuously and review it formally every quarter against your objectives, suggesting rebalancing whenever it drifts or your life changes."),
    ]
    onboarding = [
        ("Document Submission", "Share basic documents: PAN, Aadhaar, a photograph and bank proof. NRIs also share a passport and overseas address proof."),
        ("KYC Validation", "Your documents are verified and KYC is completed with a KYC Registration Agency (KRA), plus the FATCA declaration where applicable."),
        ("Platform Onboarding", "You're registered on an exchange mutual fund transaction platform (NSE / BSE) so investments can be placed online."),
        ("Fund Selection", "Schemes are evaluated against your objectives, time horizon and risk profile. You approve the final shortlist."),
        ("SIP Setup", "Systematic Investment Plans are registered with an auto-debit mandate (e-NACH), so investing becomes automatic."),
        ("Lump Sum Setup", "One-time investments are executed directly, or through an STP if staggered entry suits you better."),
        ("Portfolio Access & Login", "You receive online access to your holdings, plus your Consolidated Account Statement (CAS) from CAMS / KFintech."),
        ("Track Anytime", "View your portfolio online whenever you like. We guide you through it, with quarterly reviews and ongoing monitoring in between."),
    ]
    principles = [
        ("Discipline over timing", "Consistent SIPs and staying invested matter more than predicting markets."),
        ("Goals first", "Every rupee is mapped to a goal, a horizon and a suitable risk level."),
        ("Transparency", "Clear reasoning, costs, commissions and direct-plan alternatives are always disclosed."),
        ("Your approval", "You approve every strategy and transaction, and you can track your portfolio anytime."),
        ("Diversification", "Spread across asset classes, fund houses and, where suitable, global markets."),
        ("Continuous review", "Ongoing monitoring with formal quarterly reviews."),
    ]
    st = "".join(f'<li class="stage"><span class="stage-no">{n}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for n, t, d in stages)
    ob = "".join(f'<li><span class="ob-no">{i+1}</span><h4>{t}</h4><p>{d}</p></li>' for i, (t, d) in enumerate(onboarding))
    pr = "".join(f'<article class="mini-card"><h3>{t}</h3><p>{d}</p></article>' for t, d in principles)
    main = f"""    <main>
{page_hero("Our Investment Process", "Disciplined investing,<br />step by step", "A structured, repeatable process, from the first meeting to onboarding, implementation and ongoing support, so you always know what we're doing and why.", ["Our Investment Process"])}
      <section class="section">
        <div class="wrap">
          <div class="section-head center">
            <p class="eyebrow">Process Overview</p>
            <h2>Three stages, one goal: your long-term wealth</h2>
          </div>
          <ol class="stages stages-3">{st}</ol>
        </div>
      </section>

      <section class="section alt">
        <div class="wrap">
          <div class="section-head center">
            <p class="eyebrow">Onboarding</p>
            <h2>Getting started is 100% paperless</h2>
            <p class="lede">Most investors are onboarded within a few working days, whether in India or abroad.</p>
          </div>
          <ol class="onboard-grid">{ob}</ol>
        </div>
      </section>

      <section class="section">
        <div class="wrap">
          <div class="section-head center">
            <p class="eyebrow">Our Principles</p>
            <h2>What guides every recommendation</h2>
          </div>
          <div class="mini-grid">{pr}</div>
          <blockquote class="pull-quote">Investing takes time. Consistency and discipline are what keep investors focused on their long-term goals.</blockquote>
        </div>
      </section>
{cta_band("Ready to get your portfolio reviewed?")}
{disclaimer()}
    </main>"""
    write("investment-process/index.html", page(f"Our Investment Process | {SITE}", "How Kakani Wealth works: an initial meeting, implementation and ongoing support, plus 8-step paperless onboarding.", main))


def not_found():
    main = """    <main>
      <section class="page-hero page-hero-sm"><div class="wrap"><h1>Page not found</h1>
      <p class="hero-lede">The page you're looking for doesn't exist.</p>
      <div class="hero-actions"><a class="btn btn-accent" href="/">Go To Home</a></div></div></section>
    </main>"""
    write("404.html", page(f"Page not found | {SITE}", "Page not found", main))


if __name__ == "__main__":
    home()
    about_page()
    process_page()
    for s, _ in SERVICES:
        service_page(s)
    for c, _ in CALCS:
        calc_page(c)
    not_found()
