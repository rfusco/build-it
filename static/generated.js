const ball = document.getElementById('ball');
let x = 0;
let y = 0;
let dx = 2;
dy = 2;

function animate() {
  x += dx;
y += dy;

  if (x + 50 > window.innerWidth || x < 0) {
    dx = -dx;
  }
  if (y + 50 > window.innerHeight || y < 0) {
    dy = -dy;
  }

  ball.style.left = x + 'px';
  ball.style.top = y + 'px';
  requestAnimationFrame(animate);
}

ball.style.width = '50px';
ball.style.height = '50px';
ball.style.backgroundColor = 'red';
ball.style.position = 'absolute';

animate();