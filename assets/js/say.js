/* ============================================================
   say.js · tap-to-hear English pronunciation (Web Speech API)
   Used across the hub so students can hear how to say a place,
   word or sentence in English. Buttons: <button class="say"
   data-say="Chiayi">🔊</button>  — or any element with [data-say].
   ============================================================ */
(function () {
  var synth = window.speechSynthesis;
  if (!synth) return;

  var voice = null;
  function pickVoice() {
    var vs = synth.getVoices();
    // prefer a US/UK English voice
    voice = vs.find(function (v) { return /en[-_]US/i.test(v.lang); })
         || vs.find(function (v) { return /^en/i.test(v.lang); })
         || null;
  }
  pickVoice();
  if (synth.onvoiceschanged !== undefined) synth.onvoiceschanged = pickVoice;

  function say(text) {
    if (!text) return;
    try {
      synth.cancel();
      var u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US';
      u.rate = 0.95;
      if (voice) u.voice = voice;
      synth.speak(u);
    } catch (e) {}
  }
  window.say = say;

  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-say]');
    if (!b) return;
    e.preventDefault();
    say(b.getAttribute('data-say'));
    b.classList.add('saying');
    setTimeout(function () { b.classList.remove('saying'); }, 600);
  });
})();
