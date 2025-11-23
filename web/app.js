const tips = [
  "黛利拉小姐，今夜的夜色很美，能允许我与你跳一支舞吗？",
  "我和小黛是意定之人，你只会拥有更多的爱。",
  "可是小黛，你怎么看着那么难过啊?重逢的时候，我们都应该是最好的样子。",
  "我可以藏在你的影子里，住在你的眼眸中，你接触世间万物时，我与你如影随形，你的喜怒哀乐，我都会感同身受。",
  "现在，月色有了，我最爱的女孩也在，可是，怎么办，小黛和你在一起的时候，我总是贪得无厌。",
  "传说在布雷诺春信来临之际，看到金色流星雨的人，将得到永不失去的爱情。所以，如果天空不给我们下一场流星雨，我便，自己下一场。",
  "你若活着，我是你的江声浩荡，若你离去，我是你的死水微澜。"
];

const bgColors = [
  "lightpink", "skyblue", "lightgreen", "lavender"
];

let batchNodes = [];
let batchStarted = false;

function randomTip() {
  return tips[Math.floor(Math.random() * tips.length)];
}

function randomBg() {
  return bgColors[Math.floor(Math.random() * bgColors.length)];
}

function showModal() {
  const modal = document.createElement("div");
  modal.className = "modal";
  modal.style.background = randomBg();

  const content = document.createElement("div");
  content.className = "content";
  content.textContent = randomTip();
  modal.appendChild(content);

  const actions = document.createElement("div");
  actions.className = "actions";
  const btn = document.createElement("button");
  btn.textContent = "我知道了";
  actions.appendChild(btn);
  modal.appendChild(actions);

  btn.addEventListener("click", () => {
    modal.remove();
    startBatch(200);
  });

  document.body.appendChild(modal);
}

function startBatch(count) {
  if (batchStarted) return;
  batchStarted = true;
  createOne(count);
}

function createOne(count) {
  if (count <= 0) return;
  const node = document.createElement("div");
  node.className = "tip";
  node.style.background = randomBg();
  const text = document.createElement("div");
  text.className = "text";
  text.textContent = randomTip();
  node.appendChild(text);

  const vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  const vh = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
  const x = Math.max(0, Math.floor(Math.random() * Math.max(1, vw - 260)));
  const y = Math.max(0, Math.floor(Math.random() * Math.max(1, vh - 160)));
  node.style.left = x + "px";
  node.style.top = y + "px";

  document.body.appendChild(node);
  batchNodes.push(node);

  setTimeout(() => createOne(count - 1), 80);
}

function exitAll() {
  batchNodes.forEach(n => n.remove());
  batchNodes = [];
  batchStarted = false;
}

function main() {
  const exitBtn = document.getElementById("exitBtn");
  exitBtn.addEventListener("click", exitAll);
  document.addEventListener("keydown", e => {
    if (e.code === "Space") {
      exitAll();
    }
  });
  showModal();
}

main();
