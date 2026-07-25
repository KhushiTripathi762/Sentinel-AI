function Stats() {
  return (
    <section className="stats">

      <h2>Sentinel AI in Numbers</h2>

      <div className="stats-container">

        <div className="stat-card">
          <h3>99%</h3>
          <p>Detection Accuracy</p>
        </div>

        <div className="stat-card">
          <h3>{"< 1 sec"}</h3>
          <p>Average Analysis Time</p>
        </div>

        <div className="stat-card">
          <h3>2</h3>
          <p>Security Modules</p>
        </div>

        <div className="stat-card">
          <h3>24/7</h3>
          <p>Threat Analysis</p>
        </div>

      </div>

    </section>
  );
}

export default Stats;