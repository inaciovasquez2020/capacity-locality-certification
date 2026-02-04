<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Executive Summary — CLC Standard</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;700&family=Libre+Baskerville:ital,wght@0,400;0,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    :root {
      --bg: #0b1220;
      --card: #0e1626;
      --text: #e5e7eb;
      --text-muted: #9aa5b1;
      --accent: #38bdf8;
      --accent-green: #10b981;
      --border: #1f2933;
    }

    * { box-sizing: border-box; }
    body { 
      background: var(--bg); 
      color: var(--text); 
      font-family: 'Inter', sans-serif; 
      margin: 0; 
      padding: 0;
      line-height: 1.8;
    }

    .container { max-width: 800px; margin: 0 auto; padding: 5rem 2rem; }

    /* Navigation */
    .nav-header {
      display: flex;
      justify-content: space-between;
      margin-bottom: 4rem;
    }
    .nav-link { 
      text-decoration: none; 
      color: var(--accent); 
      font-size: 11px; 
      font-weight: 700; 
      letter-spacing: 1.5px;
      text-transform: uppercase;
      display: flex; 
      align-items: center; 
      gap: 8px; 
    }

    /* Typography */
    h1 { 
      font-family: 'Libre Baskerville', serif; 
      font-size: 2.4rem; 
      color: #f8fafc;
      margin: 0 0 1rem 0;
      letter-spacing: -1px;
    }
    .protocol-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: var(--accent-green);
      background: rgba(16, 185, 129, 0.1);
      padding: 4px 12px;
      border-radius: 4px;
      border: 1px solid var(--accent-green);
      display: inline-block;
      margin-bottom: 2rem;
    }

    /* Content Sections */
    .summary-section { margin-bottom: 3.5rem; }
    .summary-section h2 { 
      font-size: 0.85rem; 
      text-transform: uppercase; 
      letter-spacing: 2px; 
      color: var(--accent); 
      border-bottom: 1px solid var(--border);
      padding-bottom: 10px;
      margin-bottom: 1.5rem;
    }

    .highlight-box {
      background: var(--card);
      border-left: 4px solid var(--accent);
      padding: 1.5rem 2rem;
      border-radius: 0 6px 6px 0;
      font-style: italic;
      font-family: 'Libre Baskerville', serif;
      margin: 2rem 0;
      font-size: 1.1rem;
      color: #cbd5e1;
    }

    .feature-list { list-style: none; padding: 0; }
    .feature-list li { 
      display: flex; 
      gap: 15px; 
      margin-bottom: 1rem; 
      padding: 1rem;
      background: rgba(255,255,255,0.02);
      border-radius: 6px;
      border: 1px solid var(--border);
    }
    .feature-list i { color: var(--accent-green); margin-top: 5px; }

    .grid-benefits {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
    }
    .benefit-item {
      padding: 1.5rem;
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 14px;
    }
    .benefit-item strong { color: var(--accent); display: block; margin-bottom: 5px; }

    footer {
      margin-top: 6rem;
      padding-top: 2rem;
      border-top: 1px solid var(--border);
      text-align: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--text-muted);
    }

    @media (max-width: 600px) {
      .grid-benefits { grid-template-columns: 1fr; }
      h1 { font-size: 1.8rem; }
    }
  </style>
</head>
<body>

  <div class="container">
    <nav class="nav-header">
      <a href="https://inaciovasquez2020.github.io/vasquez-index/" class="nav-link">
        <i class="fa-solid fa-chevron-left"></i> System Core
      </a>
      <a href="https://inaciovasquez2020.github.io/vasquez-index/dashboard.html" class="nav-link">
        Registry Audit <i class="fa-solid fa-shield-halved"></i>
      </a>
    </nav>

    <header>
      <span class="protocol-tag">STANDARD_DEFN // CLC_1.0.2</span>
      <h1>Executive Summary</h1>
      <p style="font-family: 'Libre Baskerville', serif; font-size: 1.2rem; color: var(--text-muted);">
        The Capacity–Locality Certification (CLC) protocol.
      </p>
    </header>

    <main>
      <section class="summary-section">
        <h2>The Problem</h2>
        <p>
          Modern AI systems often produce confident predictions even when the local environment does not contain 
          sufficient information to justify them. This <strong>epistemic overreach</strong> is the primary driver of 
          unpredictable failure in high-stakes autonomous systems.
        </p>
      </section>

      <div class="highlight-box">
        "CLC does not attempt to make predictions better. It certifies when a prediction is not allowed."
      </div>

      <section class="summary-section">
        <h2>Core Functionality</h2>
        <p>The CLC standard establishes a deterministic boundary for machine inference by defining:</p>
        <ul class="feature-list">
          <li>
            <i class="fa-solid fa-circle-check"></i>
            <div><strong>Predictive Permission:</strong> When the local signal-to-capacity ratio justifies a decision.</div>
          </li>
          <li>
            <i class="fa-solid fa-circle-xmark"></i>
            <div><strong>Mandatory Abstention:</strong> When the system must yield to human oversight or safety protocols.</div>
          </li>
          <li>
            <i class="fa-solid fa-stamp"></i>
            <div><strong>Decision Certification:</strong> An auditable cryptographic witness that the decision met the URF rigidity bounds.</div>
          </li>
        </ul>
      </section>

      <section class="summary-section">
        <h2>The Principle</h2>
        <p>
          Based on the <strong>Logic-Width Dependency</strong> established in the URF research program: 
          If a system only sees a limited part of the world (Locality) and has a finite processing threshold (Capacity), 
          then global predictions are structurally unreliable. CLC enforces the "Abstention Wall" whenever these 
          mathematical bounds are breached.
        </p>
      </section>

      <section class="summary-section">
        <h2>Strategic Outcomes</h2>
        <div class="grid-benefits">
          <div class="benefit-item">
            <strong>Safety</strong>
            Prevents autonomous hallucination in edge cases.
          </div>
          <div class="benefit-item">
            <strong>Auditability</strong>
            Provides a clear trace for post-incident review.
          </div>
          <div class="benefit-item">
            <strong>Regulatory</strong>
            Meets 2026 standards for deterministic AI compliance.
          </div>
          <div class="benefit-item">
            <strong>Liability</strong>
            Reduces corporate risk by identifying structural "unpredictables."
          </div>
        </div>
      </section>
    </main>

    <footer>
      VASQUEZ_RESEARCH // ORCID: 0009-0008-8459-3400 // STATUS: [RIGID]
    </footer>
  </div>

</body>
</html>
