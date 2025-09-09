
 <p><br /></p><p>When running multiple Python scripts from a single runner, you often want to control how output is handled and whether one failure should stop the rest. This post shows how to:</p></header><section><ul>
        <li>Run multiple scripts via <code>subprocess.Popen</code></li>
        <li>Get real-time output </li>
        <li>Skip failed scripts and continue execution</li>
      </ul>
    <p></p>
    <hr>


<h2> 1. Buffered Mode (Default, No Real-Time Output)</h2>
<h3>version : 1 </h3>
    <ul>
      <li><code>subprocess.Popen</code> runs the scripts one by one</li>
      <li>Output is <strong>buffered</strong> — displayed only after script completes</li>
      <li>Standard output and errors are merged for visibility</li>
   </ul>


  <hr>
  <h2>2. Unbuffered Mode (Real-Time Output)</h2>
<h3>version : 2</h3>
    <ul>
      <li><code>-u</code> switch forces unbuffered output</li>
      <li>Use <code>flush=True</code> in child script <code>print()</code> for full real-time visibility</li>
      <li>Great for monitoring long-running scripts</li>
    </ul>
  <hr>


  <h2>3. Unbuffered Mode + Skip on Error</h2>
  <h3> version : 3 </h3>
    <ul>
      <li>Wraps execution in <code>try-except</code> to catch and log failures</li>
      <li>Continues to next script even if one fails</li>
      <li>Outputs ✅ or ❌ based on exit code</li>
    </ul>
