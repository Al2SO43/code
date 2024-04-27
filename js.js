window.onload = function() {
    var modal = document.createElement('div');
    modal.classList.add('modal');
    modal.innerHTML = '<p>请在阅读<a href="./post/1.html" target="_blank">『README.md/README_EN.md---2024.4.27』</a>条目之后浏览本站内容,否则因各种原因发生的任何问题的后果将全部由您承担!</p>';
    document.body.appendChild(modal);
    modal.style.display = 'block';
    setTimeout(function() {
      modal.style.display = 'none';
    }, 5000); // 5秒后自动隐藏
  };